---
name: blocking-malicious-ip-addresses
description: >-
  Blocks malicious IP addresses at the enforcement point closest to the threat:
  host firewalls (iptables, nftables, pf), cloud security groups and NACLs
  (AWS, Azure, GCP), and perimeter devices (PAN-OS, Check Point, FortiGate,
  Zscaler, Cloudflare). Covers source validation, direction and scope decisions,
  rule placement, and post-change verification. Use when containing an active
  intrusion, responding to brute-force or scanning alerts, or enforcing a
  threat-intelligence blocklist. Keywords: block IP, deny list, iptables,
  nftables, security group, NSG, firewall rule, EDL, containment.
  Do not use for blocking domains or URLs - use blocking-malicious-domains or
  blocking-malicious-urls. Do not use for isolating a compromised host - use
  isolating-compromised-endpoints.
domain: cybersecurity
subdomain: network-security
tags:
- incident-response
- containment
- firewall
- iptables
- cloud-security
- network-security
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- RS.MI-01
- PR.AC-05
- DE.CM-01
mitre_attack:
- T1562.004
- T1071
- T1105
---

# Blocking Malicious IP Addresses

## When to Use

- An intrusion is active and the source or destination IP must be cut off now.
- A brute-force, credential-stuffing, or port-scan alert names an external IP.
- A threat-intelligence feed or sandbox verdict marks an IP as malicious.
- A command-and-control beacon resolves to a known-bad address.
- An incident review asks you to prove that a block was applied and is working.

**Do not use** for blocking domains, URLs, or file hashes; those need different
enforcement points and different verification. **Do not use** for isolating an
endpoint that is already compromised; isolation is a host-level action that
keeps the host reachable by the responder.

## Prerequisites

- The IP list, with provenance: which alert, feed, or analyst produced it.
- Authority to change the target device or cloud account. A block on a
  production security group is a change-controlled action in most environments.
- Read access to the enforcement point so you can verify the rule after writing.
- A rollback path: the exact command that removes the rule you are about to add.
- Knowledge of the traffic direction. Blocking an inbound scanner is different
  from blocking outbound C2, and a wrong direction silently does nothing.

## Workflow

### Step 1: Validate the IP list before touching a firewall

Reject anything that is not a routable unicast address:

```bash
# Normalize and de-duplicate; drop private, loopback, multicast, and invalid entries
python3 scripts/agent.py validate --ip 203.0.113.10 --ip 198.51.100.7 --ip 10.0.0.5
```

Check each address against the environment's own ranges. Blocking an internal
address at the perimeter does nothing, and blocking a corporate egress address
breaks every user behind it.

```bash
# Confirm the address is not one of yours
whois 203.0.113.10 | grep -iE 'orgname|netname|country'
```

### Step 2: Decide direction and scope

| Question | Consequence |
|---|---|
| Is the IP the source of inbound traffic? | Block inbound at the perimeter and at the host. |
| Is the IP the destination of outbound traffic? | Block outbound at the host, proxy, and egress firewall. |
| Is it a single host or a /24? | Single host unless the whole range is attributed. |
| Is it shared infrastructure (CDN, cloud, mail)? | Block the specific path or port, not the whole address. |
| Does the business depend on it? | Get written approval before a production block. |

### Step 3: Apply at the narrowest effective point

Host firewall (fastest, survives only on that host):

```bash
# iptables: drop inbound and outbound, log before dropping
sudo iptables -I INPUT 1 -s 203.0.113.10 -j DROP
sudo iptables -I OUTPUT 1 -d 203.0.113.10 -j DROP
sudo iptables -I INPUT 1 -s 203.0.113.10 -j LOG --log-prefix "BLOCKED-IP: "

# nftables equivalent
sudo nft add rule inet filter input ip saddr 203.0.113.10 drop
sudo nft add rule inet filter output ip daddr 203.0.113.10 drop

# Persist across reboot
sudo iptables-save | sudo tee /etc/iptables/rules.v4
```

Cloud security group or firewall:

