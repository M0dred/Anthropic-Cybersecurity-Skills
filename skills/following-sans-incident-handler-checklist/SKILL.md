---
name: following-sans-incident-handler-checklist
description: >-
  Follows the "Incident Handler's Checklist" described in the SANS Institute ‘Incident Handler’s Handbook’ by Patrick Kral. ***Disclaimer: This does not ensure compliance to SANS regulations. Walks the SANS six-phase checklist. Use when an incident reaches the the SANS incident handler checklist phase, or when a response plan needs a the SANS incident handler checklist step. Keywords: following, sans, incident, handler, checklist, incident-response, playbook, incident response. Do not use for calculating incident severity - use `calculating-incident-severity`.
domain: cybersecurity
subdomain: incident-response
tags:
- incident-response
- containment
- soc-operations
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.MA-01
- RS.MI-01
- RS.AN-03
mitre_attack:
- T1486
- T1566
- T1078
---

# Following SANS Incident Handler Checklist

## When to Use

- An incident has reached the the SANS incident handler checklist phase.
- A playbook step needs a documented, repeatable execution.
- A review needs to see what was done and why.

**Do not use** for calculating incident severity - use `calculating-incident-severity`.

## Prerequisites

- The incident record, the current phase, and the owner.
- The evidence collected so far.
- Authority for the actions in this phase.

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

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

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
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
