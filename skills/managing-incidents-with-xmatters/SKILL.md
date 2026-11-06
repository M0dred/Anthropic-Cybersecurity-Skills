---
name: managing-incidents-with-xmatters
description: >-
  Trigger an xMatters workflow to notify a user for a response. This playbook would be used as a sub-playbook to notify an xMatters Group or User and then wait for a response. The user's response is passed as an output to the playbook for use in a parent playbook for branching. See the xMatters - Example Conditional Actions playbook for an example. Covers 1 vendor variants: xMatters. Use when managing incidents with xmatters must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: managing, incidents, with, xmatters, incident response. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Managing Incidents with Xmatters

## When to Use

- The environment uses one of: xMatters.
- managing incidents with xmatters must be executed through a vendor API or console.
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

### xMatters - Wait for Response

Source pack: xMatters

Trigger an xMatters workflow to notify a user for a response. This playbook would be used as a sub-playbook to notify an xMatters Group or User and then wait for a response. The user's response is passed as an output to the playbook for use in a parent playbook for branching. See the xMatters - Example Conditional Actions playbook for an example.

Inputs:

- `recipients`: A comma separated list of Groups or Users to target for a notification
- `subject`: A brief summary of the reason to notify
- `body`: Detailed description of the reason to notify
- `incident_id`: The related incident_id

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
