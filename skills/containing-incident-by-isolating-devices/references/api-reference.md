# API Reference - Containing Incident by Isolating Devices

## Script

```bash
python3 scripts/agent.py --help
```

## Platform commands

```bash
# Intune / MDM device lookup
az rest --method GET --url "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices?\$filter=userPrincipalName eq 'user@example.com'"
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |