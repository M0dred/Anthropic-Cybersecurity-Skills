---
name: parsing-nessus-nexpose-reports
description: >-
  Parses the Nexpose report into a clear table that contain risk score and vulnerability count for each server, and creates a new incident for each server. Parses Nessus and Nexpose exports into findings. Use when Nessus and Nexpose reports must be parsed for evidence, or when an alert needs confirmation from Nessus and Nexpose reports. Keywords: parsing, nessus, nexpose, reports, analysis, vulnerability management. Do not use for parsing cef logs - use `parsing-cef-logs`.
domain: cybersecurity
subdomain: vulnerability-management
tags:
- vulnerability-management
- cve
- remediation
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- ID.RA-01
- PR.IP-12
- RS.MI-02
mitre_attack:
- T1190
- T1203
- T1068
---

# Parsing Nessus Nexpose Reports

## When to Use

- A suspicious artifact, log, or document needs structured analysis.
- An alert requires confirmation from the underlying data.
- A report or hand-off needs reproducible findings rather than prose.

**Do not use** for parsing cef logs - use `parsing-cef-logs`.

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
# Tenable / Nessus export
curl -X POST "https://<nessus>:8834/scans/<id>/export" \
  -H "X-ApiKeys: accessKey=$ACCESS;secretKey=$SECRET" \
  -d '{"format":"nessus"}'
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
