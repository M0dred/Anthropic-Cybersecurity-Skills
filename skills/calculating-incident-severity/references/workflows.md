# Workflows - Calculating Incident Severity

## Scoring sequence

```
collect inputs -> normalize -> weight -> sum -> apply modifiers -> band -> record
```

## Modifiers

| Modifier | Condition | Effect |
|---|---|---|
| Active | intrusion still in progress | +1 band |
| Off-hours | outside business hours with customer impact | +1 band |
| Regulated data | confirmed regulated-data exposure | floor at High |
| Repeat | same root cause within 30 days | +1 band |
| Low confidence | fewer than two corroborating sources | cap at Medium |
| Contained | containment verified | -1 band |

Modifiers apply after the weighted score, in the order listed. A floor and a cap
are absolute; bands are relative.

## Recalculation triggers

- New enrichment result (verdict changes).
- Blast radius changes (one host to a business unit).
- Containment succeeds or fails.
- Data classification is confirmed.
- A related incident is linked.

## Review template

```
Incident:      INC-1234
Initial score: 0.78 (High) at 2026-08-31T09:00Z
Factors:       asset high 0.20, verdict malicious 0.20, T1486 0.20,
               confidential 0.105, business-unit 0.07, confidence 0.08
Modifiers:     active +1 band -> Critical
Final:         Critical at 09:00Z
Recalculated:  0.55 (Medium) at 09:30Z after containment
Rationale:     ransomware on a crown-jewel file server, active encryption
Reviewer:      soc-lead@example.com
```

## Calibration

- Sample 20 past incidents, score them, and compare with the rating the team
  actually used.
- Adjust weights only with a documented rationale and a re-run of the sample.
- Track false positives (over-rated) and misses (under-rated) monthly.
- Keep the model stable for at least a quarter so trends are comparable.

## Common disagreements

| Disagreement | Resolution |
|---|---|
| Analyst wants Critical, model says High | check modifiers; if active and regulated, the floor applies |
| Model says Critical, analyst says Medium | verify asset criticality and data classification |
| Two analysts differ | compare factor inputs, not opinions |
| Score changed after containment | expected; record both versions |
