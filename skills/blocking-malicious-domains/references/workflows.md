# Workflows - Blocking Malicious Domains

## Decision sequence

```
1. Validate the target
2. Choose the enforcement point
3. Apply the change
4. Verify the effect
5. Record and schedule review
```

## Record template

```
Skill:      blocking-malicious-domains
Incident:   INC-1234
Subject:    malicious domains
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```