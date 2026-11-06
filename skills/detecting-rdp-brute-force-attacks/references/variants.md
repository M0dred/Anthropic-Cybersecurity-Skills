# Vendor Variants - Detecting Rdp Brute Force Attacks

Vendor-specific implementations, feeds, and collectors for this procedure.


## Possible External RDP Brute-Force

**Product:** Core

**Kind:** playbook

This playbook investigates a “Possible External RDP Brute Force” XDR Alert by gathering user, IP, and hostname information, and investigating if the following suspicious elements exists: Set verdict method

**Inputs:**

- `Username`: RDP connection username.
- `ExternalIP`: Source external IP address.
- `AutoRemediation`: Set this value to "true" to enable auto remediation (IP Block and User Block).
- `FinalThreshold`: The threshold number of suspicious elements required to determine a 'True Positive' verdict.
- `CriticalElement`: You can select a specific element that, if identified as suspicious, will automatically set the final verdict as true positive. The following options are available:IP ReputationRel
- `UserEngagementThreshold`: The threshold number of suspicious elements that will trigger a user engagement. Set 0 to disable user engagement.NOTICE: If this threshold is equal to or higher than "FinalThresho
- `Hostname`: RDP connection destination hostname.
- `EndpointID`: RDP connection destination endpoint ID.
- `Country`: Source external IP country.
- `IsolateEndpoint`: Set this value to "true" to enable endpoint isolation in case of a true positive.

**Dependencies:**

- Sub-playbooks: Block Indicators - Generic v3, Threat Hunting - Generic, Get entity alerts by MITRE tactics, TIM - Indicator Relationships Analysis, Endpoint Enrichment - Generic v2.1, Possible External RDP Brute-Force - Set Verdict, Account Enrichment - Generic v2.1, User Investigation - Generic
- Integrations: CoreIOCs, CortexCoreIR
- Scripts: Set, IsIntegrationAvailable
- Commands: core-isolate-endpoint, ip, ad-expire-password, setIncident

## Possible External RDP Brute-Force

**Product:** Core

**Kind:** playbook

This playbook investigates a “Possible External RDP Brute Force” XDR Alert by gathering user, IP, and hostname information, and investigating if the following suspicious elements exists: Set verdict method

**Inputs:**

- `Username`: RDP connection username.
- `ExternalIP`: Source external IP address.
- `AutoRemediation`: Set this value to "true" to enable auto remediation (IP Block and User Block).
- `FinalThreshold`: The threshold number of suspicious elements required to determine a 'True Positive' verdict.
- `CriticalElement`: You can select a specific element that, if identified as suspicious, will automatically set the final verdict as true positive. The following options are available:IP ReputationRel
- `UserEngagementThreshold`: The threshold number of suspicious elements that will trigger a user engagement. Set 0 to disable user engagement.NOTICE: If this threshold is equal to or higher than "FinalThresho
- `Hostname`: RDP connection destination hostname.
- `EndpointID`: RDP connection destination endpoint ID.
- `Country`: Source external IP country.
- `IsolateEndpoint`: Set this value to "true" to enable endpoint isolation in case of a true positive.

**Dependencies:**

- Sub-playbooks: Block Indicators - Generic v3, Threat Hunting - Generic, Get entity alerts by MITRE tactics, TIM - Indicator Relationships Analysis, Endpoint Enrichment - Generic v2.1, Possible External RDP Brute-Force - Set Verdict, Account Enrichment - Generic v2.1, User Investigation - Generic
- Integrations: CoreIOCs, CortexCoreIR
- Scripts: Set, IsIntegrationAvailable
- Commands: core-isolate-endpoint, ip, ad-expire-password, setIncident

