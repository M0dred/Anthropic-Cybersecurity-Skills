---
name: scanning-assets-with-qualys
description: >-
  Launches a PC scan and fetches the scan when it's ready. Covers 3 vendor variants: Cortex Attack Surface Management, Qualys. Use when this procedure must run through one of these products, or when the vendor-neutral workflow needs the exact API or console steps. Keywords: scanning, assets, with, qualys, vulnerability management. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Scanning Assets with Qualys

## When to Use

- The environment uses one of: Cortex Attack Surface Management, Qualys.
- scanning assets with qualys must be executed through a vendor API or console.
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

### Cortex ASM - Qualys Enrichment

Source pack: Cortex Attack Surface Management

Given the IP address this playbook enriches information from Qualys assets.

Inputs:

- `QualysIP`: Remote IP in alert.

### Launch And Fetch PC Scan - Qualys

Source pack: Qualys

Launches a PC scan and fetches the scan when it's ready.

Inputs:

- `scan_title`: The scan title. This can be a maximum of 2000 characters (ascii).
- `target_from`: Specify “assets” (the default) when your scan target will include IP addresses/ranges and/or asset groups. Specify “tags” when your scan target will include ass
- `ip`: The IP addresses to be scanned. You may enter individual IP addresses and/or ranges. Multiple entries are comma separated. One of these parameters is required: 
- `asset_groups`: The titles of asset groups containing the hosts to be scanned. Multiple titles are comma separated. One of these parameters is required: ip, asset_groups or ass
- `asset_group_ids`: The IDs of asset groups containing the hosts to be scanned. Multiple IDs are comma separated. One of these parameters is required: ip, asset_groups or asset_gro
- `exclude_ip_per_scan`: The IP addresses to be excluded from the scan when the scan target is specified as IP addresses (not asset tags). You may enter individual IP addresses and/or r
- `tag_include_selector`: Select “any” (the default) to include hosts that match at least one of the selected tags. Select “all” to include hosts that match all of the selected tags.
- `tag_exclude_selector`: Select “any” (the default) to exclude hosts that match at least one of the selected tags. Select “all” to exclude hosts that match all of the selected tags.

### Launch And Fetch VM Scan - Qualys

Source pack: Qualys

Launches a scan and fetches the scan when it's ready.

Inputs:

- `scan_title`: The scan title. This can be a maximum of 2000 characters (ascii).
- `target_from`: Specify “assets” (the default) when your scan target will include IP addresses/ranges and/or asset groups. Specify “tags” when your scan target will include ass
- `ip`: The IP addresses to be scanned. You may enter individual IP addresses and/or ranges. Multiple entries are comma separated. One of these parameters is required: 
- `asset_groups`: The titles of asset groups containing the hosts to be scanned. Multiple titles are comma separated. One of these parameters is required: ip, asset_groups or ass
- `asset_group_ids`: The IDs of asset groups containing the hosts to be scanned. Multiple IDs are comma separated. One of these parameters is required: ip, asset_groups or asset_gro
- `exclude_ip_per_scan`: The IP addresses to be excluded from the scan when the scan target is specified as IP addresses (not asset tags). You may enter individual IP addresses and/or r
- `tag_include_selector`: Select “any” (the default) to include hosts that match at least one of the selected tags. Select “all” to include hosts that match all of the selected tags.
- `tag_exclude_selector`: Select “any” (the default) to exclude hosts that match at least one of the selected tags. Select “all” to exclude hosts that match all of the selected tags.

## Platform Commands

```bash
# Qualys: launch a vulnerability scan
curl -sS -X POST "https://qualysapi.qualys.com/api/2.0/fo/scan/" \
  -H "X-Requested-With: curl" -u "$QUALYS_USER:$QUALYS_PASS" \
  -d "action=launch&scan_title=INC-1234&ip=203.0.113.10&option_title=Initial+Options"

# Fetch scan results
curl -sS "https://qualysapi.qualys.com/api/2.0/fo/scan/?action=fetch&scan_ref=scan/12345678.12345" \
  -H "X-Requested-With: curl" -u "$QUALYS_USER:$QUALYS_PASS" -o scan_result.xml
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
