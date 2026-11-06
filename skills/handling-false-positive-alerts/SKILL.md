---
name: handling-false-positive-alerts
description: >-
  Handles false positive alerts. It creates an alert exclusion or alert exception, or adds a file to an allow list based on the alert fields and inputs. Closes the alert with a documented exclusion, not a silent suppression. Use when an incident reaches the false-positive alerts phase, or when a response plan needs a false-positive alerts step. Keywords: handling, false, positive, alerts, incident-response, playbook, incident response. Do not use for investigating masquerading alerts - use `investigating-masquerading-alerts`.
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

# Handling False Positive Alerts

## When to Use

- An incident has reached the false-positive alerts phase.
- A playbook step needs a documented, repeatable execution.
- A review needs to see what was done and why.

**Do not use** for investigating masquerading alerts - use `investigating-masquerading-alerts`.

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
