# Workflows - Analyzing macOS Artifacts with Osxcollector

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
Skill:      analyzing-macos-artifacts-with-osxcollector
Incident:   INC-1234
Subject:    macOS artifacts with osxcollector
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```