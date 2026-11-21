#!/usr/bin/env python3
"""Helper for executing-wire-fraud-recall."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Executing Wire Fraud Recall")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "executing-wire-fraud-recall", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
