---
name: inventorying-user-devices
description: >-
  Retrieves information on all of the associated user devices. In order to get a generic output, the following information on all of the retrieved devices will be saved under the UserDevices context key: Note that not all of the In order to get the full list of. Inventories devices from MDM, EDR, and IdP. Use when the assets behind user devices must be enumerated, or when an audit needs a current user devices inventory. Keywords: inventorying, user, devices, inventory, asset-management, soc operations. Do not use for investigating cloud user activity - use `investigating-cloud-user-activity`.
domain: cybersecurity
subdomain: soc-operations
tags:
- soc-operations
- siem
- triage
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- DE.AE-02
- RS.AN-03
- RS.MA-01
mitre_attack:
- T1078
- T1059
- T1566
---

# Inventorying User Devices

## When to Use

- An investigation needs the assets or devices associated with an entity.
- An audit needs a current inventory with ownership.
- A response action needs the full set of affected assets.

**Do not use** for investigating cloud user activity - use `investigating-cloud-user-activity`.

## Prerequisites

- Read access to the inventory sources: MDM, EDR, IdP, CMDB, or cloud.
- The identifier to resolve: user, email, host, or account.
- A reconciliation key so duplicates collapse.

## Workflow

### Step 1: Enumerate

Query each source for the identifier.

### Step 2: Normalize

Map to a common record with source, owner, and last-seen.

### Step 3: Reconcile

Collapse duplicates and flag conflicts between sources.

### Step 4: Report

Produce the inventory with provenance and gaps.

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

```bash
# Intune / MDM device lookup
az rest --method GET --url "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices?\$filter=userPrincipalName eq 'user@example.com'"
```

## Verification

- Every record names its source.
- Duplicates are collapsed with a documented rule.
- Conflicts between sources are flagged, not hidden.
- The inventory is reproducible from the saved queries.

## Common Pitfalls

- Trusting one source as complete.
- Collapsing records that are genuinely different.
- No last-seen timestamp.
- Ignoring stale records.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
