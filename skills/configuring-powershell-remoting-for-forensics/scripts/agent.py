#!/usr/bin/env python3
"""Configure, test, collect, and clean up PowerShell Remoting for DFIR.

Subcommands:
    configure  Print or run the WinRM setup commands for the target hosts.
    test       Test WSMan connectivity to each host.
    collect    Run a collection script on each host and copy artifacts back.
    cleanup    Remove the temporary listener, trusted hosts, and sessions.

Examples:
    python3 agent.py configure --hosts web-01,web-02 --transport https --dry-run
    python3 agent.py test --hosts web-01,web-02
    python3 agent.py collect --hosts web-01 --artifacts process,network,logs --out ./evidence
    python3 agent.py cleanup --hosts web-01,web-02 --dry-run
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys

ARTIFACTS = {
    "process": "Get-Process | Export-Csv C:\\Windows\\Temp\\processes.csv -NoTypeInformation",
    "network": "Get-NetTCPConnection | Export-Csv C:\\Windows\\Temp\\sockets.csv -NoTypeInformation",
    "loggedon": "Get-CimInstance Win32_LogonSession | Export-Csv C:\\Windows\\Temp\\logons.csv -NoTypeInformation",
    "logs": "wevtutil epl Security C:\\Windows\\Temp\\Security.evtx",
    "system": "wevtutil epl System C:\\Windows\\Temp\\System.evtx",
    "registry": "reg export HKLM\\SYSTEM C:\\Windows\\Temp\\SYSTEM.reg /y",
    "mft": "fsutil usn readjournal C: csv > C:\\Windows\\Temp\\usn.csv",
}


def run(argv, dry):
    if dry:
        return {"argv": argv, "dry_run": True, "returncode": 0}
    try:
        proc = subprocess.run(argv, capture_output=True, text=True, timeout=600)
        return {"argv": argv, "returncode": proc.returncode,
                "stdout": proc.stdout[-1500:], "stderr": proc.stderr[-1500:]}
    except FileNotFoundError:
        return {"argv": argv, "returncode": 127, "error": f"not found: {argv[0]}"}
    except subprocess.TimeoutExpired:
        return {"argv": argv, "returncode": 124, "error": "timeout"}


def ps(script):
    return ["powershell", "-NoProfile", "-NonInteractive", "-Command", script]


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="action", required=True)
    for name in ("configure", "test", "collect", "cleanup"):
        p = sub.add_parser(name)
        p.add_argument("--hosts", required=True, help="comma-separated hostnames")
        p.add_argument("--transport", default="https", choices=["http", "https"])
        p.add_argument("--artifacts", default="process,network,logs")
        p.add_argument("--out", default="./evidence")
        p.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    hosts = [h.strip() for h in args.hosts.split(",") if h.strip()]
    results = []

    if args.action == "configure":
        for host in hosts:
            script = (f"Enable-PSRemoting -Force -SkipNetworkProfileCheck; "
                      f"Set-Service WinRM -StartupType Automatic; Start-Service WinRM; "
                      f"winrm enumerate winrm/config/listener")
            results.append({"host": host, "result": run(ps(script), args.dry_run)})
    elif args.action == "test":
        for host in hosts:
            results.append({"host": host,
                            "result": run(ps(f"Test-WSMan -ComputerName {host}"), args.dry_run)})
    elif args.action == "collect":
        os.makedirs(args.out, exist_ok=True)
        wanted = [a.strip() for a in args.artifacts.split(",") if a.strip() in ARTIFACTS]
        for host in hosts:
            body = "; ".join(ARTIFACTS[a] for a in wanted)
            script = (f"$s = New-PSSession -ComputerName {host} -Authentication Negotiate; "
                      f"Invoke-Command -Session $s -ScriptBlock {{ {body} }}; "
                      f"Copy-Item -FromSession $s -Path 'C:\\Windows\\Temp\\*' -Destination '{os.path.abspath(args.out)}'; "
                      f"Remove-PSSession $s")
            results.append({"host": host, "artifacts": wanted,
                            "result": run(ps(script), args.dry_run)})
        if not args.dry_run:
            manifest = []
            for root, _dirs, files in os.walk(args.out):
                for name in files:
                    path = os.path.join(root, name)
                    manifest.append({"file": path, "size": os.path.getsize(path)})
            results.append({"manifest": manifest})
    else:
        for host in hosts:
            script = ("Remove-PSSession -Session (Get-PSSession) -ErrorAction SilentlyContinue; "
                      "Set-Item WSMan:\\localhost\\Client\\TrustedHosts -Value '' -ErrorAction SilentlyContinue; "
                      "Disable-PSRemoting -Force")
            results.append({"host": host, "result": run(ps(script), args.dry_run)})

    print(json.dumps({"action": args.action, "hosts": hosts,
                      "dry_run": args.dry_run, "results": results}, indent=1))


if __name__ == "__main__":
    main()
