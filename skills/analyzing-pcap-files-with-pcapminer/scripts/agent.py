#!/usr/bin/env python3
"""Mine pcap and pcapng captures for investigation-grade facts.

Subcommands:
    info     Capture metadata (format, link type, packets, window).
    flows    Conversation table ranked by bytes or connections.
    dns      DNS queries and answers.
    http     HTTP requests (host, URI, method, user-agent).
    tls      TLS ClientHello server names.
    beacon   Periodicity analysis per (src, dst, dport).
    carve    Reassemble TCP streams and write objects with magic bytes.

Examples:
    python3 agent.py info   --file capture.pcapng
    python3 agent.py flows  --file capture.pcapng --top 30
    python3 agent.py dns    --file capture.pcapng --out dns.json
    python3 agent.py beacon --file capture.pcapng --min-connections 5
"""
from __future__ import annotations

import argparse
import hashlib
import ipaddress
import json
import math
import os
import struct
import sys
from collections import defaultdict

PCAP_MAGICS = {0xA1B2C3D4: ("<", 1e-6), 0xD4C3B2A1: (">", 1e-6),
               0xA1B23C4D: ("<", 1e-9), 0x4D3CB2A1: (">", 1e-9)}
LINK_ETHERNET, LINK_RAW, LINK_SLL, LINK_SLL2 = 1, 101, 113, 276
MAGIC = {b"MZ": "pe", b"%PDF": "pdf", b"PK\x03\x04": "zip", b"\x7fELF": "elf",
         b"\xd0\xcf\x11\xe0": "ole", b"Rar!": "rar", b"7z\xbc\xaf": "7z"}


def read_pcap(path):
    with open(path, "rb") as handle:
        head = handle.read(24)
        if len(head) < 24:
            return
        magic = struct.unpack("<I", head[:4])[0]
        if magic in PCAP_MAGICS:
            endian, scale = PCAP_MAGICS[magic]
            linktype = struct.unpack(endian + "I", head[20:24])[0]
            while True:
                rec = handle.read(16)
                if len(rec) < 16:
                    break
                ts_sec, ts_frac, incl, _orig = struct.unpack(endian + "IIII", rec)
                data = handle.read(incl)
                if len(data) < incl:
                    break
                yield ts_sec + ts_frac * scale, linktype, data
        elif magic == 0x0A0D0D0A:
            handle.seek(0)
            yield from read_pcapng(handle)


def read_pcapng(handle):
    interfaces = []
    while True:
        header = handle.read(8)
        if len(header) < 8:
            break
        block_type, block_len = struct.unpack("<II", header)
        if block_len < 12:
            break
        body = handle.read(block_len - 12)
        handle.read(4)  # trailing length
        if block_type == 0x0A0D0D0A:
            interfaces = []
        elif block_type == 0x00000001:
            linktype = struct.unpack("<H", body[:2])[0]
            scale = 1e-6
            offset = 8
            while offset + 4 <= len(body):
                code, length = struct.unpack("<HH", body[offset:offset + 4])
                if code == 0:
                    break
                value = body[offset + 4:offset + 4 + length]
                if code == 9 and value:
                    scale = 1.0 / (2 ** value[0])
                offset += 4 + length + ((4 - length % 4) % 4)
            interfaces.append((linktype, scale))
        elif block_type == 0x00000006 and interfaces:
            iface, _flags, _cap, _orig = struct.unpack("<IIII", body[:16])
            ts_high, ts_low = struct.unpack("<II", body[16:24])
            linktype, scale = interfaces[iface] if iface < len(interfaces) else (LINK_ETHERNET, 1e-6)
            ts = ((ts_high << 32) | ts_low) * scale
            yield ts, linktype, body[24:]


def parse_packet(linktype, data):
    if linktype == LINK_ETHERNET:
        if len(data) < 14:
            return None
        ethertype = struct.unpack(">H", data[12:14])[0]
        offset = 14
        while ethertype == 0x8100 and len(data) >= offset + 4:
            ethertype = struct.unpack(">H", data[offset + 2:offset + 4])[0]
            offset += 4
        data = data[offset:]
    elif linktype in (LINK_SLL, LINK_SLL2):
        data = data[16:] if linktype == LINK_SLL else data[20:]
    if len(data) < 1:
        return None
    version = data[0] >> 4
    if version == 4:
        if len(data) < 20:
            return None
        ihl = (data[0] & 0x0F) * 4
        proto = data[9]
        src = str(ipaddress.IPv4Address(data[12:16]))
        dst = str(ipaddress.IPv4Address(data[16:20]))
        payload = data[ihl:]
    elif version == 6:
        if len(data) < 40:
            return None
        proto = data[6]
        src = str(ipaddress.IPv6Address(data[8:24]))
        dst = str(ipaddress.IPv6Address(data[24:40]))
        payload = data[40:]
    else:
        return None
    sport = dport = 0
    tcp_payload = b""
    flags = 0
    seq = 0
    if proto == 6 and len(payload) >= 20:
        sport, dport, seq = struct.unpack(">HHI", payload[:8])
        offset = (payload[12] >> 4) * 4
        flags = payload[13]
        tcp_payload = payload[offset:]
    elif proto == 17 and len(payload) >= 8:
        sport, dport = struct.unpack(">HH", payload[:4])
        tcp_payload = payload[8:]
    return {"src": src, "dst": dst, "proto": proto, "sport": sport, "dport": dport,
            "payload": tcp_payload, "flags": flags, "seq": seq}


