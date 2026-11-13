---
name: scanning-domains-with-c2sec
description: >-
  Launches a C2sec scan by domain name and waits for the scan to finish by polling its status in pre-defined intervals. Covers 1 vendor variants: C2sec irisk. Use when this procedure must run through one of these products, or when the vendor-neutral workflow needs the exact API or console steps. Keywords: scanning, domains, with, c2sec, vulnerability management. Do not use for the vendor-neutral procedure - use the matching generic skill.
domain: cybersecurity
subdomain: vulnerability-management
tags:
- vulnerability-management
- cve
- remediation
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- ID.RA-01
- PR.IP-12
- RS.MI-02
mitre_attack:
- T1190
- T1203
- T1068
---

# Scanning Domains with C2sec

## When to Use

- The environment uses one of: C2sec irisk.
- scanning domains with c2sec must be executed through a vendor API or console.
- An incident or audit needs a reproducible, vendor-specific record.

**Do not use** for the vendor-neutral procedure; use the matching generic skill.

## Prerequisites

- Access to the vendor console or API, and a credential with the required scope.
- The object identifier (host, account, resource, or indicator) and its provenance.
- A rollback path and a ticket for the change.

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

## Vendor Variants

### C2SEC-Domain Scan

Source pack: C2sec irisk

Launches a C2sec scan by domain name and waits for the scan to finish by polling its status in pre-defined intervals.

Inputs:

- `DomainName`: The domain name.
- `interval`: How often the polling command should run (in minutes).
- `timeout`: The amount of time to wait before a timeout occurs (in minutes).

## Platform Commands

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
- `references/workflows.md` - decision tree and record template
- `scripts/agent.py` - runnable helper for this procedure
