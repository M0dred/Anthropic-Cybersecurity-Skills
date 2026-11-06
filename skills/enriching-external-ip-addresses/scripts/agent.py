#!/usr/bin/env python3
"""Enrich external IP addresses with geo, ASN, PTR, and reputation.

Subcommands:
    classify  Validate addresses and label private/reserved/shared ranges.
    enrich    Query enabled sources, cache responses, and emit one record.

Environment:
    ABUSEIPDB_API_KEY, VT_API_KEY, GREYNOISE_API_KEY, IPINFO_TOKEN (optional)

Examples:
    python3 agent.py classify --ip 203.0.113.10 --ip 10.0.0.5
    python3 agent.py enrich --ip 203.0.113.10 --out enrichment.json
    python3 agent.py enrich --ip 203.0.113.10 --sources ipinfo,abuseipdb --no-cache
"""
from __future__ import annotations

import argparse
import ipaddress
import json
import os
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

RESERVED = [ipaddress.ip_network(n) for n in
            ("10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16", "127.0.0.0/8",
             "169.254.0.0/16", "0.0.0.0/8", "224.0.0.0/4", "100.64.0.0/10",
             "192.0.2.0/24", "198.51.100.0/24", "203.0.113.0/24",
             "::1/128", "fc00::/7", "fe80::/10", "2001:db8::/32")]
SHARED_HINTS = ("amazon", "google", "microsoft", "cloudflare", "akamai",
                "fastly", "digitalocean", "linode", "ovh", "hetzner",
                "vultr", "alibaba", "oracle", "azure")
CACHE_TTL = 24 * 3600


def classify(ip):
    try:
        addr = ipaddress.ip_address(ip)
    except ValueError as exc:
        return {"ip": ip, "valid": False, "reason": str(exc)}
    reserved = next((str(n) for n in RESERVED if addr in n and n.version == addr.version), None)
    return {"ip": ip, "valid": True, "version": addr.version,
            "private": addr.is_private, "loopback": addr.is_loopback,
            "multicast": addr.is_multicast, "reserved_range": reserved,
            "enrichable": reserved is None and not addr.is_private}


def cache_path(cache_dir, source, ip):
    safe = ip.replace(":", "_").replace("/", "_")
    return os.path.join(cache_dir, f"{source}__{safe}.json")


def cached(cache_dir, source, ip, use_cache):
    if not use_cache:
        return None
    path = cache_path(cache_dir, source, ip)
    if not os.path.exists(path):
        return None
    if time.time() - os.path.getmtime(path) > CACHE_TTL:
        return None
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def store(cache_dir, source, ip, payload):
    os.makedirs(cache_dir, exist_ok=True)
    with open(cache_path(cache_dir, source, ip), "w", encoding="utf-8") as handle:
        json.dump({"fetched_at": datetime.now(timezone.utc).isoformat(), "payload": payload},
                  handle)


def get_json(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode()), None
    except urllib.error.HTTPError as exc:
        return None, f"HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001 - surfaced in sources_failed
        return None, str(exc)


def source_ipinfo(ip, cache_dir, use_cache):
    hit = cached(cache_dir, "ipinfo", ip, use_cache)
    if hit:
        return hit["payload"], None
    token = os.environ.get("IPINFO_TOKEN", "")
    url = f"https://ipinfo.io/{ip}/json" + (f"?token={token}" if token else "")
    data, err = get_json(url)
    if data:
        store(cache_dir, "ipinfo", ip, data)
    return data, err


def source_abuseipdb(ip, cache_dir, use_cache):
    key = os.environ.get("ABUSEIPDB_API_KEY")
    if not key:
        return None, "missing ABUSEIPDB_API_KEY"
    hit = cached(cache_dir, "abuseipdb", ip, use_cache)
    if hit:
        return hit["payload"], None
    url = "https://api.abuseipdb.com/api/v2/check?" + urllib.parse.urlencode(
        {"ipAddress": ip, "maxAgeInDays": 90})
    data, err = get_json(url, {"Key": key, "Accept": "application/json"})
    if data:
        store(cache_dir, "abuseipdb", ip, data)
    return data, err


def source_virustotal(ip, cache_dir, use_cache):
    key = os.environ.get("VT_API_KEY")
    if not key:
        return None, "missing VT_API_KEY"
    hit = cached(cache_dir, "virustotal", ip, use_cache)
    if hit:
        return hit["payload"], None
    data, err = get_json(f"https://www.virustotal.com/api/v3/ip_addresses/{ip}",
                         {"x-apikey": key})
    if data:
        store(cache_dir, "virustotal", ip, data)
    return data, err


def source_greynoise(ip, cache_dir, use_cache):
    key = os.environ.get("GREYNOISE_API_KEY")
    if not key:
        return None, "missing GREYNOISE_API_KEY"
    hit = cached(cache_dir, "greynoise", ip, use_cache)
    if hit:
        return hit["payload"], None
    data, err = get_json(f"https://api.greynoise.io/v3/community/{ip}", {"key": key})
    if data:
        store(cache_dir, "greynoise", ip, data)
    return data, err


