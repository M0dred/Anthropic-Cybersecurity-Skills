# Workflows - Assessing Tor Onion URL Reputation

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
Skill:      assessing-tor-onion-url-reputation
Incident:   INC-1234
Subject:    Tor onion URL reputation
Operator:   analyst@example.com
Started:    2026-08-31T10:00Z
Evidence:   <path> (sha256 ...)
Result:     <success|partial|failed>
Rollback:   <command>
Review:     2026-09-30
```