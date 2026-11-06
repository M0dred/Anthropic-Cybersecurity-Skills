#!/usr/bin/env python3
"""Score incident severity from six weighted factors plus modifiers.

Subcommands:
    score    Compute the score, rating, and rationale for one incident.
    explain  Print the per-factor breakdown for one incident.
    batch    Score a JSON list of incidents.

Examples:
    python3 agent.py score   --input incident.json --out severity.json
    python3 agent.py explain --input incident.json
    python3 agent.py batch   --input incidents.json --out severities.json
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone

WEIGHTS = {"asset_criticality": 0.25, "indicator_verdict": 0.20,
           "technique_impact": 0.20, "data_sensitivity": 0.15,
           "blast_radius": 0.10, "confidence": 0.10}

ASSET = {"low": 0.2, "medium": 0.5, "high": 0.8, "crown-jewel": 1.0}
VERDICT = {"benign": 0.0, "unknown": 0.3, "suspicious": 0.6, "malicious": 1.0}
SENSITIVITY = {"public": 0.0, "internal": 0.3, "confidential": 0.7, "regulated": 1.0}
BLAST = {"host": 0.2, "user": 0.3, "business-unit": 0.7, "cross-tenant": 1.0}

TECHNIQUE_IMPACT = {
    "T1486": 1.0, "T1490": 1.0, "T1485": 1.0,
    "T1003": 0.9, "T1041": 0.9, "T1048": 0.9, "T1567": 0.9,
    "T1078": 0.8, "T1068": 0.8, "T1548": 0.8,
    "T1059": 0.7, "T1021": 0.7, "T1562": 0.7, "T1070": 0.7, "T1204": 0.7,
    "T1566": 0.6, "T1071": 0.6, "T1005": 0.6, "T1114": 0.6,
    "T1087": 0.4, "T1018": 0.4,
}
BANDS = [(0.85, "Critical"), (0.65, "High"), (0.40, "Medium"), (0.0, "Low")]
ORDER = ["Low", "Medium", "High", "Critical"]


def technique_impact(techniques):
    if not techniques:
        return 0.5, "none"
    best, name = 0.5, "default"
    for technique in techniques:
        base = technique.split(".")[0].upper()
        value = TECHNIQUE_IMPACT.get(base, 0.5)
        if value > best:
            best, name = value, base
    return best, name


def band(score):
    for threshold, rating in BANDS:
        if score >= threshold:
            return rating
    return "Low"


def shift(rating, steps):
    index = max(0, min(len(ORDER) - 1, ORDER.index(rating) + steps))
    return ORDER[index]


def score_incident(incident):
    asset = ASSET.get(str(incident.get("asset_criticality", "medium")).lower(), 0.5)
    verdict = VERDICT.get(str(incident.get("indicator_verdict", "unknown")).lower(), 0.3)
    impact, impact_source = technique_impact(incident.get("techniques") or [])
    sensitivity = SENSITIVITY.get(str(incident.get("data_sensitivity", "internal")).lower(), 0.3)
    blast = BLAST.get(str(incident.get("blast_radius", "host")).lower(), 0.2)
    confidence = max(0.0, min(1.0, float(incident.get("confidence", 0.5))))

    factors = [
        ("asset_criticality", incident.get("asset_criticality", "medium"), asset),
        ("indicator_verdict", incident.get("indicator_verdict", "unknown"), verdict),
        ("technique_impact", impact_source, impact),
        ("data_sensitivity", incident.get("data_sensitivity", "internal"), sensitivity),
        ("blast_radius", incident.get("blast_radius", "host"), blast),
        ("confidence", confidence, confidence),
    ]
    total = 0.0
    breakdown = []
    for name, value, normalized in factors:
        contribution = round(normalized * WEIGHTS[name], 4)
        total += contribution
        breakdown.append({"name": name, "value": value, "normalized": normalized,
                          "weight": WEIGHTS[name], "contribution": contribution})
    total = round(min(total, 1.0), 4)

    rating = band(total)
    modifiers = []
    if incident.get("active", True):
        rating = shift(rating, 1)
        modifiers.append("active: +1 band")
    if not incident.get("business_hours", True):
        rating = shift(rating, 1)
        modifiers.append("off-hours: +1 band")
    if str(incident.get("data_sensitivity", "")).lower() == "regulated":
        if ORDER.index(rating) < ORDER.index("High"):
            rating = "High"
        modifiers.append("regulated data: floor at High")
    if incident.get("repeat_30d"):
        rating = shift(rating, 1)
        modifiers.append("repeat within 30 days: +1 band")
    if int(incident.get("corroborating_sources", 2)) < 2:
        if ORDER.index(rating) > ORDER.index("Medium"):
            rating = "Medium"
        modifiers.append("fewer than two sources: cap at Medium")
    if incident.get("contained"):
        rating = shift(rating, -1)
        modifiers.append("contained: -1 band")

    rationale = (f"{rating}: weighted score {total:.2f} from "
                 f"{incident.get('asset_criticality', 'medium')} asset, "
                 f"{incident.get('indicator_verdict', 'unknown')} verdict, "
                 f"{impact_source} impact, "
                 f"{incident.get('data_sensitivity', 'internal')} data, "
                 f"{incident.get('blast_radius', 'host')} blast radius, "
                 f"confidence {confidence:.2f}"
                 + (f"; modifiers: {', '.join(modifiers)}" if modifiers else ""))
    return {"incident_id": incident.get("incident_id", ""), "score": total,
            "rating": rating, "factors": breakdown, "modifiers": modifiers,
            "rationale": rationale,
            "calculated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")}


def load(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="action", required=True)
    for name in ("score", "explain", "batch"):
        p = sub.add_parser(name)
        p.add_argument("--input", required=True)
        p.add_argument("--out")
    args = ap.parse_args()

    data = load(args.input)
    if args.action == "batch":
        if not isinstance(data, list):
            raise SystemExit("batch expects a JSON list")
        results = [score_incident(item) for item in data]
        text = json.dumps(results, indent=1)
    else:
        result = score_incident(data)
        text = json.dumps(result, indent=1)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as handle:
            handle.write(text)
        print(json.dumps({"written": args.out}, indent=1))
    else:
        print(text)


if __name__ == "__main__":
    main()
