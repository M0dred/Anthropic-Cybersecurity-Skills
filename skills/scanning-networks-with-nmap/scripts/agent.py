#!/usr/bin/env python3
"""Remediation runtime: plan, apply, and verify a configuration fix."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys

CONFIG = {
 "skill": "scanning-networks-with-nmap",
 "description": "scanning networks with nmap",
 "platforms": [
  "aws"
 ],
 "issues": [
  "cloudtrail"
 ]
}
FIXES = {
    ("aws", "cloudtrail"): [
        ["aws", "cloudtrail", "update-trail", "--name", "management-trail",
         "--is-multi-region-trail", "--enable-log-file-validation"]],
    ("aws", "ec2"): [
        ["aws", "ec2", "modify-instance-attribute", "--instance-id", "i-0123456789abcdef0",
         "--no-source-dest-check"]],
    ("aws", "iam"): [
        ["aws", "iam", "update-account-password-policy", "--minimum-password-length", "14",
         "--require-symbols", "--require-numbers", "--require-uppercase-characters",
         "--require-lowercase-characters", "--password-reuse-prevention", "24"]],
    ("azure", "aks"): [
        ["az", "aks", "update", "-g", "rg-prod", "-n", "aks-prod", "--enable-managed-identity",
         "--enable-azure-rbac"]],
    ("azure", "storage"): [
        ["az", "storage", "account", "update", "-g", "rg-prod", "-n", "mystorage",
         "--https-only", "true", "--min-tls-version", "TLS1_2",
         "--allow-blob-public-access", "false"]],
    ("gcp", "vpc"): [
        ["gcloud", "compute", "firewall-rules", "update", "allow-ssh",
         "--source-ranges", "10.0.0.0/8"]],
    ("kubernetes", "compliance"): [
        ["kubectl", "label", "namespace", "default", "pod-security.kubernetes.io/enforce=restricted"]],
    ("okta", "account"): [
        ["sh", "-c", "curl -sS -X POST https://$OKTA_ORG.okta.com/api/v1/users/$USER_ID/lifecycle/suspend -H 'Authorization: SSWS $OKTA_TOKEN'"]],
    ("ad", "account"): [
        ["powershell", "-Command", "Disable-ADAccount -Identity jdoe"]],
}
VERIFY = {
    "aws": ["aws", "cloudtrail", "describe-trails"],
    "azure": ["az", "storage", "account", "show", "-g", "rg-prod", "-n", "mystorage"],
    "gcp": ["gcloud", "compute", "firewall-rules", "list"],
    "kubernetes": ["kubectl", "get", "ns", "--show-labels"],
    "okta": ["sh", "-c", "curl -sS https://$OKTA_ORG.okta.com/api/v1/users/$USER_ID -H 'Authorization: SSWS $OKTA_TOKEN'"],
    "ad": ["powershell", "-Command", "Get-ADUser -Identity jdoe | Select-Object Enabled"],
}


def run(cmd, dry):
    if dry:
        return {"argv": cmd, "dry_run": True, "returncode": 0}
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
        return {"argv": cmd, "returncode": p.returncode, "stdout": p.stdout[-1500:],
                "stderr": p.stderr[-1000:]}
    except FileNotFoundError:
        return {"argv": cmd, "returncode": 127, "error": f"not found: {cmd[0]}"}


def main(config=None):
    cfg = config or CONFIG
    ap = argparse.ArgumentParser(description=cfg.get("description", "remediation"))
    ap.add_argument("--platform", default=(cfg.get("platforms") or ["aws"])[0],
                    choices=cfg.get("platforms") or ["aws"])
    ap.add_argument("--issue", default=(cfg.get("issues") or ["cloudtrail"])[0],
                    choices=cfg.get("issues") or ["cloudtrail"])
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    cmds = FIXES.get((args.platform, args.issue), [])
    if not cmds:
        print(json.dumps({"error": "no fix mapped", "platform": args.platform,
                          "issue": args.issue}, indent=1))
        sys.exit(2)
    results = [run(c, not args.apply) for c in cmds]
    verify = run(VERIFY.get(args.platform, ["true"]), not args.apply)
    out = {"skill": cfg.get("skill", ""), "platform": args.platform, "issue": args.issue,
           "applied": args.apply, "results": results, "verify": verify,
           "ok": all(r.get("returncode", 0) == 0 for r in results)}
    print(json.dumps(out, indent=1))
    sys.exit(0 if out["ok"] else 1)


if __name__ == "__main__":
    main()
