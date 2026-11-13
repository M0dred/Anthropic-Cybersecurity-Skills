# Standards and References - PowerShell Remoting for Forensics

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Respond | RS.AN-03 | Analysis establishes what happened |
| Detect | DE.CM-01 | Networks are monitored |
| Protect | PR.AC-05 | Network access is limited |

## NIST SP 800-53 Rev. 5

| Control | Title | Relevance |
|---|---|---|
| AC-17 | Remote Access | WinRM is remote access |
| AC-17(2) | Encryption in Transit | Use HTTPS, not HTTP |
| AU-6 | Audit Record Review | Collection logons are audited |
| IR-4 | Incident Handling | Evidence acquisition |
| SC-7 | Boundary Protection | Restrict 5985/5986 |

## NIST SP 800-86

- Acquire volatile data before persistent data.
- Hash every artifact.
- Document the tool, version, and operator.
- Preserve the chain of custody.

## MITRE ATT&CK

| Technique | Name | Relevance |
|---|---|---|
| T1021.006 | Remote Services: Windows Remote Management | WinRM is a lateral-movement path |
| T1059.001 | PowerShell | Collection runs in PowerShell |
| T1070 | Indicator Removal | Cleanup must not destroy evidence |

## CIS Benchmark (Windows Server)

- 2.3.1.1: Ensure WinRM service is configured for encryption.
- 2.3.1.2: Ensure WinRM is not exposed to untrusted networks.
- 18.9.59: Ensure WinRM listeners are reviewed.

## Evidence handling

- Hash before and after transfer.
- Store evidence on write-once media where possible.
- Record the collection account and its authorization.
- Remove the temporary access after collection.
