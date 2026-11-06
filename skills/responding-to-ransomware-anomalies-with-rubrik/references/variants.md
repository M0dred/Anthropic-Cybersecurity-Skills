# Vendor Variants - Responding To Ransomware Anomalies With Rubrik

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Darkmon - Ransomware Mentions Watch

**Product:** Darkmon

Every 6 hours, polls ransomware mentions for the customer organisation. New entries open a critical 'Darkmon Ransomware Mention' incident and notify the CISO via Generic Notify

**Dependencies:**

- Sub-playbooks: Darkmon - Generic Notify
- Integrations: Darkmon
- Scripts: DarkmonCreateIncidents, DarkmonFilterUnseen
- Commands: dmontip-get-ransomware


## Kaseya VSA 0-day - REvil Ransomware Supply Chain Attack

**Product:** Rapid Breach Response

On July 2nd, Kaseya company has experienced an attack against the VSA (Virtual System/Server Administrator) product. Kaseya customers pointed out a ransomware outbreak in their environments. Further investigation revealed that REvil group exploited VSA zero-day vulnerabilities for authentication bypass and arbitrary command execution. This allowed the attacker to deploy ransomware on Kaseya customers' endpoints. This playbook should be trigger manually and includes the following tasks: More information: Kaseya Incident Overview & Technical Details Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `BlockIndicatorsAutomatically`: Whether to automatically block the indicators involved.
- `SplunkEarliestTime`: The earliest time for the Splunk search query.
- `SplunkLatestTime`: The latest time for the Splunk search query.
- `YaraRulesSource`: The source of the Yara rules
- `SigmaRulesSource`: The source of the Sigma rules
- `QRadarSearchTimeRange`: The time range for the QRadar search query.
- `SplunkAdvancedSearch4FilesandReg`: Search splunk for related REvil - Kaseya breach file names.
- `SplunkAdvancedSearch4PSCMD`: Search Splunk for related REvil - Kaseya breach Powershell behaviours.
- `SplunkAdvancedSearch4WebLog`: Search Splunk for related REvil - Kaseya breach web access logs activity.
- `EDLDomainBlocklist`: The name of the EDL Domain Block List.

**Dependencies:**

- Sub-playbooks: Post Intrusion Ransomware Investigation, Splunk Indicator Hunting, Block Indicators - Generic v2, Palo Alto Networks - Hunting And Threat Detection, Search Endpoints By Hash - Generic V2, QRadar Domain Indicators Hunting, Panorama Query Logs for Kaseya breach Threat IDs, QRadar Indicator Hunting V2
- Integrations: SplunkPy
- Scripts: ParseHTMLIndicators, http, SearchIncidentsV2, isError
- Commands: qradar-get-reference-by-name, splunk-search, setIndicators, expanse-get-issues, linkIncidents, qradar-create-reference-set-value, qradar-create-reference-set, closeInvestigation


## Ransomware Playbook - Manual

**Product:** Ransomware

Master playbook for ransomware incidents. This playbook is a manual playbook


## Post Intrusion Ransomware Investigation

**Product:** Ransomware

Provides the first step in the investigation of ransomware attacks. The playbook requires the ransom note and an example of an encrypted file (<1MB) to try to identify the ransomware and find a recovery tool via the online database. You will be guided with further investigation steps throughout the playbook, some of the key features are: Playbook settings and mapping: For the full operation of the playbook, the following data should be mapped to the relevant incident fields. Username - Usernames (common incident field) Hostname - Hostnames (common incident field)

**Inputs:**

- `AutoRemediation`: Determines whether to perform auto-isolation and remediation for the infected endpoint and indicators.Values:- True- False. This is the default.
- `NotificationEmail`: The email addresses to notify if there is a possibility of the malware spreading and infecting other endpoints.Can be a CSV list.
- `EmailBody`: The malware notification message content.
- `UserVerification`: Possible values: True/False. Whether to provide user verification for blocking IPs. False - No prompt will be displayed to the user.True - The server will ask the user for blocking
- `AutoBlockIndicators`: Possible values: True/False. Default: True.Should the given indicators be automatically blocked, or should the user be given the option to choose?If set to True - no prompt will ap

**Dependencies:**

- Sub-playbooks: Endpoint Enrichment - Generic v2.1, Active Directory Investigation, Extract Indicators From File - Generic v2, Detonate File - Generic, Isolate Endpoint - Generic, Account Enrichment - Generic v2.1, File Enrichment - File reputation, Block Indicators - Generic v3
- Integrations: Active Directory Query v2, Rasterize
- Scripts: ReadFile
- Commands: setIndicators, send-mail, relatedIncidents, setIncident, rasterize-email, ad-disable-account


## Ransomware Advanced Analysis

**Product:** Core

This playbook is responsible for detecting the ransomware type and searching for available decryptors. The playbook uses the ID-Ransomware service, which allows detecting the ransomware using multiple methods

**Dependencies:**

- Integrations: Rasterize
- Scripts: ReadFile
- Commands: rasterize-email, extractIndicators


## Ransomware Enrich and Contain

**Product:** Core

This playbook is responsible for ransomware alert data enrichment and response. The playbook executes the following

**Inputs:**

- `isolateRemoteAttacker`: Whether to isolate the remote attacker host.
- `isolateSimilarEndpoints`: Whether to isolate endpoints which has been detected with the alert IoCs.
- `FileSHA256`: The ransomware file SHA256.
- `detonateRansomFile`: Whether to detonate the ransomware file in sandbox, Set to True to enable file detonation and False to disable it.By default is set to True.

**Dependencies:**

- Sub-playbooks: WildFire - Detonate file v2, Containment Plan
- Integrations: CoreIOCs, CortexCoreIR
- Scripts: isError, SearchIncidentsV2
- Commands: extractIndicators, core-isolate-endpoint, core-retrieve-file-details, domain, file, ip, core-retrieve-files, url


## Ransomware Exposure - RiskSense

**Product:** RiskSense

The ransomware exposure playbook reveals an organization's exposure to the specific vulnerabilities that are being exploited to launch ransomware attacks

**Outputs:**

- `RiskSense.RansomwareCves`
- `RiskSense.RansomwareTrendingCves`
- `RiskSense.HostFinding`
- `RiskSense.Host`

**Dependencies:**

- Scripts: IsIntegrationAvailable, DisplayCVEChartScript, RiskSenseGetRansomewareCVEScript
- Commands: risksense-get-hosts


## Rubrik Fileset Ransomware Discovery - Rubrik Polaris

**Product:** Rubrik Security Cloud

This playbook performs IOC Scan on fileset object. It also creates tickets on ServiceNow using "ServiceNow v2" integration. Supported integrations

**Inputs:**

- `ClusterId`: Cluster ID of the incident.
- `ObjectId`: Object ID of the incident.

**Dependencies:**

- Sub-playbooks: Rubrik IOC Scan - Rubrik Polaris
- Integrations: RubrikPolaris, ServiceNow v2
- Scripts: Set, Print, http
- Commands: servicenow-add-comment, servicenow-update-ticket, servicenow-create-ticket

