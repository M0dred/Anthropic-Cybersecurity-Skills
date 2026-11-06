---
name: containing-incident-by-disabling-accounts
description: >-
  Disables the account and revokes sessions. Use when an active incident requires compromised accounts to be cut off, or when a detection names compromised accounts and containment is authorized. Keywords: containing, incident, disabling, accounts, containment, response, identity access management. Do not use for containing incident by isolating devices - use `containing-incident-by-isolating-devices`.
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

# Containing Incident by Disabling Accounts

## When to Use

- An intrusion is active and compromised accounts must be cut off now.
- A detection or analyst decision requires compromised accounts to be blocked, isolated, disabled, or removed.
- A containment step needs a verifiable, reversible change with an audit trail.
- A post-incident review asks whether the containment actually worked.

**Do not use** for containing incident by isolating devices - use `containing-incident-by-isolating-devices`.

## Prerequisites

- Authority to change the target platform, and a ticket for the change.
- The exact value or object to contain, with provenance (alert, feed, analyst).
- Read access to the enforcement point so the change can be verified.
- The rollback command, written down before the change is applied.

## Workflow

### Step 1: Validate the target

Normalize the value, reject malformed or out-of-scope entries, and confirm the direction and blast radius. A containment action against shared infrastructure needs a narrower scope.

### Step 2: Choose the enforcement point

Prefer the point closest to the threat that is still reversible: host, then cloud control plane, then perimeter, then edge.

### Step 3: Apply the change

Use the platform-native command or API. Capture the exact request and response.

### Step 4: Verify the effect

Confirm the object is contained from the platform's own state, then test the path from an independent vantage point.

### Step 5: Record and schedule review

Write the change, operator, ticket, timestamp, rollback, and expiry into the incident.

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

- The platform reports the object in the contained state.
- An independent test confirms the blocked path fails while a control path succeeds.
- The rollback command has been executed once in a lab or on a canary.
- The change is recorded with an owner and an expiry date.

## Common Pitfalls

- Containing shared infrastructure and breaking legitimate users.
- Applying the change at a layer that does not see the traffic.
- No rollback, so a false positive becomes an outage.
- No expiry, so tactical blocks become permanent debt.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
