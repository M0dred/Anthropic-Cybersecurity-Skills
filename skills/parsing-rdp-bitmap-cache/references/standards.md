# Standards and References - Parsing RDP Bitmap Cache

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Respond | RS.AN-03 | See NIST CSF 2.0 category RS.AN-03 |
| Respond | DE.CM-01 | See NIST CSF 2.0 category DE.CM-01 |
| Respond | RS.MA-01 | See NIST CSF 2.0 category RS.MA-01 |

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
| T1005 | See attack.mitre.org/techniques/T1005/ |
| T1070 | See attack.mitre.org/techniques/T1070/ |
| T1112 | See attack.mitre.org/techniques/T1112/ |

## Evidence handling

- Hash every artifact before and after transfer.
- Record the tool, version, operator, and timestamp.
- Keep the original read-only and work on a copy.
- Attach the evidence manifest to the incident.