#!/usr/bin/env python3
"""Block malicious IP addresses and verify the block.

Subcommands:
    validate   Reject non-routable, private, and malformed addresses.
    plan       Print the commands for a target without executing them.
    apply      Execute the commands (or dry-run with --dry-run).
    verify     Check that a block is present on the target.

Targets: iptables, nftables, pf, aws-nacl, azure-nsg, gcp-fw,
         cloudflare, panos.

Examples:
    python3 agent.py validate --ip 203.0.113.10 --ip 10.0.0.5
    python3 agent.py plan --target iptables --ip 203.0.113.10 --direction both
    python3 agent.py apply --target iptables --ip 203.0.113.10 --dry-run
    python3 agent.py verify --target iptables --ip 203.0.113.10
"""
from __future__ import annotations

import argparse
import ipaddress
import json
import os
import shlex
import subprocess
import sys
import urllib.request

PRIVATE_NETS = [
    ipaddress.ip_network(n)
    for n in ("10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16",
              "127.0.0.0/8", "169.254.0.0/16", "::1/128", "fc00::/7", "fe80::/10")
]


def parse_ips(values):
    """Return (valid, rejected) lists. Rejected entries carry a reason."""
    valid, rejected = [], []
    for raw in values:
        try:
            net = ipaddress.ip_network(raw, strict=False)
        except ValueError as exc:
            rejected.append({"value": raw, "reason": f"invalid address: {exc}"})
            continue
        if net.is_multicast:
            rejected.append({"value": raw, "reason": "multicast"})
            continue
        if net.is_unspecified:
            rejected.append({"value": raw, "reason": "unspecified address"})
            continue
        if any(net.subnet_of(p) for p in PRIVATE_NETS if p.version == net.version):
            rejected.append({"value": raw, "reason": "private or loopback range"})
            continue
        valid.append(str(net))
    return valid, rejected


def cidr(value):
    return value if "/" in value else f"{value}/32"


def build_commands(target, ips, direction, opts):
    """Return a list of command dicts: {purpose, argv, rollback}."""
    cmds = []
    for ip in ips:
        if target == "iptables":
            if direction in ("inbound", "both"):
                cmds.append({"purpose": f"drop inbound from {ip}",
                             "argv": ["iptables", "-I", "INPUT", "1", "-s", ip, "-j", "DROP"],
                             "rollback": ["iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"]})
            if direction in ("outbound", "both"):
                cmds.append({"purpose": f"drop outbound to {ip}",
                             "argv": ["iptables", "-I", "OUTPUT", "1", "-d", ip, "-j", "DROP"],
                             "rollback": ["iptables", "-D", "OUTPUT", "-d", ip, "-j", "DROP"]})
        elif target == "nftables":
            if direction in ("inbound", "both"):
                cmds.append({"purpose": f"drop inbound from {ip}",
                             "argv": ["nft", "add", "rule", "inet", "filter", "input",
                                      "ip", "saddr", ip, "drop"],
                             "rollback": ["nft", "-a", "list", "chain", "inet", "filter", "input"]})
            if direction in ("outbound", "both"):
                cmds.append({"purpose": f"drop outbound to {ip}",
                             "argv": ["nft", "add", "rule", "inet", "filter", "output",
                                      "ip", "daddr", ip, "drop"],
                             "rollback": ["nft", "-a", "list", "chain", "inet", "filter", "output"]})
        elif target == "pf":
            cmds.append({"purpose": f"pf anchor block {ip}",
                         "argv": ["pfctl", "-a", "blocklist", "-f", "/etc/pf.anchors/blocklist"],
                         "rollback": ["pfctl", "-a", "blocklist", "-F", "rules"]})
        elif target == "aws-nacl":
            acl = opts.get("acl_id")
            if not acl:
                raise SystemExit("--acl-id is required for aws-nacl")
            rule = opts.get("rule_number", 90)
            cmds.append({"purpose": f"deny {cidr(ip)} in NACL {acl}",
                         "argv": ["aws", "ec2", "create-network-acl-entry",
                                  "--network-acl-id", acl, "--rule-number", str(rule),
                                  "--protocol", "-1", "--cidr-block", cidr(ip),
                                  "--rule-action", "deny", "--egress"],
                         "rollback": ["aws", "ec2", "delete-network-acl-entry",
                                      "--network-acl-id", acl, "--rule-number", str(rule),
                                      "--egress"]})
        elif target == "azure-nsg":
            rg, nsg = opts.get("resource_group"), opts.get("nsg_name")
            if not (rg and nsg):
                raise SystemExit("--resource-group and --nsg-name are required for azure-nsg")
            name = "deny-" + ip.replace(".", "-").replace(":", "-").replace("/", "-")
            cmds.append({"purpose": f"deny {cidr(ip)} in NSG {nsg}",
                         "argv": ["az", "network", "nsg", "rule", "create",
                                  "-g", rg, "-n", name, "--nsg-name", nsg,
                                  "--priority", str(opts.get("priority", 100)),
                                  "--direction", "Inbound", "--access", "Deny",
                                  "--protocol", "*", "--source-address-prefixes", cidr(ip),
                                  "--source-port-ranges", "*", "--destination-address-prefixes", "*",
                                  "--destination-port-ranges", "*"],
                         "rollback": ["az", "network", "nsg", "rule", "delete",
                                      "-g", rg, "--nsg-name", nsg, "-n", name]})
        elif target == "gcp-fw":
            name = "deny-" + ip.replace(".", "-").replace(":", "-").replace("/", "-")
            cmds.append({"purpose": f"deny {cidr(ip)} in VPC firewall",
                         "argv": ["gcloud", "compute", "firewall-rules", "create", name,
                                  "--action", "DENY", "--direction", "INGRESS",
                                  "--rules", "all", "--source-ranges", cidr(ip),
                                  "--priority", str(opts.get("priority", 100))],
                         "rollback": ["gcloud", "compute", "firewall-rules", "delete", name]})
        elif target == "cloudflare":
            cmds.append({"purpose": f"cloudflare access rule block {ip}",
                         "api": {"method": "POST",
                                 "url": "https://api.cloudflare.com/client/v4/accounts/"
                                        f"{opts.get('cf_account', '')}/firewall/access_rules/rules",
                                 "body": {"mode": "block",
                                          "configuration": {"target": "ip", "value": ip},
                                          "notes": opts.get("note", "blocked by agent")}},
                         "rollback": "DELETE the returned rule id"})
        elif target == "panos":
            cmds.append({"purpose": f"add {ip} to PAN-OS EDL",
                         "argv": ["echo", ip, ">>", opts.get("edl_path", "/var/www/blocklist.txt")],
                         "rollback": ["sed", "-i", f"/^{ip}$/d", opts.get("edl_path", "/var/www/blocklist.txt")]})
        else:
            raise SystemExit(f"unknown target: {target}")
    return cmds


