# API Reference - Searching Siem for Failed Logins

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

```sql
SELECT sourceip, username, COUNT(*) AS failures
FROM events
WHERE eventid = 4625
GROUP BY sourceip, username
HAVING COUNT(*) > 10
LAST 24 HOURS
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |