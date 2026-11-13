# Standards and References - Identity Lifecycle Management

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Protect | PR.AC-01 | Identities and credentials are managed |
| Protect | PR.AC-04 | Access permissions are managed |
| Govern | GV.RR-01 | Roles and responsibilities are defined |

## NIST SP 800-53 Rev. 5

| Control | Title | Relevance |
|---|---|---|
| AC-2 | Account Management | Create, enable, disable, review |
| AC-2(3) | Disable Accounts | Disable after inactivity or termination |
| AC-2(4) | Automated Audit Actions | Log account changes |
| AC-5 | Separation of Duties | Role-based groups |
| IA-4 | Identifier Management | Unique worker ID |
| PS-4 | Personnel Termination | Revoke access on exit |

## ISO/IEC 27001:2022

- A.5.15 Access control
- A.5.16 Identity management
- A.5.18 Access rights
- A.6.1 Screening
- A.7.1 Physical security

## SOX ITGC

- User access provisioning is authorized and timely.
- Termination removes access within the SLA.
- Periodic access reviews are documented.

## MITRE ATT&CK

| Technique | Name | Relevance |
|---|---|---|
| T1078 | Valid Accounts | Orphaned accounts are a target |
| T1098 | Account Manipulation | Group and role changes |
| T1136 | Create Account | Detect unauthorized creation |

## Audit evidence

- HR record for every account.
- Run ID and timestamp for every change.
- Approver for privileged access.
- Drift report after each reconciliation.