def run(argv, dry_run):
    if dry_run:
        return {"argv": argv, "returncode": 0, "dry_run": True, "stdout": ""}
    try:
        proc = subprocess.run(argv, capture_output=True, text=True, timeout=120)
        return {"argv": argv, "returncode": proc.returncode,
                "stdout": proc.stdout[-2000:], "stderr": proc.stderr[-2000:]}
    except FileNotFoundError:
        return {"argv": argv, "returncode": 127, "error": f"command not found: {argv[0]}"}
    except subprocess.TimeoutExpired:
        return {"argv": argv, "returncode": 124, "error": "timeout"}


def call_api(spec):
    req = urllib.request.Request(
        spec["url"], method=spec["method"],
        data=json.dumps(spec["body"]).encode(),
        headers={"Authorization": f"Bearer {os.environ.get('CF_TOKEN', '')}",
                 "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return {"status": resp.status, "body": resp.read().decode()[:1000]}
    except Exception as exc:  # noqa: BLE001 - surfaced to the operator
        return {"error": str(exc)}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", choices=["validate", "plan", "apply", "verify"])
    ap.add_argument("--ip", action="append", default=[], help="IP or CIDR (repeatable)")
    ap.add_argument("--target", default="iptables",
                    choices=["iptables", "nftables", "pf", "aws-nacl", "azure-nsg",
                             "gcp-fw", "cloudflare", "panos"])
    ap.add_argument("--direction", default="both", choices=["inbound", "outbound", "both"])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--acl-id")
    ap.add_argument("--rule-number", type=int, default=90)
    ap.add_argument("--resource-group")
    ap.add_argument("--nsg-name")
    ap.add_argument("--priority", type=int, default=100)
    ap.add_argument("--cf-account", default=os.environ.get("CF_ACCOUNT", ""))
    ap.add_argument("--edl-path")
    ap.add_argument("--note", default="blocked by agent")
    args = ap.parse_args()

    if not args.ip:
        raise SystemExit("--ip is required")

    valid, rejected = parse_ips(args.ip)
    report = {"action": args.action, "target": args.target,
              "valid": valid, "rejected": rejected}

    if args.action == "validate":
        report["ok"] = bool(valid) and not rejected
    else:
        if rejected:
            report["warning"] = "some addresses were rejected and will not be blocked"
        opts = vars(args)
        cmds = build_commands(args.target, valid, args.direction, opts)
        if args.action == "plan":
            report["commands"] = [c.get("argv") or c.get("api") for c in cmds]
        elif args.action == "apply":
            results = []
            for c in cmds:
                if "api" in c:
                    results.append({"purpose": c["purpose"],
                                    "result": {"dry_run": True} if args.dry_run
                                    else call_api(c["api"])})
                else:
                    results.append({"purpose": c["purpose"],
                                    "result": run(c["argv"], args.dry_run)})
            report["results"] = results
            report["ok"] = all(r["result"].get("returncode", 0) == 0 or
                               r["result"].get("status", 200) < 400 for r in results)
        elif args.action == "verify":
            check = {"iptables": ["iptables", "-L", "-n"],
                     "nftables": ["nft", "list", "ruleset"],
                     "pf": ["pfctl", "-sr"],
                     "aws-nacl": ["aws", "ec2", "describe-network-acls",
                                  "--network-acl-ids", args.acl_id or ""],
                     "azure-nsg": ["az", "network", "nsg", "rule", "list",
                                   "-g", args.resource_group or "", "--nsg-name", args.nsg_name or ""],
                     "gcp-fw": ["gcloud", "compute", "firewall-rules", "list"],
                     "cloudflare": ["true"], "panos": ["cat", args.edl_path or "/dev/null"]}
            out = run(check[args.target], args.dry_run)
            found = [ip for ip in valid if ip in (out.get("stdout") or "")]
            report["present"] = found
            report["missing"] = [ip for ip in valid if ip not in found]
            report["ok"] = not report["missing"]

    print(json.dumps(report, indent=1) if args.json else
          json.dumps(report, indent=1))
    sys.exit(0 if report.get("ok", True) else 1)


if __name__ == "__main__":
    main()