```bash
# AWS: deny by removing the allow path, then add an explicit deny in a NACL
aws ec2 describe-security-groups --group-ids sg-0123456789abcdef0 \
  --query 'SecurityGroups[0].IpPermissions'
aws ec2 revoke-security-group-ingress --group-id sg-0123456789abcdef0 \
  --ip-permissions 'IpProtocol=-1,IpRanges=[{CidrIp=203.0.113.10/32}]'
aws ec2 create-network-acl-entry --network-acl-id acl-0123456789abcdef0 \
  --rule-number 90 --protocol -1 --cidr-block 203.0.113.10/32 --rule-action deny --egress

# Azure: deny rule in the NSG, lower priority number wins
az network nsg rule create -g rg-prod -n deny-203-0-113-10 \
  --nsg-name nsg-web --priority 100 --direction Inbound \
  --access Deny --protocol '*' --source-address-prefixes 203.0.113.10/32 \
  --source-port-ranges '*' --destination-address-prefixes '*' --destination-port-ranges '*'

# GCP: VPC firewall rules are allow-only; remove the allow and use a
# hierarchical firewall policy or a deny rule at the edge
gcloud compute firewall-rules list --filter="sourceRanges:203.0.113.10"
gcloud compute firewall-rules create deny-203-0-113-10 \
  --action DENY --direction INGRESS --rules all \
  --source-ranges 203.0.113.10/32 --priority 100
```

Perimeter device:

```bash
# PAN-OS: add to an External Dynamic List, then reference it in a deny rule
set external-list blocklist type ip
set external-list blocklist url https://internal.example.com/blocklist.txt
set rulebase security rules deny-blocklist source [ blocklist ]
set rulebase security rules deny-blocklist action deny

# Cloudflare: block at the edge
curl -X POST "https://api.cloudflare.com/client/v4/accounts/$CF_ACCOUNT/firewall/access_rules/rules" \
  -H "Authorization: Bearer $CF_TOKEN" -H "Content-Type: application/json" \
  --data '{"mode":"block","configuration":{"target":"ip","value":"203.0.113.10"},"notes":"incident INC-1234"}'
```

### Step 4: Verify the block is actually in the path

```bash
# Host: rule present and counters incrementing
sudo iptables -L INPUT -n -v | grep 203.0.113.10
sudo nft list ruleset | grep 203.0.113.10

# AWS: confirm the deny entry exists in the NACL
aws ec2 describe-network-acls --network-acl-ids acl-0123456789abcdef0 \
  --query 'NetworkAcls[0].Entries[?CidrBlock==`203.0.113.10/32`]'

# Azure: confirm the rule and its priority
az network nsg rule show -g rg-prod --nsg-name nsg-web -n deny-203-0-113-10

# Active test from an external vantage point (authorized only)
curl -m 5 --connect-timeout 3 http://203.0.113.10/ ; echo "exit=$?"
```

### Step 5: Record the change

Capture, per enforcement point: the rule text, the operator, the ticket, the
timestamp, and the rollback command. Attach it to the incident. A block nobody
can find later becomes an outage nobody can explain.

## Verification

- The rule exists in the running configuration, not only in a saved file.
- A test connection from the blocked source fails while a control connection
  from an allowed source succeeds.
- Packet counters on the rule increase when traffic arrives.
- The block survives a configuration reload or reboot where persistence is
  required.
- The rollback command has been tested in a lab or on a canary host.

## Common Pitfalls

- **Wrong direction.** Blocking inbound when the beacon is outbound leaves C2
  alive; check both directions when the role is unclear.
- **Blocking shared infrastructure.** A CDN or cloud egress address can front
  thousands of legitimate customers; block the URI or port instead.
- **Rule order.** In iptables and NSGs the first match wins; an ACCEPT above
  your DROP makes the block invisible.
- **Forgetting IPv6.** The same host often has an AAAA record; block both
  families.
- **No expiry.** Every block needs an owner and a review date, or the ruleset
  grows into an unmaintainable deny-all.
- **Silent cloud behavior.** AWS security groups have no deny rule; you must
  remove the allow or use a NACL. GCP VPC rules are allow-only at the project
  level.

## References

- `references/api-reference.md` - commands per enforcement point
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and rollback procedures
- `scripts/agent.py` - validation, rule generation, dry-run and apply
