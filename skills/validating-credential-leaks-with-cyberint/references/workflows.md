# Workflows - Validating Credential Leaks with Cyberint

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
Skill:      validating-credential-leaks-with-cyberint
Incident:   INC-1234
Vendor:     <one of the variants>
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Result:     <success|partial|failed>
Rollback:   <command>
```