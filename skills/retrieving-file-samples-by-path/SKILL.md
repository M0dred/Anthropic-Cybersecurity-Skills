---
name: retrieving-file-samples-by-path
description: >-
  Returns a file sample from a specified path and host that you input in the following. Uses the absolute path and hostname. Use when file samples by path must be collected as evidence, or when volatile data about file samples by path must be preserved. Keywords: retrieving, file, samples, path, acquisition, forensics, endpoint security. Do not use for retrieving file samples by hash - use `retrieving-file-samples-by-hash`.
domain: cybersecurity
subdomain: endpoint-security
tags:
- endpoint-security
- edr
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.MI-01
- PR.AC-05
- DE.CM-01
mitre_attack:
- T1059
- T1021
- T1562
---

# Retrieving File Samples by Path

## When to Use

- An incident requires forensic evidence from a host or capture point.
- A review or legal process needs a defensible acquisition.
- Volatile data must be preserved before containment or reboot.

**Do not use** for retrieving file samples by hash - use `retrieving-file-samples-by-hash`.

## Prerequisites

- Authorization and scope for the acquisition.
- A target directory with enough space, and a write blocker where required.
- The transport: local, WinRM, SSH, or an agent.

## Workflow

### Step 1: Authorize and scope

Record who approved the acquisition and what is in scope.

### Step 2: Capture volatile data first

Memory, processes, sockets, and logged-on users before anything changes.

### Step 3: Capture persistent data

Registry, MFT, event logs, and file system metadata.

### Step 4: Hash and record

SHA-256 every artifact and record the tool, version, and time.

### Step 5: Transfer and store

Move to evidence storage, verify the hash after transfer, and restrict access.

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

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

- Every artifact has a hash that matches after transfer.
- The chain-of-custody form is complete.
- The acquisition did not alter the source more than documented.
- The evidence is stored with access controls.

## Common Pitfalls

- Rebooting before memory capture.
- Writing to the evidence disk.
- Missing the hash after transfer.
- Acquiring beyond the authorized scope.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
