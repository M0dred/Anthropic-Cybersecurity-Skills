---
name: recovering-vms-with-veeam
description: >-
  Starts Instant VM Recovery with automatic configuration. Uses Instant VM Recovery and SureBackup. Use when a finding about virtual machines through Veeam is confirmed and needs a fix, or when a compliance finding requires virtual machines through Veeam remediation. Keywords: recovering, vms, with, veeam, remediation, configuration, ransomware defense. Do not use for scanning backups with veeam - use `scanning-backups-with-veeam`.
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

# Recovering Vms with Veeam

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

```powershell
# Veeam Backup & Replication
Connect-VBRServer -Server vbr.example.com
Start-VBRInstantRecovery -RestorePoint (Get-VBRRestorePoint -Name "VM-01") -VMName "VM-01-restored"
Start-VBRScanBackup -RestorePoint (Get-VBRRestorePoint -Name "VM-01")
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
