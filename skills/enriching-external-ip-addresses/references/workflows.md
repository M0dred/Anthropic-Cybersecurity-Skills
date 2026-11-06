# Workflows - Enriching External IP Addresses

## Triage sequence

```
validate -> classify -> enrich -> normalize -> interpret -> decide -> record
```

## Interpretation matrix

| AbuseIPDB | VirusTotal | GreyNoise | Likely meaning | Action |
|---|---|---|---|---|
| >= 80 | >= 5 | malicious | confirmed malicious | block, hunt |
| >= 80 | 0 | unknown | abuse reports only | investigate further |
| 0 | 0 | benign + RIOT | known service | do not block |
| 0 | 0 | unknown | unscored | treat as unknown |
| any | any | riot | common business service | allowlist candidate |
| high | high | benign | conflict | keep both, lower confidence |

## Shared infrastructure check

| Signal | Interpretation |
|---|---|
| ASN owner is a cloud provider | shared egress; block the domain or URL |
| PTR ends in a CDN domain | shared edge; do not block the IP |
| Many domains resolve to the IP | shared hosting; pivot to the domain |
| ASN is a residential ISP | likely a compromised device |

## Confidence calculation

```python
score = 0.0
if abuse_score >= 80: score += 0.30
if vt_malicious >= 5: score += 0.25
if greynoise == "malicious": score += 0.25
if hosting_asn: score += 0.10
if ptr_mismatch: score += 0.05
if sources_agree: score += 0.05
score = min(score, 1.0)
if sources_ok < 2: score = min(score, 0.5)
```

## Caching

- Cache key: `source:ip`.
- TTL: 24 hours for reputation, 7 days for geo/ASN.
- Store the response body and the lookup timestamp.
- On `429`, serve the cached value if present and mark it stale.

## Incident record template

```
Incident:    INC-1234
IP:          203.0.113.10
Geo/ASN:     NL, AS64500 Example Hosting
PTR:         host.example.net
AbuseIPDB:   100 (412 reports, last 2026-08-30)
VirusTotal:  12 malicious / 2 suspicious
GreyNoise:   malicious, RIOT false
Confidence:  0.86
Decision:    block at perimeter and host; hunt for the same ASN
```

## Batch enrichment

```bash
# Enrich a list, respecting rate limits
while read ip; do
  python3 scripts/agent.py enrich --ip "$ip" --out "out/$ip.json"
  sleep 1
done < ips.txt
```

For more than a few hundred addresses, use the bulk endpoints or a commercial
feed rather than looping the free tiers.
