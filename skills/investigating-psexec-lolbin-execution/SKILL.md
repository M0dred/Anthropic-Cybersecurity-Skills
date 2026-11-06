---
name: investigating-psexec-lolbin-execution
description: >-
  The "Remote PsExec-like LOLBIN Command Execution" is designed to address and respond to alerts indicating suspicious activities related to remote PsExec-like LOLBIN command execution from an unsigned non-standard source. The aims to efficiently: The is. Focuses on PsExec-style service creation and LOLBIN chains. Use when an alert names PsExec-style LOLBIN execution and the scope is unknown, or when a timeline is needed for PsExec-style LOLBIN execution. Keywords: investigating, psexec, lolbin, execution, investigation, triage, endpoint security. Do not use for investigating masquerading alerts - use `investigating-masquerading-alerts`.
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

# Investigating PsExec LOLBIN Execution

## When to Use

- An alert names PsExec-style LOLBIN execution and the scope is not yet known.
- An incident needs a timeline and a verdict before containment.
- A review challenges whether the original conclusion was supported.

**Do not use** for investigating masquerading alerts - use `investigating-masquerading-alerts`.

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
