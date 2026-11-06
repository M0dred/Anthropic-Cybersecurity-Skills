# Workflows - Hunting Endpoints with Microsoft Defender

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
Skill:      hunting-endpoints-with-microsoft-defender
Incident:   INC-1234
Subject:    endpoints through Microsoft Defender for Endpoint
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```