---
name: checking-email-domains-against-blocklists
description: >-
  Accepts an array of domains as a block list, and a list of email addresses. The script then filters out any email address whose domain is in the block list. The filtered list will be returned as an array. Checks DNSBL and internal blocklists. Use when an alert names email domains against blocklists and context is needed before a decision, or when a block or escalation depends on email domains against blocklists reputation. Keywords: checking, email, domains, against, blocklists, enrichment, reputation, phishing defense. Do not use for blocking malicious domains - use `blocking-malicious-domains`.
domain: cybersecurity
subdomain: phishing-defense
tags:
- phishing-defense
- email-security
- incident-response
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- DE.AE-02
- RS.AN-03
- PR.AT-01
mitre_attack:
- T1566.001
- T1566.002
- T1204.002
---

# Checking Email Domains Against Blocklists

## When to Use

- A detection names email domains against blocklists and the analyst needs context before deciding.
- A block or escalation decision needs provenance, not a hunch.
- An incident timeline needs first-seen, last-seen, and ownership data.

**Do not use** for blocking malicious domains - use `blocking-malicious-domains`.

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

```powershell
# Microsoft 365
Get-MessageTrace -SenderAddress attacker@evil.example -StartDate (Get-Date).AddDays(-7)
New-ComplianceSearch -Name "INC-1234" -ExchangeLocation all -ContentMatchQuery 'from:attacker@evil.example'
Start-ComplianceSearch -Identity "INC-1234"
New-ComplianceSearchAction -SearchName "INC-1234" -Purge -PurgeType SoftDelete
```

```bash
# Proofpoint TAP / mail gateway
curl "https://tap.proofpoint.com/v2/siem/messages/blocked?interval=2026-08-30T00:00:00Z/2026-08-31T00:00:00Z" \
  -H "Authorization: Basic $PP_AUTH"
```

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
