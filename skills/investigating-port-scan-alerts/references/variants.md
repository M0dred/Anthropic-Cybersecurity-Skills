# Vendor Variants - Investigating Port Scan Alerts

Vendor-specific implementations, feeds, and collectors for this procedure.


## Port Scan - External Source

**Product:** Port Scan

**Kind:** playbook

This playbook remediates port scans originating outside of the organization's network

**Inputs:**

- `BlockAttackerIP`: Whether attacking IPs should be automatically blocked using firewalls.
- `SourceExternalIPs`: The external IP address(es) that initiated the port scan.
- `BlockMaliciousDomains`: In the event that reverse IP lookup is performed, and a malicious domain is found, setting this to True will automatically block the malicious domains. If set to False, an analyst 
- `DBotScore`: All the DBotScores that were calculated, either automatically by auto-reputation or using specific tasks, when the incident was ingested. This is used to calculate the incident sev

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3, Indicator Pivoting - DomainTools Iris, Calculate Severity - Generic v2, Domain Enrichment - Generic v2
- Integrations: DomainTools
- Scripts: SetAndHandleEmpty
- Commands: reverseIP, setIncident

## Port Scan - Internal Source

**Product:** Port Scan

**Kind:** playbook

Remediates port scans originating within the network

**Inputs:**

- `BlockAttackerIP`: Whether attacking IPs should be automatically blocked using firewalls.
- `WhitelistedHostnames`: A list of hostnames that should not be isolated even if used in an attack.
- `IsolateEndpointIfCriticalIncident`: Whether to automatically isolate endpoints if the severity is critical and the endpoint is not on the WhitelistedHostnames input, or opt for manual user approval. True means isolat
- `RoleForEscalation`: The name of the the platform, in case of developments like lateral movement.
- `BlockMaliciousFiles`: Whether to automatically block malicious files involved with the incident across all endpoints in the organization.
- `InternalSourceIPs`: The internal IP address(es) that performed the port scan. In order to properly respond to internal scans, either this or the SourceHostnames input has to be filled with data.
- `SourceHostnames`: The source hostname(s) that performed the port scan. In order to properly respond to internal scans, either this or the InternalSourceIPs input has to be filled with data.
- `SourceUsernames`: The Active Directory username(s) that were used in the port scan attack.
- `InvolvedFileMD5`: MD5 hashes of files that were involved in the port scan incident.
- `InvolvedFileSHA1`: SHA1 hashes of files that were involved in the port scan incident.

**Dependencies:**

- Sub-playbooks: PANW - Hunting and threat detection by indicator type V2, Account Enrichment - Generic v2.1, Active Directory - Get User Manager Details, Calculate Severity - Generic v2, Block IP - Generic v3, Splunk Indicator Hunting, Block File - Generic v2, QRadar Indicator Hunting V2
- Scripts: SetAndHandleEmpty
- Commands: xdr-get-endpoints, setIncident

## Port Scan - External Source

**Product:** Port Scan

**Kind:** playbook

This playbook remediates port scans originating outside of the organization's network

**Inputs:**

- `BlockAttackerIP`: Whether attacking IPs should be automatically blocked using firewalls.
- `SourceExternalIPs`: The external IP address(es) that initiated the port scan.
- `BlockMaliciousDomains`: In the event that reverse IP lookup is performed, and a malicious domain is found, setting this to True will automatically block the malicious domains. If set to False, an analyst 
- `DBotScore`: All the DBotScores that were calculated, either automatically by auto-reputation or using specific tasks, when the incident was ingested. This is used to calculate the incident sev

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3, Indicator Pivoting - DomainTools Iris, Calculate Severity - Generic v2, Domain Enrichment - Generic v2
- Integrations: DomainTools
- Scripts: SetAndHandleEmpty
- Commands: reverseIP, setIncident

## Port Scan - Internal Source

**Product:** Port Scan

**Kind:** playbook

Remediates port scans originating within the network

**Inputs:**

