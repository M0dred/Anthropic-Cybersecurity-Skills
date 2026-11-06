# API Reference - Parsing Email Messages for Investigation

## Header fields that matter

| Header | Why it matters |
|---|---|
| `Received` | Hop chain; read bottom-up to find the origin |
| `Authentication-Results` | SPF, DKIM, DMARC verdicts from the receiving MTA |
| `Received-SPF` | SPF result and the client IP |
| `DKIM-Signature` | `d=` signing domain, `s=` selector, `b=` signature |
| `From` | Displayed sender; trivially spoofable |
| `Return-Path` | Envelope sender; where bounces go |
| `Reply-To` | Where a reply actually goes; BEC red flag |
| `Message-ID` | Unique ID; domain should align with the sender |
| `Date` | Claimed send time; compare with Received timestamps |
| `X-Mailer` / `User-Agent` | Sending client; useful for campaign clustering |
| `X-Originating-IP` | Client IP added by some webmail providers |
| `Content-Type` | MIME structure and boundary |

## Authentication-Results grammar

```
Authentication-Results: mx.example.com;
  spf=pass smtp.mailfrom=sender@example.org;
  dkim=pass header.d=example.org header.s=selector1;
  dmarc=pass (p=reject sp=reject) header.from=example.org
```

| Result | Meaning |
|---|---|
| `pass` | The check succeeded |
| `fail` | The check failed; possible spoofing |
| `softfail` | SPF ~all; suspicious but not definitive |
| `neutral` | No assertion |
| `none` | No record published |
| `temperror` | Transient DNS failure |
| `permerror` | Malformed record |

## MIME types to treat as dangerous

| Extension | MIME type | Risk |
|---|---|---|
| `.exe`, `.dll`, `.scr` | application/x-msdownload | direct execution |
| `.js`, `.vbs`, `.wsf`, `.hta` | application/javascript, text/vbscript | script execution |
| `.lnk` | application/x-ms-shortcut | command execution |
| `.iso`, `.img`, `.vhd` | application/octet-stream | Mark-of-the-Web bypass |
| `.docm`, `.xlsm`, `.pptm` | application/vnd.ms-office | macros |
| `.ps1` | text/plain | PowerShell |
| `.jar` | application/java-archive | execution |
| `.html`, `.htm` | text/html | credential phishing |
| `.zip`, `.rar`, `.7z` | application/zip | nested payload |

## Parser commands

```bash
# Full parse to JSON
python3 scripts/agent.py parse --file message.eml --out report.json

# Header-focused summary
python3 scripts/agent.py headers --file message.eml

# Write attachments and hash them
python3 scripts/agent.py attachments --file message.eml --out-dir ./att

# Extract and defang indicators
python3 scripts/agent.py indicators --file message.eml --json
```

## Python libraries

| Library | Use |
|---|---|
| `email` (stdlib) | MIME parsing, header decoding |
| `email.policy.default` | RFC 6532-aware parsing |
| `extract_msg` | `.msg` (Outlook) parsing; optional |
| `olefile` | OLE compound file inspection |
| `dnspython` | SPF/DKIM/DMARC DNS lookups |
| `dkimpy` | DKIM signature verification |

## Manual checks

```bash
# Decode an RFC 2047 header
python3 -c "from email.header import decode_header; print(decode_header('=?utf-8?B?...?='))"

# Show the raw headers only
sed -n '1,/^$/p' message.eml

# Count hops
grep -c '^Received:' message.eml

# Extract all URLs from the raw message
grep -oE 'https?://[^"<> ]+' message.eml | sort -u
```

## Evidence record fields

```json
{
  "file": "reported.eml",
  "sha256": "...",
  "from": "IT Support <it@example.org>",
  "return_path": "bounce@mailer.example.net",
  "reply_to": "helpdesk@example.com",
  "message_id": "<...@example.org>",
  "auth": {"spf": "fail", "dkim": "none", "dmarc": "fail"},
  "received_hops": 4,
  "attachments": [{"name": "invoice.docm", "sha256": "...", "dangerous": true}],
  "urls": ["hxxps://example[.]org/login"],
  "verdict": "malicious"
}
```
