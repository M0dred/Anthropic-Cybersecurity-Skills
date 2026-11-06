# Workflows - Isolating Compromised Endpoints

## Decision tree

```
Is the host actively malicious (beaconing, lateral movement, encrypting)?
├─ no  -> monitor and enrich; do not isolate yet
└─ yes -> Is the EDR agent healthy?
          ├─ yes -> Capture volatile evidence, then EDR-isolate
          └─ no  -> Is there switch/OOB access?
                    ├─ yes -> Move the port to quarantine VLAN / shutdown
                    └─ no  -> Host firewall deny-all or physical disconnect
```

## Evidence-first sequence

1. Snapshot the VM (if virtual).
2. Capture memory, process list, sockets, and recent event logs.
3. Record the EDR device ID and the current network connections.
4. Isolate.
5. Verify isolation and responder access.
6. Preserve the agent and the host state.

## Containment layers

| Layer | Action | Reversible |
|---|---|---|
| EDR | network containment | yes, seconds |
| Hypervisor | disconnect vNIC / port group | yes |
| Switch | quarantine VLAN / shutdown | yes, console needed |
| NAC | re-authorize to remediation VLAN | yes |
| Host firewall | deny all inbound/outbound | yes, local console |

## Verification matrix

| Test | Expected after isolation |
|---|---|
| `curl https://example.com` from host | fails |
| `ping 8.8.8.8` from host | fails |
| EDR heartbeat | present |
| EDR remote shell | works |
| `nmap` from peer to host | filtered |
| SIEM still receives host logs | yes, via agent buffer |

## Unisolation checklist

- [ ] Malware removed and a full scan is clean.
- [ ] Persistence removed (services, scheduled tasks, run keys, cron).
- [ ] Credentials used on the host rotated.
- [ ] Patch applied for the exploited vulnerability.
- [ ] Incident owner approved.
- [ ] Unisolation time recorded in the timeline.
- [ ] Post-recovery monitoring for 24-72 hours.

## Incident record template

```
Incident:      INC-1234
Host:          WEB-01 (device id 0123abcd)
Mechanism:     CrowdStrike contain
Evidence:      memory.raw (sha256 ...), netstat.txt, security.csv
Isolated at:   2026-08-31T10:20Z by analyst@example.com
Responder:     EDR remote shell (verified)
Unisolated at: 2026-09-01T09:05Z after rebuild + scan
Approver:      soc-lead@example.com
```
