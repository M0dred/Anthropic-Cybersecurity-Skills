---
name: calculating-severity-from-critical-assets
description: >-
  Determines if a critical asset is associated with the investigation. It returns a severity level of "Critical" if at least one critical asset is associated with the investigation. Critical assets refer to: users, user groups, endpoints and endpoint groups. Use when severity from critical-asset exposure must be prioritized against other work, or when an SLA depends on the severity from critical-asset exposure rating. Keywords: calculating, severity, from, critical, assets, scoring, prioritization, incident response. Do not use for calculating severity from indicator scores - use `calculating-severity-from-indicator-scores`.
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

# Calculating Severity From Critical Assets

## When to Use

- A value must be prioritized against other work.
- An SLA or notification decision depends on the score.
- A review challenges how the score was derived.

**Do not use** for calculating severity from indicator scores - use `calculating-severity-from-indicator-scores`.

## Prerequisites

- The input fields and their allowed values.
- The weighting model and the band thresholds.
- A second analyst to reproduce the score.

## Workflow

### Step 1: Collect inputs

Gather each factor from its authoritative source.

### Step 2: Normalize

Map raw values to the model's scale.

### Step 3: Weight and sum

Apply the weights and compute the total.

### Step 4: Apply modifiers

Adjust for active status, data class, repeat, and confidence.

### Step 5: Explain

Write the per-factor breakdown and the final band.

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

```bash
# Generic REST call with a bearer token
curl -sS -X GET "https://api.example.com/v1/resource" \
  -H "Authorization: Bearer $API_TOKEN" -H "Accept: application/json"
```

## Verification

- The contributions sum to the total.
- The band matches the threshold table.
- A second analyst reproduces the result.
- The rationale is attached to the record.

## Common Pitfalls

- Scoring without a model.
- Letting confidence inflate the score.
- Never recalculating after facts change.
- Hiding the rationale behind a single number.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
