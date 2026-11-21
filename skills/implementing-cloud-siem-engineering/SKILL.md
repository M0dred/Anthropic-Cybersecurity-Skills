---
name: implementing-cloud-siem-engineering
description: >-
  Engineers cloud-native SIEM: deploy Splunk Cloud, Sentinel, or Chronicle, optimize ingestion pipelines, manage retention and cost, and build detections for cloud workloads. Use when migrating SIEM to cloud, when cloud log ingestion costs spike, when building cloud-native detections, or when managing multi-cloud SIEM. Keywords: cloud SIEM, Splunk Cloud, Sentinel engineering, Chronicle, cloud detection.
  Do not use for other purposes - use the matching skill for your task.
domain: cybersecurity
subdomain: soc-operations
tags:
- socoperations
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

# Implementing Cloud SIEM Engineering

## When to Use

- cloud SIEM needs engineering, optimization, or migration
- An analyst needs a repeatable procedure with verification steps.
- The task involves soc operations and requires documented evidence.

**Do not use** for tasks outside soc operations; use the matching skill.

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
