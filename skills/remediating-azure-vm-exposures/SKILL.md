---
name: remediating-azure-vm-exposures
description: >-
  Handles exposure issue remediation for cloud hosted Virtual Machines by modifying cloud network security settings to block public access to the exposed service port. Targets Azure VMs, network security groups, and public IP resources using az vm list and az network nsg rule. Use when a finding about Azure virtual-machine exposures is confirmed and needs a fix, or when a compliance finding requires Azure virtual-machine exposures remediation. Keywords: remediating, azure, exposures, remediation, configuration, vulnerability management. Do not use for remediating aws vm exposures - use `remediating-aws-vm-exposures`.
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

# Remediating Azure Vm Exposures

## When to Use

- A misconfiguration or exposure is confirmed and needs a fix.
- A compliance finding requires a configuration change.
- A recovery action must restore service safely.

**Do not use** for remediating aws vm exposures - use `remediating-aws-vm-exposures`.

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
# Azure: inspect and fix the resource
az storage account show -g rg-prod -n mystorage --query '{https:enableHttpsTrafficOnly,minTls:minimumTlsVersion,public:allowBlobPublicAccess}'
az storage account update -g rg-prod -n mystorage --https-only true --min-tls-version TLS1_2 --allow-blob-public-access false
az aks show -g rg-prod -n aks-prod --query '{rbac:enableRbac,net:networkProfile}'
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
