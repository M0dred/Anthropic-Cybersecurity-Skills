#!/usr/bin/env python3
"""Helper for securing-cloud-ai-services."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Securing Cloud AI Services")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "securing-cloud-ai-services", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
