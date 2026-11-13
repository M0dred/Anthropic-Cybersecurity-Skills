# API Reference - PowerShell Remoting for Forensics

## Enable and inspect

```powershell
Enable-PSRemoting -Force -SkipNetworkProfileCheck
winrm enumerate winrm/config/listener
winrm get winrm/config
Test-WSMan -ComputerName web-01
```

## Listeners

```powershell
# HTTP (5985)
winrm create winrm/config/Listener?Address=*+Transport=HTTP

# HTTPS (5986)
New-WSManInstance -ResourceURI winrm/config/Listener `
  -SelectorSet @{Address='*';Transport='HTTPS'} `
  -ValueSet @{Hostname='web-01.example.com';CertificateThumbprint='<thumbprint>'}
```

## Authentication

| Method | Command |
|---|---|
| Kerberos | `New-PSSession -ComputerName web-01 -Authentication Kerberos` |
| Negotiate | `New-PSSession -ComputerName web-01 -Authentication Negotiate` |
| Certificate | `New-PSSession -ComputerName web-01 -CertificateThumbprint <t>` |
| CredSSP | `New-PSSession -ComputerName web-01 -Authentication CredSSP -Credential $c` |

## Collection commands

```powershell
# Volatile
Get-Process | Export-Csv C:\Windows\Temp\processes.csv -NoTypeInformation
Get-CimInstance Win32_Process | Export-Csv C:\Windows\Temp\wmi-processes.csv -NoTypeInformation
Get-NetTCPConnection | Export-Csv C:\Windows\Temp\sockets.csv -NoTypeInformation
Get-LoggedOnUser | Export-Csv C:\Windows\Temp\loggedon.csv -NoTypeInformation

# Persistent
wevtutil epl Security C:\Windows\Temp\Security.evtx
wevtutil epl System C:\Windows\Temp\System.evtx
reg export HKLM\SYSTEM C:\Windows\Temp\SYSTEM.reg /y
reg export HKLM\SOFTWARE C:\Windows\Temp\SOFTWARE.reg /y
fsutil usn readjournal C: csv > C:\Windows\Temp\usn.csv

# Memory (requires a tool on the host)
winpmem_mini_x64.exe C:\Windows\Temp\memory.raw
```

## Copy back

```powershell
Copy-Item -FromSession $session -Path C:\Windows\Temp\*.csv -Destination .\evidence\
Copy-Item -FromSession $session -Path C:\Windows\Temp\*.evtx -Destination .\evidence\
Get-FileHash .\evidence\* -Algorithm SHA256 | Export-Csv .\evidence\manifest.csv -NoTypeInformation
```

## Limits

```powershell
Set-Item WSMan:\localhost\Shell\MaxShellsPerUser -Value 10
Set-Item WSMan:\localhost\Shell\MaxMemoryPerShellMB -Value 1024
Set-Item WSMan:\localhost\MaxEnvelopeSizekb -Value 2048
```

## Cleanup

```powershell
Remove-PSSession -Session (Get-PSSession)
Remove-WSManInstance -ResourceURI winrm/config/Listener -SelectorSet @{Address='*';Transport='HTTPS'}
Set-Item WSMan:\localhost\Client\TrustedHosts -Value ''
Disable-PSRemoting -Force
```

## CLI

```bash
python3 scripts/agent.py configure --hosts web-01,web-02 --transport https --dry-run
python3 scripts/agent.py test --hosts web-01,web-02
python3 scripts/agent.py collect --hosts web-01 --artifacts process,network,logs --out ./evidence
python3 scripts/agent.py cleanup --hosts web-01,web-02 --dry-run
```
