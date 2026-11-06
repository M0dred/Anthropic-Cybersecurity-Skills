# Standards and References - Blocking Malicious URLs

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Respond | RS.MA-01 | See NIST CSF 2.0 category RS.MA-01 |
| Respond | RS.MI-01 | See NIST CSF 2.0 category RS.MI-01 |
| Respond | RS.AN-03 | See NIST CSF 2.0 category RS.AN-03 |

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
| T1566 | See attack.mitre.org/techniques/T1566/ |
| T1078 | See attack.mitre.org/techniques/T1078/ |

## Evidence handling

- Hash every artifact before and after transfer.
- Record the tool, version, operator, and timestamp.
- Keep the original read-only and work on a copy.
- Attach the evidence manifest to the incident.