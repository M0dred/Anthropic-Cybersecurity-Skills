---
name: enriching-incidents-with-cofense
description: >-
  Allows users to quarantine various messages that meet their specified criteria. Covers 2 vendor variants: Cofense Triage, Cofense Vision. Use when enriching incidents with cofense must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: enriching, incidents, with, cofense, phishing defense. Do not use for the vendor-neutral procedure - use the matching generic skill.
domain: cybersecurity
subdomain: phishing-defense
tags:
- phishing-defense
- email-security
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- DE.AE-02
- RS.AN-03
- PR.AT-01
mitre_attack:
- T1566.001
- T1566.002
- T1204.002
---

# Enriching Incidents with Cofense

## When to Use

- The environment uses one of: Cofense Triage, Cofense Vision.
- enriching incidents with cofense must be executed through a vendor API or console.
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

### Message Quarantine - Cofense Vision

Source pack: Cofense Vision

Allows users to quarantine various messages that meet their specified criteria.

Inputs:

- `subjects`: A comma-separated string of subjects to create a search for an email's subject. It supports the use of one or more wildcard characters (*) in any position of a 
- `senders`: A comma-separated string of senders to create a search for an email's sender. It supports the use of one or more wildcard characters (*) in any position of a se
- `attachment_names`: A comma-separated string of attachment names to create a search for an email's attachments. It supports the use of one or more wildcard characters (*) in any po
- `attachment_hash_match_criteria`: The type of matching performed on the hashes specified in the attachment_hashes argument.Possible values are:ALL: Emails must include all listed attachment hash
- `attachment_hashes`: A comma-separated string of attachment hashes to create a search for an email's attachment hashes.Supported format: hashtype1:hashvalue1, hashtype2:hashvalue2Po
- `attachment_mime_types`: A comma-separated string of MIME types to create a search for an email's attachment MIME type.Note: The search can only have a maximum of 3 values.
- `attachment_exclude_mime_types`: A comma-separated string of MIME types to create a search for excluding an email's attachment MIME type.Note: The search can only have a maximum of 3 values.
- `domain_match_criteria`: The type of matching to perform on the domains specified in the domains argument.Possible values are:ALL: Emails must include all listed domains.ANY: Emails mus

### Send Indicators - Cofense Triage v3

Source pack: Cofense Triage

Send Indicators playbook is used to create or update threat indicators in Cofense Triage that have been identified as malicious or suspicious by the analysis. Users are only able to run the playbook in v6.0.0 or higher as it requires commands to execute the task.

Inputs:

- `Value`: The indicator value.
- `Level`: Represents the status of the indicator.
- `Type`: Type of the indicator.
- `Source`: The source reporting the indicator.

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
