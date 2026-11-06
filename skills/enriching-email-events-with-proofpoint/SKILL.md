---
name: enriching-email-events-with-proofpoint
description: >-
  Enriches Proofpoint Targeted Attack Protection (TAP) incidents with forensic evidence. By utilizing the 'proofpoint-get-forensics' command, the playbook retrieves forensic evidence based on the campaign ID and threat ID detected in the Proofpoint TAP incidents. Covers 1 vendor variants: Proofpoint TAP. Use when enriching email events with proofpoint must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: enriching, email, events, with, proofpoint, phishing defense. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Enriching Email Events with Proofpoint

## When to Use

- The environment uses one of: Proofpoint TAP.
- enriching email events with proofpoint must be executed through a vendor API or console.
- An incident or audit needs a reproducible, vendor-specific record.

**Do not use** for the vendor-neutral procedure; use the matching generic skill.

## Prerequisites

- Access to the vendor console or API, and a credential with the required scope.
- The object identifier (host, account, resource, or indicator) and its provenance.
- A rollback path and a ticket for the change.

## Workflow

### Step 1: Validate the value

Reject private, reserved, malformed, or out-of-scope entries before any API call.

### Step 2: Query the sources

Run the enabled sources in parallel where possible, and record failures as failures rather than as clean results.

### Step 3: Normalize

Map each source's fields into one schema with the source name attached to every value.

### Step 4: Score confidence

Combine independent signals with explicit weights; cap the score when fewer than two sources respond.

### Step 5: Hand off

Attach the record to the incident and pass the decision to the containment or escalation skill.

## Vendor Variants

### Proofpoint TAP - Event Enrichment

Source pack: Proofpoint TAP

Enriches Proofpoint Targeted Attack Protection (TAP) incidents with forensic evidence. By utilizing the 'proofpoint-get-forensics' command, the playbook retrieves forensic evidence based on the campaign ID and threat ID detected in the Proofpoint TAP incidents.

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

- Every enabled source appears in either the success or failure list.
- The confidence score is reproducible from the component signals.
- Cached values carry the original lookup timestamp.
- No credentials appear in the output.

## Common Pitfalls

- Treating no reports as clean.
- Ignoring shared infrastructure.
- Burning the daily quota on a /24.
- Using stale reputation without recording the lookup time.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and record template
- `scripts/agent.py` - runnable helper for this procedure
