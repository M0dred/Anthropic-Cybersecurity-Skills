---
name: hunting-with-logzio
description: >-
  Handles a Logz.io Alert by retrieving the events that generated it. Covers 2 vendor variants: Logz.io. Use when hunting with logzio must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: hunting, with, logzio, threat hunting. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Hunting with Logzio

## When to Use

- The environment uses one of: Logz.io.
- hunting with logzio must be executed through a vendor API or console.
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

### Logz.Io Handle Alert

Source pack: Logz.io

Handles a Logz.io Alert by retrieving the events that generated it.

Inputs:

- `AlertEventID`: Logz.Io Alert Event ID

### Logz.io Indicator Hunting

Source pack: Logz.io

Queries Logz.io in order to hunt indicators such as File Hashes IP Addresses Domains \ URLS And outputs the related users, IP addresses, host names for the indicators searched.

Inputs:

- `MD5`: MD5 hash file or an array of hashes for which to search
- `LogzioMD5Field`: The name of the fields in Logz.io for which you would like to search the MD5 values
- `Multiple fields is available by using comma-separated`: 
- `SHA1`: SHA1 hash file or an array of hashes for which to search
- `LogzioSHA1Field`: The name of the fields in Logz.io for which you would like to search the SHA1 values
- `Multiple fields is available by using comma-separated`: 
- `SHA256`: SHA256 hash file or an array of hashes for which to search
- `LogzioSHA256Field`: The name of the fields in Logz.io for which you would like to search the SHA256 values

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
