#!/usr/bin/env python3
"""Helper for measuring-detection-engineering-metrics."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Measuring Detection Engineering Metrics")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "measuring-detection-engineering-metrics", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
