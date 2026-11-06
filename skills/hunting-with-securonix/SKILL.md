---
name: hunting-with-securonix
description: >-
  Gets a list of violations with pagination using queryId parameter. Covers 2 vendor variants: Securonix. Use when hunting with securonix must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: hunting, with, securonix, threat hunting. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Hunting with Securonix

## When to Use

- The environment uses one of: Securonix.
- hunting with securonix must be executed through a vendor API or console.
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

### Fetch All Violations - Securonix

Source pack: Securonix

Gets a list of violations with pagination using queryId parameter.

Inputs:

- `from`: Start date/time for which to retrieve activity data (in the format MM/dd/yyyy HH:mm:ss).
- `to`: End date/time for which to retrieve activity data (in the format MM/dd/yyyy HH:mm:ss).
- `query`: Free-text query. For example, query="resourcegroupname=WindowsSnare and policyname=Possible Privilege Escalation - Self Escalation".

### Fetch Violations - Securonix

Source pack: Securonix

Gets a list of violation data.

Inputs:

- `from`: Start date/time for which to retrieve activity data (in the format MM/dd/yyyy HH:mm:ss).
- `to`: End date/time for which to retrieve activity data (in the format MM/dd/yyyy HH:mm:ss).
- `query`: Free-text query. For example, query="resourcegroupname=WindowsSnare and policyname=Possible Privilege Escalation - Self Escalation".

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
