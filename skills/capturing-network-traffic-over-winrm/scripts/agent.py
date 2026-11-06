#!/usr/bin/env python3
"""Acquisition runtime: collect forensic artifacts and hash them."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from datetime import datetime, timezone

CONFIG = {
 "skill": "capturing-network-traffic-over-winrm",
 "description": "capturing network traffic over winrm",
 "artifacts": [
  "network"
 ]
}
LOCAL = {
    "process": "ps auxf > {out}/processes.txt",
    "network": "ss -tunap > {out}/sockets.txt",
    "memory": "sudo dd if=/proc/kcore of={out}/memory.raw bs=1M",
    "logs": "sudo tar czf {out}/var-log.tar.gz /var/log",
    "etc": "sudo tar czf {out}/etc.tar.gz /etc",
}
WINRM = {
    "process": "Get-Process | Export-Csv {out}\\processes.csv -NoTypeInformation",
    "network": "Get-NetTCPConnection | Export-Csv {out}\\sockets.csv -NoTypeInformation",
    "registry": "reg export HKLM\\SYSTEM {out}\\SYSTEM.reg /y",
    "mft": "fsutil usn readjournal C: csv > {out}\\usn.csv",
    "logs": "wevtutil epl Security {out}\\Security.evtx",
}


def run(cmd, dry):
    if dry:
        return {"cmd": cmd, "dry_run": True, "returncode": 0}
    p = subprocess.run(cmd, shell=isinstance(cmd, str), capture_output=True, text=True, timeout=300)
    return {"cmd": cmd, "returncode": p.returncode, "stdout": p.stdout[-1000:],
            "stderr": p.stderr[-1000:]}


def hash_dir(path):
    rows = []
    for root, _dirs, files in os.walk(path):
        for name in files:
            full = os.path.join(root, name)
            with open(full, "rb") as fh:
                rows.append({"file": full, "size": os.path.getsize(full),
                             "sha256": hashlib.sha256(fh.read()).hexdigest()})
    return rows


def main(config=None):
    cfg = config or CONFIG
    ap = argparse.ArgumentParser(description=cfg.get("description", "acquisition"))
    ap.add_argument("--transport", default=cfg.get("transport", "local"), choices=["local", "winrm", "ssh"])
    ap.add_argument("--artifact", action="append",
                    default=cfg.get("artifacts") or ["process", "network"])
    ap.add_argument("--host", default="localhost")
    ap.add_argument("--out", default="./evidence")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    table = WINRM if args.transport == "winrm" else LOCAL
    results = []
    for artifact in args.artifact:
        template = table.get(artifact)
        if not template:
            results.append({"artifact": artifact, "error": "no collector mapped"})
            continue
        cmd = template.format(out=args.out)
        results.append({"artifact": artifact, "result": run(cmd, args.dry_run)})
    manifest = [] if args.dry_run else hash_dir(args.out)
    print(json.dumps({"skill": cfg.get("skill", ""), "host": args.host,
                      "transport": args.transport,
                      "collected_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                      "results": results, "manifest": manifest}, indent=1))


if __name__ == "__main__":
    main()
