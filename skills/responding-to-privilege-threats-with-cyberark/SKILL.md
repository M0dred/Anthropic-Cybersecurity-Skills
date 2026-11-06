---
name: responding-to-privilege-threats-with-cyberark
description: >-
  Deactivates a specific CyberArk EPM SOC risk plan for a specific endpoint. This reverts all security settings to the baseline EPM policies active prior to the SOC response action. Covers 2 vendor variants: CyberArk Endpoint Privilege Manager. Use when responding to privilege threats with cyberark must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: responding, to, privilege, threats, with, cyberark, identity access management. Do not use for the vendor-neutral procedure - use the matching generic skill.
domain: cybersecurity
subdomain: identity-access-management
tags:
- identity-access-management
- iam
- containment
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- PR.AC-01
- PR.AC-04
- RS.MI-01
mitre_attack:
- T1078
- T1098
- T1556
---

# Responding To Privilege Threats with Cyberark

## When to Use

- The environment uses one of: CyberArk Endpoint Privilege Manager.
- responding to privilege threats with cyberark must be executed through a vendor API or console.
- An incident or audit needs a reproducible, vendor-specific record.

**Do not use** for the vendor-neutral procedure; use the matching generic skill.

## Prerequisites

- Access to the vendor console or API, and a credential with the required scope.
- The object identifier (host, account, resource, or indicator) and its provenance.
- A rollback path and a ticket for the change.

## Workflow

### Step 1: Confirm entry criteria

Verify the facts that justify this phase.

### Step 2: Plan

List the actions, the owner, and the expected effect.

### Step 3: Execute

Perform the actions, capturing output and timestamps.

### Step 4: Verify

Confirm the phase objective is met.

### Step 5: Record

Write the decision log and the exit criteria.

## Vendor Variants

### CyberArk Deactivate EPM SOC Response

Source pack: CyberArk Endpoint Privilege Manager

Deactivates a specific CyberArk EPM SOC risk plan for a specific endpoint. This reverts all security settings to the baseline EPM policies active prior to the SOC response action.

Inputs:

- `endpoint_name`: The Hostname of the target endpoint.
- `logged_in_user`: The logged-in user of the target endpoint.
- `risk_plan`: The name of the risk plan to remove (i.e. Medium_Risk_Endpoint or High_Risk_Endpoint).

### CyberArk EPM SOC Response

Source pack: CyberArk Endpoint Privilege Manager

Activates a CyberArk EPM SOC risk plan for a specified endpoint, based on the incident severity. Endpoint name and external IP are taken from the incident to uniquely identify the on EPM.

Inputs:

- `endpoint_name`: Hostname of target endpoint.
- `logged_in_user`: Logged in user name of target endpoint.

## Platform Commands

```bash
# Generic REST call with a bearer token
curl -sS -X GET "https://api.example.com/v1/resource" \
  -H "Authorization: Bearer $API_TOKEN" -H "Accept: application/json"
```

## Verification

- The phase objective is met and evidenced.
- Every action has an owner and a timestamp.
- The decision log explains the choices.
- The next phase's entry criteria are stated.

## Common Pitfalls

- Skipping the evidence capture.
- Moving phases without exit criteria.
- No decision log.
- Losing the incident timeline.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and record template
- `scripts/agent.py` - runnable helper for this procedure
