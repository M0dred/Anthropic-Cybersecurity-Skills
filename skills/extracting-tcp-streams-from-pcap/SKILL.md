---
name: extracting-tcp-streams-from-pcap
description: >-
  Extract payloads of each stream from a pcap file. Reassembles TCP streams and carves transferred objects. Use when TCP streams from packet captures must be parsed for evidence, or when an alert needs confirmation from TCP streams from packet captures. Keywords: extracting, tcp, streams, from, pcap, analysis, parsing, digital forensics. Do not use for extracting http flows from pcap - use `extracting-http-flows-from-pcap`.
domain: cybersecurity
subdomain: digital-forensics
tags:
- digital-forensics
- evidence
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.AN-03
- DE.CM-01
- RS.MA-01
mitre_attack:
- T1005
- T1070
- T1112
---

# Extracting Tcp Streams From PCAP

## When to Use

- A suspicious artifact, log, or document needs structured analysis.
- An alert requires confirmation from the underlying data.
- A report or hand-off needs reproducible findings rather than prose.

**Do not use** for extracting http flows from pcap - use `extracting-http-flows-from-pcap`.

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
tshark -r capture.pcapng -Y 'dns' -T fields -e dns.qry.name | sort | uniq -c | sort -rn
tshark -r capture.pcapng -Y 'http.request' -T fields -e http.host -e http.request.uri
tshark -r capture.pcapng -Y 'tls.handshake.extensions_server_name' \
  -T fields -e tls.handshake.extensions_server_name
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
