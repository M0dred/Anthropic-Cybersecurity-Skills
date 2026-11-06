# API Reference - Isolating Endpoints with Cortex XDR

## Script

```bash
python3 scripts/agent.py --help
```

## Platform commands

```bash
# Cortex XDR
curl -X POST "https://api-<tenant>.xdr.us.paloaltonetworks.com/public_api/v1/endpoints/isolate" \
  -H "Authorization: $XDR_TOKEN" -H "Content-Type: application/json" \
  -d '{"request_data":{"endpoint_id":"<id>"}}'
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |