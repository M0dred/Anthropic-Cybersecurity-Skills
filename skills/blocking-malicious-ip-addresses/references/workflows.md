# Workflows - Blocking Malicious IP Addresses

## Decision tree

```
Is the IP routable and unicast?
├─ no  -> reject; fix the input
└─ yes -> Is it inside our own ranges?
          ├─ yes -> do not block at the perimeter; investigate the internal host
          └─ no  -> Is it shared infrastructure (CDN, cloud, mail)?
                    ├─ yes -> block the URI, port, or path, not the address
                    └─ no  -> Is the traffic inbound or outbound?
                              ├─ inbound  -> perimeter + host INPUT
                              ├─ outbound -> host OUTPUT + egress proxy/firewall
                              └─ both     -> apply both, verify both
```

## Containment sequence

1. **Capture evidence first.** Export the relevant logs and packet captures
   before the block, because the block removes your ability to observe.
2. **Block the narrowest scope that stops the activity.** A single host before a
   /24; a port before a protocol; a URI before an address.
3. **Apply at the closest enforcement point**, then widen if the activity
   continues.
4. **Verify with a control.** Confirm the blocked path fails and an allowed path
   still works.
5. **Set an expiry.** 24 hours for a tactical block, 30 days for an
   intelligence-driven block, with an owner.

## Multi-layer block pattern

| Layer | Control | Latency to effect |
|---|---|---|
| Host | iptables / nftables / pf | seconds |
| Cloud network | security group, NACL, VPC firewall | seconds to minutes |
| Perimeter | PAN-OS, Check Point, FortiGate | commit cycle |
| Edge / proxy | Cloudflare, Zscaler | seconds |
| DNS | sinkhole or RPZ | TTL-bound |

Apply host and edge first for immediate effect, then the perimeter for
durability.

## Rollback procedure

```bash
# 1. Identify the exact rule
sudo iptables -L INPUT -n -v --line-numbers | grep <IP>

# 2. Remove it
sudo iptables -D INPUT <NUMBER>

# 3. Confirm removal
sudo iptables -L INPUT -n | grep <IP> || echo "removed"

# 4. Re-test the path
timeout 5 bash -c 'cat < /dev/null > /dev/tcp/<IP>/443' ; echo "exit=$?"
```

## Incident record template

```
Incident:        INC-1234
Indicator:       203.0.113.10 (source, inbound, TCP/443)
Provenance:      sandbox verdict, 2026-08-31T10:12Z
Enforcement:     iptables on web-01; AWS NACL acl-0123 rule 90
Applied by:      analyst@example.com
Approved by:     soc-lead@example.com
Rollback:        iptables -D INPUT 1; aws ec2 delete-network-acl-entry ...
Expires:         2026-09-30
Verification:    curl from external vantage failed; control host succeeded
```
