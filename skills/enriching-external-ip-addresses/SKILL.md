---
name: enriching-external-ip-addresses
description: >-
  Enriches external IPv4 and IPv6 addresses with geolocation, ASN and
  organization, reverse DNS, passive DNS, and reputation from AbuseIPDB,
  VirusTotal, and GreyNoise, then normalizes the results into one record with a
  transparent confidence score. Use when triaging a firewall or IDS alert,
  judging whether an IP is a scanner, proxy, or C2, preparing a block decision,
  or adding context to an incident timeline. Keywords: IP enrichment, ASN,
  geolocation, AbuseIPDB, VirusTotal, GreyNoise, passive DNS, reputation.
  Do not use for blocking the address - use blocking-malicious-ip-addresses.
  Do not use for enriching domains or file hashes - use the matching domain or
  hash enrichment skill.
domain: cybersecurity
subdomain: threat-intelligence
tags:
- threat-intelligence
- ip-reputation
- enrichment
- asn
- geolocation
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- ID.RA-01
- DE.AE-02
- RS.AN-03
mitre_attack:
- T1590.005
- T1595
- T1071
---

# Enriching External IP Addresses

## When to Use

- A firewall, IDS, or EDR alert names an external IP and you need context fast.
- You must decide whether an IP is a scanner, a proxy, a cloud egress, or C2.
- An incident timeline needs geo, ASN, and first/last-seen data.
- A block decision needs a reputation score with provenance.
- A threat-intel platform needs a normalized enrichment record.

**Do not use** for blocking the address; enrichment informs the block, it does
not perform it. **Do not use** for internal RFC 1918 addresses; those need asset
inventory and DHCP data, not internet reputation.

## Prerequisites

- API keys for the sources you enable: `ABUSEIPDB_API_KEY`, `VT_API_KEY`,
  `GREYNOISE_API_KEY`. The free tier of each is enough for triage volume.
- Outbound HTTPS to `api.abuseipdb.com`, `www.virustotal.com`,
  `api.greynoise.io`, and `ipinfo.io`.
- A cache directory so repeated lookups do not burn quota.
- An allowlist of known-good infrastructure (corporate egress, CDNs, mail).

## Workflow

### Step 1: Validate and classify the address

```bash
python3 scripts/agent.py classify --ip 203.0.113.10 --ip 2001:db8::1
```

The classifier rejects private, loopback, link-local, multicast, and
documentation ranges, and flags shared infrastructure (cloud, CDN, proxy) so
the analyst does not over-read a reputation score.

### Step 2: Enrich

```bash
export ABUSEIPDB_API_KEY=...
export VT_API_KEY=...
python3 scripts/agent.py enrich --ip 203.0.113.10 --out enrichment.json
```

| Source | Fields |
|---|---|
| ipinfo.io | city, region, country, org, ASN |
| AbuseIPDB | abuse confidence score, report count, last reported, usage type |
| VirusTotal | malicious/suspicious/harmless counts, ASN, network |
| GreyNoise | classification (benign/unknown/malicious), RIOT, last seen |
| PTR | reverse DNS name |

### Step 3: Normalize into one record

```json
{
  "ip": "203.0.113.10",
  "version": 4,
  "geo": {"country": "NL", "city": "Amsterdam", "asn": "AS64500", "org": "Example Hosting"},
  "ptr": "host.example.net",
  "reputation": {
    "abuseipdb": {"score": 100, "reports": 412, "last_reported": "2026-08-30"},
    "virustotal": {"malicious": 12, "suspicious": 2, "harmless": 60},
    "greynoise": {"classification": "malicious", "riot": false}
  },
  "context": {"shared_infrastructure": true, "cloud_provider": "Example Cloud"},
  "confidence": 0.86,
  "sources_ok": ["ipinfo", "abuseipdb", "virustotal"],
  "sources_failed": ["greynoise"]
}
```

### Step 4: Interpret carefully

| Pattern | Likely meaning |
|---|---|
| High abuse score + many reports + hosting ASN | bulletproof host or C2 |
| High abuse score + residential ASN | compromised home device |
| GreyNoise `benign` + RIOT | known benign service; do not block |
| GreyNoise `unknown` + no reports | unscored; treat as unknown, not clean |
| Cloud ASN + many domains | shared egress; block the domain, not the IP |
| PTR matches a mail provider | mail infrastructure; avoid broad blocks |

### Step 5: Cache and rate-limit

The script caches each source response for 24 hours under `--cache-dir`. Respect
the source limits: AbuseIPDB free tier is 1,000 checks/day, VirusTotal public is
4 requests/minute, GreyNoise community is rate-limited per minute. A `429`
response is recorded as `sources_failed`, not as a clean result.

### Step 6: Feed the decision

- Attach the enrichment record to the incident.
- If the IP is malicious and the activity is active, hand off to the blocking
  skill with the provenance.
- If the IP is shared infrastructure, pivot to the domain or URL instead.
- If sources disagree, keep both values and lower the confidence.

## Verification

- Every enabled source appears in either `sources_ok` or `sources_failed`.
- The confidence score is reproducible from the component scores.
- Cached responses carry the original timestamp.
- Private and reserved addresses are rejected before any API call.
- The record contains no API keys.

## Common Pitfalls

- **Treating "no reports" as clean.** A newly registered C2 has no history.
- **Ignoring shared infrastructure.** Blocking a cloud egress IP can break
  thousands of legitimate users.
- **Quota exhaustion.** Enriching a /24 one address at a time burns the daily
  limit; batch and cache.
- **Stale data.** Reputation changes; record the lookup time.
- **Confusing ASN with ownership.** The ASN owner is not always the abuse contact.
- **Leaking keys.** Never put API keys in the output or in shell history.

## References

- `references/api-reference.md` - API endpoints, fields, rate limits
- `references/standards.md` - STIX, NIST, ATT&CK mappings
- `references/workflows.md` - interpretation matrix and confidence model
- `scripts/agent.py` - classify, enrich, cache, normalize
