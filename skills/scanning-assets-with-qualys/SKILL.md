---
name: scanning-assets-with-qualys
description: >-
  Given the IP address this playbook enriches information from Qualys assets. Covers 3 vendor variants: Cortex Attack Surface Management, Qualys. Use when scanning assets with qualys must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: scanning, assets, with, qualys, vulnerability management. Do not use for the vendor-neutral procedure - use the matching generic skill.
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
