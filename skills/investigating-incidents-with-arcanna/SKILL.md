---
name: investigating-incidents-with-arcanna
description: >-
  Takes incident data and sends it to Arcanna.Ai for ML inference and automated decision. Covers 2 vendor variants: ArcannaAI. Use when investigating incidents with arcanna must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: investigating, incidents, with, arcanna, incident response. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Investigating Incidents with Arcanna

## When to Use

- The environment uses one of: ArcannaAI.
- investigating incidents with arcanna must be executed through a vendor API or console.
- An incident or audit needs a reproducible, vendor-specific record.

**Do not use** for the vendor-neutral procedure; use the matching generic skill.

## Prerequisites

- Access to the vendor console or API, and a credential with the required scope.
- The object identifier (host, account, resource, or indicator) and its provenance.
- A rollback path and a ticket for the change.

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

## Vendor Variants

### Arcanna-Generic-Investigation-V2-With-Feedback

Source pack: ArcannaAI

Takes incident data and sends it to Arcanna.Ai for ML inference and automated decision.

Inputs:

- `incident RawJson`: Incident rawJson or another Json formatted string.

### Arcanna-Generic-Investigation

Source pack: ArcannaAI

Playbook takes incident data and sends it to Arcanna.Ai for ML inference and automated decision. Once decision is retrieved, manual input ( in this case ) from analyst is added in as feedback and sent back to Arcanna.ai. Once Feedback is provided in the final steps of the playbook, an automated AI Training is triggered and finally the full record, that contains all Arcanna.ai added metadata, is retrieved back into the context.

Inputs:

- `incident RawJson`: Incident rawJson or another Json formatted string.

## Platform Commands

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
- `references/workflows.md` - decision tree and record template
- `scripts/agent.py` - runnable helper for this procedure
