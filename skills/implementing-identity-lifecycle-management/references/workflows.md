# Workflows - Identity Lifecycle Management

## Joiner

```
HR record -> validate -> create account -> set attributes -> baseline groups
-> notify manager -> verify login -> record
```

## Mover

```
HR change -> compute delta -> add new groups -> remove old groups
-> keep role-based groups -> re-certify privileged access -> record
```

## Leaver

```
HR termination -> disable account -> revoke sessions and tokens
-> remove groups -> transfer ownership -> retain -> delete after retention
```

## Drift categories

| Drift | Detection | Action |
|---|---|---|
| Orphan | account not in HR | disable, investigate |
| Missing | HR not in directory | create |
| Attribute | department mismatch | update |
| Group | wrong department group | move |
| Status | active for a leaver | disable now |
| Duplicate | two accounts for one worker | merge, disable the extra |

## Reconciliation report

```json
{
  "run_id": "2026-08-31T10:00Z",
  "target": "ad",
  "counts": {"orphan": 3, "missing": 1, "attribute": 5, "group": 2, "status": 1},
  "actions": [
    {"worker_id": "W-12345", "action": "disable", "reason": "status=terminated"}
  ]
}
```

## Rollback

- Keep the previous attribute values in the plan.
- For a bad bulk change, re-apply the previous snapshot.
- For a disabled account, re-enable only after verifying the HR record.

## Record template

```
Run:        2026-08-31T10:00Z
Target:     Active Directory
HR source:  hr_export.csv (sha256 ...)
Created:    12
Updated:    5
Disabled:   3
Skipped:    1
Failed:     0
Approver:   identity-team@example.com
```
