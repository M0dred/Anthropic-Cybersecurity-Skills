# Workflows - Extracting Indicators from Files

## Pipeline

```
hash file -> detect type -> read content -> refang copy -> regex extract
-> normalize -> allowlist filter -> score -> dedupe -> export -> hand off
```

## Type detection

```bash
file suspicious.docx
xxd -l 16 suspicious.docx
# PK.. -> zip-based (docx/xlsx/pptx)
# %PDF -> pdf
# MZ   -> pe binary
# <html -> html
```

## Extraction by content type

| Content | Command |
|---|---|
| Text | `python3 agent.py extract --file a.txt --mode text` |
| HTML | `python3 agent.py extract --file a.html --mode html` |
| DOCX | `python3 agent.py extract --file a.docx --mode docx` |
| PDF | `pdftotext -layout a.pdf - \| python3 agent.py extract --file - --mode text` |
| Binary | `strings -n 6 a.bin \| python3 agent.py extract --file - --mode text` |

## Normalization rules

- Lowercase domains and hostnames.
- Strip trailing `.`, `,`, `;`, `)`, `]` from URLs.
- Convert IPv6 to compressed lowercase form.
- Lowercase hashes.
- Decode punycode to Unicode for display, keep punycode for matching.
- Reject values inside base64 runs longer than 40 characters.

## Allowlist strategy

1. Corporate domains and all subdomains.
2. Major CDNs and cloud providers (unless the incident is about them).
3. Common software update domains.
4. Known-good hashes from the software inventory.
5. RFC 1918 and documentation ranges for IPs.

## Hand-off matrix

| Indicator | Destination |
|---|---|
| File hash | Sandbox, EDR blocklist |
| Domain | DNS sinkhole, proxy |
| URL | Proxy, mail gateway |
| IP | Firewall, threat-intel platform |
| Email address | Mail gateway, awareness team |
| Registry key | EDR hunting query |
| CVE | Vulnerability management |

## Evidence record

```
File:        report.pdf
SHA-256:     ...
Extracted:   2026-08-31T10:00Z by analyst@example.com
Counts:      ipv4=12 domain=40 url=18 sha256=3
Allowlist:   allowlist.txt (sha256 ...)
Tool:        agent.py v1.0
Output:      iocs.json
```
