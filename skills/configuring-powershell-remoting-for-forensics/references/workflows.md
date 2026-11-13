# Workflows - PowerShell Remoting for Forensics

## Collection sequence

```
authorize -> enable WinRM -> test -> collect volatile -> collect persistent
-> copy back -> hash -> cleanup -> rotate account
```

## Artifact order

| Order | Artifact | Why |
|---|---|---|
| 1 | Memory | lost on reboot |
| 2 | Processes and sockets | change every second |
| 3 | Logged-on users | session state |
| 4 | Event logs | persistent but rotated |
| 5 | Registry hives | persistent |
| 6 | MFT / USN journal | persistent |

## Per-host checklist

- [ ] `Test-WSMan` succeeds.
- [ ] The collection account is dedicated and time-bound.
- [ ] Volatile artifacts captured first.
- [ ] Each artifact hashed after copy.
- [ ] The listener and TrustedHosts entry removed.
- [ ] The account password rotated.

## Cleanup checklist

- [ ] `Remove-PSSession` for all sessions.
- [ ] Temporary listener removed.
- [ ] `TrustedHosts` cleared.
- [ ] `Disable-PSRemoting` if it was enabled for the collection.
- [ ] Temporary files removed from the target.
- [ ] Account disabled or password rotated.

## Record template

```
Case:        INC-1234
Hosts:       web-01, web-02
Transport:   HTTPS 5986 with certificate
Account:     svc-dfir (created 2026-08-31, expires 2026-09-01)
Artifacts:   memory, processes, sockets, Security.evtx, SYSTEM.reg
Hashes:      manifest.csv (sha256 ...)
Cleanup:     listener removed, TrustedHosts cleared, account disabled
Operator:    analyst@example.com
```
