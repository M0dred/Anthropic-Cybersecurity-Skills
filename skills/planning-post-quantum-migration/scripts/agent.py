#!/usr/bin/env python3
"""Helper for planning-post-quantum-migration."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Planning Post-Quantum Migration")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "planning-post-quantum-migration", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
