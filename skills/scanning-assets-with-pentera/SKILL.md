---
name: scanning-assets-with-pentera
description: >-
  Will run a pentera task given the Pentera task name. It will generate the full action report that contains all the actions that Pentera made during the scan, and will create incidents according to the filters in the Pentera Filter and Create incidents playbook. Covers 2 vendor variants: Pentera. Use when scanning assets with pentera must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: scanning, assets, with, pentera, vulnerability management. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Scanning Assets with Pentera

## When to Use

- The environment uses one of: Pentera.
- scanning assets with pentera must be executed through a vendor API or console.
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

### Pentera Run Scan and Create Incidents

Source pack: Pentera

Will run a pentera task given the Pentera task name. It will generate the full action report that contains all the actions that Pentera made during the scan, and will create incidents according to the filters in the Pentera Filter and Create incidents playbook.

Inputs:

- `PenteraTaskName`: The name of the Pentera task to run.

### Pentera Run Scan

Source pack: Pentera

Vendor-specific implementation.

Inputs:

- `PenteraTaskName`: The name of the Pentera task to run

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
