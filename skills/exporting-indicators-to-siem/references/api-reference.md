# API Reference - Exporting Indicators to a SIEM

## Export formats

### Plain list (EDL)
```
203.0.113.10
198.51.100.7
evil.example
```
One value per line, LF line endings, no header.

### CSV (SIEM lookup)
```csv
indicator,type,reputation,source,first_seen,expires
203.0.113.10,ip,bad,Bambenek,2026-08-01,2026-09-01
evil.example,domain,suspicious,Anomali,2026-08-02,2026-09-02
```

### STIX 2.1
```json
{
  "type": "bundle",
  "id": "bundle--<uuid>",
  "objects": [
    {"type": "indicator", "spec_version": "2.1",
     "pattern": "[ipv4-addr:value = '203.0.113.10']",
     "pattern_type": "stix", "valid_from": "2026-08-01T00:00:00Z"}
  ]
}
```

## Consumer APIs

### Splunk lookup table
```bash
curl -k -u admin:$SPLUNK_PASS \
  https://splunk:8089/servicesNS/nobody/search/data/lookup-table-files/threat_intel_blocklist \
  -F "eai:data=@blocklist.csv"
```

### Microsoft Sentinel watchlist
```bash
az sentinel watchlist create --resource-group rg-soc --workspace-name ws-soc \
  --watchlist-alias threat_intel --display-name "Threat Intel" \
  --provider "SOC" --source "Local file" --raw-content blocklist.csv
```

### QRadar reference set
```bash
curl -X POST "https://qradar/api/reference_data/sets/bulk_load/threat_intel" \
  -H "SEC: $QRADAR_TOKEN" -H "Content-Type: application/json" \
  -d '["203.0.113.10","198.51.100.7"]'
```

### Firewall EDL (PAN-OS)
```bash
# The firewall pulls the list; publish it at a stable URL
curl -X PUT "https://edl.example.com/blocklist.txt" --data-binary @blocklist.txt
```

## CLI

```bash
python3 scripts/agent.py export --input indicators.json --format csv --out blocklist.csv
python3 scripts/agent.py publish --file blocklist.csv --url https://edl.example.com/blocklist.csv
python3 scripts/agent.py push --file blocklist.csv --siem splunk --lookup threat_intel_blocklist
python3 scripts/agent.py verify --url https://edl.example.com/blocklist.csv --expected 1200
```

## Selection query examples

| Store | Query |
|---|---|
| Splunk ES | `\| tstats count from datamodel=Threat_Intelligence where ...` |
| Elastic | `{"query":{"terms":{"threat.indicator.type":["ipv4-addr"]}}}` |
| MISP | `attributes/restSearch` with `to_ids:1` |
| OpenCTI | GraphQL `indicators(filters: ...)` |
| STIX/TAXII | `GET /collections/<id>/objects?match[type]=indicator` |

## Monitoring

| Signal | Threshold |
|---|---|
| Export count drop | > 30% vs previous run |
| Export age | > 2x refresh interval |
| Consumer count mismatch | > 5% |
| Parse errors | any |
