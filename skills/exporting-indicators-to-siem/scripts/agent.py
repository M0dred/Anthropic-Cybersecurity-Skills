#!/usr/bin/env python3
"""Export indicators, publish them, push to a SIEM, and verify ingestion.

Subcommands:
    export   Convert an indicator JSON list to csv, stix, list, or json.
    publish  Upload a file to an HTTP endpoint (EDL).
    push     Push a CSV to a SIEM lookup table or reference set.
    verify   Compare the consumer count with an expected count.

Examples:
    python3 agent.py export --input indicators.json --format csv --out blocklist.csv
    python3 agent.py publish --file blocklist.csv --url https://edl.example.com/blocklist.csv
    python3 agent.py push --file blocklist.csv --siem splunk --lookup threat_intel
    python3 agent.py verify --url https://edl.example.com/blocklist.csv --expected 1200
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import os
import sys
import urllib.error
import urllib.request
import uuid
from datetime import datetime, timezone

RESERVED = ("10.", "172.16.", "172.17.", "172.18.", "172.19.", "172.2", "172.30.",
            "172.31.", "192.168.", "127.", "169.254.", "0.")


def load(path):
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    if isinstance(data, dict) and "indicators" in data:
        return data["indicators"]
    return data


def is_private(value):
    return any(value.startswith(prefix) for prefix in RESERVED)


def normalize(rows):
    out, seen = [], set()
    for row in rows:
        value = str(row.get("value", "")).strip().lower()
        if not value or value in seen:
            continue
        if row.get("type") == "ipv4" and is_private(value):
            continue
        seen.add(value)
        out.append({"value": value, "type": row.get("type", "unknown"),
                    "reputation": row.get("reputation", "unknown"),
                    "source": row.get("source", ""),
                    "first_seen": row.get("first_seen", ""),
                    "expires": row.get("expires", "")})
    return out


def export(rows, fmt):
    if fmt == "list":
        return "\n".join(r["value"] for r in rows) + "\n"
    if fmt == "csv":
        buf = io.StringIO()
        writer = csv.DictWriter(buf, fieldnames=["indicator", "type", "reputation",
                                                 "source", "first_seen", "expires"])
        writer.writeheader()
        for r in rows:
            writer.writerow({"indicator": r["value"], "type": r["type"],
                             "reputation": r["reputation"], "source": r["source"],
                             "first_seen": r["first_seen"], "expires": r["expires"]})
        return buf.getvalue()
    if fmt == "stix":
        objects = []
        for r in rows:
            pattern = {
                "ipv4": f"[ipv4-addr:value = '{r['value']}']",
                "domain": f"[domain-name:value = '{r['value']}']",
                "url": f"[url:value = '{r['value']}']",
                "hash": f"[file:hashes.'SHA-256' = '{r['value']}']",
            }.get(r["type"])
            if not pattern:
                continue
            objects.append({"type": "indicator", "spec_version": "2.1",
                            "id": f"indicator--{uuid.uuid4()}",
                            "created": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                            "pattern": pattern, "pattern_type": "stix",
                            "valid_from": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})
        return json.dumps({"type": "bundle", "id": f"bundle--{uuid.uuid4()}",
                           "objects": objects}, indent=1)
    return json.dumps(rows, indent=1)


def http(method, url, data=None, headers=None):
    req = urllib.request.Request(url, data=data, method=method)
    for key, value in (headers or {}).items():
        req.add_header(key, value)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return {"status": resp.status, "body": resp.read().decode()[:500]}
    except urllib.error.HTTPError as exc:
        return {"status": exc.code, "error": exc.read().decode()[:300]}
    except Exception as exc:  # noqa: BLE001
        return {"error": str(exc)}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="action", required=True)
    ex = sub.add_parser("export")
    ex.add_argument("--input", required=True)
    ex.add_argument("--format", default="csv", choices=["csv", "stix", "list", "json"])
    ex.add_argument("--out", required=True)
    pub = sub.add_parser("publish")
    pub.add_argument("--file", required=True)
    pub.add_argument("--url", required=True)
    pub.add_argument("--token", default=os.environ.get("EDL_TOKEN", ""))
    push = sub.add_parser("push")
    push.add_argument("--file", required=True)
    push.add_argument("--siem", required=True, choices=["splunk", "sentinel", "qradar"])
    push.add_argument("--lookup", required=True)
    ver = sub.add_parser("verify")
    ver.add_argument("--url", required=True)
    ver.add_argument("--expected", type=int, required=True)
    args = ap.parse_args()

    if args.action == "export":
        rows = normalize(load(args.input))
        text = export(rows, args.format)
        with open(args.out, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        print(json.dumps({"written": args.out, "format": args.format,
                          "indicators": len(rows)}, indent=1))
    elif args.action == "publish":
        data = open(args.file, "rb").read()
        headers = {"Content-Type": "text/csv"}
        if args.token:
            headers["Authorization"] = f"Bearer {args.token}"
        print(json.dumps(http("PUT", args.url, data, headers), indent=1))
    elif args.action == "push":
        data = open(args.file, "rb").read()
        if args.siem == "splunk":
            url = os.environ.get("SPLUNK_URL", "https://splunk:8089") + \
                  f"/servicesNS/nobody/search/data/lookup-table-files/{args.lookup}"
            headers = {"Authorization": f"Splunk {os.environ.get('SPLUNK_TOKEN', '')}"}
            print(json.dumps(http("POST", url, data, headers), indent=1))
        elif args.siem == "qradar":
            url = os.environ.get("QRADAR_URL", "https://qradar") + \
                  f"/api/reference_data/sets/bulk_load/{args.lookup}"
            headers = {"SEC": os.environ.get("QRADAR_TOKEN", ""),
                       "Content-Type": "application/json"}
            values = [line.split(",")[0] for line in data.decode().splitlines()[1:] if line]
            print(json.dumps(http("POST", url, json.dumps(values).encode(), headers), indent=1))
        else:
            print(json.dumps({"error": "use the Azure CLI for Sentinel watchlists",
                              "command": "az sentinel watchlist create ..."}, indent=1))
    else:
        result = http("GET", args.url)
        body = result.get("body", "")
        count = len([line for line in body.splitlines() if line.strip()])
        print(json.dumps({"url": args.url, "expected": args.expected, "actual": count,
                          "match": count == args.expected, "status": result.get("status")}, indent=1))


if __name__ == "__main__":
    main()
