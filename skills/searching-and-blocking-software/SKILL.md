---
name: searching-and-blocking-software
description: >-
  Search a file or process activity of a software by a given image file name. The analyst can then choose the files to block. The following integrations are supported. Finds the software by image name and blocks it. Use when activity related to and blocking software is suspected elsewhere in the estate, or when a hunt needs queries for and blocking software. Keywords: searching, and, blocking, software, hunting, detection, endpoint security. Do not use for blocking compromised accounts - use `blocking-compromised-accounts`.
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

# Searching and Blocking Software

## When to Use

- A threat report or incident suggests and blocking software may be present elsewhere.
- A detection needs validation against historical telemetry.
- A proactive hunt is scheduled for the environment.

**Do not use** for blocking compromised accounts - use `blocking-compromised-accounts`.

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
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
