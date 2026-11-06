# API Reference - Blocking Malicious IP Addresses

## Host firewalls

### iptables
```bash
# Insert at the top of the chain so no earlier ACCEPT shadows the rule
iptables -I INPUT 1 -s <IP> -j DROP
iptables -I OUTPUT 1 -d <IP> -j DROP
iptables -I INPUT 1 -s <IP> -j LOG --log-prefix "BLOCKED-IP: "

# Verify counters
iptables -L INPUT -n -v --line-numbers | grep <IP>

# Remove by rule number (safer than -D by spec when duplicates exist)
iptables -D INPUT <NUMBER>

# Persist (Debian/Ubuntu)
apt install iptables-persistent
netfilter-persistent save
```

### nftables
```bash
nft add table inet filter
nft add chain inet filter input '{ type filter hook input priority 0; policy accept; }'
nft add rule inet filter input ip saddr <IP> drop
nft add rule inet filter output ip daddr <IP> drop
nft list ruleset
nft -a list chain inet filter input          # show handles
nft delete rule inet filter input handle <H>
```

### pf (macOS, BSD)
```bash
# /etc/pf.anchors/blocklist
block drop quick from <IP> to any
block drop quick from any to <IP>

pfctl -a blocklist -f /etc/pf.anchors/blocklist
pfctl -sr | grep <IP>
```

## Cloud

### AWS
```bash
# Security groups are allow-only. To deny, remove the allow or use a NACL.
aws ec2 revoke-security-group-ingress \
  --group-id sg-0123456789abcdef0 \
  --ip-permissions 'IpProtocol=-1,IpRanges=[{CidrIp=<IP>/32}]'

aws ec2 create-network-acl-entry \
  --network-acl-id acl-0123456789abcdef0 \
  --rule-number 90 --protocol -1 --cidr-block <IP>/32 \
  --rule-action deny --egress

aws ec2 describe-network-acls --network-acl-ids acl-0123456789abcdef0 \
  --query 'NetworkAcls[0].Entries[?CidrBlock==`<IP>/32`]'

# AWS Network Firewall (stateful rule group) for egress control
aws network-firewall update-rule-group \
  --rule-group-arn <ARN> --rules <SURICATA_RULES>
```

### Azure
```bash
az network nsg rule create -g <RG> -n deny-<slug> --nsg-name <NSG> \
  --priority 100 --direction Inbound --access Deny --protocol '*' \
  --source-address-prefixes <IP>/32 --source-port-ranges '*' \
  --destination-address-prefixes '*' --destination-port-ranges '*'

az network nsg rule list -g <RG> --nsg-name <NSG> -o table
az network nsg rule delete -g <RG> --nsg-name <NSG> -n deny-<slug>
```

### GCP
```bash
# VPC firewall rules are allow-only at project level; use DENY action
gcloud compute firewall-rules create deny-<slug> \
  --action DENY --direction INGRESS --rules all \
  --source-ranges <IP>/32 --priority 100

gcloud compute firewall-rules describe deny-<slug>
gcloud compute firewall-rules delete deny-<slug>

# Organization-wide: hierarchical firewall policy
gcloud compute firewall-policies rules create 1000 \
  --firewall-policy <POLICY> --action deny --direction INGRESS \
  --src-ip-ranges <IP>/32 --layer4-configs all
```

## Perimeter devices

### PAN-OS
```bash
# CLI
set external-list blocklist type ip
set external-list blocklist url https://internal.example.com/blocklist.txt
set rulebase security rules deny-blocklist source [ blocklist ]
set rulebase security rules deny-blocklist destination any
set rulebase security rules deny-blocklist application any
set rulebase security rules deny-blocklist service any
set rulebase security rules deny-blocklist action deny
commit

# REST
curl -k -X POST "https://<PANORAMA>/api/?type=config&action=set&key=$KEY" \
  --data-urlencode 'xpath=/config/devices/entry[@name="localhost.localdomain"]/vsys/entry[@name="vsys1"]/rulebase/security/rules' \
  --data-urlencode 'element=<entry name="deny-blocklist"><action>deny</action><from><member>any</member></from><to><member>any</member></to><source><member>blocklist</member></source><destination><member>any</member></destination><application><member>any</member></application><service><member>any</member></service></entry>'
```

### Check Point
```bash
# Management API
curl -X POST "https://<MGMT>/web_api/add-access-rule" \
  -H "X-chkp-sid: $SID" -H "Content-Type: application/json" \
  -d '{"layer":"Network","position":"top","name":"deny-<slug>","action":"Drop","source":"<IP>","destination":"Any","track":{"type":"Log"}}'
curl -X POST "https://<MGMT>/web_api/publish" -H "X-chkp-sid: $SID"
```

### FortiGate
```bash
config firewall address
  edit "block-<slug>"
    set subnet <IP> 255.255.255.255
  next
end
config firewall policy
  edit 0
    set name "deny-block-<slug>"
    set srcintf "any"
    set dstintf "any"
    set srcaddr "block-<slug>"
    set dstaddr "all"
    set action deny
    set schedule "always"
    set service "ALL"
  next
end
```

### Zscaler
```bash
# ZIA: add to a deny-listed destination group, then reference it in a rule
curl -X POST "https://zsapi.zscaler.net/api/v1/urlCategories" \
  -H "Content-Type: application/json" \
  -d '{"configuredName":"BLOCKLIST-IP","urls":["<IP>"],"dbCategorizedUrls":[]}'
```

### Cloudflare
```bash
curl -X POST "https://api.cloudflare.com/client/v4/accounts/$CF_ACCOUNT/firewall/access_rules/rules" \
  -H "Authorization: Bearer $CF_TOKEN" -H "Content-Type: application/json" \
  --data '{"mode":"block","configuration":{"target":"ip","value":"<IP>"},"notes":"INC-1234"}'

curl "https://api.cloudflare.com/client/v4/accounts/$CF_ACCOUNT/firewall/access_rules/rules" \
  -H "Authorization: Bearer $CF_TOKEN"
```

## Verification commands

```bash
# Local reachability test (authorized targets only)
timeout 5 bash -c 'cat < /dev/null > /dev/tcp/<IP>/443' ; echo "exit=$?"

# Traceroute to confirm the drop is at the expected hop
traceroute -n -m 8 <IP>

# SIEM confirmation: the deny log line for the source
index=firewall src_ip="<IP>" action=denied | stats count by host, rule
```

## Rollback

| Target | Rollback |
|---|---|
| iptables | `iptables -D INPUT <N>` |
| nftables | `nft delete rule inet filter input handle <H>` |
| pf | remove the anchor line, `pfctl -a blocklist -f /etc/pf.anchors/blocklist` |
| AWS NACL | `aws ec2 delete-network-acl-entry --network-acl-id <ID> --rule-number 90 --egress` |
| Azure NSG | `az network nsg rule delete -g <RG> --nsg-name <NSG> -n deny-<slug>` |
| GCP | `gcloud compute firewall-rules delete deny-<slug>` |
| Cloudflare | `DELETE /accounts/{account_id}/firewall/access_rules/rules/{rule_id}` |
