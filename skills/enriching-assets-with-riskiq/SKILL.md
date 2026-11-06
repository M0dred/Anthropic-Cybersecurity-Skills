---
name: enriching-assets-with-riskiq
description: >-
  Receives indicators from its parent playbook and enriches the basic information and the detected CVEs for the "RiskIQAsset" type of indicators. This playbook needs to be used with caution as it might use up the integrations' API license when running for large amounts of indicators. Supported Integrations. Covers 2 vendor variants: RiskIQ Digital Footprint. Use when enriching assets with riskiq must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: enriching, assets, with, riskiq, threat intelligence. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Enriching Assets with Riskiq

## When to Use

- The environment uses one of: RiskIQ Digital Footprint.
- enriching assets with riskiq must be executed through a vendor API or console.
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

### RiskIQAsset Basic Information Enrichment - RiskIQ Digital Footprint

Source pack: RiskIQ Digital Footprint

Receives indicators from its parent playbook and enriches the basic information and the detected CVEs for the "RiskIQAsset" type of indicators. This playbook needs to be used with caution as it might use up the integrations' API license when running for large amounts of indicators. Supported Integrations.

Inputs:

- `asset_name`: Name of the asset.
- `asset_type`: Type of the asset. Possible values: Domain, Host, IP Address, IP Block, ASN, Page, SSL Cert, Contact.

### RiskIQAsset Enrichment - RiskIQ Digital Footprint

Source pack: RiskIQ Digital Footprint

Enriches the "RiskIQAsset" type of indicators with basic information and CVEs detected for the asset, performs a vulnerability scan for "Host" and "IP Address" type of assets, and enriches received information in the context as well as provides the user to add to allow list a list of "IP Address" type of assets. This playbook also enriches the detected CVEs. To select the indicators you want to enrich, go to playbook inputs, choose "from indicators" and set your query. For example type:RiskIQAsset etc. The default playbook query is "type:RiskIQAsset". In case indicators with specific "riskiqassettype" are to be enriched, the query must be edited accordingly. This playbook needs to be used with caution as it might use up the integrations' API license when running for large amounts of indicators. Supported integrations.

Inputs:

- `Indicator Query`: Indicators matching the indicator query will be used as playbook input
- `InternalRange`: A list of IP ranges to check if the IP Address is in that range for adding to allow list. The list should be provided in CIDR notation, separated by commas. An 
- `auto_whitelist_ip_address`: Automatically adds the IP Address(es) to allow list. You can set this as 'Yes' or 'No' manually here or you can set it into a custom incident field 'RiskIQ Auto
- `auto_exclude_whitelisted_ip_address`: Automatically add the IP Address(es) on allow list to the exclusions list. You can set this as 'Yes' or 'No' manually here or you can set it into a custom incid
- `support_contact`: The contact email address of the support team from which manual inputs should be fetched.
- `aws_security_group_name`: Name of the AWS Security Group to update the IPs on allow list.
- `gcp_firewall_name`: Name of the GCP Firewall where the playbook should set the IPs on allow list.
- `okta_zone_id`: ID of the Okta Zone to update the IPs on allow list. Use !okta-list-zones to obtain the available zones.

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
