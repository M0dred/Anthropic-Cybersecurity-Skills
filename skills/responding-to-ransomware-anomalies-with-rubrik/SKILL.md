---
name: responding-to-ransomware-anomalies-with-rubrik
description: >-
  Investigate an anomaly incident ingested by the integration "RubrikPolaris", enrich its data, and perform a remediation according to the incident's object type. Use when an incident reaches the ransomware anomalies through Rubrik phase, or when a response plan needs a ransomware anomalies through Rubrik step. Keywords: responding, ransomware, anomalies, with, rubrik, incident-response, playbook, ransomware defense. Do not use for recovering ransomware files with rubrik - use `recovering-ransomware-files-with-rubrik`.
domain: cybersecurity
subdomain: ransomware-defense
tags:
- ransomware-defense
- backup
- recovery
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- PR.DS-11
- RC.RP-01
- RS.MI-01
mitre_attack:
- T1486
- T1490
- T1485
---

# Responding To Ransomware Anomalies with Rubrik

## When to Use

- An incident has reached the ransomware anomalies through Rubrik phase.
- A playbook step needs a documented, repeatable execution.
- A review needs to see what was done and why.

**Do not use** for recovering ransomware files with rubrik - use `recovering-ransomware-files-with-rubrik`.

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
# Rubrik Security Cloud
curl -X POST "https://<rubrik>/api/v1/fileset/request" \
  -H "Authorization: Bearer $RUBRIK_TOKEN" -H "Content-Type: application/json" \
  -d '{"filesetId":"<id>","paths":["/data"]}'
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
