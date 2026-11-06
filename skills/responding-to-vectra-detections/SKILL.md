---
name: responding-to-vectra-detections
description: >-
  Is called from the Process Incident - Vectra Detect playbook. It will fetch all active detections for the entity under investigation. It will then assign the entity to a user; if an assignment already exists, it will update that assignment and add a note in Vectra. Covers 4 vendor variants: Vectra AI, Vectra XDR. Use when responding to vectra detections must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: responding, to, vectra, detections, endpoint security. Do not use for the vendor-neutral procedure - use the matching generic skill.
domain: cybersecurity
subdomain: endpoint-security
tags:
- endpoint-security
- edr
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.MI-01
- PR.AC-05
- DE.CM-01
mitre_attack:
- T1059
- T1021
- T1562
---

# Responding To Vectra Detections

## When to Use

- The environment uses one of: Vectra AI, Vectra XDR.
- responding to vectra detections must be executed through a vendor API or console.
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

### Dispatch Incident - Vectra Detect

Source pack: Vectra AI

Is called from the Process Incident - Vectra Detect playbook. It will fetch all active detections for the entity under investigation. It will then assign the entity to a user; if an assignment already exists, it will update that assignment and add a note in Vectra.

Inputs:

- `user_id`: User ID for entity assignment.
- `entity_type`: Type of the entity.
- `entity_id`: ID of the entity.

### Dispatch Incident - Vectra XDR

Source pack: Vectra XDR

Is called from the Process Incident - Vectra XDR playbook. It will fetch all active detections for the entity under investigation. It will then assign the entity to a user; if an assignment already exists, it will update that assignment and add a note in Vectra.

Inputs:

- `UserID`: User ID for entity assignment.

### Process Incident - Vectra Detect

Source pack: Vectra AI

Is used to initiate the processing of an incident. This playbook runs when a pending incident is selected for investigation. It will change the state from pending to active and it will list the available users in Vectra and request the user ID to use for assignment. Once the data collection is complete, it will call the Dispatch Incident - Vectra Detect playbook.

Inputs:

- `entity_id`: ID of the entity.
- `entity_type`: Type of the entity.

### Process Incident - Vectra XDR

Source pack: Vectra XDR

Is used to initiate the processing of an incident. This playbook runs when a pending incident is selected for investigation. It will change the state from pending to active and it will list the available users in Vectra and request the user ID to use for assignment. Once the data collection is complete, it will call the Dispatch Incident - Vectra XDR playbook.

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
