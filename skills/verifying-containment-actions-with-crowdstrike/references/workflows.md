# Workflows - Verifying Containment Actions with CrowdStrike

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
Skill:      verifying-containment-actions-with-crowdstrike
Incident:   INC-1234
Subject:    containment actions in CrowdStrike Falcon
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```