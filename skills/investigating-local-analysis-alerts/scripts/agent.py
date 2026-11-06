#!/usr/bin/env python3
"""Investigation runtime: collect entity context and build an event timeline."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
from datetime import datetime, timezone

CONFIG = {
 "skill": "investigating-local-analysis-alerts",
 "description": "investigating local analysis alerts"
}


def ad_user(user):
    cmd = ["powershell", "-Command",
           f"Get-ADUser -Identity '{user}' -Properties LastLogonDate,MemberOf,Enabled | "
           "Select-Object Name,Enabled,LastLogonDate,MemberOf | ConvertTo-Json"]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return {"cmd": cmd, "returncode": p.returncode, "stdout": p.stdout[-2000:],
                "stderr": p.stderr[-500:]}
    except FileNotFoundError:
        return {"cmd": cmd, "returncode": 127, "error": f"not found: {cmd[0]}"}
    except subprocess.TimeoutExpired:
        return {"cmd": cmd, "returncode": 124, "error": "timeout"}


def entra_user(user):
    cmd = ["az", "ad", "user", "show", "--id", user, "--query",
           "{name:displayName,upn:userPrincipalName,enabled:accountEnabled,last:signInActivity}"]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return {"cmd": cmd, "returncode": p.returncode, "stdout": p.stdout[-2000:],
                "stderr": p.stderr[-500:]}
    except FileNotFoundError:
        return {"cmd": cmd, "returncode": 127, "error": f"not found: {cmd[0]}"}
    except subprocess.TimeoutExpired:
        return {"cmd": cmd, "returncode": 124, "error": "timeout"}


def edr_host(host):
    return {"host": host, "queries": [
        f"hostname:'{host}'", f"device.name:\"{host}\"", f"ComputerName == \"{host}\""],
        "note": "run against the EDR console or API"}


def timeline(events):
    rows = []
    for event in events:
        ts = event.get("timestamp") or event.get("time") or ""
        rows.append({"timestamp": ts, "source": event.get("source", ""),
                     "event": event.get("event", ""), "entity": event.get("entity", ""),
                     "detail": event.get("detail", "")})
    rows.sort(key=lambda r: r["timestamp"])
    return rows


def main(config=None):
    cfg = config or CONFIG
    ap = argparse.ArgumentParser(description=cfg.get("description", "investigation"))
    ap.add_argument("--entity", required=True)
    ap.add_argument("--kind", default=cfg.get("kind", "user"),
                    choices=["user", "host", "ip", "account"])
    ap.add_argument("--events", help="JSON file with timestamped events")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    record = {"skill": cfg.get("skill", ""), "entity": args.entity, "kind": args.kind,
              "collected_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}
    if args.kind == "user":
        record["ad"] = ad_user(args.entity)
        record["entra"] = entra_user(args.entity)
    elif args.kind == "host":
        record["edr"] = edr_host(args.entity)
    if args.events and os.path.exists(args.events):
        record["timeline"] = timeline(json.load(open(args.events)))
    print(json.dumps(record, indent=1))


if __name__ == "__main__":
    main()
