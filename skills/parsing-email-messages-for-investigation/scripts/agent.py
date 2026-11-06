#!/usr/bin/env python3
"""Parse .eml/.msg email files for phishing and incident investigation.

Subcommands:
    parse        Full JSON record (headers, auth, bodies, attachments, IOCs).
    headers      Header and authentication summary.
    attachments  Write attachments to a directory and hash them.
    indicators   Extract and defang URLs, domains, IPs, and email addresses.

Examples:
    python3 agent.py parse --file reported.eml --out report.json
    python3 agent.py headers --file reported.eml
    python3 agent.py attachments --file reported.eml --out-dir ./att
    python3 agent.py indicators --file reported.eml --json
"""
from __future__ import annotations

import argparse
import email
import email.policy
import hashlib
import json
import os
import re
import sys
from email.header import decode_header, make_header

URL_RE = re.compile(r"https?://[^\s\"'<>\)\]]+", re.I)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
IPV4_RE = re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\b")
DOMAIN_RE = re.compile(r"\b(?:[a-z0-9](?:[a-z0-9\-]{0,61}[a-z0-9])?\.)+(?:com|net|org|io|co|ru|cn|info|biz|xyz|top|club|online|site|shop|live|app|dev|me|us|uk|de|fr|jp|br|in|au|ca|nl|se|no|fi|pl|cz|tr|kr|tw|hk|sg|za|mx|es|it|ch|at|be|dk|ie|nz|ar|cl|pe|co|ve|ec|uy|py|bo|do|gt|sv|hn|ni|cr|pa|pr|tt|jm|bs|bb|gd|lc|vc|ag|dm|kn|ai|vg|tc|cx|cc|ws|tv|fm|am|la|to|nu|tk|ml|ga|cf|gq)\b", re.I)
HASH_RE = re.compile(r"\b(?:[a-f0-9]{32}|[a-f0-9]{40}|[a-f0-9]{64})\b", re.I)
CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b", re.I)

DANGEROUS = {".exe", ".dll", ".scr", ".js", ".vbs", ".wsf", ".hta", ".lnk",
             ".iso", ".img", ".vhd", ".docm", ".xlsm", ".pptm", ".ps1",
             ".jar", ".bat", ".cmd", ".com", ".pif", ".msi", ".reg"}


def decode(value):
    if value is None:
        return ""
    try:
        return str(make_header(decode_header(value)))
    except Exception:  # noqa: BLE001 - malformed headers are common
        return str(value)


def defang(value):
    return (value.replace("http://", "hxxp://").replace("https://", "hxxps://")
            .replace(".", "[.]").replace("@", "[@]"))


