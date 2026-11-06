#!/usr/bin/env python3
"""Extract, refang, filter, and export indicators of compromise from files.

Subcommands:
    extract   Read a file, extract indicators, score them, and export.
    refang    Convert a defanged indicator back to its live form.
    defang    Convert a live indicator to a safe form for sharing.

Examples:
    python3 agent.py extract --file report.pdf --out iocs.json
    python3 agent.py extract --file page.html --allowlist allow.txt --min-confidence 0.5
    python3 agent.py refang --value 'hxxps://evil[.]example[.]com/a'
    python3 agent.py defang --value 'https://evil.example.com/a'
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import ipaddress
import json
import os
import re
import subprocess
import sys
import uuid
import zipfile
from datetime import datetime, timezone

URL_RE = re.compile(r"https?://[^\s\"'<>\)\]]+", re.I)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
IPV4_RE = re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\b")
IPV6_RE = re.compile(r"\b(?:[A-Fa-f0-9]{1,4}:){2,7}[A-Fa-f0-9]{1,4}\b")
DOMAIN_RE = re.compile(r"\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}\b")
HASH_RE = re.compile(r"\b[a-fA-F0-9]{32}\b|\b[a-fA-F0-9]{40}\b|\b[a-fA-F0-9]{64}\b")
CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.I)
REG_RE = re.compile(r"HKEY_[A-Z_]+\\[^\s\"']+")
PATH_RE = re.compile(r"[A-Za-z]:\\[^\s\"<>|]+")
BTC_RE = re.compile(r"\b(?:bc1[a-zA-HJ-NP-Z0-9]{25,62}|[13][a-km-zA-HJ-NP-Z1-9]{25,34})\b")
BASE64_RUN = re.compile(r"[A-Za-z0-9+/]{40,}={0,2}")

SUSPICIOUS_TLDS = {"top", "xyz", "club", "online", "site", "shop", "live", "icu",
                   "buzz", "cyou", "monster", "rest", "bar", "click", "link"}
RESERVED = [ipaddress.ip_network(n) for n in
            ("10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16", "127.0.0.0/8",
             "169.254.0.0/16", "0.0.0.0/8", "224.0.0.0/4", "::1/128", "fc00::/7", "fe80::/10")]


def refang(value):
    out = value
    for a, b in (("hxxps://", "https://"), ("hxxp://", "http://"),
                 ("[.]", "."), ("(.)", "."), ("{.}", "."), ("[dot]", "."),
                 ("[//]", "//"), ("[:]", ":"), ("[@]", "@"), ("[at]", "@")):
        out = out.replace(a, b)
    return out


def defang(value):
    return (value.replace("http://", "hxxp://").replace("https://", "hxxps://")
            .replace(".", "[.]").replace("@", "[@]"))


def read_text(path, mode):
    if path == "-":
        return sys.stdin.read()
    if mode == "auto":
        ext = os.path.splitext(path)[1].lower()
        mode = {".html": "html", ".htm": "html", ".docx": "docx", ".xlsx": "xlsx",
                ".pptx": "pptx", ".pdf": "pdf", ".eml": "text"}.get(ext, "binary" if ext in
                (".exe", ".dll", ".bin", ".so", ".elf") else "text")
    if mode == "html":
        raw = open(path, "rb").read().decode("utf-8", "replace")
        raw = re.sub(r"<script[^>]*>.*?</script>", " ", raw, flags=re.S | re.I)
        raw = re.sub(r"<style[^>]*>.*?</style>", " ", raw, flags=re.S | re.I)
        raw = re.sub(r"<[^>]+>", " ", raw)
        return re.sub(r"&[a-z]+;|&#\d+;", " ", raw)
    if mode in ("docx", "xlsx", "pptx"):
        parts = {"docx": ("word/document.xml",), "xlsx": ("xl/sharedStrings.xml",),
                 "pptx": tuple(f"ppt/slides/slide{i}.xml" for i in range(1, 50))}[mode]
        out = []
        with zipfile.ZipFile(path) as zf:
            for name in zf.namelist():
                if name in parts or name.startswith(("word/header", "word/footer")):
                    out.append(re.sub(r"<[^>]+>", " ", zf.read(name).decode("utf-8", "replace")))
        return "\n".join(out)
    if mode == "pdf":
        try:
            return subprocess.run(["pdftotext", "-layout", path, "-"],
                                  capture_output=True, text=True, timeout=120).stdout
        except (FileNotFoundError, subprocess.TimeoutExpired):
            raw = open(path, "rb").read()
            return " ".join(re.findall(rb"[\x20-\x7e]{6,}", raw).__str__())
    if mode == "binary":
        raw = open(path, "rb").read()
        ascii_runs = re.findall(rb"[\x20-\x7e]{6,}", raw)
        utf16_runs = re.findall(rb"(?:[\x20-\x7e]\x00){6,}", raw)
        return "\n".join([r.decode("ascii", "ignore") for r in ascii_runs] +
                         [r.decode("utf-16le", "ignore") for r in utf16_runs])
    return open(path, "rb").read().decode("utf-8", "replace")


def context_for(text, value, width=80):
    index = text.find(value)
    if index < 0:
        return ""
    return text[max(0, index - width): index + len(value) + width].replace("\n", " ")


def valid_public_ip(value):
    try:
        ip = ipaddress.ip_address(value)
    except ValueError:
        return False
    return not any(ip in net for net in RESERVED if net.version == ip.version)


def extract(text, min_len=6):
    clean = BASE64_RUN.sub(" ", refang(text))
    found = {}

    def add(kind, value, raw=None):
        value = value.strip().rstrip(".,;:)")
        if not value or len(value) < min_len:
            return
        key = (kind, value.lower())
        if key in found:
            found[key]["count"] += 1
            return
        found[key] = {"type": kind, "value": value.lower() if kind != "path" else value,
                      "defanged": defang(value), "count": 1,
                      "context": context_for(text, raw or value)}

    for url in URL_RE.findall(clean):
        add("url", url)
    for email in EMAIL_RE.findall(clean):
        add("email", email)
    for ip in IPV4_RE.findall(clean):
        add("ipv4", ip)
    for ip in IPV6_RE.findall(clean):
        try:
            ipaddress.ip_address(ip)
            add("ipv6", ip)
        except ValueError:
            continue
    for domain in DOMAIN_RE.findall(clean):
        if not IPV4_RE.match(domain):
            add("domain", domain)
    for h in HASH_RE.findall(clean):
        add("hash", h)
    for cve in CVE_RE.findall(clean):
        add("cve", cve)
    for reg in REG_RE.findall(clean):
        add("registry", reg)
    for path in PATH_RE.findall(clean):
        add("path", path)
    for btc in BTC_RE.findall(clean):
        add("bitcoin", btc)
    return list(found.values())


def load_allowlist(path):
    entries = set()
    if not path:
        return entries
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip().lower()
            if line and not line.startswith("#"):
                entries.add(line)
    return entries


def allowed(value, allowlist):
    value = value.lower()
    return any(value == e or value.endswith("." + e) for e in allowlist)


def score(ind, allowlist):
    value = ind["value"]
    s = 0.4
    if ind["type"] == "ipv4":
        s += 0.2 if valid_public_ip(value) else -0.4
    if ind["type"] == "domain":
        tld = value.rsplit(".", 1)[-1]
        s += 0.1 if tld in SUSPICIOUS_TLDS else 0.0
        if value.count(".") >= 3:
            s += 0.05
    if ind["count"] > 1:
        s += 0.1
    ctx = ind["context"].lower()
    if any(w in ctx for w in ("malware", "phishing", "c2", "command", "payload",
                              "exploit", "ransomware", "cve-", "ioc", "indicator")):
        s += 0.2
    if allowed(value, allowlist):
        return -1.0
    return round(max(0.0, min(1.0, s)), 2)


def export(indicators, fmt, source, digest):
    if fmt == "csv":
        buf = io.StringIO()
        writer = csv.DictWriter(buf, fieldnames=["type", "value", "defanged", "confidence", "context"])
        writer.writeheader()
        for ind in indicators:
            writer.writerow({k: ind.get(k, "") for k in writer.fieldnames})
        return buf.getvalue()
    if fmt == "stix":
        objects = []
        for ind in indicators:
            pattern = {
                "ipv4": f"[ipv4-addr:value = '{ind['value']}']",
                "ipv6": f"[ipv6-addr:value = '{ind['value']}']",
                "domain": f"[domain-name:value = '{ind['value']}']",
                "url": f"[url:value = '{ind['value']}']",
                "email": f"[email-addr:value = '{ind['value']}']",
                "hash": f"[file:hashes.'SHA-256' = '{ind['value']}']",
                "cve": f"[vulnerability:name = '{ind['value'].upper()}']",
            }.get(ind["type"])
            if not pattern:
                continue
            objects.append({"type": "indicator", "spec_version": "2.1",
                            "id": f"indicator--{uuid.uuid4()}",
                            "created": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                            "pattern": pattern, "pattern_type": "stix",
                            "valid_from": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                            "confidence": int(ind["confidence"] * 100)})
        return json.dumps({"type": "bundle", "id": f"bundle--{uuid.uuid4()}",
                           "objects": objects}, indent=1)
    counts = {}
    for ind in indicators:
        counts[ind["type"]] = counts.get(ind["type"], 0) + 1
    return json.dumps({"file": source, "sha256": digest,
                       "extracted_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                       "counts": counts, "indicators": indicators}, indent=1)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="action", required=True)
    ex = sub.add_parser("extract")
    ex.add_argument("--file", required=True)
    ex.add_argument("--mode", default="auto",
                    choices=["auto", "text", "html", "docx", "xlsx", "pptx", "pdf", "binary"])
    ex.add_argument("--allowlist")
    ex.add_argument("--min-confidence", type=float, default=0.0)
    ex.add_argument("--format", default="json", choices=["json", "csv", "stix"])
    ex.add_argument("--out")
    for name in ("refang", "defang"):
        p = sub.add_parser(name)
        p.add_argument("--value", required=True)
    args = ap.parse_args()

    if args.action == "refang":
        print(refang(args.value))
        return
    if args.action == "defang":
        print(defang(args.value))
        return

    text = read_text(args.file, args.mode)
    digest = hashlib.sha256(open(args.file, "rb").read()).hexdigest() if args.file != "-" else ""
    allow = load_allowlist(args.allowlist)
    indicators = extract(text)
    for ind in indicators:
        ind["confidence"] = score(ind, allow)
    indicators = [i for i in indicators if i["confidence"] >= args.min_confidence]
    indicators.sort(key=lambda i: (-i["confidence"], i["type"], i["value"]))
    output = export(indicators, args.format, os.path.basename(args.file), digest)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(output)
        print(json.dumps({"written": args.out, "indicators": len(indicators)}, indent=1))
    else:
        print(output)


if __name__ == "__main__":
    main()
