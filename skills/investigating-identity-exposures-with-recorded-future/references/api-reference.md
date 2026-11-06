# API Reference - Investigating Identity Exposures with Recorded Future

## Vendor variants

### Recorded Future - Identity Exposure

Pack: Recorded Future Identity


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
