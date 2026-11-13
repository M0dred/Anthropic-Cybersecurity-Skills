---
name: exporting-indicators-to-siem
description: >-
  Builds a one-way indicator export pipeline from a threat-intelligence store to
  a SIEM, EDL, or firewall: select indicators by source, type, and reputation,
  normalize them, publish them in CSV, STIX, or a plain list, and verify that the
  consumer is ingesting the feed. Use when a SIEM needs an updated blocklist,
  when a firewall EDL must be refreshed from threat intelligence, when a SOC
  wants a reproducible indicator export instead of manual copy-paste, or when an
  export pipeline has silently stopped updating. Keywords: EDL, indicator
  export, threat intel to SIEM, blocklist, CSV, STIX, feed pipeline.
  Do not use for ingesting a feed into the intelligence store - use
  analyzing-threat-intelligence-feeds. Do not use for blocking a single
  indicator - use blocking-malicious-ip-addresses.
domain: cybersecurity
subdomain: threat-intelligence
tags:
- threat-intelligence
- siem
- edl
- integration
- soc-operations
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- ID.RA-01
- DE.CM-01
- RS.MI-01
mitre_attack:
- T1588.001
- T1071
- T1105
---

# Exporting Indicators to a SIEM

## When to Use

- A SIEM, firewall, or proxy consumes a blocklist that must be refreshed.
- Threat intelligence is curated in one platform but enforced in another.
- An export pipeline exists but the consumer has stale or empty data.
- A SOC needs a reproducible, auditable indicator export.

**Do not use** for ingesting a feed into the intelligence store; that is the
reverse direction. **Do not use** for blocking a single indicator by hand; use
the matching blocking skill.

## Prerequisites

- Read access to the intelligence store and a query language that can filter by
  source, indicator type, and reputation.
- A consumer endpoint: SIEM lookup table, firewall EDL URL, or proxy category.
- A stable export URL or file path, and a transport the consumer supports
  (HTTP pull, SCP, S3, or API push).
- A retention and rollback plan: the previous export must be recoverable.

## Workflow

### Step 1: Define the selection query

```text
sourceBrands:"Bambenek Consulting Feed" AND type:IP AND (reputation:Bad OR reputation:Suspicious)
```

Rules that keep the export useful:

| Rule | Reason |
|---|---|
| Only `Bad` or `Suspicious` reputation | Avoid exporting everything |
| Exclude allowlisted indicators | Prevent blocking business traffic |
| Exclude private and reserved ranges | They are not routable on the internet |
| Include an expiry | Stale indicators rot the blocklist |
| Cap the size | Consumers have line and memory limits |

### Step 2: Normalize the output

| Format | Use when |
|---|---|
| Plain list | Firewall EDL expects one value per line |
| CSV | SIEM lookup table with columns |
| STIX 2.1 | Downstream TIP or sharing community |
| JSON | Custom consumer with a schema |

Keep a stable column order and a header row. The consumer will break silently if
the schema changes.

### Step 3: Publish

```bash
# Generate the export locally
python3 scripts/agent.py export --input indicators.json --format csv --out blocklist.csv

# Publish to an HTTP EDL endpoint
python3 scripts/agent.py publish --file blocklist.csv --url https://edl.example.com/blocklist.csv

# Or push to a SIEM lookup table
python3 scripts/agent.py push --file blocklist.csv --siem splunk --lookup threat_intel_blocklist
```

### Step 4: Verify ingestion on the consumer

```bash
# Splunk lookup
| inputlookup threat_intel_blocklist | stats count

# Check the EDL response
curl -sS https://edl.example.com/blocklist.csv | wc -l

# Firewall EDL status
show external-list statistics
```

Compare the consumer count with the export count. A mismatch means the consumer
is caching, truncating, or rejecting lines.

### Step 5: Monitor freshness

- Record the export timestamp and the indicator count.
- Alert when the count drops by more than 30% or the timestamp is older than the
  refresh interval.
- Keep the last three exports for rollback.

## Verification

- The consumer count matches the export count within an accepted delta.
- A known-bad indicator from the export is present on the consumer.
- A known-good indicator is absent.
- The export timestamp is current.
- The previous export is still available for rollback.

## Common Pitfalls

- **Exporting everything.** A blocklist with millions of entries slows the
  consumer and produces false positives.
- **No allowlist.** Corporate domains and CDN ranges end up blocked.
- **Schema drift.** Adding a column breaks the consumer parser.
- **Silent failure.** The pipeline stops and nobody notices until an incident.
- **No expiry.** Indicators stay in the blocklist long after the campaign ends.
- **Line-ending changes.** CRLF vs LF breaks some EDL parsers.

## References

- `references/api-reference.md` - export formats and consumer APIs
- `references/standards.md` - STIX, TAXII, NIST mappings
- `references/workflows.md` - pipeline design and monitoring
- `scripts/agent.py` - export, publish, push, verify
