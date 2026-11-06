---
name: retrieving-original-emails-from-gateway
description: >-
  Retrieves a specified EML/MSG file directly from the email security gateway product. Retrieves the original message from the gateway. Use when original emails from the gateway must be collected as evidence, or when volatile data about original emails from the gateway must be preserved. Keywords: retrieving, original, emails, from, gateway, acquisition, forensics, phishing defense. Do not use for retrieving original email thread - use `retrieving-original-email-thread`.
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

# Retrieving Original Emails From Gateway

## When to Use

- An incident requires forensic evidence from a host or capture point.
- A review or legal process needs a defensible acquisition.
- Volatile data must be preserved before containment or reboot.

**Do not use** for retrieving original email thread - use `retrieving-original-email-thread`.

## Prerequisites

- Authorization and scope for the acquisition.
- A target directory with enough space, and a write blocker where required.
- The transport: local, WinRM, SSH, or an agent.

## Workflow

### Step 1: Authorize and scope

Record who approved the acquisition and what is in scope.

### Step 2: Capture volatile data first

Memory, processes, sockets, and logged-on users before anything changes.

### Step 3: Capture persistent data

Registry, MFT, event logs, and file system metadata.

### Step 4: Hash and record

SHA-256 every artifact and record the tool, version, and time.

### Step 5: Transfer and store

Move to evidence storage, verify the hash after transfer, and restrict access.

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

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

- Every artifact has a hash that matches after transfer.
- The chain-of-custody form is complete.
- The acquisition did not alter the source more than documented.
- The evidence is stored with access controls.

## Common Pitfalls

- Rebooting before memory capture.
- Writing to the evidence disk.
- Missing the hash after transfer.
- Acquiring beyond the authorized scope.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
