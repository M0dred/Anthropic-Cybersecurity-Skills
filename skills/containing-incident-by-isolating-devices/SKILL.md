---
name: containing-incident-by-isolating-devices
description: >-
  Isolates the device while preserving the responder channel. Use when an active incident requires affected devices to be cut off, or when a detection names affected devices and containment is authorized. Keywords: containing, incident, isolating, devices, containment, response, incident response. Do not use for containing incident by disabling accounts - use `containing-incident-by-disabling-accounts`.
domain: cybersecurity
subdomain: incident-response
tags:
- incident-response
- containment
- soc-operations
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.MA-01
- RS.MI-01
- RS.AN-03
mitre_attack:
- T1486
- T1566
- T1078
---

# Containing Incident by Isolating Devices

## When to Use

- An intrusion is active and affected devices must be cut off now.
- A detection or analyst decision requires affected devices to be blocked, isolated, disabled, or removed.
- A containment step needs a verifiable, reversible change with an audit trail.
- A post-incident review asks whether the containment actually worked.

**Do not use** for containing incident by disabling accounts - use `containing-incident-by-disabling-accounts`.

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
# Intune / MDM device lookup
az rest --method GET --url "https://graph.microsoft.com/v1.0/deviceManagement/managedDevices?\$filter=userPrincipalName eq 'user@example.com'"
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
