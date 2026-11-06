# Workflows - Searching Siem for Failed Logins

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
Skill:      searching-siem-for-failed-logins
Incident:   INC-1234
Subject:    SIEM data for failed logins
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```