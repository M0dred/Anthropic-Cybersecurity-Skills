---
name: validating-credential-leaks-with-cyberint
description: >-
  Validates and responds to leaked employee or customer credentials reported by Cyberint Argos. The playbook looks up leaked credentials for the configured company domain, escalates the incident when exposed credentials are found, and drives an automated or semi-automated remediation flow (reset sessions, force password reset, or disable the account in the identity provider), followed by user and SOC notification.. Covers 2 vendor variants: Cyberint. Use when validating credential leaks with cyberint must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: validating, credential, leaks, with, cyberint, threat intelligence. Do not use for the vendor-neutral procedure - use the matching generic skill.
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

# Validating Credential Leaks with Cyberint

## When to Use

- The environment uses one of: Cyberint.
- validating credential leaks with cyberint must be executed through a vendor API or console.
- An incident or audit needs a reproducible, vendor-specific record.

**Do not use** for the vendor-neutral procedure; use the matching generic skill.

## Prerequisites

- Access to the vendor console or API, and a credential with the required scope.
- The object identifier (host, account, resource, or indicator) and its provenance.
- A rollback path and a ticket for the change.

## Workflow

### Step 1: Preserve the artifact

Hash it before analysis and work on a copy.

### Step 2: Parse

Use the artifact-specific parser; record the tool and version.

### Step 3: Extract

Pull the fields that matter for the investigation, keeping context for each.

### Step 4: Normalize

Map to the shared schema, de-duplicate, and mark confidence.

### Step 5: Report

Write findings with the evidence path, the commands used, and the limits of the analysis.

## Vendor Variants

### Check Point - Credential Leak Validation and Response

Source pack: Cyberint

Validates and responds to leaked employee or customer credentials reported by Cyberint Argos. The playbook looks up leaked credentials for the configured company domain, escalates the incident when exposed credentials are found, and drives an automated or semi-automated remediation flow (reset sessions, force password reset, or disable the account in the identity provider), followed by user and SOC notification. Identity-provider validation and remediation steps are modeled as manual tasks so the playbook works out of the box; connect them to your Active Directory, Microsoft Entra ID or Okta integration to fully automate the response.

Inputs:

- `CompanyDomain`: The company domain to look up leaked credentials for (for example, example.com).
- `LastSeenFrom`: Only validate credentials last seen on or after this ISO-formatted date (YYYY-MM-DDTHH:MM:SSZ). Use this when running the playbook on a recurring schedule to pr
- `Limit`: Maximum number of leaked credential records to retrieve.
- `AutoRemediate`: Whether to remediate exposed accounts automatically (yes) or to require analyst review and approval first (no). Default is no.

### Check Point - IOC Enrichment and Triage

Source pack: Cyberint

Enriches IOC entities (IP, domain, URL, file hash) found in an incident with Cyberint threat intelligence, then applies triage decision logic. The playbook routes each indicator to the matching Cyberint IOC enrichment endpoint, appends the returned maliciousness score and detected activities to the incident, and escalates the incident severity when a malicious indicator is found. Requires the Check Point EM Feed (Cyberint Feed) integration to be configured.

Inputs:

- `IP`: IP address indicators to enrich with Cyberint threat intelligence. Defaults to IP indicators extracted from the incident.
- `Domain`: Domain indicators to enrich with Cyberint threat intelligence. Defaults to domain indicators extracted from the incident.
- `URL`: URL indicators to enrich with Cyberint threat intelligence. Defaults to URL indicators extracted from the incident.
- `FileSHA256`: SHA256 file hash indicators to enrich with Cyberint threat intelligence. Defaults to file hashes extracted from the incident.
- `MaliciousScoreThreshold`: The Cyberint maliciousness score (0-100) at or above which an indicator is treated as malicious and the incident is escalated. Default is 50.

## Platform Commands

```bash
# Generic REST call with a bearer token
curl -sS -X GET "https://api.example.com/v1/resource" \
  -H "Authorization: Bearer $API_TOKEN" -H "Accept: application/json"
```

## Verification

- The artifact hash in the report matches the source.
- A second run produces the same findings.
- Every finding cites the field or byte range it came from.
- The report states what the analysis could not see.

## Common Pitfalls

- Analyzing the original instead of a copy.
- Claiming content that is encrypted or truncated.
- Dropping context when de-duplicating.
- No tool version, so the result is not reproducible.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and record template
- `scripts/agent.py` - runnable helper for this procedure
