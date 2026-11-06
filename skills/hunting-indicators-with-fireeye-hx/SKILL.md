---
name: hunting-indicators-with-fireeye-hx
description: >-
  Facilitates threat hunting and detection of IOCs within FireEye Endpoint Security (HX) utilizing three . The query FireEye HX for different indicators including files, traffic, and execution flows indicators. Note that multiple search values should be. Uses HX IOC sweeps across host sets. Use when activity related to indicators through FireEye HX is suspected elsewhere in the estate, or when a hunt needs queries for indicators through FireEye HX. Keywords: hunting, indicators, with, fireeye, detection, endpoint security. Do not use for isolating endpoints with fireeye hx - use `isolating-endpoints-with-fireeye-hx`.
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

# Hunting Indicators with FireEye Hx

## When to Use

- A threat report or incident suggests indicators through FireEye HX may be present elsewhere.
- A detection needs validation against historical telemetry.
- A proactive hunt is scheduled for the environment.

**Do not use** for isolating endpoints with fireeye hx - use `isolating-endpoints-with-fireeye-hx`.

## Prerequisites

- Query access to the relevant telemetry: SIEM, EDR, cloud audit logs, or network.
- The data retention window and the field map for each source.
- A hypothesis with a falsifiable test.

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

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

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
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
