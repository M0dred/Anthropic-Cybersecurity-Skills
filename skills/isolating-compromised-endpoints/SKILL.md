---
name: isolating-compromised-endpoints
description: >-
  Network-isolates a compromised endpoint through the EDR control plane
  (CrowdStrike Falcon, Microsoft Defender for Endpoint, SentinelOne, Cortex XDR,
  Carbon Black) or the network fabric (802.1X, VLAN change, switch ACL), while
  keeping the responder's management channel open. Covers pre-isolation
  evidence capture, isolation verification, and controlled unisolation. Use when
  a host is beaconing, spreading laterally, or running confirmed malware and
  must be cut off without being powered down. Keywords: isolate host, network
  containment, EDR isolation, quarantine endpoint, contain and continue.
  Do not use for blocking an IP address at the perimeter - use
  blocking-malicious-ip-addresses. Do not use for deleting or quarantining a
  file - use eradicating-threats-by-deleting-files.
domain: cybersecurity
subdomain: endpoint-security
tags:
- incident-response
- containment
- edr
- crowdstrike
- defender
- endpoint-security
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.MI-01
- PR.AC-05
- DE.CM-01
mitre_attack:
- T1562.001
- T1071
- T1021
---

# Isolating Compromised Endpoints

## When to Use

- An endpoint is beaconing to command-and-control and must stop now.
- A host is spreading laterally through SMB, WMI, or RDP.
- Confirmed malware is running and the host cannot be rebuilt immediately.
- A ransomware pre-encryption stage is detected on a server.
- An analyst needs the host alive for memory capture but off the network.

**Do not use** when the goal is to block an external IP at a firewall; that is a
network control, not a host control. **Do not use** for file quarantine or
process termination; isolation keeps the host running and observable.

## Prerequisites

- EDR agent healthy and reporting on the target host.
- The EDR console role that allows isolation (`Host containment` in CrowdStrike,
  `Isolate device` in Defender, `Network quarantine` in SentinelOne).
- A documented responder access path: EDR remote shell, out-of-band management,
  or a console session that survives isolation.
- The host's business owner and criticality, so the blast radius is understood.
- A ticket number; isolation is a change even during an incident.

## Workflow

### Step 1: Capture volatile evidence before isolation

Isolation changes the host's network state and can terminate live sessions.
Collect first:

```bash
# Memory and process state (Windows, via EDR remote shell or PsExec)
winpmem_mini_x64.exe C:\evidence\memory.raw
tasklist /v > C:\evidence\tasklist.txt
netstat -ano > C:\evidence\netstat.txt
Get-WinEvent -LogName Security -MaxEvents 5000 | Export-Csv C:\evidence\security.csv

# Linux
sudo dd if=/proc/kcore of=/evidence/memory.raw bs=1M
ps auxf > /evidence/ps.txt
ss -tunap > /evidence/sockets.txt
```

If the EDR supports live-response commands, run them through the console so the
capture does not depend on the host's own network stack.

### Step 2: Choose the isolation mechanism

| Mechanism | When to use | Responder access |
|---|---|---|
| EDR network isolation | Agent healthy; fastest; per-host | EDR console tunnel |
| Switch port shutdown | No EDR; physical access available | Console / OOB |
| VLAN move to quarantine | Many hosts; NAC in place | Quarantine VLAN + jump host |
| 802.1X re-authentication | NAC with posture checks | Remediation VLAN |
| Host firewall deny-all | Agent absent; OS reachable | Local console only |

Prefer EDR isolation: it is reversible in seconds and preserves the management
channel.

### Step 3: Isolate

