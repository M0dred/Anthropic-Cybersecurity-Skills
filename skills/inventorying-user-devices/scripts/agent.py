#!/usr/bin/env python3
"""Inventory runtime: enumerate assets or devices for an entity."""
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, timezone

CONFIG = {
 "skill": "inventorying-user-devices",
 "description": "inventorying user devices",
 "sources": [
  "mdm",
  "idp"
 ]
}


def run(cmd):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        return {"cmd": cmd, "returncode": p.returncode, "stdout": p.stdout[-3000:],
                "stderr": p.stderr[-800:]}
    except FileNotFoundError:
        return {"cmd": cmd, "returncode": 127, "error": f"not found: {cmd[0]}"}


def main(config=None):
    cfg = config or CONFIG
    ap = argparse.ArgumentParser(description=cfg.get("description", "inventory"))
    ap.add_argument("--identifier", required=True)
    ap.add_argument("--kind", default="user", choices=["user", "email", "host", "account"])
    ap.add_argument("--source", action="append",
                    default=cfg.get("sources") or ["mdm", "idp"])
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    results = {}
    for source in args.source:
        if source == "mdm":
            results["mdm"] = run(["az", "rest", "--method", "GET", "--url",
                                  "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices"
                                  f"?$filter=userPrincipalName eq '{args.identifier}'"])
        elif source == "idp":
            results["idp"] = run(["az", "ad", "user", "show", "--id", args.identifier,
                                  "--query", "{name:displayName,upn:userPrincipalName,enabled:accountEnabled}"])
        elif source == "edr":
            results["edr"] = {"query": f"hostname:'{args.identifier}'",
                              "note": "run against the EDR API"}
        elif source == "cloud":
            results["cloud"] = run(["aws", "iam", "list-user-policies", "--user-name", args.identifier])
        elif source == "cmdb":
            results["cmdb"] = {"query": f"cmdb_ci where assigned_to = '{args.identifier}'",
                               "note": "run against the CMDB API"}
        else:
            results[source] = {"error": "unknown source"}
    print(json.dumps({"skill": cfg.get("skill", ""), "identifier": args.identifier,
                      "kind": args.kind,
                      "collected_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                      "sources": results}, indent=1))


if __name__ == "__main__":
    main()
