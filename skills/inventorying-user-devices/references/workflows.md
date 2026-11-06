# Workflows - Inventorying User Devices

## Decision sequence

```
1. Enumerate
2. Normalize
3. Reconcile
4. Report
```

## Record template

```
Skill:      inventorying-user-devices
Incident:   INC-1234
Subject:    user devices
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```