---
name: scanning-networks-with-nmap
description: >-
  Sub-playbook that conducts a single port NMAP scan and returns results to the parent playbook. Covers 1 vendor variants: Nmap. Use when scanning networks with nmap must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: scanning, networks, with, nmap, network security. Do not use for the vendor-neutral procedure - use the matching generic skill.
domain: cybersecurity
subdomain: network-security
tags:
- network-security
- firewall
- containment
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- PR.AC-05
- DE.CM-01
- RS.MI-01
mitre_attack:
- T1595
- T1071
- T1105
---

# Scanning Networks with Nmap

## When to Use

- The environment uses one of: Nmap.
- scanning networks with nmap must be executed through a vendor API or console.
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

### NMAP - Single Port Scan

Source pack: Nmap

Sub-playbook that conducts a single port NMAP scan and returns results to the parent playbook.

Inputs:

- `RemoteIP`: Remote IP address in an incident/alert.
- `RemotePort`: Remote port number in an incident/alert.
- `NMAPOptions`: Options to be used for an Nmap scan. (We do "-p\<RemotePort>" by default and recommend using "-Pn" to skip a ping check.)

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
