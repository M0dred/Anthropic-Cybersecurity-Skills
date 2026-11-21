---
name: securing-slack-workspace-against-data-exfiltration
description: >-
  Secures a Slack workspace against data exfiltration by auditing external file
  sharing, detecting anomalous download patterns, restricting guest access,
  monitoring API token usage, and enforcing data loss prevention policies.
  Covers Slack Enterprise Grid and standard workspaces. Use when sensitive data
  appears in public channels, when departing employees may exfiltrate data, when
  guest access needs review, or when building a SaaS security program. Keywords:
  Slack security, SaaS security, data exfiltration, DLP, workspace audit,
  external sharing, API token security.
  Do not use for Microsoft Teams security - use
  deleting-malicious-emails-in-m365. Do not use for general SaaS security
  assessment - use implementing-saas-security-posture-management.
domain: cybersecurity
subdomain: cloud-security
tags:
- saas-security
- slack
- dlp
- data-exfiltration
- insider-threat
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- PR.DS-01
- DE.CM-01
- RS.MI-01
mitre_attack:
- T1567
- T1052
- T1078
---

# Securing Slack Workspace Against Data Exfiltration

## When to Use

- Sensitive data (credentials, customer data, source code) appears in channels.
- A departing employee may have exfiltrated workspace data.
- Guest or external access needs review and restriction.
- API tokens show unusual usage patterns.
- Building a SaaS security program.

**Do not use** for Microsoft Teams security; that is a different platform with
different controls. **Do not use** for general SaaS posture assessment; use a
CASB or SSPM tool.

## Prerequisites

- Slack workspace admin or owner role.
- Slack Enterprise Grid (for org-level policies) or Pro/Business+.
- Access to Slack Audit Logs API (Enterprise Grid).
- A list of sensitive data patterns: API keys, customer PII, credentials.

## Workflow

### Step 1: Audit external sharing

```bash
# List all external workspaces with shared channels
curl -sS "https://slack.com/api/admin.conversations.list?limit=200" \
  -H "Authorization: Bearer $SLACK_ADMIN_TOKEN" | jq '.conversations[] | select(.is_external) | {name, team_id}'

# List all guest users
curl -sS "https://slack.com/api/admin.users.list?limit=200" \
  -H "Authorization: Bearer $SLACK_ADMIN_TOKEN" | jq '.users[] | select(.is_restricted or .is_ultra_restricted) | {name, email, teams}'
```

### Step 2: Restrict external sharing

```bash
# Disable file sharing with external workspaces
curl -sS -X POST "https://slack.com/api/admin.teams.settings.setInfo" \
  -H "Authorization: Bearer $SLACK_ADMIN_TOKEN" \
  -d 'discoverability="closed"'
```

Set **External sharing** to "Only share files with workspaces in the same org"
in Workspace Settings → Permissions.

### Step 3: Audit API tokens

```bash
# List all tokens (requires admin scope)
curl -sS "https://slack.com/api/team.billableInfo" -H "Authorization: Bearer $SLACK_ADMIN_TOKEN"
# Revoke suspicious tokens
curl -sS -X POST "https://slack.com/api/auth.revoke" \
  -H "Authorization: Bearer $SLACK_ADMIN_TOKEN" -d "token=<token>"
```

### Step 4: Monitor for exfiltration patterns

| Pattern | Detection |
|---|---|
| Mass download | User downloads >100 files in 1 hour |
| Bulk export | Admin exports workspace data without change ticket |
| Public channel exposure | Sensitive keywords in public channels |
| External upload | Files uploaded to external workspaces |
| API scraping | Token makes >10,000 API calls/hour |

Use the Audit Logs API:

```bash
curl -sS "https://api.slack.com/audit/v1/logs?limit=200&oldest=$(date -d '24 hours ago' +%s)" \
  -H "Authorization: Bearer $SLACK_AUDIT_TOKEN" | jq '.entries[] | select(.action=="file_downloaded" or .action=="user_session_reset")'
```

### Step 5: Enforce DLP

- Enable Slack's built-in DLP: Settings → Security → Data loss prevention.
- Integrate a CASB (Netskope, McAfee, Microsoft Defender for Cloud Apps).
- Block message forwarding for channels with sensitive data.
- Set retention policies: delete messages with credentials after 30 days.

## Verification

- No external workspaces have active shared channels without business justification.
- Guest users have expiry dates and restricted channel access.
- API tokens are scoped to minimum required permissions.
- Audit logs show no mass download events in the last 30 days.
- DLP policies trigger on test sensitive data within 5 minutes.

## Common Pitfalls

- **Ignoring private channels.** Most exfiltration happens in private channels.
- **No token inventory.** API tokens accumulate and are forgotten.
- **Overly broad guest access.** Guests should be channel-restricted and time-bound.
- **No retention policy.** Sensitive data persists indefinitely without deletion.

## References

- `references/api-reference.md` - Slack API commands for audit and control
- `references/standards.md` - NIST, ATT&CK mappings
- `references/workflows.md` - audit and enforcement flow
- `scripts/agent.py` - Slack audit and exfiltration detection helper
