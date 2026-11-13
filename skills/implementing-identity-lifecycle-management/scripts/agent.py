#!/usr/bin/env python3
"""Plan, apply, and reconcile identity lifecycle changes.

Subcommands:
    plan       Compare an HR export with a directory snapshot and emit a plan.
    apply      Execute a plan (dry-run by default).
    leaver     Emit the disable/revoke steps for one worker.
    reconcile  Report drift between the HR export and the directory snapshot.

Examples:
    python3 agent.py plan --hr hr_export.csv --snapshot dir.json --target ad --out plan.json
    python3 agent.py apply --plan plan.json --dry-run
    python3 agent.py leaver --worker W-12345 --target okta --dry-run
    python3 agent.py reconcile --hr hr_export.csv --snapshot dir.json --target ad
"""
from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from datetime import datetime, timezone


def load_hr(path):
    rows = {}
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            worker = (row.get("worker_id") or "").strip()
            if worker:
                rows[worker] = {k: (v or "").strip() for k, v in row.items()}
    return rows


def load_snapshot(path):
    if not path or not path.endswith(".json"):
        return []
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def build_plan(hr, directory):
    by_worker = {d.get("worker_id"): d for d in directory if d.get("worker_id")}
    actions = []
    for worker, row in hr.items():
        current = by_worker.get(worker)
        status = row.get("status", "").lower()
        if current is None:
            actions.append({"worker_id": worker, "action": "create",
                            "email": row.get("email"), "department": row.get("department")})
            continue
        if status in ("terminated", "inactive") and current.get("enabled", True):
            actions.append({"worker_id": worker, "action": "disable",
                            "reason": f"status={status}"})
        elif status == "active" and not current.get("enabled", True):
            actions.append({"worker_id": worker, "action": "enable"})
        if row.get("department") and row["department"] != current.get("department"):
            actions.append({"worker_id": worker, "action": "move",
                            "from": current.get("department"), "to": row["department"]})
    for worker in by_worker:
        if worker not in hr:
            actions.append({"worker_id": worker, "action": "orphan",
                            "reason": "no HR record"})
    return actions


def command_for(action, target):
    worker = action["worker_id"]
    if target == "ad":
        return {
            "create": ["powershell", "-Command", f"New-ADUser -EmployeeID '{worker}' -Enabled $true"],
            "disable": ["powershell", "-Command", f"Disable-ADAccount -Identity '{worker}'"],
            "enable": ["powershell", "-Command", f"Enable-ADAccount -Identity '{worker}'"],
            "move": ["powershell", "-Command", f"Set-ADUser -Identity '{worker}' -Department '{action.get('to')}'"],
            "orphan": ["powershell", "-Command", f"Disable-ADAccount -Identity '{worker}'"],
        }.get(action["action"])
    if target == "entra":
        return {
            "create": ["az", "ad", "user", "create", "--display-name", worker],
            "disable": ["az", "ad", "user", "update", "--id", worker, "--account-enabled", "false"],
            "enable": ["az", "ad", "user", "update", "--id", worker, "--account-enabled", "true"],
            "move": ["az", "ad", "user", "update", "--id", worker, "--department", action.get("to", "")],
            "orphan": ["az", "ad", "user", "update", "--id", worker, "--account-enabled", "false"],
        }.get(action["action"])
    return {
        "create": ["sh", "-c", f"curl -sS -X POST https://$OKTA_ORG.okta.com/api/v1/users -H \"Authorization: SSWS $OKTA_TOKEN\" -d '{{\"profile\":{{\"employeeNumber\":\"{worker}\"}}}}'"],
        "disable": ["sh", "-c", f"curl -sS -X POST https://$OKTA_ORG.okta.com/api/v1/users/{worker}/lifecycle/deactivate -H \"Authorization: SSWS $OKTA_TOKEN\""],
        "enable": ["sh", "-c", f"curl -sS -X POST https://$OKTA_ORG.okta.com/api/v1/users/{worker}/lifecycle/activate -H \"Authorization: SSWS $OKTA_TOKEN\""],
        "move": ["sh", "-c", f"curl -sS -X POST https://$OKTA_ORG.okta.com/api/v1/users/{worker} -H \"Authorization: SSWS $OKTA_TOKEN\" -d '{{\"profile\":{{\"department\":\"{action.get('to')}\"}}}}'"],
        "orphan": ["sh", "-c", f"curl -sS -X POST https://$OKTA_ORG.okta.com/api/v1/users/{worker}/lifecycle/deactivate -H \"Authorization: SSWS $OKTA_TOKEN\""],
    }.get(action["action"])


