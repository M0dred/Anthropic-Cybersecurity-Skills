# Workflows - Hunting Threat Indicators Across Siem

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
Skill:      hunting-threat-indicators-across-siem
Incident:   INC-1234
Subject:    threat indicators across SIEM data
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```