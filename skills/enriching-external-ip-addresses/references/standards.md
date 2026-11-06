# Standards and References - Enriching External IP Addresses

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Identify | ID.RA-01 | Threats and vulnerabilities are identified |
| Detect | DE.AE-02 | Adverse events are analyzed |
| Respond | RS.AN-03 | Analysis establishes what happened |

## NIST SP 800-53 Rev. 5

| Control | Title | Relevance |
|---|---|---|
| SI-4 | System Monitoring | Enrichment feeds monitoring |
| RA-3 | Risk Assessment | Reputation informs risk |
| IR-4 | Incident Handling | Context for triage |
| AU-6 | Audit Record Review | Record lookup provenance |

## MITRE ATT&CK

| Technique | Name | Enrichment use |
|---|---|---|
| T1590.005 | Gather Victim Network Information: IP Addresses | Understand the adversary's view of your ranges |
| T1595 | Active Scanning | Identify scanner infrastructure |
| T1071 | Application Layer Protocol | C2 endpoint context |
| T1583.003 | Acquire Infrastructure: Virtual Private Server | Hosting ASN signals |

## STIX 2.1

| Object | Use |
|---|---|
| `ipv4-addr` / `ipv6-addr` | The indicator |
| `autonomous-system` | ASN and owner |
| `location` | Country and city |
| `infrastructure` | Hosting or C2 infrastructure |
| `note` | Analyst enrichment note |

## Data sources

| Source | Strength | Weakness |
|---|---|---|
| AbuseIPDB | Crowd-sourced abuse reports | Recency bias, report spam |
| VirusTotal | Multi-engine correlation | Shared hosting noise |
| GreyNoise | Internet-wide scan classification | Coverage gaps |
| ipinfo | Accurate geo/ASN | No reputation |
| PTR | Ownership hint | Easily spoofed |

## Confidence model

| Component | Weight |
|---|---|
| AbuseIPDB score >= 80 | 0.30 |
| VirusTotal malicious >= 5 | 0.25 |
| GreyNoise malicious | 0.25 |
| Hosting or bulletproof ASN | 0.10 |
| PTR mismatch with org | 0.05 |
| Multiple independent sources agree | 0.05 |

Cap at 1.0. If fewer than two sources respond, cap at 0.5 and mark the record
as low-confidence.
