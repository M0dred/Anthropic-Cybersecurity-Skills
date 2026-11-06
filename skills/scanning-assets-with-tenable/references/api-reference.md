# API Reference - Scanning Assets with Tenable

## Vendor variants

### Cortex ASM - Tenable.io Enrichment

Pack: Cortex Attack Surface Management

### Launch Scan - Tenable.sc

Pack: Tenable.sc

### Tenable.io Scan

Pack: Tenable Vulnerability Management (formerly Tenable.io)

### Vulnerability Scan - RiskIQ Digital Footprint - Tenable.io

Pack: RiskIQ Digital Footprint


## Platform commands

```bash
# Generic REST call with a bearer token
curl -sS -X GET "https://api.example.com/v1/resource" \
  -H "Authorization: Bearer $API_TOKEN" -H "Accept: application/json"
```
