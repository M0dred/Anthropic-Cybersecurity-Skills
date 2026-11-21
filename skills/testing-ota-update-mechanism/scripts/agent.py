#!/usr/bin/env python3
"""Helper for testing-ota-update-mechanism."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Testing OTA Update Mechanism")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "testing-ota-update-mechanism", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
