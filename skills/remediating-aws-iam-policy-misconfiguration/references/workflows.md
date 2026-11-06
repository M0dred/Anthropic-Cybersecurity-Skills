# Workflows - Remediating AWS IAM Policy Misconfiguration

## Decision sequence

```
1. Confirm the finding
2. Plan the change
3. Apply
4. Verify
5. Record
```

## Record template

```
Skill:      remediating-aws-iam-policy-misconfiguration
Incident:   INC-1234
Subject:    an AWS IAM policy misconfiguration
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```