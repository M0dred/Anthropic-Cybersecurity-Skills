#!/usr/bin/env python3
"""Helper for defending-against-ai-powered-phishing."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Defending Against AI-Powered Phishing")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "defending-against-ai-powered-phishing", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
