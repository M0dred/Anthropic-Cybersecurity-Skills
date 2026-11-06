# Standards and References - Processing Email for Phishing Investigation

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Respond | DE.AE-02 | See NIST CSF 2.0 category DE.AE-02 |
| Respond | RS.AN-03 | See NIST CSF 2.0 category RS.AN-03 |
| Respond | PR.AT-01 | See NIST CSF 2.0 category PR.AT-01 |

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
| T1566.001 | See attack.mitre.org/techniques/T1566/001/ |
| T1566.002 | See attack.mitre.org/techniques/T1566/002/ |
| T1204.002 | See attack.mitre.org/techniques/T1204/002/ |

## Evidence handling

- Hash every artifact before and after transfer.
- Record the tool, version, operator, and timestamp.
- Keep the original read-only and work on a copy.
- Attach the evidence manifest to the incident.