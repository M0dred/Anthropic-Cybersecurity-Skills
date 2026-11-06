# Workflows - Retrieving File Samples by Path

## Decision sequence

```
1. Authorize and scope
2. Capture volatile data first
3. Capture persistent data
4. Hash and record
5. Transfer and store
```

## Record template

```
Skill:      retrieving-file-samples-by-path
Incident:   INC-1234
Subject:    file samples by path
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```