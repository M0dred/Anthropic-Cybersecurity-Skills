# Workflows - Handling False Positive Alerts

## Decision sequence

```
1. Confirm entry criteria
2. Plan
3. Execute
4. Verify
5. Record
```

## Record template

```
Skill:      handling-false-positive-alerts
Incident:   INC-1234
Subject:    false-positive alerts
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```