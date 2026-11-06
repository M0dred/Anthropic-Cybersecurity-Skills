# API Reference - Analyzing PCAP Files

## File formats

### Classic pcap global header (24 bytes)

| Offset | Size | Field |
|---|---|---|
| 0 | 4 | magic: `a1b2c3d4` (usec) or `a1b23c4d` (nsec) |
| 4 | 2 | major version |
| 6 | 2 | minor version |
| 8 | 4 | thiszone |
| 12 | 4 | sigfigs |
| 16 | 4 | snaplen |
| 20 | 4 | network (link type) |

Per-packet header: `ts_sec` (4), `ts_usec` (4), `incl_len` (4), `orig_len` (4).

### pcapng blocks

| Block | Type | Contents |
|---|---|---|
| Section Header | `0x0A0D0D0A` | byte order magic, version |
| Interface Description | `0x00000001` | link type, snaplen, options |
| Enhanced Packet | `0x00000006` | interface id, timestamp high/low, captured/original length, data |
| Simple Packet | `0x00000003` | original length, data |
| Name Resolution | `0x00000004` | DNS-style name records |

Timestamp resolution comes from the IDB `if_tsresol` option (code 9).

## Link types

| Value | Name |
|---|---|
| 1 | Ethernet |
| 101 | Raw IP |
| 113 | Linux cooked capture (SLL) |
| 276 | Linux cooked capture v2 (SLL2) |

## Protocol headers

### Ethernet
```
dst(6) src(6) ethertype(2)
0x0800 IPv4, 0x86DD IPv6, 0x8100 VLAN (skip 4), 0x8847 MPLS
```

### IPv4
```
version/IHL(1) TOS(1) total_len(2) id(2) flags/frag(2) ttl(1) proto(1) checksum(2) src(4) dst(4)
proto: 6 TCP, 17 UDP, 1 ICMP
```

### IPv6
```
version/traffic/flow(4) payload_len(2) next_header(1) hop_limit(1) src(16) dst(16)
```

### TCP
```
sport(2) dport(2) seq(4) ack(4) offset/flags(2) window(2) checksum(2) urgent(2)
flags: FIN 0x01, SYN 0x02, RST 0x04, PSH 0x08, ACK 0x10, URG 0x20
```

### UDP
```
sport(2) dport(2) length(2) checksum(2)
```

## DNS

```
header(12) questions answers authority additional
qname: length-prefixed labels, terminated by 0x00
qtype: 1 A, 28 AAAA, 15 MX, 16 TXT, 5 CNAME, 6 SOA, 12 PTR
```

Tunneling signals: label length > 40, entropy > 3.5, TXT/NULL query types,
high query volume to one domain, encoded subdomains.

## HTTP

```
GET /path HTTP/1.1\r\n
Host: example.com\r\n
User-Agent: ...\r\n
```

POST bodies may contain credentials or exfiltrated data.

## TLS ClientHello SNI

```
record: type=22, version, length
handshake: type=1 (client_hello), length, version, random(32), session_id, cipher_suites,
           compression, extensions
extension 0x0000 = server_name, list of host_name entries
```

## CLI

```bash
python3 scripts/agent.py info    --file capture.pcapng
python3 scripts/agent.py flows   --file capture.pcapng --top 50
python3 scripts/agent.py dns     --file capture.pcapng --out dns.json
python3 scripts/agent.py http    --file capture.pcapng --out http.json
python3 scripts/agent.py tls     --file capture.pcapng --out tls.json
python3 scripts/agent.py beacon  --file capture.pcapng --min-connections 5
python3 scripts/agent.py carve   --file capture.pcapng --out-dir ./objects
```

## Cross-check commands

```bash
capinfos capture.pcapng
tshark -r capture.pcapng -Y dns -T fields -e dns.qry.name | sort | uniq -c | sort -rn
tshark -r capture.pcapng -Y http.request -T fields -e http.host -e http.request.uri
tshark -r capture.pcapng -Y tls.handshake.extensions_server_name -T fields -e tls.handshake.extensions_server_name
tcpdump -r capture.pcapng -nn -c 20
```
