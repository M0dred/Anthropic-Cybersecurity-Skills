# API Reference - Isolating Endpoints with Cybereason

## Script

```bash
python3 scripts/agent.py --help
```

## Platform commands

```bash
# Cybereason
curl -X POST "https://<tenant>.cybereason.net/rest/visualsearch/query/simple" \
  -H "Content-Type: application/json" \
  -d '{"queryPath":[{"requestedType":"Machine","filters":[{"filters":[{"fieldName":"name","values":["WEB-01"]}]}]}]}'
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |