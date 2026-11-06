# Standards and References - Remediating Prisma Cloud Compliance Alerts

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Respond | PR.PS-01 | See NIST CSF 2.0 category PR.PS-01 |
| Respond | DE.CM-01 | See NIST CSF 2.0 category DE.CM-01 |
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
| T1610 | See attack.mitre.org/techniques/T1610/ |
| T1611 | See attack.mitre.org/techniques/T1611/ |
| T1525 | See attack.mitre.org/techniques/T1525/ |

## Evidence handling

- Hash every artifact before and after transfer.
- Record the tool, version, operator, and timestamp.
- Keep the original read-only and work on a copy.
- Attach the evidence manifest to the incident.