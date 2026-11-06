---
name: blocking-files-with-microsoft-defender
description: >-
  Receives an MD5 or a SHA256 hash and adds it to the block list in Microsoft Defender for Endpoint. The uses the integration "Microsoft Defender for Endpoint". Uses MDE indicator blocklists and custom detection rules. Use when an active incident requires files through Microsoft Defender for Endpoint to be cut off, or when a detection names files through Microsoft Defender for Endpoint and containment is authorized. Keywords: blocking, files, with, microsoft, defender, containment, response, endpoint security. Do not use for blocking files with crowdstrike - use `blocking-files-with-crowdstrike`.
domain: cybersecurity
subdomain: endpoint-security
tags:
- endpoint-security
- edr
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.MI-01
- PR.AC-05
- DE.CM-01
mitre_attack:
- T1059
- T1021
- T1562
---

# Blocking Files with Microsoft Defender

## When to Use

- An intrusion is active and files through Microsoft Defender for Endpoint must be cut off now.
- A detection or analyst decision requires files through Microsoft Defender for Endpoint to be blocked, isolated, disabled, or removed.
- A containment step needs a verifiable, reversible change with an audit trail.
- A post-incident review asks whether the containment actually worked.

**Do not use** for blocking files with crowdstrike - use `blocking-files-with-crowdstrike`.

## Prerequisites

- Authority to change the target platform, and a ticket for the change.
- The exact value or object to contain, with provenance (alert, feed, analyst).
- Read access to the enforcement point so the change can be verified.
- The rollback command, written down before the change is applied.

## Workflow

### Step 1: Validate the target

Normalize the value, reject malformed or out-of-scope entries, and confirm the direction and blast radius. A containment action against shared infrastructure needs a narrower scope.

### Step 2: Choose the enforcement point

Prefer the point closest to the threat that is still reversible: host, then cloud control plane, then perimeter, then edge.

### Step 3: Apply the change

Use the platform-native command or API. Capture the exact request and response.

### Step 4: Verify the effect

Confirm the object is contained from the platform's own state, then test the path from an independent vantage point.

### Step 5: Record and schedule review

Write the change, operator, ticket, timestamp, rollback, and expiry into the incident.

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

```bash
# Microsoft Defender for Endpoint
curl -X POST "https://api.securitycenter.microsoft.com/api/machines/<id>/isolate" \
  -H "Authorization: Bearer $MDE_TOKEN" -H "Content-Type: application/json" \
  -d '{"Comment":"INC-1234","IsolationType":"Full"}'
curl "https://api.securitycenter.microsoft.com/api/machines?\$filter=computerDnsName eq 'WEB-01'" \
  -H "Authorization: Bearer $MDE_TOKEN"
```

```bash
# CrowdStrike Falcon
curl -X POST "https://api.crowdstrike.com/devices/entities/devices-actions/v2?action_name=contain" \
  -H "Authorization: Bearer $CS_TOKEN" -H "Content-Type: application/json" \
  -d '{"ids":["<device_id>"]}'
curl "https://api.crowdstrike.com/devices/queries/devices/v1?filter=hostname:'WEB-01'" \
  -H "Authorization: Bearer $CS_TOKEN"
```

## Verification

- The platform reports the object in the contained state.
- An independent test confirms the blocked path fails while a control path succeeds.
- The rollback command has been executed once in a lab or on a canary.
- The change is recorded with an owner and an expiry date.

## Common Pitfalls

- Containing shared infrastructure and breaking legitimate users.
- Applying the change at a layer that does not see the traffic.
- No rollback, so a false positive becomes an outage.
- No expiry, so tactical blocks become permanent debt.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
