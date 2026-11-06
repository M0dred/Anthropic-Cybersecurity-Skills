# Workflows - Hunting Endpoints with CrowdStrike

## Decision sequence

```
1. State the hypothesis
2. Translate to queries
3. Run and triage
4. Pivot
5. Document
```

## Record template

```
Skill:      hunting-endpoints-with-crowdstrike
Incident:   INC-1234
Subject:    endpoints through CrowdStrike Falcon
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```