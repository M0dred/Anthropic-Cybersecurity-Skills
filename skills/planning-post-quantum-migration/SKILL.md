---
name: planning-post-quantum-migration
description: >-
  Plans migration to post-quantum cryptography: inventory cryptographic assets, assess quantum vulnerability, prioritize migration by risk, and implement hybrid classical-PQC algorithms. Use when planning for quantum threats, when cryptographic inventory is needed, when compliance requires PQC readiness, or when building a crypto migration roadmap. Keywords: post-quantum, PQC migration, NIST PQC, quantum readiness, crypto inventory.
  Do not use for other purposes - use the matching skill for your task.
domain: cybersecurity
subdomain: cryptography
tags:
- cryptography
- security
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- DE.CM-01
- RS.AN-03
- PR.AC-05
mitre_attack:
- T1078
- T1566
- T1059
---

# Planning Post-Quantum Migration

## When to Use

- post-quantum migration planning and cryptographic inventory needed
- An analyst needs a repeatable procedure with verification steps.
- The task involves cryptography and requires documented evidence.

**Do not use** for tasks outside cryptography; use the matching skill.

## Prerequisites

- Access to the target system or platform with appropriate authorization.
- The required credentials and API tokens for this procedure.
- A rollback path and a ticket for any changes.

## Workflow

### Step 1: Validate the scope

Confirm the target, the authorization, and the expected outcome. Record the
starting state so the change can be verified and rolled back.

### Step 2: Execute the procedure

Run the commands or API calls for this procedure. Capture the exact request
and response for the evidence record.

### Step 3: Verify

Confirm the outcome matches the expected state. Run an independent check
from a second vantage point where possible.

### Step 4: Record

Document the change, the operator, the ticket, the timestamp, and the
rollback command in the incident or change record.

## Verification

- The procedure completed without errors and produced the expected output.
- The output contains the expected fields and indicators.
- The change is recorded with the tool, version, timestamp, and operator.

## Common Pitfalls

- Skipping the dry run or plan phase before making changes.
- Not recording the starting state, making rollback impossible.
- No independent verification of the outcome.

## References

- `references/api-reference.md` - commands and usage for this procedure
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and record template
- `scripts/agent.py` - runnable helper for this procedure
