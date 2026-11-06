# API Reference - Hunting Indicators with Rapid7 Insightidr

## Script

```bash
python3 scripts/agent.py --help
```

## Platform commands

```spl
index=windows EventCode=4625
| stats count by src_ip, user
| where count > 10
```

```kql
SecurityEvent
| where EventID == 4625
| summarize FailedLogons = count() by IpAddress, Account
| where FailedLogons > 10
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |