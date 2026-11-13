# Workflows - Exporting Indicators to a SIEM

## Pipeline

```
select -> normalize -> allowlist filter -> publish -> verify -> monitor
```

## Selection rules

| Rule | Example |
|---|---|
| Source allowlist | only feeds with a known reliability |
| Reputation floor | `bad` or `suspicious` only |
| Type filter | `ip`, `domain`, `url`, `file` |
| Age | first seen within 90 days |
| Expiry | not expired |
| Size cap | 100k lines for an EDL |

## Publish targets

| Target | Transport | Refresh |
|---|---|---|
| PAN-OS EDL | HTTPS pull | 5 min |
| Splunk lookup | REST upload | 15 min |
| Sentinel watchlist | Azure API | 15 min |
| QRadar reference set | REST bulk load | 15 min |
| Proxy category | vendor API | 1 hour |

## Verification

```bash
# Local count
wc -l blocklist.csv

# Consumer count
curl -sS https://edl.example.com/blocklist.csv | wc -l

# Spot check
grep -c '203.0.113.10' blocklist.csv
```

## Monitoring alerts

- Export count changed by more than 30%.
- Export older than twice the refresh interval.
- Consumer count differs by more than 5%.
- Publish returned a non-2xx status.
- The previous export is missing.

## Rollback

Keep the last three exports with timestamps. To roll back, republish the previous
file and verify the consumer count matches. Record the rollback in the incident.

## Record template

```
Pipeline:    TIM -> EDL -> PAN-OS
Query:       sourceBrands:"Bambenek" AND type:IP AND reputation:Bad
Export:      blocklist.csv, 1,204 lines, 2026-08-31T10:00Z
Published:   https://edl.example.com/blocklist.csv
Consumer:    PAN-OS external-list statistics, 1,204 entries
Verified:    known-bad present, known-good absent
Owner:       soc@example.com
Review:      2026-09-30
```