```bash
# CrowdStrike Falcon
curl -X POST "https://api.crowdstrike.com/devices/entities/devices-actions/v2?action_name=contain" \
  -H "Authorization: Bearer $CS_TOKEN" -H "Content-Type: application/json" \
  -d '{"ids":["<device_id>"]}'

# Microsoft Defender for Endpoint
curl -X POST "https://api.securitycenter.microsoft.com/api/machines/<id>/isolate" \
  -H "Authorization: Bearer $MDE_TOKEN" -H "Content-Type: application/json" \
  -d '{"Comment":"INC-1234 containment","IsolationType":"Full"}'

# SentinelOne
curl -X POST "https://<tenant>.sentinelone.net/web/api/v2.1/agents/actions/isolate" \
  -H "Authorization: ApiToken $S1_TOKEN" -H "Content-Type: application/json" \
  -d '{"filter":{"ids":["<agent_id>"]}}'

# Cortex XDR
curl -X POST "https://api-<tenant>.xdr.us.paloaltonetworks.com/public_api/v1/endpoints/isolate" \
  -H "Authorization: $XDR_TOKEN" -H "Content-Type: application/json" \
  -d '{"request_data":{"endpoint_id":"<id>"}}'
```

Network fallback:

```bash
# Cisco IOS: move the port to a quarantine VLAN
configure terminal
interface GigabitEthernet1/0/12
 switchport access vlan 999
 description QUARANTINE-INC-1234
 shutdown
 end
write memory
```

### Step 4: Verify isolation

```bash
# From the host (via EDR remote shell): outbound must fail
curl -m 5 https://example.com ; echo "exit=$?"
ping -c 2 8.8.8.8

# From the EDR console: status must read contained/isolated
curl "https://api.crowdstrike.com/devices/entities/devices/v2?ids=<device_id>" \
  -H "Authorization: Bearer $CS_TOKEN" | jq '.resources[0].status'

# From the network: the switch port is down or in the quarantine VLAN
show interface GigabitEthernet1/0/12 status
```

Confirm the responder channel still works. If it does not, you have lost the
ability to investigate and must unisolate or use out-of-band access.

### Step 5: Keep the host observable

- Leave the agent running; do not uninstall or disable it.
- Keep the host powered on so memory and volatile state survive.
- Snapshot the VM if the host is virtual, before any remediation.
- Record the isolation timestamp and the exact API call for the timeline.

### Step 6: Unisolate under control

Unisolate only after one of: the host is rebuilt, the malware is removed and
verified, or the incident is closed with a documented exception.

```bash
# CrowdStrike
curl -X POST "https://api.crowdstrike.com/devices/entities/devices-actions/v2?action_name=lift_containment" \
  -H "Authorization: Bearer $CS_TOKEN" -H "Content-Type: application/json" \
  -d '{"ids":["<device_id>"]}'

# Defender
curl -X POST "https://api.securitycenter.microsoft.com/api/machines/<id>/unisolate" \
  -H "Authorization: Bearer $MDE_TOKEN" -H "Content-Type: application/json" \
  -d '{"Comment":"INC-1234 remediation verified"}'
```

## Verification

- The EDR console reports the host as contained or isolated.
- Outbound connections from the host fail; the responder channel succeeds.
- The host still reports telemetry to the EDR (heartbeat is present).
- The isolation action is recorded in the incident timeline with the device ID.
- A second analyst can find the host by name and see the isolation state.

## Common Pitfalls

- **Powering off instead of isolating.** Losing memory and volatile state is
  usually worse than leaving the host running.
- **Isolating the jump host.** Verify the responder path does not traverse the
  host being isolated.
- **Forgetting virtual hosts.** Isolating a VM's guest OS does not stop
  hypervisor-level traffic; isolate the vNIC or the port group too.
- **No expiry.** An isolated server that nobody unisolates becomes an outage.
- **Isolating by hostname only.** Hostnames are spoofable and duplicated; use
  the EDR device ID.
- **Skipping the business owner.** Isolation of a production database can be an
  outage; notify before, not after.

## References

- `references/api-reference.md` - EDR and network isolation APIs
- `references/standards.md` - NIST CSF, 800-53, ATT&CK mappings
- `references/workflows.md` - decision tree, evidence-first sequence, unisolation
- `scripts/agent.py` - isolate, verify, and unisolate through EDR APIs
