# API Reference - Deleting Malicious Emails in M365

## Vendor variants

### Exchange 2016 Search and Delete

Pack: Exchange 2016 Compliance Search

### O365 - Security And Compliance - Search Action - Delete

Pack: Microsoft Exchange Online

### O365 - Security And Compliance - Search Action - Preview

Pack: Microsoft Exchange Online

### O365 - Security And Compliance - Search And Delete

Pack: Microsoft Exchange Online

### O365 - Security And Compliance - Search

Pack: Microsoft Exchange Online

### Office 365 and Azure Hunting

Pack: Office 365 and Azure (Audit Log)

### Office 365 Search and Delete

Pack: Microsoft Exchange Online

### Search And Delete Emails - Gmail

Pack: Gmail

### Search And Delete Emails - Microsoft Graph Security

Pack: Microsoft Graph Security


## Platform commands

```powershell
# Microsoft 365
Get-MessageTrace -SenderAddress attacker@evil.example -StartDate (Get-Date).AddDays(-7)
New-ComplianceSearch -Name "INC-1234" -ExchangeLocation all -ContentMatchQuery 'from:attacker@evil.example'
Start-ComplianceSearch -Identity "INC-1234"
New-ComplianceSearchAction -SearchName "INC-1234" -Purge -PurgeType SoftDelete
```

```bash
# Proofpoint TAP / mail gateway
curl "https://tap.proofpoint.com/v2/siem/messages/blocked?interval=2026-08-30T00:00:00Z/2026-08-31T00:00:00Z" \
  -H "Authorization: Basic $PP_AUTH"
```
