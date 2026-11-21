#!/usr/bin/env python3
"""Helper for securing-cloud-data-lake."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Securing Cloud Data Lake")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "securing-cloud-data-lake", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
