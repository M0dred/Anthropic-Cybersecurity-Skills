#!/usr/bin/env python3
"""Scoring runtime: severity model and CVSS base score."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone

CONFIG = {
 "skill": "calculating-severity-from-critical-assets",
 "description": "calculating severity from critical assets",
 "model": "severity"
}
WEIGHTS = {"asset": 0.25, "verdict": 0.20, "impact": 0.20,
           "sensitivity": 0.15, "blast": 0.10, "confidence": 0.10}
ASSET = {"low": 0.2, "medium": 0.5, "high": 0.8, "crown-jewel": 1.0}
VERDICT = {"benign": 0.0, "unknown": 0.3, "suspicious": 0.6, "malicious": 1.0}
SENS = {"public": 0.0, "internal": 0.3, "confidential": 0.7, "regulated": 1.0}
BLAST = {"host": 0.2, "user": 0.3, "business-unit": 0.7, "cross-tenant": 1.0}
IMPACT = {"T1486": 1.0, "T1490": 1.0, "T1485": 1.0, "T1003": 0.9, "T1041": 0.9,
          "T1078": 0.8, "T1059": 0.7, "T1021": 0.7, "T1562": 0.7, "T1566": 0.6,
          "T1071": 0.6, "T1087": 0.4}
BANDS = [(0.85, "Critical"), (0.65, "High"), (0.40, "Medium"), (0.0, "Low")]
ORDER = ["Low", "Medium", "High", "Critical"]


def severity(data):
    asset = ASSET.get(str(data.get("asset_criticality", "medium")).lower(), 0.5)
    verdict = VERDICT.get(str(data.get("indicator_verdict", "unknown")).lower(), 0.3)
    techniques = data.get("techniques") or []
    impact = max([IMPACT.get(t.split(".")[0].upper(), 0.5) for t in techniques] or [0.5])
    sens = SENS.get(str(data.get("data_sensitivity", "internal")).lower(), 0.3)
    blast = BLAST.get(str(data.get("blast_radius", "host")).lower(), 0.2)
    conf = max(0.0, min(1.0, float(data.get("confidence", 0.5))))
    factors = {"asset": asset, "verdict": verdict, "impact": impact,
               "sensitivity": sens, "blast": blast, "confidence": conf}
    total = round(sum(factors[k] * WEIGHTS[k] for k in WEIGHTS), 4)
    rating = next(r for t, r in BANDS if total >= t)
    if data.get("active", True):
        rating = ORDER[min(len(ORDER) - 1, ORDER.index(rating) + 1)]
    if data.get("contained"):
        rating = ORDER[max(0, ORDER.index(rating) - 1)]
    return {"score": total, "rating": rating,
            "factors": {k: {"value": v, "weight": WEIGHTS[k],
                            "contribution": round(v * WEIGHTS[k], 4)}
                        for k, v in factors.items()}}


def cvss(data):
    av = {"network": 0.85, "adjacent": 0.62, "local": 0.55, "physical": 0.2}
    ac = {"low": 0.77, "high": 0.44}
    pr = {"none": 0.85, "low": 0.62, "high": 0.27}
    ui = {"none": 0.85, "required": 0.62}
    cia = {"high": 0.56, "low": 0.22, "none": 0.0}
    scope_changed = str(data.get("scope", "unchanged")).lower() == "changed"
    exploit = 8.22 * av[data.get("attack_vector", "network")] * ac[data.get("attack_complexity", "low")] \
        * pr[data.get("privileges_required", "none")] * ui[data.get("user_interaction", "none")]
    iss = 1 - ((1 - cia[data.get("confidentiality", "high")]) *
               (1 - cia[data.get("integrity", "high")]) *
               (1 - cia[data.get("availability", "high")]))
    if scope_changed:
        impact = 7.52 * (iss - 0.029) - 3.25 * (iss - 0.02) ** 15
    else:
        impact = 6.42 * iss
    score = 0.0 if impact <= 0 else min(10.0, round(1.08 * (impact + exploit), 1) if scope_changed
                                        else round(min(impact + exploit, 10.0), 1))
    return {"base_score": score,
            "severity": "Critical" if score >= 9 else "High" if score >= 7 else
                        "Medium" if score >= 4 else "Low" if score > 0 else "None"}


def main(config=None):
    cfg = config or CONFIG
    ap = argparse.ArgumentParser(description=cfg.get("description", "scoring"))
    ap.add_argument("--model", default=cfg.get("model", "severity"),
                    choices=["severity", "cvss"])
    ap.add_argument("--input", required=True)
    ap.add_argument("--out")
    args = ap.parse_args()
    data = json.load(open(args.input))
    result = severity(data) if args.model == "severity" else cvss(data)
    result.update({"skill": cfg.get("skill", ""), "model": args.model,
                   "calculated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})
    text = json.dumps(result, indent=1)
    if args.out:
        open(args.out, "w", encoding="utf-8").write(text)
        print(json.dumps({"written": args.out}, indent=1))
    else:
        print(text)


if __name__ == "__main__":
    main()
