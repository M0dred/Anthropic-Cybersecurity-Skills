# Standards and References - Detecting Beaconing From Timestamp Intervals

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Respond | DE.CM-01 | See NIST CSF 2.0 category DE.CM-01 |
| Respond | DE.AE-02 | See NIST CSF 2.0 category DE.AE-02 |
| Respond | DE.AE-07 | See NIST CSF 2.0 category DE.AE-07 |

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
| T1071 | See attack.mitre.org/techniques/T1071/ |
| T1059 | See attack.mitre.org/techniques/T1059/ |
| T1021 | See attack.mitre.org/techniques/T1021/ |

## Evidence handling

- Hash every artifact before and after transfer.
- Record the tool, version, operator, and timestamp.
- Keep the original read-only and work on a copy.
- Attach the evidence manifest to the incident.