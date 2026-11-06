# Vendor Variants - Investigating Cloud Cryptojacking

Vendor-specific implementations, feeds, and collectors for this procedure.


## Cortex XDR - XCloud Cryptojacking

**Product:** Cloud Incident Response

**Kind:** playbook

Investigates a Cortex XDR incident containing a Cloud Cryptojacking related alert. The playbook supports AWS, Azure, and GCP and executes the following

**Inputs:**

- `SOCEmailAddress`: The SOC email address to use for the alert status notification.
- `requireAnalystReview`: Whether to require an analyst review after the alert remediation.
- `incident_id`: The incident ID.
- `alert_id`: The alert ID.
- `cloudProvider`: The cloud service provider involved.
- `ResolveIP`: Determines whether to convert the IP address to a hostname using a DNS query (True/ False).
- `InternalRange`: A list of internal IP ranges to check IP addresses against. For IP Enrichment - Generic v2 playbook.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `autoAccessKeyRemediation`: Whether to execute the user remediation flow automatically.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.

**Dependencies:**

- Sub-playbooks: Cortex XDR - XCloud Cryptojacking - Set Verdict, Cortex XDR - Cloud Enrichment, Cloud Credentials Rotation - Generic, Cloud Response - Generic
- Scripts: IncreaseIncidentSeverity
- Commands: send-mail, setIncident, xdr-get-cloud-original-alerts, xdr-update-incident, xdr-get-incident-extra-data, closeInvestigation

## Cortex XDR - XCloud Cryptojacking

**Product:** Cloud Incident Response

**Kind:** playbook

Investigates a Cortex XDR incident containing a Cloud Cryptojacking related alert. The playbook supports AWS, Azure, and GCP and executes the following

**Inputs:**

- `SOCEmailAddress`: The SOC email address to use for the alert status notification.
- `requireAnalystReview`: Whether to require an analyst review after the alert remediation.
- `incident_id`: The incident ID.
- `alert_id`: The alert ID.
- `cloudProvider`: The cloud service provider involved.
- `ResolveIP`: Determines whether to convert the IP address to a hostname using a DNS query (True/ False).
- `InternalRange`: A list of internal IP ranges to check IP addresses against. For IP Enrichment - Generic v2 playbook.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `autoAccessKeyRemediation`: Whether to execute the user remediation flow automatically.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.

**Dependencies:**

- Sub-playbooks: Cortex XDR - XCloud Cryptojacking - Set Verdict, Cortex XDR - Cloud Enrichment, Cloud Credentials Rotation - Generic, Cloud Response - Generic
- Scripts: IncreaseIncidentSeverity
- Commands: send-mail, setIncident, xdr-get-cloud-original-alerts, xdr-update-incident, xdr-get-incident-extra-data, closeInvestigation

## Cortex XDR - XCloud Cryptojacking

**Product:** Cloud Incident Response

**Kind:** playbook

Investigates a Cortex XDR incident containing a Cloud Cryptojacking related alert. The playbook supports AWS, Azure, and GCP and executes the following

**Inputs:**

- `SOCEmailAddress`: The SOC email address to use for the alert status notification.
- `requireAnalystReview`: Whether to require an analyst review after the alert remediation.
- `incident_id`: The incident ID.
- `alert_id`: The alert ID.
- `cloudProvider`: The cloud service provider involved.
- `ResolveIP`: Determines whether to convert the IP address to a hostname using a DNS query (True/ False).
- `InternalRange`: A list of internal IP ranges to check IP addresses against. For IP Enrichment - Generic v2 playbook.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `autoAccessKeyRemediation`: Whether to execute the user remediation flow automatically.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.

**Dependencies:**

- Sub-playbooks: Cortex XDR - XCloud Cryptojacking - Set Verdict, Cortex XDR - Cloud Enrichment, Cloud Credentials Rotation - Generic, Cloud Response - Generic
- Scripts: IncreaseIncidentSeverity
- Commands: send-mail, setIncident, xdr-get-cloud-original-alerts, xdr-update-incident, xdr-get-incident-extra-data, closeInvestigation

