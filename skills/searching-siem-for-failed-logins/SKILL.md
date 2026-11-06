---
name: searching-siem-for-failed-logins
description: >-
  Searches for failed logon on a specific user by querying logs from different sources. Searches SIEM, IdP, and VPN logs for failed logins. Use when activity related to SIEM data for failed logins is suspected elsewhere in the estate, or when a hunt needs queries for SIEM data for failed logins. Keywords: searching, siem, for, failed, logins, hunting, detection, soc operations. Do not use for searching sandbox for hash - use `searching-sandbox-for-hash`.
domain: cybersecurity
subdomain: soc-operations
tags:
- soc-operations
- siem
- triage
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- DE.AE-02
- RS.AN-03
- RS.MA-01
mitre_attack:
- T1078
- T1059
- T1566
---

# Searching Siem for Failed Logins

## When to Use

- A threat report or incident suggests SIEM data for failed logins may be present elsewhere.
- A detection needs validation against historical telemetry.
- A proactive hunt is scheduled for the environment.

**Do not use** for searching sandbox for hash - use `searching-sandbox-for-hash`.

## Prerequisites

- Query access to the relevant telemetry: SIEM, EDR, cloud audit logs, or network.
- The data retention window and the field map for each source.
- A hypothesis with a falsifiable test.

## Workflow

### Step 1: State the hypothesis

Write what you expect to see if the activity is present, and what would prove it absent.

### Step 2: Translate to queries

Write one query per telemetry source, with the fields and time window explicit.

### Step 3: Run and triage

Execute, de-duplicate, and rank hits by confidence and asset criticality.

### Step 4: Pivot

For each confirmed hit, pivot on the entity, the technique, and the infrastructure.

### Step 5: Document

Record the queries, the hit counts, the false positives, and the coverage gaps.

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

```spl
index=windows EventCode=4625
| stats count by src_ip, user
| where count > 10
```

```kql
SecurityEvent
| where EventID == 4625
| summarize FailedLogons = count() by IpAddress, Account
| where FailedLogons > 10
```

```sql
SELECT sourceip, username, COUNT(*) AS failures
FROM events
WHERE eventid = 4625
GROUP BY sourceip, username
HAVING COUNT(*) > 10
LAST 24 HOURS
```

## Verification

- The queries are saved and rerunnable.
- Hit counts reconcile with a manual spot check.
- False positives are explained, not silently dropped.
- Coverage gaps are stated explicitly.

## Common Pitfalls

- Hunting without a hypothesis.
- Querying only one telemetry source.
- Ignoring retention limits.
- Reporting hits without triage.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
