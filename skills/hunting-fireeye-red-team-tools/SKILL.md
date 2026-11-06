---
name: hunting-fireeye-red-team-tools
description: >-
  Collect indicators to aid in your threat hunting process. Hunt for the indicators. Uses the published FireEye red-team tool indicators. Use when activity related to FireEye red-team tooling is suspected elsewhere in the estate, or when a hunt needs queries for FireEye red-team tooling. Keywords: hunting, fireeye, red, team, tools, detection, threat hunting. Do not use for hunting indicators with fireeye hx - use `hunting-indicators-with-fireeye-hx`.
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

# Hunting FireEye Red Team Tools

## When to Use

- A threat report or incident suggests FireEye red-team tooling may be present elsewhere.
- A detection needs validation against historical telemetry.
- A proactive hunt is scheduled for the environment.

**Do not use** for hunting indicators with fireeye hx - use `hunting-indicators-with-fireeye-hx`.

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
