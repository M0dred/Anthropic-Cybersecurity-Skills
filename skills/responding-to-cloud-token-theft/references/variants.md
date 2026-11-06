# Vendor Variants - Responding To Cloud Token Theft

Vendor-specific implementations, feeds, and collectors for this procedure.


## Cortex XDR - XCloud Token Theft Response

**Product:** Cloud Incident Response

**Kind:** playbook

**Inputs:**

- `alert_id`: The alert ID.
- `InternalRange`: A comma-separated list of internal IP ranges to check IP addresses against. The list should be provided in CIDR notation.
- `ResolveIP`: Determines whether to convert the IP address to a hostname using a DNS query (True/ False).
- `earlyContainment`: Whether to execute early containment.This action allows you to respond rapidly but have higher probability for false positives.
- `VPNIPList`: This input can process two types of data:1. A comma-separated list of internal IPs assigned by the VPN provider using a XSIAM list or an hardcoded array.2. A link to an IP list whi
- `autoResourceRemediation`: Whether to execute the resource remediation automatically.
- `autoAccessKeyRemediation`: Whether to execute the access key remediation automatically.
- `autoUserRemediation`: Whether to execute the user remediation automatically.
- `autoBlockIndicators`: Whether to execute the indicators remediation automatically.
- `credentialsRemediationType`: The response playbook provides the following remediation actions using AWS, MSGraph Users, GCP and GSuite Admin:Reset: By entering "Reset" in the input, the playbook will execute p

**Dependencies:**

- Sub-playbooks: IP Enrichment - Generic v2, Entity Enrichment - Generic v3, Cortex XDR - XCloud Token Theft - Set Verdict, Cloud Enrichment - Generic, Cloud Credentials Rotation - Generic, Cloud Threat Hunting - Persistence, TIM - Indicator Relationships Analysis, Cloud Response - Generic
- Scripts: ParseHTMLIndicators
- Commands: xdr-update-incident, xdr-get-cloud-original-alerts, setIncident, closeInvestigation

## Cortex XDR - XCloud Token Theft Response

**Product:** Cloud Incident Response

**Kind:** playbook

**Inputs:**

- `alert_id`: The alert ID.
- `InternalRange`: A comma-separated list of internal IP ranges to check IP addresses against. The list should be provided in CIDR notation.
- `ResolveIP`: Determines whether to convert the IP address to a hostname using a DNS query (True/ False).
- `earlyContainment`: Whether to execute early containment.This action allows you to respond rapidly but have higher probability for false positives.
- `VPNIPList`: This input can process two types of data:1. A comma-separated list of internal IPs assigned by the VPN provider using a XSIAM list or an hardcoded array.2. A link to an IP list whi
- `autoResourceRemediation`: Whether to execute the resource remediation automatically.
- `autoAccessKeyRemediation`: Whether to execute the access key remediation automatically.
- `autoUserRemediation`: Whether to execute the user remediation automatically.
- `autoBlockIndicators`: Whether to execute the indicators remediation automatically.
- `credentialsRemediationType`: The response playbook provides the following remediation actions using AWS, MSGraph Users, GCP and GSuite Admin:Reset: By entering "Reset" in the input, the playbook will execute p

**Dependencies:**

- Sub-playbooks: IP Enrichment - Generic v2, Entity Enrichment - Generic v3, Cortex XDR - XCloud Token Theft - Set Verdict, Cloud Enrichment - Generic, Cloud Credentials Rotation - Generic, Cloud Threat Hunting - Persistence, TIM - Indicator Relationships Analysis, Cloud Response - Generic
- Scripts: ParseHTMLIndicators
- Commands: xdr-update-incident, xdr-get-cloud-original-alerts, setIncident, closeInvestigation

## Cortex XDR - XCloud Token Theft Response

**Product:** Cloud Incident Response

**Kind:** playbook

**Inputs:**

- `alert_id`: The alert ID.
- `InternalRange`: A comma-separated list of internal IP ranges to check IP addresses against. The list should be provided in CIDR notation.
- `ResolveIP`: Determines whether to convert the IP address to a hostname using a DNS query (True/ False).
- `earlyContainment`: Whether to execute early containment.This action allows you to respond rapidly but have higher probability for false positives.
- `VPNIPList`: This input can process two types of data:1. A comma-separated list of internal IPs assigned by the VPN provider using a XSIAM list or an hardcoded array.2. A link to an IP list whi
- `autoResourceRemediation`: Whether to execute the resource remediation automatically.
- `autoAccessKeyRemediation`: Whether to execute the access key remediation automatically.
- `autoUserRemediation`: Whether to execute the user remediation automatically.
- `autoBlockIndicators`: Whether to execute the indicators remediation automatically.
- `credentialsRemediationType`: The response playbook provides the following remediation actions using AWS, MSGraph Users, GCP and GSuite Admin:Reset: By entering "Reset" in the input, the playbook will execute p

**Dependencies:**

- Sub-playbooks: IP Enrichment - Generic v2, Entity Enrichment - Generic v3, Cortex XDR - XCloud Token Theft - Set Verdict, Cloud Enrichment - Generic, Cloud Credentials Rotation - Generic, Cloud Threat Hunting - Persistence, TIM - Indicator Relationships Analysis, Cloud Response - Generic
- Scripts: ParseHTMLIndicators
- Commands: xdr-update-incident, xdr-get-cloud-original-alerts, setIncident, closeInvestigation

