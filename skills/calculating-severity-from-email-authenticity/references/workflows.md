# Workflows - Calculating Severity From Email Authenticity

## Decision sequence

```
1. Collect inputs
2. Normalize
3. Weight and sum
4. Apply modifiers
5. Explain
```

## Record template

```
Skill:      calculating-severity-from-email-authenticity
Incident:   INC-1234
Subject:    severity from email authentication results
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```