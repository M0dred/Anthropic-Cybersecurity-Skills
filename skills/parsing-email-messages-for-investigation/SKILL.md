---
name: parsing-email-messages-for-investigation
description: >-
  Parses .eml and .msg email files into a normalized investigation record:
  full Received chain, SPF/DKIM/DMARC results, Message-ID and Return-Path,
  Reply-To mismatches, body text and HTML, attachment names, types and SHA-256
  hashes, embedded URLs, and nested attached messages. Use when triaging a
  reported phishing email, verifying sender authenticity, extracting
  attachments for sandbox analysis, or building an email evidence record.
  Keywords: parse eml, parse msg, email headers, Received chain, SPF, DKIM,
  DMARC, attachment hash, phishing triage.
  Do not use for analyzing Outlook PST archives - use
  analyzing-outlook-pst-for-email-forensics. Do not use for writing detection
  rules against email gateways - use detecting-spearphishing-with-email-gateway.
domain: cybersecurity
subdomain: phishing-defense
tags:
- phishing
- email-forensics
- eml
- msg
- header-analysis
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.AN-03
- DE.AE-02
- PR.AT-01
mitre_attack:
- T1566.001
- T1566.002
- T1204.002
---

# Parsing Email Messages for Investigation

## When to Use

- A user reports a suspicious email and you need the facts before judging it.
- You must verify SPF, DKIM, and DMARC results from the raw headers.
- An attachment needs a hash and type before sandbox submission.
- A nested or forwarded message hides the original sender.
- An incident timeline needs the exact Received chain and timestamps.

**Do not use** for PST/OST mailbox extraction; that needs a mailbox parser and
custodian scoping. **Do not use** for tuning the mail gateway; that is a
detection-engineering task on gateway logs, not a message parse.

## Prerequisites

- The original message as a file (`.eml`, `.msg`) or raw MIME text. Forwarded
  copies lose the original headers; always ask for the source message.
- Python 3.9+ for the helper script; no third-party packages required.
- A sandbox or static-analysis pipeline for attachments you decide to open.
- A hash allowlist so known-good corporate attachments do not create noise.

## Workflow

### Step 1: Acquire the message without altering it

```bash
# From a mailbox export, a gateway quarantine, or a user submission
sha256sum reported.eml > reported.eml.sha256
cp reported.eml /evidence/INC-1234/
```

Never open an attachment on the analyst workstation. Parse first, detonate in a
sandbox second.

### Step 2: Parse the message

```bash
python3 scripts/agent.py parse --file reported.eml --out report.json
```

The parser returns:

| Field | Meaning |
|---|---|
| `headers.received` | Ordered hop chain, oldest last |
| `auth.spf` / `auth.dkim` / `auth.dmarc` | Authentication-Results values |
| `headers.from` / `headers.return_path` | Envelope vs header sender |
| `headers.reply_to` | Where a reply would actually go |
| `headers.message_id` | Unique message identifier |
| `body.text` / `body.html` | Decoded bodies |
| `attachments[]` | Name, MIME type, size, SHA-256, whether executable |
| `urls[]` | URLs from body and HTML, defanged |
| `nested[]` | Attached messages parsed recursively |

### Step 3: Judge sender authenticity

```bash
python3 scripts/agent.py headers --file reported.eml
```

Check, in order:

1. **SPF** — does the sending IP belong to the envelope domain?
2. **DKIM** — is the signature valid and does the `d=` domain align with From?
3. **DMARC** — is the alignment `pass`, and what is the policy?
4. **Return-Path vs From** — a mismatch is common in bulk mail but suspicious
   when combined with a failed DMARC.
5. **Reply-To** — a Reply-To on a different domain than From is the classic
   business-email-compromise pattern.
6. **Received chain** — the first hop should be the sender's infrastructure; a
   private IP or an unexpected relay indicates spoofing or a compromised host.
7. **Message-ID** — a Message-ID domain that does not match From is a weak but
   useful signal.

### Step 4: Extract and hash attachments

```bash
python3 scripts/agent.py attachments --file reported.eml --out-dir /evidence/INC-1234/att
```

The script writes each attachment to disk and prints a JSON manifest with the
SHA-256. Submit the hash to the sandbox before opening the file. Flag executable
and macro-bearing types: `.exe`, `.dll`, `.js`, `.vbs`, `.lnk`, `.iso`, `.img`,
`.docm`, `.xlsm`, `.hta`, `.ps1`, `.scr`, `.jar`.

### Step 5: Extract indicators

```bash
python3 scripts/agent.py indicators --file reported.eml --json
```

Extract URLs, domains, IPs, and email addresses from the body, the HTML, and
the headers. Defang before sharing: `hxxps://`, `[.]`, `[@]`. Keep the original
value alongside the defanged one in the evidence record.

### Step 6: Decide and record

| Signal | Verdict |
|---|---|
| DMARC fail + Reply-To mismatch + credential lure | malicious |
| Valid auth + known vendor + expected attachment | benign |
| Valid auth + unusual payment request | business-email-compromise suspicion |
| Unsigned + first contact + archive attachment | high risk, sandbox it |

Write the verdict, the evidence fields, and the attachment hashes into the
incident. The parse report is the evidence; do not paraphrase it away.

## Verification

- The parsed `Received` chain is in the same order as the raw headers.
- `auth.*` values match the `Authentication-Results` header exactly.
- Every attachment hash in the report matches `sha256sum` of the written file.
- Nested messages are parsed to the configured depth and their attachments are
  hashed too.
- URLs are defanged in the report and preserved verbatim in a separate field.

## Common Pitfalls

- **Forwarded messages.** A forward rewrites headers; the original is lost.
- **HTML-only bodies.** Text extraction misses the tracking URL; parse both.
- **Encoded headers.** RFC 2047 encoded words (`=?utf-8?B?...?=`) hide the real
  subject and display name; decode them.
- **Attachment name spoofing.** The declared MIME type and the magic bytes often
  disagree; trust the magic bytes.
- **Nested message bombs.** Cap recursion depth and total size.
- **Assuming DMARC fail means spoofing.** Forwarding lists and some senders
  legitimately fail alignment.

## References

- `references/api-reference.md` - header fields, MIME types, parser commands
- `references/standards.md` - RFC 5322, 7208, 6376, 7489, NIST mappings
- `references/workflows.md` - triage decision tree and evidence template
- `scripts/agent.py` - parse, headers, attachments, indicators
