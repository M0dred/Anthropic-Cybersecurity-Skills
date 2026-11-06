# Workflows - Preprocessing Email for Phishing Triage

## Decision sequence

```
1. Preserve the artifact
2. Parse
3. Extract
4. Normalize
5. Report
```

## Record template

```
Skill:      preprocessing-email-for-phishing-triage
Incident:   INC-1234
Subject:    email for phishing triage
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```