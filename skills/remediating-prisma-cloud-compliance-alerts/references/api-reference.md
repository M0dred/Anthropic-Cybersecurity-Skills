# API Reference - Remediating Prisma Cloud Compliance Alerts

## Script

```bash
python3 scripts/agent.py --help
```

## Platform commands

```bash
# Prisma Cloud / CSPM API
curl -X POST "https://api.prismacloud.io/login" \
  -H "Content-Type: application/json" \
  -d '{"customerName":"$PC_TENANT","username":"$PC_USER","password":"$PC_PASS"}'
curl "https://api.prismacloud.io/v2/inventory?resourceType=aws_cloudtrail" \
  -H "x-redlock-auth: $PC_TOKEN"
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |