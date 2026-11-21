#!/usr/bin/env python3
"""Helper for analyzing-harvest-now-decrypt-later."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Analyzing Harvest Now Decrypt Later")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "analyzing-harvest-now-decrypt-later", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
