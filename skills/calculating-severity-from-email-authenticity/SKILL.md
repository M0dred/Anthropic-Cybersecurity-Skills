---
name: calculating-severity-from-email-authenticity
description: >-
  Calculates the severity according to the verdict coming from the CheckEmailAuthenticity script. Weights SPF, DKIM, and DMARC failures into severity. Use when severity from email authentication results must be prioritized against other work, or when an SLA depends on the severity from email authentication results rating. Keywords: calculating, severity, from, email, authenticity, scoring, prioritization, phishing defense. Do not use for calculating severity from critical assets - use `calculating-severity-from-critical-assets`.
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

# Calculating Severity From Email Authenticity

## When to Use

- A value must be prioritized against other work.
- An SLA or notification decision depends on the score.
- A review challenges how the score was derived.

**Do not use** for calculating severity from critical assets - use `calculating-severity-from-critical-assets`.

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

```powershell
# Microsoft 365
Get-MessageTrace -SenderAddress attacker@evil.example -StartDate (Get-Date).AddDays(-7)
New-ComplianceSearch -Name "INC-1234" -ExchangeLocation all -ContentMatchQuery 'from:attacker@evil.example'
Start-ComplianceSearch -Identity "INC-1234"
New-ComplianceSearchAction -SearchName "INC-1234" -Purge -PurgeType SoftDelete
```

```bash
# Proofpoint TAP / mail gateway
curl "https://tap.proofpoint.com/v2/siem/messages/blocked?interval=2026-08-30T00:00:00Z/2026-08-31T00:00:00Z" \
  -H "Authorization: Basic $PP_AUTH"
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
