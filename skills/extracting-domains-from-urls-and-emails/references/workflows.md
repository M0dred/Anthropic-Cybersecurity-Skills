# Workflows - Extracting Domains From URLs and Emails

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
Skill:      extracting-domains-from-urls-and-emails
Incident:   INC-1234
Subject:    domains from URLs and email addresses
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```