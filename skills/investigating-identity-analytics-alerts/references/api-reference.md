# API Reference - Investigating Identity Analytics Alerts

## Script

```bash
python3 scripts/agent.py --help
```

## Platform commands

```bash
# Microsoft Entra ID: disable the account and revoke sessions
az ad user update --id user@example.com --account-enabled false
az rest --method POST --url "https://graph.microsoft.com/v1.0/users/user@example.com/revokeSignInSessions"
```

```powershell
# Active Directory
Disable-ADAccount -Identity jdoe
Get-ADUser -Identity jdoe -Properties LastLogonDate,MemberOf | Select-Object Name,LastLogonDate,MemberOf
Revoke-AzureADUserAllRefreshToken -ObjectId jdoe@example.com
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |