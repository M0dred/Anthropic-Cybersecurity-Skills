# Vendor Variants - Enriching External Ip Addresses

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Vega Incident - External IP Enrichment - Generic

**Product:** Vega

Enriches incoming IP addresses using the 'IP Enrichment - External - Generic v2' sub-playbook and automatically posts the retrieved endpoint details back to the Vega incident as a comment

**Inputs:**

- `IP_Address`: The IP address(es) to enrich.

**Dependencies:**

- Sub-playbooks: IP Enrichment - External - Generic v2
- Integrations: Vega
- Scripts: IsIntegrationAvailable, Print
- Commands: vega-update-incident

## Vega Incident - External IP Enrichment - Generic

**Product:** Vega

Enriches incoming IP addresses using the 'IP Enrichment - External - Generic v2' sub-playbook and automatically posts the retrieved endpoint details back to the Vega incident as a comment

**Inputs:**

- `IP_Address`: The IP address(es) to enrich.

**Dependencies:**

- Sub-playbooks: IP Enrichment - External - Generic v2
- Integrations: Vega
- Scripts: IsIntegrationAvailable, Print
- Commands: vega-update-incident

## Vega Incident - External IP Enrichment - Generic

**Product:** Vega

Enriches incoming IP addresses using the 'IP Enrichment - External - Generic v2' sub-playbook and automatically posts the retrieved endpoint details back to the Vega incident as a comment

**Inputs:**

- `IP_Address`: The IP address(es) to enrich.

**Dependencies:**

- Sub-playbooks: IP Enrichment - External - Generic v2
- Integrations: Vega
- Scripts: IsIntegrationAvailable, Print
- Commands: vega-update-incident

## Vega Incident - External IP Enrichment - Generic

**Product:** Vega

Enriches incoming IP addresses using the 'IP Enrichment - External - Generic v2' sub-playbook and automatically posts the retrieved endpoint details back to the Vega incident as a comment

**Inputs:**

- `IP_Address`: The IP address(es) to enrich.

**Dependencies:**

- Sub-playbooks: IP Enrichment - External - Generic v2
- Integrations: Vega
- Scripts: IsIntegrationAvailable, Print
- Commands: vega-update-incident

## IP Enrichment - Generic v2

**Product:** Common Playbooks

**Kind:** playbook

Enrich IP addresses using one or more integrations. When executing this playbook through IP Enrichment - Generic v2, IP classification and resolution will be handled by the main playbook, improving performance

**Inputs:**

- `IP`: The IP address to enrich.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `ResolveIP`: Determines whether to convert the IP address to a hostname using a DNS query (True/ False).The default value is true.
- `UseReputationCommand`: Define if you would like to use the !IP command.Note: This input should be used whenever there is no auto-extract enabled in the investigation flow.Possible values: True / False.Th
- `extended_data`: Define whether you want the generic reputation command to return extended data (last_analysis_results).Possible values: True / False.The default value is false.
- `threat_model_association`: Define whether you wish to enhance generic reputation command to include additional information such as Threat Bulletins, Attack patterns, Actors, Campaigns, TTPs, vulnerabilities,
- `ExecutedFromParent`: Whether to execute common logic, like the classification of IP addresses to ranges and resolving, in the the main (IP Enrichment - Generic v2) enrichment playbook, instead of in th

**Dependencies:**

- Sub-playbooks: IP Enrichment - External - Generic v2, IP Enrichment - Internal - Generic v2
- Scripts: IPToHost, IsIPInRanges

## IP Enrichment - Generic v2

**Product:** Common Playbooks

**Kind:** playbook

Enrich IP addresses using one or more integrations. When executing this playbook through IP Enrichment - Generic v2, IP classification and resolution will be handled by the main playbook, improving performance

**Inputs:**

- `IP`: The IP address to enrich.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `ResolveIP`: Determines whether to convert the IP address to a hostname using a DNS query (True/ False).The default value is true.
- `UseReputationCommand`: Define if you would like to use the !IP command.Note: This input should be used whenever there is no auto-extract enabled in the investigation flow.Possible values: True / False.Th
- `extended_data`: Define whether you want the generic reputation command to return extended data (last_analysis_results).Possible values: True / False.The default value is false.
- `threat_model_association`: Define whether you wish to enhance generic reputation command to include additional information such as Threat Bulletins, Attack patterns, Actors, Campaigns, TTPs, vulnerabilities,
- `ExecutedFromParent`: Whether to execute common logic, like the classification of IP addresses to ranges and resolving, in the the main (IP Enrichment - Generic v2) enrichment playbook, instead of in th

**Dependencies:**

- Sub-playbooks: IP Enrichment - External - Generic v2, IP Enrichment - Internal - Generic v2
- Scripts: IPToHost, IsIPInRanges

## IP Enrichment - Generic v2

**Product:** Common Playbooks

**Kind:** playbook

Enrich IP addresses using one or more integrations. When executing this playbook through IP Enrichment - Generic v2, IP classification and resolution will be handled by the main playbook, improving performance

**Inputs:**

- `IP`: The IP address to enrich.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `ResolveIP`: Determines whether to convert the IP address to a hostname using a DNS query (True/ False).The default value is true.
- `UseReputationCommand`: Define if you would like to use the !IP command.Note: This input should be used whenever there is no auto-extract enabled in the investigation flow.Possible values: True / False.Th
- `extended_data`: Define whether you want the generic reputation command to return extended data (last_analysis_results).Possible values: True / False.The default value is false.
- `threat_model_association`: Define whether you wish to enhance generic reputation command to include additional information such as Threat Bulletins, Attack patterns, Actors, Campaigns, TTPs, vulnerabilities,
- `ExecutedFromParent`: Whether to execute common logic, like the classification of IP addresses to ranges and resolving, in the the main (IP Enrichment - Generic v2) enrichment playbook, instead of in th

**Dependencies:**

- Sub-playbooks: IP Enrichment - External - Generic v2, IP Enrichment - Internal - Generic v2
- Scripts: IPToHost, IsIPInRanges

