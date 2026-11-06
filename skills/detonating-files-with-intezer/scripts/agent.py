#!/usr/bin/env python3
"""Analysis runtime: parse an artifact, extract facts, and emit a JSON record."""
from __future__ import annotations

import argparse
import email
import email.policy
import hashlib
import json
import os
import re
import subprocess
import sys
import zipfile
from email.header import decode_header, make_header

CONFIG = {
 "skill": "detonating-files-with-intezer",
 "description": "detonating files with intezer",
 "mode": "auto"
}
URL_RE = re.compile(r"https?://[^\s\"'<>\)\]]+", re.I)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
IP_RE = re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\b")
HASH_RE = re.compile(r"\b[a-fA-F0-9]{32}\b|\b[a-fA-F0-9]{40}\b|\b[a-fA-F0-9]{64}\b")
CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.I)
DOMAIN_RE = re.compile(r"\b(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,63}\b")
BASE64_RUN = re.compile(r"[A-Za-z0-9+/]{40,}={0,2}")


def read(path, mode):
    if mode == "auto":
        ext = os.path.splitext(path)[1].lower()
        mode = {".html": "html", ".htm": "html", ".docx": "docx", ".xlsx": "xlsx",
                ".pdf": "pdf", ".eml": "email", ".msg": "email", ".pcap": "pcap",
                ".pcapng": "pcap", ".json": "json", ".csv": "csv"}.get(ext, "binary"
                if ext in (".exe", ".dll", ".bin", ".so", ".elf") else "text")
    if mode == "html":
        raw = open(path, "rb").read().decode("utf-8", "replace")
        raw = re.sub(r"<script[^>]*>.*?</script>", " ", raw, flags=re.S | re.I)
        raw = re.sub(r"<style[^>]*>.*?</style>", " ", raw, flags=re.S | re.I)
        return re.sub(r"<[^>]+>", " ", raw)
    if mode in ("docx", "xlsx"):
        out = []
        with zipfile.ZipFile(path) as zf:
            for name in zf.namelist():
                if name.endswith(".xml") and ("document" in name or "sharedStrings" in name
                                              or "header" in name or "footer" in name):
                    out.append(re.sub(r"<[^>]+>", " ", zf.read(name).decode("utf-8", "replace")))
        return "\n".join(out)
    if mode == "pdf":
        try:
            return subprocess.run(["pdftotext", "-layout", path, "-"],
                                  capture_output=True, text=True, timeout=120).stdout
        except (FileNotFoundError, subprocess.TimeoutExpired):
            raw = open(path, "rb").read()
            return " ".join(x.decode("latin-1", "ignore") for x in re.findall(rb"[\x20-\x7e]{6,}", raw))
    if mode == "email":
        with open(path, "rb") as fh:
            msg = email.message_from_bytes(fh.read(), policy=email.policy.default)
        parts = []
        for part in msg.walk():
            if part.get_content_type() in ("text/plain", "text/html"):
                payload = part.get_payload(decode=True) or b""
                parts.append(payload.decode(part.get_content_charset() or "utf-8", "replace"))
        return "\n".join(parts)
    if mode == "binary":
        raw = open(path, "rb").read()
        return "\n".join(x.decode("ascii", "ignore") for x in re.findall(rb"[\x20-\x7e]{6,}", raw))
    return open(path, "rb").read().decode("utf-8", "replace")


def email_record(path):
    with open(path, "rb") as fh:
        msg = email.message_from_bytes(fh.read(), policy=email.policy.default)
    def dec(v):
        try:
            return str(make_header(decode_header(v))) if v else ""
        except Exception:  # noqa: BLE001
            return v or ""
    auth = {}
    joined = " ".join(msg.get_all("Authentication-Results") or [])
    for mech in ("spf", "dkim", "dmarc"):
        m = re.search(rf"\b{mech}\s*=\s*([a-z]+)", joined, re.I)
        auth[mech] = m.group(1).lower() if m else "none"
    attachments = []
    for part in msg.walk():
        name = part.get_filename()
        if name:
            payload = part.get_payload(decode=True) or b""
            attachments.append({"name": dec(name), "size": len(payload),
                                "sha256": hashlib.sha256(payload).hexdigest()})
    return {"headers": {"from": dec(msg.get("From")), "to": dec(msg.get("To")),
                        "subject": dec(msg.get("Subject")), "reply_to": dec(msg.get("Reply-To")),
                        "return_path": dec(msg.get("Return-Path")),
                        "message_id": dec(msg.get("Message-ID")),
                        "received": [dec(v) for v in (msg.get_all("Received") or [])]},
            "auth": auth, "attachments": attachments}


def extract(text):
    clean = BASE64_RUN.sub(" ", text)
    return {"urls": sorted({u.rstrip(".,;") for u in URL_RE.findall(clean)}),
            "emails": sorted(set(EMAIL_RE.findall(clean))),
            "ips": sorted(set(IP_RE.findall(clean))),
            "domains": sorted({d for d in DOMAIN_RE.findall(clean) if not IP_RE.match(d)}),
            "hashes": sorted(set(HASH_RE.findall(clean))),
            "cves": sorted(set(CVE_RE.findall(clean)))}


def main(config=None):
    cfg = config or CONFIG
    ap = argparse.ArgumentParser(description=cfg.get("description", "analysis"))
    ap.add_argument("--input", required=True)
    ap.add_argument("--mode", default=cfg.get("mode", "auto"),
                    choices=["auto", "text", "html", "docx", "xlsx", "pdf", "email",
                             "binary", "json", "csv"])
    ap.add_argument("--out")
    args = ap.parse_args()
    digest = hashlib.sha256(open(args.input, "rb").read()).hexdigest()
    text = read(args.input, args.mode)
    record = {"skill": cfg.get("skill", ""), "file": os.path.basename(args.input),
              "sha256": digest, "mode": args.mode,
              "size": os.path.getsize(args.input),
              "indicators": extract(text), "text_sample": text[:4000]}
    if args.mode in ("email", "auto") and args.input.lower().endswith((".eml", ".msg")):
        record["email"] = email_record(args.input)
    out = json.dumps(record, indent=1)
    if args.out:
        open(args.out, "w", encoding="utf-8").write(out)
        print(json.dumps({"written": args.out}, indent=1))
    else:
        print(out)


if __name__ == "__main__":
    main()
