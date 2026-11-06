# API Reference - Extracting Indicators from Files

## Indicator regexes

| Type | Pattern (abridged) | Notes |
|---|---|---|
| IPv4 | `\b(?:(?:25[0-5]\|2[0-4]\d\|1?\d?\d)\.){3}(?:...)\b` | Exclude 0.0.0.0/8, 127/8, 224/4 |
| IPv6 | `\b(?:[A-F0-9]{1,4}:){2,7}[A-F0-9]{1,4}\b` | Normalize with `ipaddress` |
| Domain | `\b(?:[a-z0-9-]+\.)+[a-z]{2,63}\b` | Validate with `idna` |
| URL | `https?://[^\s"'<>\)\]]+` | Strip trailing punctuation |
| Email | `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}` | |
| MD5 | `\b[a-f0-9]{32}\b` | Case-insensitive |
| SHA-1 | `\b[a-f0-9]{40}\b` | |
| SHA-256 | `\b[a-f0-9]{64}\b` | |
| CVE | `\bCVE-\d{4}-\d{4,7}\b` | |
| Registry key | `HKEY_[A-Z_]+\\[^\s"]+` | Windows |
| File path | `[A-Za-z]:\\[^\s"<>|]+` | Windows |
| Bitcoin | `\b(?:bc1|[13])[a-zA-HJ-NP-Z0-9]{25,62}\b` | |
| YARA rule | `rule\s+\w+\s*\{` | Reference only |

## Refang rules

| Defanged | Refanged |
|---|---|
| `hxxp://`, `hxxps://` | `http://`, `https://` |
| `[.]`, `(.)`, `{.}`, `[dot]`, ` dot ` | `.` |
| `[@]`, `[at]`, ` at ` | `@` |
| `[:]` | `:` |
| `[//]` | `//` |
| `\\.` | `.` |

## File-type readers

| Type | Reader | Fallback |
|---|---|---|
| `.txt`, `.log`, `.csv` | UTF-8 read | latin-1 |
| `.html`, `.htm` | `html.parser` text + attributes | regex strip tags |
| `.docx` | `zipfile` + `xml.etree` on `word/document.xml` | `strings` |
| `.xlsx` | `zipfile` + `xl/sharedStrings.xml` | `strings` |
| `.pptx` | `zipfile` + `ppt/slides/*.xml` | `strings` |
| `.pdf` | `pdftotext -layout` | printable strings + `zlib` streams |
| `.eml` | `email` parser | raw text |
| binary | ASCII + UTF-16LE strings, min length 6 | |

## Export formats

### JSON
```json
{
  "file": "report.pdf",
  "sha256": "...",
  "counts": {"ipv4": 12, "domain": 40, "url": 18, "sha256": 3},
  "indicators": [
    {"type": "domain", "value": "evil.example", "defanged": "evil[.]example",
     "confidence": 0.8, "context": "...login at evil.example..."}
  ]
}
```

### CSV
```csv
type,value,defanged,confidence,context
domain,evil.example,evil[.]example,0.8,"...login at evil.example..."
```

### STIX 2.1
```json
{
  "type": "bundle",
  "id": "bundle--<uuid>",
  "objects": [
    {"type": "indicator", "spec_version": "2.1",
     "pattern": "[domain-name:value = 'evil.example']",
     "pattern_type": "stix", "valid_from": "2026-08-31T00:00:00Z"}
  ]
}
```

## CLI

```bash
python3 scripts/agent.py extract --file sample.docx --out iocs.json
python3 scripts/agent.py extract --file report.pdf --format stix --out iocs.json
python3 scripts/agent.py extract --file page.html --allowlist allow.txt --min-confidence 0.5
python3 scripts/agent.py refang --value 'hxxps://evil[.]example[.]com/a'
python3 scripts/agent.py defang --value 'https://evil.example.com/a'
```

## Allowlist format

One entry per line; `#` starts a comment. Entries match by suffix for domains
(`example.com` also matches `mail.example.com`) and by exact value otherwise.

```
# corporate
example.com
example.org
# known-good hashes
d41d8cd98f00b204e9800998ecf8427e
```
