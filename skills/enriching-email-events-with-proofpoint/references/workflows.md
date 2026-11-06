# Workflows - Enriching Email Events with Proofpoint

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
Skill:      enriching-email-events-with-proofpoint
Incident:   INC-1234
Vendor:     <one of the variants>
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Result:     <success|partial|failed>
Rollback:   <command>
```