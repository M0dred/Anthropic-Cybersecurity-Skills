---
name: investigating-access-incidents
description: >-
  Investigates an access incident by gathering user and IP information, and handling the incident based on the stages in "Handling an incident - Computer Security Incident Handling Guide" by NIST. Used Sub-playbooks. Covers 3 vendor variants: Access Investigation, IBM QRadar, NIST. Use when investigating access incidents must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: investigating, access, incidents, incident response. Do not use for the vendor-neutral procedure - use the matching generic skill.
domain: cybersecurity
subdomain: incident-response
tags:
- incident-response
- containment
- soc-operations
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.MA-01
- RS.MI-01
- RS.AN-03
mitre_attack:
- T1486
- T1566
- T1078
---

# Investigating Access Incidents

## When to Use

- The environment uses one of: Access Investigation, IBM QRadar, NIST.
- investigating access incidents must be executed through a vendor API or console.
- An incident or audit needs a reproducible, vendor-specific record.

**Do not use** for the vendor-neutral procedure; use the matching generic skill.

## Prerequisites

- Access to the vendor console or API, and a credential with the required scope.
- The object identifier (host, account, resource, or indicator) and its provenance.
- A rollback path and a ticket for the change.

## Workflow

### Step 1: Scope the entity

Resolve the identifier to all of its identities and assets.

### Step 2: Collect evidence

Pull authentication, process, network, and cloud audit events for the window.

### Step 3: Build the timeline

Order events, resolve time zones, and mark the first and last malicious action.

### Step 4: Test hypotheses

Distinguish the observed facts from the inference, and check alternative explanations.

### Step 5: Conclude

State the verdict, the confidence, and the recommended containment.

## Vendor Variants

### Access Investigation - Generic - NIST

Source pack: NIST

Investigates an access incident by gathering user and IP information, and handling the incident based on the stages in "Handling an incident - Computer Security Incident Handling Guide" by NIST. Used Sub-playbooks.

Inputs:

- `SrcIP`: The source IP address from which the incident originated.
- `DstIP`: The target IP address that was accessed.
- `Username`: The email address of the account that was used to access the DstIP.
- `NotifyEmail`: Email addresses to notify about the incident.
- `RemediationSLA`: The Remediation SLA for the 'Containment, Eradication, and Recovery' stage (in minutes).
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be

### Access Investigation - Generic

Source pack: Access Investigation

Investigates an access incident by gathering user and IP information. The playbook then interacts with the user that triggered the incident to confirm whether or not they initiated the access action.

Inputs:

- `SrcIP`: The source IP address from which the incident originated.
- `DstIP`: The target IP address that was accessed.
- `Username`: The username of the account that was used to access the DstIP.
- `Role`: The default role to assign the incident to.
- `OnCall`: Set to true to assign only the users that are currently on shift. Requires the platform.5 or later.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be

### Access Investigation - QRadar

Source pack: IBM QRadar

Investigates an Access incident by gathering user and IP address information. The playbook then interacts with the user that triggered the incident to confirm whether or not they initiated the access action.

## Platform Commands

```bash
# Generic REST call with a bearer token
curl -sS -X GET "https://api.example.com/v1/resource" \
  -H "Authorization: Bearer $API_TOKEN" -H "Accept: application/json"
```

## Verification

- Every timeline entry has a source and a timestamp.
- The verdict distinguishes facts from inference.
- Alternative explanations are addressed.
- The evidence is attached to the case.

## Common Pitfalls

- Confirmation bias toward the first alert.
- Mixing time zones in the timeline.
- Treating a single log line as proof.
- Closing without checking lateral movement.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and record template
- `scripts/agent.py` - runnable helper for this procedure