def load_message(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    if path.lower().endswith(".msg"):
        try:
            import extract_msg  # type: ignore
        except ImportError as exc:
            raise SystemExit("install extract_msg for .msg support: pip install extract-msg") from exc
        msg = extract_msg.Message(path)
        return email.message_from_string(str(msg.asEmailMessage()), policy=email.policy.default), raw
    return email.message_from_bytes(raw, policy=email.policy.default), raw


def walk_parts(msg, depth=0, max_depth=3, path="root"):
    """Yield (part, depth, path) for every MIME part, including nested messages."""
    if depth > max_depth:
        return
    if msg.is_multipart():
        for index, part in enumerate(msg.iter_parts()):
            child = f"{path}.{index}"
            if part.get_content_type() == "message/rfc822":
                payload = part.get_payload()
                nested = payload[0] if isinstance(payload, list) and payload else None
                if nested is not None:
                    yield nested, depth + 1, child
                    yield from walk_parts(nested, depth + 1, max_depth, child)
            else:
                yield part, depth, child
                if part.is_multipart():
                    yield from walk_parts(part, depth, max_depth, child)
    else:
        yield msg, depth, path


def auth_results(msg):
    values = msg.get_all("Authentication-Results") or []
    joined = " ".join(values)
    out = {}
    for mech in ("spf", "dkim", "dmarc"):
        match = re.search(rf"\b{mech}\s*=\s*([a-z]+)", joined, re.I)
        out[mech] = match.group(1).lower() if match else "none"
    return out


def parse(path, max_depth=3):
    msg, raw = load_message(path)
    body_text, body_html = [], []
    attachments, nested = [], []
    for part, depth, part_path in walk_parts(msg, max_depth=max_depth):
        ctype = part.get_content_type()
        if ctype == "message/rfc822":
            continue
        filename = part.get_filename()
        payload = part.get_payload(decode=True)
        if filename:
            digest = hashlib.sha256(payload or b"").hexdigest()
            ext = os.path.splitext(filename)[1].lower()
            attachments.append({"name": decode(filename), "mime": ctype,
                                "size": len(payload or b""), "sha256": digest,
                                "dangerous": ext in DANGEROUS, "depth": depth,
                                "path": part_path})
            continue
        if payload is None:
            continue
        text = payload.decode(part.get_content_charset() or "utf-8", errors="replace")
        if ctype == "text/plain":
            body_text.append(text)
        elif ctype == "text/html":
            body_html.append(text)
    text = "\n".join(body_text)
    html = "\n".join(body_html)
    combined = text + "\n" + html
    urls = sorted({u.rstrip(".,;") for u in URL_RE.findall(combined)})
    record = {
        "file": os.path.basename(path),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "headers": {
            "from": decode(msg.get("From")),
            "to": decode(msg.get("To")),
            "cc": decode(msg.get("Cc")),
            "subject": decode(msg.get("Subject")),
            "date": decode(msg.get("Date")),
            "return_path": decode(msg.get("Return-Path")),
            "reply_to": decode(msg.get("Reply-To")),
            "message_id": decode(msg.get("Message-ID")),
            "received": [decode(v) for v in (msg.get_all("Received") or [])],
        },
        "auth": auth_results(msg),
        "body": {"text": text[:20000], "html": html[:20000]},
        "attachments": attachments,
        "urls": urls,
        "urls_defanged": [defang(u) for u in urls],
        "indicators": extract_indicators(combined),
    }
    return record


def extract_indicators(text):
    return {
        "urls": sorted({u.rstrip(".,;") for u in URL_RE.findall(text)}),
        "emails": sorted(set(EMAIL_RE.findall(text))),
        "ips": sorted(set(IPV4_RE.findall(text))),
        "domains": sorted({d for d in DOMAIN_RE.findall(text) if not IPV4_RE.match(d)}),
        "hashes": sorted(set(HASH_RE.findall(text))),
        "cves": sorted(set(CVE_RE.findall(text))),
    }


def write_attachments(path, out_dir, max_depth=3):
    msg, _ = load_message(path)
    os.makedirs(out_dir, exist_ok=True)
    manifest = []
    for part, depth, part_path in walk_parts(msg, max_depth=max_depth):
        filename = part.get_filename()
        if not filename:
            continue
        payload = part.get_payload(decode=True) or b""
        safe = re.sub(r"[^A-Za-z0-9._-]", "_", decode(filename)) or "attachment"
        target = os.path.join(out_dir, f"{len(manifest):02d}_{safe}")
        with open(target, "wb") as handle:
            handle.write(payload)
        manifest.append({"file": target, "name": decode(filename),
                         "sha256": hashlib.sha256(payload).hexdigest(),
                         "size": len(payload), "depth": depth})
    return manifest


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", choices=["parse", "headers", "attachments", "indicators"])
    ap.add_argument("--file", required=True)
    ap.add_argument("--out")
    ap.add_argument("--out-dir", default="./attachments")
    ap.add_argument("--max-depth", type=int, default=3)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.action == "parse":
        record = parse(args.file, args.max_depth)
        text = json.dumps(record, indent=1)
        if args.out:
            with open(args.out, "w", encoding="utf-8") as handle:
                handle.write(text)
            print(json.dumps({"written": args.out, "attachments": len(record["attachments"]),
                              "urls": len(record["urls"])}, indent=1))
        else:
            print(text)
    elif args.action == "headers":
        record = parse(args.file, args.max_depth)
        print(json.dumps({"headers": record["headers"], "auth": record["auth"]}, indent=1))
    elif args.action == "attachments":
        print(json.dumps(write_attachments(args.file, args.out_dir, args.max_depth), indent=1))
    else:
        record = parse(args.file, args.max_depth)
        ind = record["indicators"]
        ind["urls_defanged"] = [defang(u) for u in ind["urls"]]
        print(json.dumps(ind, indent=1))


if __name__ == "__main__":
    main()
