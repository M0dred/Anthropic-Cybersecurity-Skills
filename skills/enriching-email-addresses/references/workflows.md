# Workflows - Enriching Email Addresses

## Decision sequence

```
1. Validate the value
2. Query the sources
3. Normalize
4. Score confidence
5. Hand off
```

## Record template

```
Skill:      enriching-email-addresses
Incident:   INC-1234
Subject:    email addresses
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```