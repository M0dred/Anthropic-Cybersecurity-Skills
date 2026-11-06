#!/usr/bin/env python3
"""Hunting runtime: turn indicators into queries, run or print them, triage hits."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys

CONFIG = {
 "skill": "hunting-with-securonix",
 "description": "hunting with securonix",
 "platforms": [
  "splunk"
 ]
}
QUERIES = {
    "splunk": 'index=* ({terms}) | stats count by host, user, src_ip, dest_ip | sort -count',
    "sentinel": 'union SecurityEvent, DeviceProcessEvents, DeviceNetworkEvents\n| where {kql}\n| summarize count() by DeviceName, AccountName, RemoteIP',
    "qradar": "SELECT sourceip, destinationip, username, COUNT(*) FROM events WHERE {sql} GROUP BY sourceip, destinationip, username",
    "elastic": '{"query":{"bool":{"should":[{"match_phrase":{"url.full":"{value}"}},{"match_phrase":{"dns.question.name":"{value}"}}]}}}',
    "cloudtrail": 'fields @timestamp, eventName, userIdentity.arn, sourceIPAddress | filter eventName like /{value}/ | sort @timestamp desc',
    "edr": 'event_simpleName IN (NetworkConnectIP4, DnsRequest, ProcessRollup2) AND ({terms})',
}


def terms(values):
    return " OR ".join(f'"{v}"' for v in values)


def build(platform, values, field):
    template = QUERIES.get(platform, QUERIES["splunk"])
    joined = terms(values)
    return template.format(terms=joined, value=values[0] if values else "",
                           kql=" or ".join(f'{field} has "{v}"' for v in values),
                           sql=" OR ".join(f"destinationip = '{v}'" for v in values))


def run(platform, query, dry):
    if dry:
        return {"query": query, "dry_run": True}
    if platform == "splunk":
        cmd = ["curl", "-sS", "-k", "-H", "Authorization: Bearer " + __import__("os").environ.get("SPLUNK_TOKEN", ""),
               "https://splunk.example.com:8089/services/search/jobs/export",
               "-d", "search=" + query, "-d", "output_mode=json"]
    elif platform == "sentinel":
        cmd = ["az", "monitor", "log-analytics", "query", "--workspace",
               __import__("os").environ.get("LOG_ANALYTICS_WORKSPACE", ""), "--analytics-query", query]
    elif platform == "qradar":
        cmd = ["curl", "-sS", "-H", "SEC: " + __import__("os").environ.get("QRADAR_TOKEN", ""),
               "-H", "Version: 12.0", "https://qradar.example.com/api/ariel/searches",
               "-d", "query_expression=" + query]
    else:
        return {"query": query, "error": "no runner configured for this platform"}
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    return {"query": query, "returncode": p.returncode, "stdout": p.stdout[-3000:],
            "stderr": p.stderr[-1000:]}


def main(config=None):
    cfg = config or CONFIG
    ap = argparse.ArgumentParser(description=cfg.get("description", "hunt"))
    ap.add_argument("--platform", default=(cfg.get("platforms") or ["splunk"])[0],
                    choices=cfg.get("platforms") or ["splunk"])
    ap.add_argument("--value", action="append", required=True)
    ap.add_argument("--field", default="dest_ip")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    query = build(args.platform, args.value, args.field)
    result = run(args.platform, query, not args.run)
    print(json.dumps({"skill": cfg.get("skill", ""), "platform": args.platform,
                      "values": args.value, "result": result}, indent=1))


if __name__ == "__main__":
    main()
