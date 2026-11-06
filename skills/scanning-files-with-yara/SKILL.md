---
name: scanning-files-with-yara
description: >-
  A playbook to run YARA scan against uploaded file. To run the playbook, provide the YARA rule content and the entry ID of the file you intend to scan. Covers 1 vendor variants: Yara. Use when scanning files with yara must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: scanning, files, with, yara, malware analysis. Do not use for the vendor-neutral procedure - use the matching generic skill.
domain: cybersecurity
subdomain: malware-analysis
tags:
- malware-analysis
- sandbox
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.MI-01
mitre_attack:
- T1078
---

# Scanning Files with Yara

## When to Use

- The environment uses one of: Yara.
- scanning files with yara must be executed through a vendor API or console.
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

### YARA - File Scan

Source pack: Yara

A playbook to run YARA scan against uploaded file. To run the playbook, provide the YARA rule content and the entry ID of the file you intend to scan.

Inputs:

- `EntryID`: The entry ID of a file to scan
- `YARA`: The YARA rule content

## Platform Commands

```bash
# CrowdStrike Falcon
curl -X POST "https://api.crowdstrike.com/devices/entities/devices-actions/v2?action_name=contain" \
  -H "Authorization: Bearer $CS_TOKEN" -H "Content-Type: application/json" \
  -d '{"ids":["<device_id>"]}'
curl "https://api.crowdstrike.com/devices/queries/devices/v1?filter=hostname:'WEB-01'" \
  -H "Authorization: Bearer $CS_TOKEN"
```

```bash
# Microsoft Defender for Endpoint
curl -X POST "https://api.securitycenter.microsoft.com/api/machines/<id>/isolate" \
  -H "Authorization: Bearer $MDE_TOKEN" -H "Content-Type: application/json" \
  -d '{"Comment":"INC-1234","IsolationType":"Full"}'
curl "https://api.securitycenter.microsoft.com/api/machines?\$filter=computerDnsName eq 'WEB-01'" \
  -H "Authorization: Bearer $MDE_TOKEN"
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
