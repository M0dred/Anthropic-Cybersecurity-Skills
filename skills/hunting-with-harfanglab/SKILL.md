---
name: hunting-with-harfanglab
description: >-
  Allows is triggered by the Hurukai - Process Indicators - Manual Review playbook. It allows to search for IOC sightings in the HarfangLab EDR and tag sighted IOCs accordingly for manual review. All IOCs are tagged in order to be further inserted into a HarfangLab EDR IOC source. Covers 1 vendor variants: HarfangLab EDR. Use when hunting with harfanglab must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: hunting, with, harfanglab, endpoint security. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Hunting with Harfanglab

## When to Use

- The environment uses one of: HarfangLab EDR.
- hunting with harfanglab must be executed through a vendor API or console.
- An incident or audit needs a reproducible, vendor-specific record.

**Do not use** for the vendor-neutral procedure; use the matching generic skill.

## Prerequisites

- Access to the vendor console or API, and a credential with the required scope.
- The object identifier (host, account, resource, or indicator) and its provenance.
- A rollback path and a ticket for the change.

## Workflow

### Step 1: State the hypothesis

Write what you expect to see if the activity is present, and what would prove it absent.

### Step 2: Translate to queries

Write one query per telemetry source, with the fields and time window explicit.

### Step 3: Run and triage

Execute, de-duplicate, and rank hits by confidence and asset criticality.

### Step 4: Pivot

For each confirmed hit, pivot on the entity, the technique, and the infrastructure.

### Step 5: Document

Record the queries, the hit counts, the false positives, and the coverage gaps.

## Vendor Variants

### Hurukai - Hunt IOCs

Source pack: HarfangLab EDR

Allows is triggered by the Hurukai - Process Indicators - Manual Review playbook. It allows to search for IOC sightings in the HarfangLab EDR and tag sighted IOCs accordingly for manual review. All IOCs are tagged in order to be further inserted into a HarfangLab EDR IOC source.

Inputs:

- `Indicator Query`: Indicators matching the indicator query will be used as playbook input

## Platform Commands

```bash
# Generic REST call with a bearer token
curl -sS -X GET "https://api.example.com/v1/resource" \
  -H "Authorization: Bearer $API_TOKEN" -H "Accept: application/json"
```

## Verification

- The queries are saved and rerunnable.
- Hit counts reconcile with a manual spot check.
- False positives are explained, not silently dropped.
- Coverage gaps are stated explicitly.

## Common Pitfalls

- Hunting without a hypothesis.
- Querying only one telemetry source.
- Ignoring retention limits.
- Reporting hits without triage.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and record template
- `scripts/agent.py` - runnable helper for this procedure
