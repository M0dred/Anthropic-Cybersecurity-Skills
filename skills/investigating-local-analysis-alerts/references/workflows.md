# Workflows - Investigating Local Analysis Alerts

## Decision sequence

```
1. Scope the entity
2. Collect evidence
3. Build the timeline
4. Test hypotheses
5. Conclude
```

## Record template

```
Skill:      investigating-local-analysis-alerts
Incident:   INC-1234
Subject:    local-analysis alerts
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```