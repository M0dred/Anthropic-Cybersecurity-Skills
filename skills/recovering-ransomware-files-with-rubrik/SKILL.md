---
name: recovering-ransomware-files-with-rubrik
description: >-
  Performs an IOC Scan based on the provided inputs, search the recoverable snapshot and performs recovery on the searched recoverable snapshot. This also creates tickets on ServiceNow using "ServiceNow v2" integration. Use when a finding about ransomware-affected files through Rubrik is confirmed and needs a fix, or when a compliance finding requires ransomware-affected files through Rubrik remediation. Keywords: recovering, ransomware, files, with, rubrik, remediation, configuration, ransomware defense. Do not use for responding to ransomware anomalies with rubrik - use `responding-to-ransomware-anomalies-with-rubrik`.
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

# Recovering Ransomware Files with Rubrik

## When to Use

- A misconfiguration or exposure is confirmed and needs a fix.
- A compliance finding requires a configuration change.
- A recovery action must restore service safely.

**Do not use** for responding to ransomware anomalies with rubrik - use `responding-to-ransomware-anomalies-with-rubrik`.

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
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
