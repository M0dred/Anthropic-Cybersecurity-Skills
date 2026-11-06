# API Reference - Isolating Compromised Endpoints

## CrowdStrike Falcon

```bash
# Find the device id
curl "https://api.crowdstrike.com/devices/queries/devices/v1?filter=hostname:'WEB-01'" \
  -H "Authorization: Bearer $CS_TOKEN"

# Contain
curl -X POST "https://api.crowdstrike.com/devices/entities/devices-actions/v2?action_name=contain" \
  -H "Authorization: Bearer $CS_TOKEN" -H "Content-Type: application/json" \
  -d '{"ids":["<device_id>"]}'

# Lift containment
curl -X POST "https://api.crowdstrike.com/devices/entities/devices-actions/v2?action_name=lift_containment" \
  -H "Authorization: Bearer $CS_TOKEN" -H "Content-Type: application/json" \
  -d '{"ids":["<device_id>"]}'

# Status
curl "https://api.crowdstrike.com/devices/entities/devices/v2?ids=<device_id>" \
  -H "Authorization: Bearer $CS_TOKEN" | jq '.resources[0].status'
```

OAuth2 token: `POST https://api.crowdstrike.com/oauth2/token` with
`client_id`/`client_secret` form fields; tokens last 30 minutes.

## Microsoft Defender for Endpoint

```bash
# Device id
curl "https://api.securitycenter.microsoft.com/api/machines?$filter=computerDnsName eq 'WEB-01'" \
  -H "Authorization: Bearer $MDE_TOKEN"

# Isolate (Full or Selective)
curl -X POST "https://api.securitycenter.microsoft.com/api/machines/<id>/isolate" \
  -H "Authorization: Bearer $MDE_TOKEN" -H "Content-Type: application/json" \
  -d '{"Comment":"INC-1234","IsolationType":"Full"}'

# Unisolate
curl -X POST "https://api.securitycenter.microsoft.com/api/machines/<id>/unisolate" \
  -H "Authorization: Bearer $MDE_TOKEN" -H "Content-Type: application/json" \
  -d '{"Comment":"remediated"}'

# Live response session (requires IsolationType Selective or Full)
curl -X POST "https://api.securitycenter.microsoft.com/api/machines/<id>/runliveresponse" \
  -H "Authorization: Bearer $MDE_TOKEN" -H "Content-Type: application/json" \
  -d '{"Commands":[{"type":"RunScript","params":[{"key":"ScriptName","value":"collect.ps1"}]}]}'
```

## SentinelOne

```bash
curl -X POST "https://<tenant>.sentinelone.net/web/api/v2.1/agents/actions/isolate" \
  -H "Authorization: ApiToken $S1_TOKEN" -H "Content-Type: application/json" \
  -d '{"filter":{"ids":["<agent_id>"]}}'

curl -X POST "https://<tenant>.sentinelone.net/web/api/v2.1/agents/actions/unisolate" \
  -H "Authorization: ApiToken $S1_TOKEN" -H "Content-Type: application/json" \
  -d '{"filter":{"ids":["<agent_id>"]}}'
```

## Cortex XDR

```bash
curl -X POST "https://api-<tenant>.xdr.<region>.paloaltonetworks.com/public_api/v1/endpoints/isolate" \
  -H "Authorization: $XDR_TOKEN" -H "Content-Type: application/json" \
  -d '{"request_data":{"endpoint_id":"<id>"}}'

curl -X POST "https://api-<tenant>.xdr.<region>.paloaltonetworks.com/public_api/v1/endpoints/unisolate" \
  -H "Authorization: $XDR_TOKEN" -H "Content-Type: application/json" \
  -d '{"request_data":{"endpoint_id":"<id>"}}'
```

## Carbon Black Cloud

```bash
curl -X POST "https://defense.conferdeploy.net/appservices/v6/orgs/<org_key>/device_actions" \
  -H "X-Auth-Token: $CB_TOKEN" -H "Content-Type: application/json" \
  -d '{"action_type":"QUARANTINE","device_id":["<id>"],"options":{}}'
```

## Network fabric

### Cisco IOS / NX-OS
```
interface GigabitEthernet1/0/12
 switchport access vlan 999
 description QUARANTINE-INC-1234
 shutdown
```

### Arista EOS
```
interface Ethernet12
 switchport access vlan 999
 description QUARANTINE-INC-1234
 shutdown
```

### Juniper Junos
```
set interfaces ge-0/0/12 unit 0 family ethernet-switching vlan members QUARANTINE
set interfaces ge-0/0/12 disable
```

### 802.1X / NAC
```
# Cisco ISE: change authorization profile to Quarantine
# Aruba ClearPass: set role to [Quarantine]
# Port bounce to force re-authentication
interface GigabitEthernet1/0/12
 shutdown
 no shutdown
```

## Verification

| Check | Command |
|---|---|
| EDR status | `jq '.resources[0].status'` on the device API |
| Host outbound | `curl -m 5 https://example.com` from the host |
| Host inbound | `nmap -Pn -p 22,445 <host>` from another host |
| Responder channel | EDR remote shell or OOB console |
| Switch state | `show interface status` |

## Unisolation gate

Do not unisolate until all of: malware removed and rescanned clean, persistence
removed, credentials rotated, and the incident owner approves. Record the
approver and timestamp.
