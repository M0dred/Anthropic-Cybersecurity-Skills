---
name: implementing-identity-lifecycle-management
description: >-
  Automates joiner, mover, and leaver flows from an HR system of record into
  Active Directory, Entra ID, and Okta: create and disable accounts, sync group
  membership, assign and revoke application access, and reconcile drift between
  the HR record and the directory. Use when onboarding or offboarding must be
  repeatable, when group membership drifts from the HR source, when an audit
  finds orphaned accounts, or when access must be revoked within a fixed SLA.
  Keywords: identity lifecycle, joiner mover leaver, JML, user provisioning,
  group sync, access revocation, orphaned accounts.
  Do not use for investigating a compromised account - use
  investigating-identity-analytics-alerts. Do not use for rotating secrets -
  use rotating-cloud-credentials.
domain: cybersecurity
subdomain: identity-access-management
tags:
- identity-access-management
- iam
- provisioning
- okta
- active-directory
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- PR.AC-01
- PR.AC-04
- GV.RR-01
mitre_attack:
- T1078
- T1098
- T1136
---

# Implementing Identity Lifecycle Management

## When to Use

- HR is the system of record and accounts must follow hires, moves, and exits.
- Group membership has drifted from the HR record.
- An audit found active accounts for people who left.
- Access must be revoked within a contractual or regulatory SLA.
- A merger or reorganization requires bulk identity changes.

**Do not use** for investigating a suspicious account; that is a detection and
response task. **Do not use** for rotating application secrets; that is a
credential-management task.

## Prerequisites

- An authoritative HR export: worker ID, name, email, department, manager,
  status, and start/end dates.
- Directory APIs: AD (LDAP or PowerShell), Entra ID (Graph), Okta (Users API).
- A mapping from HR attributes to directory attributes and group rules.
- A staging tenant or dry-run mode, because a bad rule can disable the company.

## Workflow

### Step 1: Define the identity model

| HR field | Directory attribute | Rule |
|---|---|---|
| worker_id | employeeID | immutable join key |
| email | userPrincipalName / login | generated if missing |
| department | department | drives group membership |
| manager | manager | drives approval routing |
| status | accountEnabled | `active` → true, else false |
| end_date | accountExpires | set for contractors |

### Step 2: Build the joiner flow

```bash
python3 scripts/agent.py plan --hr hr_export.csv --target ad --out plan.json
python3 scripts/agent.py apply --plan plan.json --dry-run
python3 scripts/agent.py apply --plan plan.json
```

The joiner flow creates the account, sets the attributes, adds the baseline
groups, and sends the welcome message. It must be idempotent: running it twice
must not create a second account.

### Step 3: Build the mover flow

A mover changes department, manager, or location. The flow must:

1. Add the new department groups.
2. Remove the old department groups.
3. Keep the groups that are role-based, not department-based.
4. Re-certify any privileged access separately.

### Step 4: Build the leaver flow

```bash
python3 scripts/agent.py leaver --worker W-12345 --target okta --dry-run
```

Order matters: disable the account, revoke sessions and refresh tokens, remove
group memberships, transfer ownership of files and mailboxes, then delete after
the retention window.

### Step 5: Reconcile drift

```bash
python3 scripts/agent.py reconcile --hr hr_export.csv --target ad --out drift.json
```

Drift categories:

| Drift | Example | Action |
|---|---|---|
| Orphan | account with no HR record | disable, investigate |
| Missing | HR record with no account | create |
| Attribute | department mismatch | update |
| Group | wrong department group | move |
| Status | active account for a leaver | disable now |

### Step 6: Report and audit

Produce a per-run report: created, updated, disabled, skipped, and failed. Keep
it for the audit trail. Alert on any failure in the leaver flow.

## Verification

- A test joiner produces exactly one account with the expected groups.
- A test leaver is disabled and has no active sessions within the SLA.
- A second run of the same plan changes nothing (idempotency).
- The drift report is empty after reconciliation.
- Every change is attributable to an HR record and a run ID.

## Common Pitfalls

- **Deleting instead of disabling.** Deletion loses the audit trail and the
  mailbox; disable first, delete after retention.
- **Matching on email.** Email changes; use the immutable worker ID.
- **Skipping session revocation.** A disabled account with a live token still
  works.
- **Removing role-based groups on a move.** Only department groups should move.
- **No dry run.** A bad rule can disable every account in the tenant.
- **No reconciliation.** Drift accumulates silently between runs.

## References

- `references/api-reference.md` - AD, Entra ID, and Okta APIs
- `references/standards.md` - NIST, ISO 27001, SOX mappings
- `references/workflows.md` - JML flows and drift categories
- `scripts/agent.py` - plan, apply, leaver, reconcile
