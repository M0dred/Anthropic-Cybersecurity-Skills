---
name: remediating-gcp-vpc-network-misconfiguration
description: >-
  Remediates GCP VPC Network alerts. Fixes overly broad ingress rules and default network exposure. Use when a finding about a GCP VPC network misconfiguration is confirmed and needs a fix, or when a compliance finding requires a GCP VPC network misconfiguration remediation. Keywords: remediating, gcp, vpc, network, misconfiguration, remediation, configuration, cloud security. Do not use for remediating gcp vm exposures - use `remediating-gcp-vm-exposures`.
domain: cybersecurity
subdomain: cloud-security
tags:
- cloud-security
- aws
- azure
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- PR.AC-05
- DE.CM-01
- RS.MI-01
mitre_attack:
- T1078.004
- T1530
- T1562.008
---

# Remediating GCP VPC Network Misconfiguration

## When to Use

- A misconfiguration or exposure is confirmed and needs a fix.
- A compliance finding requires a configuration change.
- A recovery action must restore service safely.

**Do not use** for remediating gcp vm exposures - use `remediating-gcp-vm-exposures`.

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
# GCP: inspect and fix the resource
gcloud compute firewall-rules list --format='table(name,sourceRanges,allowed)'
gcloud compute firewall-rules update deny-all-ingress --source-ranges 10.0.0.0/8
gcloud container clusters describe prod --zone us-central1-a --format='value(masterAuthorizedNetworksConfig)'
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
