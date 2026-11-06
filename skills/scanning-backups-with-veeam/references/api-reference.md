# API Reference - Scanning Backups with Veeam

## Script

```bash
python3 scripts/agent.py --help
```

## Platform commands

```powershell
# Veeam Backup & Replication
Connect-VBRServer -Server vbr.example.com
Start-VBRInstantRecovery -RestorePoint (Get-VBRRestorePoint -Name "VM-01") -VMName "VM-01-restored"
Start-VBRScanBackup -RestorePoint (Get-VBRRestorePoint -Name "VM-01")
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |