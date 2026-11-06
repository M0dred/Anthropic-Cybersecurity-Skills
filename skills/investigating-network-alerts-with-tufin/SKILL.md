---
name: investigating-network-alerts-with-tufin
description: >-
  Example Playbook utilizing the Tufin integration to enrich a network alert and perform containment, if needed. Requires the following incident details: Source IP, Destination IP, Destination Ports. Covers 1 vendor variants: Tufin. Use when investigating network alerts with tufin must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: investigating, network, alerts, with, tufin, network security. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Investigating Network Alerts with Tufin

## When to Use

- The environment uses one of: Tufin.
- investigating network alerts with tufin must be executed through a vendor API or console.
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

### Tufin - Investigate Network Alert

Source pack: Tufin

Example Playbook utilizing the Tufin integration to enrich a network alert and perform containment, if needed. Requires the following incident details: Source IP, Destination IP, Destination Ports.

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