def ptr(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror, OSError):
        return ""


def normalize(ip, results):
    record = {"ip": ip, "geo": {}, "ptr": ptr(ip), "reputation": {},
              "sources_ok": [], "sources_failed": []}
    ipinfo = results.get("ipinfo") or {}
    if ipinfo:
        org = ipinfo.get("org", "")
        asn, _, owner = org.partition(" ")
        record["geo"] = {"country": ipinfo.get("country", ""), "city": ipinfo.get("city", ""),
                         "region": ipinfo.get("region", ""), "asn": asn, "org": owner or org}
        record["sources_ok"].append("ipinfo")
    else:
        record["sources_failed"].append("ipinfo")

    abuse = (results.get("abuseipdb") or {}).get("data") or {}
    if abuse:
        record["reputation"]["abuseipdb"] = {
            "score": abuse.get("abuseConfidenceScore"),
            "reports": abuse.get("totalReports"),
            "last_reported": abuse.get("lastReportedAt"),
            "usage_type": abuse.get("usageType"),
            "isp": abuse.get("isp")}
        record["sources_ok"].append("abuseipdb")
    else:
        record["sources_failed"].append("abuseipdb")

    vt = ((results.get("virustotal") or {}).get("data") or {}).get("attributes") or {}
    if vt:
        stats = vt.get("last_analysis_stats", {})
        record["reputation"]["virustotal"] = {
            "malicious": stats.get("malicious", 0), "suspicious": stats.get("suspicious", 0),
            "harmless": stats.get("harmless", 0), "reputation": vt.get("reputation")}
        record["sources_ok"].append("virustotal")
    else:
        record["sources_failed"].append("virustotal")

    gn = results.get("greynoise") or {}
    if gn:
        record["reputation"]["greynoise"] = {
            "classification": gn.get("classification"), "riot": gn.get("riot"),
            "name": gn.get("name"), "last_seen": gn.get("last_seen")}
        record["sources_ok"].append("greynoise")
    else:
        record["sources_failed"].append("greynoise")

    org = record["geo"].get("org", "").lower()
    record["context"] = {
        "shared_infrastructure": any(h in org for h in SHARED_HINTS),
        "asn": record["geo"].get("asn", ""),
        "ptr_matches_org": bool(record["ptr"]) and any(
            part in record["ptr"].lower() for part in org.split() if len(part) > 3)}
    record["confidence"] = confidence(record)
    return record


def confidence(record):
    score = 0.0
    abuse = record["reputation"].get("abuseipdb", {})
    vt = record["reputation"].get("virustotal", {})
    gn = record["reputation"].get("greynoise", {})
    if (abuse.get("score") or 0) >= 80:
        score += 0.30
    if (vt.get("malicious") or 0) >= 5:
        score += 0.25
    if gn.get("classification") == "malicious":
        score += 0.25
    if record["context"].get("shared_infrastructure"):
        score += 0.10
    if record["context"].get("ptr_matches_org"):
        score += 0.05
    signals = [bool((abuse.get("score") or 0) >= 80), bool((vt.get("malicious") or 0) >= 5),
               gn.get("classification") == "malicious"]
    if sum(signals) >= 2:
        score += 0.05
    score = min(score, 1.0)
    if len(record["sources_ok"]) < 2:
        score = min(score, 0.5)
    return round(score, 2)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="action", required=True)
    for name in ("classify", "enrich"):
        p = sub.add_parser(name)
        p.add_argument("--ip", action="append", required=True)
        p.add_argument("--out")
        p.add_argument("--sources", default="ipinfo,abuseipdb,virustotal,greynoise")
        p.add_argument("--cache-dir", default=os.path.expanduser("~/.cache/ip-enrich"))
        p.add_argument("--no-cache", action="store_true")
    args = ap.parse_args()

    if args.action == "classify":
        print(json.dumps([classify(ip) for ip in args.ip], indent=1))
        return

    enabled = [s.strip() for s in args.sources.split(",") if s.strip()]
    fetchers = {"ipinfo": source_ipinfo, "abuseipdb": source_abuseipdb,
                "virustotal": source_virustotal, "greynoise": source_greynoise}
    output = []
    for ip in args.ip:
        info = classify(ip)
        if not info["enrichable"]:
            output.append({"ip": ip, "skipped": True, "reason": info.get("reserved_range")
                           or "private or reserved"})
            continue
        results, errors = {}, {}
        for source in enabled:
            if source not in fetchers:
                errors[source] = "unknown source"
                continue
            data, err = fetchers[source](ip, args.cache_dir, not args.no_cache)
            results[source] = data
            if err:
                errors[source] = err
        record = normalize(ip, results)
        record["errors"] = errors
        output.append(record)
    text = json.dumps(output if len(output) > 1 else output[0], indent=1)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(text)
        print(json.dumps({"written": args.out, "records": len(output)}, indent=1))
    else:
        print(text)


if __name__ == "__main__":
    main()
