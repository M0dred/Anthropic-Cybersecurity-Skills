# Workflows - Analyzing PCAP Files

## Triage sequence

```
1. Verify provenance (hash, capture point, window)
2. Inventory protocols and top talkers
3. Extract DNS, HTTP, TLS artifacts
4. Rank flows by bytes and by connection count
5. Detect beaconing
6. Carve objects and hash them
7. Correlate with threat intelligence and host logs
8. Write the timeline and findings
```

## What each view answers

| View | Question |
|---|---|
| Flows | Who talked to whom, how much, how long |
| DNS | What names were resolved, how often, how long |
| HTTP | What was requested, with which Host and User-Agent |
| TLS | What server name was contacted, with which certificate |
| Beacon | Is the timing periodic, and how regular |
| Carve | What files crossed the wire |

## Beaconing math

For connection timestamps `t1..tn`, intervals `d_i = t_{i+1} - t_i`:

```
mean      = sum(d_i) / (n-1)
variance  = sum((d_i - mean)^2) / (n-2)
stdev     = sqrt(variance)
CV        = stdev / mean
```

| CV | Interpretation |
|---|---|
| < 0.10 | machine-timed beacon |
| 0.10 - 0.25 | beacon with light jitter |
| 0.25 - 0.50 | scheduled task or polling |
| > 0.50 | human or highly jittered traffic |

Also report the median interval and a histogram; malware often jitters by a
fixed percentage, which keeps the CV moderate but the histogram narrow.

## DNS tunneling signals

| Signal | Threshold |
|---|---|
| Query name length | > 100 characters |
| Label length | > 40 characters |
| Shannon entropy of the label | > 3.5 bits/char |
| Query type | TXT, NULL, CNAME |
| Unique subdomains per parent | > 100 in an hour |
| Response size | consistently large TXT |

## HTTP exfiltration signals

- POST to a rare destination with a large body.
- `Content-Type: multipart/form-data` to a non-business host.
- Unusual User-Agent or missing User-Agent.
- URI path with high-entropy segments.

## Carving rules

- Reassemble by TCP sequence number, not arrival order.
- Detect magic bytes: `MZ` (PE), `%PDF`, `PK\x03\x04` (ZIP/Office), `\x7fELF`.
- Cap object size (default 50 MB) and count.
- Hash every object and record the stream tuple and byte range.

## Report template

```
Capture:      capture.pcapng (sha256 ...)
Window:       2026-08-31T09:55Z - 10:25Z
Point:        span port on core switch
Top flows:    10.0.1.5:51544 -> 203.0.113.10:443, 1.2 MB, 30 min
DNS:          a1b2c3.evil.example (TXT, 62 chars, entropy 4.1)
TLS SNI:      cdn.evil.example
Beacon:       mean 60.2s, stdev 1.8s, CV 0.03, 30 connections
Objects:      invoice.exe (sha256 ...), 1.1 MB
Assessment:   C2 beacon with DNS fallback
```
