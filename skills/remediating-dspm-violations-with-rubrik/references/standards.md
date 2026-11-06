# Standards and References - Remediating Dspm Violations with Rubrik

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Respond | PR.DS-11 | See NIST CSF 2.0 category PR.DS-11 |
| Respond | RC.RP-01 | See NIST CSF 2.0 category RC.RP-01 |
| Respond | RS.MI-01 | See NIST CSF 2.0 category RS.MI-01 |

## NIST SP 800-53 Rev. 5

| Control | Title |
|---|---|
| IR-4 | Incident Handling |
| IR-5 | Incident Monitoring |
| AU-6 | Audit Record Review |
| SI-4 | System Monitoring |

## MITRE ATT&CK

| Technique | Name |
|---|---|
| T1486 | See attack.mitre.org/techniques/T1486/ |
| T1490 | See attack.mitre.org/techniques/T1490/ |
| T1485 | See attack.mitre.org/techniques/T1485/ |

## Evidence handling

- Hash every artifact before and after transfer.
- Record the tool, version, operator, and timestamp.
- Keep the original read-only and work on a copy.
- Attach the evidence manifest to the incident.