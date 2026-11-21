#!/usr/bin/env python3
"""Helper for securing-llm-agent-tool-access."""
import argparse, json, sys

def main():
    ap = argparse.ArgumentParser(description="Securing LLM Agent Tool Access")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    print(json.dumps({"skill": "securing-llm-agent-tool-access", "dry_run": args.dry_run}, indent=1))

if __name__ == "__main__":
    main()
