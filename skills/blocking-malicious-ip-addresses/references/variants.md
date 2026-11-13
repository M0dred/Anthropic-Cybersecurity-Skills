# Vendor Variants - Blocking Malicious Ip Addresses

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Block IP - Network Profile - Netskope

**Product:** Netskope - Direct to Zero Trust

Blocks an IP address, IP range, or CIDR netmask via a Netskope Network Profile (shown as "Network Location" in the Netskope UI) - the same "check input / check integration enabled / act" pattern as Block Domain - Destination Profile - Netskope, adapted for Network Profiles instead of Destination Profiles. Looks up the network profile by name and either appends the value to that existing profile or, if no profile with that name exists yet, creates a new one with the value as its first entry. Unlike Destination Profiles, Network Profiles have no match type at all (netskopev2-create- network-profile takes no "type" argument) - so unlike the destination profile playbook, there's no "choose a match type" prompt here; creating a new profile needs nothing beyond the name and the value itself. Profile names are unique in Netskope, so the playbook performs an exact-name lookup without constructing a filter expression. IMPORTANT: like Destination Profiles, Network Profile values "append" has no server-side dedup - calling it twice with the same value (e.g. re-running this playbook for a value that's already present) adds it twice. This playbook checks the profile's current values first and only appends when the value isn't already present, so re-running it for an already-blocked value is a safe no-op. Also make sure only one Netskope integration instance is enabled at a time - if two are enabled,   dispatches the command to both, causing the same double-add. Network Profile

**Inputs:**

- `ProfileName`: Name of the Netskope Network Profile (shown as "Network Location" in the Netskope UI). The playbook performs an exact-name lookup without constructing a filter expression.
- `Value`: IP address, IP range, or CIDR netmask to add (e.g. "192.0.2.0/27").
- `Deploy`: Whether to deploy the pending Network Profile change. Defaults to false.
- `ChangeNote`: Change note recorded when Deploy is true.

**Dependencies:**

- Integrations: NetskopeV2
- Commands: netskopev2-create-network-profile, netskopev2-deploy-network-profiles, netskopev2-list-network-profiles, netskopev2-update-network-profile-values


## Checkpoint - Block IP - Append Group

**Product:** Check Point Firewall

The playbook receives malicious IP addresses as inputs, checks if the object group exists (if not, the object group is created), and appends the related IPs to that object. If you have not assigned the appended group to a rule in your firewall policy, you can use rule_name and the playbook creates a new rule

**Inputs:**

- `IP`: An array of malicious IPs to block (Can be also provided as a context path. e.g. ${IP} ).Example: 1.1.1.1,2.2.2.2
- `install_policy`: Whether the playbook should continue install policy process for Check Point Firewall.
- `policy_package`: The name of the policy package to be installed.
- `block_IP_error_handling`: If one of the actions for the Block IP playbook fails due to issues on the Check Point Firewall, this input determines whether the playbook continues or stops for manual review. If
- `checkpoint_error_handling`: If one of the actions for publish/install policy fails due to issues on the Check Point side, this input determines whether the playbook continues or stops for manual review. If th
- `group_name`: The group name to be appended with the provided IPs. The group is created if it does not already exist.
- `rule_name`: Creates a new blocking rule using this Check Point Firewall group. Use this option if you have not assigned the appended group to a rule in your firewall policy.
- `rule_layer`: Determines which Check Point Firewall rule layer is used.By default, the "Network" layer is used, but this can be changed.
- `rule_position`: Determines which Check Point Firewall rule position is used.By default, the "top" position is used, but this can be changed.

**Dependencies:**

- Sub-playbooks: Checkpoint - Publish&Install configuration
- Integrations: CheckPointFirewallV2
- Scripts: isError, CompareLists, SetAndHandleEmpty, Print
- Commands: checkpoint-group-update, checkpoint-show-objects, checkpoint-logout, checkpoint-host-add, checkpoint-group-get, checkpoint-access-rule-add, checkpoint-login-and-get-session-id, checkpoint-group-add


## Checkpoint - Block IP - Custom Block Rule

**Product:** Check Point Firewall

This playbook blocks IP addresses using Custom Block Rules in Check Point Firewall. The playbook receives malicious IP addresses as inputs, creates a custom bi-directional rule to block them, and publishes the configuration

**Inputs:**

- `IP`: An array of malicious IPs to block (Can be also provided as a context path. e.g. ${IP} ).Example: 1.1.1.1,2.2.2.2
- `install_policy`: Whether the playbook should continue install policy process for Check Point Firewall.
- `policy_package`: The name of the policy package to be installed.
- `block_IP_error_handling`: If one of the actions for the Block IP playbook fails due to issues on the Check Point Firewall, this input determines whether the playbook continues or stops for manual review. If
- `checkpoint_error_handling`: If one of the actions for publish/install policy fails due to issues on the Check Point side, this input determines whether the playbook continues or stops for manual review. If th
- `rule_layer`: Determines which Check Point Firewall rule layer is used.By default, the "Network" layer is used, but this can be changed.
- `rule_position`: Determines which Check Point Firewall rule position is used.By default, the "top" position is used, but this can be changed.
- `rule_name`: Creates a new blocking rule using this Check Point Firewall group. Use this option if you have not assigned the appended group to a rule in your firewall policy.

