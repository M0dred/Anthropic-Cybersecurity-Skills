---
name: extracting-domains-from-urls-and-emails
description: >-
  Extract Domain(s) from URL(s) and/or Email(s). Extracts domains from URLs and email addresses. Use when domains from URLs and email addresses must be parsed for evidence, or when an alert needs confirmation from domains from URLs and email addresses. Keywords: extracting, domains, from, urls, and, emails, analysis, parsing, phishing defense. Do not use for extracting indicators from files - use `extracting-indicators-from-files`.
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

# Extracting Domains From URLs and Emails

## When to Use

- A suspicious artifact, log, or document needs structured analysis.
- An alert requires confirmation from the underlying data.
- A report or hand-off needs reproducible findings rather than prose.

**Do not use** for extracting indicators from files - use `extracting-indicators-from-files`.

## Prerequisites

- The artifact, copied to an evidence directory with a SHA-256 recorded.
- The parser or toolchain for the artifact type, and a known-good sample to validate it.
- The schema the output must satisfy.

## Workflow

### Step 1: Preserve the artifact

Hash it before analysis and work on a copy.

### Step 2: Parse

Use the artifact-specific parser; record the tool and version.

### Step 3: Extract

Pull the fields that matter for the investigation, keeping context for each.

### Step 4: Normalize

Map to the shared schema, de-duplicate, and mark confidence.

### Step 5: Report

Write findings with the evidence path, the commands used, and the limits of the analysis.

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

- The artifact hash in the report matches the source.
- A second run produces the same findings.
- Every finding cites the field or byte range it came from.
- The report states what the analysis could not see.

## Common Pitfalls

- Analyzing the original instead of a copy.
- Claiming content that is encrypted or truncated.
- Dropping context when de-duplicating.
- No tool version, so the result is not reproducible.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
