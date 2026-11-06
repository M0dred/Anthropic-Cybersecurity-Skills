---
name: enriching-incidents-with-group-ib
description: >-
  Handles postprocessing of violation incidents detected by Group-IB Digital Risk Protection. A violation incident is closed when the work on the violation is over: as Resolved when Group-IB DRP reports the violation as resolved (taken down; older API versions spell it solved) or legal (handed to legal), and as False Positive when DRP found it false (false_status) or the customer rejected it. Approving a violation. Covers 2 vendor variants: Group-IB Digital Risk Protection, Group-IB Threat Intelligence. Use when enriching incidents with group ib must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: enriching, incidents, with, group, ib, threat intelligence. Do not use for the vendor-neutral procedure - use the matching generic skill.
domain: cybersecurity
subdomain: threat-intelligence
tags:
- threat-intelligence
- ioc
- enrichment
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- ID.RA-01
- DE.AE-02
- RS.AN-03
mitre_attack:
- T1588.001
- T1071
- T1595
---

# Enriching Incidents with Group Ib

## When to Use

- The environment uses one of: Group-IB Digital Risk Protection, Group-IB Threat Intelligence.
- enriching incidents with group ib must be executed through a vendor API or console.
- An incident or audit needs a reproducible, vendor-specific record.

**Do not use** for the vendor-neutral procedure; use the matching generic skill.

## Prerequisites

- Access to the vendor console or API, and a credential with the required scope.
- The object identifier (host, account, resource, or indicator) and its provenance.
- A rollback path and a ticket for the change.

## Workflow

### Step 1: Validate the value

Reject private, reserved, malformed, or out-of-scope entries before any API call.

### Step 2: Query the sources

Run the enabled sources in parallel where possible, and record failures as failures rather than as clean results.

### Step 3: Normalize

Map each source's fields into one schema with the source name attached to every value.

### Step 4: Score confidence

Combine independent signals with explicit weights; cap the score when fewer than two sources respond.

### Step 5: Hand off

Attach the record to the incident and pass the decision to the containment or escalation skill.

## Vendor Variants

### Group-IB Digital Risk Protection - Violation Incident Postprocessing

Source pack: Group-IB Digital Risk Protection

Handles postprocessing of violation incidents detected by Group-IB Digital Risk Protection. A violation incident is closed when the work on the violation is over: as Resolved when Group-IB DRP reports the violation as resolved (taken down; older API versions spell it solved) or legal (handed to legal), and as False Positive when DRP found it false (false_status) or the customer rejected it. Approving a violation does not close the incident - it only settles the customer's decision, and the take-down carries on afterwards - unless the instance has Close the incident when a violation is approved enabled, in which case GIBDRPResolveViolation closes it with the approval. Incidents whose violation ends later are closed by the GIBDRPIncidentUpdate pre-processing rule, which sees the change arrive on the next fetch. The playbook's first two conditions cover a violation that is already over when its incident is created; the fetch does not create incidents for such violations, so this is a safeguard for incidents created another way. When the incident's GIB DRP Indicator Wanted field is set - the fetch sets it for the violation types selected in Create indicators from Violations on the instance - the playbook runs GIBDRPCreateViolationIndicator, which creates the indicator from the violation URI, linked to the incident and with Group-IB Digital Risk Protection as its source. While Group-IB DRP is waiting for the customer - status detected and approve state under_review - the playbook.

### Incident Postprocessing - Group-IB Threat Intelligence & Attribution

Source pack: Group-IB Threat Intelligence

Obtains additional information on the threat actor involved in the incident and associates related indicators to the incident.

## Platform Commands

```bash
# Generic REST call with a bearer token
curl -sS -X GET "https://api.example.com/v1/resource" \
  -H "Authorization: Bearer $API_TOKEN" -H "Accept: application/json"
```

## Verification

- Every enabled source appears in either the success or failure list.
- The confidence score is reproducible from the component signals.
- Cached values carry the original lookup timestamp.
- No credentials appear in the output.

## Common Pitfalls

- Treating no reports as clean.
- Ignoring shared infrastructure.
- Burning the daily quota on a /24.
- Using stale reputation without recording the lookup time.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and record template
- `scripts/agent.py` - runnable helper for this procedure