**Dependencies:**

- Sub-playbooks: Checkpoint - Publish&Install configuration
- Integrations: CheckPointFirewallV2
- Scripts: Print, CompareLists
- Commands: checkpoint-access-rule-add, checkpoint-logout, checkpoint-login-and-get-session-id, checkpoint-access-rule-list, checkpoint-group-update, checkpoint-show-objects, checkpoint-host-add, checkpoint-group-add


## PAN-OS - Block IPs From EDL - Custom Block Rule

**Product:** PAN-OS by Palo Alto Networks

This playbook blocks IP addresses from an External Dynamic List using Custom Block Rules in Palo Alto Networks Panorama or Firewall. The playbook receives an EDL name as input, creates a custom "from" directional rule to block, and commits the configuration

**Inputs:**

- `RuleName`: Panorama rule name.
- `EDLName`: EDL IPs to block.
- `AutoCommit`: This input establishes whether to commit the configuration automatically.Yes - Commit automatically.No - Commit manually.
- `LogForwarding`: Panorama log forwarding object name.

**Dependencies:**

- Commands: pan-os-commit, pan-os-custom-block-rule


## PAN-OS - Block IP - Custom Block Rule

**Product:** PAN-OS by Palo Alto Networks

Blocks IP addresses using Custom Block Rules in Palo Alto Networks Panorama or Firewall. The playbook receives malicious IP addresses as inputs, creates a custom bi-directional rule to block them, and commits the configuration

**Inputs:**

- `LogForwarding`: The Panorama log forwarding object name.
- `IP`: The IP address to block.
- `AutoCommit`: Whether to commit the configuration automatically. "Yes", will commit automatically. "No" will commit manually.

**Dependencies:**

- Sub-playbooks: PAN-OS Commit Configuration
- Commands: pan-os-create-address, pan-os-custom-block-rule


## PAN-OS - Block IP - Static Address Group

**Product:** PAN-OS by Palo Alto Networks

This playbook blocks IP addresses using Static Address Groups in Palo Alto Networks Panorama or Firewall. The playbook receives malicious IP addresses and an address group name as inputs, verifies that the addresses are not already a part of the address group, adds them and commits the configuration. ***Note - The playbook does not block the address group communication using a policy block rule. This step will be taken once outside of the playbook

**Inputs:**

- `IP`: IP address to block
- `AddressGroupName`: Static address group name
- `AutoCommit`: This input establishes whether to commit the configuration automatically.Yes - Commit automatically.No - Commit manually.
- `IPDescription`: The description of the IP in case it will get created by the playbook.

**Dependencies:**

- Sub-playbooks: PAN-OS Commit Configuration v2
- Integrations: Panorama
- Commands: pan-os-create-address, pan-os-get-address-group, pan-os-edit-address-group


## PAN-OS - Block IP

**Product:** PAN-OS by Palo Alto Networks

This playbook blocks IP addresses with 2 optional actions

**Inputs:**

- `MaliciousIPs`: IP or list of IPs.

**Dependencies:**

- Sub-playbooks: PAN-OS DAG Configuration, PAN-OS - Block IP - Static Address Group
- Integrations: Panorama
- Commands: pan-os-list-tag, pan-os-list-address-groups


## Prisma SASE - Block IP

**Product:** Palo Alto Networks - Strata Cloud Manager

This playbook assists in blocking communication with the provided IPs in the Prisma SASE policy. If a group name is provided, the IPs will be added to the mentioned static address group (there should be a rule associated with the group name to block communication with that group). And if the group name is not provided, a new group will be created with a dedicated rule to block communication with those IPs

**Inputs:**

- `TSGID`: Tenant services group ID. If not provided, the tsg_id integration parameter will be used as the default.
- `IP`: The address value (should match the type).
- `Folder`: The configuration folder group setting.The default value is 'Shared'.
- `StaticAddressGroupName`: The static address group name will be appended with IP indicators.
- `AutoCommit`: Possible Values:True -&gt; Will commit and push configuration.False -&gt; Manual push will be required.Else --&gt; Will ignore the push section and continue the playbook.

**Outputs:**

- `PrismaSase.AddressGroup`
- `PrismaSase.AddressGroup.id`
- `PrismaSase.AddressGroup.name`
- `PrismaSase.AddressGroup.description`
- `PrismaSase.AddressGroup.addresses`
- `PrismaSase.AddressGroup.dynamic_filter`
- `PrismaSase.AddressGroup.folder`
- `PrismaSase`
- `PrismaSase.SecurityRule`
- `PrismaSase.SecurityRule.action`

**Dependencies:**

- Sub-playbooks: Prisma SASE - Create Address Object, Prisma SASE - Add IPs to Static Address Group
- Integrations: PrismaSASE
- Commands: prisma-sase-candidate-config-push, prisma-sase-security-rule-create, prisma-sase-address-group-list, prisma-sase-address-group-create

