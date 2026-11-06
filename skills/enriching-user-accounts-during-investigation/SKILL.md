---
name: enriching-user-accounts-during-investigation
description: >-
  Enrich accounts using one or more integrations. Adds directory, IdP, and breach data. Use when an alert names user accounts during an investigation and context is needed before a decision, or when a block or escalation depends on user accounts during an investigation reputation. Keywords: enriching, user, accounts, during, investigation, enrichment, reputation, identity access management. Do not use for enriching endpoints during investigation - use `enriching-endpoints-during-investigation`.
domain: cybersecurity
subdomain: identity-access-management
tags:
- identity-access-management
- iam
- containment
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- PR.AC-01
- PR.AC-04
- RS.MI-01
mitre_attack:
- T1078
- T1098
- T1556
---

# Enriching User Accounts During Investigation

## When to Use

- A detection names user accounts during an investigation and the analyst needs context before deciding.
- A block or escalation decision needs provenance, not a hunch.
- An incident timeline needs first-seen, last-seen, and ownership data.

**Do not use** for enriching endpoints during investigation - use `enriching-endpoints-during-investigation`.

## Prerequisites

- API access to the sources you enable, and a cache directory.
- An allowlist of known-good values so shared infrastructure is not misread.
- The source's rate limits, so a batch does not exhaust the quota.

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

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

```powershell
# Active Directory
Disable-ADAccount -Identity jdoe
Get-ADUser -Identity jdoe -Properties LastLogonDate,MemberOf | Select-Object Name,LastLogonDate,MemberOf
Revoke-AzureADUserAllRefreshToken -ObjectId jdoe@example.com
```

```bash
# Microsoft Entra ID: disable the account and revoke sessions
az ad user update --id user@example.com --account-enabled false
az rest --method POST --url "https://graph.microsoft.com/v1.0/users/user@example.com/revokeSignInSessions"
```

```bash
# Okta: suspend the account and revoke sessions
curl -X POST "https://<org>.okta.com/api/v1/users/<user_id>/lifecycle/suspend" \
  -H "Authorization: SSWS $OKTA_TOKEN"
curl -X DELETE "https://<org>.okta.com/api/v1/users/<user_id>/sessions" \
  -H "Authorization: SSWS $OKTA_TOKEN"
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
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
