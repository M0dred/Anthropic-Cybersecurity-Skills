# Standards and References - Blocking Malicious IP Addresses

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Protect | PR.AC-05 | Network access is limited to authorized users, processes, and devices |
| Detect | DE.CM-01 | Networks are monitored to detect potential cybersecurity events |
| Respond | RS.MI-01 | Incidents are contained |
| Respond | RS.MI-02 | Incidents are mitigated |

## NIST SP 800-53 Rev. 5

| Control | Title | Relevance |
|---|---|---|
| SC-7 | Boundary Protection | Enforce at managed interfaces; deny by default |
| SC-7(5) | Deny by Default / Allow by Exception | The blocklist is an explicit exception to the allowlist |
| AC-4 | Information Flow Enforcement | Approve and enforce flows between systems |
| SI-4 | System Monitoring | Verify the block through logs and counters |
| IR-4 | Incident Handling | Containment is a documented IR phase |

## MITRE ATT&CK

| Technique | Name | Why the block matters |
|---|---|---|
| T1562.004 | Impair Defenses: Disable or Modify System Firewall | Attackers remove blocks; verify the rule still exists |
| T1071 | Application Layer Protocol | C2 over HTTP/DNS is stopped at egress |
| T1105 | Ingress Tool Transfer | Blocks the download of second-stage payloads |
| T1595 | Active Scanning | Stops the scanner at the perimeter |

## CIS Controls v8

- 4.4: Implement and manage a firewall on servers and workstations
- 4.5: Implement and manage a firewall on cloud infrastructure
- 12.2: Establish and maintain a secure network architecture
- 13.1: Centralize security event alerting

## Regulatory notes

- **PCI DSS 4.0** 1.3: restrict inbound and outbound traffic to that which is
  necessary for the cardholder data environment.
- **HIPAA Security Rule** 164.312(a)(1): access control, including network
  isolation of ePHI systems.
- **NIS2** Article 21(2)(e): network and information system security, including
  traffic filtering.

## Change management

A production block is a change. Record: ticket ID, approver, target, rule text,
rollback command, and expiry date. Blocks without an expiry become permanent
technical debt and are a common audit finding.
