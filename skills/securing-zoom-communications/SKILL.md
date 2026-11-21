---
name: securing-zoom-communications
description: >-
  Secures Zoom meetings and communications: configure waiting rooms, restrict screen sharing, prevent Zoom bombing, audit cloud recordings, and enforce authentication requirements. Use when Zoom meetings are disrupted, when confidential meetings need protection, when cloud recordings contain sensitive data, or when configuring enterprise Zoom security. Keywords: Zoom security, Zoom bombing, meeting security, Zoom waiting room, Zoom recording.
  Do not use for other purposes - use the matching skill for your task.
domain: cybersecurity
subdomain: cloud-security
tags:
- cloudsecurity
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

# Securing Zoom Communications

## When to Use

- Zoom meetings need security hardening or a Zoom incident occurred
- An analyst needs a repeatable procedure with verification steps.
- The task involves cloud security and requires documented evidence.

**Do not use** for tasks outside cloud security; use the matching skill.

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
