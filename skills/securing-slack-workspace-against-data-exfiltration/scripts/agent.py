#!/usr/bin/env python3
"""Helper for this skill. Run with --help for usage."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="Print actions without executing")
    ap.add_argument("--json", action="store_true", help="Output JSON")
    args = ap.parse_args()
    print(json.dumps({"skill": __file__.split("/")[-3], "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
