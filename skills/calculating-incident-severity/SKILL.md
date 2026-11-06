---
name: calculating-incident-severity
description: >-
  Computes a defensible incident severity from six inputs: asset criticality,
  indicator verdicts, ATT&CK technique impact, data sensitivity, blast radius,
  and confidence. Produces a Critical/High/Medium/Low rating with a per-factor
  rationale that survives review, and supports recalculation as facts change.
  Use when a new alert needs triage, when an incident is escalated or
  de-escalated, when SLA timers must be set, or when a post-incident review asks
  why the response was sized the way it was. Keywords: severity, triage,
  prioritization, SLA, incident scoring, risk rating.
  Do not use for vulnerability severity - use CVSS or
  performing-cve-prioritization-with-kev-catalog. Do not use for alert
  deduplication - use a SIEM correlation rule.
domain: cybersecurity
subdomain: incident-response
tags:
- incident-response
- triage
- severity
- risk-scoring
- sla
- soc-operations
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.MA-01
- RS.AN-03
- GV.RM-01
mitre_attack:
- T1486
- T1566
- T1078
---

# Calculating Incident Severity

## When to Use

- A new alert or report needs a severity before it enters the queue.
- An incident is escalated, de-escalated, or merged with another.
- SLA timers and notification lists depend on the rating.
- A post-incident review challenges the original triage decision.
- A tabletop or audit needs a repeatable scoring method.

**Do not use** for vulnerability severity; CVSS and KEV prioritization answer a
different question. **Do not use** for deduplicating alerts; that is a
correlation problem, not a scoring one.

## Prerequisites

- An asset inventory with a criticality tier per host or service.
- The indicator verdicts from enrichment (malicious, suspicious, unknown).
- The ATT&CK techniques observed, or enough evidence to infer them.
- A data-classification scheme (public, internal, confidential, regulated).
- The incident's current blast radius: one host, one user, one business unit,
  or cross-tenant.

## Workflow

### Step 1: Collect the six inputs

```bash
python3 scripts/agent.py score --input incident.json --out severity.json
```

`incident.json`:

```json
{
  "incident_id": "INC-1234",
  "asset_criticality": "high",
  "indicator_verdict": "malicious",
  "techniques": ["T1486", "T1078"],
  "data_sensitivity": "confidential",
  "blast_radius": "business_unit",
  "confidence": 0.8,
  "business_hours": true,
  "active": true
}
```

### Step 2: Score each factor

| Factor | Values | Weight |
|---|---|---|
| Asset criticality | low 0.2, medium 0.5, high 0.8, crown-jewel 1.0 | 0.25 |
| Indicator verdict | benign 0.0, unknown 0.3, suspicious 0.6, malicious 1.0 | 0.20 |
| Technique impact | see table below | 0.20 |
| Data sensitivity | public 0.0, internal 0.3, confidential 0.7, regulated 1.0 | 0.15 |
| Blast radius | host 0.2, user 0.3, business unit 0.7, cross-tenant 1.0 | 0.10 |
| Confidence | 0.0-1.0 | 0.10 |

Technique impact is the maximum over the observed techniques:

| Technique | Impact |
|---|---|
| T1486 Data Encrypted for Impact | 1.0 |
| T1490 Inhibit System Recovery | 1.0 |
| T1485 Data Destruction | 1.0 |
| T1078 Valid Accounts | 0.8 |
| T1566 Phishing | 0.6 |
| T1059 Command and Scripting Interpreter | 0.7 |
| T1003 OS Credential Dumping | 0.9 |
| T1021 Remote Services | 0.7 |
| T1071 Application Layer Protocol | 0.6 |
| T1041 Exfiltration Over C2 | 0.9 |
| T1562 Impair Defenses | 0.7 |
| default | 0.5 |

### Step 3: Map the score to a rating

| Score | Rating | First response | Notification |
|---|---|---|---|
| >= 0.85 | Critical | 15 min | CISO, IR lead, business owner |
| 0.65 - 0.84 | High | 30 min | IR lead, SOC lead |
| 0.40 - 0.64 | Medium | 2 hours | SOC queue |
| < 0.40 | Low | next business day | ticket only |

### Step 4: Apply the modifiers

- **Active vs contained.** An active intrusion is one band higher until
  contained.
- **Business hours.** Off-hours incidents with customer impact are one band
  higher.
- **Regulated data.** Any confirmed regulated-data exposure is at least High.
- **Repeat incident.** The same root cause within 30 days is one band higher.
- **Confidence floor.** A score built on fewer than two corroborating sources
  cannot exceed Medium.

### Step 5: Record the rationale

```bash
python3 scripts/agent.py explain --input incident.json
```

The explanation lists each factor, its raw value, its normalized score, its
weighted contribution, and the modifiers applied. This is the text that goes
into the incident and survives the post-incident review.

### Step 6: Recalculate as facts change

Severity is not static. Re-run the score when enrichment returns, when the
blast radius grows, when containment succeeds, and when data classification is
confirmed. Keep every version with a timestamp.

## Verification

- The weighted contributions sum to the total score (within rounding).
- The rating matches the band table, including modifiers.
- Every factor has a source: inventory, enrichment, ATT&CK mapping, or
  classification policy.
- A second analyst given the same inputs produces the same rating.
- The incident record contains the rationale, not just the number.

## Common Pitfalls

- **Severity by vibes.** Without a model, the loudest analyst sets the rating.
- **Ignoring asset criticality.** A malware hit on a build server is not the
  same as on a laptop.
- **Over-weighting confidence.** Low confidence should cap the rating, not
  inflate it.
- **Forgetting blast radius.** One phished user and a domain-wide compromise
  are different incidents.
- **Never recalculating.** An incident scored at 09:00 may be contained by
  09:30; the SLA should follow the facts.
- **Regulated data blind spot.** Confirm the classification before closing.

## References

- `references/api-reference.md` - input schema, weights, technique table
- `references/standards.md` - NIST, ISO 27035, ATT&CK impact mapping
- `references/workflows.md` - modifiers, recalculation, review template
- `scripts/agent.py` - score, explain, batch