def dns_name(payload):
    if len(payload) < 12:
        return None, None
    qdcount = struct.unpack(">H", payload[4:6])[0]
    if qdcount < 1:
        return None, None
    offset, labels = 12, []
    while offset < len(payload):
        length = payload[offset]
        if length == 0:
            offset += 1
            break
        if length & 0xC0:
            break
        labels.append(payload[offset + 1:offset + 1 + length].decode("ascii", "replace"))
        offset += 1 + length
    qtype = struct.unpack(">H", payload[offset:offset + 2])[0] if offset + 2 <= len(payload) else 0
    return ".".join(labels), qtype


def http_request(payload):
    if not payload or not payload[:8].isupper():
        return None
    head = payload.split(b"\r\n\r\n", 1)[0].decode("latin-1", "replace")
    lines = head.split("\r\n")
    if not lines or " HTTP/" not in lines[0]:
        return None
    method, uri, _ = (lines[0].split(" ") + ["", "", ""])[:3]
    headers = {}
    for line in lines[1:]:
        if ":" in line:
            key, value = line.split(":", 1)
            headers[key.strip().lower()] = value.strip()
    return {"method": method, "uri": uri, "host": headers.get("host", ""),
            "user_agent": headers.get("user-agent", ""),
            "content_type": headers.get("content-type", "")}


def tls_sni(payload):
    if len(payload) < 6 or payload[0] != 0x16:
        return None
    try:
        offset = 5 + 4 + 2 + 32
        session_len = payload[offset]
        offset += 1 + session_len
        cipher_len = struct.unpack(">H", payload[offset:offset + 2])[0]
        offset += 2 + cipher_len
        comp_len = payload[offset]
        offset += 1 + comp_len
        ext_total = struct.unpack(">H", payload[offset:offset + 2])[0]
        offset += 2
        end = offset + ext_total
        while offset + 4 <= end:
            ext_type, ext_len = struct.unpack(">HH", payload[offset:offset + 4])
            offset += 4
            if ext_type == 0:
                name_len = struct.unpack(">H", payload[offset + 3:offset + 5])[0]
                return payload[offset + 5:offset + 5 + name_len].decode("ascii", "replace")
            offset += ext_len
    except (IndexError, struct.error):
        return None
    return None


def entropy(value):
    if not value:
        return 0.0
    counts = defaultdict(int)
    for char in value:
        counts[char] += 1
    return -sum((c / len(value)) * math.log2(c / len(value)) for c in counts.values())


def cmd_info(args):
    packets, first, last, linktypes = 0, None, None, set()
    for ts, linktype, _data in read_pcap(args.file):
        packets += 1
        linktypes.add(linktype)
        first = ts if first is None else min(first, ts)
        last = ts if last is None else max(last, ts)
    print(json.dumps({"file": args.file, "packets": packets,
                      "link_types": sorted(linktypes),
                      "first_ts": first, "last_ts": last,
                      "duration_s": round((last or 0) - (first or 0), 3),
                      "sha256": hashlib.sha256(open(args.file, "rb").read()).hexdigest()}, indent=1))


def cmd_flows(args):
    flows = {}
    for ts, linktype, data in read_pcap(args.file):
        pkt = parse_packet(linktype, data)
        if not pkt:
            continue
        key = (pkt["src"], pkt["sport"], pkt["dst"], pkt["dport"], pkt["proto"])
        flow = flows.setdefault(key, {"packets": 0, "bytes": 0, "first": ts, "last": ts})
        flow["packets"] += 1
        flow["bytes"] += len(data)
        flow["first"] = min(flow["first"], ts)
        flow["last"] = max(flow["last"], ts)
    rows = [{"src": k[0], "sport": k[1], "dst": k[2], "dport": k[3],
             "proto": {6: "tcp", 17: "udp", 1: "icmp"}.get(k[4], str(k[4])),
             **v, "duration_s": round(v["last"] - v["first"], 3)}
            for k, v in flows.items()]
    rows.sort(key=lambda r: r["bytes"], reverse=True)
    print(json.dumps({"flows": rows[:args.top], "total_flows": len(rows)}, indent=1))


