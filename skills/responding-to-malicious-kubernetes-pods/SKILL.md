---
name: responding-to-malicious-kubernetes-pods
description: >-
  Ensures a swift and effective response to malicious activities within Kubernetes environments, leveraging cloud-native tools to maintain cluster security and integrity. The is designed to handle agent-generated alerts due to malicious activities within. Use when an incident reaches the malicious Kubernetes pods phase, or when a response plan needs a malicious Kubernetes pods step. Keywords: responding, malicious, kubernetes, pods, incident-response, playbook, container security. Do not use for responding to cloud data exfiltration - use `responding-to-cloud-data-exfiltration`.
domain: cybersecurity
subdomain: container-security
tags:
- container-security
- kubernetes
- cloud-security
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- PR.PS-01
- DE.CM-01
- RS.MI-01
mitre_attack:
- T1610
- T1611
- T1525
---

# Responding To Malicious Kubernetes Pods

## When to Use

- An incident has reached the malicious Kubernetes pods phase.
- A playbook step needs a documented, repeatable execution.
- A review needs to see what was done and why.

**Do not use** for responding to cloud data exfiltration - use `responding-to-cloud-data-exfiltration`.

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
# Kubernetes
kubectl get pods -A -o wide
kubectl describe pod suspicious-pod -n default
kubectl delete pod suspicious-pod -n default --grace-period=0
kubectl cordon node-01
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