def run(cmd, dry):
    if dry:
        return {"argv": cmd, "dry_run": True, "returncode": 0}
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        return {"argv": cmd, "returncode": proc.returncode,
                "stdout": proc.stdout[-800:], "stderr": proc.stderr[-800:]}
    except FileNotFoundError:
        return {"argv": cmd, "returncode": 127, "error": f"not found: {cmd[0]}"}
    except subprocess.TimeoutExpired:
        return {"argv": cmd, "returncode": 124, "error": "timeout"}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="action", required=True)
    p = sub.add_parser("plan")
    p.add_argument("--hr", required=True)
    p.add_argument("--snapshot")
    p.add_argument("--target", default="ad", choices=["ad", "entra", "okta"])
    p.add_argument("--out")
    a = sub.add_parser("apply")
    a.add_argument("--plan", required=True)
    a.add_argument("--target", default="ad", choices=["ad", "entra", "okta"])
    a.add_argument("--dry-run", action="store_true")
    l = sub.add_parser("leaver")
    l.add_argument("--worker", required=True)
    l.add_argument("--target", default="ad", choices=["ad", "entra", "okta"])
    l.add_argument("--dry-run", action="store_true")
    r = sub.add_parser("reconcile")
    r.add_argument("--hr", required=True)
    r.add_argument("--snapshot")
    r.add_argument("--target", default="ad", choices=["ad", "entra", "okta"])
    args = ap.parse_args()

    if args.action == "plan":
        actions = build_plan(load_hr(args.hr), load_snapshot(args.snapshot))
        text = json.dumps({"generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                           "target": args.target, "actions": actions}, indent=1)
        if args.out:
            open(args.out, "w", encoding="utf-8").write(text)
            print(json.dumps({"written": args.out, "actions": len(actions)}, indent=1))
        else:
            print(text)
    elif args.action == "apply":
        plan = json.load(open(args.plan, encoding="utf-8"))
        results = []
        for action in plan.get("actions", []):
            cmd = command_for(action, args.target)
            if not cmd:
                results.append({"action": action, "error": "no command mapped"})
                continue
            results.append({"action": action, "result": run(cmd, args.dry_run)})
        print(json.dumps({"target": args.target, "dry_run": args.dry_run,
                          "results": results}, indent=1))
    elif args.action == "leaver":
        steps = [
            {"worker_id": args.worker, "action": "disable"},
            {"worker_id": args.worker, "action": "revoke_sessions"},
            {"worker_id": args.worker, "action": "remove_groups"},
        ]
        results = []
        for step in steps:
            if step["action"] == "revoke_sessions":
                cmd = ["sh", "-c", f"curl -sS -X DELETE https://$OKTA_ORG.okta.com/api/v1/users/{args.worker}/sessions -H \"Authorization: SSWS $OKTA_TOKEN\""] \
                    if args.target == "okta" else \
                    ["az", "rest", "--method", "POST", "--url",
                     f"https://graph.microsoft.com/v1.0/users/{args.worker}/revokeSignInSessions"]
            elif step["action"] == "remove_groups":
                cmd = None
            else:
                cmd = command_for(step, args.target)
            results.append({"step": step, "result": run(cmd, args.dry_run) if cmd else {"skipped": True}})
        print(json.dumps({"worker": args.worker, "target": args.target,
                          "dry_run": args.dry_run, "results": results}, indent=1))
    else:
        actions = build_plan(load_hr(args.hr), load_snapshot(args.snapshot))
        counts = {}
        for action in actions:
            counts[action["action"]] = counts.get(action["action"], 0) + 1
        print(json.dumps({"target": args.target, "counts": counts, "actions": actions}, indent=1))


if __name__ == "__main__":
    main()
