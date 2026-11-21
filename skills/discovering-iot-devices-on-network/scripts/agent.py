#!/usr/bin/env python3
"""Helper for discovering-iot-devices-on-network."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Discovering IoT Devices on Network")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "discovering-iot-devices-on-network", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
