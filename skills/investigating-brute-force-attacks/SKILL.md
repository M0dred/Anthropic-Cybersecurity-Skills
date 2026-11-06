---
name: investigating-brute-force-attacks
description: >-
  Investigates a "Brute Force" incident by gathering user and IP information, and calculating the incident severity based on the gathered information and information received from the user. It then performs remediation. This is done based on the phases for handling an incident as they are described in the SANS Institute â€˜Incident Handlerâ€™s Handbookâ€™ by Patrick Kral. The playbook handles the following. Covers 3 vendor variants: Brute Force, CyberArk Identity, SANS. Use when investigating brute force attacks must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: investigating, brute, force, attacks, incident response. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Investigating Brute Force Attacks

## When to Use

- The environment uses one of: Brute Force, CyberArk Identity, SANS.
- investigating brute force attacks must be executed through a vendor API or console.
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

### Brute Force Investigation - Generic - SANS

Source pack: SANS

Investigates a "Brute Force" incident by gathering user and IP information, and calculating the incident severity based on the gathered information and information received from the user. It then performs remediation. This is done based on the phases for handling an incident as they are described in the SANS Institute â€˜Incident Handlerâ€™s Handbookâ€™ by Patrick Kral. The playbook handles the following use-cases: Used Sub-playbooks: ***Disclaimer: This playbook does not ensure compliance to SANS regulations.

Inputs:

- `username`: Username of the user who is suspected of the activity.
- `traps_endpoint_id`: Traps endpoint ID, used for endpoint isolation.
- `logins_count_threshold`: The threshold for number of logins, from which the investigation and remediation will start automatically without waiting for the user's reply. Default is 10.
- `severity_threshold`: The threshold for the severity value from which an automatic remediation takes place. Specify the severity number (default is Critical):0 - Unknown0.5 - Informa
- `internal_range`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be
- `critical_users`: Critical users, separated by comma.
- `critical_endpoints`: Critical endpoints, separated by comma.
- `critical_groups`: Critical groups, separated by comma.

### Brute Force Investigation - Generic

Source pack: Brute Force

Investigates a "Brute Force" incident by gathering user and IP information, calculating the incident severity based on the gathered information and information received from the user, and performs remediation. The playbook handles the following use-cases: Used Sub-playbooks.

Inputs:

- `username`: Username of the user who is suspected of the activity.
- `src`: Source endpoint that triggered the incident.
- `traps_endpoint_id`: Traps endpoint ID, used for endpoint isolation.
- `logins_count_threshold`: The threshold for number of logins, from which the investigation and remediation will start automatically without waiting for the user"s reply. Default is 10.
- `severity_threshold`: The threshold for the severity value from which an automatic remediation takes place. Specify the severity number (default is Critical): 0 - Unknown, 0.5 - Info
- `internal_range`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be
- `critical_users`: Critical users, separated by comma.
- `critical_endpoints`: Critical endpoints, separated by comma.

### CyberArk - Brute Force_Investigation

Source pack: CyberArk Identity

Investigates a “Brute Force” incident by gathering user and IP information and performs remediation based on the information gathered and received from the user. Used Sub-playbooks: If you wish to link this playbook to the relevant alerts automatically, we recommend using the following filters when configuring the playbook triggers: Alert Source = Correlation AND Alert Name = CyberArk Failed Logins.

Inputs:

- `InternalRange`: List of Internal IP ranges
- `UserVerification`: Whether to wait for user verification for blocking those IPs. False - No prompt will be displayed to the user.True - The server will ask the user for blocking v

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
