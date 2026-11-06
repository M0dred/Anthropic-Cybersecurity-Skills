---
name: parsing-cef-logs
description: >-
  Parses CEF data into the context. Outputs will display only the 7 mandatory fields even if the CEF event includes many other custom or extended fields. Parses Common Event Format logs into structured fields. Use when CEF logs must be parsed for evidence, or when an alert needs confirmation from CEF logs. Keywords: parsing, cef, logs, analysis, threat intelligence. Do not use for parsing registry for forensics - use `parsing-registry-for-forensics`.
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

# Parsing CEF Logs

## When to Use

- A suspicious artifact, log, or document needs structured analysis.
- An alert requires confirmation from the underlying data.
- A report or hand-off needs reproducible findings rather than prose.

**Do not use** for parsing registry for forensics - use `parsing-registry-for-forensics`.

## Prerequisites

- The artifact, copied to an evidence directory with a SHA-256 recorded.
- The parser or toolchain for the artifact type, and a known-good sample to validate it.
- The schema the output must satisfy.

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

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

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
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
