---
name: configuring-powershell-remoting-for-forensics
description: >-
  Configures WinRM and PowerShell Remoting so a responder can collect volatile
  and persistent evidence from Windows hosts at scale, then hardens the channel
  after use. Covers listener setup, certificate or Kerberos authentication,
  trusted-host scoping, session limits, collection commands for memory, process,
  network, registry, event logs, and MFT, and the cleanup that removes the
  temporary access. Use when a DFIR collection needs remote access to many
  Windows hosts, when WinRM is blocked or misconfigured, or when a collection
  channel must be opened and then closed cleanly. Keywords: WinRM, PowerShell
  Remoting, Enter-PSSession, Invoke-Command, WSMan, DFIR collection, remote
  forensics.
  Do not use for Linux host collection - use acquiring-host-forensics. Do not
  use for isolating a host - use isolating-compromised-endpoints.
domain: cybersecurity
subdomain: digital-forensics
tags:
- digital-forensics
- windows
- winrm
- powershell
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.AN-03
- DE.CM-01
- PR.AC-05
mitre_attack:
- T1021.006
- T1059.001
- T1070
---

# Configuring PowerShell Remoting for Forensics

## When to Use

- A DFIR collection must reach many Windows hosts without an agent.
- WinRM is disabled, firewalled, or failing authentication.
- A temporary collection channel must be opened and then removed.
- A responder needs memory, registry, event logs, or MFT from a host.

**Do not use** for Linux collection; SSH and the Linux collectors are different.
**Do not use** for network isolation; that is a containment action.

## Prerequisites

- Local administrator on the target hosts, and domain admin where Kerberos is
  used.
- Network reachability to TCP 5985 (HTTP) or 5986 (HTTPS).
- A service account dedicated to collection, with a defined expiry.
- Authorization and scope: which hosts, which artifacts, and for how long.

## Workflow

### Step 1: Enable WinRM on the targets

```powershell
Enable-PSRemoting -Force -SkipNetworkProfileCheck
Set-Service WinRM -StartupType Automatic
Start-Service WinRM
winrm enumerate winrm/config/listener
```

### Step 2: Choose the authentication and transport

| Transport | Port | Use when |
|---|---|---|
| HTTP + Kerberos | 5985 | domain-joined hosts, trusted network |
| HTTPS + certificate | 5986 | untrusted network or workgroup |
| CredSSP | 5985 | double-hop needed (avoid if possible) |

```powershell
# HTTPS listener with a certificate
New-WSManInstance -ResourceURI winrm/config/Listener -SelectorSet @{Address='*';Transport='HTTPS'} `
  -ValueSet @{Hostname='web-01.example.com';CertificateThumbprint='<thumbprint>'}
```

### Step 3: Scope the trust

```powershell
# Trusted hosts for workgroup scenarios (prefer HTTPS instead)
Set-Item WSMan:\localhost\Client\TrustedHosts -Value 'web-01,web-02' -Concatenate

# Limit concurrent shells and memory per shell
Set-Item WSMan:\localhost\Shell\MaxShellsPerUser -Value 10
Set-Item WSMan:\localhost\Shell\MaxMemoryPerShellMB -Value 1024
```

### Step 4: Collect evidence

```powershell
$session = New-PSSession -ComputerName web-01 -Credential (Get-Credential) -Authentication Negotiate
Invoke-Command -Session $session -ScriptBlock {
    Get-Process | Export-Csv C:\Windows\Temp\processes.csv -NoTypeInformation
    Get-NetTCPConnection | Export-Csv C:\Windows\Temp\sockets.csv -NoTypeInformation
    wevtutil epl Security C:\Windows\Temp\Security.evtx
    reg export HKLM\SYSTEM C:\Windows\Temp\SYSTEM.reg /y
}
Copy-Item -FromSession $session -Path C:\Windows\Temp\*.csv -Destination .\evidence\
Copy-Item -FromSession $session -Path C:\Windows\Temp\Security.evtx -Destination .\evidence\
Remove-PSSession $session
```

Memory capture needs a tool on the host (WinPmem or Magnet RAM Capture); run it
through the session and copy the raw file back.

### Step 5: Hash and record

```powershell
Get-FileHash .\evidence\* -Algorithm SHA256 | Export-Csv .\evidence\manifest.csv -NoTypeInformation
```

Record the host, the artifacts, the collection account, the time, and the
hashes in the case file.

### Step 6: Harden and clean up

```powershell
# Remove the temporary listener and trusted hosts
Remove-WSManInstance -ResourceURI winrm/config/Listener -SelectorSet @{Address='*';Transport='HTTPS'}
Set-Item WSMan:\localhost\Client\TrustedHosts -Value ''
# Disable WinRM if it was enabled only for the collection
Disable-PSRemoting -Force
```

Rotate the collection account password and remove it from any group added for
the engagement.

## Verification

- `Test-WSMan -ComputerName <host>` succeeds before collection.
- Each artifact exists locally and its hash matches the remote hash.
- The collection account's logon events are present in the target's Security log.
- The listener and trusted-host entries are removed after collection.
- The collection account is disabled or its password rotated.

## Common Pitfalls

- **TrustedHosts as a shortcut.** It disables the mutual authentication check;
  prefer HTTPS with a certificate.
- **CredSSP for convenience.** It delegates credentials to the target and is a
  common lateral-movement path.
- **Leaving WinRM enabled.** A collection channel left open is an attack path.
- **No hash after copy.** Evidence without a hash is not evidence.
- **Collecting into the target's temp directory without cleanup.** Leaves
  artifacts that confuse later analysis.
- **Using a domain admin for collection.** Use a dedicated, time-bound account.

## References

- `references/api-reference.md` - WinRM configuration and collection commands
- `references/standards.md` - NIST, ATT&CK, evidence handling
- `references/workflows.md` - collection sequence and cleanup checklist
- `scripts/agent.py` - configure, test, collect, cleanup
