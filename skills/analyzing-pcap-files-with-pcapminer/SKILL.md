---
name: analyzing-pcap-files-with-pcapminer
description: >-
  Mines packet captures (pcap and pcapng) for investigation-grade facts:
  conversation and flow tables, DNS queries and answers, HTTP hosts and URIs,
  TLS server names, cleartext credentials, transferred files, and periodic
  beaconing detected from inter-arrival timing. Use when a network alert needs
  packet-level confirmation, when malware traffic must be characterized, when a
  data-exfiltration path is suspected, or when a capture must be reduced to a
  timeline. Keywords: pcap, pcapng, packet analysis, DNS exfiltration, TLS SNI,
  beaconing, network forensics.
  Do not use for live interface capture - use tcpdump or dumpcap first. Do not
  use for NetFlow or IPFIX records - use analyzing-network-flow-data-with-netflow.
domain: cybersecurity
subdomain: digital-forensics
tags:
- pcap
- network-forensics
- dns
- tls
- beaconing
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- DE.CM-01
- RS.AN-03
- DE.AE-02
mitre_attack:
- T1071.004
- T1048.003
- T1573.002
---

# Analyzing PCAP Files with PcapMiner

## When to Use

- An IDS alert needs packet-level confirmation before escalation.
- Malware traffic must be characterized: C2 host, protocol, jitter, payload.
- DNS tunneling or data exfiltration over DNS is suspected.
- A capture must be reduced to a timeline of hosts, ports, and protocols.
- A beaconing pattern needs a periodicity measurement, not a guess.

**Do not use** for live capture; capture first with `tcpdump`/`dumpcap`, then
analyze the file. **Do not use** for flow records exported by routers; those
lack payload and need a different parser.

## Prerequisites

- The capture file, with its SHA-256 recorded, and the capture point (span
  port, tap, host interface) documented.
- Python 3.9+ for the helper; `tshark`/`tcpdump` optional for cross-checks.
- Knowledge of the network's address plan so internal/external is unambiguous.
- Disk space for carved objects; captures can be large.

## Workflow

### Step 1: Establish capture provenance

```bash
sha256sum capture.pcapng | tee capture.pcapng.sha256
capinfos capture.pcapng 2>/dev/null || python3 scripts/agent.py info --file capture.pcapng
```

Record: capture start/end, packet count, interface, snaplen, and filter. A
capture taken after the incident may have missed the initial payload.

### Step 2: Build the conversation table

```bash
python3 scripts/agent.py flows --file capture.pcapng --top 50
```

The flow table answers: who talked to whom, on which port, how much, and for
how long. Sort by bytes to find exfiltration and by connection count to find
scanning.

### Step 3: Extract protocol artifacts

```bash
python3 scripts/agent.py dns    --file capture.pcapng --out dns.json
python3 scripts/agent.py http   --file capture.pcapng --out http.json
python3 scripts/agent.py tls    --file capture.pcapng --out tls.json
```

| Artifact | Why it matters |
|---|---|
| DNS query name and length | Long, high-entropy labels indicate tunneling |
| DNS answer | Sinkhole or fast-flux detection |
| HTTP Host and URI | C2 path, staging URL, credential POST |
| User-Agent | Tool fingerprint |
| TLS SNI | Destination when IP is shared |
| TLS certificate subject | Self-signed or lookalike infrastructure |

### Step 4: Detect beaconing

```bash
python3 scripts/agent.py beacon --file capture.pcapng --min-connections 5
```

The detector groups connections by `(src, dst, dport)`, computes inter-arrival
times, and reports the mean interval, standard deviation, and coefficient of
variation (CV). A CV below 0.2 with a stable interval is a strong beacon
signal; jittered malware raises the CV, so also report the median and the
interval histogram.

### Step 5: Carve and hash transferred objects

```bash
python3 scripts/agent.py carve --file capture.pcapng --out-dir ./objects
```

The carver reassembles TCP streams and writes objects with recognizable magic
bytes (PE, PDF, ZIP, Office, ELF). Every object gets a SHA-256 so it can be
submitted to a sandbox.

### Step 6: Correlate and report

- Map external IPs to ASN and reputation (separate enrichment step).
- Compare DNS names against threat-intelligence feeds.
- Build a timeline: first packet, first DNS, first TLS, first POST, last packet.
- Attach the flow table and the carved-object manifest to the incident.

## Verification

- Packet count and capture window from `info` match `capinfos`/`tcpdump -r`.
- Flow byte totals reconcile with the sum of packet lengths.
- DNS names extracted match a `tshark -Y dns` spot check.
- TLS SNI matches the certificate subject where the handshake is complete.
- Carved object hashes are stable across two runs.

## Common Pitfalls

- **Snaplen truncation.** A 96-byte snaplen cuts payloads; TLS SNI and HTTP
  bodies may be missing.
- **TCP reassembly.** Out-of-order and retransmitted segments break naive
  carving; use sequence numbers.
- **Encrypted traffic.** Without keys you get metadata only; do not claim
  content you cannot see.
- **NAT and proxies.** The capture point changes which IP is "the client".
- **Clock skew.** Capture timestamps come from the capturing host; note drift.
- **Huge captures.** Filter by host or port before analysis to keep runtime
  bounded.

## References

- `references/api-reference.md` - pcap/pcapng formats, protocol fields
- `references/standards.md` - NIST, ATT&CK, evidence handling
- `references/workflows.md` - triage sequence and beaconing math
- `scripts/agent.py` - info, flows, dns, http, tls, beacon, carve
