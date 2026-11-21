#!/usr/bin/env python3
"""Helper for detecting-bec-payroll-diversion."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Detecting BEC Payroll Diversion")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "detecting-bec-payroll-diversion", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
