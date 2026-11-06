# Standards and References - Enriching Domains with Threat Intelligence

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Respond | ID.RA-01 | See NIST CSF 2.0 category ID.RA-01 |
| Respond | DE.AE-02 | See NIST CSF 2.0 category DE.AE-02 |
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
| T1588.001 | See attack.mitre.org/techniques/T1588/001/ |
| T1071 | See attack.mitre.org/techniques/T1071/ |
| T1595 | See attack.mitre.org/techniques/T1595/ |

## Evidence handling

- Hash every artifact before and after transfer.
- Record the tool, version, operator, and timestamp.
- Keep the original read-only and work on a copy.
- Attach the evidence manifest to the incident.