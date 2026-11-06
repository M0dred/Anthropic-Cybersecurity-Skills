---
name: enriching-incidents-with-illusive
description: >-
  Is used for automatic enrichment of incidents in the organization network, with Illusive's set of forensics and data. Covers 1 vendor variants: Illusive Networks. Use when enriching incidents with illusive must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: enriching, incidents, with, illusive, threat intelligence. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Enriching Incidents with Illusive

## When to Use

- The environment uses one of: Illusive Networks.
- enriching incidents with illusive must be executed through a vendor API or console.
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

### Illusive - Data Enrichment

Source pack: Illusive Networks

Is used for automatic enrichment of incidents in the organization network, with Illusive's set of forensics and data.

Inputs:

- `illusive_incident_id`: Illusive incident ID
- `${incident.illusivenetworksid}`: Optional
- `fqdn_or_ip`: The endpoint's fqdn or IP address
- `${Endpoint.Hostname}`: Optional

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
