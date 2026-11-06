# Standards and References - Isolating Compromised Endpoints

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Respond | RS.MI-01 | Incidents are contained |
| Respond | RS.MI-02 | Incidents are mitigated |
| Respond | RS.AN-03 | Analysis establishes what happened |
| Protect | PR.AC-05 | Network access is limited to authorized devices |

## NIST SP 800-53 Rev. 5

| Control | Title | Relevance |
|---|---|---|
| IR-4 | Incident Handling | Containment is a defined IR phase |
| IR-4(1) | Automated Incident Handling | EDR isolation is automated containment |
| SC-7 | Boundary Protection | Isolate the host from the network |
| AC-17 | Remote Access | Preserve the responder channel |
| AU-6 | Audit Record Review | Isolation events must be logged |
| SI-4 | System Monitoring | Keep telemetry flowing during isolation |

## NIST SP 800-61r3

- Containment strategies: isolation, segmentation, and removal.
- Isolation is preferred when the adversary is active and the host holds
  evidence.
- Document the containment decision and its business impact.

## MITRE ATT&CK

| Technique | Name | Why isolation matters |
|---|---|---|
| T1021 | Remote Services | Stops lateral movement over SMB/RDP/WinRM |
| T1071 | Application Layer Protocol | Cuts C2 channels |
| T1562.001 | Impair Defenses: Disable or Modify Tools | Attackers may try to disable the agent; verify it is healthy |
| T1486 | Data Encrypted for Impact | Isolation before encryption limits ransomware spread |
| T1041 | Exfiltration Over C2 Channel | Stops data leaving the host |

## CIS Controls v8

- 13.6: Collect network traffic flow logs
- 17.4: Establish and maintain an incident response process
- 4.4: Implement and manage a host-based firewall

## Evidence handling

- Capture memory before isolation when the host is stable.
- Keep a hash of every collected artifact (`sha256sum`).
- Record the chain of custody: who collected, when, from which host, using
  which tool.
- Do not reboot until memory is captured or the decision to discard it is
  documented.
