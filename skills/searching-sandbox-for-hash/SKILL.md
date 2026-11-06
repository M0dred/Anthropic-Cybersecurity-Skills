---
name: searching-sandbox-for-hash
description: >-
  Searches for a specific hash in the supported sandboxes. If the hash is known, the provides a detailed analysis of the sandbox report. Currently, supported sandboxes are Falcon Intelligence Sandbox, Wildfire and Joe Sandbox. Searches sandboxes for a known hash. Use when activity related to sandboxes for a hash is suspected elsewhere in the estate, or when a hunt needs queries for sandboxes for a hash. Keywords: searching, sandbox, for, hash, hunting, detection, threat intelligence. Do not use for searching endpoints by hash - use `searching-endpoints-by-hash`.
domain: cybersecurity
subdomain: threat-intelligence
tags:
- threat-intelligence
- ioc
- enrichment
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- ID.RA-01
- DE.AE-02
- RS.AN-03
mitre_attack:
- T1588.001
- T1071
- T1595
---

# Searching Sandbox for Hash

## When to Use

- A threat report or incident suggests sandboxes for a hash may be present elsewhere.
- A detection needs validation against historical telemetry.
- A proactive hunt is scheduled for the environment.

**Do not use** for searching endpoints by hash - use `searching-endpoints-by-hash`.

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
curl "https://www.virustotal.com/api/v3/files/<sha256>" -H "x-apikey: $VT_API_KEY"
curl -X POST "https://www.virustotal.com/api/v3/files" -H "x-apikey: $VT_API_KEY" -F "file=@sample.bin"
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
