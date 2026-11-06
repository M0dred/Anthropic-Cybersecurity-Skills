# Workflows - Parsing Email Messages for Investigation

## Triage decision tree

```
Is the message authenticated (SPF+DKIM+DMARC pass, aligned)?
├─ yes -> Does the content ask for credentials, payment, or a file open?
│         ├─ yes -> BEC / phishing suspicion; verify by out-of-band call
│         └─ no  -> likely benign; close with the parse report
└─ no  -> Does Reply-To or Return-Path differ from From?
          ├─ yes -> spoofing or BEC; treat as malicious
          └─ no  -> Check attachments and URLs
                    ├─ dangerous attachment -> sandbox, then verdict
                    ├─ credential-harvesting URL -> malicious
                    └─ no payload -> low confidence; monitor
```

## Evidence-first sequence

1. Save the original file and hash it.
2. Parse headers and bodies; do not open attachments.
3. Hash attachments; submit hashes to the sandbox.
4. Extract and defang indicators.
5. Correlate with mail-gateway logs (sender IP, recipient list, delivery time).
6. Write the verdict and the evidence fields into the incident.

## Header analysis order

| Order | Check | Failure means |
|---|---|---|
| 1 | SPF | sending IP not authorized for the envelope domain |
| 2 | DKIM | body or headers altered, or signature domain mismatch |
| 3 | DMARC | alignment failure; policy decides action |
| 4 | Return-Path vs From | envelope spoofing or bulk sender |
| 5 | Reply-To vs From | reply diversion (BEC) |
| 6 | Received chain | unexpected relay or private IP |
| 7 | Message-ID | weak sender-consistency signal |
| 8 | Date vs Received | delayed or replayed message |

## Attachment handling

```bash
# Hash before opening
python3 scripts/agent.py attachments --file message.eml --out-dir ./att
sha256sum ./att/*

# Static checks
file ./att/*
strings -n 8 ./att/sample.docm | head -50
olevba ./att/sample.docm          # oletools
pdfid ./att/sample.pdf            # pdfid
```

## Nested message handling

- Parse attached `message/rfc822` parts recursively.
- Cap depth (default 3) and total size (default 50 MB).
- Record the nesting path, e.g. `outer -> attached.eml -> inner.eml`.

## Incident record template

```
Incident:      INC-1234
Reporter:      user@example.com
Message file:  reported.eml (sha256 ...)
From:          IT Support <it@example.org>
Return-Path:   bounce@mailer.example.net
Reply-To:      helpdesk@example.com
Auth:          spf=fail dkim=none dmarc=fail
Attachments:   invoice.docm (sha256 ..., macro-enabled)
URLs:          hxxps://example[.]org/login
Verdict:       malicious - credential phishing
Actions:       message purged, URL blocked, user reset, awareness note sent
```
