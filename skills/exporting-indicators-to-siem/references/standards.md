# Standards and References - Exporting Indicators to a SIEM

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Identify | ID.RA-01 | Threats are identified |
| Detect | DE.CM-01 | Networks are monitored |
| Respond | RS.MI-01 | Incidents are contained |

## NIST SP 800-53 Rev. 5

| Control | Title | Relevance |
|---|---|---|
| SI-4 | System Monitoring | Indicators feed monitoring |
| SC-7 | Boundary Protection | EDL feeds firewall rules |
| AU-6 | Audit Record Review | Export logs are auditable |
| PM-16 | Threat Awareness Program | Intelligence sharing |

## STIX 2.1 / TAXII 2.1

| Object | Use |
|---|---|
| `indicator` | The exported pattern |
| `observed-data` | First/last observed |
| `malware` | Family attribution |
| `relationship` | `indicates` links |
| TAXII `collection` | Pull endpoint for consumers |

## MITRE ATT&CK

| Technique | Name | Relevance |
|---|---|---|
| T1588.001 | Obtain Capabilities: Malware | Indicator source |
| T1071 | Application Layer Protocol | C2 indicators |
| T1105 | Ingress Tool Transfer | Payload hashes |

## Data quality rules

- Every indicator has a type, a source, and a first-seen date.
- Every indicator has an expiry or a review date.
- Allowlisted values are excluded at export time, not at ingest time.
- Duplicates are removed on the normalized value.
- Private and reserved ranges are excluded.
