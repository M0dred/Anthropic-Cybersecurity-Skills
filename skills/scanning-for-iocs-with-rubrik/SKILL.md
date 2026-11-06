---
name: scanning-for-iocs-with-rubrik
description: >-
  Starts an IOC Scan with the provided IOC values. It can be looped until recoverable snapshots are obtained or the limit to loop is reached. Use when a finding about backups for indicators through Rubrik is confirmed and needs a fix, or when a compliance finding requires backups for indicators through Rubrik remediation. Keywords: scanning, for, iocs, with, rubrik, remediation, configuration, ransomware defense. Do not use for scanning backups with veeam - use `scanning-backups-with-veeam`.
domain: cybersecurity
subdomain: ransomware-defense
tags:
- ransomware-defense
- backup
- recovery
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- PR.DS-11
- RC.RP-01
- RS.MI-01
mitre_attack:
- T1486
- T1490
- T1485
---

# Scanning for Iocs with Rubrik

## When to Use

- A misconfiguration or exposure is confirmed and needs a fix.
- A compliance finding requires a configuration change.
- A recovery action must restore service safely.

**Do not use** for scanning backups with veeam - use `scanning-backups-with-veeam`.

## Prerequisites

- The finding, its resource identifier, and the expected secure state.
- Change authority and a maintenance window where required.
- A dry-run or plan capability for the target platform.

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

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

```bash
# Rubrik Security Cloud
curl -X POST "https://<rubrik>/api/v1/fileset/request" \
  -H "Authorization: Bearer $RUBRIK_TOKEN" -H "Content-Type: application/json" \
  -d '{"filesetId":"<id>","paths":["/data"]}'
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
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
