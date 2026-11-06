# API Reference - Parsing Nessus Nexpose Reports

## Script

```bash
python3 scripts/agent.py --help
```

## Platform commands

```bash
# Tenable / Nessus export
curl -X POST "https://<nessus>:8834/scans/<id>/export" \
  -H "X-ApiKeys: accessKey=$ACCESS;secretKey=$SECRET" \
  -d '{"format":"nessus"}'
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |