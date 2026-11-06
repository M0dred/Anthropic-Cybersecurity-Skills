---
name: deleting-malicious-emails-in-m365
description: >-
  Runs a compliance search in Exchange Server 2016, and delete the results. Covers 9 vendor variants: Exchange 2016 Compliance Search, Gmail, Microsoft Exchange Online, Microsoft Graph Security, Office 365 and Azure (Audit Log). Use when deleting malicious emails in m365 must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: deleting, malicious, emails, in, m365, phishing defense. Do not use for the vendor-neutral procedure - use the matching generic skill.
domain: cybersecurity
subdomain: phishing-defense
tags:
- phishing-defense
- email-security
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- DE.AE-02
- RS.AN-03
- PR.AT-01
mitre_attack:
- T1566.001
- T1566.002
- T1204.002
---

# Deleting Malicious Emails in M365

## When to Use

- The environment uses one of: Exchange 2016 Compliance Search, Gmail, Microsoft Exchange Online, Microsoft Graph Security, Office 365 and Azure (Audit Log).
- deleting malicious emails in m365 must be executed through a vendor API or console.
- An incident or audit needs a reproducible, vendor-specific record.

**Do not use** for the vendor-neutral procedure; use the matching generic skill.

## Prerequisites

- Access to the vendor console or API, and a credential with the required scope.
- The object identifier (host, account, resource, or indicator) and its provenance.
- A rollback path and a ticket for the change.

## Workflow

### Step 1: Confirm entry criteria

Verify the facts that justify this phase.

### Step 2: Plan

List the actions, the owner, and the expected effect.

### Step 3: Execute

Perform the actions, capturing output and timestamps.

### Step 4: Verify

Confirm the phase objective is met.

### Step 5: Record

Write the decision log and the exit criteria.

## Vendor Variants

### Exchange 2016 Search and Delete

Source pack: Exchange 2016 Compliance Search

Runs a compliance search in Exchange Server 2016, and delete the results.

Inputs:

- `Query`: The query used to find mail messages.

### O365 - Security And Compliance - Search Action - Delete

Source pack: Microsoft Exchange Online

Performs the following steps.

Inputs:

- `search_name`: The name of the compliance search.
- `delete_type`: Purge type. Possible values are: "Soft" and "Hard". Default is "Soft".
- `polling_timeout`: Search action polling timeout.
- `polling_interval`: Search action polling interval.

### O365 - Security And Compliance - Search Action - Preview

Source pack: Microsoft Exchange Online

Perform.

Inputs:

- `search_name`: The name of the compliance search.
- `polling_interval`: Search action polling interval.
- `polling_timeout`: Search action polling timeout.

### O365 - Security And Compliance - Search And Delete

Source pack: Microsoft Exchange Online

Performs the following steps.

Inputs:

- `search_name`: The name of the compliance search. If not specified will have prefix of "the platform-" and GUID e.g. auto-generated.
- `case`: The name of a Core eDiscovery case to associate with the new compliance search.
- `kql`: Text search string or a query that is formatted using the Keyword Query Language (KQL).
- `description`: Description of the compliance search.
- `allow_not_found_exchange_locations`: Whether to include mailboxes other than regular user mailboxes in the compliance search. Default is "false".
- `exchange_location`: Comma-separated list of mailboxes/distribution groups to include, or use the value "All" to include all.
- `exchange_location_exclusion`: Comma-separated list of mailboxes/distribution groups to exclude when you use the value "All" for the exchange_location parameter.
- `force`: Whether to replace the existing search. If "true", the existing search will be removed and a new search will be created. If "false", the existing search will be

### O365 - Security And Compliance - Search

Source pack: Microsoft Exchange Online

Performs the following steps.

Inputs:

- `search_name`: The name of the compliance search. If not specified will have prefix of "the platform-" and GUID e.g. auto-generated.
- `force`: If false, use the existing search without modifying any search parameters. If true, overwrite the existing search. Possible values are: "true" and "false".
- `preview`: Whether to preview results using the search action. Possible values are: "true" and "false".
- `case`: The name of a Core eDiscovery case to associate with the new compliance search.
- `kql`: Text search string or a query that is formatted using the Keyword Query Language (KQL).
- `description`: Description of the compliance search.
- `allow_not_found_exchange_locations`: Whether to include mailboxes other than regular user mailboxes in the compliance search. Possible values are: "true" and "false".
- `exchange_location`: Comma-separated list of mailboxes/distribution groups to include, or use the value "All" to include all.

### Office 365 and Azure Hunting

Source pack: Office 365 and Azure (Audit Log)

Enables you to collect and investigate suspicious security events from Azure AD environment.

### Office 365 Search and Delete

Source pack: Microsoft Exchange Online

Runs a compliance search on Office 365 and deletes the results.

Inputs:

- `Query`: The compliance search query.

### Search And Delete Emails - Gmail

Source pack: Gmail

Searches Gmail to identify and delete emails with similar attributes to the malicious email.\ Note: Searching through large amount of mailboxes might trigger a 429 error code. You can find more details here.

Inputs:

- `From`: The value of the malicious email's "From" attribute.
- `Subject`: The value of the malicious email's "Subject" attribute.
- `AttachmentName`: The value of the malicious email's "AttachmentName" attribute.
- `Limit`: The maximum number of search results.
- `DeleteType`: The deletion type (trash or permanent).For permanent choose 'True'.
- `SearchThisWeek`: Limit the search to the current week (true/false).

### Search And Delete Emails - Microsoft Graph Security

Source pack: Microsoft Graph Security

Performs the following steps.

Inputs:

- `case`: eDiscovery case to use. Looked up by name; created if missing.
- `mailbox_scope`: One of: recipientsOnly, allTenantMailboxes, allCaseCustodians, allCaseNoncustodialDataSources, allTenantSites. Drives data_source_scopes and KQL composition.
- `mailbox_exclusion`: CSV of mailboxes to exclude. Honored only when mailbox_scope=allTenantMailboxes.
- `kql`: KQL query identifying the emails to search/delete. Additional clauses are composed around it depending on mailbox_scope.
- `recipients`: CSV of email addresses. Required when mailbox_scope=recipientsOnly. Optional when mailbox_scope=allCaseCustodians.
- `search_name`: When provided, plays into the force semantics (force=true delete-and-recreate, force=false reuse). When omitted, an auto-name like auto-generated${incident.id}-
- `description`: eDiscovery search description. Defaults to "Created by the platform for incident ${incident.id}" when empty.
- `force`: Only meaningful when search_name is provided. true ⇒ delete-and-recreate. false ⇒ reuse existing.

## Platform Commands

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

## Verification

- The phase objective is met and evidenced.
- Every action has an owner and a timestamp.
- The decision log explains the choices.
- The next phase's entry criteria are stated.

## Common Pitfalls

- Skipping the evidence capture.
- Moving phases without exit criteria.
- No decision log.
- Losing the incident timeline.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and record template
- `scripts/agent.py` - runnable helper for this procedure
