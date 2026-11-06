---
name: searching-endpoints-by-cve
description: >-
  Hunt for assets with a given CVE using available tools. Searches the estate for a CVE. Use when activity related to endpoints by CVE is suspected elsewhere in the estate, or when a hunt needs queries for endpoints by CVE. Keywords: searching, endpoints, cve, hunting, detection, vulnerability management. Do not use for searching endpoints by hash - use `searching-endpoints-by-hash`.
domain: cybersecurity
subdomain: vulnerability-management
tags:
- vulnerability-management
- cve
- remediation
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- ID.RA-01
- PR.IP-12
- RS.MI-02
mitre_attack:
- T1190
- T1203
- T1068
---

# Searching Endpoints by CVE

## When to Use

- A threat report or incident suggests endpoints by CVE may be present elsewhere.
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
# Tenable / Nessus export
curl -X POST "https://<nessus>:8834/scans/<id>/export" \
  -H "X-ApiKeys: accessKey=$ACCESS;secretKey=$SECRET" \
  -d '{"format":"nessus"}'
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
