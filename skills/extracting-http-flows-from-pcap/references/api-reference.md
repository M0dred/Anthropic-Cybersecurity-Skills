# API Reference - Extracting HTTP Flows From PCAP

## Script

```bash
python3 scripts/agent.py --help
```

## Platform commands

```bash
tshark -r capture.pcapng -Y 'dns' -T fields -e dns.qry.name | sort | uniq -c | sort -rn
tshark -r capture.pcapng -Y 'http.request' -T fields -e http.host -e http.request.uri
tshark -r capture.pcapng -Y 'tls.handshake.extensions_server_name' \
  -T fields -e tls.handshake.extensions_server_name
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |