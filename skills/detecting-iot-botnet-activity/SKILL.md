---
name: detecting-iot-botnet-activity
description: >-
  Detects IoT botnet activity by analyzing network traffic for command-and-control
  patterns, scanning behavior, and known botnet signatures across smart devices,
  cameras, routers, and industrial sensors. Covers Mirai, Gafgyt, Mozi, and
  emerging IoT malware families. Use when unusual outbound traffic originates from
  IoT devices, when a device shows signs of compromise, or when building IoT
  network segmentation. Keywords: IoT security, botnet, Mirai, Gafgyt, Mozi,
  smart device compromise, camera security, router botnet.
  Do not use for enterprise server botnet detection - use
  hunting-threat-indicators-across-siem. Do not use for OT/ICS botnet detection -
  use monitoring-scada-modbus-traffic-anomalies.
domain: cybersecurity
subdomain: network-security
tags:
- iot-security
- botnet
- network-monitoring
- threat-hunting
- mirai
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- DE.CM-01
- RS.AN-03
- PR.AC-05
mitre_attack:
- T1059
- T1071
- T1498
---

# Detecting IoT Botnet Activity

## When to Use

- A smart camera, router, or sensor generates unusual outbound traffic.
- An IoT device is suspected of participating in a DDoS botnet.
- Network scanning originates from devices that should not scan.
- Building IoT network segmentation to contain compromised devices.

**Do not use** for enterprise server botnet detection; that is SIEM/EDR territory.
**Do not use** for OT/ICS botnet detection; that requires ICS-specific protocols.

## Prerequisites

- Network traffic visibility: SPAN port, tap, or flow data (NetFlow/sFlow).
- A list of known IoT device MAC addresses or OUIs for inventory.
- DNS query logs and DHCP lease logs for IoT VLANs.
- tcpdump or Zeek for packet capture and analysis.

## Workflow

### Step 1: Identify IoT devices on the network

```bash
# Inventory IoT devices by MAC OUI
nmap -sn 192.168.1.0/24 | grep -i "Nmap scan report"
# Cross-reference with known IoT OUIs
curl -sS https://raw.githubusercontent.com/royhills/arp-scan/master/ieee-oui.txt | grep -i "xiaomi\|tp-link\|d-link\|hikvision\|dahua"
```

### Step 2: Baseline normal IoT traffic

IoT devices should have predictable patterns: NTP, occasional cloud API calls,
minimal peer-to-peer traffic. Deviations indicate compromise.

```bash
# Capture IoT VLAN traffic for 24 hours
tcpdump -i eth1 -nn -s0 -w iot_baseline.pcap vlan 100
# Analyze with Zeek
zeek -r iot_baseline.pcap
```

### Step 3: Detect botnet C2 patterns

| Pattern | Indicator |
|---|---|
| Hardcoded C2 IPs | Repeated connections to rare destinations |
| DNS DGA | High-entropy domain queries from one device |
| Telnet/SSH scanning | Outbound connection attempts to port 23/22 on many IPs |
| IRC traffic | TCP 6667-6669 from non-user devices |
| Mirai signature | Telnet login attempts with default credentials |

```bash
# Detect scanning behavior
tshark -r iot_baseline.pcap -Y "tcp.flags.syn==1 && tcp.flags.ack==0" \
  -T fields -e ip.src | sort | uniq -c | sort -rn | head -20

# Detect DNS DGA
zeek -r iot_baseline.pcap dns.log
awk '{print $9}' dns.log | sort | uniq -c | sort -rn | head -20
```

### Step 4: Identify the botnet family

| Family | C2 Pattern | Scanning | Payload |
|---|---|---|---|
| Mirai | Hardcoded IPs + Telnet | Aggressive 23/22 | DDoS |
| Gafgyt | IRC-based | Telnet + SSH | DDoS |
| Mozi | P2P (DHT) | Persistent | DDoS + proxy |
| Hide 'N Seek | Custom TCP | Proprietary | Data theft |

### Step 5: Contain and remediate

```bash
# Isolate the device
iptables -A FORWARD -s <device_ip> -j DROP
# Block C2 at DNS
echo "0.0.0.0 <c2_domain>" >> /etc/dnsmasq.conf
# Factory reset the device and change default credentials
```

## Verification

- The device no longer generates outbound scanning traffic.
- DNS queries from the device return to baseline volume.
- No connections to known C2 IPs or domains.
- The device is isolated from the production VLAN.

## Common Pitfalls

- **Ignoring P2P botnets.** Mozi uses DHT; there is no central C2 to block.
- **Blocking all IoT traffic.** Breaks device functionality; segment instead.
- **Not changing default passwords.** Most IoT botnets exploit default credentials.
- **No inventory.** You cannot detect anomalous traffic from unknown devices.

## References

- `references/api-reference.md` - detection commands and botnet signatures
- `references/standards.md` - NIST, ATT&CK mappings
- `references/workflows.md` - detection and containment flow
- `scripts/agent.py` - traffic analysis and botnet detection helper
