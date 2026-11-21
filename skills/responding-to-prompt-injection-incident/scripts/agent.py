#!/usr/bin/env python3
"""Helper for responding-to-prompt-injection-incident."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Responding to Prompt Injection Incident")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "responding-to-prompt-injection-incident", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
