---
name: capturing-network-traffic-over-winrm
description: >-
  Leverages the Windows built-in PowerShell and WinRM capabilities to connect to a Windows host. It then connects to the Netsh tool to create an ETL file which is the equivalent of a Wireshark PCAP file by using the PS-Remote integration. After receiving the. Starts a packet capture on the host and retrieves the pcap. Use when network traffic over WinRM must be collected as evidence, or when volatile data about network traffic over WinRM must be preserved. Keywords: capturing, network, traffic, over, winrm, acquisition, forensics, digital forensics. Do not use for acquiring mft over winrm - use `acquiring-mft-over-winrm`.
domain: cybersecurity
subdomain: digital-forensics
tags:
- digital-forensics
- evidence
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.AN-03
- DE.CM-01
- RS.MA-01
mitre_attack:
- T1005
- T1070
- T1112
---

# Capturing Network Traffic Over WinRM

## When to Use

- An incident requires forensic evidence from a host or capture point.
- A review or legal process needs a defensible acquisition.
- Volatile data must be preserved before containment or reboot.

**Do not use** for acquiring mft over winrm - use `acquiring-mft-over-winrm`.

## Prerequisites

- Authorization and scope for the acquisition.
- A target directory with enough space, and a write blocker where required.
- The transport: local, WinRM, SSH, or an agent.

## Workflow

### Step 1: Authorize and scope

Record who approved the acquisition and what is in scope.

### Step 2: Capture volatile data first

Memory, processes, sockets, and logged-on users before anything changes.

### Step 3: Capture persistent data

Registry, MFT, event logs, and file system metadata.

### Step 4: Hash and record

SHA-256 every artifact and record the tool, version, and time.

### Step 5: Transfer and store

Move to evidence storage, verify the hash after transfer, and restrict access.

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

```powershell
# WinRM collection
$s = New-PSSession -ComputerName WEB-01 -Credential (Get-Credential)
Invoke-Command -Session $s -ScriptBlock { Get-Process | Export-Csv C:\evidence\processes.csv }
Copy-Item -FromSession $s -Path C:\evidence\processes.csv -Destination .\evidence\
```

## Verification

- Every artifact has a hash that matches after transfer.
- The chain-of-custody form is complete.
- The acquisition did not alter the source more than documented.
- The evidence is stored with access controls.

## Common Pitfalls

- Rebooting before memory capture.
- Writing to the evidence disk.
- Missing the hash after transfer.
- Acquiring beyond the authorized scope.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
