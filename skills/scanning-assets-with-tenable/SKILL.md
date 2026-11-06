---
name: scanning-assets-with-tenable
description: >-
  Given the IP address this playbook enriches Tenable.io information relevant to ASM alerts. Covers 4 vendor variants: Cortex Attack Surface Management, RiskIQ Digital Footprint, Tenable Vulnerability Management (formerly Tenable.io), Tenable.sc. Use when scanning assets with tenable must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: scanning, assets, with, tenable, vulnerability management. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

### Step 1: Confirm the finding

Reproduce the misconfiguration from the platform's own API or CLI.

### Step 2: Plan the change

Generate the exact command or template diff, and review it before applying.

### Step 3: Apply

Execute with the least privilege that accomplishes the fix, and capture the response.

### Step 4: Verify

Re-read the resource state and confirm it matches the expected secure state.

### Step 5: Record

Write the change, the approver, the verification, and the rollback.

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
# Generic REST call with a bearer token
curl -sS -X GET "https://api.example.com/v1/resource" \
  -H "Authorization: Bearer $API_TOKEN" -H "Accept: application/json"
```

## Verification

- The resource state matches the expected secure state.
- The change did not break dependent services.
- The rollback is documented and tested.
- The finding is closed with the evidence attached.

## Common Pitfalls

- Applying a fix without a dry run.
- Breaking a dependent service.
- Fixing one resource and leaving the pattern elsewhere.
- No rollback for a change that cannot be reversed.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and record template
- `scripts/agent.py` - runnable helper for this procedure
