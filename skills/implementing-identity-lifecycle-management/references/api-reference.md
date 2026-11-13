# API Reference - Identity Lifecycle Management

## HR export schema

```csv
worker_id,first_name,last_name,email,department,manager,status,start_date,end_date
W-12345,Jane,Doe,jane.doe@example.com,Finance,John Roe,active,2026-01-15,
W-12346,Sam,Smith,sam.smith@example.com,Engineering,Jane Doe,terminated,2024-03-01,2026-08-31
```

## Active Directory

```powershell
New-ADUser -Name "Jane Doe" -SamAccountName jdoe -UserPrincipalName jane.doe@example.com `
  -Department Finance -Manager "John Roe" -Enabled $true -EmployeeID W-12345

Set-ADUser -Identity jdoe -Department Engineering -Manager "Jane Doe"
Add-ADGroupMember -Identity "Finance-Users" -Members jdoe
Remove-ADGroupMember -Identity "Finance-Users" -Members jdoe -Confirm:$false
Disable-ADAccount -Identity jdoe
Get-ADUser -Filter * -Properties EmployeeID,Department,Enabled | Select-Object Name,EmployeeID,Department,Enabled
```

## Microsoft Entra ID (Graph)

```bash
# Create a user
az ad user create --display-name "Jane Doe" --user-principal-name jane.doe@example.com \
  --password "<temporary>" --force-change-password-next-sign-in true

# Update department and manager
az ad user update --id jane.doe@example.com --department Finance

# Disable and revoke sessions
az ad user update --id jane.doe@example.com --account-enabled false
az rest --method POST --url "https://graph.microsoft.com/v1.0/users/jane.doe@example.com/revokeSignInSessions"

# Group membership
az ad group member add --group Finance-Users --member-id <object-id>
az ad group member remove --group Finance-Users --member-id <object-id>
```

## Okta

```bash
# Create
curl -X POST "https://<org>.okta.com/api/v1/users?activate=true" \
  -H "Authorization: SSWS $OKTA_TOKEN" -H "Content-Type: application/json" \
  -d '{"profile":{"firstName":"Jane","lastName":"Doe","email":"jane.doe@example.com","login":"jane.doe@example.com","department":"Finance","employeeNumber":"W-12345"}}'

# Update
curl -X POST "https://<org>.okta.com/api/v1/users/<id>" \
  -H "Authorization: SSWS $OKTA_TOKEN" -H "Content-Type: application/json" \
  -d '{"profile":{"department":"Engineering"}}'

# Deactivate and revoke sessions
curl -X POST "https://<org>.okta.com/api/v1/users/<id>/lifecycle/deactivate" \
  -H "Authorization: SSWS $OKTA_TOKEN"
curl -X DELETE "https://<org>.okta.com/api/v1/users/<id>/sessions" \
  -H "Authorization: SSWS $OKTA_TOKEN"

# Group membership
curl -X PUT "https://<org>.okta.com/api/v1/groups/<gid>/users/<uid>" \
  -H "Authorization: SSWS $OKTA_TOKEN"
```

## CLI

```bash
python3 scripts/agent.py plan --hr hr_export.csv --target ad --out plan.json
python3 scripts/agent.py apply --plan plan.json --dry-run
python3 scripts/agent.py apply --plan plan.json
python3 scripts/agent.py leaver --worker W-12345 --target okta --dry-run
python3 scripts/agent.py reconcile --hr hr_export.csv --target ad --out drift.json
```

## Directory snapshot format

```json
[
  {"worker_id": "W-12345", "login": "jdoe", "email": "jane.doe@example.com",
   "department": "Finance", "enabled": true, "groups": ["Finance-Users", "VPN-Users"]}
]
```

## SLA targets

| Flow | Target |
|---|---|
| Joiner | account within 1 business day of start |
| Mover | group change within 4 hours |
| Leaver | disabled within 1 hour, sessions revoked within 1 hour |