def cmd_dns(args):
    queries = defaultdict(lambda: {"count": 0, "qtypes": set(), "lengths": []})
    for ts, linktype, data in read_pcap(args.file):
        pkt = parse_packet(linktype, data)
        if not pkt or pkt["proto"] != 17 or pkt["dport"] != 53:
            continue
        name, qtype = dns_name(pkt["payload"])
        if not name:
            continue
        entry = queries[name]
        entry["count"] += 1
        entry["qtypes"].add(qtype)
        entry["lengths"].append(len(name))
    rows = [{"name": name, "count": v["count"], "qtypes": sorted(v["qtypes"]),
             "max_len": max(v["lengths"]), "entropy": round(entropy(name), 2)}
            for name, v in queries.items()]
    rows.sort(key=lambda r: (-r["entropy"], -r["count"]))
    print(json.dumps({"queries": rows[:args.top], "total": len(rows)}, indent=1))


def cmd_http(args):
    rows = []
    for ts, linktype, data in read_pcap(args.file):
        pkt = parse_packet(linktype, data)
        if not pkt or pkt["proto"] != 6 or pkt["dport"] not in (80, 8080, 8000, 8888):
            continue
        req = http_request(pkt["payload"])
        if req:
            rows.append({"ts": ts, "src": pkt["src"], "dst": pkt["dst"], **req})
    print(json.dumps({"requests": rows[:args.top], "total": len(rows)}, indent=1))


def cmd_tls(args):
    rows = []
    for ts, linktype, data in read_pcap(args.file):
        pkt = parse_packet(linktype, data)
        if not pkt or pkt["proto"] != 6 or pkt["dport"] != 443:
            continue
        sni = tls_sni(pkt["payload"])
        if sni:
            rows.append({"ts": ts, "src": pkt["src"], "dst": pkt["dst"], "sni": sni})
    print(json.dumps({"server_names": rows[:args.top], "total": len(rows)}, indent=1))


def cmd_beacon(args):
    groups = defaultdict(list)
    for ts, linktype, data in read_pcap(args.file):
        pkt = parse_packet(linktype, data)
        if not pkt or pkt["proto"] != 6:
            continue
        if pkt["flags"] & 0x02:  # SYN
            groups[(pkt["src"], pkt["dst"], pkt["dport"])].append(ts)
    rows = []
    for key, times in groups.items():
        if len(times) < args.min_connections:
            continue
        times.sort()
        intervals = [b - a for a, b in zip(times, times[1:]) if b > a]
        if len(intervals) < 2:
            continue
        mean = sum(intervals) / len(intervals)
        variance = sum((x - mean) ** 2 for x in intervals) / (len(intervals) - 1)
        stdev = math.sqrt(variance)
        rows.append({"src": key[0], "dst": key[1], "dport": key[2],
                     "connections": len(times), "mean_s": round(mean, 2),
                     "stdev_s": round(stdev, 2), "cv": round(stdev / mean, 3) if mean else 0,
                     "median_s": round(sorted(intervals)[len(intervals) // 2], 2)})
    rows.sort(key=lambda r: r["cv"])
    print(json.dumps({"beacons": rows[:args.top], "total": len(rows)}, indent=1))


def cmd_carve(args):
    os.makedirs(args.out_dir, exist_ok=True)
    streams = defaultdict(lambda: {"chunks": [], "seen": 0})
    for ts, linktype, data in read_pcap(args.file):
        pkt = parse_packet(linktype, data)
        if not pkt or pkt["proto"] != 6 or not pkt["payload"]:
            continue
        key = (pkt["src"], pkt["sport"], pkt["dst"], pkt["dport"])
        stream = streams[key]
        stream["chunks"].append((pkt["seq"], pkt["payload"]))
        stream["seen"] += len(pkt["payload"])
    manifest = []
    for key, stream in streams.items():
        chunks = sorted(stream["chunks"], key=lambda c: c[0])
        blob = b"".join(c[1] for c in chunks)
        if len(blob) < args.min_size:
            continue
        for magic, kind in MAGIC.items():
            index = blob.find(magic)
            if index < 0:
                continue
            obj = blob[index:index + args.max_size]
            digest = hashlib.sha256(obj).hexdigest()
            name = f"{kind}_{digest[:12]}.bin"
            with open(os.path.join(args.out_dir, name), "wb") as handle:
                handle.write(obj)
            manifest.append({"type": kind, "file": name, "sha256": digest,
                             "size": len(obj), "src": key[0], "sport": key[1],
                             "dst": key[2], "dport": key[3]})
            break
    print(json.dumps({"objects": manifest, "count": len(manifest)}, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="action", required=True)
    for name in ("info", "flows", "dns", "http", "tls", "beacon", "carve"):
        p = sub.add_parser(name)
        p.add_argument("--file", required=True)
        p.add_argument("--top", type=int, default=50)
        p.add_argument("--min-connections", type=int, default=5)
        p.add_argument("--min-size", type=int, default=1024)
        p.add_argument("--max-size", type=int, default=50 * 1024 * 1024)
        p.add_argument("--out")
        p.add_argument("--out-dir", default="./objects")
    args = ap.parse_args()
    {"info": cmd_info, "flows": cmd_flows, "dns": cmd_dns, "http": cmd_http,
     "tls": cmd_tls, "beacon": cmd_beacon, "carve": cmd_carve}[args.action](args)


if __name__ == "__main__":
    main()
