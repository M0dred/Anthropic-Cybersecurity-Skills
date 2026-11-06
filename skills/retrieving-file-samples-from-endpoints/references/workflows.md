# Workflows - Retrieving File Samples From Endpoints

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
Skill:      retrieving-file-samples-from-endpoints
Incident:   INC-1234
Subject:    file samples from endpoints
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```