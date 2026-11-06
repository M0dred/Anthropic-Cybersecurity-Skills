---
name: detonating-files-with-crowdstrike-sandbox
description: >-
  Uploads, detonates, and analyzes files for the CrowdStrike Falcon Intelligence Sandbox. Covers 1 vendor variants: CrowdStrike Falcon Intelligence Sandbox. Use when detonating files with crowdstrike sandbox must be executed through a specific vendor product, or when the vendor-neutral procedure needs the exact API or console steps. Keywords: detonating, files, with, crowdstrike, sandbox, malware analysis. Do not use for the vendor-neutral procedure - use the matching generic skill.
domain: cybersecurity
subdomain: malware-analysis
tags:
- malware-analysis
- sandbox
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.MI-01
mitre_attack:
- T1078
---

# Detonating Files with CrowdStrike Sandbox

## When to Use

- The environment uses one of: CrowdStrike Falcon Intelligence Sandbox.
- detonating files with crowdstrike sandbox must be executed through a vendor API or console.
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

### CrowdStrike Falcon Intelligence Sandbox Detonate and Analyze File

Source pack: CrowdStrike Falcon Intelligence Sandbox

Uploads, detonates, and analyzes files for the CrowdStrike Falcon Intelligence Sandbox.

Inputs:

- `File`: The details of the file to detonate.
- `AlertOS`: The operating system for which the alert was raised.Possible values: Windows Linux* Android

## Platform Commands

```bash
# CrowdStrike Falcon
curl -X POST "https://api.crowdstrike.com/devices/entities/devices-actions/v2?action_name=contain" \
  -H "Authorization: Bearer $CS_TOKEN" -H "Content-Type: application/json" \
  -d '{"ids":["<device_id>"]}'
curl "https://api.crowdstrike.com/devices/queries/devices/v1?filter=hostname:'WEB-01'" \
  -H "Authorization: Bearer $CS_TOKEN"
```

```bash
# Microsoft Defender for Endpoint
curl -X POST "https://api.securitycenter.microsoft.com/api/machines/<id>/isolate" \
  -H "Authorization: Bearer $MDE_TOKEN" -H "Content-Type: application/json" \
  -d '{"Comment":"INC-1234","IsolationType":"Full"}'
curl "https://api.securitycenter.microsoft.com/api/machines?\$filter=computerDnsName eq 'WEB-01'" \
  -H "Authorization: Bearer $MDE_TOKEN"
```

```bash
curl "https://www.virustotal.com/api/v3/files/<sha256>" -H "x-apikey: $VT_API_KEY"
curl -X POST "https://www.virustotal.com/api/v3/files" -H "x-apikey: $VT_API_KEY" -F "file=@sample.bin"
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
