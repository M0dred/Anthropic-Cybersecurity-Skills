---
name: triaging-third-party-findings-with-panorays
description: >-
  Triages a Panorays "Self Company" finding incident end-to-end without depending on any specific external ITSM tool. Flow. Covers 1 vendor variants: Panorays. Use when triaging third party findings with panorays must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: triaging, third, party, findings, with, panorays, vulnerability management. Do not use for the vendor-neutral procedure - use the matching generic skill.
domain: cybersecurity
subdomain: vulnerability-management
tags:
- vulnerability-management
- cve
- remediation
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- ID.RA-01
- PR.IP-12
- RS.MI-02
mitre_attack:
- T1190
- T1203
- T1068
---

# Triaging Third Party Findings with Panorays

## When to Use

- The environment uses one of: Panorays.
- triaging third party findings with panorays must be executed through a vendor API or console.
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

### Panorays Finding - Triage and Response

Source pack: Panorays

Triages a Panorays "Self Company" finding incident end-to-end without depending on any specific external ITSM tool. Flow.

Inputs:

- `NotificationTarget`: Recipient for Critical/High severity notifications (email address, Slack/Teams channel, or user - whichever matches the notification integration you have enable
- `AutoCloseReason`: closeReason used when auto-closing Low/Informational severity findings. Align this to your own close-reason taxonomy if needed.
- `AutoCloseNotes`: closeNotes used when auto-closing Low/Informational severity findings.
- `DuplicateCloseReason`: closeReason used when auto-closing this incident as a duplicate of an already-open incident.
- `DuplicateCloseNotes`: closeNotes used when auto-closing this incident as a duplicate of an already-open incident.

## Platform Commands

```bash
# Generic REST call with a bearer token
curl -sS -X GET "https://api.example.com/v1/resource" \
  -H "Authorization: Bearer $API_TOKEN" -H "Accept: application/json"
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
