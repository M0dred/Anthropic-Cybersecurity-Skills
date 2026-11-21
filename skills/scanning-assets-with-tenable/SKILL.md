---
name: scanning-assets-with-tenable
description: >-
  Launches an existing Tenable.sc scan by scan ID and waits for the scan to finish by polling its status in pre-defined intervals. Covers 4 vendor variants: Cortex Attack Surface Management, RiskIQ Digital Footprint, Tenable Vulnerability Management (formerly Tenable.io), Tenable.sc. Use when this procedure must run through one of these products, or when the vendor-neutral workflow needs the exact API or console steps. Keywords: scanning, assets, with, tenable, vulnerability management. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Scanning Assets with Tenable

## When to Use

- The environment uses one of: Cortex Attack Surface Management, RiskIQ Digital Footprint, Tenable Vulnerability Management (formerly Tenable.io), Tenable.sc.
- scanning assets with tenable must be executed through a vendor API or console.
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

### Cortex ASM - Tenable.io Enrichment

Source pack: Cortex Attack Surface Management

Given the IP address this playbook enriches Tenable.io information relevant to ASM alerts.

Inputs:

- `Indicator Query`: Indicators matching the indicator query will be used as playbook input
- `IPAddress`: IP addresses to enrich.

### Launch Scan - Tenable.sc

Source pack: Tenable.sc

Launches an existing Tenable.sc scan by scan ID and waits for the scan to finish by polling its status in pre-defined intervals.

Inputs:

- `ScanID`: The scan ID to launch.
- `diagnosticTarget`: The valid IP address/hostname of a specific target to scan. Must be provided with diagnosticPassword.
- `diagnosticPassword`: The non-empty string password.

### Tenable.io Scan

Source pack: Tenable Vulnerability Management (formerly Tenable.io)

Runs a Tenable.io scan.

Inputs:

- `scan-id`: The ID of the tenable scan to run.
- `targets`: The alternative targets list to the scan's configured targets.

### Vulnerability Scan - RiskIQ Digital Footprint - Tenable.io

Source pack: RiskIQ Digital Footprint

Performs a vulnerability scan for an asset of type "Host" and "IP Address" using Tenable.io integration. Supported integration.

Inputs:

- `asset_name`: Name of the asset.
- `asset_type`: Type of the asset. Possible values: Domain, Host, IP Address, IP Block, ASN, Page, SSL Cert, Contact.

## Platform Commands

```bash
# Tenable.io: launch a scan
curl -sS -X POST "https://cloud.tenable.com/scans" \
  -H "X-ApiKeys: accessKey=$TIO_ACCESS;secretKey=$TIO_SECRET" \
  -H "Content-Type: application/json" \
  -d '{"uuid":"<template-uuid>","settings":{"name":"INC-1234","text_targets":"203.0.113.10"}}'

# Get scan status
curl -sS "https://cloud.tenable.com/scans/<scan_id>" \
  -H "X-ApiKeys: accessKey=$TIO_ACCESS;secretKey=$TIO_SECRET" | jq '.status'
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