- `BlockAttackerIP`: Whether attacking IPs should be automatically blocked using firewalls.
- `WhitelistedHostnames`: A list of hostnames that should not be isolated even if used in an attack.
- `IsolateEndpointIfCriticalIncident`: Whether to automatically isolate endpoints if the severity is critical and the endpoint is not on the WhitelistedHostnames input, or opt for manual user approval. True means isolat
- `RoleForEscalation`: The name of the the platform, in case of developments like lateral movement.
- `BlockMaliciousFiles`: Whether to automatically block malicious files involved with the incident across all endpoints in the organization.
- `InternalSourceIPs`: The internal IP address(es) that performed the port scan. In order to properly respond to internal scans, either this or the SourceHostnames input has to be filled with data.
- `SourceHostnames`: The source hostname(s) that performed the port scan. In order to properly respond to internal scans, either this or the InternalSourceIPs input has to be filled with data.
- `SourceUsernames`: The Active Directory username(s) that were used in the port scan attack.
- `InvolvedFileMD5`: MD5 hashes of files that were involved in the port scan incident.
- `InvolvedFileSHA1`: SHA1 hashes of files that were involved in the port scan incident.

**Dependencies:**

- Sub-playbooks: PANW - Hunting and threat detection by indicator type V2, Account Enrichment - Generic v2.1, Active Directory - Get User Manager Details, Calculate Severity - Generic v2, Block IP - Generic v3, Splunk Indicator Hunting, Block File - Generic v2, QRadar Indicator Hunting V2
- Scripts: SetAndHandleEmpty
- Commands: xdr-get-endpoints, setIncident

## Port Scan - External Source

**Product:** Port Scan

**Kind:** playbook

This playbook remediates port scans originating outside of the organization's network

**Inputs:**

- `BlockAttackerIP`: Whether attacking IPs should be automatically blocked using firewalls.
- `SourceExternalIPs`: The external IP address(es) that initiated the port scan.
- `BlockMaliciousDomains`: In the event that reverse IP lookup is performed, and a malicious domain is found, setting this to True will automatically block the malicious domains. If set to False, an analyst 
- `DBotScore`: All the DBotScores that were calculated, either automatically by auto-reputation or using specific tasks, when the incident was ingested. This is used to calculate the incident sev

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3, Indicator Pivoting - DomainTools Iris, Calculate Severity - Generic v2, Domain Enrichment - Generic v2
- Integrations: DomainTools
- Scripts: SetAndHandleEmpty
- Commands: reverseIP, setIncident

## Port Scan - Internal Source

**Product:** Port Scan

**Kind:** playbook

Remediates port scans originating within the network

**Inputs:**

- `BlockAttackerIP`: Whether attacking IPs should be automatically blocked using firewalls.
- `WhitelistedHostnames`: A list of hostnames that should not be isolated even if used in an attack.
- `IsolateEndpointIfCriticalIncident`: Whether to automatically isolate endpoints if the severity is critical and the endpoint is not on the WhitelistedHostnames input, or opt for manual user approval. True means isolat
- `RoleForEscalation`: The name of the the platform, in case of developments like lateral movement.
- `BlockMaliciousFiles`: Whether to automatically block malicious files involved with the incident across all endpoints in the organization.
- `InternalSourceIPs`: The internal IP address(es) that performed the port scan. In order to properly respond to internal scans, either this or the SourceHostnames input has to be filled with data.
- `SourceHostnames`: The source hostname(s) that performed the port scan. In order to properly respond to internal scans, either this or the InternalSourceIPs input has to be filled with data.
- `SourceUsernames`: The Active Directory username(s) that were used in the port scan attack.
- `InvolvedFileMD5`: MD5 hashes of files that were involved in the port scan incident.
- `InvolvedFileSHA1`: SHA1 hashes of files that were involved in the port scan incident.

**Dependencies:**

- Sub-playbooks: PANW - Hunting and threat detection by indicator type V2, Account Enrichment - Generic v2.1, Active Directory - Get User Manager Details, Calculate Severity - Generic v2, Block IP - Generic v3, Splunk Indicator Hunting, Block File - Generic v2, QRadar Indicator Hunting V2
- Scripts: SetAndHandleEmpty
- Commands: xdr-get-endpoints, setIncident

