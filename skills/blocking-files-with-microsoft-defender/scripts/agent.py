#!/usr/bin/env python3
"""Containment runtime: block, isolate, disable, terminate, delete, quarantine.

The generated skill supplies CONFIG with the platforms it supports. Every action
supports --dry-run, prints the exact request, and returns JSON.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

CONFIG = {
 "skill": "blocking-files-with-microsoft-defender",
 "description": "blocking files with microsoft defender",
 "targets": [
  "defender",
  "crowdstrike"
 ],
 "action": "block"
}


def run(argv, dry):
    if dry:
        return {"argv": argv, "dry_run": True, "returncode": 0}
    try:
        p = subprocess.run(argv, capture_output=True, text=True, timeout=120)
        return {"argv": argv, "returncode": p.returncode,
                "stdout": p.stdout[-1500:], "stderr": p.stderr[-1500:]}
    except FileNotFoundError:
        return {"argv": argv, "returncode": 127, "error": f"not found: {argv[0]}"}


def api(method, url, token, body=None, header="Authorization", prefix="Bearer "):
    req = urllib.request.Request(url, method=method,
                                 data=json.dumps(body).encode() if body is not None else None)
    req.add_header(header, f"{prefix}{token}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            return {"status": r.status, "body": r.read().decode()[:800]}
    except urllib.error.HTTPError as e:
        return {"status": e.code, "error": e.read().decode()[:400]}
    except Exception as e:  # noqa: BLE001
        return {"error": str(e)}


def env(name, default=""):
    return os.environ.get(name, default)


def build(action, target, value, opts):
    v = value
    host = opts.get("host") or v
    if target == "iptables":
        return [["iptables", "-I", "INPUT", "1", "-s", v, "-j", "DROP"]]
    if target == "nftables":
        return [["nft", "add", "rule", "inet", "filter", "input", "ip", "saddr", v, "drop"]]
    if target == "aws":
        return [["aws", "ec2", "revoke-security-group-ingress", "--group-id",
                 opts.get("group") or "sg-0123456789abcdef0", "--ip-permissions",
                 f"IpProtocol=-1,IpRanges=[{{CidrIp={v}/32}}]"]]
    if target == "azure":
        return [["az", "network", "nsg", "rule", "create", "-g", opts.get("rg") or "rg-prod",
                 "-n", "deny-" + v.replace(".", "-"), "--nsg-name", opts.get("nsg") or "nsg-web",
                 "--priority", "100", "--direction", "Inbound", "--access", "Deny",
                 "--protocol", "*", "--source-address-prefixes", f"{v}/32",
                 "--source-port-ranges", "*", "--destination-address-prefixes", "*",
                 "--destination-port-ranges", "*"]]
    if target == "gcp":
        return [["gcloud", "compute", "firewall-rules", "create", "deny-" + v.replace(".", "-"),
                 "--action", "DENY", "--direction", "INGRESS", "--rules", "all",
                 "--source-ranges", f"{v}/32", "--priority", "100"]]
    if target == "pan-os":
        return [["sh", "-c", f"echo {v} >> /var/www/blocklist.txt"]]
    if target == "cloudflare":
        return [["sh", "-c", f"curl -sS -X POST https://api.cloudflare.com/client/v4/accounts/$CF_ACCOUNT/firewall/access_rules/rules -H 'Authorization: Bearer $CF_TOKEN' -H 'Content-Type: application/json' --data '{{\"mode\":\"block\",\"configuration\":{{\"target\":\"ip\",\"value\":\"{v}\"}}}}'"]]
    if target == "kubernetes":
        return [["kubectl", "delete", "pod", v, "-n", opts.get("namespace") or "default",
                 "--grace-period=0"]]
    if target == "crowdstrike":
        return [["sh", "-c", f"curl -sS -X POST 'https://api.crowdstrike.com/devices/entities/devices-actions/v2?action_name={'contain' if action == 'isolate' else 'lift_containment'}' -H 'Authorization: Bearer $CS_TOKEN' -H 'Content-Type: application/json' -d '{{\"ids\":[\"{v}\"]}}'"]]
    if target == "defender":
        verb = "isolate" if action == "isolate" else "unisolate"
        return [["sh", "-c", f"curl -sS -X POST 'https://api.securitycenter.microsoft.com/api/machines/{v}/{verb}' -H 'Authorization: Bearer $MDE_TOKEN' -H 'Content-Type: application/json' -d '{{\"Comment\":\"containment\",\"IsolationType\":\"Full\"}}'"]]
    if target == "sentinelone":
        verb = "isolate" if action == "isolate" else "unisolate"
        return [["sh", "-c", f"curl -sS -X POST '$S1_BASE_URL/web/api/v2.1/agents/actions/{verb}' -H 'Authorization: ApiToken $S1_TOKEN' -H 'Content-Type: application/json' -d '{{\"filter\":{{\"ids\":[\"{v}\"]}}}}'"]]
    if target == "cybereason":
        return [["sh", "-c", f"curl -sS -X POST 'https://$CYBER_BASE/rest/visualsearch/query/simple' -H 'Content-Type: application/json' -d '{{\"queryPath\":[{{\"requestedType\":\"Machine\",\"filters\":[{{\"filters\":[{{\"fieldName\":\"name\",\"values\":[\"{v}\"]}}]}}]}}]}}'"]]
    if target == "fireeye":
        return [["sh", "-c", f"curl -sS -X POST 'https://$HX_BASE/hx/api/v3/hosts/{v}/containment' -H 'Authorization: Bearer $HX_TOKEN' -H 'Content-Type: application/json' -d '{{\"action\":\"{'contain' if action == 'isolate' else 'uncontain'}\"}}'"]]
    if target == "cortex-xdr":
        verb = "isolate" if action == "isolate" else "unisolate"
        return [["sh", "-c", f"curl -sS -X POST '$XDR_BASE/public_api/v1/endpoints/{verb}' -H 'Authorization: $XDR_TOKEN' -H 'Content-Type: application/json' -d '{{\"request_data\":{{\"endpoint_id\":\"{v}\"}}}}'"]]
    if target == "okta":
        return [["sh", "-c", f"curl -sS -X POST 'https://$OKTA_ORG.okta.com/api/v1/users/{v}/lifecycle/suspend' -H 'Authorization: SSWS $OKTA_TOKEN'"]]
    if target == "entra":
        return [["az", "ad", "user", "update", "--id", v, "--account-enabled", "false"]]
    if target == "ad":
        return [["powershell", "-Command", f"Disable-ADAccount -Identity '{v}'"]]
    if target == "m365":
        return [["powershell", "-Command", f"New-ComplianceSearch -Name 'INC-1234' -ExchangeLocation all -ContentMatchQuery 'from:{v}'; Start-ComplianceSearch -Identity 'INC-1234'"]]
    return None


def main(config=None):
    cfg = config or CONFIG
    ap = argparse.ArgumentParser(description=cfg.get("description", "containment"))
    ap.add_argument("--action", default=cfg.get("action", "block"),
                    choices=["block", "isolate", "unisolate", "disable", "terminate",
                             "delete", "quarantine"])
    ap.add_argument("--target", default=(cfg.get("targets") or ["iptables"])[0],
                    choices=cfg.get("targets") or ["iptables"])
    ap.add_argument("--value", required=True)
    ap.add_argument("--host")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--group")
    ap.add_argument("--rg")
    ap.add_argument("--nsg")
    ap.add_argument("--namespace")
    args = ap.parse_args()
    cmds = build(args.action, args.target, args.value, vars(args)) or []
    results = [run(c, args.dry_run) for c in cmds]
    out = {"skill": cfg.get("skill", ""), "action": args.action, "target": args.target,
           "value": args.value, "results": results,
           "ok": all(r.get("returncode", 0) == 0 for r in results)}
    print(json.dumps(out, indent=1))
    sys.exit(0 if out["ok"] else 1)


if __name__ == "__main__":
    main()
