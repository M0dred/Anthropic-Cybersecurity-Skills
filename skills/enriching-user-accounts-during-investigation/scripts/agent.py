#!/usr/bin/env python3
"""Enrichment runtime: normalize one indicator or entity across sources."""
from __future__ import annotations

import argparse
import ipaddress
import json
import os
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

CONFIG = {
 "skill": "enriching-user-accounts-during-investigation",
 "description": "enriching user accounts during investigation",
 "type": "account"
}
RESERVED = [ipaddress.ip_network(n) for n in
            ("10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16", "127.0.0.0/8",
             "169.254.0.0/16", "0.0.0.0/8", "224.0.0.0/4", "::1/128", "fc00::/7",
             "fe80::/10", "2001:db8::/32")]


def get(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read().decode()), None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001
        return None, str(e)


def ip_sources(value):
    out, errs = {}, {}
    data, err = get(f"https://ipinfo.io/{value}/json")
    if data:
        out["ipinfo"] = data
    else:
        errs["ipinfo"] = err
    key = os.environ.get("ABUSEIPDB_API_KEY")
    if key:
        data, err = get("https://api.abuseipdb.com/api/v2/check?" + urllib.parse.urlencode(
            {"ipAddress": value, "maxAgeInDays": 90}), {"Key": key, "Accept": "application/json"})
        if data:
            out["abuseipdb"] = data
        else:
            errs["abuseipdb"] = err
    key = os.environ.get("VT_API_KEY")
    if key:
        data, err = get(f"https://www.virustotal.com/api/v3/ip_addresses/{value}",
                        {"x-apikey": key})
        if data:
            out["virustotal"] = data
        else:
            errs["virustotal"] = err
    return out, errs


def domain_sources(value):
    out, errs = {}, {}
    try:
        out["dns_a"] = sorted({r[4][0] for r in socket.getaddrinfo(value, None)})
    except socket.gaierror as e:
        errs["dns_a"] = str(e)
    data, err = get(f"https://rdap.org/domain/{value}")
    if data:
        out["rdap"] = {"handle": data.get("handle"),
                       "events": data.get("events", [])[:5]}
    else:
        errs["rdap"] = err
    key = os.environ.get("VT_API_KEY")
    if key:
        data, err = get(f"https://www.virustotal.com/api/v3/domains/{value}", {"x-apikey": key})
        if data:
            out["virustotal"] = data
        else:
            errs["virustotal"] = err
    return out, errs


def hash_sources(value):
    out, errs = {}, {}
    key = os.environ.get("VT_API_KEY")
    if key:
        data, err = get(f"https://www.virustotal.com/api/v3/files/{value}", {"x-apikey": key})
        if data:
            out["virustotal"] = data
        else:
            errs["virustotal"] = err
    else:
        errs["virustotal"] = "missing VT_API_KEY"
    return out, errs


def score(kind, data):
    s = 0.3
    if kind == "ip":
        abuse = ((data.get("abuseipdb") or {}).get("data") or {})
        vt = ((data.get("virustotal") or {}).get("data") or {}).get("attributes", {})
        if (abuse.get("abuseConfidenceScore") or 0) >= 80:
            s += 0.35
        if (vt.get("last_analysis_stats", {}).get("malicious") or 0) >= 5:
            s += 0.35
    if kind == "hash":
        vt = ((data.get("virustotal") or {}).get("data") or {}).get("attributes", {})
        if (vt.get("last_analysis_stats", {}).get("malicious") or 0) >= 5:
            s += 0.5
    return round(min(s, 1.0), 2)


def main(config=None):
    cfg = config or CONFIG
    ap = argparse.ArgumentParser(description=cfg.get("description", "enrichment"))
    ap.add_argument("--type", default=cfg.get("type", "ip"),
                    choices=["ip", "domain", "url", "hash", "email", "cve", "account", "asset"])
    ap.add_argument("--value", required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    kind = args.type
    if kind == "ip":
        try:
            addr = ipaddress.ip_address(args.value)
            if any(addr in n for n in RESERVED if n.version == addr.version):
                print(json.dumps({"value": args.value, "skipped": "private or reserved"}, indent=1))
                return
        except ValueError:
            print(json.dumps({"value": args.value, "error": "invalid ip"}, indent=1))
            sys.exit(2)
        data, errs = ip_sources(args.value)
    elif kind == "domain":
        data, errs = domain_sources(args.value)
    elif kind == "hash":
        data, errs = hash_sources(args.value)
    else:
        data, errs = {}, {"note": "no free source configured for this type"}
    record = {"type": kind, "value": args.value, "sources": data, "errors": errs,
              "confidence": score(kind, data),
              "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "skill": cfg.get("skill", "")}
    print(json.dumps(record, indent=1))


if __name__ == "__main__":
    main()
