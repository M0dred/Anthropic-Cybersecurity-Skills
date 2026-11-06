# Standards and References - Rotating Cloud Credentials

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Respond | PR.AC-01 | See NIST CSF 2.0 category PR.AC-01 |
| Respond | PR.AC-04 | See NIST CSF 2.0 category PR.AC-04 |
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
| T1078 | See attack.mitre.org/techniques/T1078/ |
| T1098 | See attack.mitre.org/techniques/T1098/ |
| T1556 | See attack.mitre.org/techniques/T1556/ |

## Evidence handling

- Hash every artifact before and after transfer.
- Record the tool, version, operator, and timestamp.
- Keep the original read-only and work on a copy.
- Attach the evidence manifest to the incident.