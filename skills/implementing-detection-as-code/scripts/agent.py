#!/usr/bin/env python3
"""Helper for implementing-detection-as-code."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Implementing Detection as Code")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "implementing-detection-as-code", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
