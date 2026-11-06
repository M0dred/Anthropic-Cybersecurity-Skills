---
name: running-proactive-threat-hunts
description: >-
  Is the main of the 'Proactive Threat Hunting' pack. It automatically runs during a new hunting session and guides the threat hunter through the session based on the selected hunting method. The available hunting methods are. Runs on a scheduled cadence with a hypothesis per hunt. Use when an incident reaches the proactive threat hunts phase, or when a response plan needs a proactive threat hunts step. Keywords: running, proactive, threat, hunts, incident-response, playbook, threat hunting. Do not use for parsing stix threat intelligence - use `parsing-stix-threat-intelligence`.
domain: cybersecurity
subdomain: threat-hunting
tags:
- threat-hunting
- siem
- detection
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- DE.CM-01
- DE.AE-02
- DE.AE-07
mitre_attack:
- T1071
- T1059
- T1021
---

# Running Proactive Threat Hunts

## When to Use

- An incident has reached the proactive threat hunts phase.
- A playbook step needs a documented, repeatable execution.
- A review needs to see what was done and why.

**Do not use** for parsing stix threat intelligence - use `parsing-stix-threat-intelligence`.

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
