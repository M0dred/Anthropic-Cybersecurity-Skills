# API Reference - Acquiring Windows Forensics Over WinRM

## Script

```bash
python3 scripts/agent.py --help
```

## Platform commands

```powershell
# WinRM collection
$s = New-PSSession -ComputerName WEB-01 -Credential (Get-Credential)
Invoke-Command -Session $s -ScriptBlock { Get-Process | Export-Csv C:\evidence\processes.csv }
Copy-Item -FromSession $s -Path C:\evidence\processes.csv -Destination .\evidence\
```

```bash
# Linux collection
ps auxf > /evidence/ps.txt
ss -tunap > /evidence/sockets.txt
sudo dd if=/proc/kcore of=/evidence/memory.raw bs=1M
sudo tar czf /evidence/etc.tar.gz /etc
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |