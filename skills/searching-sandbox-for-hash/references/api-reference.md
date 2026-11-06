# API Reference - Searching Sandbox for Hash

## Script

```bash
python3 scripts/agent.py --help
```

## Platform commands

```bash
curl "https://www.virustotal.com/api/v3/files/<sha256>" -H "x-apikey: $VT_API_KEY"
curl -X POST "https://www.virustotal.com/api/v3/files" -H "x-apikey: $VT_API_KEY" -F "file=@sample.bin"
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |