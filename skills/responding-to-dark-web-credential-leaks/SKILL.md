---
name: responding-to-dark-web-credential-leaks
description: >-
  Gets the affected username of a Bechtle Dark Web Scan issue, then sends an email for human confirmation if the affected user should be blocked. Covers 1 vendor variants: Bechtle Dark Web Scan. Use when responding to dark web credential leaks must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: responding, to, dark, web, credential, leaks, identity access management. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Responding To Dark Web Credential Leaks

## When to Use

- The environment uses one of: Bechtle Dark Web Scan.
- responding to dark web credential leaks must be executed through a vendor API or console.
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

### DarkWebScan Block AD User Human-in-the-loop

Source pack: Bechtle Dark Web Scan

Gets the affected username of a Bechtle Dark Web Scan issue, then sends an email for human confirmation if the affected user should be blocked.

Inputs:

- `IssueID`: Issue ID
- `Severity`: Issue Severity
- `Details`: Issue Details
- `IssueUsername`: Username as reported from the Dark Web Scan Integration Evidence
- `UsernameWithoutDomain`: The username but with the mail domain removed (e.g. @example.org)
- `SendMailsTo`: Send all email notifications from this playbook to this email address

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
