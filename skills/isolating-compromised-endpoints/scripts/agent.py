#!/usr/bin/env python3
"""Isolate, verify, and unisolate an endpoint through an EDR control plane.

Providers: crowdstrike, defender, sentinelone, cortexxdr.

Environment:
    CS_TOKEN, CS_BASE_URL          CrowdStrike Falcon
    MDE_TOKEN                      Microsoft Defender for Endpoint
    S1_TOKEN, S1_BASE_URL          SentinelOne
    XDR_TOKEN, XDR_BASE_URL        Cortex XDR

Examples:
    python3 agent.py resolve  --provider crowdstrike --host WEB-01
    python3 agent.py isolate  --provider crowdstrike --host WEB-01 --dry-run
    python3 agent.py verify   --provider crowdstrike --host WEB-01
    python3 agent.py unisolate --provider crowdstrike --host WEB-01
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

TIMEOUT = 45


def env(name, default=""):
    value = os.environ.get(name, default)
    if not value and not default:
        raise SystemExit(f"missing environment variable: {name}")
    return value


def http(method, url, token, body=None, header="Authorization", prefix="Bearer "):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header(header, f"{prefix}{token}")
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return {"status": resp.status, "body": json.loads(resp.read().decode() or "{}")}
    except urllib.error.HTTPError as exc:
        return {"status": exc.code, "error": exc.read().decode()[:500]}
    except Exception as exc:  # noqa: BLE001 - surfaced to the operator
        return {"error": str(exc)}


def resolve(provider, host):
    if provider == "crowdstrike":
        base = env("CS_BASE_URL", "https://api.crowdstrike.com")
        q = urllib.parse.quote(f"hostname:'{host}'")
        r = http("GET", f"{base}/devices/queries/devices/v1?filter={q}", env("CS_TOKEN"))
        ids = (r.get("body") or {}).get("resources", [])
        return ids[0] if ids else None
    if provider == "defender":
        q = urllib.parse.quote(f"computerDnsName eq '{host}'")
        r = http("GET", f"https://api.securitycenter.microsoft.com/api/machines?$filter={q}",
                 env("MDE_TOKEN"))
        items = (r.get("body") or {}).get("value", [])
        return items[0].get("id") if items else None
    if provider == "sentinelone":
        base = env("S1_BASE_URL")
        q = urllib.parse.quote(f'{"computerName__contains":["%s"]}' % host)
        r = http("GET", f"{base}/web/api/v2.1/agents?query={q}", env("S1_TOKEN"),
                 header="Authorization", prefix="ApiToken ")
        items = (r.get("body") or {}).get("data", [])
        return items[0].get("id") if items else None
    if provider == "cortexxdr":
        base = env("XDR_BASE_URL")
        r = http("POST", f"{base}/public_api/v1/endpoints/get_endpoint", env("XDR_TOKEN"),
                 body={"request_data": {"filters": [{"field": "endpoint_name",
                                                     "operator": "contains",
                                                     "value": host}]}})
        items = (r.get("body") or {}).get("reply", {}).get("endpoints", [])
        return items[0].get("endpoint_id") if items else None
    raise SystemExit(f"unknown provider: {provider}")


def act(provider, device_id, action, dry_run):
    if dry_run:
        return {"dry_run": True, "provider": provider, "device_id": device_id, "action": action}
    if provider == "crowdstrike":
        base = env("CS_BASE_URL", "https://api.crowdstrike.com")
        name = "contain" if action == "isolate" else "lift_containment"
        return http("POST", f"{base}/devices/entities/devices-actions/v2?action_name={name}",
                    env("CS_TOKEN"), body={"ids": [device_id]})
    if provider == "defender":
        verb = "isolate" if action == "isolate" else "unisolate"
        body = {"Comment": "containment action"} if verb == "isolate" else {"Comment": "unisolate"}
        if verb == "isolate":
            body["IsolationType"] = "Full"
        return http("POST", f"https://api.securitycenter.microsoft.com/api/machines/{device_id}/{verb}",
                    env("MDE_TOKEN"), body=body)
    if provider == "sentinelone":
        base = env("S1_BASE_URL")
        return http("POST", f"{base}/web/api/v2.1/agents/actions/{action}", env("S1_TOKEN"),
                    body={"filter": {"ids": [device_id]}}, prefix="ApiToken ")
    if provider == "cortexxdr":
        base = env("XDR_BASE_URL")
        return http("POST", f"{base}/public_api/v1/endpoints/{action}", env("XDR_TOKEN"),
                    body={"request_data": {"endpoint_id": device_id}})
    raise SystemExit(f"unknown provider: {provider}")


def status(provider, device_id):
    if provider == "crowdstrike":
        base = env("CS_BASE_URL", "https://api.crowdstrike.com")
        return http("GET", f"{base}/devices/entities/devices/v2?ids={device_id}", env("CS_TOKEN"))
    if provider == "defender":
        return http("GET", f"https://api.securitycenter.microsoft.com/api/machines/{device_id}",
                    env("MDE_TOKEN"))
    if provider == "sentinelone":
        return http("GET", f"{env('S1_BASE_URL')}/web/api/v2.1/agents/{device_id}",
                    env("S1_TOKEN"), prefix="ApiToken ")
    if provider == "cortexxdr":
        return http("POST", f"{env('XDR_BASE_URL')}/public_api/v1/endpoints/get_endpoint",
                    env("XDR_TOKEN"), body={"request_data": {"filters": [
                        {"field": "endpoint_id", "operator": "in", "value": [device_id]}]}})
    raise SystemExit(f"unknown provider: {provider}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("action", choices=["resolve", "isolate", "unisolate", "verify"])
    ap.add_argument("--provider", required=True,
                    choices=["crowdstrike", "defender", "sentinelone", "cortexxdr"])
    ap.add_argument("--host", help="hostname to resolve to a device id")
    ap.add_argument("--device-id", help="skip resolution and use this id")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    device_id = args.device_id or (resolve(args.provider, args.host) if args.host else None)
    if not device_id:
        print(json.dumps({"error": "device not found", "host": args.host}, indent=1))
        sys.exit(2)

    if args.action == "resolve":
        result = {"provider": args.provider, "host": args.host, "device_id": device_id}
    elif args.action == "verify":
        result = {"provider": args.provider, "device_id": device_id,
                  "status": status(args.provider, device_id)}
    else:
        result = {"provider": args.provider, "device_id": device_id,
                  "action": args.action,
                  "result": act(args.provider, device_id, args.action, args.dry_run)}
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
