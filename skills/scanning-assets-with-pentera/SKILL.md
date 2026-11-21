---
name: scanning-assets-with-pentera
description: >-
  Will run a pentera task given the Pentera task name. It will generate the full action report that contains all the actions that Pentera made during the scan, and will create incidents according to the filters in the Pentera Filter and Create incidents playbook. Covers 2 vendor variants: Pentera. Use when this procedure must run through one of these products, or when the vendor-neutral workflow needs the exact API or console steps. Keywords: scanning, assets, with, pentera, vulnerability management. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Scanning Assets with Pentera

## When to Use

- The environment uses one of: Pentera.
- scanning assets with pentera must be executed through a vendor API or console.
- An incident or audit needs a reproducible, vendor-specific record.

**Do not use** for the vendor-neutral procedure; use the matching generic skill.

## Prerequisites

- Access to the vendor console or API, and a credential with the required scope.
- The object identifier (host, account, resource, or indicator) and its provenance.
- A rollback path and a ticket for the change.

## Workflow

### Step 1: Preserve the artifact

Hash it before analysis and work on a copy.

### Step 2: Parse

Use the artifact-specific parser; record the tool and version.

### Step 3: Extract

Pull the fields that matter for the investigation, keeping context for each.

### Step 4: Normalize

Map to the shared schema, de-duplicate, and mark confidence.

### Step 5: Report

Write findings with the evidence path, the commands used, and the limits of the analysis.

## Vendor Variants

### Pentera Run Scan and Create Incidents

Source pack: Pentera

Will run a pentera task given the Pentera task name. It will generate the full action report that contains all the actions that Pentera made during the scan, and will create incidents according to the filters in the Pentera Filter and Create incidents playbook.

Inputs:

- `PenteraTaskName`: The name of the Pentera task to run.

### Pentera Run Scan

Source pack: Pentera

Vendor-specific implementation.

Inputs:

- `PenteraTaskName`: The name of the Pentera task to run

## Platform Commands

```bash
# Pentera: run a security test
curl -sS -X POST "https://<pentera>/api/v1/tests" \
  -H "Authorization: Bearer $PENTERA_TOKEN" -H "Content-Type: application/json" \
  -d '{"name":"INC-1234","targets":["203.0.113.10"],"profile":"full"}'

# Get test results
curl -sS "https://<pentera>/api/v1/tests/<test_id>" \
  -H "Authorization: Bearer $PENTERA_TOKEN" | jq '{status, findings}'
```

## Verification

- The artifact hash in the report matches the source.
- A second run produces the same findings.
- Every finding cites the field or byte range it came from.
- The report states what the analysis could not see.

## Common Pitfalls

- Analyzing the original instead of a copy.
- Claiming content that is encrypted or truncated.
- Dropping context when de-duplicating.
- No tool version, so the result is not reproducible.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and record template
- `scripts/agent.py` - runnable helper for this procedure
