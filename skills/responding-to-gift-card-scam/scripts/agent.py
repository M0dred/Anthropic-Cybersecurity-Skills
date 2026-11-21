#!/usr/bin/env python3
"""Helper for responding-to-gift-card-scam."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Responding to Gift Card Scam")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "responding-to-gift-card-scam", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
