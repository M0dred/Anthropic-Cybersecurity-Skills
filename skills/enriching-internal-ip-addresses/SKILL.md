---
name: enriching-internal-ip-addresses
description: >-
  Enrich Internal IP addresses using one or more integrations. Resolves internal IPs to assets via DHCP, DNS, and CMDB. Use when an alert names internal ip addresses and context is needed before a decision, or when a block or escalation depends on internal ip addresses reputation. Keywords: enriching, internal, addresses, enrichment, reputation, threat intelligence. Do not use for enriching external ip addresses - use `enriching-external-ip-addresses`.
domain: cybersecurity
subdomain: threat-intelligence
tags:
- threat-intelligence
- ioc
- enrichment
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- ID.RA-01
- DE.AE-02
- RS.AN-03
mitre_attack:
- T1588.001
- T1071
- T1595
---

# Enriching Internal IP Addresses

## When to Use

- A detection names internal ip addresses and the analyst needs context before deciding.
- A block or escalation decision needs provenance, not a hunch.
- An incident timeline needs first-seen, last-seen, and ownership data.

**Do not use** for enriching external ip addresses - use `enriching-external-ip-addresses`.

## Prerequisites

- API access to the sources you enable, and a cache directory.
- An allowlist of known-good values so shared infrastructure is not misread.
- The source's rate limits, so a batch does not exhaust the quota.

## Workflow

### Step 1: Validate the value

Reject private, reserved, malformed, or out-of-scope entries before any API call.

### Step 2: Query the sources

Run the enabled sources in parallel where possible, and record failures as failures rather than as clean results.

### Step 3: Normalize

Map each source's fields into one schema with the source name attached to every value.

### Step 4: Score confidence

Combine independent signals with explicit weights; cap the score when fewer than two sources respond.

### Step 5: Hand off

Attach the record to the incident and pass the decision to the containment or escalation skill.

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

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

- Every enabled source appears in either the success or failure list.
- The confidence score is reproducible from the component signals.
- Cached values carry the original lookup timestamp.
- No credentials appear in the output.

## Common Pitfalls

- Treating no reports as clean.
- Ignoring shared infrastructure.
- Burning the daily quota on a /24.
- Using stale reputation without recording the lookup time.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
