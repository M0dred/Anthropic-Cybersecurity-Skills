# API Reference - Enriching External IP Addresses

## ipinfo.io

```bash
curl "https://ipinfo.io/203.0.113.10/json"
```

```json
{
  "ip": "203.0.113.10",
  "city": "Amsterdam",
  "region": "North Holland",
  "country": "NL",
  "loc": "52.3740,4.8897",
  "org": "AS64500 Example Hosting B.V.",
  "postal": "1012",
  "timezone": "Europe/Amsterdam"
}
```

No key required for the basic endpoint; a token raises the quota. Parse `org`
into ASN (`AS64500`) and organization.

## AbuseIPDB

```bash
curl -G "https://api.abuseipdb.com/api/v2/check" \
  --data-urlencode "ipAddress=203.0.113.10" \
  -d maxAgeInDays=90 -d verbose \
  -H "Key: $ABUSEIPDB_API_KEY" -H "Accept: application/json"
```

```json
{
  "data": {
    "ipAddress": "203.0.113.10",
    "isPublic": true,
    "ipVersion": 4,
    "abuseConfidenceScore": 100,
    "countryCode": "NL",
    "usageType": "Data Center/Web Hosting/Transit",
    "isp": "Example Hosting",
    "domain": "example.net",
    "totalReports": 412,
    "numDistinctUsers": 88,
    "lastReportedAt": "2026-08-30T12:00:00+00:00"
  }
}
```

Free tier: 1,000 checks/day. `abuseConfidenceScore` is 0-100.

## VirusTotal

```bash
curl "https://www.virustotal.com/api/v3/ip_addresses/203.0.113.10" \
  -H "x-apikey: $VT_API_KEY"
```

```json
{
  "data": {
    "attributes": {
      "last_analysis_stats": {"malicious": 12, "suspicious": 2, "harmless": 60, "undetected": 5},
      "asn": 64500,
      "as_owner": "Example Hosting",
      "network": "203.0.113.0/24",
      "country": "NL",
      "reputation": -42
    }
  }
}
```

Public tier: 4 requests/minute, 500/day.

## GreyNoise

```bash
curl "https://api.greynoise.io/v3/community/203.0.113.10" \
  -H "key: $GREYNOISE_API_KEY"
```

```json
{
  "ip": "203.0.113.10",
  "noise": true,
  "riot": false,
  "classification": "malicious",
  "name": "Example Scanner",
  "last_seen": "2026-08-30",
  "link": "https://viz.greynoise.io/ip/203.0.113.10"
}
```

`classification` is `benign`, `unknown`, or `malicious`. `riot` means a known
common business service.

## Reverse DNS

```bash
dig +short -x 203.0.113.10
python3 -c "import socket; print(socket.gethostbyaddr('203.0.113.10'))"
```

## CLI

```bash
python3 scripts/agent.py classify --ip 203.0.113.10 --ip 10.0.0.5
python3 scripts/agent.py enrich --ip 203.0.113.10 --out enrichment.json
python3 scripts/agent.py enrich --ip 203.0.113.10 --sources ipinfo,abuseipdb --no-cache
```

## Rate limits

| Source | Limit | Header on 429 |
|---|---|---|
| AbuseIPDB | 1,000/day | `X-RateLimit-Remaining` |
| VirusTotal | 4/min, 500/day | `X-RateLimit-Remaining` |
| GreyNoise | per plan | `Retry-After` |
| ipinfo | 50k/month (token) | `X-RateLimit-Remaining` |

## Normalized record

```json
{
  "ip": "203.0.113.10",
  "geo": {"country": "NL", "city": "Amsterdam", "asn": "AS64500", "org": "Example Hosting"},
  "ptr": "host.example.net",
  "reputation": {
    "abuseipdb": {"score": 100, "reports": 412},
    "virustotal": {"malicious": 12, "suspicious": 2},
    "greynoise": {"classification": "malicious", "riot": false}
  },
  "confidence": 0.86
}
```
