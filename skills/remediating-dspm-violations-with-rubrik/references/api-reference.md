# API Reference - Remediating Dspm Violations with Rubrik

## Script

```bash
python3 scripts/agent.py --help
```

## Platform commands

```bash
# Rubrik Security Cloud
curl -X POST "https://<rubrik>/api/v1/fileset/request" \
  -H "Authorization: Bearer $RUBRIK_TOKEN" -H "Content-Type: application/json" \
  -d '{"filesetId":"<id>","paths":["/data"]}'
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |