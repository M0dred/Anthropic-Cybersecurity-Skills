---
name: enriching-assets-with-infoblox
description: >-
  Is used to initiate the incident response. This playbook runs when an incident is selected for investigation. It will change the state from pending to active and it will list the available indicators, events, assets, and comments from Infoblox corresponding to the incident. If incident severity is found to be higher than or equivalent to medium, it will create a ServiceNow incident otherwise the given incident. Covers 3 vendor variants: Infoblox Threat Defense with DDI. Use when enriching assets with infoblox must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: enriching, assets, with, infoblox, threat intelligence. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Enriching Assets with Infoblox

## When to Use

- The environment uses one of: Infoblox Threat Defense with DDI.
- enriching assets with infoblox must be executed through a vendor API or console.
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

### Incident Response - Infoblox Cloud

Source pack: Infoblox Threat Defense with DDI

Is used to initiate the incident response. This playbook runs when an incident is selected for investigation. It will change the state from pending to active and it will list the available indicators, events, assets, and comments from Infoblox corresponding to the incident. If incident severity is found to be higher than or equivalent to medium, it will create a ServiceNow incident otherwise the given incident will be assigned to an analyst.

Inputs:

- `soc_insight_id`: Collect incident severity from incident.
- `incident_severity`: Collect incident severity from incident.
- `limit`: No of indicators, events, assets and comments to fetch for the provided SOC Insight.
- `onCall`: Set to true to assign only the user that is currently on shift. Default is False.

### IQ for TD Insight Response - Infoblox Cloud

Source pack: Infoblox Threat Defense with DDI

Collects the insight's full detail (including AI-generated recommendations), indicators, assets, and events. Executes the insight's pending recommendation actions along with undo option. If incident severity is Low, notifies the SOC and assigns an analyst; if severity is Medium, High, or Critical, creates a ServiceNow ticket. Updates the insight's workflow status on Infoblox at the end of the run.

Inputs:

- `insight_id`: Collect IQ for TD Insight ID from incident.
- `incident_severity`: Collect incident severity from incident.
- `limit`: No of indicators, events or assets to fetch for the provided IQ for TD Insight.
- `onCall`: Set to true (case-insensitive) to assign only the user that is currently on shift. Default is False.
- `insight_status`: Workflow status to set on the insight at the end of the run.

### MAC Enrichment - Infoblox Cloud

Source pack: Infoblox Threat Defense with DDI

Enriches MAC addresses with DHCP lease information using Infoblox Threat Defense with DDI integration.

Inputs:

- `mac_addresses`: The comma-separated list of MAC addresses to enrich.

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
