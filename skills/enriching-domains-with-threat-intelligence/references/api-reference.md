# API Reference - Enriching Domains with Threat Intelligence

## Script

```bash
python3 scripts/agent.py --help
```

## Platform commands

```bash
# PAN-OS: add the value to an External Dynamic List and deny it
set external-list blocklist type ip
set external-list blocklist url https://internal.example.com/blocklist.txt
set rulebase security rules deny-blocklist source [ blocklist ]
set rulebase security rules deny-blocklist action deny
commit
```

```bash
# Cloudflare: block at the edge
curl -X POST "https://api.cloudflare.com/client/v4/accounts/$CF_ACCOUNT/firewall/access_rules/rules" \
  -H "Authorization: Bearer $CF_TOKEN" -H "Content-Type: application/json" \
  --data '{"mode":"block","configuration":{"target":"ip","value":"203.0.113.10"},"notes":"INC-1234"}'
```

```bash
# BIND RPZ: sinkhole the domain
cat >> /etc/bind/db.rpz <<'EOF'
evil.example.  IN  CNAME  .
EOF
rndc reload

# Unbound: local block
echo 'local-zone: "evil.example." always_nxdomain' >> /etc/unbound/unbound.conf
unbound-control reload
```

## Verification

| Check | Command |
|---|---|
| Object state | read the platform's own object state |
| Independent test | run the check from a second vantage point |
| Rollback | execute the recorded rollback on a canary |