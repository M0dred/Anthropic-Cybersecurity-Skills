---
name: converting-file-hashes
description: >-
  The enables you to get all of the corresponding file hashes for a file even if there is only one hash type available. For example, if we have only the SHA256 hash, the will get the SHA1 and MD5 hashes as long as the original searched hash is recognized by. Converts between MD5, SHA-1, and SHA-256. Use when an alert names file hashes between algorithms and context is needed before a decision, or when a block or escalation depends on file hashes between algorithms reputation. Keywords: converting, file, hashes, enrichment, reputation, threat intelligence. Do not use for retrieving file samples from endpoints - use `retrieving-file-samples-from-endpoints`.
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

# Converting File Hashes

## When to Use

- A detection names file hashes between algorithms and the analyst needs context before deciding.
- A block or escalation decision needs provenance, not a hunch.
- An incident timeline needs first-seen, last-seen, and ownership data.

**Do not use** for retrieving file samples from endpoints - use `retrieving-file-samples-from-endpoints`.

## Prerequisites

- API access to the sources you enable, and a cache directory.
- An allowlist of known-good values so shared infrastructure is not misread.
- The source's rate limits, so a batch does not exhaust the quota.

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

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

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
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
