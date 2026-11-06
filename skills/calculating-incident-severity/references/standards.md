# Standards and References - Calculating Incident Severity

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Govern | GV.RM-01 | Risk management objectives are established |
| Respond | RS.MA-01 | The incident response plan is executed |
| Respond | RS.AN-03 | Analysis establishes what happened |

## NIST SP 800-61r3

- Incident prioritization considers functional impact, information impact,
  and recoverability.
- Document the triage decision and revisit it as facts change.
- Severity drives notification and escalation.

## ISO/IEC 27035

- Incident classification by impact and urgency.
- Escalation criteria and communication paths.
- Post-incident review of the classification decision.

## NIST SP 800-53 Rev. 5

| Control | Title | Relevance |
|---|---|---|
| IR-4 | Incident Handling | Triage and escalation |
| IR-5 | Incident Monitoring | Track status and severity |
| RA-3 | Risk Assessment | Impact and likelihood |
| AU-6 | Audit Record Review | Record the decision |

## MITRE ATT&CK impact mapping

| Tactic | Techniques | Impact weight |
|---|---|---|
| Impact | T1486, T1485, T1490 | 1.0 |
| Credential Access | T1003, T1555, T1558 | 0.9 |
| Exfiltration | T1041, T1048, T1567 | 0.9 |
| Privilege Escalation | T1068, T1548 | 0.8 |
| Initial Access | T1566, T1190, T1133 | 0.6-0.8 |
| Execution | T1059, T1204 | 0.7 |
| Lateral Movement | T1021, T1570 | 0.7 |
| Defense Evasion | T1562, T1070 | 0.7 |
| Discovery | T1087, T1018 | 0.4 |
| Collection | T1005, T1114 | 0.6 |

## Data classification

| Class | Examples | Score |
|---|---|---|
| Public | marketing site, public docs | 0.0 |
| Internal | intranet, internal wiki | 0.3 |
| Confidential | customer PII, contracts | 0.7 |
| Regulated | PHI, cardholder data, secrets | 1.0 |

## SLA alignment

| Rating | Acknowledge | Contain | Notify |
|---|---|---|---|
| Critical | 15 min | 1 hour | CISO, IR lead, business owner |
| High | 30 min | 4 hours | IR lead, SOC lead |
| Medium | 2 hours | 24 hours | SOC queue |
| Low | next business day | 72 hours | ticket only |
