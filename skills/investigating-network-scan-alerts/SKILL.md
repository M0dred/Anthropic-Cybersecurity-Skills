---
name: investigating-network-scan-alerts
description: >-
  Handles external and internal scanning alerts. Attacker's Goals: Adversaries may attempt to get a listing of services running on remote hosts, including those that may be vulnerable to remote software exploitation. Methods to acquire this information. Focuses on external scan sources and targeted ports. Use when an alert names network-scan alerts and the scope is unknown, or when a timeline is needed for network-scan alerts. Keywords: investigating, network, scan, alerts, investigation, triage, network security. Do not use for investigating port scan alerts - use `investigating-port-scan-alerts`.
domain: cybersecurity
subdomain: network-security
tags:
- network-security
- firewall
- containment
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- PR.AC-05
- DE.CM-01
- RS.MI-01
mitre_attack:
- T1595
- T1071
- T1105
---

# Investigating Network Scan Alerts

## When to Use

- An alert names network-scan alerts and the scope is not yet known.
- An incident needs a timeline and a verdict before containment.
- A review challenges whether the original conclusion was supported.

**Do not use** for investigating port scan alerts - use `investigating-port-scan-alerts`.

## Prerequisites

- Read access to the relevant telemetry and asset inventory.
- The entity identifiers: user, host, IP, or application.
- A case or ticket to attach evidence to.

## Workflow

### Step 1: Scope the entity

Resolve the identifier to all of its identities and assets.

### Step 2: Collect evidence

Pull authentication, process, network, and cloud audit events for the window.

### Step 3: Build the timeline

Order events, resolve time zones, and mark the first and last malicious action.

### Step 4: Test hypotheses

Distinguish the observed facts from the inference, and check alternative explanations.

### Step 5: Conclude

State the verdict, the confidence, and the recommended containment.

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

```bash
# Generic REST call with a bearer token
curl -sS -X GET "https://api.example.com/v1/resource" \
  -H "Authorization: Bearer $API_TOKEN" -H "Accept: application/json"
```

## Verification

- Every timeline entry has a source and a timestamp.
- The verdict distinguishes facts from inference.
- Alternative explanations are addressed.
- The evidence is attached to the case.

## Common Pitfalls

- Confirmation bias toward the first alert.
- Mixing time zones in the timeline.
- Treating a single log line as proof.
- Closing without checking lateral movement.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
