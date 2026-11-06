#!/usr/bin/env python3
"""Response runtime: phase checklist with entry/exit criteria and a decision log."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone

CONFIG = {
 "skill": "triaging-third-party-findings-with-panorays",
 "description": "triaging third party findings with panorays",
 "phase": "contain"
}
PHASES = {
    "contain": ["Confirm the scope", "Capture volatile evidence", "Isolate or block",
                "Preserve the responder channel", "Verify containment"],
    "eradicate": ["Identify the persistence", "Remove the payload", "Reset credentials",
                  "Patch the exploited path", "Rescan and confirm clean"],
    "recover": ["Restore from a known-good source", "Validate integrity",
                "Reconnect in stages", "Monitor for recurrence", "Close with lessons learned"],
}


def main(config=None):
    cfg = config or CONFIG
    ap = argparse.ArgumentParser(description=cfg.get("description", "response"))
    ap.add_argument("--phase", default=cfg.get("phase", "contain"),
                    choices=list(PHASES))
    ap.add_argument("--incident", required=True)
    ap.add_argument("--done", action="append", default=[])
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    steps = PHASES[args.phase]
    done = set(args.done)
    record = {"skill": cfg.get("skill", ""), "incident": args.incident,
              "phase": args.phase,
              "started_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "steps": [{"step": s, "done": s in done} for s in steps],
              "complete": all(s in done for s in steps),
              "exit_criteria": "all steps done and evidence attached"}
    print(json.dumps(record, indent=1))


if __name__ == "__main__":
    main()
