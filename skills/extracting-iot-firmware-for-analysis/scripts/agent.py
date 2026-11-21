#!/usr/bin/env python3
"""Helper for extracting-iot-firmware-for-analysis."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Extracting IoT Firmware for Analysis")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "extracting-iot-firmware-for-analysis", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
