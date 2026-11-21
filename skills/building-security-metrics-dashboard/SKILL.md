---
name: building-security-metrics-dashboard
description: >-
  Builds a security metrics dashboard for executives and SOC managers: mean time
  to detect (MTTD), mean time to respond (MTTR), coverage by MITRE ATT&CK tactic,
  vulnerability remediation SLA compliance, phishing simulation click rates, and
  board-level risk indicators. Use when presenting security posture to leadership,
  when justifying budget with data, when tracking SOC performance, or when
  building a security program from scratch. Keywords: security metrics, KPI,
  dashboard, MTTD, MTTR, board reporting, risk quantification, security posture.
  Do not use for real-time alerting - use triaging-security-alerts-in-splunk.
  Do not use for compliance audit evidence - use
  achieving-cmmc-level-2-compliance.
domain: cybersecurity
subdomain: soc-operations
tags:
- security-metrics
- kpi
- dashboard
- reporting
- risk-management
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- GV.ME-01
- GV.OV-02
- ID.RA-01
mitre_attack:
- T1078
- T1059
- T1566
---

# Building Security Metrics Dashboard

## When to Use

- Presenting security posture to executives or the board.
- Justifying security budget with data.
- Tracking SOC team performance.
- Building a security program from scratch.
- Measuring the effectiveness of security investments.

**Do not use** for real-time alerting; that is SIEM/EDR territory. **Do not use**
for compliance audit evidence; that is a GRC function.

## Prerequisites

- Data sources: SIEM, EDR, vulnerability scanner, ticketing system.
- A defined reporting period: weekly, monthly, quarterly.
- Stakeholder agreement on which metrics matter.
- A dashboard tool: Grafana, Tableau, Power BI, or custom.

## Workflow

### Step 1: Select metrics that matter

| Category | Metric | Formula |
|---|---|---|
| Detection | MTTD | mean(alert_time - event_time) |
| Response | MTTR | mean(resolve_time - alert_time) |
| Coverage | ATT&CK coverage | tactics_with_detections / 14 |
| Vulnerability | SLA compliance | remediated_in_sla / total |
| Phishing | Click rate | clicks / delivered_emails |
| Access | Orphaned accounts | active_accounts_without_owner |
| Incident | Repeat incidents | incidents_with_same_root_cause / total |

### Step 2: Collect data from sources

```bash
# Splunk: MTTD and MTTR
index=incidents
| stats avg(alert_time - event_time) as MTTD avg(resolve_time - alert_time) as MTTR by severity

# Nessus: SLA compliance
curl -sS "https://nessus:8834/scans" -H "X-ApiKeys: accessKey=$ACCESS;secretKey=$SECRET" \
  | jq '.scans[] | {name, status, completion_time}'
```

### Step 3: Build the dashboard

| Audience | Metrics | Refresh |
|---|---|---|
| Board | Risk score, top 5 threats, budget utilization | Quarterly |
| CISO | MTTD/MTTR trend, coverage, SLA compliance | Monthly |
| SOC Manager | Alert volume, false positive rate, analyst workload | Weekly |
| Analyst | Open incidents, queue depth, SLA breaches | Real-time |

### Step 4: Automate data collection

```bash
# Pull metrics weekly
python3 scripts/agent.py collect --siem splunk --days 7 --format json --out metrics_weekly.json
python3 scripts/agent.py render --input metrics_weekly.json --format grafana --out dashboard.json
```

### Step 5: Review and iterate

- Monthly: review metric definitions with stakeholders.
- Quarterly: retire metrics that do not drive decisions.
- Annually: benchmark against industry peers (e.g., Ponemon, SANS).

## Verification

- MTTD/MTTR are calculated consistently across all severity levels.
- Coverage maps to at least 12 of 14 ATT&CK tactics.
- SLA compliance is measured against documented targets.
- Dashboard refreshes automatically without manual intervention.
- Stakeholders can explain each metric in one sentence.

## Common Pitfalls

- **Vanity metrics.** "Number of alerts" without context is meaningless.
- **No baseline.** Metrics without a starting point cannot show improvement.
- **Too many metrics.** 5 metrics that drive decisions beat 50 that do not.
- **Manual collection.** Automate or the dashboard will be abandoned.
- **No action loop.** Every metric should trigger a decision or action.

## References

- `references/api-reference.md` - data collection queries by platform
- `references/standards.md` - NIST CSF, ISO 27004 mappings
- `references/workflows.md` - metric selection and review cadence
- `scripts/agent.py` - metrics collection and dashboard rendering helper
