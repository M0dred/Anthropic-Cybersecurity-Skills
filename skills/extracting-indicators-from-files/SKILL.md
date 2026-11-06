---
name: extracting-indicators-from-files
description: >-
  Extracts and normalizes indicators of compromise from unstructured files:
  plain text, HTML, Word documents, PDFs, and binary blobs. Recovers IPv4/IPv6
  addresses, domains, URLs, email addresses, MD5/SHA-1/SHA-256 hashes, CVE IDs,
  registry keys, file paths, and cryptocurrency addresses, then refangs,
  de-duplicates, filters allowlists, and assigns a confidence score. Use when
  triaging a suspicious document, mining a threat report, processing an email
  attachment, or building an IOC feed from collected evidence. Keywords: IOC
  extraction, defang, refang, regex, threat report, document analysis.
  Do not use for extracting indicators from email headers and bodies - use
  parsing-email-messages-for-investigation. Do not use for enriching the
  extracted indicators with reputation data - use enriching-external-ip-addresses.
domain: cybersecurity
subdomain: threat-intelligence
tags:
- threat-intelligence
- ioc
- extraction
- defang
- document-analysis
- malware-analysis
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- ID.RA-01
- DE.AE-02
- RS.AN-03
mitre_attack:
- T1588.001
- T1204.002
- T1027
---

# Extracting Indicators from Files

## When to Use

- A suspicious document, PDF, or HTML file needs indicators before analysis.
- A threat report or blog post must be turned into a machine-readable IOC list.
- An email attachment contains URLs, domains, or hashes worth pivoting on.
- A binary's strings need a first-pass indicator sweep.
- A detection team needs a de-duplicated, allowlist-filtered IOC export.

**Do not use** for parsing email headers and MIME structure; that is a different
parser with different evidence rules. **Do not use** for judging whether an
indicator is malicious; extraction is not enrichment.

## Prerequisites

- The file, copied to an evidence directory with a SHA-256 recorded.
- An allowlist of corporate domains, CDN ranges, and known-good hashes.
- Python 3.9+; the helper uses only the standard library.
- For PDFs, `pdftotext` (poppler-utils) improves recall; the script falls back
  to raw string extraction.

## Workflow

### Step 1: Record the file hash before extraction

```bash
sha256sum suspicious.docx | tee suspicious.docx.sha256
```

The file hash is itself an indicator and the anchor for the evidence record.

### Step 2: Extract by file type

```bash
# Auto-detect and extract
python3 scripts/agent.py extract --file suspicious.docx --out iocs.json

# Force a mode when detection is wrong
python3 scripts/agent.py extract --file sample.bin --mode binary --out iocs.json

# Text and HTML
python3 scripts/agent.py extract --file page.html --mode html
```

| Mode | How it reads |
|---|---|
| `text` | UTF-8 with replacement, line by line |
| `html` | Strips tags, decodes entities, keeps href/src values |
| `docx` | Unzips `word/document.xml` and header/footer parts |
| `pdf` | `pdftotext` if present, else printable-string sweep |
| `binary` | Printable ASCII and UTF-16LE strings, minimum length 6 |

### Step 3: Refang before matching

Attackers defang indicators in documents (`hxxp://`, `example[.]com`,
`user[@]example[.]com`). The extractor refangs a copy for matching and keeps
the original string for the evidence record.

```bash
python3 scripts/agent.py refang --value 'hxxps://evil[.]example[.]com/a'
# -> https://evil.example.com/a
```

### Step 4: Filter and score

```bash
python3 scripts/agent.py extract --file report.pdf \
  --allowlist allowlist.txt --min-confidence 0.5 --out iocs.json
```

Confidence heuristics:

| Signal | Effect |
|---|---|
| Appears in a URL path or query | +0.1 |
| Appears in an attachment name | +0.1 |
| Matches a known-bad TLD or free-hosting domain | +0.1 |
| Is a private or reserved IP | -0.5 (usually infrastructure noise) |
| Is on the allowlist | excluded |
| Appears once in a large document | -0.1 |
| Appears in a CVE or vendor context | -0.2 (often a reference) |

### Step 5: De-duplicate and export

```bash
python3 scripts/agent.py extract --file report.pdf --format csv --out iocs.csv
python3 scripts/agent.py extract --file report.pdf --format stix --out iocs.json
```

The JSON export groups indicators by type and keeps first-seen context (the
surrounding 80 characters), which is what an analyst needs to judge a hit.

### Step 6: Hand off

- Send hashes to the sandbox and the EDR blocklist.
- Send domains and URLs to the proxy and DNS sinkhole.
- Send IPs to the firewall team with provenance.
- Attach the extraction report to the incident.

## Verification

- The number of unique indicators matches a manual `grep -o` count on a sample.
- Defanged and refanged forms are both present in the report.
- Allowlisted values are absent from the output.
- Private and reserved IPs are flagged, not silently dropped.
- The file SHA-256 in the report matches `sha256sum`.

## Common Pitfalls

- **Matching inside base64.** Base64 blobs produce false domains; strip long
  base64 runs before matching.
- **HTML entities.** `&#46;` and `&period;` hide dots; decode entities first.
- **PDF compression.** Raw PDF streams are compressed; use `pdftotext` or
  decompress with `zlib`.
- **Unicode homoglyphs.** Cyrillic `а` looks like Latin `a`; normalize with
  NFKC and flag mixed-script labels.
- **Over-extraction.** A 200-page report yields thousands of benign vendor
  domains; always allowlist and score.
- **No context.** An indicator without its surrounding text cannot be judged.

## References

- `references/api-reference.md` - regexes, refang rules, export formats
- `references/standards.md` - STIX 2.1, MISP, NIST mappings
- `references/workflows.md` - extraction pipeline and confidence model
- `scripts/agent.py` - extract, refang, filter, export
