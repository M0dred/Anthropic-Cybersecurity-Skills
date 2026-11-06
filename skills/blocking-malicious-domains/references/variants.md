# Vendor Variants - Blocking Malicious Domains

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Block Domain - Cisco Stealthwatch

**Product:** Cisco Secure Network Analytics (Stealthwatch)

This playbook blocks domains using Cisco Stealthwatch Cloud

**Inputs:**

- `Domain`: The domain to block.

**Dependencies:**

- Integrations: Stealthwatch Cloud
- Commands: sw-block-domain-or-ip


## Block Domain - Destination Profile - Netskope

**Product:** Netskope - Direct to Zero Trust

Blocks a domain via a Netskope Destination Profile: looks up the profile by name and either appends the domain to that existing profile or, if no profile with that name exists yet, prompts the analyst to pick a match type and creates a new one with the domain as its first value. The match type prompt is a single-select with exactly three choices - sensitive (Exact - Case Sensitive), insensitive (Exact - Case Insensitive), or regex (RegEx), mirroring the "Match Type" choice in the Netskope UI's destination profile editor - so there's no risk of a typo or wrong casing (e.g. "Regex" instead of "regex") getting rejected by the create command. It's only asked when a new profile actually needs to be created - it's skipped entirely when appending to a profile that already exists (its match type was already fixed at creation). The integration performs the profile-name lookup safely by retrieving profile pages and comparing names locally, without interpolating ProfileName into an API filter. No manual ID lookup is needed; provide only the profile's display name. IMPORTANT: unlike the URL List and File Hash List "append" behavior, Netskope's destination profile values "append" operation has no server-side dedup - calling it twice with the same domain (e.g. re-running this playbook for a domain that's already blocked) adds it twice. This playbook checks the profile's current values (fetched by the name lookup) first and only appends when the domain isn't already present, so re-running i

**Inputs:**

- `Domain`: The domain to block.
- `ProfileName`: Name of the Netskope Destination Profile to add the domain to. The playbook performs an exact-name lookup without constructing a filter expression. If no profile exists, the analys
- `Deploy`: Whether to deploy the pending Destination Profile change. Defaults to false.
- `ChangeNote`: Change note recorded when Deploy is true.

**Dependencies:**

- Integrations: NetskopeV2
- Commands: netskopev2-create-destination-profile, netskopev2-deploy-destination-profiles, netskopev2-list-destination-profiles, netskopev2-update-destination-profile-values


## Block Domain - External Dynamic List

**Product:** Generic Export Indicators Service

This playbook blocks domains using External Dynamic Link. The playbook adds a tag to the inputs domain indicators. the tagged domains can be publish as External Dynamic list that can be added to blocklist using products like Panorama by Palo Alto Networks. For Panorama - You can block the tagged domains by creating EDL(in Panorama) with the  EDL Url, and assign it to Anti-Spyware profile under "DNS Signature Policies"

**Inputs:**

- `Domains`: The domains to block
- `Tag`: Indicator tag to assign

**Dependencies:**

- Commands: setIndicators


## Block Domain - FireEye Email Security

**Product:** FireEye Email Security (EX)

This playbook blocks domains using FireEye Email Security. The playbook checks whether the FireEye Email Security integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.

**Dependencies:**

- Integrations: FireEyeEX
- Commands: fireeye-ex-create-blockedlist


## Block Domain - Netskope

**Product:** Netskope - Direct to Zero Trust

Blocks a domain by adding it to an existing Netskope URL List. Checks whether the Domain and ListName inputs were provided, verifies that a Netskope integration instance is enabled, and adds the domain to the existing Netskope URL List. This pack has no "create list" command - the ListName input must reference a list that already exists

**Inputs:**

- `Domain`: The domain to block.
- `ListName`: Name of an existing Netskope URL List to add the domain to. Must already exist - this pack has no create-list command.

**Dependencies:**

- Integrations: NetskopeV2
- Commands: netskopev2-add-url


## Block Domain - Proofpoint Threat Response

**Product:** Proofpoint Threat Response

This playbook blocks domains using Proofpoint Threat Response. The playbook checks whether the Proofpoint Threat Response integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.
- `DomainBlackListID`: The ID of the block list to block the domain in.
- `Expiration`: The UTC expiration date and time of the suspicious object, for example: 2020-01-25T09:00:00Z

**Dependencies:**

- Integrations: ProofpointThreatResponse
- Commands: proofpoint-tr-block-domain


## Block Domain - Symantec Messaging Gateway

**Product:** Symantec Messaging Gateway

This playbook blocks domains using Symantec Messaging Gateway. The playbook checks whether the Symantec Messaging Gateway integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.

**Dependencies:**

- Integrations: integration-Symantec_Messaging_Gateway
- Commands: smg-block-domain


## Block Domain - Trend Micro Apex One

**Product:** TrendAI™ Apex One

This playbook blocks domains using TrendAI™ Apex One. The playbook checks whether the TrendAI™ Apex One integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The domain to block.
- `Expiration`: The UTC expiration date and time of the suspicious object, for example: 2020-01-25T09:00:00Z.

**Dependencies:**

- Integrations: TrendMicroApex
- Commands: trendmicro-apex-udso-add


## Block Domain - Zscaler

**Product:** Zscaler Internet Access

This playbook blocks domains using Zscaler. The playbook checks whether the Zscaler integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.

**Dependencies:**

- Integrations: Zscaler
- Commands: zscaler-blacklist-url

## Block Domain - Cisco Stealthwatch

**Product:** Cisco Secure Network Analytics (Stealthwatch)

This playbook blocks domains using Cisco Stealthwatch Cloud

**Inputs:**

- `Domain`: The domain to block.

**Dependencies:**

- Integrations: Stealthwatch Cloud
- Commands: sw-block-domain-or-ip


## Block Domain - Destination Profile - Netskope

**Product:** Netskope - Direct to Zero Trust

Blocks a domain via a Netskope Destination Profile: looks up the profile by name and either appends the domain to that existing profile or, if no profile with that name exists yet, prompts the analyst to pick a match type and creates a new one with the domain as its first value. The match type prompt is a single-select with exactly three choices - sensitive (Exact - Case Sensitive), insensitive (Exact - Case Insensitive), or regex (RegEx), mirroring the "Match Type" choice in the Netskope UI's destination profile editor - so there's no risk of a typo or wrong casing (e.g. "Regex" instead of "regex") getting rejected by the create command. It's only asked when a new profile actually needs to be created - it's skipped entirely when appending to a profile that already exists (its match type was already fixed at creation). The integration performs the profile-name lookup safely by retrieving profile pages and comparing names locally, without interpolating ProfileName into an API filter. No manual ID lookup is needed; provide only the profile's display name. IMPORTANT: unlike the URL List and File Hash List "append" behavior, Netskope's destination profile values "append" operation has no server-side dedup - calling it twice with the same domain (e.g. re-running this playbook for a domain that's already blocked) adds it twice. This playbook checks the profile's current values (fetched by the name lookup) first and only appends when the domain isn't already present, so re-running i

**Inputs:**

- `Domain`: The domain to block.
- `ProfileName`: Name of the Netskope Destination Profile to add the domain to. The playbook performs an exact-name lookup without constructing a filter expression. If no profile exists, the analys
- `Deploy`: Whether to deploy the pending Destination Profile change. Defaults to false.
- `ChangeNote`: Change note recorded when Deploy is true.

**Dependencies:**

- Integrations: NetskopeV2
- Commands: netskopev2-create-destination-profile, netskopev2-deploy-destination-profiles, netskopev2-list-destination-profiles, netskopev2-update-destination-profile-values


## Block Domain - External Dynamic List

**Product:** Generic Export Indicators Service

This playbook blocks domains using External Dynamic Link. The playbook adds a tag to the inputs domain indicators. the tagged domains can be publish as External Dynamic list that can be added to blocklist using products like Panorama by Palo Alto Networks. For Panorama - You can block the tagged domains by creating EDL(in Panorama) with the  EDL Url, and assign it to Anti-Spyware profile under "DNS Signature Policies"

**Inputs:**

- `Domains`: The domains to block
- `Tag`: Indicator tag to assign

**Dependencies:**

- Commands: setIndicators


## Block Domain - FireEye Email Security

**Product:** FireEye Email Security (EX)

This playbook blocks domains using FireEye Email Security. The playbook checks whether the FireEye Email Security integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.

**Dependencies:**

- Integrations: FireEyeEX
- Commands: fireeye-ex-create-blockedlist


## Block Domain - Netskope

**Product:** Netskope - Direct to Zero Trust

Blocks a domain by adding it to an existing Netskope URL List. Checks whether the Domain and ListName inputs were provided, verifies that a Netskope integration instance is enabled, and adds the domain to the existing Netskope URL List. This pack has no "create list" command - the ListName input must reference a list that already exists

**Inputs:**

- `Domain`: The domain to block.
- `ListName`: Name of an existing Netskope URL List to add the domain to. Must already exist - this pack has no create-list command.

**Dependencies:**

- Integrations: NetskopeV2
- Commands: netskopev2-add-url


## Block Domain - Proofpoint Threat Response

**Product:** Proofpoint Threat Response

This playbook blocks domains using Proofpoint Threat Response. The playbook checks whether the Proofpoint Threat Response integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.
- `DomainBlackListID`: The ID of the block list to block the domain in.
- `Expiration`: The UTC expiration date and time of the suspicious object, for example: 2020-01-25T09:00:00Z

**Dependencies:**

- Integrations: ProofpointThreatResponse
- Commands: proofpoint-tr-block-domain


## Block Domain - Symantec Messaging Gateway

**Product:** Symantec Messaging Gateway

This playbook blocks domains using Symantec Messaging Gateway. The playbook checks whether the Symantec Messaging Gateway integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.

**Dependencies:**

- Integrations: integration-Symantec_Messaging_Gateway
- Commands: smg-block-domain


## Block Domain - Trend Micro Apex One

**Product:** TrendAI™ Apex One

This playbook blocks domains using TrendAI™ Apex One. The playbook checks whether the TrendAI™ Apex One integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The domain to block.
- `Expiration`: The UTC expiration date and time of the suspicious object, for example: 2020-01-25T09:00:00Z.

**Dependencies:**

- Integrations: TrendMicroApex
- Commands: trendmicro-apex-udso-add


## Block Domain - Zscaler

**Product:** Zscaler Internet Access

This playbook blocks domains using Zscaler. The playbook checks whether the Zscaler integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.

**Dependencies:**

- Integrations: Zscaler
- Commands: zscaler-blacklist-url

## Block Domain - Cisco Stealthwatch

**Product:** Cisco Secure Network Analytics (Stealthwatch)

This playbook blocks domains using Cisco Stealthwatch Cloud

**Inputs:**

- `Domain`: The domain to block.

**Dependencies:**

- Integrations: Stealthwatch Cloud
- Commands: sw-block-domain-or-ip


## Block Domain - Destination Profile - Netskope

**Product:** Netskope - Direct to Zero Trust

Blocks a domain via a Netskope Destination Profile: looks up the profile by name and either appends the domain to that existing profile or, if no profile with that name exists yet, prompts the analyst to pick a match type and creates a new one with the domain as its first value. The match type prompt is a single-select with exactly three choices - sensitive (Exact - Case Sensitive), insensitive (Exact - Case Insensitive), or regex (RegEx), mirroring the "Match Type" choice in the Netskope UI's destination profile editor - so there's no risk of a typo or wrong casing (e.g. "Regex" instead of "regex") getting rejected by the create command. It's only asked when a new profile actually needs to be created - it's skipped entirely when appending to a profile that already exists (its match type was already fixed at creation). The integration performs the profile-name lookup safely by retrieving profile pages and comparing names locally, without interpolating ProfileName into an API filter. No manual ID lookup is needed; provide only the profile's display name. IMPORTANT: unlike the URL List and File Hash List "append" behavior, Netskope's destination profile values "append" operation has no server-side dedup - calling it twice with the same domain (e.g. re-running this playbook for a domain that's already blocked) adds it twice. This playbook checks the profile's current values (fetched by the name lookup) first and only appends when the domain isn't already present, so re-running i

**Inputs:**

- `Domain`: The domain to block.
- `ProfileName`: Name of the Netskope Destination Profile to add the domain to. The playbook performs an exact-name lookup without constructing a filter expression. If no profile exists, the analys
- `Deploy`: Whether to deploy the pending Destination Profile change. Defaults to false.
- `ChangeNote`: Change note recorded when Deploy is true.

**Dependencies:**

- Integrations: NetskopeV2
- Commands: netskopev2-create-destination-profile, netskopev2-deploy-destination-profiles, netskopev2-list-destination-profiles, netskopev2-update-destination-profile-values


## Block Domain - External Dynamic List

**Product:** Generic Export Indicators Service

This playbook blocks domains using External Dynamic Link. The playbook adds a tag to the inputs domain indicators. the tagged domains can be publish as External Dynamic list that can be added to blocklist using products like Panorama by Palo Alto Networks. For Panorama - You can block the tagged domains by creating EDL(in Panorama) with the  EDL Url, and assign it to Anti-Spyware profile under "DNS Signature Policies"

**Inputs:**

- `Domains`: The domains to block
- `Tag`: Indicator tag to assign

**Dependencies:**

- Commands: setIndicators


## Block Domain - FireEye Email Security

**Product:** FireEye Email Security (EX)

This playbook blocks domains using FireEye Email Security. The playbook checks whether the FireEye Email Security integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.

**Dependencies:**

- Integrations: FireEyeEX
- Commands: fireeye-ex-create-blockedlist


## Block Domain - Netskope

**Product:** Netskope - Direct to Zero Trust

Blocks a domain by adding it to an existing Netskope URL List. Checks whether the Domain and ListName inputs were provided, verifies that a Netskope integration instance is enabled, and adds the domain to the existing Netskope URL List. This pack has no "create list" command - the ListName input must reference a list that already exists

**Inputs:**

- `Domain`: The domain to block.
- `ListName`: Name of an existing Netskope URL List to add the domain to. Must already exist - this pack has no create-list command.

**Dependencies:**

- Integrations: NetskopeV2
- Commands: netskopev2-add-url


## Block Domain - Proofpoint Threat Response

**Product:** Proofpoint Threat Response

This playbook blocks domains using Proofpoint Threat Response. The playbook checks whether the Proofpoint Threat Response integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.
- `DomainBlackListID`: The ID of the block list to block the domain in.
- `Expiration`: The UTC expiration date and time of the suspicious object, for example: 2020-01-25T09:00:00Z

**Dependencies:**

- Integrations: ProofpointThreatResponse
- Commands: proofpoint-tr-block-domain


## Block Domain - Symantec Messaging Gateway

**Product:** Symantec Messaging Gateway

This playbook blocks domains using Symantec Messaging Gateway. The playbook checks whether the Symantec Messaging Gateway integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.

**Dependencies:**

- Integrations: integration-Symantec_Messaging_Gateway
- Commands: smg-block-domain


## Block Domain - Trend Micro Apex One

**Product:** TrendAI™ Apex One

This playbook blocks domains using TrendAI™ Apex One. The playbook checks whether the TrendAI™ Apex One integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The domain to block.
- `Expiration`: The UTC expiration date and time of the suspicious object, for example: 2020-01-25T09:00:00Z.

**Dependencies:**

- Integrations: TrendMicroApex
- Commands: trendmicro-apex-udso-add


## Block Domain - Zscaler

**Product:** Zscaler Internet Access

This playbook blocks domains using Zscaler. The playbook checks whether the Zscaler integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.

**Dependencies:**

- Integrations: Zscaler
- Commands: zscaler-blacklist-url

## Block Domain - Cisco Stealthwatch

**Product:** Cisco Secure Network Analytics (Stealthwatch)

This playbook blocks domains using Cisco Stealthwatch Cloud

**Inputs:**

- `Domain`: The domain to block.

**Dependencies:**

- Integrations: Stealthwatch Cloud
- Commands: sw-block-domain-or-ip


## Block Domain - Destination Profile - Netskope

**Product:** Netskope - Direct to Zero Trust

Blocks a domain via a Netskope Destination Profile: looks up the profile by name and either appends the domain to that existing profile or, if no profile with that name exists yet, prompts the analyst to pick a match type and creates a new one with the domain as its first value. The match type prompt is a single-select with exactly three choices - sensitive (Exact - Case Sensitive), insensitive (Exact - Case Insensitive), or regex (RegEx), mirroring the "Match Type" choice in the Netskope UI's destination profile editor - so there's no risk of a typo or wrong casing (e.g. "Regex" instead of "regex") getting rejected by the create command. It's only asked when a new profile actually needs to be created - it's skipped entirely when appending to a profile that already exists (its match type was already fixed at creation). The integration performs the profile-name lookup safely by retrieving profile pages and comparing names locally, without interpolating ProfileName into an API filter. No manual ID lookup is needed; provide only the profile's display name. IMPORTANT: unlike the URL List and File Hash List "append" behavior, Netskope's destination profile values "append" operation has no server-side dedup - calling it twice with the same domain (e.g. re-running this playbook for a domain that's already blocked) adds it twice. This playbook checks the profile's current values (fetched by the name lookup) first and only appends when the domain isn't already present, so re-running i

**Inputs:**

- `Domain`: The domain to block.
- `ProfileName`: Name of the Netskope Destination Profile to add the domain to. The playbook performs an exact-name lookup without constructing a filter expression. If no profile exists, the analys
- `Deploy`: Whether to deploy the pending Destination Profile change. Defaults to false.
- `ChangeNote`: Change note recorded when Deploy is true.

**Dependencies:**

- Integrations: NetskopeV2
- Commands: netskopev2-create-destination-profile, netskopev2-deploy-destination-profiles, netskopev2-list-destination-profiles, netskopev2-update-destination-profile-values


## Block Domain - External Dynamic List

**Product:** Generic Export Indicators Service

This playbook blocks domains using External Dynamic Link. The playbook adds a tag to the inputs domain indicators. the tagged domains can be publish as External Dynamic list that can be added to blocklist using products like Panorama by Palo Alto Networks. For Panorama - You can block the tagged domains by creating EDL(in Panorama) with the  EDL Url, and assign it to Anti-Spyware profile under "DNS Signature Policies"

**Inputs:**

- `Domains`: The domains to block
- `Tag`: Indicator tag to assign

**Dependencies:**

- Commands: setIndicators


## Block Domain - FireEye Email Security

**Product:** FireEye Email Security (EX)

This playbook blocks domains using FireEye Email Security. The playbook checks whether the FireEye Email Security integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.

**Dependencies:**

- Integrations: FireEyeEX
- Commands: fireeye-ex-create-blockedlist


## Block Domain - Netskope

**Product:** Netskope - Direct to Zero Trust

Blocks a domain by adding it to an existing Netskope URL List. Checks whether the Domain and ListName inputs were provided, verifies that a Netskope integration instance is enabled, and adds the domain to the existing Netskope URL List. This pack has no "create list" command - the ListName input must reference a list that already exists

**Inputs:**

- `Domain`: The domain to block.
- `ListName`: Name of an existing Netskope URL List to add the domain to. Must already exist - this pack has no create-list command.

**Dependencies:**

- Integrations: NetskopeV2
- Commands: netskopev2-add-url


## Block Domain - Proofpoint Threat Response

**Product:** Proofpoint Threat Response

This playbook blocks domains using Proofpoint Threat Response. The playbook checks whether the Proofpoint Threat Response integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.
- `DomainBlackListID`: The ID of the block list to block the domain in.
- `Expiration`: The UTC expiration date and time of the suspicious object, for example: 2020-01-25T09:00:00Z

**Dependencies:**

- Integrations: ProofpointThreatResponse
- Commands: proofpoint-tr-block-domain


## Block Domain - Symantec Messaging Gateway

**Product:** Symantec Messaging Gateway

This playbook blocks domains using Symantec Messaging Gateway. The playbook checks whether the Symantec Messaging Gateway integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.

**Dependencies:**

- Integrations: integration-Symantec_Messaging_Gateway
- Commands: smg-block-domain


## Block Domain - Trend Micro Apex One

**Product:** TrendAI™ Apex One

This playbook blocks domains using TrendAI™ Apex One. The playbook checks whether the TrendAI™ Apex One integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The domain to block.
- `Expiration`: The UTC expiration date and time of the suspicious object, for example: 2020-01-25T09:00:00Z.

**Dependencies:**

- Integrations: TrendMicroApex
- Commands: trendmicro-apex-udso-add


## Block Domain - Zscaler

**Product:** Zscaler Internet Access

This playbook blocks domains using Zscaler. The playbook checks whether the Zscaler integration is enabled, whether the Domain input has been provided and if so, blocks the domain

**Inputs:**

- `Domain`: The Domain to block.

**Dependencies:**

- Integrations: Zscaler
- Commands: zscaler-blacklist-url

