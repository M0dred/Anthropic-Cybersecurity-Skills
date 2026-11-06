# Standards and References - Analyzing PCAP Files

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Detect | DE.CM-01 | Networks are monitored to detect events |
| Detect | DE.AE-02 | Adverse events are analyzed |
| Respond | RS.AN-03 | Analysis establishes what happened |

## NIST SP 800-53 Rev. 5

| Control | Title | Relevance |
|---|---|---|
| AU-6 | Audit Record Review | Packet data is an audit source |
| SI-4 | System Monitoring | Network monitoring |
| IR-4 | Incident Handling | Evidence for analysis |
| SC-7 | Boundary Protection | Confirm egress controls |

## NIST SP 800-86

Guide to Integrating Forensic Techniques into Incident Response:

- Identify data sources (network traffic, logs, host artifacts).
- Acquire without alteration; hash the capture.
- Examine and analyze; correlate with other sources.
- Report with reproducible steps.

## MITRE ATT&CK

| Technique | Name | Packet evidence |
|---|---|---|
| T1071.004 | Application Layer Protocol: DNS | Long or high-entropy DNS queries |
| T1048.003 | Exfiltration Over Alternative Protocol | Large outbound transfers |
| T1573.002 | Encrypted Channel: Asymmetric Cryptography | TLS to rare destinations |
| T1095 | Non-Application Layer Protocol | Raw TCP/UDP C2 |
| T1041 | Exfiltration Over C2 Channel | POST bodies to C2 |
| T1595.002 | Active Scanning: Vulnerability Scanning | SYN sweeps, many ports |

## RFCs

| RFC | Title |
|---|---|
| RFC 791 | IPv4 |
| RFC 8200 | IPv6 |
| RFC 9293 | TCP |
| RFC 768 | UDP |
| RFC 1035 | DNS |
| RFC 9112 | HTTP/1.1 |
| RFC 8446 | TLS 1.3 |

## Evidence handling

- Hash the capture at acquisition and again before analysis.
- Record the capture point, filter, snaplen, and time source.
- Keep the original read-only; analyze a copy.
- Document tool versions and commands so results are reproducible.
