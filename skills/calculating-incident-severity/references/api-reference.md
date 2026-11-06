# API Reference - Calculating Incident Severity

## Input schema

```json
{
  "incident_id": "INC-1234",
  "asset_criticality": "low|medium|high|crown-jewel",
  "indicator_verdict": "benign|unknown|suspicious|malicious",
  "techniques": ["T1486", "T1078"],
  "data_sensitivity": "public|internal|confidential|regulated",
  "blast_radius": "host|user|business-unit|cross-tenant",
  "confidence": 0.0,
  "business_hours": true,
  "active": true,
  "repeat_30d": false,
  "corroborating_sources": 2
}
```

## Weights

| Factor | Weight |
|---|---|
| asset_criticality | 0.25 |
| indicator_verdict | 0.20 |
| technique_impact | 0.20 |
| data_sensitivity | 0.15 |
| blast_radius | 0.10 |
| confidence | 0.10 |

## Normalized values

| Field | Value | Score |
|---|---|---|
| asset_criticality | low | 0.2 |
| | medium | 0.5 |
| | high | 0.8 |
| | crown-jewel | 1.0 |
| indicator_verdict | benign | 0.0 |
| | unknown | 0.3 |
| | suspicious | 0.6 |
| | malicious | 1.0 |
| data_sensitivity | public | 0.0 |
| | internal | 0.3 |
| | confidential | 0.7 |
| | regulated | 1.0 |
| blast_radius | host | 0.2 |
| | user | 0.3 |
| | business-unit | 0.7 |
| | cross-tenant | 1.0 |
| confidence | 0.0-1.0 | as given |

## Technique impact

| Technique | Impact | Name |
|---|---|---|
| T1486 | 1.0 | Data Encrypted for Impact |
| T1490 | 1.0 | Inhibit System Recovery |
| T1485 | 1.0 | Data Destruction |
| T1003 | 0.9 | OS Credential Dumping |
| T1041 | 0.9 | Exfiltration Over C2 Channel |
| T1078 | 0.8 | Valid Accounts |
| T1059 | 0.7 | Command and Scripting Interpreter |
| T1021 | 0.7 | Remote Services |
| T1562 | 0.7 | Impair Defenses |
| T1566 | 0.6 | Phishing |
| T1071 | 0.6 | Application Layer Protocol |
| default | 0.5 | unknown technique |

## Output schema

```json
{
  "incident_id": "INC-1234",
  "score": 0.78,
  "rating": "High",
  "factors": [
    {"name": "asset_criticality", "value": "high", "normalized": 0.8,
     "weight": 0.25, "contribution": 0.20},
    {"name": "indicator_verdict", "value": "malicious", "normalized": 1.0,
     "weight": 0.20, "contribution": 0.20}
  ],
  "modifiers": ["active: +1 band"],
  "rationale": "High because ...",
  "calculated_at": "2026-08-31T10:00:00Z"
}
```

## Rating bands

| Score | Rating |
|---|---|
| >= 0.85 | Critical |
| 0.65 - 0.84 | High |
| 0.40 - 0.64 | Medium |
| < 0.40 | Low |

## CLI

```bash
python3 scripts/agent.py score   --input incident.json --out severity.json
python3 scripts/agent.py explain --input incident.json
python3 scripts/agent.py batch   --input incidents.json --out severities.json
```

## Recalculation

Every run writes `calculated_at`. Keep a list of runs per incident:

```json
{"incident_id": "INC-1234",
 "history": [
   {"at": "2026-08-31T09:00:00Z", "score": 0.78, "rating": "High"},
   {"at": "2026-08-31T09:30:00Z", "score": 0.55, "rating": "Medium", "reason": "contained"}
 ]}
```
