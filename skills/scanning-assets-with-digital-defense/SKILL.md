---
name: scanning-assets-with-digital-defense
description: >-
  Pulls IP addresses from the detail value of an incident and check if that asset has been scanned within the past 60 days. If not then it will then prompt the user to perform a scan on the asset. Covers 1 vendor variants: Digital Defense Frontline VM. Use when this procedure must run through one of these products, or when the vendor-neutral workflow needs the exact API or console steps. Keywords: scanning, assets, with, digital, defense, vulnerability management. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Scanning Assets with Digital Defense

## When to Use

- The environment uses one of: Digital Defense Frontline VM.
- scanning assets with digital defense must be executed through a vendor API or console.
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

### Digital Defense FrontlineVM - Scan Asset Not Recently Scanned

Source pack: Digital Defense Frontline VM

Pulls IP addresses from the detail value of an incident and check if that asset has been scanned within the past 60 days. If not then it will then prompt the user to perform a scan on the asset.

## Platform Commands

```bash
# Digital Defense Frontline VM: list assets
curl -sS "https://api.digitaldefense.com/v1/assets?ip=203.0.113.10" \
  -H "Authorization: Bearer $DD_TOKEN" | jq '.assets[] | {id, hostname, vulnerabilities}'

# Trigger a scan
curl -sS -X POST "https://api.digitaldefense.com/v1/scans" \
  -H "Authorization: Bearer $DD_TOKEN" -H "Content-Type: application/json" \
  -d '{"targets":["203.0.113.10"],"profile":"standard"}'
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
