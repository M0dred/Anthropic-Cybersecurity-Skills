# Vendor Variants - Enriching Incident Entities

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## ACTI Incident Enrichment

**Product:** Accenture CTI v2

**Inputs:**

- `ia_uuid`: Intelligence Alert unique ID.
- `ir_uuid`: Intelligence Report unique ID.
- `MalwareFamily_uuid`: Malware Family unique ID.
- `ThreatGroup_uuid`: Threat Group unique ID.
- `ThreatCampaign_uuid`: Threat Campaign unique ID.
- `ThreatActor_uuid`: Threat Actor unique ID.

**Dependencies:**

- Integrations: ACTI Indicator Query
- Commands: acti-get-fundamentals-by-uuid, acti-getThreatIntelReport


## ACTI Indicator Enrichment

**Product:** Accenture CTI v2

**Inputs:**

- `IP_Pre_Enrich`: The extracted IP.
- `Domain_Pre_Enrich`: The extracted Domain.
- `URL_Pre_Enrich`: The extracted URL.

**Outputs:**

- `IP`
- `DBotScore`
- `Domain`
- `URL`
- `intelligence_alerts`
- `intelligence_reports`

**Dependencies:**

- Integrations: ACTI Indicator Query
- Scripts: Exists
- Commands: ip, domain, url


## Armis Alert Enrichment

**Product:** Armis

Enrich Armis alerts with the devices in the context details

**Inputs:**

- `Armis_Device_Identifier`: Get the device ID that is associated with the alert.

**Outputs:**

- `Device ID`
- `Armis.Device.name`
- `Armis.Device.riskLevel`
- `Armis.Device.ipAddress`
- `Armis.Device.site`
- `Armis.Device.tags`

**Dependencies:**

- Integrations: Armis
- Commands: armis-search-devices


## ASM Issue Incident Response - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook initiates the response for ASM Issues in  when an incident is investigated. For medium, high, or critical severity, it creates a ServiceNow ticket using the "ServiceNow v2" integration; otherwise, the incident is assigned to an analyst. The ticket is enriched with GTI ASM Issue details, including entity name, status, confidence, tags, UUID, collection info, and other relevant incident information

**Inputs:**

- `issue_uid`: Collection ASM issue UID from incident.
- `incident_severity`: Collect incident severity from incident.
- `onCall`: Set to true to assign only the user that is currently on shift. Default is False.
- `severity_mapping`: Set the ASM Issue severity as per GTI platform.

**Dependencies:**

- Sub-playbooks: Create ServiceNow Ticket
- Scripts: AssignAnalystToIncident, DeleteContext, Print, SetAndHandleEmpty
- Commands: servicenow-update-ticket


## AWS - Enrichment

**Product:** AWS Enrichment and Remediation

Given the IP address this playbook enriches EC2 and IAM information

**Inputs:**

- `AwsIP`: AWS IP in alert
- `AWSAssumeRoleName`: If assuming roles for AWS, this is the name of the role to assume (should be the same for all organizations).
- `Indicator Query`: Indicators matching the indicator query will be used as playbook input.

**Outputs:**

- `AWS.EC2.Instances`
- `AWS.EC2.SecurityGroups`
- `AWSHierarchy`
- `AWS.SSM`

**Dependencies:**

- Integrations: AWS - EC2, AWS - System Manager
- Scripts: Set, AWSAccountHierarchy
- Commands: aws-ec2-describe-instances, aws-ec2-describe-security-groups, aws-ec2-describe-regions, aws-ec2-get-ipam-discovered-public-addresses, aws-ssm-inventory-entry-list, aws-ec2-describe-ipam-resource-discoveries


## Azure - Enrichment

**Product:** Azure Enrichment and Remediation

Given the IP address, this playbook enriches Azure Compute, Azure asset hierarchy path, IAM, and User information

**Inputs:**

- `AzureIP`: Azure IP in alert

**Outputs:**

- `Azure.Compute`
- `Azure.Network`
- `MSGraphIdentity.Role`
- `Account`
- `MSGraphUser`
- `AzureAssetHierarchy`

**Dependencies:**

- Integrations: Entra ID Identity And Access, Entra ID Users, Azure Compute v2, Azure Resource Graph
- Commands: azure-rg-query, azure-vm-get-public-ip-details, azure-vm-get-nic-details, azure-vm-get-instance-details, msgraph-identity-directory-roles-list, msgraph-identity-directory-role-members-list, msgraph-user-get


## Case Investigation - Google SecOps

**Product:** Google SecOps

This playbook investigates a Google SecOps case by retrieving the latest case information, related alerts, and their entities, and updating the case stage. It also calculates severity from IOC scores, updates the incident and case priority accordingly, creates entities in the case from the identified IOCs, and posts a summary comment on the case

**Inputs:**

- `case_id`: The ID of the case.Note: Use gcb-case-list command to retrieve case ID.
- `alert_limit`: Number of alerts to retrieve in the response. The maximum allowed size is 1000.
- `entity_limit`: Number of entities to retrieve in the response. The maximum allowed size is 1000.

**Dependencies:**

- Scripts: DeleteContext, GoogleSecOpsSyncCaseInformation, Set
- Commands: findIndicators, gcb-case-alert-entity-create, gcb-case-comment-create, gcb-case-priority-change, gcb-case-stage-change, setIncident


## ChronicleAsset Investigation - Chronicle

**Product:** Google SecOps

This playbook receives indicators from its parent playbook, performs enrichment and investigation for each one of them, provides an opportunity to isolate and block the hostname or IP address associated with the current indicator, and gives out a list of isolated and blocked entities. This playbook also lists the events fetched for the asset identifier information associated with the indicator

**Inputs:**

- `chronicleasset_value`: The value of the ChronicleAsset indicator.
- `chronicleasset_support_contact`: The support email address for the chronicle asset.
- `auto_block_entities`: Autoblock the detected suspicious IP Address(es). You can manually set this as 'Yes' or 'No' here or you can set it into a 'Chronicle Auto Block Entities' custom incident field.
- `skip_entity_isolation`: Skip the isolation of entities. You can manually set this as 'Yes' or 'No' here or you can set it into a 'Chronicle Skip Entity Isolation' custom incident field.

**Outputs:**

- `IsolatedEntities`
- `PotentiallyBlockedIPs`

**Dependencies:**

- Scripts: SixgillSearchIndicators, DeleteContext


## Cloud Response - AWS

**Product:** AWS Enrichment and Remediation

This playbook provides response actions to AWS. The following are available for execution automatically/manually

**Inputs:**

- `accessKeyRemediationType`: Choose the remediation type for the user's access key.Disable - for disabling the user's access key.Delete - for the user's access key deletion.
- `userRemediationType`: Choose the remediation type for the user involved.Delete - for the user deletion.Revoke - for revoking the user's credentials.
- `resourceRemediationType`: Choose the remediation type for the instances created.Stop - for stopping the instances.Terminate - for terminating the instances.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `autoAccessKeyRemediation`: Whether to execute the access key remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `resourceName`: The resource name to take action on.
- `region`: The resource's region.
- `username`: The username to take action on.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3
- Scripts: Set
- Commands: aws-iam-delete-login-profile, aws-iam-delete-user, aws-iam-update-access-key, aws-ec2-stop-instances, aws-iam-delete-access-key, aws-ec2-terminate-instances


## Cloud Response - Azure

**Product:** Azure Enrichment and Remediation

This playbook provides response actions to Azure. The following are available for execution automatically/manually

**Inputs:**

- `resourceRemediationType`: Choose the remediation type for the instances created.Poweroff - for shutting down the instances.Delete - for deleting the instances.
- `userRemediationType`: Choose the remediation type for the user involved.Disable - for disabling the user.Delete - for deleting the user.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `resourceName`: The resource name to take action on.
- `resourceGroup`: The resource group.
- `username`: The username to take action on.
- `sourceIP`: The source IP address of the attacker.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3
- Scripts: Set
- Commands: azure-vm-poweroff-instance, azure-vm-delete-instance, msgraph-user-delete, msgraph-user-account-disable


## Cloud Response - GCP

**Product:** GCP Enrichment and Remediation

This playbook provides response actions to GCP. The following are available for execution automatically/manually

**Inputs:**

- `accessKeyRemediationType`: Choose the remediation type for the user's access key.Disable - For disabling the user's access key.Delete - For deleting user's access key.
- `userRemediationType`: Choose the remediation type for the user involved.Delete - For deleting the user.Disable - For disabling the user.
- `resourceRemediationType`: Choose the remediation type for the instances created.Stop - For stopping the instances.Delete - For deleting the instances.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `autoAccessKeyRemediation`: Whether to execute the access key remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `resourceName`: The resource name to take action on.
- `resourceZone`: The resource's zone.
- `username`: The username to take action on.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3
- Scripts: Set
- Commands: gcp-iam-service-account-disable, gcp-iam-service-account-key-disable, gsuite-user-delete, gcp-compute-stop-instance, gcp-iam-service-account-delete, gcp-iam-service-account-key-delete, gcp-compute-delete-instance


## Code42 File Download

**Product:** Code42

This playbook downloads a file via Code42 by either MD5 or SHA256 hash

**Inputs:**

- `XFC ID`: XFC Event ID to search for
- `MD5`: MD5 hash to search for
- `SHA256`: SHA256 hash to search for
- `Filename`: The name of the file to save as.

**Outputs:**

- `File.Size`
- `File.SHA1`
- `File.SHA256`
- `File.Name`
- `File.SSDeep`
- `File.EntryID`
- `File.Info`
- `File.Type`
- `File.MD5`
- `File.Extension`

**Dependencies:**

- Integrations: Code42
- Commands: code42-download-file


## Codecov Breach - Bash Uploader

**Product:** Rapid Breach Response

This playbook includes the following tasks: More information: Codecov Security Notice

**Inputs:**

- `KnownRelatedIOCs`: Known related IOCs to the Codecov Bash Uploader breach to hunt.
- `CustomIOCs`: Add your own custom Codecov Bash Uploader breach IOCs to hunt.
- `EWSSearchQuery`: The EWS query to find the Codecov security notice email
- `EWSSearchQuery_Limit`: The limit of results to return from the search
- `Github_Code_Search_query`: Github query to search for Codecov bash uploader use.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.

**Dependencies:**

- Sub-playbooks: Splunk Indicator Hunting, Panorama search thread-ids in threat logs, QRadar Indicator Hunting V2, Palo Alto Networks - Hunting And Threat Detection
- Commands: extractIndicators, GitHub-search-code, ews-search-mailbox


## Cortex ASM - Active Directory Enrichment

**Product:** Cortex Attack Surface Management

Playbook to enriches Service ownership info in Azure and On-Prem Active Directory

**Inputs:**

- `serviceowner`: The service owner to enrich in Azure directory.

**Dependencies:**

- Integrations: Microsoft Graph User, Active Directory Query v2
- Scripts: Set, GridFieldSetup
- Commands: msgraph-user-get, ad-get-user


## Cortex ASM - AWS Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches AWS information relevant to ASM alerts

**Inputs:**

- `RemoteIP`: IP address of service
- `ASMRuleID`: Attack Surface Management Rule ID.
- `AWSAssumeRoleName`: If assuming roles for AWS, this is the name of the role to assume (should be the same for all organizations).

**Dependencies:**

- Sub-playbooks: AWS - Enrichment, AWS - Unclaimed S3 Bucket Validation
- Scripts: GridFieldSetup, Set
- Commands: setAlert


## Cortex ASM - Azure Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address, this playbook enriches Azure information relevant to ASM alerts

**Inputs:**

- `RemoteIP`: IP address of service.

**Dependencies:**

- Scripts: GetTime, GridFieldSetup


## Cortex ASM - CMDB Enrichment

**Product:** Cortex Attack Surface Management

This playbook will look up a CI in ServiceNow CMDB by IP

**Inputs:**

- `IP`: IP address to search in ServiceNow

**Dependencies:**

- Integrations: ServiceNow CMDB
- Commands: servicenow-cmdb-records-list, servicenow-cmdb-record-get-by-id


## Cortex ASM - GCP Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches GCP and Firewall information

**Inputs:**

- `RemoteIP`: IP address of service

**Dependencies:**

- Sub-playbooks: GCP - Enrichment
- Scripts: Set GridFieldSetup


## Cortex ASM - On Prem Enrichment

**Product:** Cortex Attack Surface Management

Given an IP address, port, and protocol of a service, this playbook enriches on-prem integrations to find the related firewall rule and other related information. Conditions

**Inputs:**

- `RemoteIP`: IP address of the service.
- `RemotePort`: Port number of the service.
- `RemoteProtocol`: Protocol of the service.

**Dependencies:**

- Integrations: Panorama
- Scripts: GridFieldSetup, Set
- Commands: pan-os-security-policy-match, pan-os-platform-get-device-groups, pan-os-list-rules, pan-os-show-device-version


## Cortex ASM - Rapid7 Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches Rapid7 InsightVM (Nexpose) information relevant to ASM alerts

**Inputs:**

- `IPAddress`: IP addresses to enrich.

**Dependencies:**

- Sub-playbooks: Rapid7 - Nexpose - Enrichment
- Scripts: GetTime, GridFieldSetup


## Cortex ASM - Splunk Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches information from Splunk results relevant to ASM alerts

**Inputs:**

- `IP`: Remote IP in an incident/alert.

**Dependencies:**

- Scripts: GetTime, GridFieldSetup
- Commands: splunk-search


## Cortex XDR - Endpoint Investigation

**Product:** Cortex XDR by Palo Alto Networks

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook handles all the endpoint investigation actions available with  , including the following tasks

**Inputs:**

- `HuntReconnaissanceTechniques`: Set to True to hunt for identified alerts with MITRE Reconnaissance techniques.
- `HuntInitialAccessTechniques`: Set to True to hunt for identified alerts with MITRE Access techniques.
- `HuntExecutionTechniques`: Set to True to hunt for identified alerts with MITRE Execution techniques.
- `HuntPersistenceTechniques`: Set to True to hunt for identified alerts with MITRE Persistence techniques.
- `HuntPrivilegeEscalationTechniques`: Set to True to hunt for identified alerts with MITRE Privilege Escalation techniques.
- `HuntDefenseEvasionTechniques`: Set to True to hunt for identified alerts with MITRE Defense Evasion techniques.
- `HuntDiscoveryTechniques`: Set to True to hunt for identified alerts with MITRE Discovery techniques.
- `HuntLateralMovementTechniques`: Set to True to hunt for identified alerts with MITRE Lateral Movement techniques.
- `HuntCollectionTechniques`: Set to True to hunt for MITRE Collection techniques identified alerts.
- `HuntCnCTechniques`: Set to True to hunt for identified alerts with MITRE Command and Control techniques.

**Outputs:**

- `PaloAltoNetworksXDR.Alert`
- `PaloAltoNetworksXDR.Alert.internal_id`
- `PaloAltoNetworksXDR.Alert.source_insert_ts`
- `PaloAltoNetworksXDR.Alert.alert_name`
- `PaloAltoNetworksXDR.Alert.severity`
- `PaloAltoNetworksXDR.Alert.alert_category`
- `PaloAltoNetworksXDR.Alert.alert_action_status`
- `PaloAltoNetworksXDR.Alert.alert_action_status_readable`
- `PaloAltoNetworksXDR.Alert.alert_description`
- `PaloAltoNetworksXDR.Alert.agent_ip_addresses`

**Dependencies:**

- Integrations: CortexXDRIR
- Commands: xdr-get-alerts


## Cortex XDR - Malware Investigation

**Product:** Cortex XDR by Palo Alto Networks

Investigates a  XDR incident containing internal malware alerts. The playbook: The playbook is used as a sub- playbook in ‘ XDR Incident Handling - v2’

**Inputs:**

- `xdr_alert_id`: Unique ID for the XDR alert.
- `host_ip`: Host IP involved in the alert.
- `file_name`: The name of the malicious file.
- `file_sha256`: SHA-256 hash of the file.
- `file_path`: Full Path of the file.
- `endpoint_id`: the endpoint_id

**Outputs:**

- `Joe.Analysis`
- `File`
- `File.Malicious`
- `DBotScore`
- `IP`
- `DBotScore.Malicious`
- `Sample`
- `InfoFile`
- `WildFire`
- `WildFire.Report`

**Dependencies:**

- Sub-playbooks: Cortex XDR - Retrieve File v2, Detonate File - Generic
- Integrations: Cortex XDR - IR
- Scripts: SetMultipleValues
- Commands: xdr-get-endpoints


## Cortex XDR - Port Scan - Adjusted

**Product:** Cortex XDR by Palo Alto Networks

The playbook investigates  XDR incidents involving port scan alerts. The playbook is designed to run as a sub-playbook of ‘ XDR Alerts Handling’. The playbook consists of the following procedures: This playbook supports the following  XDR alert names

**Inputs:**

- `InternalIPRanges`: A list of IP ranges to check the IP against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.0.0.0/8,192.168
- `Username`: The user name used for port scanning.
- `SrcIPAddress`: The source IP address from which the port scanning was initiated.
- `DstIPAddress`: Scanned destination IP address.
- `DstPort`: Scanned port numbers.
- `EarlyContainment`: Whether early containment should be allowed when the IP address is known to be malicious.Possible values:True/False. Default:True.
- `SrcHostname`: Source host name from which port scanning was initiated.
- `EndpointID`: Source endpoint ID from which port scanning was initiated.
- `Initiator_CMD`: The command used to initiate port scan activity.
- `Initiator_Process_SHA256`: Process SHA256 file hash initiated port scanning.

**Outputs:**

- `PortScan.BlockPorts`
- `PortScan.AttackerIPs`
- `PortScan.AttackerHostnames`
- `PortScan.AttackerUsername`
- `PortScan.FileArtifacts`
- `PortScan.LateralMovementFirstDatetime`
- `PortScan.PortScanFirstDatetime`

**Dependencies:**

- Sub-playbooks: Cortex XDR - Endpoint Investigation, Account Enrichment - Generic v2.1, Cortex XDR - Isolate Endpoint, TIM - Indicator Relationships Analysis, User Investigation - Generic, Command-Line Analysis, Block Indicators - Generic v3, File Enrichment - Generic v2
- Scripts: IsIPInRanges, GetTime, Set
- Commands: setIncident


## Cortex XDR - Port Scan

**Product:** Cortex XDR by Palo Alto Networks

Investigates a  XDR incident containing internal port scan alerts. The playbook

**Inputs:**

- `BlockAttackerIP`: Whether attacking IPs should be automatically blocked using firewalls.
- `WhitelistedHostnames`: A list of comma-separated hostnames that should not be isolated even if used in an attack.
- `EmailAddressesToNotify`: A list of comma-separated values of email addresses that should receive a notification about compromised hosts.
- `CriticalUsernames`: A list of comma-separated names of critical users in the organization. This will affect the calculated severity of the incident.
- `IsolateEndpointAutomatically`: Whether to automatically isolate endpoints, or opt for manual user approval. True means isolation will be done automatically.
- `InternalIPRanges`: A list of IP ranges to check the IP against. The list should be provided in CIDR notation, separated by commas. An example of a list of ranges would be: "172.16.0.0/12,10.0.0.0/8,1
- `CriticalHostnames`: A list of comma-separated names of critical endpoints in the organization. This will affect the calculated severity of the incident.
- `RoleForEscalation`: The name of the the platform.
- `BlockMaliciousFiles`: Whether to automatically block malicious files involved with the incident across all endpoints in the organization.
- `CriticalADGroups`: CSV of DN names of critical Active Directory groups. This will affect the severity calculated for this incident.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3, IP Enrichment - Internal - Generic v2, Block File - Generic v2, Isolate Endpoint - Generic V2, Calculate Severity - Generic v2, PANW - Hunting and threat detection by indicator type V2
- Integrations: CortexXDRIR
- Scripts: AssignAnalystToIncident, IsIPInRanges, StopScheduledTask, SetAndHandleEmpty, XDRSyncScript
- Commands: closeInvestigation, xdr-get-endpoints, xdr-update-incident, send-mail, setIncident


## Cortex XDR - PrintNightmare Detection and Response

**Product:** Cortex XDR by Palo Alto Networks

The playbook targets specific PrintNightmare rules written by  XDR for both vulnerabilities: CVE-2021-1675 LPE CVE-2021-34527 RCE This playbook includes the following tasks: ** Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `IsolateEndpointAutomatically`: Whether to isolate the endpoint automatically
- `DisableAccountAutomatically`: Whether to disable the account automatically
- `BlockIPAutomatically`: Whether to block the IP Address automatically
- `EnrichAutomatically`: Whether to run indicators auto enrichment automatically
- `UserVerification`: Possible values: True/False.Whether to provide user verification for blocking IPs. False - No prompt will be displayed to the user.True - The server will ask the user for blocking 

**Dependencies:**

- Sub-playbooks: Account Enrichment - Generic v2.1, Endpoint Enrichment - Generic v2.1, Cortex XDR - Isolate Endpoint, Block IP - Generic v3, Threat Hunting - Generic
- Integrations: CortexXDRIR
- Scripts: SearchIncidentsV2
- Commands: ad-disable-account, enrichIndicators, xdr-get-incident-extra-data


## Cortex XDR device control violations

**Product:** Cortex XDR by Palo Alto Networks

Queries  XDR for device control violations for the specified hosts, IP address, or XDR endpoint ID. It then communicates via email with the involved users to understand the nature of the incident and if the user connected the device. All the collected data will be displayed in the XDR device control incident layout. This playbook can also be associated with  XDR device control violation job to periodically query and investigate XDR device control violations. In this configuration, the playbook will only communicate with the involved users

**Inputs:**

- `TimeStamp`: Timestamp in relative date format for query device control eventsfrom Cortex XDR.For example "1 day", "3 weeks".
- `EndpointID`: Comma-separated list of endpoint IDs to filter results for.
- `Hostname`: Comma-separated list of hostnames to filter results for.
- `IPAddress`: Comma-separated list of endpoints IP addresses to filter results for.
- `MessageSubject`: The subject of the message for communication with the involved users.
- `MessageBody`: A body of the message for communication with the involved users.

**Dependencies:**

- Integrations: CortexXDRIR
- Scripts: Set, SetGridField
- Commands: ad-get-user, xdr-get-endpoint-device-control-violations


## Cortex XDR Malware - Incident Enrichment

**Product:** Cortex XDR by Palo Alto Networks

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook enriches the  XDR incident. The enrichment is done on the involved endpoint and Mitre technique ID information, and sets the 'Malware-Investigation and Response' layout

**Inputs:**

- `IncidentID`: The incident ID to be enriched.

**Outputs:**

- `PaloAltoNetworksXDR.Incident`
- `File`
- `Process`
- `IP`
- `Domain`
- `Endpoint.ID`
- `Endpoint.Hostname`
- `Endpoint.OS`
- `Endpoint.OSVersion`
- `Endpoint.IPAddress`

**Dependencies:**

- Sub-playbooks: Mitre Attack - Extract Technique Information From ID, Account Enrichment - Generic v2.1
- Integrations: Cortex XDR - IR, CortexXDRIR
- Scripts: isError, SetGridField
- Commands: extractIndicators, endpoint, xdr-get-incident-extra-data, setIncident


## CrowdStrike Falcon Malware - Incident Enrichment

**Product:** CrowdStrike Falcon

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook enables enriching CrowdStrike Falcon incidents by pivoting to their detections as well as mapping all the relevant data to the   incident fields

**Inputs:**

- `DetectionOrCaseID`: The ID of the CrowdStrike detection or Case.

**Outputs:**

- `CrowdStrike`
- `Endpoint`
- `CrowdStrike.FoundDetections`

**Dependencies:**

- Sub-playbooks: Account Enrichment - Generic v2.1, CrowdStrike Falcon - Get Detections by Case
- Integrations: CrowdstrikeFalcon
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty, SetGridField, SetMultipleValues, isError
- Commands: endpoint, extractIndicators, setIncident


## CVE-2021-34527 | CVE-2021-1675 - PrintNightmare

**Product:** Rapid Breach Response

The playbook can be triggered manually or automatically by setting up a reoccurring job. Microsoft has released a security update in June 2021 Patch Tuesday for CVE-2021-1675, a Local Privilege Escalation vulnerability in the Print Spooler Service. Later that month, researchers found another method to exploit the Print Spooler service remotely, which raised the severity of the vulnerability due to the fact that the new method allows Remote Code Execution, a new ID was given to the critical vulnerability - CVE-2021-34527. Microsoft patched the vulnerability in June but an exploit POC and complete technical analysis were made publicly available online. **Update 7.8.2021 - Microsoft has released an emergency patch for the PrintNightmare. A reference for the patch can be found in "Install Microsoft spooler service patches" task. This playbook includes the following tasks: More details on the vulnerabilities: CVE-2021-1675 LPE CVE-2021-34527 RCE ** Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `CVE`: PrintNightmare CVEs
- `SplunkEarliestTime`: The earliest time for the Splunk search query.
- `SplunkLatestTime`: The latest time for the Splunk search query.

**Dependencies:**

- Sub-playbooks: Cortex XDR - PrintNightmare Detection and Response, QRadarFullSearch, Search Endpoint by CVE - Generic, Panorama Query Logs
- Commands: closeInvestigation, splunk-search


## CVE-2021-22893 - Pulse Connect Secure RCE

**Product:** Rapid Breach Response

On April 20th, a new Remote Code Execution vulnerability in Pulse Connect Secure was disclosed. The reference number for the vulnerability is CVE-2021-22893 with the CVSS Score of 10.0. This playbook should be trigger manually and includes the following tasks: Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve. More information: Exploitation of Pulse Connect Secure Vulnerabilities

**Inputs:**

- `Related_Hashes`: The known hashes of different malware families associated with the exploitation.
- `Related_CVEs`: The known CVEs associated with the exploitation.
- `BlockAutomatically`: Whether to block the indicators automatically.Default: False.
- `QRadarWebshellsQuery`: The QRadar search query used for "Hunt Activity Using QRadar".Please note that there aren't specified fields which may cause a longer run time.
- `SplunkWebshellsQuery`: The Splunk search query used for "Hunt Activity Using Splunk".Please note that there are two specified fields: msg, message. the query will work for both field names.
- `RunWebshellsQuery`: If you would like to skip "Hunt Activity Using Splunk" OR "Hunt Activity Using Qradar" please change the value to 'False'.
- `QRadar_MD5_Field`: The name of the field for MD5 entries in QRadar.If not configured, QRadar Indicator Hunting may reach timeout.
- `QRadar_SHA1_Field`: The name of the field for SHA1 entries in QRadar.If not configured, QRadar Indicator Hunting may reach timeout.
- `QRadar_SHA256_Field`: The name of the field for SHA256 entries in QRadar.If not configured, QRadar Indicator Hunting may reach timeout.
- `SplunkEarliestTime`: The earliest time for the Splunk search query.

**Dependencies:**

- Sub-playbooks: QRadar Indicator Hunting V2, QRadarFullSearch, Search Endpoint by CVE - Generic, Palo Alto Networks - Hunting And Threat Detection, Block Indicators - Generic v2, Splunk Indicator Hunting
- Commands: expanse-get-issues, enrichIndicators, splunk-search, extractIndicators


## CVE Exposure - RiskSense

**Product:** RiskSense

Block IPs and apply the tag to assets that are vulnerable to specified CVE

**Inputs:**

- `CVES`: Specify Common Vulnerabilities and Exposures (CVE). You can mention multiple CVEs using a comma-separated list.
- `TagName`: Tags in RiskSense can be applied to assets, web applications, and vulnerabilities. Tags are useful in the soft grouping, workflow creation, and to identify compliance-related asset

**Outputs:**

- `RiskSense.TagAssociation`
- `RiskSense.HostFinding`
- `RiskSense.Host`

**Dependencies:**

- Sub-playbooks: Block IP - Generic v2
- Integrations: RiskSense
- Scripts: IsIntegrationAvailable
- Commands: risksense-apply-tag, risksense-get-hosts, risksense-get-host-findings


## Cybereason - Download Close File

**Product:** Cybereason

This playbook aborts a file download operation which is in progress based on the Malop ID and username provided

**Inputs:**

- `malopGUID, userName`: Malop GUID for fetching a file from a sonsor to download, The complete Cybereason user name string for the user performing the request

**Dependencies:**

- Commands: cybereason-start-fetchfile, cybereason-fetchfile-progress, cybereason-close-file-batch-id


## Darkfeed - malware download from feed

**Product:** Sixgill Darkfeed - Annual Subscription

**Inputs:**

- `Indicator Query`: Indicators matching the indicator query will be used as playbook input

**Dependencies:**

- Sub-playbooks: Darkfeed IOC detonation and proactive blocking
- Scripts: SetAndHandleEmpty


## Darkmon - Compromised Account Response

**Product:** Darkmon

Incident-type playbook for 'Darkmon Compromised Credential' (and similar). Identifies the user via the configured directory, suspends, forces a password reset, revokes active sessions, and notifies SOC + the user

**Dependencies:**

- Sub-playbooks: Disable account, Force password reset, Notify SOC + user, Revoke active sessions


## Darkmon - EDR Alert Enrichment

**Product:** Darkmon

Designed to be invoked from CrowdStrike / SentinelOne / Defender alert playbooks. Takes the alert's IOCs, enriches each via Darkmon, and if any are scored Bad, escalates incident severity and notifies the SOC. Endpoint containment is left to the EDR-specific playbook

**Outputs:**

- `DBotScore`

**Dependencies:**

- Sub-playbooks: Enrich IOCs via Darkmon (URL pass), Notify SOC
- Scripts: Set


## Darkmon - Phishing Email Triage

**Product:** Darkmon

Extracts URLs/IPs/file-hashes from a reported phishing email, enriches each via the Darkmon - Enrich * sub-playbooks, and if any indicator is scored Bad (DBotScore=3) calls Generic Block Indicator on it. Notifies the reporter and the SOC at the end

**Outputs:**

- `ExtractedIndicators`
- `DBotScore`

**Dependencies:**

- Sub-playbooks: Block malicious indicators, Enrich each IOC via Darkmon, Notify SOC, Notify reporter
- Scripts: ExtractIndicatorsFromTextFile


## Digital Shadows - CVE_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of CVE IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_CVE`: A Digital Shadows ShadowSearch query containing CVE IDs

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## Digital Shadows - Domain_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of Domain IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_Domain`: A Digital Shadows ShadowSearch query containing domains

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## Digital Shadows - IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrich indicators by providing intelligence and more associated indicators based on confirmed reporting in Digital Shadows SearchLight

**Inputs:**

- `IoC_IP`: An IP address for assessment and enrichment
- `IoC_CVE`: A CVE for assessment and enrichment
- `IoC_Domain`: A domain for assessment and enrichment
- `IoC_URL`: A URL for assessment and enrichment
- `IoC_MD5`: A MD5 hash for assessment and enrichment
- `IoC_SHA256`: A SHA256 hash for assessment and enrichment
- `IoC_SHA1`: A SHA1 hash for assessment and enrichment

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Sub-playbooks: Digital Shadows - CVE_IoC Assessment & Enrichment, Digital Shadows - URL_IoC Assessment & Enrichment, Digital Shadows - SHA1_IoC Assessment & Enrichment, Digital Shadows - MD5_IoC Assessment & Enrichment, Digital Shadows - IP_IoC Assessment & Enrichment, Digital Shadows - SHA256_IoC Assessment & Enrichment, Digital Shadows - Domain_IoC Assessment & Enrichment


## Digital Shadows - IP_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of IP IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_IP`: A Digital Shadows ShadowSearch query containing IP addresses

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## Digital Shadows - MD5_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of MD5 IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_MD5`: A Digital Shadows ShadowSearch query containing MD5 hashes

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: AddEvidence, Print
- Commands: ds-search


## Digital Shadows - SHA1_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of SHA1 IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_SHA1`: A Digital Shadows ShadowSearch query containing SHA1 hashes

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: AddEvidence, Print
- Commands: ds-search


## Digital Shadows - SHA256_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of SHA256 IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_SHA256`: A Digital Shadows ShadowSearch query containing SHA256 hashes

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: AddEvidence, Print
- Commands: ds-search


## Digital Shadows - URL_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of URL IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_URL`: A Digital Shadows ShadowSearch query containing URLs

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## DTM Alert Incident Response - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook initiates the response for DTM Alerts in  when an incident is investigated. For medium or higher severity, it creates a ServiceNow ticket using the "ServiceNow v2" integration; otherwise, the incident is assigned to an analyst. The ticket is enriched with GTI DTM Alert details, including alert type, status, monitor information, summary, AI Doc summary, and tags

**Inputs:**

- `alert_id`: Collection DTM Alert ID from incident.
- `incident_severity`: Collect incident severity from incident.
- `onCall`: Set to true to assign only the user that is currently on shift. Default is False.
- `severity_mapping`: Set the alert severity mapping as per GTI platform.

**Dependencies:**

- Sub-playbooks: Create ServiceNow Ticket
- Scripts: AssignAnalystToIncident, DeleteContext, Print, SetAndHandleEmpty
- Commands: servicenow-update-ticket


## Endpoint Investigation Plan

**Product:** Common Playbooks

This playbook handles all the endpoint investigation actions by performing the following tasks on every alert associated with the incident: Note: The playbook inputs enable manipulating the execution flow; read the input descriptions for details

**Inputs:**

- `HuntReconnaissanceTechniques`: Set to True to hunt for identified alerts with MITRE Reconnaissance techniques.
- `HuntInitialAccessTechniques`: Set to True to hunt for identified alerts with MITRE Access techniques.
- `HuntExecutionTechniques`: Set to True to hunt for identified alerts with MITRE Execution techniques.
- `HuntPersistenceTechniques`: Set to True to hunt for identified alerts with MITRE Persistence techniques.
- `HuntPrivilegeEscalationTechniques`: Set to True to hunt for identified alerts with MITRE Privilege Escalation techniques.
- `HuntDefenseEvasionTechniques`: Set to True to hunt for identified alerts with MITRE Defense Evasion techniques.
- `HuntDiscoveryTechniques`: Set to True to hunt for identified alerts with MITRE Discovery techniques.
- `HuntLateralMovementTechniques`: Set to True to hunt for identified alerts with MITRE Lateral Movement techniques.
- `HuntCollectionTechniques`: Set to True to hunt for MITRE Collection techniques identified alerts.
- `HuntCnCTechniques`: Set to True to hunt for identified alerts with MITRE Command and Control techniques.

**Dependencies:**

- Scripts: SearchIncidentsV2


## File Private Scanning - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook submits a file for private scanning, retrieves and evaluates the analysis verdict, and automatically creates a ServiceNow ticket using the "ServiceNow v2" integration when the file is determined to be malicious

**Inputs:**

- `file_id`: Fetch the Entry ID of the last submitted file from the incident.

**Dependencies:**

- Sub-playbooks: Create ServiceNow Ticket
- Scripts: DeleteContext, Print
- Commands: gti-private-file-scan-and-analysis-get, servicenow-update-ticket


## GCP - Enrichment

**Product:** GCP Enrichment and Remediation

Given the IP address this playbook enriches GCP and Firewall information

**Inputs:**

- `GcpIP`: GCP IP in alert
- `port`: Port to match traffic on for firewall rules.
- `protocol`: Protocol to match traffic on for firewall rules.

**Outputs:**

- `GoogleCloudCompute.Instances`
- `GCPIAM.Policy`
- `GCPIAM.TagBindings`
- `GCPHierarchy`
- `GCPOffendingFirewallRule`

**Dependencies:**

- Integrations: GCP-IAM, Google Cloud Compute
- Scripts: GCPOffendingFirewallRule, Set, GCPProjectHierarchy
- Commands: gcp-iam-tagbindings-list, gcp-iam-project-iam-policy-get, gcp-compute-aggregated-list-instances-by-ip, gcp-compute-get-instance


## Get entity alerts by MITRE tactics

**Product:** Core

This playbook searches XDR alerts related to specific entities, on a given timeframe, based on MITRE tactics. Note: The playbook's inputs enable manipulating the execution flow. Read the input descriptions for details

**Inputs:**

- `HuntReconnaissanceTechniques`: Set to True to hunt for identified alerts with MITRE Reconnaissance techniques.
- `HuntInitialAccessTechniques`: Set to True to hunt for identified alerts with MITRE Initial Access techniques.
- `HuntExecutionTechniques`: Set to True to hunt for identified alerts with MITRE Execution techniques.
- `HuntPersistenceTechniques`: Set to True to hunt for identified alerts with MITRE Persistence techniques.
- `HuntPrivilegeEscalationTechniques`: Set to True to hunt for identified alerts with MITRE Privilege Escalation techniques.
- `HuntDefenseEvasionTechniques`: Set to True to hunt for identified alerts with MITRE Defense Evasion techniques.
- `HuntDiscoveryTechniques`: Set to True to hunt for identified alerts with MITRE Discovery techniques.
- `HuntLateralMovementTechniques`: Set to True to hunt for identified alerts with MITRE Lateral Movement techniques.
- `HuntCollectionTechniques`: Set to True to hunt for identified alerts with MITRE Collection techniques .
- `HuntCnCTechniques`: Set to True to hunt for identified alerts with MITRE Command and Control techniques.

**Outputs:**

- `foundIncidents`

**Dependencies:**

- Scripts: SearchAlertsV2, SetAndHandleEmpty


## Hunt Extracted Hashes V2

**Product:** Hunting

This playbook extracts IOCs from the incident details and attached files using regular expressions and then hunts for hashes on endpoints in the organization using available tools. The playbook supports multiple types of attachments. For the full supported attachments list, refer to "Extract Indicators From File - Generic v2"

**Inputs:**

- `File`: The file from which to extract indicators.

**Dependencies:**

- Sub-playbooks: Extract Indicators From File - Generic v2, Search Endpoints By Hash - Generic V2
- Commands: extractIndicators


## Incident Enrichment - XM Cyber

**Product:** XM Cyber

This playbook enriches the incident using the hostname indicators and user data and increases the severity based on the calculated risk score and pushes breach points of the identified entities to XM Cyber

**Inputs:**

- `entity_values`: Specify the hostname or user entity. Supports comma separated values.
- `compromise_risk_score`: Specify the weight of Compromise Risk Score to apply to the final score calculation. Provide the value between 0 and 1.
- `choke_point_score`: Specify the weight of Choke Point Score to apply to the final score calculation. Provide the value between 0 and 1.
- `attribute_name`: The name of the custom label you want to push to CEM as an imported attribute.
- `parameter`: When setting up the condition for when to push the breach point data, this is the parameter of the condition. It is a list of predefined parameters for determining the criteria. Se
- `operator`: When setting up the condition for when to push the breach point data, this is the operator of the condition.Possible values are: Less than, Greater than, Less than equal to, Greate
- `value`: When setting up the condition for when to push the breach point data, this is the value of the condition. Can be boolean, string, integer, float, or date values.Supported date form

**Dependencies:**

- Scripts: DeleteContext, Set
- Commands: findIndicators, setIncident, xmcyber-calculate-risk-score, xmcyber-enrich-incident, xmcyber-push-breach-point, xmcyber-remove-breach-point


## Investigate On Bad Domain Matches - Chronicle

**Product:** Google SecOps

Use this playbook to investigate and remediate Bad IOC domain matches with recent activity found in the enterprise, as well as notify the SOC lead and network team about the matches. Supported Integrations

**Inputs:**

- `networkteam_email`: Enter the email address of the network team that needs to be notified.
- `stakeholder_email`: Enter the email of the stakeholder to whom you want to send the investigation summary report.

**Dependencies:**

- Integrations: Chronicle, Google SecOps, Whois, Mail Sender (New), Palo Alto Networks PAN-OS, Palo Alto Networks AutoFocus v2
- Scripts: AssignAnalystToIncident, GenerateInvestigationSummaryReport, Print
- Commands: domain, gcb-assets, gcb-ioc-details, pan-os-register-user-tag, send-mail, whois


## IOCs Curated Threat Intelligence Enrichment - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook extracts IOCs from incident details and enriches the selected IOCs with curated Google Threat Intelligence data, including malware families, campaigns, and threat actors

**Dependencies:**

- Sub-playbooks: IOC Curated Enrichment - Google Threat Intelligence
- Scripts: DeleteContext
- Commands: findIndicators


## IOC Alert

**Product:** Core

IOCs provide the ability to alert on known malicious objects on endpoints across the organization. Analysis Actions: The playbook will use several enrichment sources to determine the IOC verdict. Additionally, will use the Analytics module to run a prevalence check for the IOC. Response Actions: The playbook's first response action is a containment plan that is based on the playbook input. In that phase, the playbook will execute endpoint isolation Investigative Actions: When the playbook executes, it checks for additional abnormal activity using the Endpoint Investigation Plan playbook that can indicate the endpoint might be compromised. Remediation Actions: In case results are found within the investigation phase, the playbook will execute remediation actions that include containment and eradication. This phase will execute the following containment actions: And the following eradication actions

**Inputs:**

- `BlockIndicatorsAutomatically`: Whether to block suspicious/malicious indicators automatically. Specify True/False.
- `ShouldCloseAutomatically`: Whether to close the alert automatically if it's established verdict is False Positive. Specify True/False.
- `PreHostContainment`: Whether to isolate the host before the investigation phase in case an IOC was found to be suspicious. Specify True/False.
- `ShouldHandleFPautomatically`: Whether to automatically handle false positive alerts. Specify true/false.
- `AutoRestoreEndpoint`: Whether to execute the Recovery playbook. Specify True/False.
- `AutoContainment`: Setting this input will impact both Containment Plan sub-playbooks. Without setting this input, the default values are True for the first occurrence and False for the second.Whethe
- `FileRemediation`: Should be either 'Quarantine' or 'Delete'.
- `AutoEradication`: Whether to execute automatically or manually the eradication plan tasks:* Terminate process* Delete file* Reset the user's passwordSpecify True/False.
- `ShouldOpenTicket`: Whether to open a ticket automatically in a ticketing system. (True/False).
- `serviceNowShortDescription`: A short description of the ticket.

**Dependencies:**

- Sub-playbooks: Endpoint Investigation Plan, Recovery Plan, Eradication Plan, Enrichment for Verdict, Handle False Positive Alerts, Ticket Management - Generic, Containment Plan
- Commands: extractIndicators, setParentIncidentFields, closeInvestigation


## IOC Curated Enrichment - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook provides IOC curated enrichment using Google Threat Intelligence data, including malware families, campaigns, and threat actors, and displays the results in the War Room for investigation

**Inputs:**

- `resource`: The file hash (MD5, SHA1, or SHA256), Domain, URL or IP.
- `resource_type`: The type of the resource (IP, domain, URL, or file hash).

**Dependencies:**

- Scripts: DeleteContext, Print, SetAndHandleEmpty
- Commands: gti-curated-campaigns-get, gti-curated-malware-families-get, gti-curated-threat-actors-get


## IOC Enrichment and Blocking - Google SecOps

**Product:** Google SecOps

This playbook enriches IOCs using the enrichment commands (IP, Email, Domain, URL, and File) and blocks the malicious IOCs based on DBot Score

**Dependencies:**

- Sub-playbooks: Block Domain - Generic v2, Block Email - Generic v2, Block File - Generic v2, Block IP - Generic v3, Block URL - Generic v2
- Scripts: DeleteContext, SetAndHandleEmpty
- Commands: domain, email, file, findIndicators, ip, url


## IOC Enrichment and Blocking - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook enriches IOCs using the GTI enrichment commands (IP, Domain, URL, and File) and blocks the IOCs based on GTI assessment parameters such as Threat Score, Severity, and Verdict

**Inputs:**

- `ip_addresses`: Provide a comma-separated list of IPs.
- `domains`: Provide a comma-separated list of Domains.
- `files`: Provide a comma-separated list of Files.
- `urls`: Provide a comma-separated list of URLs.

**Dependencies:**

- Sub-playbooks: Block Domain - Generic v2, Block File - Generic v2, Block IP - Generic v3, Block URL - Generic v2
- Scripts: DeleteContext, Set
- Commands: domain, file, findIndicators, ip, url


## Large Upload Alert

**Product:** Core

The playbook investigates  XDR alerts involving large upload alerts. The playbook consists of the following procedures

**Inputs:**

- `InternalIPRanges`: A list of IP ranges to check the IP against. The list should be provided in CIDR notation, separated by commas. An example of a list of ranges would be: "172.16.0.0/12,10.0.0.0/8,1
- `FurtherInvestigation`: Determines whether an alert should be further investigated if similar previous false positive alerts were found.Possible values:True/False. Default: False.
- `AutoBlockIndicators`: Determine whether the given indicators be automatically blocked, or if the user should be given the option to choose.Possible values:True/False. Default: True.If set to True - no p
- `BlockIndicators_UserVerification`: Determine whether the blocking of any indicator requires the verification of the user.Possible values:True/False. Default: False.
- `EarlyContainment`: Whether early containment should be allowed when the IP address is known to be malicious.Possible values:True/False. Default: True.
- `AutoIsolateEndpoint`: Whether to isolate the initiating endpoint automatically if the investigation verdict is malicious.Possible values:True/False. Default: False.
- `Transferred_Data _Threshold`: Specify the uploaded data threshold volume (in MB) from which large upload alerts should be investigated.By setting a threshold, you will be able to determine which large upload al
- `FWApps_Processes_Whitlist`: A list of known and authorized FW application IDs and processes used in the organization.
- `Alert_ID`: The Cortex XDR alert ID.

**Dependencies:**

- Sub-playbooks: Block Indicators - Generic v3, User Investigation - Generic, TIM - Indicator Relationships Analysis, Command-Line Analysis, Threat Hunting - Generic, Entity Enrichment - Generic v3, Endpoint Investigation Plan, Search and Compare Process Executions - Generic
- Integrations: CortexCoreIR
- Scripts: DBotFindSimilarIncidents, SetAndHandleEmpty, Set
- Commands: setAlertStatus, core-isolate-endpoint, setAlert, core-get-cloud-original-alerts


## Malware Investigation & Response Incident Handler

**Product:** Malware Investigation and Response

This playbook is triggered by a malware incident from an endpoint integration. It performs enrichment, detonation, and hunting within the organization, and remediation on the malware. The playbook also covers the SIEM ingestion flow in which the fetching integration is the SIEM and EDR integrations grab all additional data. Currently supported EDR integrations are XDR, CrowdStrike Falcon, and Microsoft Defender for Endpoint. Currently supported SIEM integrations are QRadar and Splunk

**Inputs:**

- `OnCall`: Define whether to assign OnCall to this flow.Possible values: True/False.Leave it empty if you do want not to assign an analyst to the incident.
- `EnableDeduplication`: Whether the deduplication playbook will be used.
- `DedupLimit`: The maximum number of incidents to query and set to context data.
- `DedupCloseSimilar`: "Defines the threshold of similarity to close a similar incident. All similar incidents with similarity above this value will be closed.For example, if CloseSimilar is set to .8 an
- `DedupHandleSimilar`: "This input defines how to handle Similar incidents. You may choose between: ""Link"", ""Close"", ""Link and Close"".Note: that closing incidents will require you to define ""Close
- `SIEMEDRProductToUse`: For EDR alerts routed through a SIEM, provide the supported originating EDR. Possible values: CrowdStrike, XDR, or Microsoft Defender.
- `EnableClosureSteps`: When closing an incident, whether to use closure steps to close automatically.
- `TicketProjectName`: For ticketing systems such as Jira a project name is required.
- `OverrideSIEMSeverity`: Whether to set the severity according to the ScaleToSetSeverity and SeverityValuesMapping settings (True) or keep the original severity as mapped by the SIEM (False).
- `SIEMincidentFieldForID`: The name of the field that provides the external ID of the alert or incident in the EDR.

**Dependencies:**

- Sub-playbooks: Cortex XDR Malware - Investigation And Response, MDE Malware - Investigation and Response, Malware SIEM Ingestion - Get Incident Data, CrowdStrike Falcon Malware - Investigation and Response
- Scripts: SetMultipleValues, Set, AssignAnalystToIncident


## Malware Investigation and Response - Set Alerts Grid

**Product:** Malware Investigation and Response

This playbook sets the alert grid for the Malware Investigation & Response layout

**Inputs:**

- `AlertName`: The alert name.
- `HostName`: The host name.
- `FileName`: The file name.
- `ProcessID`: The process ID.
- `SHA256`: The SHA256 file hash.
- `CommandLine`: The command line.
- `ParentProcess`: The parent process.

**Dependencies:**

- Scripts: Set, SetGridField


## Malware Triage - ReversingLabs TitaniumCloud

**Product:** ReversingLabs TitaniumCloud

Provides the TitaniumCloud classification of a file hash, and takes remediation actions based on that classification

**Inputs:**

- `hash`: SHA1 hash of a file.
- `file`: The file itself.
- `EndpointIP`: IP address of the endpoint from which the indicator came.

**Outputs:**

- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `DBotScore.Score`
- `DBotScore.Type`
- `DBotScore.Indicator`
- `DBotScore.Vendor`
- `ReversingLabs.file_reputation`

**Dependencies:**

- Sub-playbooks: Isolate Endpoint
- Integrations: ReversingLabs TitaniumCloud v2
- Scripts: IncreaseIncidentSeverity
- Commands: setIndicator, setIncident, reversinglabs-titaniumcloud-file-upload, reversinglabs-titaniumcloud-get-sample-dynamic-analysis-results, reversinglabs-titaniumcloud-submit-sample-for-dynamic-analysis, reversinglabs-titaniumcloud-file-reputation


## MDE Malware - Incident Enrichment

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook enriches Microsoft Defender For Endpoint alerts. The enrichment is done on the involved endpoint and Mitre technique ID information, and it sets the 'Malware-Investigation and Response' layout

**Inputs:**

- `DidAlertOriginateFromSIEM`: Whether the incident is fetched through a SIEM product.
- `AlertID`: The Microsoft Defender For Endpoint alert ID.

**Outputs:**

- `MITREATTACK`
- `AttackPattern`
- `MicrosoftATP.Alert`
- `Endpoint`

**Dependencies:**

- Sub-playbooks: Mitre Attack - Extract Technique Information From ID, Account Enrichment - Generic v2.1
- Integrations: Microsoft365DefenderEventCollector, MicrosoftDefenderAdvancedThreatProtection
- Scripts: SetGridField, isError, SetAndHandleEmpty
- Commands: microsoft-atp-get-alert-by-id, setIncident, endpoint, extractIndicators, file


## Microsoft 365 Defender - Emails Indicators Hunt

**Product:** Microsoft 365 Defender

This playbook retrieves email data based on the "URLDomain", "SHA256" and "IPAddress" inputs. SHA256 - Emails with attachments matching the "SHA256" input are retrieved. URLDomain - If the "URLDomain" value is found as a substring of URL(s) in the body of the email, the email is retrieved. IPAddress - Emails with "SenderIPv4"/SenderIPv6" or URLs (in the body) matching the "IPAddress" input are retrieved

**Inputs:**

- `URLDomain`: Domain or URL to search within emails. Can be a single domain or URL or an array of domains or URLs to search. The search looks for the exact Domain or URL.
- `SHA256`: The SHA256 hash file or an array of hashes to search within emails.
- `IPAddress`: The source or destination IP address to search. Can be a single address or an array of IP addresses.
- `Timeout`: The time limit in seconds for the HTTP request to run. Default is 60.
- `SearchTimeframe`: Number of days past to search. Default is 7.
- `ResultsLimit`: Number of retrieved entries. Enter -1 for unlimited query. 50 is the default.
- `ListenerMailbox`: The mailbox of the listening integration. In case it is provided, the emails found in it will be ignored.

**Outputs:**

- `Microsoft365Defender.RetrievedEmails`
- `Microsoft365Defender.RetrievedEmails.InternetMessageId`
- `Microsoft365Defender.RetrievedEmails.SenderFromDomain`
- `Microsoft365Defender.RetrievedEmails.EmailDirection`
- `Microsoft365Defender.RetrievedEmails.DeliveryLocation`
- `Microsoft365Defender.RetrievedEmails.AuthenticationDetails`
- `Microsoft365Defender.RetrievedEmails.DeliveryAction`
- `Microsoft365Defender.RetrievedEmails.Subject`
- `Microsoft365Defender.RetrievedEmails.AttachmentCount`
- `Microsoft365Defender.RetrievedEmails.ThreatNames`

**Dependencies:**

- Integrations: Microsoft 365 Defender
- Scripts: Set, IsIntegrationAvailable, SetAndHandleEmpty
- Commands: microsoft-365-defender-advanced-hunting


## Microsoft Defender For Endpoint - Collect investigation package

**Product:** Microsoft Defender for Endpoint

This playbook simplifies retrieving investigation packages to   from supported machines (See  The playbook receives information about the target devices (host name, IP, and device ID), validates the devices exist, and retrieves the collection package from those machines into the   console. Note: This action may take time, the average package size is around ~15 MB

**Inputs:**

- `AutoCollectinvestigationPackege`: Choose True to skip user validation on retrieving the investigation pack within the provided assets.
- `Hostnames`: A comma-separated list of host names.
- `MachineIDs`: A comma-separated list of machine IDs.
- `IPs`: A comma-separated list of machine IPs.

**Outputs:**

- `MicrosoftATP.MachineAction`

**Dependencies:**

- Commands: endpoint, microsoft-atp-request-and-download-investigation-package


## Microsoft Office File Enrichment - Oletools

**Product:** Oletools

Oletools is a tool for analyzing Microsoft OLE2 files, such as Microsoft Office documents or Outlook messages, mainly for malware analysis, forensics, and debugging. This playbook will run run the "oleid" command on the files which are passed to to it as playbook inputs. In case any macros or external relationships were found, it will also run "olevba" and "oleobj" commands as well on the relevant files. oleid - Analyze OLE files to detect specific characteristics usually found in malicious files. oleobj - Extract embedded objects from OLE files. olevba - Extract and analyze VBA Macro source code from MS Office documents (OLE and OpenXML)

**Inputs:**

- `FileObject`: A list of file objects. Default is "File" key.
- `Decode`: Available values: "True" or "False". Default is "False"When this is set to "True", in case a macro was found within the file, it will output all the obfuscated strings with their d
- `NonSecretPassword`: Will be used to decrypt encrypted files. Encrypted files cannot be analyzed otherwise.Please note that this input is "Non Secret" because it will be visible as plain text.

**Outputs:**

- `Oletools.Oleid.ole_command_result`
- `Oletools.Oleid.file_name`
- `Oletools.Oleid.sha256`
- `Oletools.Oleid.ole_command_result.File_format`
- `Oletools.Oleid.ole_command_result.Container_format`
- `Oletools.Oleid.ole_command_result.Encrypted`
- `Oletools.Oleid.ole_command_result.VBA_Macros`
- `Oletools.Oleid.ole_command_result.XLM_Macros`
- `Oletools.Oleid.ole_command_result.External_Relationships`
- `Oletools.Oleid.ole_command_result.ObjectPool`

**Dependencies:**

- Scripts: Set, Oletools


## Palo Alto Networks BPA - Submit Scan

**Product:** MITRE ATT&CK - Courses of Action

This playbook accepts a list of BPA checks, triggers a job and returns the checks results

**Inputs:**

- `check_id`: A comma-separated list of the BPA IDs of the results to return.
- `check_name`: A comma-separated list of the name of the results to return.

**Outputs:**

- `PAN-OS-BPA.JobResults.JobID`
- `PAN-OS-BPA.JobResults.Checks.check_id`
- `PAN-OS-BPA.JobResults.Checks.check_name`
- `PAN-OS-BPA.JobResults.Checks.check_message`
- `PAN-OS-BPA.JobResults.Checks.check_passed`
- `BPA.Passed`
- `BPA.Failed`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: BPA
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable, DeleteContext
- Commands: pan-os-bpa-get-job-results, pan-os-bpa-submit-job


## PhishUp Mail Scanner

**Product:** PhishUp

Extracts URLs from mail body and checks URLs with PhishUp. Takes action based on PhishUp results

**Inputs:**

- `EmailBodyHtml`: Email Mail Body for extracting URLs. Default Value is "${incident.emailbodyhtml}"
- `ShouldPhishUpActionWork`: If you do not want actions such as deleting mail and moving to spam in PhishUp playbook, you should set the value False. Default value is True
- `GmailMessageID`: Identify mail for deleting and moving funcitons. Defaultly it comes from incident which is setted from PhishUp Gmail Mapper
- `GmailUserID`: Identify user for deleting and moving funcitons. Defaultly it comes from incident which is setted from PhishUp Gmail Mapper

**Outputs:**

- `PhishUp.Evaluation`

**Dependencies:**

- Integrations: PhishUp, Gmail
- Scripts: IncreaseIncidentSeverity
- Commands: closeInvestigation, phishup-get-chosen-action, url, extractIndicators, phishup-evaluate-response, gmail-delete-mail, gmail-move-mail


## Phishing Alerts Investigation

**Product:** PhishingAlerts

This playbook investigates and remediates potential phishing incidents produced by either an email security gateway or a SIEM product. It retrieves original email files from the email security gateway or email service provider and generates a response based on the initial severity, hunting results, and the existence of similar phishing incidents in . No action is taken without an initial approval given by the analyst using the playbook inputs

**Inputs:**

- `Role`: The default role to assign the incident to.
- `SearchAndDelete`: Whether to enable the "Search and Delete" capability.For a malicious email, the Search and Delete sub-playbook looks for other instances of the email and deletes them pending analy
- `BlockIndicators`: Whether to enable the "Block Indicators" capability.For a malicious email, the Block Indicators sub-playbook blocks all malicious indicators in the relevant integrations.
- `AuthenticateEmail`: Whether the authenticity of the email should be verified using SPF, DKIM, and DMARC.
- `OnCall`: Set to True to assign only to analysts on the current shift. Requires the platform.5 or later.
- `SearchAndDeleteIntegration`: Determines which product and playbook is used to search and delete the phishing email from user inboxes.Set this to "O365" to use the O365 - Security And Compliance - Search And De
- `O365DeleteType`: The method to delete emails using the O365 - Security And Compliance - Search And Delete playbook. Can be "Soft" (recoverable), or "Hard" (unrecoverable). Leave empty to decide man
- `O365ExchangeLocationExclusion`: The exchange location. Determines from where to search and delete emails searched using O365 playbooks. Use the value 'All' to search all mailboxes, use 'SingleMailbox' to search a
- `SOCEmailAddress`: The SOC email address to set if the playbook handles phishing alerts.
- `escalationRole`: The role to assign the incident to if the incident severity is critical.

**Dependencies:**

- Sub-playbooks: Process Email - Generic v2, Phishing Alerts - Check Severity, Detonate File - Generic, Extract Indicators From File - Generic v2, Email Headers Check - Generic, Threat Hunting - Generic, Search And Delete Emails - Generic v2, Block Indicators - Generic v3
- Scripts: SearchIncidentsV2
- Commands: linkIncidents, closeInvestigation


## Phishing Triage and Response - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook extracts email addresses from phishing alerts, enriches their associated domains using the GTI domain enrichment command, and evaluates the GTI Threat Score, severity, and verdict. Based on these enrichment results, the playbook automatically blocks the malicious or high-risk email addresses to prevent further compromise

**Inputs:**

- `email_addresses`: Provide a comma-separated list of email addresses.

**Dependencies:**

- Sub-playbooks: Block Email - Generic v2, Email Collection by Enriched Domain - Google Threat Intelligence
- Scripts: DeleteContext, SetAndHandleEmpty
- Commands: domain, findIndicators


## Powershell Payload Response

**Product:** Malware Lateral Movement Assessment and Response

The Powershell Payload Response playbook is designed to be used when file payload executions are detected from an endpoint machines Powershell and begins the remediation process

**Inputs:**

- `Endpoint ID`: ID of the endpoint in question.
- `Hostname`: Hostname of the endpoint in question.
- `Email`: Email attachment.
- `File`: Payload file that was executed.
- `File Path`: File Path of the Executed Payload.

**Dependencies:**

- Sub-playbooks: Process Email - Generic, Isolate Endpoint - Generic V2, Block File - Generic v2, Dedup - Generic v3, Detonate File - Generic
- Integrations: Carbon Black Defense, Carbon Black Enterprise EDR, ServiceNow v2, SplunkPy
- Scripts: AssignAnalystToIncident, IncreaseIncidentSeverity
- Commands: cb-eedr-device-background-scan, splunk-search, closeInvestigation, cbd-create-policy, servicenow-update-ticket, cb-eedr-device-unquarantine, servicenow-create-ticket


## Prisma Cloud Compute - Audit Alert Enrichment

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook. It does the following

**Inputs:**

- `Hostname`: The hostname to retrieve events for. Relevant only for audit events.
- `ImageName`: The image name to retrieve events for.
- `AuditAlertType`: The type of the audit alert. Will be used to determine whether to retrieve WAAS events or not.
- `BaseURL`: The base URL of the Prisma Cloud Compute Instance used to create a link back to the alerts for an image.
- `ConsoleLink`: The value of the alert's console link. Part of the original incident values.
- `AccountID`: The cloud account ID.
- `Namespace`: The namespace which will be used to search associated users with in the "Get Account Owner" playbook.

**Outputs:**

- `PrismaCloudCompute.ReportsImagesScan`
- `PrismaCloud.Users`
- `PrismaCloud.UserRoles`
- `PrismaCloud.UserRoles.associatedUsers`
- `PrismaCloudCompute.ReportHostScan`
- `PrismaCloudCompute.ReportHostScan.complianceIssues`
- `PrismaCloudCompute.ReportsImagesScan.complianceIssues`

**Dependencies:**

- Sub-playbooks: Prisma Cloud - Get Account Owner, Prisma Cloud Compute - Get Container Events
- Commands: prisma-cloud-compute-images-scan-list, prisma-cloud-compute-hosts-scan-list, setIncident


## Prisma Cloud Compute - Audit Alert Vulnerabilities Enrichment

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook. It creates CVE indicators based on image or host vulnerabilities

**Inputs:**

- `ImageVulnerabilities`: Image vulnerabilities that were retrieved.
- `HostVulnerabilities`: Host vulnerabilities that were retrieved.
- `CVEsIndicatorsSeverities`: A list of the image or host CVE severities that the playbook creates indicators from.Available options (not case sensitive):- Critical- High- Medium- Low- NegligibleDefault value: 

**Outputs:**

- `CVEReport`


## Prisma Cloud Compute - Container Forensics

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook. Gets the container profile and forensics

**Inputs:**

- `AuditAlertType`: The audit alert type.
- `Image`: Image name.
- `DefenderType`: The defender type.
- `AlertCluster`: The alert's cluster name.
- `Hostname`: The hostname.
- `ForensicLink`: This link exists in audit runtime incidents.

**Dependencies:**

- Commands: prisma-cloud-compute-profile-container-list, prisma-cloud-compute-profile-container-forensic-list


## Prisma Cloud Compute - Get Container Events

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook

**Inputs:**

- `hostname`: The hostname to retrieve events for. Relevant only for audit events.
- `ImageName`: The image name to retrieve events for.
- `AuditAlertType`: The type of the audit alert. Will be used to determine whether to retrieve WAAS events or not.

**Dependencies:**

- Commands: prisma-cloud-compute-runtime-container-audit-events-list, setIncident, prisma-cloud-compute-get-audit-firewall-container-alerts


## Rapid7 - Nexpose - Enrichment

**Product:** Rapid7 InsightVM

Given an IP address, this playbook searches Rapid7 Nexpose assets for an asset with the associated IP address to retrieve asset information and proceeds to return all associated tags with it

**Inputs:**

- `IP`: IP used to search for asset information and tags.

**Outputs:**

- `Nexpose.Asset`
- `Nexpose.AssetTag`

**Dependencies:**

- Commands: nexpose-get-asset-tags, nexpose-search-assets


## RDP Bitmap Cache - Detect and Hunt

**Product:** RDPCacheHunting

**Inputs:**

- `ShouldCollectRDPCache`: When set to True, will use XDR to get RDP cache files from the endpoints. When set to False will try and use existing cache files from context.
- `EndpointIDs`: A comma-separated list of endpoint ID's to retrieve cache files from.
- `FilePath`: The path of the file to retrieve or use wildcard for multiple files.For example:C:\the\path\to\cache_file.binC:\the\path\to\*
- `Hostname`: Hostname of the machine on which the file is located. For PS remote it can also be an IP address.
- `min_score`: StringSifter - Limit output to strings with score >= min-score.
- `limit`: StringSifter - Limit output to the top limit ranked strings.
- `similiarity_threshold`: StringSimilarity - The similarity threshold to show results for, a value between 0 < x >1.
- `QRadarTimeFrame`: The time frame for the QRadar hunting query.
- `SplunkEarliestTime`: The earliest time for the Splunk hunting query.
- `SplunkLatestTime`: The latest time for the Splunk hunting query,

**Dependencies:**

- Sub-playbooks: Retrieve File from Endpoint - Generic V3, Threat Hunting - Generic
- Scripts: Set, PreProcessImage, StringSimilarity, StringSifter, UnzipFile, SetGridField, BMCTool
- Commands: xdr-file-retrieve, lolbas-get-indicators, image-ocr-extract-text, rasterize-image, splunk-search, extractIndicators, rasterize-pdf, setIncident


## Recorded Future Entity Enrichment

**Product:** Recorded Future Intelligence

Template playbook to incorporate Recorded Future enrichment for IPs, Hashes, Domains, URLs into your current workflows. Playbook also shows how to look up available 'Links' data for IOCs

**Inputs:**

- `MD5`: File MD5 hash to enrich.
- `SHA256`: The file SHA256 hash to enrich.
- `SHA1`: The file SHA1 hash to enrich.
- `IP`: The IP Address to enrich.
- `Domain`: The Domain name to enrich.
- `URL`: The URL to enrich.

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`
- `DBotScore`
- `DBotScore.Vendor`
- `DBotScore.Score`

**Dependencies:**

- Integrations: Recorded Future v2
- Commands: recordedfuture-intelligence, recordedfuture-links


## Rubrik Turbo IOC Scan - Rubrik Polaris

**Product:** Rubrik Security Cloud

This playbook starts a Turbo IOC scan with the specified IOC values and shows the results upon completion

**Inputs:**

- `ioc`: The value of the indicator to scan for. Supports comma separated values.Note: Users can retrieve the Md5, SHA1 or SHA256 by executing the "rubrik-threat-monitoring-matched-file-get
- `scan_name`: Name of the new turbo threat hunt scan.
- `cluster_id`: The ID of the cluster on which to perform a scan. If not provided, all the clusters will be scanned.Note: Users can retrieve the list of the cluster IDs by executing the "rubrik-gp
- `start_time`: Filter the snapshots from the provided date. Any snapshots taken before the provided date-time will be excluded.Formats accepted: 2 minutes, 2 hours, 2 days, 2 weeks, 2 months, 2 y
- `end_time`: Filter the snapshots until the provided date. Any snapshots taken after the provided date-time will be excluded.Formats accepted: 2 minutes, 2 hours, 2 days, 2 weeks, 2 months, 2 y
- `max_snapshots_per_object`: Maximum number of snapshots to scan per object.
- `polling_interval`: Frequency that the IOC scan command will run (minutes).
- `polling_timeout`: Amount of time to poll before declaring a timeout and resuming the playbook (in minutes).

**Outputs:**

- `RubrikPolaris.IOCScan`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Scripts: DeleteContext
- Commands: rubrik-turbo-ioc-scan, rubrik-ioc-scan-results-v2


## SANS - Incident Handler's Handbook Template

**Product:** SANS

Contains the phases for handling an incident as they are described in the SANS Institute ‘Incident Handler's Handbook’ by Patrick Kral. ***Disclaimer: This playbook does not ensure compliance to SANS regulations


## Scan Assets - Nexpose

**Product:** Rapid7 InsightVM

Scans according to asset IP addresses or host names, and waits for the scan to finish by polling the scan status in pre-defined intervals

**Inputs:**

- `IPs`: The asset IP addresses to scan.
- `HostNames`: The hostnames of the assets to scan.
- `Name`: The scan name as specified by the user.

**Outputs:**

- `Nexpose.Scan.ScanType`
- `Nexpose.Scan.Completed`
- `Nexpose.Scan.StartedBy`
- `Nexpose.Scan.Assets`
- `Nexpose.Scan.TotalTime`
- `Nexpose.Scan.Id`
- `Nexpose.Scan.Status`
- `Nexpose.Scan.Vulnerabilities.Critical`
- `Nexpose.Scan.Vulnerabilities.Moderate`
- `Nexpose.Scan.Vulnerabilities.Severe`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: Rapid7 Nexpose
- Commands: nexpose-get-scan, nexpose-start-assets-scan


## Search And Delete Emails - EWS

**Product:** Microsoft Exchange On-Premise

Searches EWS to identify and delete emails with similar attributes of a malicious email

**Inputs:**

- `From`: The value of the malicious email's "From" attribute.
- `Subject`: The value of the malicious email's "Subject" attribute.
- `AttachmentName`: The value of the malicious email's AttachmentName attribute.
- `SearchThisWeek`: Limit the search to the current week. Can be "true" or "false".
- `Limit`: The maximum number of search results.
- `DeleteType`: The deletion type. Can be, "trash", "soft", or "hard".

**Dependencies:**

- Integrations: EWS v2
- Scripts: BuildEWSQuery
- Commands: ews-delete-items, ews-search-mailboxes


## Search And Delete Emails - Generic v2

**Product:** Common Playbooks

This playbook searches and deletes emails with similar attributes of a malicious email using one of the following integrations: EWS Microsoft Graph Security Gmail Agari Phishing Defense

**Inputs:**

- `From`: The value of the malicious email's "From" attribute.
- `Subject`: The value of the malicious email's "Subject" attribute.
- `AttachmentName`: The value of the malicious email's "AttachmentName" attribute.
- `SearchAndDeleteIntegration`: The integration in which to run the search and delete action. Can be MS Graph, Gmail, EWS, or Agari Phishing Defense.
- `SearchThisWeek`: Whether to limit the search to the current week. Disabling this may increase search scope, execution time, and risk of timeout for large mailboxes.
- `MsgCase`: Used only with Microsoft Graph Security. The eDiscovery case name to use. Looked up by name and created if missing.
- `MsgKQL`: Used only with Microsoft Graph Security. KQL query identifying the emails to search and delete. Built automatically from the From, Subject, and AttachmentName inputs if left empty.
- `MsgRecipients`: Used only with Microsoft Graph Security. CSV of recipient email addresses to scope the search when MsgMailboxScope is recipientsOnly.
- `MsgMailboxScope`: Used only with Microsoft Graph Security. Determines which mailboxes to search. Use recipientsOnly to limit to specific recipients, allTenantMailboxes to search the entire tenant.
- `MsgDeleteType`: Used only with Microsoft Graph Security. The delete type to perform on the search results. Possible values are Hard or Soft, or leave empty to select manually (Hard = unrecoverable

**Dependencies:**

- Sub-playbooks: Search And Delete Emails - Microsoft Graph Security, Search And Delete Emails - EWS, Search And Delete Emails - Gmail
- Integrations: Agari Phishing Defense
- Scripts: DeleteContext, GetTime, Set
- Commands: apd-remediate-message


## Social Engineering Domain Investigation

**Product:** Social Engineering Domain Analysis

Enrich and Investigate domains which may present a social engineering threat to your organization. Review before blocking potentially dangerous indicators

**Inputs:**

- `SocialEngineeringDomainList`: The CSV list of domains to test or array of domains
- `SocialEngineeringRegisteredDomain`: Your company domain
- `BadNameservers`: An the platform BadNameserver list. This should be a CSV list with a single column and the header of "nameserver"Example List Contents:nameserverbadnameserver1.combadnameserver2.com

**Dependencies:**

- Sub-playbooks: Social Engineering Domain Enrichment
- Scripts: ConvertTableToHTML
- Commands: setIndicator, extractIndicators


## URL Private Scanning - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook performs private URL scanning and analyses the URL based on GTI assessment parameters such as Threat Score, Verdict, and Severity. Based on these parameters, the playbook blocks the URL

**Inputs:**

- `url`: Provide a comma-separated list of URLs.

**Dependencies:**

- Sub-playbooks: Block URL - Generic v2, URL Scan - Google Threat Intelligence
- Scripts: DeleteContext
- Commands: findIndicators


## Xpanse - Alert Enrichment

**Product:** Cortex Xpanse

This playbook handles ASM alerts by enriching asset information via integrations with Cloud Service Providers and other IT and Security tools

**Dependencies:**

- Sub-playbooks: Azure - Enrichment, GCP - Enrichment, AWS - Enrichment


## Xpanse - Alert Self-Enrichment

**Product:** Cortex Xpanse

Enrichment on the alert itself using  Xpanse APIs

**Dependencies:**

- Integrations: Cortex Xpanse
- Scripts: GridFieldSetup, Set
- Commands: asm-get-asset-internet-exposure, asm-get-external-service, extractIndicators


## Zimperium Incident Enrichment

**Product:** Zimperium

Enriches Zimperium incidents

**Dependencies:**

- Integrations: Zimperium, Zimperium v2
- Scripts: IsIntegrationAvailable
- Commands: zimperium-users-search, zimperium-device-get-by-id, zimperium-devices-search


## CheckPDFEncryptionAndValidity

**Product:** Common Scripts

This script checks whether a given PDF file is valid and whether it is encrypted. The results are returned as fields in the file’s context. The script will not fail on invalid/ encrypted files. Instead, the error details will be captured and returned in the file’s context


## ExtractAttackPattern

**Product:** Common Scripts

Extract Attack Pattern Threat Intel Object. After auto extract extracts the Attack Pattern IDs, this script is executed and extracts the value (name) of the Attack Pattern

**Inputs:**

- `input`: A comma-separated list of Attack Pattern IDs.


## IsDomainInternal

**Product:** Common Scripts

The script takes one or more domain names and checks whether they're in the   list defined in the InternalDomainsListName argument. By default, the InternalDomainsListName argument will use the   list called "InternalDomains". The list can be customized by the user. It should contain the organization's internal domain names, separated by new lines. Subdomains are also supported in the list. The results of the script are tagged with the "Internal_Domain_Check_Results" tag, so they can be displayed in the War Room entry sections in incident layouts

**Inputs:**

- `InternalDomainsListName`: The name of the the platform. If no list is specified, the script will use the InternalDomains list by default.
- `Domains`: A domain name or a list of domain names to check for being internal or external, against the specified list of internal domains.

**Outputs:**

- `Domain.Name`
- `Domain.Internal`

## ACTI Incident Enrichment

**Product:** Accenture CTI v2

**Inputs:**

- `ia_uuid`: Intelligence Alert unique ID.
- `ir_uuid`: Intelligence Report unique ID.
- `MalwareFamily_uuid`: Malware Family unique ID.
- `ThreatGroup_uuid`: Threat Group unique ID.
- `ThreatCampaign_uuid`: Threat Campaign unique ID.
- `ThreatActor_uuid`: Threat Actor unique ID.

**Dependencies:**

- Integrations: ACTI Indicator Query
- Commands: acti-get-fundamentals-by-uuid, acti-getThreatIntelReport


## ACTI Indicator Enrichment

**Product:** Accenture CTI v2

**Inputs:**

- `IP_Pre_Enrich`: The extracted IP.
- `Domain_Pre_Enrich`: The extracted Domain.
- `URL_Pre_Enrich`: The extracted URL.

**Outputs:**

- `IP`
- `DBotScore`
- `Domain`
- `URL`
- `intelligence_alerts`
- `intelligence_reports`

**Dependencies:**

- Integrations: ACTI Indicator Query
- Scripts: Exists
- Commands: ip, domain, url


## Armis Alert Enrichment

**Product:** Armis

Enrich Armis alerts with the devices in the context details

**Inputs:**

- `Armis_Device_Identifier`: Get the device ID that is associated with the alert.

**Outputs:**

- `Device ID`
- `Armis.Device.name`
- `Armis.Device.riskLevel`
- `Armis.Device.ipAddress`
- `Armis.Device.site`
- `Armis.Device.tags`

**Dependencies:**

- Integrations: Armis
- Commands: armis-search-devices


## ASM Issue Incident Response - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook initiates the response for ASM Issues in  when an incident is investigated. For medium, high, or critical severity, it creates a ServiceNow ticket using the "ServiceNow v2" integration; otherwise, the incident is assigned to an analyst. The ticket is enriched with GTI ASM Issue details, including entity name, status, confidence, tags, UUID, collection info, and other relevant incident information

**Inputs:**

- `issue_uid`: Collection ASM issue UID from incident.
- `incident_severity`: Collect incident severity from incident.
- `onCall`: Set to true to assign only the user that is currently on shift. Default is False.
- `severity_mapping`: Set the ASM Issue severity as per GTI platform.

**Dependencies:**

- Sub-playbooks: Create ServiceNow Ticket
- Scripts: AssignAnalystToIncident, DeleteContext, Print, SetAndHandleEmpty
- Commands: servicenow-update-ticket


## AWS - Enrichment

**Product:** AWS Enrichment and Remediation

Given the IP address this playbook enriches EC2 and IAM information

**Inputs:**

- `AwsIP`: AWS IP in alert
- `AWSAssumeRoleName`: If assuming roles for AWS, this is the name of the role to assume (should be the same for all organizations).
- `Indicator Query`: Indicators matching the indicator query will be used as playbook input.

**Outputs:**

- `AWS.EC2.Instances`
- `AWS.EC2.SecurityGroups`
- `AWSHierarchy`
- `AWS.SSM`

**Dependencies:**

- Integrations: AWS - EC2, AWS - System Manager
- Scripts: Set, AWSAccountHierarchy
- Commands: aws-ec2-describe-instances, aws-ec2-describe-security-groups, aws-ec2-describe-regions, aws-ec2-get-ipam-discovered-public-addresses, aws-ssm-inventory-entry-list, aws-ec2-describe-ipam-resource-discoveries


## Azure - Enrichment

**Product:** Azure Enrichment and Remediation

Given the IP address, this playbook enriches Azure Compute, Azure asset hierarchy path, IAM, and User information

**Inputs:**

- `AzureIP`: Azure IP in alert

**Outputs:**

- `Azure.Compute`
- `Azure.Network`
- `MSGraphIdentity.Role`
- `Account`
- `MSGraphUser`
- `AzureAssetHierarchy`

**Dependencies:**

- Integrations: Entra ID Identity And Access, Entra ID Users, Azure Compute v2, Azure Resource Graph
- Commands: azure-rg-query, azure-vm-get-public-ip-details, azure-vm-get-nic-details, azure-vm-get-instance-details, msgraph-identity-directory-roles-list, msgraph-identity-directory-role-members-list, msgraph-user-get


## Case Investigation - Google SecOps

**Product:** Google SecOps

This playbook investigates a Google SecOps case by retrieving the latest case information, related alerts, and their entities, and updating the case stage. It also calculates severity from IOC scores, updates the incident and case priority accordingly, creates entities in the case from the identified IOCs, and posts a summary comment on the case

**Inputs:**

- `case_id`: The ID of the case.Note: Use gcb-case-list command to retrieve case ID.
- `alert_limit`: Number of alerts to retrieve in the response. The maximum allowed size is 1000.
- `entity_limit`: Number of entities to retrieve in the response. The maximum allowed size is 1000.

**Dependencies:**

- Scripts: DeleteContext, GoogleSecOpsSyncCaseInformation, Set
- Commands: findIndicators, gcb-case-alert-entity-create, gcb-case-comment-create, gcb-case-priority-change, gcb-case-stage-change, setIncident


## ChronicleAsset Investigation - Chronicle

**Product:** Google SecOps

This playbook receives indicators from its parent playbook, performs enrichment and investigation for each one of them, provides an opportunity to isolate and block the hostname or IP address associated with the current indicator, and gives out a list of isolated and blocked entities. This playbook also lists the events fetched for the asset identifier information associated with the indicator

**Inputs:**

- `chronicleasset_value`: The value of the ChronicleAsset indicator.
- `chronicleasset_support_contact`: The support email address for the chronicle asset.
- `auto_block_entities`: Autoblock the detected suspicious IP Address(es). You can manually set this as 'Yes' or 'No' here or you can set it into a 'Chronicle Auto Block Entities' custom incident field.
- `skip_entity_isolation`: Skip the isolation of entities. You can manually set this as 'Yes' or 'No' here or you can set it into a 'Chronicle Skip Entity Isolation' custom incident field.

**Outputs:**

- `IsolatedEntities`
- `PotentiallyBlockedIPs`

**Dependencies:**

- Scripts: SixgillSearchIndicators, DeleteContext


## Cloud Response - AWS

**Product:** AWS Enrichment and Remediation

This playbook provides response actions to AWS. The following are available for execution automatically/manually

**Inputs:**

- `accessKeyRemediationType`: Choose the remediation type for the user's access key.Disable - for disabling the user's access key.Delete - for the user's access key deletion.
- `userRemediationType`: Choose the remediation type for the user involved.Delete - for the user deletion.Revoke - for revoking the user's credentials.
- `resourceRemediationType`: Choose the remediation type for the instances created.Stop - for stopping the instances.Terminate - for terminating the instances.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `autoAccessKeyRemediation`: Whether to execute the access key remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `resourceName`: The resource name to take action on.
- `region`: The resource's region.
- `username`: The username to take action on.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3
- Scripts: Set
- Commands: aws-iam-delete-login-profile, aws-iam-delete-user, aws-iam-update-access-key, aws-ec2-stop-instances, aws-iam-delete-access-key, aws-ec2-terminate-instances


## Cloud Response - Azure

**Product:** Azure Enrichment and Remediation

This playbook provides response actions to Azure. The following are available for execution automatically/manually

**Inputs:**

- `resourceRemediationType`: Choose the remediation type for the instances created.Poweroff - for shutting down the instances.Delete - for deleting the instances.
- `userRemediationType`: Choose the remediation type for the user involved.Disable - for disabling the user.Delete - for deleting the user.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `resourceName`: The resource name to take action on.
- `resourceGroup`: The resource group.
- `username`: The username to take action on.
- `sourceIP`: The source IP address of the attacker.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3
- Scripts: Set
- Commands: azure-vm-poweroff-instance, azure-vm-delete-instance, msgraph-user-delete, msgraph-user-account-disable


## Cloud Response - GCP

**Product:** GCP Enrichment and Remediation

This playbook provides response actions to GCP. The following are available for execution automatically/manually

**Inputs:**

- `accessKeyRemediationType`: Choose the remediation type for the user's access key.Disable - For disabling the user's access key.Delete - For deleting user's access key.
- `userRemediationType`: Choose the remediation type for the user involved.Delete - For deleting the user.Disable - For disabling the user.
- `resourceRemediationType`: Choose the remediation type for the instances created.Stop - For stopping the instances.Delete - For deleting the instances.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `autoAccessKeyRemediation`: Whether to execute the access key remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `resourceName`: The resource name to take action on.
- `resourceZone`: The resource's zone.
- `username`: The username to take action on.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3
- Scripts: Set
- Commands: gcp-iam-service-account-disable, gcp-iam-service-account-key-disable, gsuite-user-delete, gcp-compute-stop-instance, gcp-iam-service-account-delete, gcp-iam-service-account-key-delete, gcp-compute-delete-instance


## Code42 File Download

**Product:** Code42

This playbook downloads a file via Code42 by either MD5 or SHA256 hash

**Inputs:**

- `XFC ID`: XFC Event ID to search for
- `MD5`: MD5 hash to search for
- `SHA256`: SHA256 hash to search for
- `Filename`: The name of the file to save as.

**Outputs:**

- `File.Size`
- `File.SHA1`
- `File.SHA256`
- `File.Name`
- `File.SSDeep`
- `File.EntryID`
- `File.Info`
- `File.Type`
- `File.MD5`
- `File.Extension`

**Dependencies:**

- Integrations: Code42
- Commands: code42-download-file


## Codecov Breach - Bash Uploader

**Product:** Rapid Breach Response

This playbook includes the following tasks: More information: Codecov Security Notice

**Inputs:**

- `KnownRelatedIOCs`: Known related IOCs to the Codecov Bash Uploader breach to hunt.
- `CustomIOCs`: Add your own custom Codecov Bash Uploader breach IOCs to hunt.
- `EWSSearchQuery`: The EWS query to find the Codecov security notice email
- `EWSSearchQuery_Limit`: The limit of results to return from the search
- `Github_Code_Search_query`: Github query to search for Codecov bash uploader use.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.

**Dependencies:**

- Sub-playbooks: Splunk Indicator Hunting, Panorama search thread-ids in threat logs, QRadar Indicator Hunting V2, Palo Alto Networks - Hunting And Threat Detection
- Commands: extractIndicators, GitHub-search-code, ews-search-mailbox


## Cortex ASM - Active Directory Enrichment

**Product:** Cortex Attack Surface Management

Playbook to enriches Service ownership info in Azure and On-Prem Active Directory

**Inputs:**

- `serviceowner`: The service owner to enrich in Azure directory.

**Dependencies:**

- Integrations: Microsoft Graph User, Active Directory Query v2
- Scripts: Set, GridFieldSetup
- Commands: msgraph-user-get, ad-get-user


## Cortex ASM - AWS Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches AWS information relevant to ASM alerts

**Inputs:**

- `RemoteIP`: IP address of service
- `ASMRuleID`: Attack Surface Management Rule ID.
- `AWSAssumeRoleName`: If assuming roles for AWS, this is the name of the role to assume (should be the same for all organizations).

**Dependencies:**

- Sub-playbooks: AWS - Enrichment, AWS - Unclaimed S3 Bucket Validation
- Scripts: GridFieldSetup, Set
- Commands: setAlert


## Cortex ASM - Azure Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address, this playbook enriches Azure information relevant to ASM alerts

**Inputs:**

- `RemoteIP`: IP address of service.

**Dependencies:**

- Scripts: GetTime, GridFieldSetup


## Cortex ASM - CMDB Enrichment

**Product:** Cortex Attack Surface Management

This playbook will look up a CI in ServiceNow CMDB by IP

**Inputs:**

- `IP`: IP address to search in ServiceNow

**Dependencies:**

- Integrations: ServiceNow CMDB
- Commands: servicenow-cmdb-records-list, servicenow-cmdb-record-get-by-id


## Cortex ASM - GCP Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches GCP and Firewall information

**Inputs:**

- `RemoteIP`: IP address of service

**Dependencies:**

- Sub-playbooks: GCP - Enrichment
- Scripts: Set GridFieldSetup


## Cortex ASM - On Prem Enrichment

**Product:** Cortex Attack Surface Management

Given an IP address, port, and protocol of a service, this playbook enriches on-prem integrations to find the related firewall rule and other related information. Conditions

**Inputs:**

- `RemoteIP`: IP address of the service.
- `RemotePort`: Port number of the service.
- `RemoteProtocol`: Protocol of the service.

**Dependencies:**

- Integrations: Panorama
- Scripts: GridFieldSetup, Set
- Commands: pan-os-security-policy-match, pan-os-platform-get-device-groups, pan-os-list-rules, pan-os-show-device-version


## Cortex ASM - Rapid7 Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches Rapid7 InsightVM (Nexpose) information relevant to ASM alerts

**Inputs:**

- `IPAddress`: IP addresses to enrich.

**Dependencies:**

- Sub-playbooks: Rapid7 - Nexpose - Enrichment
- Scripts: GetTime, GridFieldSetup


## Cortex ASM - Splunk Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches information from Splunk results relevant to ASM alerts

**Inputs:**

- `IP`: Remote IP in an incident/alert.

**Dependencies:**

- Scripts: GetTime, GridFieldSetup
- Commands: splunk-search


## Cortex XDR - Endpoint Investigation

**Product:** Cortex XDR by Palo Alto Networks

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook handles all the endpoint investigation actions available with  , including the following tasks

**Inputs:**

- `HuntReconnaissanceTechniques`: Set to True to hunt for identified alerts with MITRE Reconnaissance techniques.
- `HuntInitialAccessTechniques`: Set to True to hunt for identified alerts with MITRE Access techniques.
- `HuntExecutionTechniques`: Set to True to hunt for identified alerts with MITRE Execution techniques.
- `HuntPersistenceTechniques`: Set to True to hunt for identified alerts with MITRE Persistence techniques.
- `HuntPrivilegeEscalationTechniques`: Set to True to hunt for identified alerts with MITRE Privilege Escalation techniques.
- `HuntDefenseEvasionTechniques`: Set to True to hunt for identified alerts with MITRE Defense Evasion techniques.
- `HuntDiscoveryTechniques`: Set to True to hunt for identified alerts with MITRE Discovery techniques.
- `HuntLateralMovementTechniques`: Set to True to hunt for identified alerts with MITRE Lateral Movement techniques.
- `HuntCollectionTechniques`: Set to True to hunt for MITRE Collection techniques identified alerts.
- `HuntCnCTechniques`: Set to True to hunt for identified alerts with MITRE Command and Control techniques.

**Outputs:**

- `PaloAltoNetworksXDR.Alert`
- `PaloAltoNetworksXDR.Alert.internal_id`
- `PaloAltoNetworksXDR.Alert.source_insert_ts`
- `PaloAltoNetworksXDR.Alert.alert_name`
- `PaloAltoNetworksXDR.Alert.severity`
- `PaloAltoNetworksXDR.Alert.alert_category`
- `PaloAltoNetworksXDR.Alert.alert_action_status`
- `PaloAltoNetworksXDR.Alert.alert_action_status_readable`
- `PaloAltoNetworksXDR.Alert.alert_description`
- `PaloAltoNetworksXDR.Alert.agent_ip_addresses`

**Dependencies:**

- Integrations: CortexXDRIR
- Commands: xdr-get-alerts


## Cortex XDR - Malware Investigation

**Product:** Cortex XDR by Palo Alto Networks

Investigates a  XDR incident containing internal malware alerts. The playbook: The playbook is used as a sub- playbook in ‘ XDR Incident Handling - v2’

**Inputs:**

- `xdr_alert_id`: Unique ID for the XDR alert.
- `host_ip`: Host IP involved in the alert.
- `file_name`: The name of the malicious file.
- `file_sha256`: SHA-256 hash of the file.
- `file_path`: Full Path of the file.
- `endpoint_id`: the endpoint_id

**Outputs:**

- `Joe.Analysis`
- `File`
- `File.Malicious`
- `DBotScore`
- `IP`
- `DBotScore.Malicious`
- `Sample`
- `InfoFile`
- `WildFire`
- `WildFire.Report`

**Dependencies:**

- Sub-playbooks: Cortex XDR - Retrieve File v2, Detonate File - Generic
- Integrations: Cortex XDR - IR
- Scripts: SetMultipleValues
- Commands: xdr-get-endpoints


## Cortex XDR - Port Scan - Adjusted

**Product:** Cortex XDR by Palo Alto Networks

The playbook investigates  XDR incidents involving port scan alerts. The playbook is designed to run as a sub-playbook of ‘ XDR Alerts Handling’. The playbook consists of the following procedures: This playbook supports the following  XDR alert names

**Inputs:**

- `InternalIPRanges`: A list of IP ranges to check the IP against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.0.0.0/8,192.168
- `Username`: The user name used for port scanning.
- `SrcIPAddress`: The source IP address from which the port scanning was initiated.
- `DstIPAddress`: Scanned destination IP address.
- `DstPort`: Scanned port numbers.
- `EarlyContainment`: Whether early containment should be allowed when the IP address is known to be malicious.Possible values:True/False. Default:True.
- `SrcHostname`: Source host name from which port scanning was initiated.
- `EndpointID`: Source endpoint ID from which port scanning was initiated.
- `Initiator_CMD`: The command used to initiate port scan activity.
- `Initiator_Process_SHA256`: Process SHA256 file hash initiated port scanning.

**Outputs:**

- `PortScan.BlockPorts`
- `PortScan.AttackerIPs`
- `PortScan.AttackerHostnames`
- `PortScan.AttackerUsername`
- `PortScan.FileArtifacts`
- `PortScan.LateralMovementFirstDatetime`
- `PortScan.PortScanFirstDatetime`

**Dependencies:**

- Sub-playbooks: Cortex XDR - Endpoint Investigation, Account Enrichment - Generic v2.1, Cortex XDR - Isolate Endpoint, TIM - Indicator Relationships Analysis, User Investigation - Generic, Command-Line Analysis, Block Indicators - Generic v3, File Enrichment - Generic v2
- Scripts: IsIPInRanges, GetTime, Set
- Commands: setIncident


## Cortex XDR - Port Scan

**Product:** Cortex XDR by Palo Alto Networks

Investigates a  XDR incident containing internal port scan alerts. The playbook

**Inputs:**

- `BlockAttackerIP`: Whether attacking IPs should be automatically blocked using firewalls.
- `WhitelistedHostnames`: A list of comma-separated hostnames that should not be isolated even if used in an attack.
- `EmailAddressesToNotify`: A list of comma-separated values of email addresses that should receive a notification about compromised hosts.
- `CriticalUsernames`: A list of comma-separated names of critical users in the organization. This will affect the calculated severity of the incident.
- `IsolateEndpointAutomatically`: Whether to automatically isolate endpoints, or opt for manual user approval. True means isolation will be done automatically.
- `InternalIPRanges`: A list of IP ranges to check the IP against. The list should be provided in CIDR notation, separated by commas. An example of a list of ranges would be: "172.16.0.0/12,10.0.0.0/8,1
- `CriticalHostnames`: A list of comma-separated names of critical endpoints in the organization. This will affect the calculated severity of the incident.
- `RoleForEscalation`: The name of the the platform.
- `BlockMaliciousFiles`: Whether to automatically block malicious files involved with the incident across all endpoints in the organization.
- `CriticalADGroups`: CSV of DN names of critical Active Directory groups. This will affect the severity calculated for this incident.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3, IP Enrichment - Internal - Generic v2, Block File - Generic v2, Isolate Endpoint - Generic V2, Calculate Severity - Generic v2, PANW - Hunting and threat detection by indicator type V2
- Integrations: CortexXDRIR
- Scripts: AssignAnalystToIncident, IsIPInRanges, StopScheduledTask, SetAndHandleEmpty, XDRSyncScript
- Commands: closeInvestigation, xdr-get-endpoints, xdr-update-incident, send-mail, setIncident


## Cortex XDR - PrintNightmare Detection and Response

**Product:** Cortex XDR by Palo Alto Networks

The playbook targets specific PrintNightmare rules written by  XDR for both vulnerabilities: CVE-2021-1675 LPE CVE-2021-34527 RCE This playbook includes the following tasks: ** Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `IsolateEndpointAutomatically`: Whether to isolate the endpoint automatically
- `DisableAccountAutomatically`: Whether to disable the account automatically
- `BlockIPAutomatically`: Whether to block the IP Address automatically
- `EnrichAutomatically`: Whether to run indicators auto enrichment automatically
- `UserVerification`: Possible values: True/False.Whether to provide user verification for blocking IPs. False - No prompt will be displayed to the user.True - The server will ask the user for blocking 

**Dependencies:**

- Sub-playbooks: Account Enrichment - Generic v2.1, Endpoint Enrichment - Generic v2.1, Cortex XDR - Isolate Endpoint, Block IP - Generic v3, Threat Hunting - Generic
- Integrations: CortexXDRIR
- Scripts: SearchIncidentsV2
- Commands: ad-disable-account, enrichIndicators, xdr-get-incident-extra-data


## Cortex XDR device control violations

**Product:** Cortex XDR by Palo Alto Networks

Queries  XDR for device control violations for the specified hosts, IP address, or XDR endpoint ID. It then communicates via email with the involved users to understand the nature of the incident and if the user connected the device. All the collected data will be displayed in the XDR device control incident layout. This playbook can also be associated with  XDR device control violation job to periodically query and investigate XDR device control violations. In this configuration, the playbook will only communicate with the involved users

**Inputs:**

- `TimeStamp`: Timestamp in relative date format for query device control eventsfrom Cortex XDR.For example "1 day", "3 weeks".
- `EndpointID`: Comma-separated list of endpoint IDs to filter results for.
- `Hostname`: Comma-separated list of hostnames to filter results for.
- `IPAddress`: Comma-separated list of endpoints IP addresses to filter results for.
- `MessageSubject`: The subject of the message for communication with the involved users.
- `MessageBody`: A body of the message for communication with the involved users.

**Dependencies:**

- Integrations: CortexXDRIR
- Scripts: Set, SetGridField
- Commands: ad-get-user, xdr-get-endpoint-device-control-violations


## Cortex XDR Malware - Incident Enrichment

**Product:** Cortex XDR by Palo Alto Networks

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook enriches the  XDR incident. The enrichment is done on the involved endpoint and Mitre technique ID information, and sets the 'Malware-Investigation and Response' layout

**Inputs:**

- `IncidentID`: The incident ID to be enriched.

**Outputs:**

- `PaloAltoNetworksXDR.Incident`
- `File`
- `Process`
- `IP`
- `Domain`
- `Endpoint.ID`
- `Endpoint.Hostname`
- `Endpoint.OS`
- `Endpoint.OSVersion`
- `Endpoint.IPAddress`

**Dependencies:**

- Sub-playbooks: Mitre Attack - Extract Technique Information From ID, Account Enrichment - Generic v2.1
- Integrations: Cortex XDR - IR, CortexXDRIR
- Scripts: isError, SetGridField
- Commands: extractIndicators, endpoint, xdr-get-incident-extra-data, setIncident


## CrowdStrike Falcon Malware - Incident Enrichment

**Product:** CrowdStrike Falcon

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook enables enriching CrowdStrike Falcon incidents by pivoting to their detections as well as mapping all the relevant data to the   incident fields

**Inputs:**

- `DetectionOrCaseID`: The ID of the CrowdStrike detection or Case.

**Outputs:**

- `CrowdStrike`
- `Endpoint`
- `CrowdStrike.FoundDetections`

**Dependencies:**

- Sub-playbooks: Account Enrichment - Generic v2.1, CrowdStrike Falcon - Get Detections by Case
- Integrations: CrowdstrikeFalcon
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty, SetGridField, SetMultipleValues, isError
- Commands: endpoint, extractIndicators, setIncident


## CVE-2021-34527 | CVE-2021-1675 - PrintNightmare

**Product:** Rapid Breach Response

The playbook can be triggered manually or automatically by setting up a reoccurring job. Microsoft has released a security update in June 2021 Patch Tuesday for CVE-2021-1675, a Local Privilege Escalation vulnerability in the Print Spooler Service. Later that month, researchers found another method to exploit the Print Spooler service remotely, which raised the severity of the vulnerability due to the fact that the new method allows Remote Code Execution, a new ID was given to the critical vulnerability - CVE-2021-34527. Microsoft patched the vulnerability in June but an exploit POC and complete technical analysis were made publicly available online. **Update 7.8.2021 - Microsoft has released an emergency patch for the PrintNightmare. A reference for the patch can be found in "Install Microsoft spooler service patches" task. This playbook includes the following tasks: More details on the vulnerabilities: CVE-2021-1675 LPE CVE-2021-34527 RCE ** Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `CVE`: PrintNightmare CVEs
- `SplunkEarliestTime`: The earliest time for the Splunk search query.
- `SplunkLatestTime`: The latest time for the Splunk search query.

**Dependencies:**

- Sub-playbooks: Cortex XDR - PrintNightmare Detection and Response, QRadarFullSearch, Search Endpoint by CVE - Generic, Panorama Query Logs
- Commands: closeInvestigation, splunk-search


## CVE-2021-22893 - Pulse Connect Secure RCE

**Product:** Rapid Breach Response

On April 20th, a new Remote Code Execution vulnerability in Pulse Connect Secure was disclosed. The reference number for the vulnerability is CVE-2021-22893 with the CVSS Score of 10.0. This playbook should be trigger manually and includes the following tasks: Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve. More information: Exploitation of Pulse Connect Secure Vulnerabilities

**Inputs:**

- `Related_Hashes`: The known hashes of different malware families associated with the exploitation.
- `Related_CVEs`: The known CVEs associated with the exploitation.
- `BlockAutomatically`: Whether to block the indicators automatically.Default: False.
- `QRadarWebshellsQuery`: The QRadar search query used for "Hunt Activity Using QRadar".Please note that there aren't specified fields which may cause a longer run time.
- `SplunkWebshellsQuery`: The Splunk search query used for "Hunt Activity Using Splunk".Please note that there are two specified fields: msg, message. the query will work for both field names.
- `RunWebshellsQuery`: If you would like to skip "Hunt Activity Using Splunk" OR "Hunt Activity Using Qradar" please change the value to 'False'.
- `QRadar_MD5_Field`: The name of the field for MD5 entries in QRadar.If not configured, QRadar Indicator Hunting may reach timeout.
- `QRadar_SHA1_Field`: The name of the field for SHA1 entries in QRadar.If not configured, QRadar Indicator Hunting may reach timeout.
- `QRadar_SHA256_Field`: The name of the field for SHA256 entries in QRadar.If not configured, QRadar Indicator Hunting may reach timeout.
- `SplunkEarliestTime`: The earliest time for the Splunk search query.

**Dependencies:**

- Sub-playbooks: QRadar Indicator Hunting V2, QRadarFullSearch, Search Endpoint by CVE - Generic, Palo Alto Networks - Hunting And Threat Detection, Block Indicators - Generic v2, Splunk Indicator Hunting
- Commands: expanse-get-issues, enrichIndicators, splunk-search, extractIndicators


## CVE Exposure - RiskSense

**Product:** RiskSense

Block IPs and apply the tag to assets that are vulnerable to specified CVE

**Inputs:**

- `CVES`: Specify Common Vulnerabilities and Exposures (CVE). You can mention multiple CVEs using a comma-separated list.
- `TagName`: Tags in RiskSense can be applied to assets, web applications, and vulnerabilities. Tags are useful in the soft grouping, workflow creation, and to identify compliance-related asset

**Outputs:**

- `RiskSense.TagAssociation`
- `RiskSense.HostFinding`
- `RiskSense.Host`

**Dependencies:**

- Sub-playbooks: Block IP - Generic v2
- Integrations: RiskSense
- Scripts: IsIntegrationAvailable
- Commands: risksense-apply-tag, risksense-get-hosts, risksense-get-host-findings


## Cybereason - Download Close File

**Product:** Cybereason

This playbook aborts a file download operation which is in progress based on the Malop ID and username provided

**Inputs:**

- `malopGUID, userName`: Malop GUID for fetching a file from a sonsor to download, The complete Cybereason user name string for the user performing the request

**Dependencies:**

- Commands: cybereason-start-fetchfile, cybereason-fetchfile-progress, cybereason-close-file-batch-id


## Darkfeed - malware download from feed

**Product:** Sixgill Darkfeed - Annual Subscription

**Inputs:**

- `Indicator Query`: Indicators matching the indicator query will be used as playbook input

**Dependencies:**

- Sub-playbooks: Darkfeed IOC detonation and proactive blocking
- Scripts: SetAndHandleEmpty


## Darkmon - Compromised Account Response

**Product:** Darkmon

Incident-type playbook for 'Darkmon Compromised Credential' (and similar). Identifies the user via the configured directory, suspends, forces a password reset, revokes active sessions, and notifies SOC + the user

**Dependencies:**

- Sub-playbooks: Disable account, Force password reset, Notify SOC + user, Revoke active sessions


## Darkmon - EDR Alert Enrichment

**Product:** Darkmon

Designed to be invoked from CrowdStrike / SentinelOne / Defender alert playbooks. Takes the alert's IOCs, enriches each via Darkmon, and if any are scored Bad, escalates incident severity and notifies the SOC. Endpoint containment is left to the EDR-specific playbook

**Outputs:**

- `DBotScore`

**Dependencies:**

- Sub-playbooks: Enrich IOCs via Darkmon (URL pass), Notify SOC
- Scripts: Set


## Darkmon - Phishing Email Triage

**Product:** Darkmon

Extracts URLs/IPs/file-hashes from a reported phishing email, enriches each via the Darkmon - Enrich * sub-playbooks, and if any indicator is scored Bad (DBotScore=3) calls Generic Block Indicator on it. Notifies the reporter and the SOC at the end

**Outputs:**

- `ExtractedIndicators`
- `DBotScore`

**Dependencies:**

- Sub-playbooks: Block malicious indicators, Enrich each IOC via Darkmon, Notify SOC, Notify reporter
- Scripts: ExtractIndicatorsFromTextFile


## Digital Shadows - CVE_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of CVE IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_CVE`: A Digital Shadows ShadowSearch query containing CVE IDs

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## Digital Shadows - Domain_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of Domain IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_Domain`: A Digital Shadows ShadowSearch query containing domains

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## Digital Shadows - IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrich indicators by providing intelligence and more associated indicators based on confirmed reporting in Digital Shadows SearchLight

**Inputs:**

- `IoC_IP`: An IP address for assessment and enrichment
- `IoC_CVE`: A CVE for assessment and enrichment
- `IoC_Domain`: A domain for assessment and enrichment
- `IoC_URL`: A URL for assessment and enrichment
- `IoC_MD5`: A MD5 hash for assessment and enrichment
- `IoC_SHA256`: A SHA256 hash for assessment and enrichment
- `IoC_SHA1`: A SHA1 hash for assessment and enrichment

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Sub-playbooks: Digital Shadows - CVE_IoC Assessment & Enrichment, Digital Shadows - URL_IoC Assessment & Enrichment, Digital Shadows - SHA1_IoC Assessment & Enrichment, Digital Shadows - MD5_IoC Assessment & Enrichment, Digital Shadows - IP_IoC Assessment & Enrichment, Digital Shadows - SHA256_IoC Assessment & Enrichment, Digital Shadows - Domain_IoC Assessment & Enrichment


## Digital Shadows - IP_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of IP IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_IP`: A Digital Shadows ShadowSearch query containing IP addresses

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## Digital Shadows - MD5_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of MD5 IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_MD5`: A Digital Shadows ShadowSearch query containing MD5 hashes

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: AddEvidence, Print
- Commands: ds-search


## Digital Shadows - SHA1_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of SHA1 IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_SHA1`: A Digital Shadows ShadowSearch query containing SHA1 hashes

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: AddEvidence, Print
- Commands: ds-search


## Digital Shadows - SHA256_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of SHA256 IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_SHA256`: A Digital Shadows ShadowSearch query containing SHA256 hashes

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: AddEvidence, Print
- Commands: ds-search


## Digital Shadows - URL_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of URL IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_URL`: A Digital Shadows ShadowSearch query containing URLs

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## DTM Alert Incident Response - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook initiates the response for DTM Alerts in  when an incident is investigated. For medium or higher severity, it creates a ServiceNow ticket using the "ServiceNow v2" integration; otherwise, the incident is assigned to an analyst. The ticket is enriched with GTI DTM Alert details, including alert type, status, monitor information, summary, AI Doc summary, and tags

**Inputs:**

- `alert_id`: Collection DTM Alert ID from incident.
- `incident_severity`: Collect incident severity from incident.
- `onCall`: Set to true to assign only the user that is currently on shift. Default is False.
- `severity_mapping`: Set the alert severity mapping as per GTI platform.

**Dependencies:**

- Sub-playbooks: Create ServiceNow Ticket
- Scripts: AssignAnalystToIncident, DeleteContext, Print, SetAndHandleEmpty
- Commands: servicenow-update-ticket


## Endpoint Investigation Plan

**Product:** Common Playbooks

This playbook handles all the endpoint investigation actions by performing the following tasks on every alert associated with the incident: Note: The playbook inputs enable manipulating the execution flow; read the input descriptions for details

**Inputs:**

- `HuntReconnaissanceTechniques`: Set to True to hunt for identified alerts with MITRE Reconnaissance techniques.
- `HuntInitialAccessTechniques`: Set to True to hunt for identified alerts with MITRE Access techniques.
- `HuntExecutionTechniques`: Set to True to hunt for identified alerts with MITRE Execution techniques.
- `HuntPersistenceTechniques`: Set to True to hunt for identified alerts with MITRE Persistence techniques.
- `HuntPrivilegeEscalationTechniques`: Set to True to hunt for identified alerts with MITRE Privilege Escalation techniques.
- `HuntDefenseEvasionTechniques`: Set to True to hunt for identified alerts with MITRE Defense Evasion techniques.
- `HuntDiscoveryTechniques`: Set to True to hunt for identified alerts with MITRE Discovery techniques.
- `HuntLateralMovementTechniques`: Set to True to hunt for identified alerts with MITRE Lateral Movement techniques.
- `HuntCollectionTechniques`: Set to True to hunt for MITRE Collection techniques identified alerts.
- `HuntCnCTechniques`: Set to True to hunt for identified alerts with MITRE Command and Control techniques.

**Dependencies:**

- Scripts: SearchIncidentsV2


## File Private Scanning - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook submits a file for private scanning, retrieves and evaluates the analysis verdict, and automatically creates a ServiceNow ticket using the "ServiceNow v2" integration when the file is determined to be malicious

**Inputs:**

- `file_id`: Fetch the Entry ID of the last submitted file from the incident.

**Dependencies:**

- Sub-playbooks: Create ServiceNow Ticket
- Scripts: DeleteContext, Print
- Commands: gti-private-file-scan-and-analysis-get, servicenow-update-ticket


## GCP - Enrichment

**Product:** GCP Enrichment and Remediation

Given the IP address this playbook enriches GCP and Firewall information

**Inputs:**

- `GcpIP`: GCP IP in alert
- `port`: Port to match traffic on for firewall rules.
- `protocol`: Protocol to match traffic on for firewall rules.

**Outputs:**

- `GoogleCloudCompute.Instances`
- `GCPIAM.Policy`
- `GCPIAM.TagBindings`
- `GCPHierarchy`
- `GCPOffendingFirewallRule`

**Dependencies:**

- Integrations: GCP-IAM, Google Cloud Compute
- Scripts: GCPOffendingFirewallRule, Set, GCPProjectHierarchy
- Commands: gcp-iam-tagbindings-list, gcp-iam-project-iam-policy-get, gcp-compute-aggregated-list-instances-by-ip, gcp-compute-get-instance


## Get entity alerts by MITRE tactics

**Product:** Core

This playbook searches XDR alerts related to specific entities, on a given timeframe, based on MITRE tactics. Note: The playbook's inputs enable manipulating the execution flow. Read the input descriptions for details

**Inputs:**

- `HuntReconnaissanceTechniques`: Set to True to hunt for identified alerts with MITRE Reconnaissance techniques.
- `HuntInitialAccessTechniques`: Set to True to hunt for identified alerts with MITRE Initial Access techniques.
- `HuntExecutionTechniques`: Set to True to hunt for identified alerts with MITRE Execution techniques.
- `HuntPersistenceTechniques`: Set to True to hunt for identified alerts with MITRE Persistence techniques.
- `HuntPrivilegeEscalationTechniques`: Set to True to hunt for identified alerts with MITRE Privilege Escalation techniques.
- `HuntDefenseEvasionTechniques`: Set to True to hunt for identified alerts with MITRE Defense Evasion techniques.
- `HuntDiscoveryTechniques`: Set to True to hunt for identified alerts with MITRE Discovery techniques.
- `HuntLateralMovementTechniques`: Set to True to hunt for identified alerts with MITRE Lateral Movement techniques.
- `HuntCollectionTechniques`: Set to True to hunt for identified alerts with MITRE Collection techniques .
- `HuntCnCTechniques`: Set to True to hunt for identified alerts with MITRE Command and Control techniques.

**Outputs:**

- `foundIncidents`

**Dependencies:**

- Scripts: SearchAlertsV2, SetAndHandleEmpty


## Hunt Extracted Hashes V2

**Product:** Hunting

This playbook extracts IOCs from the incident details and attached files using regular expressions and then hunts for hashes on endpoints in the organization using available tools. The playbook supports multiple types of attachments. For the full supported attachments list, refer to "Extract Indicators From File - Generic v2"

**Inputs:**

- `File`: The file from which to extract indicators.

**Dependencies:**

- Sub-playbooks: Extract Indicators From File - Generic v2, Search Endpoints By Hash - Generic V2
- Commands: extractIndicators


## Incident Enrichment - XM Cyber

**Product:** XM Cyber

This playbook enriches the incident using the hostname indicators and user data and increases the severity based on the calculated risk score and pushes breach points of the identified entities to XM Cyber

**Inputs:**

- `entity_values`: Specify the hostname or user entity. Supports comma separated values.
- `compromise_risk_score`: Specify the weight of Compromise Risk Score to apply to the final score calculation. Provide the value between 0 and 1.
- `choke_point_score`: Specify the weight of Choke Point Score to apply to the final score calculation. Provide the value between 0 and 1.
- `attribute_name`: The name of the custom label you want to push to CEM as an imported attribute.
- `parameter`: When setting up the condition for when to push the breach point data, this is the parameter of the condition. It is a list of predefined parameters for determining the criteria. Se
- `operator`: When setting up the condition for when to push the breach point data, this is the operator of the condition.Possible values are: Less than, Greater than, Less than equal to, Greate
- `value`: When setting up the condition for when to push the breach point data, this is the value of the condition. Can be boolean, string, integer, float, or date values.Supported date form

**Dependencies:**

- Scripts: DeleteContext, Set
- Commands: findIndicators, setIncident, xmcyber-calculate-risk-score, xmcyber-enrich-incident, xmcyber-push-breach-point, xmcyber-remove-breach-point


## Investigate On Bad Domain Matches - Chronicle

**Product:** Google SecOps

Use this playbook to investigate and remediate Bad IOC domain matches with recent activity found in the enterprise, as well as notify the SOC lead and network team about the matches. Supported Integrations

**Inputs:**

- `networkteam_email`: Enter the email address of the network team that needs to be notified.
- `stakeholder_email`: Enter the email of the stakeholder to whom you want to send the investigation summary report.

**Dependencies:**

- Integrations: Chronicle, Google SecOps, Whois, Mail Sender (New), Palo Alto Networks PAN-OS, Palo Alto Networks AutoFocus v2
- Scripts: AssignAnalystToIncident, GenerateInvestigationSummaryReport, Print
- Commands: domain, gcb-assets, gcb-ioc-details, pan-os-register-user-tag, send-mail, whois


## IOCs Curated Threat Intelligence Enrichment - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook extracts IOCs from incident details and enriches the selected IOCs with curated Google Threat Intelligence data, including malware families, campaigns, and threat actors

**Dependencies:**

- Sub-playbooks: IOC Curated Enrichment - Google Threat Intelligence
- Scripts: DeleteContext
- Commands: findIndicators


## IOC Alert

**Product:** Core

IOCs provide the ability to alert on known malicious objects on endpoints across the organization. Analysis Actions: The playbook will use several enrichment sources to determine the IOC verdict. Additionally, will use the Analytics module to run a prevalence check for the IOC. Response Actions: The playbook's first response action is a containment plan that is based on the playbook input. In that phase, the playbook will execute endpoint isolation Investigative Actions: When the playbook executes, it checks for additional abnormal activity using the Endpoint Investigation Plan playbook that can indicate the endpoint might be compromised. Remediation Actions: In case results are found within the investigation phase, the playbook will execute remediation actions that include containment and eradication. This phase will execute the following containment actions: And the following eradication actions

**Inputs:**

- `BlockIndicatorsAutomatically`: Whether to block suspicious/malicious indicators automatically. Specify True/False.
- `ShouldCloseAutomatically`: Whether to close the alert automatically if it's established verdict is False Positive. Specify True/False.
- `PreHostContainment`: Whether to isolate the host before the investigation phase in case an IOC was found to be suspicious. Specify True/False.
- `ShouldHandleFPautomatically`: Whether to automatically handle false positive alerts. Specify true/false.
- `AutoRestoreEndpoint`: Whether to execute the Recovery playbook. Specify True/False.
- `AutoContainment`: Setting this input will impact both Containment Plan sub-playbooks. Without setting this input, the default values are True for the first occurrence and False for the second.Whethe
- `FileRemediation`: Should be either 'Quarantine' or 'Delete'.
- `AutoEradication`: Whether to execute automatically or manually the eradication plan tasks:* Terminate process* Delete file* Reset the user's passwordSpecify True/False.
- `ShouldOpenTicket`: Whether to open a ticket automatically in a ticketing system. (True/False).
- `serviceNowShortDescription`: A short description of the ticket.

**Dependencies:**

- Sub-playbooks: Endpoint Investigation Plan, Recovery Plan, Eradication Plan, Enrichment for Verdict, Handle False Positive Alerts, Ticket Management - Generic, Containment Plan
- Commands: extractIndicators, setParentIncidentFields, closeInvestigation


## IOC Curated Enrichment - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook provides IOC curated enrichment using Google Threat Intelligence data, including malware families, campaigns, and threat actors, and displays the results in the War Room for investigation

**Inputs:**

- `resource`: The file hash (MD5, SHA1, or SHA256), Domain, URL or IP.
- `resource_type`: The type of the resource (IP, domain, URL, or file hash).

**Dependencies:**

- Scripts: DeleteContext, Print, SetAndHandleEmpty
- Commands: gti-curated-campaigns-get, gti-curated-malware-families-get, gti-curated-threat-actors-get


## IOC Enrichment and Blocking - Google SecOps

**Product:** Google SecOps

This playbook enriches IOCs using the enrichment commands (IP, Email, Domain, URL, and File) and blocks the malicious IOCs based on DBot Score

**Dependencies:**

- Sub-playbooks: Block Domain - Generic v2, Block Email - Generic v2, Block File - Generic v2, Block IP - Generic v3, Block URL - Generic v2
- Scripts: DeleteContext, SetAndHandleEmpty
- Commands: domain, email, file, findIndicators, ip, url


## IOC Enrichment and Blocking - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook enriches IOCs using the GTI enrichment commands (IP, Domain, URL, and File) and blocks the IOCs based on GTI assessment parameters such as Threat Score, Severity, and Verdict

**Inputs:**

- `ip_addresses`: Provide a comma-separated list of IPs.
- `domains`: Provide a comma-separated list of Domains.
- `files`: Provide a comma-separated list of Files.
- `urls`: Provide a comma-separated list of URLs.

**Dependencies:**

- Sub-playbooks: Block Domain - Generic v2, Block File - Generic v2, Block IP - Generic v3, Block URL - Generic v2
- Scripts: DeleteContext, Set
- Commands: domain, file, findIndicators, ip, url


## Large Upload Alert

**Product:** Core

The playbook investigates  XDR alerts involving large upload alerts. The playbook consists of the following procedures

**Inputs:**

- `InternalIPRanges`: A list of IP ranges to check the IP against. The list should be provided in CIDR notation, separated by commas. An example of a list of ranges would be: "172.16.0.0/12,10.0.0.0/8,1
- `FurtherInvestigation`: Determines whether an alert should be further investigated if similar previous false positive alerts were found.Possible values:True/False. Default: False.
- `AutoBlockIndicators`: Determine whether the given indicators be automatically blocked, or if the user should be given the option to choose.Possible values:True/False. Default: True.If set to True - no p
- `BlockIndicators_UserVerification`: Determine whether the blocking of any indicator requires the verification of the user.Possible values:True/False. Default: False.
- `EarlyContainment`: Whether early containment should be allowed when the IP address is known to be malicious.Possible values:True/False. Default: True.
- `AutoIsolateEndpoint`: Whether to isolate the initiating endpoint automatically if the investigation verdict is malicious.Possible values:True/False. Default: False.
- `Transferred_Data _Threshold`: Specify the uploaded data threshold volume (in MB) from which large upload alerts should be investigated.By setting a threshold, you will be able to determine which large upload al
- `FWApps_Processes_Whitlist`: A list of known and authorized FW application IDs and processes used in the organization.
- `Alert_ID`: The Cortex XDR alert ID.

**Dependencies:**

- Sub-playbooks: Block Indicators - Generic v3, User Investigation - Generic, TIM - Indicator Relationships Analysis, Command-Line Analysis, Threat Hunting - Generic, Entity Enrichment - Generic v3, Endpoint Investigation Plan, Search and Compare Process Executions - Generic
- Integrations: CortexCoreIR
- Scripts: DBotFindSimilarIncidents, SetAndHandleEmpty, Set
- Commands: setAlertStatus, core-isolate-endpoint, setAlert, core-get-cloud-original-alerts


## Malware Investigation & Response Incident Handler

**Product:** Malware Investigation and Response

This playbook is triggered by a malware incident from an endpoint integration. It performs enrichment, detonation, and hunting within the organization, and remediation on the malware. The playbook also covers the SIEM ingestion flow in which the fetching integration is the SIEM and EDR integrations grab all additional data. Currently supported EDR integrations are XDR, CrowdStrike Falcon, and Microsoft Defender for Endpoint. Currently supported SIEM integrations are QRadar and Splunk

**Inputs:**

- `OnCall`: Define whether to assign OnCall to this flow.Possible values: True/False.Leave it empty if you do want not to assign an analyst to the incident.
- `EnableDeduplication`: Whether the deduplication playbook will be used.
- `DedupLimit`: The maximum number of incidents to query and set to context data.
- `DedupCloseSimilar`: "Defines the threshold of similarity to close a similar incident. All similar incidents with similarity above this value will be closed.For example, if CloseSimilar is set to .8 an
- `DedupHandleSimilar`: "This input defines how to handle Similar incidents. You may choose between: ""Link"", ""Close"", ""Link and Close"".Note: that closing incidents will require you to define ""Close
- `SIEMEDRProductToUse`: For EDR alerts routed through a SIEM, provide the supported originating EDR. Possible values: CrowdStrike, XDR, or Microsoft Defender.
- `EnableClosureSteps`: When closing an incident, whether to use closure steps to close automatically.
- `TicketProjectName`: For ticketing systems such as Jira a project name is required.
- `OverrideSIEMSeverity`: Whether to set the severity according to the ScaleToSetSeverity and SeverityValuesMapping settings (True) or keep the original severity as mapped by the SIEM (False).
- `SIEMincidentFieldForID`: The name of the field that provides the external ID of the alert or incident in the EDR.

**Dependencies:**

- Sub-playbooks: Cortex XDR Malware - Investigation And Response, MDE Malware - Investigation and Response, Malware SIEM Ingestion - Get Incident Data, CrowdStrike Falcon Malware - Investigation and Response
- Scripts: SetMultipleValues, Set, AssignAnalystToIncident


## Malware Investigation and Response - Set Alerts Grid

**Product:** Malware Investigation and Response

This playbook sets the alert grid for the Malware Investigation & Response layout

**Inputs:**

- `AlertName`: The alert name.
- `HostName`: The host name.
- `FileName`: The file name.
- `ProcessID`: The process ID.
- `SHA256`: The SHA256 file hash.
- `CommandLine`: The command line.
- `ParentProcess`: The parent process.

**Dependencies:**

- Scripts: Set, SetGridField


## Malware Triage - ReversingLabs TitaniumCloud

**Product:** ReversingLabs TitaniumCloud

Provides the TitaniumCloud classification of a file hash, and takes remediation actions based on that classification

**Inputs:**

- `hash`: SHA1 hash of a file.
- `file`: The file itself.
- `EndpointIP`: IP address of the endpoint from which the indicator came.

**Outputs:**

- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `DBotScore.Score`
- `DBotScore.Type`
- `DBotScore.Indicator`
- `DBotScore.Vendor`
- `ReversingLabs.file_reputation`

**Dependencies:**

- Sub-playbooks: Isolate Endpoint
- Integrations: ReversingLabs TitaniumCloud v2
- Scripts: IncreaseIncidentSeverity
- Commands: setIndicator, setIncident, reversinglabs-titaniumcloud-file-upload, reversinglabs-titaniumcloud-get-sample-dynamic-analysis-results, reversinglabs-titaniumcloud-submit-sample-for-dynamic-analysis, reversinglabs-titaniumcloud-file-reputation


## MDE Malware - Incident Enrichment

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook enriches Microsoft Defender For Endpoint alerts. The enrichment is done on the involved endpoint and Mitre technique ID information, and it sets the 'Malware-Investigation and Response' layout

**Inputs:**

- `DidAlertOriginateFromSIEM`: Whether the incident is fetched through a SIEM product.
- `AlertID`: The Microsoft Defender For Endpoint alert ID.

**Outputs:**

- `MITREATTACK`
- `AttackPattern`
- `MicrosoftATP.Alert`
- `Endpoint`

**Dependencies:**

- Sub-playbooks: Mitre Attack - Extract Technique Information From ID, Account Enrichment - Generic v2.1
- Integrations: Microsoft365DefenderEventCollector, MicrosoftDefenderAdvancedThreatProtection
- Scripts: SetGridField, isError, SetAndHandleEmpty
- Commands: microsoft-atp-get-alert-by-id, setIncident, endpoint, extractIndicators, file


## Microsoft 365 Defender - Emails Indicators Hunt

**Product:** Microsoft 365 Defender

This playbook retrieves email data based on the "URLDomain", "SHA256" and "IPAddress" inputs. SHA256 - Emails with attachments matching the "SHA256" input are retrieved. URLDomain - If the "URLDomain" value is found as a substring of URL(s) in the body of the email, the email is retrieved. IPAddress - Emails with "SenderIPv4"/SenderIPv6" or URLs (in the body) matching the "IPAddress" input are retrieved

**Inputs:**

- `URLDomain`: Domain or URL to search within emails. Can be a single domain or URL or an array of domains or URLs to search. The search looks for the exact Domain or URL.
- `SHA256`: The SHA256 hash file or an array of hashes to search within emails.
- `IPAddress`: The source or destination IP address to search. Can be a single address or an array of IP addresses.
- `Timeout`: The time limit in seconds for the HTTP request to run. Default is 60.
- `SearchTimeframe`: Number of days past to search. Default is 7.
- `ResultsLimit`: Number of retrieved entries. Enter -1 for unlimited query. 50 is the default.
- `ListenerMailbox`: The mailbox of the listening integration. In case it is provided, the emails found in it will be ignored.

**Outputs:**

- `Microsoft365Defender.RetrievedEmails`
- `Microsoft365Defender.RetrievedEmails.InternetMessageId`
- `Microsoft365Defender.RetrievedEmails.SenderFromDomain`
- `Microsoft365Defender.RetrievedEmails.EmailDirection`
- `Microsoft365Defender.RetrievedEmails.DeliveryLocation`
- `Microsoft365Defender.RetrievedEmails.AuthenticationDetails`
- `Microsoft365Defender.RetrievedEmails.DeliveryAction`
- `Microsoft365Defender.RetrievedEmails.Subject`
- `Microsoft365Defender.RetrievedEmails.AttachmentCount`
- `Microsoft365Defender.RetrievedEmails.ThreatNames`

**Dependencies:**

- Integrations: Microsoft 365 Defender
- Scripts: Set, IsIntegrationAvailable, SetAndHandleEmpty
- Commands: microsoft-365-defender-advanced-hunting


## Microsoft Defender For Endpoint - Collect investigation package

**Product:** Microsoft Defender for Endpoint

This playbook simplifies retrieving investigation packages to   from supported machines (See  The playbook receives information about the target devices (host name, IP, and device ID), validates the devices exist, and retrieves the collection package from those machines into the   console. Note: This action may take time, the average package size is around ~15 MB

**Inputs:**

- `AutoCollectinvestigationPackege`: Choose True to skip user validation on retrieving the investigation pack within the provided assets.
- `Hostnames`: A comma-separated list of host names.
- `MachineIDs`: A comma-separated list of machine IDs.
- `IPs`: A comma-separated list of machine IPs.

**Outputs:**

- `MicrosoftATP.MachineAction`

**Dependencies:**

- Commands: endpoint, microsoft-atp-request-and-download-investigation-package


## Microsoft Office File Enrichment - Oletools

**Product:** Oletools

Oletools is a tool for analyzing Microsoft OLE2 files, such as Microsoft Office documents or Outlook messages, mainly for malware analysis, forensics, and debugging. This playbook will run run the "oleid" command on the files which are passed to to it as playbook inputs. In case any macros or external relationships were found, it will also run "olevba" and "oleobj" commands as well on the relevant files. oleid - Analyze OLE files to detect specific characteristics usually found in malicious files. oleobj - Extract embedded objects from OLE files. olevba - Extract and analyze VBA Macro source code from MS Office documents (OLE and OpenXML)

**Inputs:**

- `FileObject`: A list of file objects. Default is "File" key.
- `Decode`: Available values: "True" or "False". Default is "False"When this is set to "True", in case a macro was found within the file, it will output all the obfuscated strings with their d
- `NonSecretPassword`: Will be used to decrypt encrypted files. Encrypted files cannot be analyzed otherwise.Please note that this input is "Non Secret" because it will be visible as plain text.

**Outputs:**

- `Oletools.Oleid.ole_command_result`
- `Oletools.Oleid.file_name`
- `Oletools.Oleid.sha256`
- `Oletools.Oleid.ole_command_result.File_format`
- `Oletools.Oleid.ole_command_result.Container_format`
- `Oletools.Oleid.ole_command_result.Encrypted`
- `Oletools.Oleid.ole_command_result.VBA_Macros`
- `Oletools.Oleid.ole_command_result.XLM_Macros`
- `Oletools.Oleid.ole_command_result.External_Relationships`
- `Oletools.Oleid.ole_command_result.ObjectPool`

**Dependencies:**

- Scripts: Set, Oletools


## Palo Alto Networks BPA - Submit Scan

**Product:** MITRE ATT&CK - Courses of Action

This playbook accepts a list of BPA checks, triggers a job and returns the checks results

**Inputs:**

- `check_id`: A comma-separated list of the BPA IDs of the results to return.
- `check_name`: A comma-separated list of the name of the results to return.

**Outputs:**

- `PAN-OS-BPA.JobResults.JobID`
- `PAN-OS-BPA.JobResults.Checks.check_id`
- `PAN-OS-BPA.JobResults.Checks.check_name`
- `PAN-OS-BPA.JobResults.Checks.check_message`
- `PAN-OS-BPA.JobResults.Checks.check_passed`
- `BPA.Passed`
- `BPA.Failed`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: BPA
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable, DeleteContext
- Commands: pan-os-bpa-get-job-results, pan-os-bpa-submit-job


## PhishUp Mail Scanner

**Product:** PhishUp

Extracts URLs from mail body and checks URLs with PhishUp. Takes action based on PhishUp results

**Inputs:**

- `EmailBodyHtml`: Email Mail Body for extracting URLs. Default Value is "${incident.emailbodyhtml}"
- `ShouldPhishUpActionWork`: If you do not want actions such as deleting mail and moving to spam in PhishUp playbook, you should set the value False. Default value is True
- `GmailMessageID`: Identify mail for deleting and moving funcitons. Defaultly it comes from incident which is setted from PhishUp Gmail Mapper
- `GmailUserID`: Identify user for deleting and moving funcitons. Defaultly it comes from incident which is setted from PhishUp Gmail Mapper

**Outputs:**

- `PhishUp.Evaluation`

**Dependencies:**

- Integrations: PhishUp, Gmail
- Scripts: IncreaseIncidentSeverity
- Commands: closeInvestigation, phishup-get-chosen-action, url, extractIndicators, phishup-evaluate-response, gmail-delete-mail, gmail-move-mail


## Phishing Alerts Investigation

**Product:** PhishingAlerts

This playbook investigates and remediates potential phishing incidents produced by either an email security gateway or a SIEM product. It retrieves original email files from the email security gateway or email service provider and generates a response based on the initial severity, hunting results, and the existence of similar phishing incidents in . No action is taken without an initial approval given by the analyst using the playbook inputs

**Inputs:**

- `Role`: The default role to assign the incident to.
- `SearchAndDelete`: Whether to enable the "Search and Delete" capability.For a malicious email, the Search and Delete sub-playbook looks for other instances of the email and deletes them pending analy
- `BlockIndicators`: Whether to enable the "Block Indicators" capability.For a malicious email, the Block Indicators sub-playbook blocks all malicious indicators in the relevant integrations.
- `AuthenticateEmail`: Whether the authenticity of the email should be verified using SPF, DKIM, and DMARC.
- `OnCall`: Set to True to assign only to analysts on the current shift. Requires the platform.5 or later.
- `SearchAndDeleteIntegration`: Determines which product and playbook is used to search and delete the phishing email from user inboxes.Set this to "O365" to use the O365 - Security And Compliance - Search And De
- `O365DeleteType`: The method to delete emails using the O365 - Security And Compliance - Search And Delete playbook. Can be "Soft" (recoverable), or "Hard" (unrecoverable). Leave empty to decide man
- `O365ExchangeLocationExclusion`: The exchange location. Determines from where to search and delete emails searched using O365 playbooks. Use the value 'All' to search all mailboxes, use 'SingleMailbox' to search a
- `SOCEmailAddress`: The SOC email address to set if the playbook handles phishing alerts.
- `escalationRole`: The role to assign the incident to if the incident severity is critical.

**Dependencies:**

- Sub-playbooks: Process Email - Generic v2, Phishing Alerts - Check Severity, Detonate File - Generic, Extract Indicators From File - Generic v2, Email Headers Check - Generic, Threat Hunting - Generic, Search And Delete Emails - Generic v2, Block Indicators - Generic v3
- Scripts: SearchIncidentsV2
- Commands: linkIncidents, closeInvestigation


## Phishing Triage and Response - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook extracts email addresses from phishing alerts, enriches their associated domains using the GTI domain enrichment command, and evaluates the GTI Threat Score, severity, and verdict. Based on these enrichment results, the playbook automatically blocks the malicious or high-risk email addresses to prevent further compromise

**Inputs:**

- `email_addresses`: Provide a comma-separated list of email addresses.

**Dependencies:**

- Sub-playbooks: Block Email - Generic v2, Email Collection by Enriched Domain - Google Threat Intelligence
- Scripts: DeleteContext, SetAndHandleEmpty
- Commands: domain, findIndicators


## Powershell Payload Response

**Product:** Malware Lateral Movement Assessment and Response

The Powershell Payload Response playbook is designed to be used when file payload executions are detected from an endpoint machines Powershell and begins the remediation process

**Inputs:**

- `Endpoint ID`: ID of the endpoint in question.
- `Hostname`: Hostname of the endpoint in question.
- `Email`: Email attachment.
- `File`: Payload file that was executed.
- `File Path`: File Path of the Executed Payload.

**Dependencies:**

- Sub-playbooks: Process Email - Generic, Isolate Endpoint - Generic V2, Block File - Generic v2, Dedup - Generic v3, Detonate File - Generic
- Integrations: Carbon Black Defense, Carbon Black Enterprise EDR, ServiceNow v2, SplunkPy
- Scripts: AssignAnalystToIncident, IncreaseIncidentSeverity
- Commands: cb-eedr-device-background-scan, splunk-search, closeInvestigation, cbd-create-policy, servicenow-update-ticket, cb-eedr-device-unquarantine, servicenow-create-ticket


## Prisma Cloud Compute - Audit Alert Enrichment

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook. It does the following

**Inputs:**

- `Hostname`: The hostname to retrieve events for. Relevant only for audit events.
- `ImageName`: The image name to retrieve events for.
- `AuditAlertType`: The type of the audit alert. Will be used to determine whether to retrieve WAAS events or not.
- `BaseURL`: The base URL of the Prisma Cloud Compute Instance used to create a link back to the alerts for an image.
- `ConsoleLink`: The value of the alert's console link. Part of the original incident values.
- `AccountID`: The cloud account ID.
- `Namespace`: The namespace which will be used to search associated users with in the "Get Account Owner" playbook.

**Outputs:**

- `PrismaCloudCompute.ReportsImagesScan`
- `PrismaCloud.Users`
- `PrismaCloud.UserRoles`
- `PrismaCloud.UserRoles.associatedUsers`
- `PrismaCloudCompute.ReportHostScan`
- `PrismaCloudCompute.ReportHostScan.complianceIssues`
- `PrismaCloudCompute.ReportsImagesScan.complianceIssues`

**Dependencies:**

- Sub-playbooks: Prisma Cloud - Get Account Owner, Prisma Cloud Compute - Get Container Events
- Commands: prisma-cloud-compute-images-scan-list, prisma-cloud-compute-hosts-scan-list, setIncident


## Prisma Cloud Compute - Audit Alert Vulnerabilities Enrichment

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook. It creates CVE indicators based on image or host vulnerabilities

**Inputs:**

- `ImageVulnerabilities`: Image vulnerabilities that were retrieved.
- `HostVulnerabilities`: Host vulnerabilities that were retrieved.
- `CVEsIndicatorsSeverities`: A list of the image or host CVE severities that the playbook creates indicators from.Available options (not case sensitive):- Critical- High- Medium- Low- NegligibleDefault value: 

**Outputs:**

- `CVEReport`


## Prisma Cloud Compute - Container Forensics

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook. Gets the container profile and forensics

**Inputs:**

- `AuditAlertType`: The audit alert type.
- `Image`: Image name.
- `DefenderType`: The defender type.
- `AlertCluster`: The alert's cluster name.
- `Hostname`: The hostname.
- `ForensicLink`: This link exists in audit runtime incidents.

**Dependencies:**

- Commands: prisma-cloud-compute-profile-container-list, prisma-cloud-compute-profile-container-forensic-list


## Prisma Cloud Compute - Get Container Events

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook

**Inputs:**

- `hostname`: The hostname to retrieve events for. Relevant only for audit events.
- `ImageName`: The image name to retrieve events for.
- `AuditAlertType`: The type of the audit alert. Will be used to determine whether to retrieve WAAS events or not.

**Dependencies:**

- Commands: prisma-cloud-compute-runtime-container-audit-events-list, setIncident, prisma-cloud-compute-get-audit-firewall-container-alerts


## Rapid7 - Nexpose - Enrichment

**Product:** Rapid7 InsightVM

Given an IP address, this playbook searches Rapid7 Nexpose assets for an asset with the associated IP address to retrieve asset information and proceeds to return all associated tags with it

**Inputs:**

- `IP`: IP used to search for asset information and tags.

**Outputs:**

- `Nexpose.Asset`
- `Nexpose.AssetTag`

**Dependencies:**

- Commands: nexpose-get-asset-tags, nexpose-search-assets


## RDP Bitmap Cache - Detect and Hunt

**Product:** RDPCacheHunting

**Inputs:**

- `ShouldCollectRDPCache`: When set to True, will use XDR to get RDP cache files from the endpoints. When set to False will try and use existing cache files from context.
- `EndpointIDs`: A comma-separated list of endpoint ID's to retrieve cache files from.
- `FilePath`: The path of the file to retrieve or use wildcard for multiple files.For example:C:\the\path\to\cache_file.binC:\the\path\to\*
- `Hostname`: Hostname of the machine on which the file is located. For PS remote it can also be an IP address.
- `min_score`: StringSifter - Limit output to strings with score >= min-score.
- `limit`: StringSifter - Limit output to the top limit ranked strings.
- `similiarity_threshold`: StringSimilarity - The similarity threshold to show results for, a value between 0 < x >1.
- `QRadarTimeFrame`: The time frame for the QRadar hunting query.
- `SplunkEarliestTime`: The earliest time for the Splunk hunting query.
- `SplunkLatestTime`: The latest time for the Splunk hunting query,

**Dependencies:**

- Sub-playbooks: Retrieve File from Endpoint - Generic V3, Threat Hunting - Generic
- Scripts: Set, PreProcessImage, StringSimilarity, StringSifter, UnzipFile, SetGridField, BMCTool
- Commands: xdr-file-retrieve, lolbas-get-indicators, image-ocr-extract-text, rasterize-image, splunk-search, extractIndicators, rasterize-pdf, setIncident


## Recorded Future Entity Enrichment

**Product:** Recorded Future Intelligence

Template playbook to incorporate Recorded Future enrichment for IPs, Hashes, Domains, URLs into your current workflows. Playbook also shows how to look up available 'Links' data for IOCs

**Inputs:**

- `MD5`: File MD5 hash to enrich.
- `SHA256`: The file SHA256 hash to enrich.
- `SHA1`: The file SHA1 hash to enrich.
- `IP`: The IP Address to enrich.
- `Domain`: The Domain name to enrich.
- `URL`: The URL to enrich.

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`
- `DBotScore`
- `DBotScore.Vendor`
- `DBotScore.Score`

**Dependencies:**

- Integrations: Recorded Future v2
- Commands: recordedfuture-intelligence, recordedfuture-links


## Rubrik Turbo IOC Scan - Rubrik Polaris

**Product:** Rubrik Security Cloud

This playbook starts a Turbo IOC scan with the specified IOC values and shows the results upon completion

**Inputs:**

- `ioc`: The value of the indicator to scan for. Supports comma separated values.Note: Users can retrieve the Md5, SHA1 or SHA256 by executing the "rubrik-threat-monitoring-matched-file-get
- `scan_name`: Name of the new turbo threat hunt scan.
- `cluster_id`: The ID of the cluster on which to perform a scan. If not provided, all the clusters will be scanned.Note: Users can retrieve the list of the cluster IDs by executing the "rubrik-gp
- `start_time`: Filter the snapshots from the provided date. Any snapshots taken before the provided date-time will be excluded.Formats accepted: 2 minutes, 2 hours, 2 days, 2 weeks, 2 months, 2 y
- `end_time`: Filter the snapshots until the provided date. Any snapshots taken after the provided date-time will be excluded.Formats accepted: 2 minutes, 2 hours, 2 days, 2 weeks, 2 months, 2 y
- `max_snapshots_per_object`: Maximum number of snapshots to scan per object.
- `polling_interval`: Frequency that the IOC scan command will run (minutes).
- `polling_timeout`: Amount of time to poll before declaring a timeout and resuming the playbook (in minutes).

**Outputs:**

- `RubrikPolaris.IOCScan`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Scripts: DeleteContext
- Commands: rubrik-turbo-ioc-scan, rubrik-ioc-scan-results-v2


## SANS - Incident Handler's Handbook Template

**Product:** SANS

Contains the phases for handling an incident as they are described in the SANS Institute ‘Incident Handler's Handbook’ by Patrick Kral. ***Disclaimer: This playbook does not ensure compliance to SANS regulations


## Scan Assets - Nexpose

**Product:** Rapid7 InsightVM

Scans according to asset IP addresses or host names, and waits for the scan to finish by polling the scan status in pre-defined intervals

**Inputs:**

- `IPs`: The asset IP addresses to scan.
- `HostNames`: The hostnames of the assets to scan.
- `Name`: The scan name as specified by the user.

**Outputs:**

- `Nexpose.Scan.ScanType`
- `Nexpose.Scan.Completed`
- `Nexpose.Scan.StartedBy`
- `Nexpose.Scan.Assets`
- `Nexpose.Scan.TotalTime`
- `Nexpose.Scan.Id`
- `Nexpose.Scan.Status`
- `Nexpose.Scan.Vulnerabilities.Critical`
- `Nexpose.Scan.Vulnerabilities.Moderate`
- `Nexpose.Scan.Vulnerabilities.Severe`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: Rapid7 Nexpose
- Commands: nexpose-get-scan, nexpose-start-assets-scan


## Search And Delete Emails - EWS

**Product:** Microsoft Exchange On-Premise

Searches EWS to identify and delete emails with similar attributes of a malicious email

**Inputs:**

- `From`: The value of the malicious email's "From" attribute.
- `Subject`: The value of the malicious email's "Subject" attribute.
- `AttachmentName`: The value of the malicious email's AttachmentName attribute.
- `SearchThisWeek`: Limit the search to the current week. Can be "true" or "false".
- `Limit`: The maximum number of search results.
- `DeleteType`: The deletion type. Can be, "trash", "soft", or "hard".

**Dependencies:**

- Integrations: EWS v2
- Scripts: BuildEWSQuery
- Commands: ews-delete-items, ews-search-mailboxes


## Search And Delete Emails - Generic v2

**Product:** Common Playbooks

This playbook searches and deletes emails with similar attributes of a malicious email using one of the following integrations: EWS Microsoft Graph Security Gmail Agari Phishing Defense

**Inputs:**

- `From`: The value of the malicious email's "From" attribute.
- `Subject`: The value of the malicious email's "Subject" attribute.
- `AttachmentName`: The value of the malicious email's "AttachmentName" attribute.
- `SearchAndDeleteIntegration`: The integration in which to run the search and delete action. Can be MS Graph, Gmail, EWS, or Agari Phishing Defense.
- `SearchThisWeek`: Whether to limit the search to the current week. Disabling this may increase search scope, execution time, and risk of timeout for large mailboxes.
- `MsgCase`: Used only with Microsoft Graph Security. The eDiscovery case name to use. Looked up by name and created if missing.
- `MsgKQL`: Used only with Microsoft Graph Security. KQL query identifying the emails to search and delete. Built automatically from the From, Subject, and AttachmentName inputs if left empty.
- `MsgRecipients`: Used only with Microsoft Graph Security. CSV of recipient email addresses to scope the search when MsgMailboxScope is recipientsOnly.
- `MsgMailboxScope`: Used only with Microsoft Graph Security. Determines which mailboxes to search. Use recipientsOnly to limit to specific recipients, allTenantMailboxes to search the entire tenant.
- `MsgDeleteType`: Used only with Microsoft Graph Security. The delete type to perform on the search results. Possible values are Hard or Soft, or leave empty to select manually (Hard = unrecoverable

**Dependencies:**

- Sub-playbooks: Search And Delete Emails - Microsoft Graph Security, Search And Delete Emails - EWS, Search And Delete Emails - Gmail
- Integrations: Agari Phishing Defense
- Scripts: DeleteContext, GetTime, Set
- Commands: apd-remediate-message


## Social Engineering Domain Investigation

**Product:** Social Engineering Domain Analysis

Enrich and Investigate domains which may present a social engineering threat to your organization. Review before blocking potentially dangerous indicators

**Inputs:**

- `SocialEngineeringDomainList`: The CSV list of domains to test or array of domains
- `SocialEngineeringRegisteredDomain`: Your company domain
- `BadNameservers`: An the platform BadNameserver list. This should be a CSV list with a single column and the header of "nameserver"Example List Contents:nameserverbadnameserver1.combadnameserver2.co

**Dependencies:**

- Sub-playbooks: Social Engineering Domain Enrichment
- Scripts: ConvertTableToHTML
- Commands: setIndicator, extractIndicators


## URL Private Scanning - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook performs private URL scanning and analyses the URL based on GTI assessment parameters such as Threat Score, Verdict, and Severity. Based on these parameters, the playbook blocks the URL

**Inputs:**

- `url`: Provide a comma-separated list of URLs.

**Dependencies:**

- Sub-playbooks: Block URL - Generic v2, URL Scan - Google Threat Intelligence
- Scripts: DeleteContext
- Commands: findIndicators


## Xpanse - Alert Enrichment

**Product:** Cortex Xpanse

This playbook handles ASM alerts by enriching asset information via integrations with Cloud Service Providers and other IT and Security tools

**Dependencies:**

- Sub-playbooks: Azure - Enrichment, GCP - Enrichment, AWS - Enrichment


## Xpanse - Alert Self-Enrichment

**Product:** Cortex Xpanse

Enrichment on the alert itself using  Xpanse APIs

**Dependencies:**

- Integrations: Cortex Xpanse
- Scripts: GridFieldSetup, Set
- Commands: asm-get-asset-internet-exposure, asm-get-external-service, extractIndicators


## Zimperium Incident Enrichment

**Product:** Zimperium

Enriches Zimperium incidents

**Dependencies:**

- Integrations: Zimperium, Zimperium v2
- Scripts: IsIntegrationAvailable
- Commands: zimperium-users-search, zimperium-device-get-by-id, zimperium-devices-search


## CheckPDFEncryptionAndValidity

**Product:** Common Scripts

This script checks whether a given PDF file is valid and whether it is encrypted. The results are returned as fields in the file’s context. The script will not fail on invalid/ encrypted files. Instead, the error details will be captured and returned in the file’s context


## ExtractAttackPattern

**Product:** Common Scripts

Extract Attack Pattern Threat Intel Object. After auto extract extracts the Attack Pattern IDs, this script is executed and extracts the value (name) of the Attack Pattern

**Inputs:**

- `input`: A comma-separated list of Attack Pattern IDs.


## IsDomainInternal

**Product:** Common Scripts

The script takes one or more domain names and checks whether they're in the   list defined in the InternalDomainsListName argument. By default, the InternalDomainsListName argument will use the   list called "InternalDomains". The list can be customized by the user. It should contain the organization's internal domain names, separated by new lines. Subdomains are also supported in the list. The results of the script are tagged with the "Internal_Domain_Check_Results" tag, so they can be displayed in the War Room entry sections in incident layouts

**Inputs:**

- `InternalDomainsListName`: The name of the the platform. If no list is specified, the script will use the InternalDomains list by default.
- `Domains`: A domain name or a list of domain names to check for being internal or external, against the specified list of internal domains.

**Outputs:**

- `Domain.Name`
- `Domain.Internal`

## ACTI Incident Enrichment

**Product:** Accenture CTI v2

**Inputs:**

- `ia_uuid`: Intelligence Alert unique ID.
- `ir_uuid`: Intelligence Report unique ID.
- `MalwareFamily_uuid`: Malware Family unique ID.
- `ThreatGroup_uuid`: Threat Group unique ID.
- `ThreatCampaign_uuid`: Threat Campaign unique ID.
- `ThreatActor_uuid`: Threat Actor unique ID.

**Dependencies:**

- Integrations: ACTI Indicator Query
- Commands: acti-get-fundamentals-by-uuid, acti-getThreatIntelReport


## ACTI Indicator Enrichment

**Product:** Accenture CTI v2

**Inputs:**

- `IP_Pre_Enrich`: The extracted IP.
- `Domain_Pre_Enrich`: The extracted Domain.
- `URL_Pre_Enrich`: The extracted URL.

**Outputs:**

- `IP`
- `DBotScore`
- `Domain`
- `URL`
- `intelligence_alerts`
- `intelligence_reports`

**Dependencies:**

- Integrations: ACTI Indicator Query
- Scripts: Exists
- Commands: ip, domain, url


## Armis Alert Enrichment

**Product:** Armis

Enrich Armis alerts with the devices in the context details

**Inputs:**

- `Armis_Device_Identifier`: Get the device ID that is associated with the alert.

**Outputs:**

- `Device ID`
- `Armis.Device.name`
- `Armis.Device.riskLevel`
- `Armis.Device.ipAddress`
- `Armis.Device.site`
- `Armis.Device.tags`

**Dependencies:**

- Integrations: Armis
- Commands: armis-search-devices


## ASM Issue Incident Response - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook initiates the response for ASM Issues in  when an incident is investigated. For medium, high, or critical severity, it creates a ServiceNow ticket using the "ServiceNow v2" integration; otherwise, the incident is assigned to an analyst. The ticket is enriched with GTI ASM Issue details, including entity name, status, confidence, tags, UUID, collection info, and other relevant incident information

**Inputs:**

- `issue_uid`: Collection ASM issue UID from incident.
- `incident_severity`: Collect incident severity from incident.
- `onCall`: Set to true to assign only the user that is currently on shift. Default is False.
- `severity_mapping`: Set the ASM Issue severity as per GTI platform.

**Dependencies:**

- Sub-playbooks: Create ServiceNow Ticket
- Scripts: AssignAnalystToIncident, DeleteContext, Print, SetAndHandleEmpty
- Commands: servicenow-update-ticket


## AWS - Enrichment

**Product:** AWS Enrichment and Remediation

Given the IP address this playbook enriches EC2 and IAM information

**Inputs:**

- `AwsIP`: AWS IP in alert
- `AWSAssumeRoleName`: If assuming roles for AWS, this is the name of the role to assume (should be the same for all organizations).
- `Indicator Query`: Indicators matching the indicator query will be used as playbook input.

**Outputs:**

- `AWS.EC2.Instances`
- `AWS.EC2.SecurityGroups`
- `AWSHierarchy`
- `AWS.SSM`

**Dependencies:**

- Integrations: AWS - EC2, AWS - System Manager
- Scripts: Set, AWSAccountHierarchy
- Commands: aws-ec2-describe-instances, aws-ec2-describe-security-groups, aws-ec2-describe-regions, aws-ec2-get-ipam-discovered-public-addresses, aws-ssm-inventory-entry-list, aws-ec2-describe-ipam-resource-discoveries


## Azure - Enrichment

**Product:** Azure Enrichment and Remediation

Given the IP address, this playbook enriches Azure Compute, Azure asset hierarchy path, IAM, and User information

**Inputs:**

- `AzureIP`: Azure IP in alert

**Outputs:**

- `Azure.Compute`
- `Azure.Network`
- `MSGraphIdentity.Role`
- `Account`
- `MSGraphUser`
- `AzureAssetHierarchy`

**Dependencies:**

- Integrations: Entra ID Identity And Access, Entra ID Users, Azure Compute v2, Azure Resource Graph
- Commands: azure-rg-query, azure-vm-get-public-ip-details, azure-vm-get-nic-details, azure-vm-get-instance-details, msgraph-identity-directory-roles-list, msgraph-identity-directory-role-members-list, msgraph-user-get


## Case Investigation - Google SecOps

**Product:** Google SecOps

This playbook investigates a Google SecOps case by retrieving the latest case information, related alerts, and their entities, and updating the case stage. It also calculates severity from IOC scores, updates the incident and case priority accordingly, creates entities in the case from the identified IOCs, and posts a summary comment on the case

**Inputs:**

- `case_id`: The ID of the case.Note: Use gcb-case-list command to retrieve case ID.
- `alert_limit`: Number of alerts to retrieve in the response. The maximum allowed size is 1000.
- `entity_limit`: Number of entities to retrieve in the response. The maximum allowed size is 1000.

**Dependencies:**

- Scripts: DeleteContext, GoogleSecOpsSyncCaseInformation, Set
- Commands: findIndicators, gcb-case-alert-entity-create, gcb-case-comment-create, gcb-case-priority-change, gcb-case-stage-change, setIncident


## ChronicleAsset Investigation - Chronicle

**Product:** Google SecOps

This playbook receives indicators from its parent playbook, performs enrichment and investigation for each one of them, provides an opportunity to isolate and block the hostname or IP address associated with the current indicator, and gives out a list of isolated and blocked entities. This playbook also lists the events fetched for the asset identifier information associated with the indicator

**Inputs:**

- `chronicleasset_value`: The value of the ChronicleAsset indicator.
- `chronicleasset_support_contact`: The support email address for the chronicle asset.
- `auto_block_entities`: Autoblock the detected suspicious IP Address(es). You can manually set this as 'Yes' or 'No' here or you can set it into a 'Chronicle Auto Block Entities' custom incident field.
- `skip_entity_isolation`: Skip the isolation of entities. You can manually set this as 'Yes' or 'No' here or you can set it into a 'Chronicle Skip Entity Isolation' custom incident field.

**Outputs:**

- `IsolatedEntities`
- `PotentiallyBlockedIPs`

**Dependencies:**

- Scripts: SixgillSearchIndicators, DeleteContext


## Cloud Response - AWS

**Product:** AWS Enrichment and Remediation

This playbook provides response actions to AWS. The following are available for execution automatically/manually

**Inputs:**

- `accessKeyRemediationType`: Choose the remediation type for the user's access key.Disable - for disabling the user's access key.Delete - for the user's access key deletion.
- `userRemediationType`: Choose the remediation type for the user involved.Delete - for the user deletion.Revoke - for revoking the user's credentials.
- `resourceRemediationType`: Choose the remediation type for the instances created.Stop - for stopping the instances.Terminate - for terminating the instances.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `autoAccessKeyRemediation`: Whether to execute the access key remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `resourceName`: The resource name to take action on.
- `region`: The resource's region.
- `username`: The username to take action on.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3
- Scripts: Set
- Commands: aws-iam-delete-login-profile, aws-iam-delete-user, aws-iam-update-access-key, aws-ec2-stop-instances, aws-iam-delete-access-key, aws-ec2-terminate-instances


## Cloud Response - Azure

**Product:** Azure Enrichment and Remediation

This playbook provides response actions to Azure. The following are available for execution automatically/manually

**Inputs:**

- `resourceRemediationType`: Choose the remediation type for the instances created.Poweroff - for shutting down the instances.Delete - for deleting the instances.
- `userRemediationType`: Choose the remediation type for the user involved.Disable - for disabling the user.Delete - for deleting the user.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `resourceName`: The resource name to take action on.
- `resourceGroup`: The resource group.
- `username`: The username to take action on.
- `sourceIP`: The source IP address of the attacker.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3
- Scripts: Set
- Commands: azure-vm-poweroff-instance, azure-vm-delete-instance, msgraph-user-delete, msgraph-user-account-disable


## Cloud Response - GCP

**Product:** GCP Enrichment and Remediation

This playbook provides response actions to GCP. The following are available for execution automatically/manually

**Inputs:**

- `accessKeyRemediationType`: Choose the remediation type for the user's access key.Disable - For disabling the user's access key.Delete - For deleting user's access key.
- `userRemediationType`: Choose the remediation type for the user involved.Delete - For deleting the user.Disable - For disabling the user.
- `resourceRemediationType`: Choose the remediation type for the instances created.Stop - For stopping the instances.Delete - For deleting the instances.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `autoAccessKeyRemediation`: Whether to execute the access key remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `resourceName`: The resource name to take action on.
- `resourceZone`: The resource's zone.
- `username`: The username to take action on.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3
- Scripts: Set
- Commands: gcp-iam-service-account-disable, gcp-iam-service-account-key-disable, gsuite-user-delete, gcp-compute-stop-instance, gcp-iam-service-account-delete, gcp-iam-service-account-key-delete, gcp-compute-delete-instance


## Code42 File Download

**Product:** Code42

This playbook downloads a file via Code42 by either MD5 or SHA256 hash

**Inputs:**

- `XFC ID`: XFC Event ID to search for
- `MD5`: MD5 hash to search for
- `SHA256`: SHA256 hash to search for
- `Filename`: The name of the file to save as.

**Outputs:**

- `File.Size`
- `File.SHA1`
- `File.SHA256`
- `File.Name`
- `File.SSDeep`
- `File.EntryID`
- `File.Info`
- `File.Type`
- `File.MD5`
- `File.Extension`

**Dependencies:**

- Integrations: Code42
- Commands: code42-download-file


## Codecov Breach - Bash Uploader

**Product:** Rapid Breach Response

This playbook includes the following tasks: More information: Codecov Security Notice

**Inputs:**

- `KnownRelatedIOCs`: Known related IOCs to the Codecov Bash Uploader breach to hunt.
- `CustomIOCs`: Add your own custom Codecov Bash Uploader breach IOCs to hunt.
- `EWSSearchQuery`: The EWS query to find the Codecov security notice email
- `EWSSearchQuery_Limit`: The limit of results to return from the search
- `Github_Code_Search_query`: Github query to search for Codecov bash uploader use.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.

**Dependencies:**

- Sub-playbooks: Splunk Indicator Hunting, Panorama search thread-ids in threat logs, QRadar Indicator Hunting V2, Palo Alto Networks - Hunting And Threat Detection
- Commands: extractIndicators, GitHub-search-code, ews-search-mailbox


## Cortex ASM - Active Directory Enrichment

**Product:** Cortex Attack Surface Management

Playbook to enriches Service ownership info in Azure and On-Prem Active Directory

**Inputs:**

- `serviceowner`: The service owner to enrich in Azure directory.

**Dependencies:**

- Integrations: Microsoft Graph User, Active Directory Query v2
- Scripts: Set, GridFieldSetup
- Commands: msgraph-user-get, ad-get-user


## Cortex ASM - AWS Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches AWS information relevant to ASM alerts

**Inputs:**

- `RemoteIP`: IP address of service
- `ASMRuleID`: Attack Surface Management Rule ID.
- `AWSAssumeRoleName`: If assuming roles for AWS, this is the name of the role to assume (should be the same for all organizations).

**Dependencies:**

- Sub-playbooks: AWS - Enrichment, AWS - Unclaimed S3 Bucket Validation
- Scripts: GridFieldSetup, Set
- Commands: setAlert


## Cortex ASM - Azure Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address, this playbook enriches Azure information relevant to ASM alerts

**Inputs:**

- `RemoteIP`: IP address of service.

**Dependencies:**

- Scripts: GetTime, GridFieldSetup


## Cortex ASM - CMDB Enrichment

**Product:** Cortex Attack Surface Management

This playbook will look up a CI in ServiceNow CMDB by IP

**Inputs:**

- `IP`: IP address to search in ServiceNow

**Dependencies:**

- Integrations: ServiceNow CMDB
- Commands: servicenow-cmdb-records-list, servicenow-cmdb-record-get-by-id


## Cortex ASM - GCP Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches GCP and Firewall information

**Inputs:**

- `RemoteIP`: IP address of service

**Dependencies:**

- Sub-playbooks: GCP - Enrichment
- Scripts: Set GridFieldSetup


## Cortex ASM - On Prem Enrichment

**Product:** Cortex Attack Surface Management

Given an IP address, port, and protocol of a service, this playbook enriches on-prem integrations to find the related firewall rule and other related information. Conditions

**Inputs:**

- `RemoteIP`: IP address of the service.
- `RemotePort`: Port number of the service.
- `RemoteProtocol`: Protocol of the service.

**Dependencies:**

- Integrations: Panorama
- Scripts: GridFieldSetup, Set
- Commands: pan-os-security-policy-match, pan-os-platform-get-device-groups, pan-os-list-rules, pan-os-show-device-version


## Cortex ASM - Rapid7 Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches Rapid7 InsightVM (Nexpose) information relevant to ASM alerts

**Inputs:**

- `IPAddress`: IP addresses to enrich.

**Dependencies:**

- Sub-playbooks: Rapid7 - Nexpose - Enrichment
- Scripts: GetTime, GridFieldSetup


## Cortex ASM - Splunk Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches information from Splunk results relevant to ASM alerts

**Inputs:**

- `IP`: Remote IP in an incident/alert.

**Dependencies:**

- Scripts: GetTime, GridFieldSetup
- Commands: splunk-search


## Cortex XDR - Endpoint Investigation

**Product:** Cortex XDR by Palo Alto Networks

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook handles all the endpoint investigation actions available with  , including the following tasks

**Inputs:**

- `HuntReconnaissanceTechniques`: Set to True to hunt for identified alerts with MITRE Reconnaissance techniques.
- `HuntInitialAccessTechniques`: Set to True to hunt for identified alerts with MITRE Access techniques.
- `HuntExecutionTechniques`: Set to True to hunt for identified alerts with MITRE Execution techniques.
- `HuntPersistenceTechniques`: Set to True to hunt for identified alerts with MITRE Persistence techniques.
- `HuntPrivilegeEscalationTechniques`: Set to True to hunt for identified alerts with MITRE Privilege Escalation techniques.
- `HuntDefenseEvasionTechniques`: Set to True to hunt for identified alerts with MITRE Defense Evasion techniques.
- `HuntDiscoveryTechniques`: Set to True to hunt for identified alerts with MITRE Discovery techniques.
- `HuntLateralMovementTechniques`: Set to True to hunt for identified alerts with MITRE Lateral Movement techniques.
- `HuntCollectionTechniques`: Set to True to hunt for MITRE Collection techniques identified alerts.
- `HuntCnCTechniques`: Set to True to hunt for identified alerts with MITRE Command and Control techniques.

**Outputs:**

- `PaloAltoNetworksXDR.Alert`
- `PaloAltoNetworksXDR.Alert.internal_id`
- `PaloAltoNetworksXDR.Alert.source_insert_ts`
- `PaloAltoNetworksXDR.Alert.alert_name`
- `PaloAltoNetworksXDR.Alert.severity`
- `PaloAltoNetworksXDR.Alert.alert_category`
- `PaloAltoNetworksXDR.Alert.alert_action_status`
- `PaloAltoNetworksXDR.Alert.alert_action_status_readable`
- `PaloAltoNetworksXDR.Alert.alert_description`
- `PaloAltoNetworksXDR.Alert.agent_ip_addresses`

**Dependencies:**

- Integrations: CortexXDRIR
- Commands: xdr-get-alerts


## Cortex XDR - Malware Investigation

**Product:** Cortex XDR by Palo Alto Networks

Investigates a  XDR incident containing internal malware alerts. The playbook: The playbook is used as a sub- playbook in ‘ XDR Incident Handling - v2’

**Inputs:**

- `xdr_alert_id`: Unique ID for the XDR alert.
- `host_ip`: Host IP involved in the alert.
- `file_name`: The name of the malicious file.
- `file_sha256`: SHA-256 hash of the file.
- `file_path`: Full Path of the file.
- `endpoint_id`: the endpoint_id

**Outputs:**

- `Joe.Analysis`
- `File`
- `File.Malicious`
- `DBotScore`
- `IP`
- `DBotScore.Malicious`
- `Sample`
- `InfoFile`
- `WildFire`
- `WildFire.Report`

**Dependencies:**

- Sub-playbooks: Cortex XDR - Retrieve File v2, Detonate File - Generic
- Integrations: Cortex XDR - IR
- Scripts: SetMultipleValues
- Commands: xdr-get-endpoints


## Cortex XDR - Port Scan - Adjusted

**Product:** Cortex XDR by Palo Alto Networks

The playbook investigates  XDR incidents involving port scan alerts. The playbook is designed to run as a sub-playbook of ‘ XDR Alerts Handling’. The playbook consists of the following procedures: This playbook supports the following  XDR alert names

**Inputs:**

- `InternalIPRanges`: A list of IP ranges to check the IP against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.0.0.0/8,192.168
- `Username`: The user name used for port scanning.
- `SrcIPAddress`: The source IP address from which the port scanning was initiated.
- `DstIPAddress`: Scanned destination IP address.
- `DstPort`: Scanned port numbers.
- `EarlyContainment`: Whether early containment should be allowed when the IP address is known to be malicious.Possible values:True/False. Default:True.
- `SrcHostname`: Source host name from which port scanning was initiated.
- `EndpointID`: Source endpoint ID from which port scanning was initiated.
- `Initiator_CMD`: The command used to initiate port scan activity.
- `Initiator_Process_SHA256`: Process SHA256 file hash initiated port scanning.

**Outputs:**

- `PortScan.BlockPorts`
- `PortScan.AttackerIPs`
- `PortScan.AttackerHostnames`
- `PortScan.AttackerUsername`
- `PortScan.FileArtifacts`
- `PortScan.LateralMovementFirstDatetime`
- `PortScan.PortScanFirstDatetime`

**Dependencies:**

- Sub-playbooks: Cortex XDR - Endpoint Investigation, Account Enrichment - Generic v2.1, Cortex XDR - Isolate Endpoint, TIM - Indicator Relationships Analysis, User Investigation - Generic, Command-Line Analysis, Block Indicators - Generic v3, File Enrichment - Generic v2
- Scripts: IsIPInRanges, GetTime, Set
- Commands: setIncident


## Cortex XDR - Port Scan

**Product:** Cortex XDR by Palo Alto Networks

Investigates a  XDR incident containing internal port scan alerts. The playbook

**Inputs:**

- `BlockAttackerIP`: Whether attacking IPs should be automatically blocked using firewalls.
- `WhitelistedHostnames`: A list of comma-separated hostnames that should not be isolated even if used in an attack.
- `EmailAddressesToNotify`: A list of comma-separated values of email addresses that should receive a notification about compromised hosts.
- `CriticalUsernames`: A list of comma-separated names of critical users in the organization. This will affect the calculated severity of the incident.
- `IsolateEndpointAutomatically`: Whether to automatically isolate endpoints, or opt for manual user approval. True means isolation will be done automatically.
- `InternalIPRanges`: A list of IP ranges to check the IP against. The list should be provided in CIDR notation, separated by commas. An example of a list of ranges would be: "172.16.0.0/12,10.0.0.0/8,1
- `CriticalHostnames`: A list of comma-separated names of critical endpoints in the organization. This will affect the calculated severity of the incident.
- `RoleForEscalation`: The name of the the platform.
- `BlockMaliciousFiles`: Whether to automatically block malicious files involved with the incident across all endpoints in the organization.
- `CriticalADGroups`: CSV of DN names of critical Active Directory groups. This will affect the severity calculated for this incident.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3, IP Enrichment - Internal - Generic v2, Block File - Generic v2, Isolate Endpoint - Generic V2, Calculate Severity - Generic v2, PANW - Hunting and threat detection by indicator type V2
- Integrations: CortexXDRIR
- Scripts: AssignAnalystToIncident, IsIPInRanges, StopScheduledTask, SetAndHandleEmpty, XDRSyncScript
- Commands: closeInvestigation, xdr-get-endpoints, xdr-update-incident, send-mail, setIncident


## Cortex XDR - PrintNightmare Detection and Response

**Product:** Cortex XDR by Palo Alto Networks

The playbook targets specific PrintNightmare rules written by  XDR for both vulnerabilities: CVE-2021-1675 LPE CVE-2021-34527 RCE This playbook includes the following tasks: ** Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `IsolateEndpointAutomatically`: Whether to isolate the endpoint automatically
- `DisableAccountAutomatically`: Whether to disable the account automatically
- `BlockIPAutomatically`: Whether to block the IP Address automatically
- `EnrichAutomatically`: Whether to run indicators auto enrichment automatically
- `UserVerification`: Possible values: True/False.Whether to provide user verification for blocking IPs. False - No prompt will be displayed to the user.True - The server will ask the user for blocking 

**Dependencies:**

- Sub-playbooks: Account Enrichment - Generic v2.1, Endpoint Enrichment - Generic v2.1, Cortex XDR - Isolate Endpoint, Block IP - Generic v3, Threat Hunting - Generic
- Integrations: CortexXDRIR
- Scripts: SearchIncidentsV2
- Commands: ad-disable-account, enrichIndicators, xdr-get-incident-extra-data


## Cortex XDR device control violations

**Product:** Cortex XDR by Palo Alto Networks

Queries  XDR for device control violations for the specified hosts, IP address, or XDR endpoint ID. It then communicates via email with the involved users to understand the nature of the incident and if the user connected the device. All the collected data will be displayed in the XDR device control incident layout. This playbook can also be associated with  XDR device control violation job to periodically query and investigate XDR device control violations. In this configuration, the playbook will only communicate with the involved users

**Inputs:**

- `TimeStamp`: Timestamp in relative date format for query device control eventsfrom Cortex XDR.For example "1 day", "3 weeks".
- `EndpointID`: Comma-separated list of endpoint IDs to filter results for.
- `Hostname`: Comma-separated list of hostnames to filter results for.
- `IPAddress`: Comma-separated list of endpoints IP addresses to filter results for.
- `MessageSubject`: The subject of the message for communication with the involved users.
- `MessageBody`: A body of the message for communication with the involved users.

**Dependencies:**

- Integrations: CortexXDRIR
- Scripts: Set, SetGridField
- Commands: ad-get-user, xdr-get-endpoint-device-control-violations


## Cortex XDR Malware - Incident Enrichment

**Product:** Cortex XDR by Palo Alto Networks

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook enriches the  XDR incident. The enrichment is done on the involved endpoint and Mitre technique ID information, and sets the 'Malware-Investigation and Response' layout

**Inputs:**

- `IncidentID`: The incident ID to be enriched.

**Outputs:**

- `PaloAltoNetworksXDR.Incident`
- `File`
- `Process`
- `IP`
- `Domain`
- `Endpoint.ID`
- `Endpoint.Hostname`
- `Endpoint.OS`
- `Endpoint.OSVersion`
- `Endpoint.IPAddress`

**Dependencies:**

- Sub-playbooks: Mitre Attack - Extract Technique Information From ID, Account Enrichment - Generic v2.1
- Integrations: Cortex XDR - IR, CortexXDRIR
- Scripts: isError, SetGridField
- Commands: extractIndicators, endpoint, xdr-get-incident-extra-data, setIncident


## CrowdStrike Falcon Malware - Incident Enrichment

**Product:** CrowdStrike Falcon

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook enables enriching CrowdStrike Falcon incidents by pivoting to their detections as well as mapping all the relevant data to the   incident fields

**Inputs:**

- `DetectionOrCaseID`: The ID of the CrowdStrike detection or Case.

**Outputs:**

- `CrowdStrike`
- `Endpoint`
- `CrowdStrike.FoundDetections`

**Dependencies:**

- Sub-playbooks: Account Enrichment - Generic v2.1, CrowdStrike Falcon - Get Detections by Case
- Integrations: CrowdstrikeFalcon
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty, SetGridField, SetMultipleValues, isError
- Commands: endpoint, extractIndicators, setIncident


## CVE-2021-34527 | CVE-2021-1675 - PrintNightmare

**Product:** Rapid Breach Response

The playbook can be triggered manually or automatically by setting up a reoccurring job. Microsoft has released a security update in June 2021 Patch Tuesday for CVE-2021-1675, a Local Privilege Escalation vulnerability in the Print Spooler Service. Later that month, researchers found another method to exploit the Print Spooler service remotely, which raised the severity of the vulnerability due to the fact that the new method allows Remote Code Execution, a new ID was given to the critical vulnerability - CVE-2021-34527. Microsoft patched the vulnerability in June but an exploit POC and complete technical analysis were made publicly available online. **Update 7.8.2021 - Microsoft has released an emergency patch for the PrintNightmare. A reference for the patch can be found in "Install Microsoft spooler service patches" task. This playbook includes the following tasks: More details on the vulnerabilities: CVE-2021-1675 LPE CVE-2021-34527 RCE ** Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `CVE`: PrintNightmare CVEs
- `SplunkEarliestTime`: The earliest time for the Splunk search query.
- `SplunkLatestTime`: The latest time for the Splunk search query.

**Dependencies:**

- Sub-playbooks: Cortex XDR - PrintNightmare Detection and Response, QRadarFullSearch, Search Endpoint by CVE - Generic, Panorama Query Logs
- Commands: closeInvestigation, splunk-search


## CVE-2021-22893 - Pulse Connect Secure RCE

**Product:** Rapid Breach Response

On April 20th, a new Remote Code Execution vulnerability in Pulse Connect Secure was disclosed. The reference number for the vulnerability is CVE-2021-22893 with the CVSS Score of 10.0. This playbook should be trigger manually and includes the following tasks: Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve. More information: Exploitation of Pulse Connect Secure Vulnerabilities

**Inputs:**

- `Related_Hashes`: The known hashes of different malware families associated with the exploitation.
- `Related_CVEs`: The known CVEs associated with the exploitation.
- `BlockAutomatically`: Whether to block the indicators automatically.Default: False.
- `QRadarWebshellsQuery`: The QRadar search query used for "Hunt Activity Using QRadar".Please note that there aren't specified fields which may cause a longer run time.
- `SplunkWebshellsQuery`: The Splunk search query used for "Hunt Activity Using Splunk".Please note that there are two specified fields: msg, message. the query will work for both field names.
- `RunWebshellsQuery`: If you would like to skip "Hunt Activity Using Splunk" OR "Hunt Activity Using Qradar" please change the value to 'False'.
- `QRadar_MD5_Field`: The name of the field for MD5 entries in QRadar.If not configured, QRadar Indicator Hunting may reach timeout.
- `QRadar_SHA1_Field`: The name of the field for SHA1 entries in QRadar.If not configured, QRadar Indicator Hunting may reach timeout.
- `QRadar_SHA256_Field`: The name of the field for SHA256 entries in QRadar.If not configured, QRadar Indicator Hunting may reach timeout.
- `SplunkEarliestTime`: The earliest time for the Splunk search query.

**Dependencies:**

- Sub-playbooks: QRadar Indicator Hunting V2, QRadarFullSearch, Search Endpoint by CVE - Generic, Palo Alto Networks - Hunting And Threat Detection, Block Indicators - Generic v2, Splunk Indicator Hunting
- Commands: expanse-get-issues, enrichIndicators, splunk-search, extractIndicators


## CVE Exposure - RiskSense

**Product:** RiskSense

Block IPs and apply the tag to assets that are vulnerable to specified CVE

**Inputs:**

- `CVES`: Specify Common Vulnerabilities and Exposures (CVE). You can mention multiple CVEs using a comma-separated list.
- `TagName`: Tags in RiskSense can be applied to assets, web applications, and vulnerabilities. Tags are useful in the soft grouping, workflow creation, and to identify compliance-related asset

**Outputs:**

- `RiskSense.TagAssociation`
- `RiskSense.HostFinding`
- `RiskSense.Host`

**Dependencies:**

- Sub-playbooks: Block IP - Generic v2
- Integrations: RiskSense
- Scripts: IsIntegrationAvailable
- Commands: risksense-apply-tag, risksense-get-hosts, risksense-get-host-findings


## Cybereason - Download Close File

**Product:** Cybereason

This playbook aborts a file download operation which is in progress based on the Malop ID and username provided

**Inputs:**

- `malopGUID, userName`: Malop GUID for fetching a file from a sonsor to download, The complete Cybereason user name string for the user performing the request

**Dependencies:**

- Commands: cybereason-start-fetchfile, cybereason-fetchfile-progress, cybereason-close-file-batch-id


## Darkfeed - malware download from feed

**Product:** Sixgill Darkfeed - Annual Subscription

**Inputs:**

- `Indicator Query`: Indicators matching the indicator query will be used as playbook input

**Dependencies:**

- Sub-playbooks: Darkfeed IOC detonation and proactive blocking
- Scripts: SetAndHandleEmpty


## Darkmon - Compromised Account Response

**Product:** Darkmon

Incident-type playbook for 'Darkmon Compromised Credential' (and similar). Identifies the user via the configured directory, suspends, forces a password reset, revokes active sessions, and notifies SOC + the user

**Dependencies:**

- Sub-playbooks: Disable account, Force password reset, Notify SOC + user, Revoke active sessions


## Darkmon - EDR Alert Enrichment

**Product:** Darkmon

Designed to be invoked from CrowdStrike / SentinelOne / Defender alert playbooks. Takes the alert's IOCs, enriches each via Darkmon, and if any are scored Bad, escalates incident severity and notifies the SOC. Endpoint containment is left to the EDR-specific playbook

**Outputs:**

- `DBotScore`

**Dependencies:**

- Sub-playbooks: Enrich IOCs via Darkmon (URL pass), Notify SOC
- Scripts: Set


## Darkmon - Phishing Email Triage

**Product:** Darkmon

Extracts URLs/IPs/file-hashes from a reported phishing email, enriches each via the Darkmon - Enrich * sub-playbooks, and if any indicator is scored Bad (DBotScore=3) calls Generic Block Indicator on it. Notifies the reporter and the SOC at the end

**Outputs:**

- `ExtractedIndicators`
- `DBotScore`

**Dependencies:**

- Sub-playbooks: Block malicious indicators, Enrich each IOC via Darkmon, Notify SOC, Notify reporter
- Scripts: ExtractIndicatorsFromTextFile


## Digital Shadows - CVE_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of CVE IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_CVE`: A Digital Shadows ShadowSearch query containing CVE IDs

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## Digital Shadows - Domain_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of Domain IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_Domain`: A Digital Shadows ShadowSearch query containing domains

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## Digital Shadows - IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrich indicators by providing intelligence and more associated indicators based on confirmed reporting in Digital Shadows SearchLight

**Inputs:**

- `IoC_IP`: An IP address for assessment and enrichment
- `IoC_CVE`: A CVE for assessment and enrichment
- `IoC_Domain`: A domain for assessment and enrichment
- `IoC_URL`: A URL for assessment and enrichment
- `IoC_MD5`: A MD5 hash for assessment and enrichment
- `IoC_SHA256`: A SHA256 hash for assessment and enrichment
- `IoC_SHA1`: A SHA1 hash for assessment and enrichment

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Sub-playbooks: Digital Shadows - CVE_IoC Assessment & Enrichment, Digital Shadows - URL_IoC Assessment & Enrichment, Digital Shadows - SHA1_IoC Assessment & Enrichment, Digital Shadows - MD5_IoC Assessment & Enrichment, Digital Shadows - IP_IoC Assessment & Enrichment, Digital Shadows - SHA256_IoC Assessment & Enrichment, Digital Shadows - Domain_IoC Assessment & Enrichment


## Digital Shadows - IP_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of IP IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_IP`: A Digital Shadows ShadowSearch query containing IP addresses

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## Digital Shadows - MD5_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of MD5 IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_MD5`: A Digital Shadows ShadowSearch query containing MD5 hashes

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: AddEvidence, Print
- Commands: ds-search


## Digital Shadows - SHA1_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of SHA1 IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_SHA1`: A Digital Shadows ShadowSearch query containing SHA1 hashes

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: AddEvidence, Print
- Commands: ds-search


## Digital Shadows - SHA256_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of SHA256 IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_SHA256`: A Digital Shadows ShadowSearch query containing SHA256 hashes

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: AddEvidence, Print
- Commands: ds-search


## Digital Shadows - URL_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of URL IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_URL`: A Digital Shadows ShadowSearch query containing URLs

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## DTM Alert Incident Response - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook initiates the response for DTM Alerts in  when an incident is investigated. For medium or higher severity, it creates a ServiceNow ticket using the "ServiceNow v2" integration; otherwise, the incident is assigned to an analyst. The ticket is enriched with GTI DTM Alert details, including alert type, status, monitor information, summary, AI Doc summary, and tags

**Inputs:**

- `alert_id`: Collection DTM Alert ID from incident.
- `incident_severity`: Collect incident severity from incident.
- `onCall`: Set to true to assign only the user that is currently on shift. Default is False.
- `severity_mapping`: Set the alert severity mapping as per GTI platform.

**Dependencies:**

- Sub-playbooks: Create ServiceNow Ticket
- Scripts: AssignAnalystToIncident, DeleteContext, Print, SetAndHandleEmpty
- Commands: servicenow-update-ticket


## Endpoint Investigation Plan

**Product:** Common Playbooks

This playbook handles all the endpoint investigation actions by performing the following tasks on every alert associated with the incident: Note: The playbook inputs enable manipulating the execution flow; read the input descriptions for details

**Inputs:**

- `HuntReconnaissanceTechniques`: Set to True to hunt for identified alerts with MITRE Reconnaissance techniques.
- `HuntInitialAccessTechniques`: Set to True to hunt for identified alerts with MITRE Access techniques.
- `HuntExecutionTechniques`: Set to True to hunt for identified alerts with MITRE Execution techniques.
- `HuntPersistenceTechniques`: Set to True to hunt for identified alerts with MITRE Persistence techniques.
- `HuntPrivilegeEscalationTechniques`: Set to True to hunt for identified alerts with MITRE Privilege Escalation techniques.
- `HuntDefenseEvasionTechniques`: Set to True to hunt for identified alerts with MITRE Defense Evasion techniques.
- `HuntDiscoveryTechniques`: Set to True to hunt for identified alerts with MITRE Discovery techniques.
- `HuntLateralMovementTechniques`: Set to True to hunt for identified alerts with MITRE Lateral Movement techniques.
- `HuntCollectionTechniques`: Set to True to hunt for MITRE Collection techniques identified alerts.
- `HuntCnCTechniques`: Set to True to hunt for identified alerts with MITRE Command and Control techniques.

**Dependencies:**

- Scripts: SearchIncidentsV2


## File Private Scanning - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook submits a file for private scanning, retrieves and evaluates the analysis verdict, and automatically creates a ServiceNow ticket using the "ServiceNow v2" integration when the file is determined to be malicious

**Inputs:**

- `file_id`: Fetch the Entry ID of the last submitted file from the incident.

**Dependencies:**

- Sub-playbooks: Create ServiceNow Ticket
- Scripts: DeleteContext, Print
- Commands: gti-private-file-scan-and-analysis-get, servicenow-update-ticket


## GCP - Enrichment

**Product:** GCP Enrichment and Remediation

Given the IP address this playbook enriches GCP and Firewall information

**Inputs:**

- `GcpIP`: GCP IP in alert
- `port`: Port to match traffic on for firewall rules.
- `protocol`: Protocol to match traffic on for firewall rules.

**Outputs:**

- `GoogleCloudCompute.Instances`
- `GCPIAM.Policy`
- `GCPIAM.TagBindings`
- `GCPHierarchy`
- `GCPOffendingFirewallRule`

**Dependencies:**

- Integrations: GCP-IAM, Google Cloud Compute
- Scripts: GCPOffendingFirewallRule, Set, GCPProjectHierarchy
- Commands: gcp-iam-tagbindings-list, gcp-iam-project-iam-policy-get, gcp-compute-aggregated-list-instances-by-ip, gcp-compute-get-instance


## Get entity alerts by MITRE tactics

**Product:** Core

This playbook searches XDR alerts related to specific entities, on a given timeframe, based on MITRE tactics. Note: The playbook's inputs enable manipulating the execution flow. Read the input descriptions for details

**Inputs:**

- `HuntReconnaissanceTechniques`: Set to True to hunt for identified alerts with MITRE Reconnaissance techniques.
- `HuntInitialAccessTechniques`: Set to True to hunt for identified alerts with MITRE Initial Access techniques.
- `HuntExecutionTechniques`: Set to True to hunt for identified alerts with MITRE Execution techniques.
- `HuntPersistenceTechniques`: Set to True to hunt for identified alerts with MITRE Persistence techniques.
- `HuntPrivilegeEscalationTechniques`: Set to True to hunt for identified alerts with MITRE Privilege Escalation techniques.
- `HuntDefenseEvasionTechniques`: Set to True to hunt for identified alerts with MITRE Defense Evasion techniques.
- `HuntDiscoveryTechniques`: Set to True to hunt for identified alerts with MITRE Discovery techniques.
- `HuntLateralMovementTechniques`: Set to True to hunt for identified alerts with MITRE Lateral Movement techniques.
- `HuntCollectionTechniques`: Set to True to hunt for identified alerts with MITRE Collection techniques .
- `HuntCnCTechniques`: Set to True to hunt for identified alerts with MITRE Command and Control techniques.

**Outputs:**

- `foundIncidents`

**Dependencies:**

- Scripts: SearchAlertsV2, SetAndHandleEmpty


## Hunt Extracted Hashes V2

**Product:** Hunting

This playbook extracts IOCs from the incident details and attached files using regular expressions and then hunts for hashes on endpoints in the organization using available tools. The playbook supports multiple types of attachments. For the full supported attachments list, refer to "Extract Indicators From File - Generic v2"

**Inputs:**

- `File`: The file from which to extract indicators.

**Dependencies:**

- Sub-playbooks: Extract Indicators From File - Generic v2, Search Endpoints By Hash - Generic V2
- Commands: extractIndicators


## Incident Enrichment - XM Cyber

**Product:** XM Cyber

This playbook enriches the incident using the hostname indicators and user data and increases the severity based on the calculated risk score and pushes breach points of the identified entities to XM Cyber

**Inputs:**

- `entity_values`: Specify the hostname or user entity. Supports comma separated values.
- `compromise_risk_score`: Specify the weight of Compromise Risk Score to apply to the final score calculation. Provide the value between 0 and 1.
- `choke_point_score`: Specify the weight of Choke Point Score to apply to the final score calculation. Provide the value between 0 and 1.
- `attribute_name`: The name of the custom label you want to push to CEM as an imported attribute.
- `parameter`: When setting up the condition for when to push the breach point data, this is the parameter of the condition. It is a list of predefined parameters for determining the criteria. Se
- `operator`: When setting up the condition for when to push the breach point data, this is the operator of the condition.Possible values are: Less than, Greater than, Less than equal to, Greate
- `value`: When setting up the condition for when to push the breach point data, this is the value of the condition. Can be boolean, string, integer, float, or date values.Supported date form

**Dependencies:**

- Scripts: DeleteContext, Set
- Commands: findIndicators, setIncident, xmcyber-calculate-risk-score, xmcyber-enrich-incident, xmcyber-push-breach-point, xmcyber-remove-breach-point


## Investigate On Bad Domain Matches - Chronicle

**Product:** Google SecOps

Use this playbook to investigate and remediate Bad IOC domain matches with recent activity found in the enterprise, as well as notify the SOC lead and network team about the matches. Supported Integrations

**Inputs:**

- `networkteam_email`: Enter the email address of the network team that needs to be notified.
- `stakeholder_email`: Enter the email of the stakeholder to whom you want to send the investigation summary report.

**Dependencies:**

- Integrations: Chronicle, Google SecOps, Whois, Mail Sender (New), Palo Alto Networks PAN-OS, Palo Alto Networks AutoFocus v2
- Scripts: AssignAnalystToIncident, GenerateInvestigationSummaryReport, Print
- Commands: domain, gcb-assets, gcb-ioc-details, pan-os-register-user-tag, send-mail, whois


## IOCs Curated Threat Intelligence Enrichment - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook extracts IOCs from incident details and enriches the selected IOCs with curated Google Threat Intelligence data, including malware families, campaigns, and threat actors

**Dependencies:**

- Sub-playbooks: IOC Curated Enrichment - Google Threat Intelligence
- Scripts: DeleteContext
- Commands: findIndicators


## IOC Alert

**Product:** Core

IOCs provide the ability to alert on known malicious objects on endpoints across the organization. Analysis Actions: The playbook will use several enrichment sources to determine the IOC verdict. Additionally, will use the Analytics module to run a prevalence check for the IOC. Response Actions: The playbook's first response action is a containment plan that is based on the playbook input. In that phase, the playbook will execute endpoint isolation Investigative Actions: When the playbook executes, it checks for additional abnormal activity using the Endpoint Investigation Plan playbook that can indicate the endpoint might be compromised. Remediation Actions: In case results are found within the investigation phase, the playbook will execute remediation actions that include containment and eradication. This phase will execute the following containment actions: And the following eradication actions

**Inputs:**

- `BlockIndicatorsAutomatically`: Whether to block suspicious/malicious indicators automatically. Specify True/False.
- `ShouldCloseAutomatically`: Whether to close the alert automatically if it's established verdict is False Positive. Specify True/False.
- `PreHostContainment`: Whether to isolate the host before the investigation phase in case an IOC was found to be suspicious. Specify True/False.
- `ShouldHandleFPautomatically`: Whether to automatically handle false positive alerts. Specify true/false.
- `AutoRestoreEndpoint`: Whether to execute the Recovery playbook. Specify True/False.
- `AutoContainment`: Setting this input will impact both Containment Plan sub-playbooks. Without setting this input, the default values are True for the first occurrence and False for the second.Whethe
- `FileRemediation`: Should be either 'Quarantine' or 'Delete'.
- `AutoEradication`: Whether to execute automatically or manually the eradication plan tasks:* Terminate process* Delete file* Reset the user's passwordSpecify True/False.
- `ShouldOpenTicket`: Whether to open a ticket automatically in a ticketing system. (True/False).
- `serviceNowShortDescription`: A short description of the ticket.

**Dependencies:**

- Sub-playbooks: Endpoint Investigation Plan, Recovery Plan, Eradication Plan, Enrichment for Verdict, Handle False Positive Alerts, Ticket Management - Generic, Containment Plan
- Commands: extractIndicators, setParentIncidentFields, closeInvestigation


## IOC Curated Enrichment - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook provides IOC curated enrichment using Google Threat Intelligence data, including malware families, campaigns, and threat actors, and displays the results in the War Room for investigation

**Inputs:**

- `resource`: The file hash (MD5, SHA1, or SHA256), Domain, URL or IP.
- `resource_type`: The type of the resource (IP, domain, URL, or file hash).

**Dependencies:**

- Scripts: DeleteContext, Print, SetAndHandleEmpty
- Commands: gti-curated-campaigns-get, gti-curated-malware-families-get, gti-curated-threat-actors-get


## IOC Enrichment and Blocking - Google SecOps

**Product:** Google SecOps

This playbook enriches IOCs using the enrichment commands (IP, Email, Domain, URL, and File) and blocks the malicious IOCs based on DBot Score

**Dependencies:**

- Sub-playbooks: Block Domain - Generic v2, Block Email - Generic v2, Block File - Generic v2, Block IP - Generic v3, Block URL - Generic v2
- Scripts: DeleteContext, SetAndHandleEmpty
- Commands: domain, email, file, findIndicators, ip, url


## IOC Enrichment and Blocking - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook enriches IOCs using the GTI enrichment commands (IP, Domain, URL, and File) and blocks the IOCs based on GTI assessment parameters such as Threat Score, Severity, and Verdict

**Inputs:**

- `ip_addresses`: Provide a comma-separated list of IPs.
- `domains`: Provide a comma-separated list of Domains.
- `files`: Provide a comma-separated list of Files.
- `urls`: Provide a comma-separated list of URLs.

**Dependencies:**

- Sub-playbooks: Block Domain - Generic v2, Block File - Generic v2, Block IP - Generic v3, Block URL - Generic v2
- Scripts: DeleteContext, Set
- Commands: domain, file, findIndicators, ip, url


## Large Upload Alert

**Product:** Core

The playbook investigates  XDR alerts involving large upload alerts. The playbook consists of the following procedures

**Inputs:**

- `InternalIPRanges`: A list of IP ranges to check the IP against. The list should be provided in CIDR notation, separated by commas. An example of a list of ranges would be: "172.16.0.0/12,10.0.0.0/8,1
- `FurtherInvestigation`: Determines whether an alert should be further investigated if similar previous false positive alerts were found.Possible values:True/False. Default: False.
- `AutoBlockIndicators`: Determine whether the given indicators be automatically blocked, or if the user should be given the option to choose.Possible values:True/False. Default: True.If set to True - no p
- `BlockIndicators_UserVerification`: Determine whether the blocking of any indicator requires the verification of the user.Possible values:True/False. Default: False.
- `EarlyContainment`: Whether early containment should be allowed when the IP address is known to be malicious.Possible values:True/False. Default: True.
- `AutoIsolateEndpoint`: Whether to isolate the initiating endpoint automatically if the investigation verdict is malicious.Possible values:True/False. Default: False.
- `Transferred_Data _Threshold`: Specify the uploaded data threshold volume (in MB) from which large upload alerts should be investigated.By setting a threshold, you will be able to determine which large upload al
- `FWApps_Processes_Whitlist`: A list of known and authorized FW application IDs and processes used in the organization.
- `Alert_ID`: The Cortex XDR alert ID.

**Dependencies:**

- Sub-playbooks: Block Indicators - Generic v3, User Investigation - Generic, TIM - Indicator Relationships Analysis, Command-Line Analysis, Threat Hunting - Generic, Entity Enrichment - Generic v3, Endpoint Investigation Plan, Search and Compare Process Executions - Generic
- Integrations: CortexCoreIR
- Scripts: DBotFindSimilarIncidents, SetAndHandleEmpty, Set
- Commands: setAlertStatus, core-isolate-endpoint, setAlert, core-get-cloud-original-alerts


## Malware Investigation & Response Incident Handler

**Product:** Malware Investigation and Response

This playbook is triggered by a malware incident from an endpoint integration. It performs enrichment, detonation, and hunting within the organization, and remediation on the malware. The playbook also covers the SIEM ingestion flow in which the fetching integration is the SIEM and EDR integrations grab all additional data. Currently supported EDR integrations are XDR, CrowdStrike Falcon, and Microsoft Defender for Endpoint. Currently supported SIEM integrations are QRadar and Splunk

**Inputs:**

- `OnCall`: Define whether to assign OnCall to this flow.Possible values: True/False.Leave it empty if you do want not to assign an analyst to the incident.
- `EnableDeduplication`: Whether the deduplication playbook will be used.
- `DedupLimit`: The maximum number of incidents to query and set to context data.
- `DedupCloseSimilar`: "Defines the threshold of similarity to close a similar incident. All similar incidents with similarity above this value will be closed.For example, if CloseSimilar is set to .8 an
- `DedupHandleSimilar`: "This input defines how to handle Similar incidents. You may choose between: ""Link"", ""Close"", ""Link and Close"".Note: that closing incidents will require you to define ""Close
- `SIEMEDRProductToUse`: For EDR alerts routed through a SIEM, provide the supported originating EDR. Possible values: CrowdStrike, XDR, or Microsoft Defender.
- `EnableClosureSteps`: When closing an incident, whether to use closure steps to close automatically.
- `TicketProjectName`: For ticketing systems such as Jira a project name is required.
- `OverrideSIEMSeverity`: Whether to set the severity according to the ScaleToSetSeverity and SeverityValuesMapping settings (True) or keep the original severity as mapped by the SIEM (False).
- `SIEMincidentFieldForID`: The name of the field that provides the external ID of the alert or incident in the EDR.

**Dependencies:**

- Sub-playbooks: Cortex XDR Malware - Investigation And Response, MDE Malware - Investigation and Response, Malware SIEM Ingestion - Get Incident Data, CrowdStrike Falcon Malware - Investigation and Response
- Scripts: SetMultipleValues, Set, AssignAnalystToIncident


## Malware Investigation and Response - Set Alerts Grid

**Product:** Malware Investigation and Response

This playbook sets the alert grid for the Malware Investigation & Response layout

**Inputs:**

- `AlertName`: The alert name.
- `HostName`: The host name.
- `FileName`: The file name.
- `ProcessID`: The process ID.
- `SHA256`: The SHA256 file hash.
- `CommandLine`: The command line.
- `ParentProcess`: The parent process.

**Dependencies:**

- Scripts: Set, SetGridField


## Malware Triage - ReversingLabs TitaniumCloud

**Product:** ReversingLabs TitaniumCloud

Provides the TitaniumCloud classification of a file hash, and takes remediation actions based on that classification

**Inputs:**

- `hash`: SHA1 hash of a file.
- `file`: The file itself.
- `EndpointIP`: IP address of the endpoint from which the indicator came.

**Outputs:**

- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `DBotScore.Score`
- `DBotScore.Type`
- `DBotScore.Indicator`
- `DBotScore.Vendor`
- `ReversingLabs.file_reputation`

**Dependencies:**

- Sub-playbooks: Isolate Endpoint
- Integrations: ReversingLabs TitaniumCloud v2
- Scripts: IncreaseIncidentSeverity
- Commands: setIndicator, setIncident, reversinglabs-titaniumcloud-file-upload, reversinglabs-titaniumcloud-get-sample-dynamic-analysis-results, reversinglabs-titaniumcloud-submit-sample-for-dynamic-analysis, reversinglabs-titaniumcloud-file-reputation


## MDE Malware - Incident Enrichment

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook enriches Microsoft Defender For Endpoint alerts. The enrichment is done on the involved endpoint and Mitre technique ID information, and it sets the 'Malware-Investigation and Response' layout

**Inputs:**

- `DidAlertOriginateFromSIEM`: Whether the incident is fetched through a SIEM product.
- `AlertID`: The Microsoft Defender For Endpoint alert ID.

**Outputs:**

- `MITREATTACK`
- `AttackPattern`
- `MicrosoftATP.Alert`
- `Endpoint`

**Dependencies:**

- Sub-playbooks: Mitre Attack - Extract Technique Information From ID, Account Enrichment - Generic v2.1
- Integrations: Microsoft365DefenderEventCollector, MicrosoftDefenderAdvancedThreatProtection
- Scripts: SetGridField, isError, SetAndHandleEmpty
- Commands: microsoft-atp-get-alert-by-id, setIncident, endpoint, extractIndicators, file


## Microsoft 365 Defender - Emails Indicators Hunt

**Product:** Microsoft 365 Defender

This playbook retrieves email data based on the "URLDomain", "SHA256" and "IPAddress" inputs. SHA256 - Emails with attachments matching the "SHA256" input are retrieved. URLDomain - If the "URLDomain" value is found as a substring of URL(s) in the body of the email, the email is retrieved. IPAddress - Emails with "SenderIPv4"/SenderIPv6" or URLs (in the body) matching the "IPAddress" input are retrieved

**Inputs:**

- `URLDomain`: Domain or URL to search within emails. Can be a single domain or URL or an array of domains or URLs to search. The search looks for the exact Domain or URL.
- `SHA256`: The SHA256 hash file or an array of hashes to search within emails.
- `IPAddress`: The source or destination IP address to search. Can be a single address or an array of IP addresses.
- `Timeout`: The time limit in seconds for the HTTP request to run. Default is 60.
- `SearchTimeframe`: Number of days past to search. Default is 7.
- `ResultsLimit`: Number of retrieved entries. Enter -1 for unlimited query. 50 is the default.
- `ListenerMailbox`: The mailbox of the listening integration. In case it is provided, the emails found in it will be ignored.

**Outputs:**

- `Microsoft365Defender.RetrievedEmails`
- `Microsoft365Defender.RetrievedEmails.InternetMessageId`
- `Microsoft365Defender.RetrievedEmails.SenderFromDomain`
- `Microsoft365Defender.RetrievedEmails.EmailDirection`
- `Microsoft365Defender.RetrievedEmails.DeliveryLocation`
- `Microsoft365Defender.RetrievedEmails.AuthenticationDetails`
- `Microsoft365Defender.RetrievedEmails.DeliveryAction`
- `Microsoft365Defender.RetrievedEmails.Subject`
- `Microsoft365Defender.RetrievedEmails.AttachmentCount`
- `Microsoft365Defender.RetrievedEmails.ThreatNames`

**Dependencies:**

- Integrations: Microsoft 365 Defender
- Scripts: Set, IsIntegrationAvailable, SetAndHandleEmpty
- Commands: microsoft-365-defender-advanced-hunting


## Microsoft Defender For Endpoint - Collect investigation package

**Product:** Microsoft Defender for Endpoint

This playbook simplifies retrieving investigation packages to   from supported machines (See  The playbook receives information about the target devices (host name, IP, and device ID), validates the devices exist, and retrieves the collection package from those machines into the   console. Note: This action may take time, the average package size is around ~15 MB

**Inputs:**

- `AutoCollectinvestigationPackege`: Choose True to skip user validation on retrieving the investigation pack within the provided assets.
- `Hostnames`: A comma-separated list of host names.
- `MachineIDs`: A comma-separated list of machine IDs.
- `IPs`: A comma-separated list of machine IPs.

**Outputs:**

- `MicrosoftATP.MachineAction`

**Dependencies:**

- Commands: endpoint, microsoft-atp-request-and-download-investigation-package


## Microsoft Office File Enrichment - Oletools

**Product:** Oletools

Oletools is a tool for analyzing Microsoft OLE2 files, such as Microsoft Office documents or Outlook messages, mainly for malware analysis, forensics, and debugging. This playbook will run run the "oleid" command on the files which are passed to to it as playbook inputs. In case any macros or external relationships were found, it will also run "olevba" and "oleobj" commands as well on the relevant files. oleid - Analyze OLE files to detect specific characteristics usually found in malicious files. oleobj - Extract embedded objects from OLE files. olevba - Extract and analyze VBA Macro source code from MS Office documents (OLE and OpenXML)

**Inputs:**

- `FileObject`: A list of file objects. Default is "File" key.
- `Decode`: Available values: "True" or "False". Default is "False"When this is set to "True", in case a macro was found within the file, it will output all the obfuscated strings with their d
- `NonSecretPassword`: Will be used to decrypt encrypted files. Encrypted files cannot be analyzed otherwise.Please note that this input is "Non Secret" because it will be visible as plain text.

**Outputs:**

- `Oletools.Oleid.ole_command_result`
- `Oletools.Oleid.file_name`
- `Oletools.Oleid.sha256`
- `Oletools.Oleid.ole_command_result.File_format`
- `Oletools.Oleid.ole_command_result.Container_format`
- `Oletools.Oleid.ole_command_result.Encrypted`
- `Oletools.Oleid.ole_command_result.VBA_Macros`
- `Oletools.Oleid.ole_command_result.XLM_Macros`
- `Oletools.Oleid.ole_command_result.External_Relationships`
- `Oletools.Oleid.ole_command_result.ObjectPool`

**Dependencies:**

- Scripts: Set, Oletools


## Palo Alto Networks BPA - Submit Scan

**Product:** MITRE ATT&CK - Courses of Action

This playbook accepts a list of BPA checks, triggers a job and returns the checks results

**Inputs:**

- `check_id`: A comma-separated list of the BPA IDs of the results to return.
- `check_name`: A comma-separated list of the name of the results to return.

**Outputs:**

- `PAN-OS-BPA.JobResults.JobID`
- `PAN-OS-BPA.JobResults.Checks.check_id`
- `PAN-OS-BPA.JobResults.Checks.check_name`
- `PAN-OS-BPA.JobResults.Checks.check_message`
- `PAN-OS-BPA.JobResults.Checks.check_passed`
- `BPA.Passed`
- `BPA.Failed`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: BPA
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable, DeleteContext
- Commands: pan-os-bpa-get-job-results, pan-os-bpa-submit-job


## PhishUp Mail Scanner

**Product:** PhishUp

Extracts URLs from mail body and checks URLs with PhishUp. Takes action based on PhishUp results

**Inputs:**

- `EmailBodyHtml`: Email Mail Body for extracting URLs. Default Value is "${incident.emailbodyhtml}"
- `ShouldPhishUpActionWork`: If you do not want actions such as deleting mail and moving to spam in PhishUp playbook, you should set the value False. Default value is True
- `GmailMessageID`: Identify mail for deleting and moving funcitons. Defaultly it comes from incident which is setted from PhishUp Gmail Mapper
- `GmailUserID`: Identify user for deleting and moving funcitons. Defaultly it comes from incident which is setted from PhishUp Gmail Mapper

**Outputs:**

- `PhishUp.Evaluation`

**Dependencies:**

- Integrations: PhishUp, Gmail
- Scripts: IncreaseIncidentSeverity
- Commands: closeInvestigation, phishup-get-chosen-action, url, extractIndicators, phishup-evaluate-response, gmail-delete-mail, gmail-move-mail


## Phishing Alerts Investigation

**Product:** PhishingAlerts

This playbook investigates and remediates potential phishing incidents produced by either an email security gateway or a SIEM product. It retrieves original email files from the email security gateway or email service provider and generates a response based on the initial severity, hunting results, and the existence of similar phishing incidents in . No action is taken without an initial approval given by the analyst using the playbook inputs

**Inputs:**

- `Role`: The default role to assign the incident to.
- `SearchAndDelete`: Whether to enable the "Search and Delete" capability.For a malicious email, the Search and Delete sub-playbook looks for other instances of the email and deletes them pending analy
- `BlockIndicators`: Whether to enable the "Block Indicators" capability.For a malicious email, the Block Indicators sub-playbook blocks all malicious indicators in the relevant integrations.
- `AuthenticateEmail`: Whether the authenticity of the email should be verified using SPF, DKIM, and DMARC.
- `OnCall`: Set to True to assign only to analysts on the current shift. Requires the platform.5 or later.
- `SearchAndDeleteIntegration`: Determines which product and playbook is used to search and delete the phishing email from user inboxes.Set this to "O365" to use the O365 - Security And Compliance - Search And De
- `O365DeleteType`: The method to delete emails using the O365 - Security And Compliance - Search And Delete playbook. Can be "Soft" (recoverable), or "Hard" (unrecoverable). Leave empty to decide man
- `O365ExchangeLocationExclusion`: The exchange location. Determines from where to search and delete emails searched using O365 playbooks. Use the value 'All' to search all mailboxes, use 'SingleMailbox' to search a
- `SOCEmailAddress`: The SOC email address to set if the playbook handles phishing alerts.
- `escalationRole`: The role to assign the incident to if the incident severity is critical.

**Dependencies:**

- Sub-playbooks: Process Email - Generic v2, Phishing Alerts - Check Severity, Detonate File - Generic, Extract Indicators From File - Generic v2, Email Headers Check - Generic, Threat Hunting - Generic, Search And Delete Emails - Generic v2, Block Indicators - Generic v3
- Scripts: SearchIncidentsV2
- Commands: linkIncidents, closeInvestigation


## Phishing Triage and Response - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook extracts email addresses from phishing alerts, enriches their associated domains using the GTI domain enrichment command, and evaluates the GTI Threat Score, severity, and verdict. Based on these enrichment results, the playbook automatically blocks the malicious or high-risk email addresses to prevent further compromise

**Inputs:**

- `email_addresses`: Provide a comma-separated list of email addresses.

**Dependencies:**

- Sub-playbooks: Block Email - Generic v2, Email Collection by Enriched Domain - Google Threat Intelligence
- Scripts: DeleteContext, SetAndHandleEmpty
- Commands: domain, findIndicators


## Powershell Payload Response

**Product:** Malware Lateral Movement Assessment and Response

The Powershell Payload Response playbook is designed to be used when file payload executions are detected from an endpoint machines Powershell and begins the remediation process

**Inputs:**

- `Endpoint ID`: ID of the endpoint in question.
- `Hostname`: Hostname of the endpoint in question.
- `Email`: Email attachment.
- `File`: Payload file that was executed.
- `File Path`: File Path of the Executed Payload.

**Dependencies:**

- Sub-playbooks: Process Email - Generic, Isolate Endpoint - Generic V2, Block File - Generic v2, Dedup - Generic v3, Detonate File - Generic
- Integrations: Carbon Black Defense, Carbon Black Enterprise EDR, ServiceNow v2, SplunkPy
- Scripts: AssignAnalystToIncident, IncreaseIncidentSeverity
- Commands: cb-eedr-device-background-scan, splunk-search, closeInvestigation, cbd-create-policy, servicenow-update-ticket, cb-eedr-device-unquarantine, servicenow-create-ticket


## Prisma Cloud Compute - Audit Alert Enrichment

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook. It does the following

**Inputs:**

- `Hostname`: The hostname to retrieve events for. Relevant only for audit events.
- `ImageName`: The image name to retrieve events for.
- `AuditAlertType`: The type of the audit alert. Will be used to determine whether to retrieve WAAS events or not.
- `BaseURL`: The base URL of the Prisma Cloud Compute Instance used to create a link back to the alerts for an image.
- `ConsoleLink`: The value of the alert's console link. Part of the original incident values.
- `AccountID`: The cloud account ID.
- `Namespace`: The namespace which will be used to search associated users with in the "Get Account Owner" playbook.

**Outputs:**

- `PrismaCloudCompute.ReportsImagesScan`
- `PrismaCloud.Users`
- `PrismaCloud.UserRoles`
- `PrismaCloud.UserRoles.associatedUsers`
- `PrismaCloudCompute.ReportHostScan`
- `PrismaCloudCompute.ReportHostScan.complianceIssues`
- `PrismaCloudCompute.ReportsImagesScan.complianceIssues`

**Dependencies:**

- Sub-playbooks: Prisma Cloud - Get Account Owner, Prisma Cloud Compute - Get Container Events
- Commands: prisma-cloud-compute-images-scan-list, prisma-cloud-compute-hosts-scan-list, setIncident


## Prisma Cloud Compute - Audit Alert Vulnerabilities Enrichment

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook. It creates CVE indicators based on image or host vulnerabilities

**Inputs:**

- `ImageVulnerabilities`: Image vulnerabilities that were retrieved.
- `HostVulnerabilities`: Host vulnerabilities that were retrieved.
- `CVEsIndicatorsSeverities`: A list of the image or host CVE severities that the playbook creates indicators from.Available options (not case sensitive):- Critical- High- Medium- Low- NegligibleDefault value: 

**Outputs:**

- `CVEReport`


## Prisma Cloud Compute - Container Forensics

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook. Gets the container profile and forensics

**Inputs:**

- `AuditAlertType`: The audit alert type.
- `Image`: Image name.
- `DefenderType`: The defender type.
- `AlertCluster`: The alert's cluster name.
- `Hostname`: The hostname.
- `ForensicLink`: This link exists in audit runtime incidents.

**Dependencies:**

- Commands: prisma-cloud-compute-profile-container-list, prisma-cloud-compute-profile-container-forensic-list


## Prisma Cloud Compute - Get Container Events

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook

**Inputs:**

- `hostname`: The hostname to retrieve events for. Relevant only for audit events.
- `ImageName`: The image name to retrieve events for.
- `AuditAlertType`: The type of the audit alert. Will be used to determine whether to retrieve WAAS events or not.

**Dependencies:**

- Commands: prisma-cloud-compute-runtime-container-audit-events-list, setIncident, prisma-cloud-compute-get-audit-firewall-container-alerts


## Rapid7 - Nexpose - Enrichment

**Product:** Rapid7 InsightVM

Given an IP address, this playbook searches Rapid7 Nexpose assets for an asset with the associated IP address to retrieve asset information and proceeds to return all associated tags with it

**Inputs:**

- `IP`: IP used to search for asset information and tags.

**Outputs:**

- `Nexpose.Asset`
- `Nexpose.AssetTag`

**Dependencies:**

- Commands: nexpose-get-asset-tags, nexpose-search-assets


## RDP Bitmap Cache - Detect and Hunt

**Product:** RDPCacheHunting

**Inputs:**

- `ShouldCollectRDPCache`: When set to True, will use XDR to get RDP cache files from the endpoints. When set to False will try and use existing cache files from context.
- `EndpointIDs`: A comma-separated list of endpoint ID's to retrieve cache files from.
- `FilePath`: The path of the file to retrieve or use wildcard for multiple files.For example:C:\the\path\to\cache_file.binC:\the\path\to\*
- `Hostname`: Hostname of the machine on which the file is located. For PS remote it can also be an IP address.
- `min_score`: StringSifter - Limit output to strings with score >= min-score.
- `limit`: StringSifter - Limit output to the top limit ranked strings.
- `similiarity_threshold`: StringSimilarity - The similarity threshold to show results for, a value between 0 < x >1.
- `QRadarTimeFrame`: The time frame for the QRadar hunting query.
- `SplunkEarliestTime`: The earliest time for the Splunk hunting query.
- `SplunkLatestTime`: The latest time for the Splunk hunting query,

**Dependencies:**

- Sub-playbooks: Retrieve File from Endpoint - Generic V3, Threat Hunting - Generic
- Scripts: Set, PreProcessImage, StringSimilarity, StringSifter, UnzipFile, SetGridField, BMCTool
- Commands: xdr-file-retrieve, lolbas-get-indicators, image-ocr-extract-text, rasterize-image, splunk-search, extractIndicators, rasterize-pdf, setIncident


## Recorded Future Entity Enrichment

**Product:** Recorded Future Intelligence

Template playbook to incorporate Recorded Future enrichment for IPs, Hashes, Domains, URLs into your current workflows. Playbook also shows how to look up available 'Links' data for IOCs

**Inputs:**

- `MD5`: File MD5 hash to enrich.
- `SHA256`: The file SHA256 hash to enrich.
- `SHA1`: The file SHA1 hash to enrich.
- `IP`: The IP Address to enrich.
- `Domain`: The Domain name to enrich.
- `URL`: The URL to enrich.

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`
- `DBotScore`
- `DBotScore.Vendor`
- `DBotScore.Score`

**Dependencies:**

- Integrations: Recorded Future v2
- Commands: recordedfuture-intelligence, recordedfuture-links


## Rubrik Turbo IOC Scan - Rubrik Polaris

**Product:** Rubrik Security Cloud

This playbook starts a Turbo IOC scan with the specified IOC values and shows the results upon completion

**Inputs:**

- `ioc`: The value of the indicator to scan for. Supports comma separated values.Note: Users can retrieve the Md5, SHA1 or SHA256 by executing the "rubrik-threat-monitoring-matched-file-get
- `scan_name`: Name of the new turbo threat hunt scan.
- `cluster_id`: The ID of the cluster on which to perform a scan. If not provided, all the clusters will be scanned.Note: Users can retrieve the list of the cluster IDs by executing the "rubrik-gp
- `start_time`: Filter the snapshots from the provided date. Any snapshots taken before the provided date-time will be excluded.Formats accepted: 2 minutes, 2 hours, 2 days, 2 weeks, 2 months, 2 y
- `end_time`: Filter the snapshots until the provided date. Any snapshots taken after the provided date-time will be excluded.Formats accepted: 2 minutes, 2 hours, 2 days, 2 weeks, 2 months, 2 y
- `max_snapshots_per_object`: Maximum number of snapshots to scan per object.
- `polling_interval`: Frequency that the IOC scan command will run (minutes).
- `polling_timeout`: Amount of time to poll before declaring a timeout and resuming the playbook (in minutes).

**Outputs:**

- `RubrikPolaris.IOCScan`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Scripts: DeleteContext
- Commands: rubrik-turbo-ioc-scan, rubrik-ioc-scan-results-v2


## SANS - Incident Handler's Handbook Template

**Product:** SANS

Contains the phases for handling an incident as they are described in the SANS Institute ‘Incident Handler's Handbook’ by Patrick Kral. ***Disclaimer: This playbook does not ensure compliance to SANS regulations


## Scan Assets - Nexpose

**Product:** Rapid7 InsightVM

Scans according to asset IP addresses or host names, and waits for the scan to finish by polling the scan status in pre-defined intervals

**Inputs:**

- `IPs`: The asset IP addresses to scan.
- `HostNames`: The hostnames of the assets to scan.
- `Name`: The scan name as specified by the user.

**Outputs:**

- `Nexpose.Scan.ScanType`
- `Nexpose.Scan.Completed`
- `Nexpose.Scan.StartedBy`
- `Nexpose.Scan.Assets`
- `Nexpose.Scan.TotalTime`
- `Nexpose.Scan.Id`
- `Nexpose.Scan.Status`
- `Nexpose.Scan.Vulnerabilities.Critical`
- `Nexpose.Scan.Vulnerabilities.Moderate`
- `Nexpose.Scan.Vulnerabilities.Severe`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: Rapid7 Nexpose
- Commands: nexpose-get-scan, nexpose-start-assets-scan


## Search And Delete Emails - EWS

**Product:** Microsoft Exchange On-Premise

Searches EWS to identify and delete emails with similar attributes of a malicious email

**Inputs:**

- `From`: The value of the malicious email's "From" attribute.
- `Subject`: The value of the malicious email's "Subject" attribute.
- `AttachmentName`: The value of the malicious email's AttachmentName attribute.
- `SearchThisWeek`: Limit the search to the current week. Can be "true" or "false".
- `Limit`: The maximum number of search results.
- `DeleteType`: The deletion type. Can be, "trash", "soft", or "hard".

**Dependencies:**

- Integrations: EWS v2
- Scripts: BuildEWSQuery
- Commands: ews-delete-items, ews-search-mailboxes


## Search And Delete Emails - Generic v2

**Product:** Common Playbooks

This playbook searches and deletes emails with similar attributes of a malicious email using one of the following integrations: EWS Microsoft Graph Security Gmail Agari Phishing Defense

**Inputs:**

- `From`: The value of the malicious email's "From" attribute.
- `Subject`: The value of the malicious email's "Subject" attribute.
- `AttachmentName`: The value of the malicious email's "AttachmentName" attribute.
- `SearchAndDeleteIntegration`: The integration in which to run the search and delete action. Can be MS Graph, Gmail, EWS, or Agari Phishing Defense.
- `SearchThisWeek`: Whether to limit the search to the current week. Disabling this may increase search scope, execution time, and risk of timeout for large mailboxes.
- `MsgCase`: Used only with Microsoft Graph Security. The eDiscovery case name to use. Looked up by name and created if missing.
- `MsgKQL`: Used only with Microsoft Graph Security. KQL query identifying the emails to search and delete. Built automatically from the From, Subject, and AttachmentName inputs if left empty.
- `MsgRecipients`: Used only with Microsoft Graph Security. CSV of recipient email addresses to scope the search when MsgMailboxScope is recipientsOnly.
- `MsgMailboxScope`: Used only with Microsoft Graph Security. Determines which mailboxes to search. Use recipientsOnly to limit to specific recipients, allTenantMailboxes to search the entire tenant.
- `MsgDeleteType`: Used only with Microsoft Graph Security. The delete type to perform on the search results. Possible values are Hard or Soft, or leave empty to select manually (Hard = unrecoverable

**Dependencies:**

- Sub-playbooks: Search And Delete Emails - Microsoft Graph Security, Search And Delete Emails - EWS, Search And Delete Emails - Gmail
- Integrations: Agari Phishing Defense
- Scripts: DeleteContext, GetTime, Set
- Commands: apd-remediate-message


## Social Engineering Domain Investigation

**Product:** Social Engineering Domain Analysis

Enrich and Investigate domains which may present a social engineering threat to your organization. Review before blocking potentially dangerous indicators

**Inputs:**

- `SocialEngineeringDomainList`: The CSV list of domains to test or array of domains
- `SocialEngineeringRegisteredDomain`: Your company domain
- `BadNameservers`: An the platform BadNameserver list. This should be a CSV list with a single column and the header of "nameserver"Example List Contents:nameserverbadnameserver1.combadnameserver2.co

**Dependencies:**

- Sub-playbooks: Social Engineering Domain Enrichment
- Scripts: ConvertTableToHTML
- Commands: setIndicator, extractIndicators


## URL Private Scanning - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook performs private URL scanning and analyses the URL based on GTI assessment parameters such as Threat Score, Verdict, and Severity. Based on these parameters, the playbook blocks the URL

**Inputs:**

- `url`: Provide a comma-separated list of URLs.

**Dependencies:**

- Sub-playbooks: Block URL - Generic v2, URL Scan - Google Threat Intelligence
- Scripts: DeleteContext
- Commands: findIndicators


## Xpanse - Alert Enrichment

**Product:** Cortex Xpanse

This playbook handles ASM alerts by enriching asset information via integrations with Cloud Service Providers and other IT and Security tools

**Dependencies:**

- Sub-playbooks: Azure - Enrichment, GCP - Enrichment, AWS - Enrichment


## Xpanse - Alert Self-Enrichment

**Product:** Cortex Xpanse

Enrichment on the alert itself using  Xpanse APIs

**Dependencies:**

- Integrations: Cortex Xpanse
- Scripts: GridFieldSetup, Set
- Commands: asm-get-asset-internet-exposure, asm-get-external-service, extractIndicators


## Zimperium Incident Enrichment

**Product:** Zimperium

Enriches Zimperium incidents

**Dependencies:**

- Integrations: Zimperium, Zimperium v2
- Scripts: IsIntegrationAvailable
- Commands: zimperium-users-search, zimperium-device-get-by-id, zimperium-devices-search


## CheckPDFEncryptionAndValidity

**Product:** Common Scripts

This script checks whether a given PDF file is valid and whether it is encrypted. The results are returned as fields in the file’s context. The script will not fail on invalid/ encrypted files. Instead, the error details will be captured and returned in the file’s context


## ExtractAttackPattern

**Product:** Common Scripts

Extract Attack Pattern Threat Intel Object. After auto extract extracts the Attack Pattern IDs, this script is executed and extracts the value (name) of the Attack Pattern

**Inputs:**

- `input`: A comma-separated list of Attack Pattern IDs.


## IsDomainInternal

**Product:** Common Scripts

The script takes one or more domain names and checks whether they're in the   list defined in the InternalDomainsListName argument. By default, the InternalDomainsListName argument will use the   list called "InternalDomains". The list can be customized by the user. It should contain the organization's internal domain names, separated by new lines. Subdomains are also supported in the list. The results of the script are tagged with the "Internal_Domain_Check_Results" tag, so they can be displayed in the War Room entry sections in incident layouts

**Inputs:**

- `InternalDomainsListName`: The name of the the platform. If no list is specified, the script will use the InternalDomains list by default.
- `Domains`: A domain name or a list of domain names to check for being internal or external, against the specified list of internal domains.

**Outputs:**

- `Domain.Name`
- `Domain.Internal`

## ACTI Incident Enrichment

**Product:** Accenture CTI v2

**Inputs:**

- `ia_uuid`: Intelligence Alert unique ID.
- `ir_uuid`: Intelligence Report unique ID.
- `MalwareFamily_uuid`: Malware Family unique ID.
- `ThreatGroup_uuid`: Threat Group unique ID.
- `ThreatCampaign_uuid`: Threat Campaign unique ID.
- `ThreatActor_uuid`: Threat Actor unique ID.

**Dependencies:**

- Integrations: ACTI Indicator Query
- Commands: acti-get-fundamentals-by-uuid, acti-getThreatIntelReport


## ACTI Indicator Enrichment

**Product:** Accenture CTI v2

**Inputs:**

- `IP_Pre_Enrich`: The extracted IP.
- `Domain_Pre_Enrich`: The extracted Domain.
- `URL_Pre_Enrich`: The extracted URL.

**Outputs:**

- `IP`
- `DBotScore`
- `Domain`
- `URL`
- `intelligence_alerts`
- `intelligence_reports`

**Dependencies:**

- Integrations: ACTI Indicator Query
- Scripts: Exists
- Commands: ip, domain, url


## Armis Alert Enrichment

**Product:** Armis

Enrich Armis alerts with the devices in the context details

**Inputs:**

- `Armis_Device_Identifier`: Get the device ID that is associated with the alert.

**Outputs:**

- `Device ID`
- `Armis.Device.name`
- `Armis.Device.riskLevel`
- `Armis.Device.ipAddress`
- `Armis.Device.site`
- `Armis.Device.tags`

**Dependencies:**

- Integrations: Armis
- Commands: armis-search-devices


## ASM Issue Incident Response - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook initiates the response for ASM Issues in  when an incident is investigated. For medium, high, or critical severity, it creates a ServiceNow ticket using the "ServiceNow v2" integration; otherwise, the incident is assigned to an analyst. The ticket is enriched with GTI ASM Issue details, including entity name, status, confidence, tags, UUID, collection info, and other relevant incident information

**Inputs:**

- `issue_uid`: Collection ASM issue UID from incident.
- `incident_severity`: Collect incident severity from incident.
- `onCall`: Set to true to assign only the user that is currently on shift. Default is False.
- `severity_mapping`: Set the ASM Issue severity as per GTI platform.

**Dependencies:**

- Sub-playbooks: Create ServiceNow Ticket
- Scripts: AssignAnalystToIncident, DeleteContext, Print, SetAndHandleEmpty
- Commands: servicenow-update-ticket


## AWS - Enrichment

**Product:** AWS Enrichment and Remediation

Given the IP address this playbook enriches EC2 and IAM information

**Inputs:**

- `AwsIP`: AWS IP in alert
- `AWSAssumeRoleName`: If assuming roles for AWS, this is the name of the role to assume (should be the same for all organizations).
- `Indicator Query`: Indicators matching the indicator query will be used as playbook input.

**Outputs:**

- `AWS.EC2.Instances`
- `AWS.EC2.SecurityGroups`
- `AWSHierarchy`
- `AWS.SSM`

**Dependencies:**

- Integrations: AWS - EC2, AWS - System Manager
- Scripts: Set, AWSAccountHierarchy
- Commands: aws-ec2-describe-instances, aws-ec2-describe-security-groups, aws-ec2-describe-regions, aws-ec2-get-ipam-discovered-public-addresses, aws-ssm-inventory-entry-list, aws-ec2-describe-ipam-resource-discoveries


## Azure - Enrichment

**Product:** Azure Enrichment and Remediation

Given the IP address, this playbook enriches Azure Compute, Azure asset hierarchy path, IAM, and User information

**Inputs:**

- `AzureIP`: Azure IP in alert

**Outputs:**

- `Azure.Compute`
- `Azure.Network`
- `MSGraphIdentity.Role`
- `Account`
- `MSGraphUser`
- `AzureAssetHierarchy`

**Dependencies:**

- Integrations: Entra ID Identity And Access, Entra ID Users, Azure Compute v2, Azure Resource Graph
- Commands: azure-rg-query, azure-vm-get-public-ip-details, azure-vm-get-nic-details, azure-vm-get-instance-details, msgraph-identity-directory-roles-list, msgraph-identity-directory-role-members-list, msgraph-user-get


## Case Investigation - Google SecOps

**Product:** Google SecOps

This playbook investigates a Google SecOps case by retrieving the latest case information, related alerts, and their entities, and updating the case stage. It also calculates severity from IOC scores, updates the incident and case priority accordingly, creates entities in the case from the identified IOCs, and posts a summary comment on the case

**Inputs:**

- `case_id`: The ID of the case.Note: Use gcb-case-list command to retrieve case ID.
- `alert_limit`: Number of alerts to retrieve in the response. The maximum allowed size is 1000.
- `entity_limit`: Number of entities to retrieve in the response. The maximum allowed size is 1000.

**Dependencies:**

- Scripts: DeleteContext, GoogleSecOpsSyncCaseInformation, Set
- Commands: findIndicators, gcb-case-alert-entity-create, gcb-case-comment-create, gcb-case-priority-change, gcb-case-stage-change, setIncident


## ChronicleAsset Investigation - Chronicle

**Product:** Google SecOps

This playbook receives indicators from its parent playbook, performs enrichment and investigation for each one of them, provides an opportunity to isolate and block the hostname or IP address associated with the current indicator, and gives out a list of isolated and blocked entities. This playbook also lists the events fetched for the asset identifier information associated with the indicator

**Inputs:**

- `chronicleasset_value`: The value of the ChronicleAsset indicator.
- `chronicleasset_support_contact`: The support email address for the chronicle asset.
- `auto_block_entities`: Autoblock the detected suspicious IP Address(es). You can manually set this as 'Yes' or 'No' here or you can set it into a 'Chronicle Auto Block Entities' custom incident field.
- `skip_entity_isolation`: Skip the isolation of entities. You can manually set this as 'Yes' or 'No' here or you can set it into a 'Chronicle Skip Entity Isolation' custom incident field.

**Outputs:**

- `IsolatedEntities`
- `PotentiallyBlockedIPs`

**Dependencies:**

- Scripts: SixgillSearchIndicators, DeleteContext


## Cloud Response - AWS

**Product:** AWS Enrichment and Remediation

This playbook provides response actions to AWS. The following are available for execution automatically/manually

**Inputs:**

- `accessKeyRemediationType`: Choose the remediation type for the user's access key.Disable - for disabling the user's access key.Delete - for the user's access key deletion.
- `userRemediationType`: Choose the remediation type for the user involved.Delete - for the user deletion.Revoke - for revoking the user's credentials.
- `resourceRemediationType`: Choose the remediation type for the instances created.Stop - for stopping the instances.Terminate - for terminating the instances.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `autoAccessKeyRemediation`: Whether to execute the access key remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `resourceName`: The resource name to take action on.
- `region`: The resource's region.
- `username`: The username to take action on.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3
- Scripts: Set
- Commands: aws-iam-delete-login-profile, aws-iam-delete-user, aws-iam-update-access-key, aws-ec2-stop-instances, aws-iam-delete-access-key, aws-ec2-terminate-instances


## Cloud Response - Azure

**Product:** Azure Enrichment and Remediation

This playbook provides response actions to Azure. The following are available for execution automatically/manually

**Inputs:**

- `resourceRemediationType`: Choose the remediation type for the instances created.Poweroff - for shutting down the instances.Delete - for deleting the instances.
- `userRemediationType`: Choose the remediation type for the user involved.Disable - for disabling the user.Delete - for deleting the user.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `resourceName`: The resource name to take action on.
- `resourceGroup`: The resource group.
- `username`: The username to take action on.
- `sourceIP`: The source IP address of the attacker.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3
- Scripts: Set
- Commands: azure-vm-poweroff-instance, azure-vm-delete-instance, msgraph-user-delete, msgraph-user-account-disable


## Cloud Response - GCP

**Product:** GCP Enrichment and Remediation

This playbook provides response actions to GCP. The following are available for execution automatically/manually

**Inputs:**

- `accessKeyRemediationType`: Choose the remediation type for the user's access key.Disable - For disabling the user's access key.Delete - For deleting user's access key.
- `userRemediationType`: Choose the remediation type for the user involved.Delete - For deleting the user.Disable - For disabling the user.
- `resourceRemediationType`: Choose the remediation type for the instances created.Stop - For stopping the instances.Delete - For deleting the instances.
- `autoResourceRemediation`: Whether to execute the resource remediation flow automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `autoAccessKeyRemediation`: Whether to execute the access key remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `resourceName`: The resource name to take action on.
- `resourceZone`: The resource's zone.
- `username`: The username to take action on.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3
- Scripts: Set
- Commands: gcp-iam-service-account-disable, gcp-iam-service-account-key-disable, gsuite-user-delete, gcp-compute-stop-instance, gcp-iam-service-account-delete, gcp-iam-service-account-key-delete, gcp-compute-delete-instance


## Code42 File Download

**Product:** Code42

This playbook downloads a file via Code42 by either MD5 or SHA256 hash

**Inputs:**

- `XFC ID`: XFC Event ID to search for
- `MD5`: MD5 hash to search for
- `SHA256`: SHA256 hash to search for
- `Filename`: The name of the file to save as.

**Outputs:**

- `File.Size`
- `File.SHA1`
- `File.SHA256`
- `File.Name`
- `File.SSDeep`
- `File.EntryID`
- `File.Info`
- `File.Type`
- `File.MD5`
- `File.Extension`

**Dependencies:**

- Integrations: Code42
- Commands: code42-download-file


## Codecov Breach - Bash Uploader

**Product:** Rapid Breach Response

This playbook includes the following tasks: More information: Codecov Security Notice

**Inputs:**

- `KnownRelatedIOCs`: Known related IOCs to the Codecov Bash Uploader breach to hunt.
- `CustomIOCs`: Add your own custom Codecov Bash Uploader breach IOCs to hunt.
- `EWSSearchQuery`: The EWS query to find the Codecov security notice email
- `EWSSearchQuery_Limit`: The limit of results to return from the search
- `Github_Code_Search_query`: Github query to search for Codecov bash uploader use.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.

**Dependencies:**

- Sub-playbooks: Splunk Indicator Hunting, Panorama search thread-ids in threat logs, QRadar Indicator Hunting V2, Palo Alto Networks - Hunting And Threat Detection
- Commands: extractIndicators, GitHub-search-code, ews-search-mailbox


## Cortex ASM - Active Directory Enrichment

**Product:** Cortex Attack Surface Management

Playbook to enriches Service ownership info in Azure and On-Prem Active Directory

**Inputs:**

- `serviceowner`: The service owner to enrich in Azure directory.

**Dependencies:**

- Integrations: Microsoft Graph User, Active Directory Query v2
- Scripts: Set, GridFieldSetup
- Commands: msgraph-user-get, ad-get-user


## Cortex ASM - AWS Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches AWS information relevant to ASM alerts

**Inputs:**

- `RemoteIP`: IP address of service
- `ASMRuleID`: Attack Surface Management Rule ID.
- `AWSAssumeRoleName`: If assuming roles for AWS, this is the name of the role to assume (should be the same for all organizations).

**Dependencies:**

- Sub-playbooks: AWS - Enrichment, AWS - Unclaimed S3 Bucket Validation
- Scripts: GridFieldSetup, Set
- Commands: setAlert


## Cortex ASM - Azure Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address, this playbook enriches Azure information relevant to ASM alerts

**Inputs:**

- `RemoteIP`: IP address of service.

**Dependencies:**

- Scripts: GetTime, GridFieldSetup


## Cortex ASM - CMDB Enrichment

**Product:** Cortex Attack Surface Management

This playbook will look up a CI in ServiceNow CMDB by IP

**Inputs:**

- `IP`: IP address to search in ServiceNow

**Dependencies:**

- Integrations: ServiceNow CMDB
- Commands: servicenow-cmdb-records-list, servicenow-cmdb-record-get-by-id


## Cortex ASM - GCP Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches GCP and Firewall information

**Inputs:**

- `RemoteIP`: IP address of service

**Dependencies:**

- Sub-playbooks: GCP - Enrichment
- Scripts: Set GridFieldSetup


## Cortex ASM - On Prem Enrichment

**Product:** Cortex Attack Surface Management

Given an IP address, port, and protocol of a service, this playbook enriches on-prem integrations to find the related firewall rule and other related information. Conditions

**Inputs:**

- `RemoteIP`: IP address of the service.
- `RemotePort`: Port number of the service.
- `RemoteProtocol`: Protocol of the service.

**Dependencies:**

- Integrations: Panorama
- Scripts: GridFieldSetup, Set
- Commands: pan-os-security-policy-match, pan-os-platform-get-device-groups, pan-os-list-rules, pan-os-show-device-version


## Cortex ASM - Rapid7 Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches Rapid7 InsightVM (Nexpose) information relevant to ASM alerts

**Inputs:**

- `IPAddress`: IP addresses to enrich.

**Dependencies:**

- Sub-playbooks: Rapid7 - Nexpose - Enrichment
- Scripts: GetTime, GridFieldSetup


## Cortex ASM - Splunk Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches information from Splunk results relevant to ASM alerts

**Inputs:**

- `IP`: Remote IP in an incident/alert.

**Dependencies:**

- Scripts: GetTime, GridFieldSetup
- Commands: splunk-search


## Cortex XDR - Endpoint Investigation

**Product:** Cortex XDR by Palo Alto Networks

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook handles all the endpoint investigation actions available with  , including the following tasks

**Inputs:**

- `HuntReconnaissanceTechniques`: Set to True to hunt for identified alerts with MITRE Reconnaissance techniques.
- `HuntInitialAccessTechniques`: Set to True to hunt for identified alerts with MITRE Access techniques.
- `HuntExecutionTechniques`: Set to True to hunt for identified alerts with MITRE Execution techniques.
- `HuntPersistenceTechniques`: Set to True to hunt for identified alerts with MITRE Persistence techniques.
- `HuntPrivilegeEscalationTechniques`: Set to True to hunt for identified alerts with MITRE Privilege Escalation techniques.
- `HuntDefenseEvasionTechniques`: Set to True to hunt for identified alerts with MITRE Defense Evasion techniques.
- `HuntDiscoveryTechniques`: Set to True to hunt for identified alerts with MITRE Discovery techniques.
- `HuntLateralMovementTechniques`: Set to True to hunt for identified alerts with MITRE Lateral Movement techniques.
- `HuntCollectionTechniques`: Set to True to hunt for MITRE Collection techniques identified alerts.
- `HuntCnCTechniques`: Set to True to hunt for identified alerts with MITRE Command and Control techniques.

**Outputs:**

- `PaloAltoNetworksXDR.Alert`
- `PaloAltoNetworksXDR.Alert.internal_id`
- `PaloAltoNetworksXDR.Alert.source_insert_ts`
- `PaloAltoNetworksXDR.Alert.alert_name`
- `PaloAltoNetworksXDR.Alert.severity`
- `PaloAltoNetworksXDR.Alert.alert_category`
- `PaloAltoNetworksXDR.Alert.alert_action_status`
- `PaloAltoNetworksXDR.Alert.alert_action_status_readable`
- `PaloAltoNetworksXDR.Alert.alert_description`
- `PaloAltoNetworksXDR.Alert.agent_ip_addresses`

**Dependencies:**

- Integrations: CortexXDRIR
- Commands: xdr-get-alerts


## Cortex XDR - Malware Investigation

**Product:** Cortex XDR by Palo Alto Networks

Investigates a  XDR incident containing internal malware alerts. The playbook: The playbook is used as a sub- playbook in ‘ XDR Incident Handling - v2’

**Inputs:**

- `xdr_alert_id`: Unique ID for the XDR alert.
- `host_ip`: Host IP involved in the alert.
- `file_name`: The name of the malicious file.
- `file_sha256`: SHA-256 hash of the file.
- `file_path`: Full Path of the file.
- `endpoint_id`: the endpoint_id

**Outputs:**

- `Joe.Analysis`
- `File`
- `File.Malicious`
- `DBotScore`
- `IP`
- `DBotScore.Malicious`
- `Sample`
- `InfoFile`
- `WildFire`
- `WildFire.Report`

**Dependencies:**

- Sub-playbooks: Cortex XDR - Retrieve File v2, Detonate File - Generic
- Integrations: Cortex XDR - IR
- Scripts: SetMultipleValues
- Commands: xdr-get-endpoints


## Cortex XDR - Port Scan - Adjusted

**Product:** Cortex XDR by Palo Alto Networks

The playbook investigates  XDR incidents involving port scan alerts. The playbook is designed to run as a sub-playbook of ‘ XDR Alerts Handling’. The playbook consists of the following procedures: This playbook supports the following  XDR alert names

**Inputs:**

- `InternalIPRanges`: A list of IP ranges to check the IP against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.0.0.0/8,192.168
- `Username`: The user name used for port scanning.
- `SrcIPAddress`: The source IP address from which the port scanning was initiated.
- `DstIPAddress`: Scanned destination IP address.
- `DstPort`: Scanned port numbers.
- `EarlyContainment`: Whether early containment should be allowed when the IP address is known to be malicious.Possible values:True/False. Default:True.
- `SrcHostname`: Source host name from which port scanning was initiated.
- `EndpointID`: Source endpoint ID from which port scanning was initiated.
- `Initiator_CMD`: The command used to initiate port scan activity.
- `Initiator_Process_SHA256`: Process SHA256 file hash initiated port scanning.

**Outputs:**

- `PortScan.BlockPorts`
- `PortScan.AttackerIPs`
- `PortScan.AttackerHostnames`
- `PortScan.AttackerUsername`
- `PortScan.FileArtifacts`
- `PortScan.LateralMovementFirstDatetime`
- `PortScan.PortScanFirstDatetime`

**Dependencies:**

- Sub-playbooks: Cortex XDR - Endpoint Investigation, Account Enrichment - Generic v2.1, Cortex XDR - Isolate Endpoint, TIM - Indicator Relationships Analysis, User Investigation - Generic, Command-Line Analysis, Block Indicators - Generic v3, File Enrichment - Generic v2
- Scripts: IsIPInRanges, GetTime, Set
- Commands: setIncident


## Cortex XDR - Port Scan

**Product:** Cortex XDR by Palo Alto Networks

Investigates a  XDR incident containing internal port scan alerts. The playbook

**Inputs:**

- `BlockAttackerIP`: Whether attacking IPs should be automatically blocked using firewalls.
- `WhitelistedHostnames`: A list of comma-separated hostnames that should not be isolated even if used in an attack.
- `EmailAddressesToNotify`: A list of comma-separated values of email addresses that should receive a notification about compromised hosts.
- `CriticalUsernames`: A list of comma-separated names of critical users in the organization. This will affect the calculated severity of the incident.
- `IsolateEndpointAutomatically`: Whether to automatically isolate endpoints, or opt for manual user approval. True means isolation will be done automatically.
- `InternalIPRanges`: A list of IP ranges to check the IP against. The list should be provided in CIDR notation, separated by commas. An example of a list of ranges would be: "172.16.0.0/12,10.0.0.0/8,1
- `CriticalHostnames`: A list of comma-separated names of critical endpoints in the organization. This will affect the calculated severity of the incident.
- `RoleForEscalation`: The name of the the platform.
- `BlockMaliciousFiles`: Whether to automatically block malicious files involved with the incident across all endpoints in the organization.
- `CriticalADGroups`: CSV of DN names of critical Active Directory groups. This will affect the severity calculated for this incident.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3, IP Enrichment - Internal - Generic v2, Block File - Generic v2, Isolate Endpoint - Generic V2, Calculate Severity - Generic v2, PANW - Hunting and threat detection by indicator type V2
- Integrations: CortexXDRIR
- Scripts: AssignAnalystToIncident, IsIPInRanges, StopScheduledTask, SetAndHandleEmpty, XDRSyncScript
- Commands: closeInvestigation, xdr-get-endpoints, xdr-update-incident, send-mail, setIncident


## Cortex XDR - PrintNightmare Detection and Response

**Product:** Cortex XDR by Palo Alto Networks

The playbook targets specific PrintNightmare rules written by  XDR for both vulnerabilities: CVE-2021-1675 LPE CVE-2021-34527 RCE This playbook includes the following tasks: ** Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `IsolateEndpointAutomatically`: Whether to isolate the endpoint automatically
- `DisableAccountAutomatically`: Whether to disable the account automatically
- `BlockIPAutomatically`: Whether to block the IP Address automatically
- `EnrichAutomatically`: Whether to run indicators auto enrichment automatically
- `UserVerification`: Possible values: True/False.Whether to provide user verification for blocking IPs. False - No prompt will be displayed to the user.True - The server will ask the user for blocking 

**Dependencies:**

- Sub-playbooks: Account Enrichment - Generic v2.1, Endpoint Enrichment - Generic v2.1, Cortex XDR - Isolate Endpoint, Block IP - Generic v3, Threat Hunting - Generic
- Integrations: CortexXDRIR
- Scripts: SearchIncidentsV2
- Commands: ad-disable-account, enrichIndicators, xdr-get-incident-extra-data


## Cortex XDR device control violations

**Product:** Cortex XDR by Palo Alto Networks

Queries  XDR for device control violations for the specified hosts, IP address, or XDR endpoint ID. It then communicates via email with the involved users to understand the nature of the incident and if the user connected the device. All the collected data will be displayed in the XDR device control incident layout. This playbook can also be associated with  XDR device control violation job to periodically query and investigate XDR device control violations. In this configuration, the playbook will only communicate with the involved users

**Inputs:**

- `TimeStamp`: Timestamp in relative date format for query device control eventsfrom Cortex XDR.For example "1 day", "3 weeks".
- `EndpointID`: Comma-separated list of endpoint IDs to filter results for.
- `Hostname`: Comma-separated list of hostnames to filter results for.
- `IPAddress`: Comma-separated list of endpoints IP addresses to filter results for.
- `MessageSubject`: The subject of the message for communication with the involved users.
- `MessageBody`: A body of the message for communication with the involved users.

**Dependencies:**

- Integrations: CortexXDRIR
- Scripts: Set, SetGridField
- Commands: ad-get-user, xdr-get-endpoint-device-control-violations


## Cortex XDR Malware - Incident Enrichment

**Product:** Cortex XDR by Palo Alto Networks

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook enriches the  XDR incident. The enrichment is done on the involved endpoint and Mitre technique ID information, and sets the 'Malware-Investigation and Response' layout

**Inputs:**

- `IncidentID`: The incident ID to be enriched.

**Outputs:**

- `PaloAltoNetworksXDR.Incident`
- `File`
- `Process`
- `IP`
- `Domain`
- `Endpoint.ID`
- `Endpoint.Hostname`
- `Endpoint.OS`
- `Endpoint.OSVersion`
- `Endpoint.IPAddress`

**Dependencies:**

- Sub-playbooks: Mitre Attack - Extract Technique Information From ID, Account Enrichment - Generic v2.1
- Integrations: Cortex XDR - IR, CortexXDRIR
- Scripts: isError, SetGridField
- Commands: extractIndicators, endpoint, xdr-get-incident-extra-data, setIncident


## CrowdStrike Falcon Malware - Incident Enrichment

**Product:** CrowdStrike Falcon

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook enables enriching CrowdStrike Falcon incidents by pivoting to their detections as well as mapping all the relevant data to the   incident fields

**Inputs:**

- `DetectionOrCaseID`: The ID of the CrowdStrike detection or Case.

**Outputs:**

- `CrowdStrike`
- `Endpoint`
- `CrowdStrike.FoundDetections`

**Dependencies:**

- Sub-playbooks: Account Enrichment - Generic v2.1, CrowdStrike Falcon - Get Detections by Case
- Integrations: CrowdstrikeFalcon
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty, SetGridField, SetMultipleValues, isError
- Commands: endpoint, extractIndicators, setIncident


## CVE-2021-34527 | CVE-2021-1675 - PrintNightmare

**Product:** Rapid Breach Response

The playbook can be triggered manually or automatically by setting up a reoccurring job. Microsoft has released a security update in June 2021 Patch Tuesday for CVE-2021-1675, a Local Privilege Escalation vulnerability in the Print Spooler Service. Later that month, researchers found another method to exploit the Print Spooler service remotely, which raised the severity of the vulnerability due to the fact that the new method allows Remote Code Execution, a new ID was given to the critical vulnerability - CVE-2021-34527. Microsoft patched the vulnerability in June but an exploit POC and complete technical analysis were made publicly available online. **Update 7.8.2021 - Microsoft has released an emergency patch for the PrintNightmare. A reference for the patch can be found in "Install Microsoft spooler service patches" task. This playbook includes the following tasks: More details on the vulnerabilities: CVE-2021-1675 LPE CVE-2021-34527 RCE ** Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `CVE`: PrintNightmare CVEs
- `SplunkEarliestTime`: The earliest time for the Splunk search query.
- `SplunkLatestTime`: The latest time for the Splunk search query.

**Dependencies:**

- Sub-playbooks: Cortex XDR - PrintNightmare Detection and Response, QRadarFullSearch, Search Endpoint by CVE - Generic, Panorama Query Logs
- Commands: closeInvestigation, splunk-search


## CVE-2021-22893 - Pulse Connect Secure RCE

**Product:** Rapid Breach Response

On April 20th, a new Remote Code Execution vulnerability in Pulse Connect Secure was disclosed. The reference number for the vulnerability is CVE-2021-22893 with the CVSS Score of 10.0. This playbook should be trigger manually and includes the following tasks: Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve. More information: Exploitation of Pulse Connect Secure Vulnerabilities

**Inputs:**

- `Related_Hashes`: The known hashes of different malware families associated with the exploitation.
- `Related_CVEs`: The known CVEs associated with the exploitation.
- `BlockAutomatically`: Whether to block the indicators automatically.Default: False.
- `QRadarWebshellsQuery`: The QRadar search query used for "Hunt Activity Using QRadar".Please note that there aren't specified fields which may cause a longer run time.
- `SplunkWebshellsQuery`: The Splunk search query used for "Hunt Activity Using Splunk".Please note that there are two specified fields: msg, message. the query will work for both field names.
- `RunWebshellsQuery`: If you would like to skip "Hunt Activity Using Splunk" OR "Hunt Activity Using Qradar" please change the value to 'False'.
- `QRadar_MD5_Field`: The name of the field for MD5 entries in QRadar.If not configured, QRadar Indicator Hunting may reach timeout.
- `QRadar_SHA1_Field`: The name of the field for SHA1 entries in QRadar.If not configured, QRadar Indicator Hunting may reach timeout.
- `QRadar_SHA256_Field`: The name of the field for SHA256 entries in QRadar.If not configured, QRadar Indicator Hunting may reach timeout.
- `SplunkEarliestTime`: The earliest time for the Splunk search query.

**Dependencies:**

- Sub-playbooks: QRadar Indicator Hunting V2, QRadarFullSearch, Search Endpoint by CVE - Generic, Palo Alto Networks - Hunting And Threat Detection, Block Indicators - Generic v2, Splunk Indicator Hunting
- Commands: expanse-get-issues, enrichIndicators, splunk-search, extractIndicators


## CVE Exposure - RiskSense

**Product:** RiskSense

Block IPs and apply the tag to assets that are vulnerable to specified CVE

**Inputs:**

- `CVES`: Specify Common Vulnerabilities and Exposures (CVE). You can mention multiple CVEs using a comma-separated list.
- `TagName`: Tags in RiskSense can be applied to assets, web applications, and vulnerabilities. Tags are useful in the soft grouping, workflow creation, and to identify compliance-related asset

**Outputs:**

- `RiskSense.TagAssociation`
- `RiskSense.HostFinding`
- `RiskSense.Host`

**Dependencies:**

- Sub-playbooks: Block IP - Generic v2
- Integrations: RiskSense
- Scripts: IsIntegrationAvailable
- Commands: risksense-apply-tag, risksense-get-hosts, risksense-get-host-findings


## Cybereason - Download Close File

**Product:** Cybereason

This playbook aborts a file download operation which is in progress based on the Malop ID and username provided

**Inputs:**

- `malopGUID, userName`: Malop GUID for fetching a file from a sonsor to download, The complete Cybereason user name string for the user performing the request

**Dependencies:**

- Commands: cybereason-start-fetchfile, cybereason-fetchfile-progress, cybereason-close-file-batch-id


## Darkfeed - malware download from feed

**Product:** Sixgill Darkfeed - Annual Subscription

**Inputs:**

- `Indicator Query`: Indicators matching the indicator query will be used as playbook input

**Dependencies:**

- Sub-playbooks: Darkfeed IOC detonation and proactive blocking
- Scripts: SetAndHandleEmpty


## Darkmon - Compromised Account Response

**Product:** Darkmon

Incident-type playbook for 'Darkmon Compromised Credential' (and similar). Identifies the user via the configured directory, suspends, forces a password reset, revokes active sessions, and notifies SOC + the user

**Dependencies:**

- Sub-playbooks: Disable account, Force password reset, Notify SOC + user, Revoke active sessions


## Darkmon - EDR Alert Enrichment

**Product:** Darkmon

Designed to be invoked from CrowdStrike / SentinelOne / Defender alert playbooks. Takes the alert's IOCs, enriches each via Darkmon, and if any are scored Bad, escalates incident severity and notifies the SOC. Endpoint containment is left to the EDR-specific playbook

**Outputs:**

- `DBotScore`

**Dependencies:**

- Sub-playbooks: Enrich IOCs via Darkmon (URL pass), Notify SOC
- Scripts: Set


## Darkmon - Phishing Email Triage

**Product:** Darkmon

Extracts URLs/IPs/file-hashes from a reported phishing email, enriches each via the Darkmon - Enrich * sub-playbooks, and if any indicator is scored Bad (DBotScore=3) calls Generic Block Indicator on it. Notifies the reporter and the SOC at the end

**Outputs:**

- `ExtractedIndicators`
- `DBotScore`

**Dependencies:**

- Sub-playbooks: Block malicious indicators, Enrich each IOC via Darkmon, Notify SOC, Notify reporter
- Scripts: ExtractIndicatorsFromTextFile


## Digital Shadows - CVE_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of CVE IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_CVE`: A Digital Shadows ShadowSearch query containing CVE IDs

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## Digital Shadows - Domain_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of Domain IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_Domain`: A Digital Shadows ShadowSearch query containing domains

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## Digital Shadows - IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrich indicators by providing intelligence and more associated indicators based on confirmed reporting in Digital Shadows SearchLight

**Inputs:**

- `IoC_IP`: An IP address for assessment and enrichment
- `IoC_CVE`: A CVE for assessment and enrichment
- `IoC_Domain`: A domain for assessment and enrichment
- `IoC_URL`: A URL for assessment and enrichment
- `IoC_MD5`: A MD5 hash for assessment and enrichment
- `IoC_SHA256`: A SHA256 hash for assessment and enrichment
- `IoC_SHA1`: A SHA1 hash for assessment and enrichment

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Sub-playbooks: Digital Shadows - CVE_IoC Assessment & Enrichment, Digital Shadows - URL_IoC Assessment & Enrichment, Digital Shadows - SHA1_IoC Assessment & Enrichment, Digital Shadows - MD5_IoC Assessment & Enrichment, Digital Shadows - IP_IoC Assessment & Enrichment, Digital Shadows - SHA256_IoC Assessment & Enrichment, Digital Shadows - Domain_IoC Assessment & Enrichment


## Digital Shadows - IP_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of IP IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_IP`: A Digital Shadows ShadowSearch query containing IP addresses

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## Digital Shadows - MD5_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of MD5 IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_MD5`: A Digital Shadows ShadowSearch query containing MD5 hashes

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: AddEvidence, Print
- Commands: ds-search


## Digital Shadows - SHA1_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of SHA1 IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_SHA1`: A Digital Shadows ShadowSearch query containing SHA1 hashes

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: AddEvidence, Print
- Commands: ds-search


## Digital Shadows - SHA256_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of SHA256 IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_SHA256`: A Digital Shadows ShadowSearch query containing SHA256 hashes

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: AddEvidence, Print
- Commands: ds-search


## Digital Shadows - URL_IoC Assessment & Enrichment

**Product:** ReliaQuest Digital Risk Protection

Enrichment of URL IOC types - sub-playbook for IOC Assessment & Enrichment playbook

**Inputs:**

- `IoC_URL`: A Digital Shadows ShadowSearch query containing URLs

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`

**Dependencies:**

- Integrations: Digital Shadows
- Scripts: Print, AddEvidence
- Commands: ds-search


## DTM Alert Incident Response - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook initiates the response for DTM Alerts in  when an incident is investigated. For medium or higher severity, it creates a ServiceNow ticket using the "ServiceNow v2" integration; otherwise, the incident is assigned to an analyst. The ticket is enriched with GTI DTM Alert details, including alert type, status, monitor information, summary, AI Doc summary, and tags

**Inputs:**

- `alert_id`: Collection DTM Alert ID from incident.
- `incident_severity`: Collect incident severity from incident.
- `onCall`: Set to true to assign only the user that is currently on shift. Default is False.
- `severity_mapping`: Set the alert severity mapping as per GTI platform.

**Dependencies:**

- Sub-playbooks: Create ServiceNow Ticket
- Scripts: AssignAnalystToIncident, DeleteContext, Print, SetAndHandleEmpty
- Commands: servicenow-update-ticket


## Endpoint Investigation Plan

**Product:** Common Playbooks

This playbook handles all the endpoint investigation actions by performing the following tasks on every alert associated with the incident: Note: The playbook inputs enable manipulating the execution flow; read the input descriptions for details

**Inputs:**

- `HuntReconnaissanceTechniques`: Set to True to hunt for identified alerts with MITRE Reconnaissance techniques.
- `HuntInitialAccessTechniques`: Set to True to hunt for identified alerts with MITRE Access techniques.
- `HuntExecutionTechniques`: Set to True to hunt for identified alerts with MITRE Execution techniques.
- `HuntPersistenceTechniques`: Set to True to hunt for identified alerts with MITRE Persistence techniques.
- `HuntPrivilegeEscalationTechniques`: Set to True to hunt for identified alerts with MITRE Privilege Escalation techniques.
- `HuntDefenseEvasionTechniques`: Set to True to hunt for identified alerts with MITRE Defense Evasion techniques.
- `HuntDiscoveryTechniques`: Set to True to hunt for identified alerts with MITRE Discovery techniques.
- `HuntLateralMovementTechniques`: Set to True to hunt for identified alerts with MITRE Lateral Movement techniques.
- `HuntCollectionTechniques`: Set to True to hunt for MITRE Collection techniques identified alerts.
- `HuntCnCTechniques`: Set to True to hunt for identified alerts with MITRE Command and Control techniques.

**Dependencies:**

- Scripts: SearchIncidentsV2


## File Private Scanning - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook submits a file for private scanning, retrieves and evaluates the analysis verdict, and automatically creates a ServiceNow ticket using the "ServiceNow v2" integration when the file is determined to be malicious

**Inputs:**

- `file_id`: Fetch the Entry ID of the last submitted file from the incident.

**Dependencies:**

- Sub-playbooks: Create ServiceNow Ticket
- Scripts: DeleteContext, Print
- Commands: gti-private-file-scan-and-analysis-get, servicenow-update-ticket


## GCP - Enrichment

**Product:** GCP Enrichment and Remediation

Given the IP address this playbook enriches GCP and Firewall information

**Inputs:**

- `GcpIP`: GCP IP in alert
- `port`: Port to match traffic on for firewall rules.
- `protocol`: Protocol to match traffic on for firewall rules.

**Outputs:**

- `GoogleCloudCompute.Instances`
- `GCPIAM.Policy`
- `GCPIAM.TagBindings`
- `GCPHierarchy`
- `GCPOffendingFirewallRule`

**Dependencies:**

- Integrations: GCP-IAM, Google Cloud Compute
- Scripts: GCPOffendingFirewallRule, Set, GCPProjectHierarchy
- Commands: gcp-iam-tagbindings-list, gcp-iam-project-iam-policy-get, gcp-compute-aggregated-list-instances-by-ip, gcp-compute-get-instance


## Get entity alerts by MITRE tactics

**Product:** Core

This playbook searches XDR alerts related to specific entities, on a given timeframe, based on MITRE tactics. Note: The playbook's inputs enable manipulating the execution flow. Read the input descriptions for details

**Inputs:**

- `HuntReconnaissanceTechniques`: Set to True to hunt for identified alerts with MITRE Reconnaissance techniques.
- `HuntInitialAccessTechniques`: Set to True to hunt for identified alerts with MITRE Initial Access techniques.
- `HuntExecutionTechniques`: Set to True to hunt for identified alerts with MITRE Execution techniques.
- `HuntPersistenceTechniques`: Set to True to hunt for identified alerts with MITRE Persistence techniques.
- `HuntPrivilegeEscalationTechniques`: Set to True to hunt for identified alerts with MITRE Privilege Escalation techniques.
- `HuntDefenseEvasionTechniques`: Set to True to hunt for identified alerts with MITRE Defense Evasion techniques.
- `HuntDiscoveryTechniques`: Set to True to hunt for identified alerts with MITRE Discovery techniques.
- `HuntLateralMovementTechniques`: Set to True to hunt for identified alerts with MITRE Lateral Movement techniques.
- `HuntCollectionTechniques`: Set to True to hunt for identified alerts with MITRE Collection techniques .
- `HuntCnCTechniques`: Set to True to hunt for identified alerts with MITRE Command and Control techniques.

**Outputs:**

- `foundIncidents`

**Dependencies:**

- Scripts: SearchAlertsV2, SetAndHandleEmpty


## Hunt Extracted Hashes V2

**Product:** Hunting

This playbook extracts IOCs from the incident details and attached files using regular expressions and then hunts for hashes on endpoints in the organization using available tools. The playbook supports multiple types of attachments. For the full supported attachments list, refer to "Extract Indicators From File - Generic v2"

**Inputs:**

- `File`: The file from which to extract indicators.

**Dependencies:**

- Sub-playbooks: Extract Indicators From File - Generic v2, Search Endpoints By Hash - Generic V2
- Commands: extractIndicators


## Incident Enrichment - XM Cyber

**Product:** XM Cyber

This playbook enriches the incident using the hostname indicators and user data and increases the severity based on the calculated risk score and pushes breach points of the identified entities to XM Cyber

**Inputs:**

- `entity_values`: Specify the hostname or user entity. Supports comma separated values.
- `compromise_risk_score`: Specify the weight of Compromise Risk Score to apply to the final score calculation. Provide the value between 0 and 1.
- `choke_point_score`: Specify the weight of Choke Point Score to apply to the final score calculation. Provide the value between 0 and 1.
- `attribute_name`: The name of the custom label you want to push to CEM as an imported attribute.
- `parameter`: When setting up the condition for when to push the breach point data, this is the parameter of the condition. It is a list of predefined parameters for determining the criteria. Se
- `operator`: When setting up the condition for when to push the breach point data, this is the operator of the condition.Possible values are: Less than, Greater than, Less than equal to, Greate
- `value`: When setting up the condition for when to push the breach point data, this is the value of the condition. Can be boolean, string, integer, float, or date values.Supported date form

**Dependencies:**

- Scripts: DeleteContext, Set
- Commands: findIndicators, setIncident, xmcyber-calculate-risk-score, xmcyber-enrich-incident, xmcyber-push-breach-point, xmcyber-remove-breach-point


## Investigate On Bad Domain Matches - Chronicle

**Product:** Google SecOps

Use this playbook to investigate and remediate Bad IOC domain matches with recent activity found in the enterprise, as well as notify the SOC lead and network team about the matches. Supported Integrations

**Inputs:**

- `networkteam_email`: Enter the email address of the network team that needs to be notified.
- `stakeholder_email`: Enter the email of the stakeholder to whom you want to send the investigation summary report.

**Dependencies:**

- Integrations: Chronicle, Google SecOps, Whois, Mail Sender (New), Palo Alto Networks PAN-OS, Palo Alto Networks AutoFocus v2
- Scripts: AssignAnalystToIncident, GenerateInvestigationSummaryReport, Print
- Commands: domain, gcb-assets, gcb-ioc-details, pan-os-register-user-tag, send-mail, whois


## IOCs Curated Threat Intelligence Enrichment - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook extracts IOCs from incident details and enriches the selected IOCs with curated Google Threat Intelligence data, including malware families, campaigns, and threat actors

**Dependencies:**

- Sub-playbooks: IOC Curated Enrichment - Google Threat Intelligence
- Scripts: DeleteContext
- Commands: findIndicators


## IOC Alert

**Product:** Core

IOCs provide the ability to alert on known malicious objects on endpoints across the organization. Analysis Actions: The playbook will use several enrichment sources to determine the IOC verdict. Additionally, will use the Analytics module to run a prevalence check for the IOC. Response Actions: The playbook's first response action is a containment plan that is based on the playbook input. In that phase, the playbook will execute endpoint isolation Investigative Actions: When the playbook executes, it checks for additional abnormal activity using the Endpoint Investigation Plan playbook that can indicate the endpoint might be compromised. Remediation Actions: In case results are found within the investigation phase, the playbook will execute remediation actions that include containment and eradication. This phase will execute the following containment actions: And the following eradication actions

**Inputs:**

- `BlockIndicatorsAutomatically`: Whether to block suspicious/malicious indicators automatically. Specify True/False.
- `ShouldCloseAutomatically`: Whether to close the alert automatically if it's established verdict is False Positive. Specify True/False.
- `PreHostContainment`: Whether to isolate the host before the investigation phase in case an IOC was found to be suspicious. Specify True/False.
- `ShouldHandleFPautomatically`: Whether to automatically handle false positive alerts. Specify true/false.
- `AutoRestoreEndpoint`: Whether to execute the Recovery playbook. Specify True/False.
- `AutoContainment`: Setting this input will impact both Containment Plan sub-playbooks. Without setting this input, the default values are True for the first occurrence and False for the second.Whethe
- `FileRemediation`: Should be either 'Quarantine' or 'Delete'.
- `AutoEradication`: Whether to execute automatically or manually the eradication plan tasks:* Terminate process* Delete file* Reset the user's passwordSpecify True/False.
- `ShouldOpenTicket`: Whether to open a ticket automatically in a ticketing system. (True/False).
- `serviceNowShortDescription`: A short description of the ticket.

**Dependencies:**

- Sub-playbooks: Endpoint Investigation Plan, Recovery Plan, Eradication Plan, Enrichment for Verdict, Handle False Positive Alerts, Ticket Management - Generic, Containment Plan
- Commands: extractIndicators, setParentIncidentFields, closeInvestigation


## IOC Curated Enrichment - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook provides IOC curated enrichment using Google Threat Intelligence data, including malware families, campaigns, and threat actors, and displays the results in the War Room for investigation

**Inputs:**

- `resource`: The file hash (MD5, SHA1, or SHA256), Domain, URL or IP.
- `resource_type`: The type of the resource (IP, domain, URL, or file hash).

**Dependencies:**

- Scripts: DeleteContext, Print, SetAndHandleEmpty
- Commands: gti-curated-campaigns-get, gti-curated-malware-families-get, gti-curated-threat-actors-get


## IOC Enrichment and Blocking - Google SecOps

**Product:** Google SecOps

This playbook enriches IOCs using the enrichment commands (IP, Email, Domain, URL, and File) and blocks the malicious IOCs based on DBot Score

**Dependencies:**

- Sub-playbooks: Block Domain - Generic v2, Block Email - Generic v2, Block File - Generic v2, Block IP - Generic v3, Block URL - Generic v2
- Scripts: DeleteContext, SetAndHandleEmpty
- Commands: domain, email, file, findIndicators, ip, url


## IOC Enrichment and Blocking - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook enriches IOCs using the GTI enrichment commands (IP, Domain, URL, and File) and blocks the IOCs based on GTI assessment parameters such as Threat Score, Severity, and Verdict

**Inputs:**

- `ip_addresses`: Provide a comma-separated list of IPs.
- `domains`: Provide a comma-separated list of Domains.
- `files`: Provide a comma-separated list of Files.
- `urls`: Provide a comma-separated list of URLs.

**Dependencies:**

- Sub-playbooks: Block Domain - Generic v2, Block File - Generic v2, Block IP - Generic v3, Block URL - Generic v2
- Scripts: DeleteContext, Set
- Commands: domain, file, findIndicators, ip, url


## Large Upload Alert

**Product:** Core

The playbook investigates  XDR alerts involving large upload alerts. The playbook consists of the following procedures

**Inputs:**

- `InternalIPRanges`: A list of IP ranges to check the IP against. The list should be provided in CIDR notation, separated by commas. An example of a list of ranges would be: "172.16.0.0/12,10.0.0.0/8,1
- `FurtherInvestigation`: Determines whether an alert should be further investigated if similar previous false positive alerts were found.Possible values:True/False. Default: False.
- `AutoBlockIndicators`: Determine whether the given indicators be automatically blocked, or if the user should be given the option to choose.Possible values:True/False. Default: True.If set to True - no p
- `BlockIndicators_UserVerification`: Determine whether the blocking of any indicator requires the verification of the user.Possible values:True/False. Default: False.
- `EarlyContainment`: Whether early containment should be allowed when the IP address is known to be malicious.Possible values:True/False. Default: True.
- `AutoIsolateEndpoint`: Whether to isolate the initiating endpoint automatically if the investigation verdict is malicious.Possible values:True/False. Default: False.
- `Transferred_Data _Threshold`: Specify the uploaded data threshold volume (in MB) from which large upload alerts should be investigated.By setting a threshold, you will be able to determine which large upload al
- `FWApps_Processes_Whitlist`: A list of known and authorized FW application IDs and processes used in the organization.
- `Alert_ID`: The Cortex XDR alert ID.

**Dependencies:**

- Sub-playbooks: Block Indicators - Generic v3, User Investigation - Generic, TIM - Indicator Relationships Analysis, Command-Line Analysis, Threat Hunting - Generic, Entity Enrichment - Generic v3, Endpoint Investigation Plan, Search and Compare Process Executions - Generic
- Integrations: CortexCoreIR
- Scripts: DBotFindSimilarIncidents, SetAndHandleEmpty, Set
- Commands: setAlertStatus, core-isolate-endpoint, setAlert, core-get-cloud-original-alerts


## Malware Investigation & Response Incident Handler

**Product:** Malware Investigation and Response

This playbook is triggered by a malware incident from an endpoint integration. It performs enrichment, detonation, and hunting within the organization, and remediation on the malware. The playbook also covers the SIEM ingestion flow in which the fetching integration is the SIEM and EDR integrations grab all additional data. Currently supported EDR integrations are XDR, CrowdStrike Falcon, and Microsoft Defender for Endpoint. Currently supported SIEM integrations are QRadar and Splunk

**Inputs:**

- `OnCall`: Define whether to assign OnCall to this flow.Possible values: True/False.Leave it empty if you do want not to assign an analyst to the incident.
- `EnableDeduplication`: Whether the deduplication playbook will be used.
- `DedupLimit`: The maximum number of incidents to query and set to context data.
- `DedupCloseSimilar`: "Defines the threshold of similarity to close a similar incident. All similar incidents with similarity above this value will be closed.For example, if CloseSimilar is set to .8 an
- `DedupHandleSimilar`: "This input defines how to handle Similar incidents. You may choose between: ""Link"", ""Close"", ""Link and Close"".Note: that closing incidents will require you to define ""Close
- `SIEMEDRProductToUse`: For EDR alerts routed through a SIEM, provide the supported originating EDR. Possible values: CrowdStrike, XDR, or Microsoft Defender.
- `EnableClosureSteps`: When closing an incident, whether to use closure steps to close automatically.
- `TicketProjectName`: For ticketing systems such as Jira a project name is required.
- `OverrideSIEMSeverity`: Whether to set the severity according to the ScaleToSetSeverity and SeverityValuesMapping settings (True) or keep the original severity as mapped by the SIEM (False).
- `SIEMincidentFieldForID`: The name of the field that provides the external ID of the alert or incident in the EDR.

**Dependencies:**

- Sub-playbooks: Cortex XDR Malware - Investigation And Response, MDE Malware - Investigation and Response, Malware SIEM Ingestion - Get Incident Data, CrowdStrike Falcon Malware - Investigation and Response
- Scripts: SetMultipleValues, Set, AssignAnalystToIncident


## Malware Investigation and Response - Set Alerts Grid

**Product:** Malware Investigation and Response

This playbook sets the alert grid for the Malware Investigation & Response layout

**Inputs:**

- `AlertName`: The alert name.
- `HostName`: The host name.
- `FileName`: The file name.
- `ProcessID`: The process ID.
- `SHA256`: The SHA256 file hash.
- `CommandLine`: The command line.
- `ParentProcess`: The parent process.

**Dependencies:**

- Scripts: Set, SetGridField


## Malware Triage - ReversingLabs TitaniumCloud

**Product:** ReversingLabs TitaniumCloud

Provides the TitaniumCloud classification of a file hash, and takes remediation actions based on that classification

**Inputs:**

- `hash`: SHA1 hash of a file.
- `file`: The file itself.
- `EndpointIP`: IP address of the endpoint from which the indicator came.

**Outputs:**

- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `DBotScore.Score`
- `DBotScore.Type`
- `DBotScore.Indicator`
- `DBotScore.Vendor`
- `ReversingLabs.file_reputation`

**Dependencies:**

- Sub-playbooks: Isolate Endpoint
- Integrations: ReversingLabs TitaniumCloud v2
- Scripts: IncreaseIncidentSeverity
- Commands: setIndicator, setIncident, reversinglabs-titaniumcloud-file-upload, reversinglabs-titaniumcloud-get-sample-dynamic-analysis-results, reversinglabs-titaniumcloud-submit-sample-for-dynamic-analysis, reversinglabs-titaniumcloud-file-reputation


## MDE Malware - Incident Enrichment

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook enriches Microsoft Defender For Endpoint alerts. The enrichment is done on the involved endpoint and Mitre technique ID information, and it sets the 'Malware-Investigation and Response' layout

**Inputs:**

- `DidAlertOriginateFromSIEM`: Whether the incident is fetched through a SIEM product.
- `AlertID`: The Microsoft Defender For Endpoint alert ID.

**Outputs:**

- `MITREATTACK`
- `AttackPattern`
- `MicrosoftATP.Alert`
- `Endpoint`

**Dependencies:**

- Sub-playbooks: Mitre Attack - Extract Technique Information From ID, Account Enrichment - Generic v2.1
- Integrations: Microsoft365DefenderEventCollector, MicrosoftDefenderAdvancedThreatProtection
- Scripts: SetGridField, isError, SetAndHandleEmpty
- Commands: microsoft-atp-get-alert-by-id, setIncident, endpoint, extractIndicators, file


## Microsoft 365 Defender - Emails Indicators Hunt

**Product:** Microsoft 365 Defender

This playbook retrieves email data based on the "URLDomain", "SHA256" and "IPAddress" inputs. SHA256 - Emails with attachments matching the "SHA256" input are retrieved. URLDomain - If the "URLDomain" value is found as a substring of URL(s) in the body of the email, the email is retrieved. IPAddress - Emails with "SenderIPv4"/SenderIPv6" or URLs (in the body) matching the "IPAddress" input are retrieved

**Inputs:**

- `URLDomain`: Domain or URL to search within emails. Can be a single domain or URL or an array of domains or URLs to search. The search looks for the exact Domain or URL.
- `SHA256`: The SHA256 hash file or an array of hashes to search within emails.
- `IPAddress`: The source or destination IP address to search. Can be a single address or an array of IP addresses.
- `Timeout`: The time limit in seconds for the HTTP request to run. Default is 60.
- `SearchTimeframe`: Number of days past to search. Default is 7.
- `ResultsLimit`: Number of retrieved entries. Enter -1 for unlimited query. 50 is the default.
- `ListenerMailbox`: The mailbox of the listening integration. In case it is provided, the emails found in it will be ignored.

**Outputs:**

- `Microsoft365Defender.RetrievedEmails`
- `Microsoft365Defender.RetrievedEmails.InternetMessageId`
- `Microsoft365Defender.RetrievedEmails.SenderFromDomain`
- `Microsoft365Defender.RetrievedEmails.EmailDirection`
- `Microsoft365Defender.RetrievedEmails.DeliveryLocation`
- `Microsoft365Defender.RetrievedEmails.AuthenticationDetails`
- `Microsoft365Defender.RetrievedEmails.DeliveryAction`
- `Microsoft365Defender.RetrievedEmails.Subject`
- `Microsoft365Defender.RetrievedEmails.AttachmentCount`
- `Microsoft365Defender.RetrievedEmails.ThreatNames`

**Dependencies:**

- Integrations: Microsoft 365 Defender
- Scripts: Set, IsIntegrationAvailable, SetAndHandleEmpty
- Commands: microsoft-365-defender-advanced-hunting


## Microsoft Defender For Endpoint - Collect investigation package

**Product:** Microsoft Defender for Endpoint

This playbook simplifies retrieving investigation packages to   from supported machines (See  The playbook receives information about the target devices (host name, IP, and device ID), validates the devices exist, and retrieves the collection package from those machines into the   console. Note: This action may take time, the average package size is around ~15 MB

**Inputs:**

- `AutoCollectinvestigationPackege`: Choose True to skip user validation on retrieving the investigation pack within the provided assets.
- `Hostnames`: A comma-separated list of host names.
- `MachineIDs`: A comma-separated list of machine IDs.
- `IPs`: A comma-separated list of machine IPs.

**Outputs:**

- `MicrosoftATP.MachineAction`

**Dependencies:**

- Commands: endpoint, microsoft-atp-request-and-download-investigation-package


## Microsoft Office File Enrichment - Oletools

**Product:** Oletools

Oletools is a tool for analyzing Microsoft OLE2 files, such as Microsoft Office documents or Outlook messages, mainly for malware analysis, forensics, and debugging. This playbook will run run the "oleid" command on the files which are passed to to it as playbook inputs. In case any macros or external relationships were found, it will also run "olevba" and "oleobj" commands as well on the relevant files. oleid - Analyze OLE files to detect specific characteristics usually found in malicious files. oleobj - Extract embedded objects from OLE files. olevba - Extract and analyze VBA Macro source code from MS Office documents (OLE and OpenXML)

**Inputs:**

- `FileObject`: A list of file objects. Default is "File" key.
- `Decode`: Available values: "True" or "False". Default is "False"When this is set to "True", in case a macro was found within the file, it will output all the obfuscated strings with their d
- `NonSecretPassword`: Will be used to decrypt encrypted files. Encrypted files cannot be analyzed otherwise.Please note that this input is "Non Secret" because it will be visible as plain text.

**Outputs:**

- `Oletools.Oleid.ole_command_result`
- `Oletools.Oleid.file_name`
- `Oletools.Oleid.sha256`
- `Oletools.Oleid.ole_command_result.File_format`
- `Oletools.Oleid.ole_command_result.Container_format`
- `Oletools.Oleid.ole_command_result.Encrypted`
- `Oletools.Oleid.ole_command_result.VBA_Macros`
- `Oletools.Oleid.ole_command_result.XLM_Macros`
- `Oletools.Oleid.ole_command_result.External_Relationships`
- `Oletools.Oleid.ole_command_result.ObjectPool`

**Dependencies:**

- Scripts: Set, Oletools


## Palo Alto Networks BPA - Submit Scan

**Product:** MITRE ATT&CK - Courses of Action

This playbook accepts a list of BPA checks, triggers a job and returns the checks results

**Inputs:**

- `check_id`: A comma-separated list of the BPA IDs of the results to return.
- `check_name`: A comma-separated list of the name of the results to return.

**Outputs:**

- `PAN-OS-BPA.JobResults.JobID`
- `PAN-OS-BPA.JobResults.Checks.check_id`
- `PAN-OS-BPA.JobResults.Checks.check_name`
- `PAN-OS-BPA.JobResults.Checks.check_message`
- `PAN-OS-BPA.JobResults.Checks.check_passed`
- `BPA.Passed`
- `BPA.Failed`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: BPA
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable, DeleteContext
- Commands: pan-os-bpa-get-job-results, pan-os-bpa-submit-job


## PhishUp Mail Scanner

**Product:** PhishUp

Extracts URLs from mail body and checks URLs with PhishUp. Takes action based on PhishUp results

**Inputs:**

- `EmailBodyHtml`: Email Mail Body for extracting URLs. Default Value is "${incident.emailbodyhtml}"
- `ShouldPhishUpActionWork`: If you do not want actions such as deleting mail and moving to spam in PhishUp playbook, you should set the value False. Default value is True
- `GmailMessageID`: Identify mail for deleting and moving funcitons. Defaultly it comes from incident which is setted from PhishUp Gmail Mapper
- `GmailUserID`: Identify user for deleting and moving funcitons. Defaultly it comes from incident which is setted from PhishUp Gmail Mapper

**Outputs:**

- `PhishUp.Evaluation`

**Dependencies:**

- Integrations: PhishUp, Gmail
- Scripts: IncreaseIncidentSeverity
- Commands: closeInvestigation, phishup-get-chosen-action, url, extractIndicators, phishup-evaluate-response, gmail-delete-mail, gmail-move-mail


## Phishing Alerts Investigation

**Product:** PhishingAlerts

This playbook investigates and remediates potential phishing incidents produced by either an email security gateway or a SIEM product. It retrieves original email files from the email security gateway or email service provider and generates a response based on the initial severity, hunting results, and the existence of similar phishing incidents in . No action is taken without an initial approval given by the analyst using the playbook inputs

**Inputs:**

- `Role`: The default role to assign the incident to.
- `SearchAndDelete`: Whether to enable the "Search and Delete" capability.For a malicious email, the Search and Delete sub-playbook looks for other instances of the email and deletes them pending analy
- `BlockIndicators`: Whether to enable the "Block Indicators" capability.For a malicious email, the Block Indicators sub-playbook blocks all malicious indicators in the relevant integrations.
- `AuthenticateEmail`: Whether the authenticity of the email should be verified using SPF, DKIM, and DMARC.
- `OnCall`: Set to True to assign only to analysts on the current shift. Requires the platform.5 or later.
- `SearchAndDeleteIntegration`: Determines which product and playbook is used to search and delete the phishing email from user inboxes.Set this to "O365" to use the O365 - Security And Compliance - Search And De
- `O365DeleteType`: The method to delete emails using the O365 - Security And Compliance - Search And Delete playbook. Can be "Soft" (recoverable), or "Hard" (unrecoverable). Leave empty to decide man
- `O365ExchangeLocationExclusion`: The exchange location. Determines from where to search and delete emails searched using O365 playbooks. Use the value 'All' to search all mailboxes, use 'SingleMailbox' to search a
- `SOCEmailAddress`: The SOC email address to set if the playbook handles phishing alerts.
- `escalationRole`: The role to assign the incident to if the incident severity is critical.

**Dependencies:**

- Sub-playbooks: Process Email - Generic v2, Phishing Alerts - Check Severity, Detonate File - Generic, Extract Indicators From File - Generic v2, Email Headers Check - Generic, Threat Hunting - Generic, Search And Delete Emails - Generic v2, Block Indicators - Generic v3
- Scripts: SearchIncidentsV2
- Commands: linkIncidents, closeInvestigation


## Phishing Triage and Response - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook extracts email addresses from phishing alerts, enriches their associated domains using the GTI domain enrichment command, and evaluates the GTI Threat Score, severity, and verdict. Based on these enrichment results, the playbook automatically blocks the malicious or high-risk email addresses to prevent further compromise

**Inputs:**

- `email_addresses`: Provide a comma-separated list of email addresses.

**Dependencies:**

- Sub-playbooks: Block Email - Generic v2, Email Collection by Enriched Domain - Google Threat Intelligence
- Scripts: DeleteContext, SetAndHandleEmpty
- Commands: domain, findIndicators


## Powershell Payload Response

**Product:** Malware Lateral Movement Assessment and Response

The Powershell Payload Response playbook is designed to be used when file payload executions are detected from an endpoint machines Powershell and begins the remediation process

**Inputs:**

- `Endpoint ID`: ID of the endpoint in question.
- `Hostname`: Hostname of the endpoint in question.
- `Email`: Email attachment.
- `File`: Payload file that was executed.
- `File Path`: File Path of the Executed Payload.

**Dependencies:**

- Sub-playbooks: Process Email - Generic, Isolate Endpoint - Generic V2, Block File - Generic v2, Dedup - Generic v3, Detonate File - Generic
- Integrations: Carbon Black Defense, Carbon Black Enterprise EDR, ServiceNow v2, SplunkPy
- Scripts: AssignAnalystToIncident, IncreaseIncidentSeverity
- Commands: cb-eedr-device-background-scan, splunk-search, closeInvestigation, cbd-create-policy, servicenow-update-ticket, cb-eedr-device-unquarantine, servicenow-create-ticket


## Prisma Cloud Compute - Audit Alert Enrichment

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook. It does the following

**Inputs:**

- `Hostname`: The hostname to retrieve events for. Relevant only for audit events.
- `ImageName`: The image name to retrieve events for.
- `AuditAlertType`: The type of the audit alert. Will be used to determine whether to retrieve WAAS events or not.
- `BaseURL`: The base URL of the Prisma Cloud Compute Instance used to create a link back to the alerts for an image.
- `ConsoleLink`: The value of the alert's console link. Part of the original incident values.
- `AccountID`: The cloud account ID.
- `Namespace`: The namespace which will be used to search associated users with in the "Get Account Owner" playbook.

**Outputs:**

- `PrismaCloudCompute.ReportsImagesScan`
- `PrismaCloud.Users`
- `PrismaCloud.UserRoles`
- `PrismaCloud.UserRoles.associatedUsers`
- `PrismaCloudCompute.ReportHostScan`
- `PrismaCloudCompute.ReportHostScan.complianceIssues`
- `PrismaCloudCompute.ReportsImagesScan.complianceIssues`

**Dependencies:**

- Sub-playbooks: Prisma Cloud - Get Account Owner, Prisma Cloud Compute - Get Container Events
- Commands: prisma-cloud-compute-images-scan-list, prisma-cloud-compute-hosts-scan-list, setIncident


## Prisma Cloud Compute - Audit Alert Vulnerabilities Enrichment

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook. It creates CVE indicators based on image or host vulnerabilities

**Inputs:**

- `ImageVulnerabilities`: Image vulnerabilities that were retrieved.
- `HostVulnerabilities`: Host vulnerabilities that were retrieved.
- `CVEsIndicatorsSeverities`: A list of the image or host CVE severities that the playbook creates indicators from.Available options (not case sensitive):- Critical- High- Medium- Low- NegligibleDefault value: 

**Outputs:**

- `CVEReport`


## Prisma Cloud Compute - Container Forensics

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook. Gets the container profile and forensics

**Inputs:**

- `AuditAlertType`: The audit alert type.
- `Image`: Image name.
- `DefenderType`: The defender type.
- `AlertCluster`: The alert's cluster name.
- `Hostname`: The hostname.
- `ForensicLink`: This link exists in audit runtime incidents.

**Dependencies:**

- Commands: prisma-cloud-compute-profile-container-list, prisma-cloud-compute-profile-container-forensic-list


## Prisma Cloud Compute - Get Container Events

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook

**Inputs:**

- `hostname`: The hostname to retrieve events for. Relevant only for audit events.
- `ImageName`: The image name to retrieve events for.
- `AuditAlertType`: The type of the audit alert. Will be used to determine whether to retrieve WAAS events or not.

**Dependencies:**

- Commands: prisma-cloud-compute-runtime-container-audit-events-list, setIncident, prisma-cloud-compute-get-audit-firewall-container-alerts


## Rapid7 - Nexpose - Enrichment

**Product:** Rapid7 InsightVM

Given an IP address, this playbook searches Rapid7 Nexpose assets for an asset with the associated IP address to retrieve asset information and proceeds to return all associated tags with it

**Inputs:**

- `IP`: IP used to search for asset information and tags.

**Outputs:**

- `Nexpose.Asset`
- `Nexpose.AssetTag`

**Dependencies:**

- Commands: nexpose-get-asset-tags, nexpose-search-assets


## RDP Bitmap Cache - Detect and Hunt

**Product:** RDPCacheHunting

**Inputs:**

- `ShouldCollectRDPCache`: When set to True, will use XDR to get RDP cache files from the endpoints. When set to False will try and use existing cache files from context.
- `EndpointIDs`: A comma-separated list of endpoint ID's to retrieve cache files from.
- `FilePath`: The path of the file to retrieve or use wildcard for multiple files.For example:C:\the\path\to\cache_file.binC:\the\path\to\*
- `Hostname`: Hostname of the machine on which the file is located. For PS remote it can also be an IP address.
- `min_score`: StringSifter - Limit output to strings with score >= min-score.
- `limit`: StringSifter - Limit output to the top limit ranked strings.
- `similiarity_threshold`: StringSimilarity - The similarity threshold to show results for, a value between 0 < x >1.
- `QRadarTimeFrame`: The time frame for the QRadar hunting query.
- `SplunkEarliestTime`: The earliest time for the Splunk hunting query.
- `SplunkLatestTime`: The latest time for the Splunk hunting query,

**Dependencies:**

- Sub-playbooks: Retrieve File from Endpoint - Generic V3, Threat Hunting - Generic
- Scripts: Set, PreProcessImage, StringSimilarity, StringSifter, UnzipFile, SetGridField, BMCTool
- Commands: xdr-file-retrieve, lolbas-get-indicators, image-ocr-extract-text, rasterize-image, splunk-search, extractIndicators, rasterize-pdf, setIncident


## Recorded Future Entity Enrichment

**Product:** Recorded Future Intelligence

Template playbook to incorporate Recorded Future enrichment for IPs, Hashes, Domains, URLs into your current workflows. Playbook also shows how to look up available 'Links' data for IOCs

**Inputs:**

- `MD5`: File MD5 hash to enrich.
- `SHA256`: The file SHA256 hash to enrich.
- `SHA1`: The file SHA1 hash to enrich.
- `IP`: The IP Address to enrich.
- `Domain`: The Domain name to enrich.
- `URL`: The URL to enrich.

**Outputs:**

- `DBotScore.Indicator`
- `DBotScore.Type`
- `DBotScore`
- `DBotScore.Vendor`
- `DBotScore.Score`

**Dependencies:**

- Integrations: Recorded Future v2
- Commands: recordedfuture-intelligence, recordedfuture-links


## Rubrik Turbo IOC Scan - Rubrik Polaris

**Product:** Rubrik Security Cloud

This playbook starts a Turbo IOC scan with the specified IOC values and shows the results upon completion

**Inputs:**

- `ioc`: The value of the indicator to scan for. Supports comma separated values.Note: Users can retrieve the Md5, SHA1 or SHA256 by executing the "rubrik-threat-monitoring-matched-file-get
- `scan_name`: Name of the new turbo threat hunt scan.
- `cluster_id`: The ID of the cluster on which to perform a scan. If not provided, all the clusters will be scanned.Note: Users can retrieve the list of the cluster IDs by executing the "rubrik-gp
- `start_time`: Filter the snapshots from the provided date. Any snapshots taken before the provided date-time will be excluded.Formats accepted: 2 minutes, 2 hours, 2 days, 2 weeks, 2 months, 2 y
- `end_time`: Filter the snapshots until the provided date. Any snapshots taken after the provided date-time will be excluded.Formats accepted: 2 minutes, 2 hours, 2 days, 2 weeks, 2 months, 2 y
- `max_snapshots_per_object`: Maximum number of snapshots to scan per object.
- `polling_interval`: Frequency that the IOC scan command will run (minutes).
- `polling_timeout`: Amount of time to poll before declaring a timeout and resuming the playbook (in minutes).

**Outputs:**

- `RubrikPolaris.IOCScan`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Scripts: DeleteContext
- Commands: rubrik-turbo-ioc-scan, rubrik-ioc-scan-results-v2


## SANS - Incident Handler's Handbook Template

**Product:** SANS

Contains the phases for handling an incident as they are described in the SANS Institute ‘Incident Handler's Handbook’ by Patrick Kral. ***Disclaimer: This playbook does not ensure compliance to SANS regulations


## Scan Assets - Nexpose

**Product:** Rapid7 InsightVM

Scans according to asset IP addresses or host names, and waits for the scan to finish by polling the scan status in pre-defined intervals

**Inputs:**

- `IPs`: The asset IP addresses to scan.
- `HostNames`: The hostnames of the assets to scan.
- `Name`: The scan name as specified by the user.

**Outputs:**

- `Nexpose.Scan.ScanType`
- `Nexpose.Scan.Completed`
- `Nexpose.Scan.StartedBy`
- `Nexpose.Scan.Assets`
- `Nexpose.Scan.TotalTime`
- `Nexpose.Scan.Id`
- `Nexpose.Scan.Status`
- `Nexpose.Scan.Vulnerabilities.Critical`
- `Nexpose.Scan.Vulnerabilities.Moderate`
- `Nexpose.Scan.Vulnerabilities.Severe`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: Rapid7 Nexpose
- Commands: nexpose-get-scan, nexpose-start-assets-scan


## Search And Delete Emails - EWS

**Product:** Microsoft Exchange On-Premise

Searches EWS to identify and delete emails with similar attributes of a malicious email

**Inputs:**

- `From`: The value of the malicious email's "From" attribute.
- `Subject`: The value of the malicious email's "Subject" attribute.
- `AttachmentName`: The value of the malicious email's AttachmentName attribute.
- `SearchThisWeek`: Limit the search to the current week. Can be "true" or "false".
- `Limit`: The maximum number of search results.
- `DeleteType`: The deletion type. Can be, "trash", "soft", or "hard".

**Dependencies:**

- Integrations: EWS v2
- Scripts: BuildEWSQuery
- Commands: ews-delete-items, ews-search-mailboxes


## Search And Delete Emails - Generic v2

**Product:** Common Playbooks

This playbook searches and deletes emails with similar attributes of a malicious email using one of the following integrations: EWS Microsoft Graph Security Gmail Agari Phishing Defense

**Inputs:**

- `From`: The value of the malicious email's "From" attribute.
- `Subject`: The value of the malicious email's "Subject" attribute.
- `AttachmentName`: The value of the malicious email's "AttachmentName" attribute.
- `SearchAndDeleteIntegration`: The integration in which to run the search and delete action. Can be MS Graph, Gmail, EWS, or Agari Phishing Defense.
- `SearchThisWeek`: Whether to limit the search to the current week. Disabling this may increase search scope, execution time, and risk of timeout for large mailboxes.
- `MsgCase`: Used only with Microsoft Graph Security. The eDiscovery case name to use. Looked up by name and created if missing.
- `MsgKQL`: Used only with Microsoft Graph Security. KQL query identifying the emails to search and delete. Built automatically from the From, Subject, and AttachmentName inputs if left empty.
- `MsgRecipients`: Used only with Microsoft Graph Security. CSV of recipient email addresses to scope the search when MsgMailboxScope is recipientsOnly.
- `MsgMailboxScope`: Used only with Microsoft Graph Security. Determines which mailboxes to search. Use recipientsOnly to limit to specific recipients, allTenantMailboxes to search the entire tenant.
- `MsgDeleteType`: Used only with Microsoft Graph Security. The delete type to perform on the search results. Possible values are Hard or Soft, or leave empty to select manually (Hard = unrecoverable

**Dependencies:**

- Sub-playbooks: Search And Delete Emails - Microsoft Graph Security, Search And Delete Emails - EWS, Search And Delete Emails - Gmail
- Integrations: Agari Phishing Defense
- Scripts: DeleteContext, GetTime, Set
- Commands: apd-remediate-message


## Social Engineering Domain Investigation

**Product:** Social Engineering Domain Analysis

Enrich and Investigate domains which may present a social engineering threat to your organization. Review before blocking potentially dangerous indicators

**Inputs:**

- `SocialEngineeringDomainList`: The CSV list of domains to test or array of domains
- `SocialEngineeringRegisteredDomain`: Your company domain
- `BadNameservers`: An the platform BadNameserver list. This should be a CSV list with a single column and the header of "nameserver"Example List Contents:nameserverbadnameserver1.combadnameserver2.co

**Dependencies:**

- Sub-playbooks: Social Engineering Domain Enrichment
- Scripts: ConvertTableToHTML
- Commands: setIndicator, extractIndicators


## URL Private Scanning - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook performs private URL scanning and analyses the URL based on GTI assessment parameters such as Threat Score, Verdict, and Severity. Based on these parameters, the playbook blocks the URL

**Inputs:**

- `url`: Provide a comma-separated list of URLs.

**Dependencies:**

- Sub-playbooks: Block URL - Generic v2, URL Scan - Google Threat Intelligence
- Scripts: DeleteContext
- Commands: findIndicators


## Xpanse - Alert Enrichment

**Product:** Cortex Xpanse

This playbook handles ASM alerts by enriching asset information via integrations with Cloud Service Providers and other IT and Security tools

**Dependencies:**

- Sub-playbooks: Azure - Enrichment, GCP - Enrichment, AWS - Enrichment


## Xpanse - Alert Self-Enrichment

**Product:** Cortex Xpanse

Enrichment on the alert itself using  Xpanse APIs

**Dependencies:**

- Integrations: Cortex Xpanse
- Scripts: GridFieldSetup, Set
- Commands: asm-get-asset-internet-exposure, asm-get-external-service, extractIndicators


## Zimperium Incident Enrichment

**Product:** Zimperium

Enriches Zimperium incidents

**Dependencies:**

- Integrations: Zimperium, Zimperium v2
- Scripts: IsIntegrationAvailable
- Commands: zimperium-users-search, zimperium-device-get-by-id, zimperium-devices-search


## CheckPDFEncryptionAndValidity

**Product:** Common Scripts

This script checks whether a given PDF file is valid and whether it is encrypted. The results are returned as fields in the file’s context. The script will not fail on invalid/ encrypted files. Instead, the error details will be captured and returned in the file’s context


## ExtractAttackPattern

**Product:** Common Scripts

Extract Attack Pattern Threat Intel Object. After auto extract extracts the Attack Pattern IDs, this script is executed and extracts the value (name) of the Attack Pattern

**Inputs:**

- `input`: A comma-separated list of Attack Pattern IDs.


## IsDomainInternal

**Product:** Common Scripts

The script takes one or more domain names and checks whether they're in the   list defined in the InternalDomainsListName argument. By default, the InternalDomainsListName argument will use the   list called "InternalDomains". The list can be customized by the user. It should contain the organization's internal domain names, separated by new lines. Subdomains are also supported in the list. The results of the script are tagged with the "Internal_Domain_Check_Results" tag, so they can be displayed in the War Room entry sections in incident layouts

**Inputs:**

- `InternalDomainsListName`: The name of the the platform. If no list is specified, the script will use the InternalDomains list by default.
- `Domains`: A domain name or a list of domain names to check for being internal or external, against the specified list of internal domains.

**Outputs:**

- `Domain.Name`
- `Domain.Internal`

## DBot Indicator Enrichment - Generic

**Product:** Common Playbooks

**Kind:** playbook

Gets indicator's internal Dbot score

**Inputs:**

- `Email`: The email address to enrich with Dbot ccore.
- `URL`: The URL to enrich with Dbot score.
- `IP`: The IP address to enrich with Dbot score.
- `MD5`: The MD5 hash of the file to enrich with Dbot score.
- `SHA1`: The SHA1 hash of the file to enrich with Dbot score.
- `SHA256`: The SHA256 hash of the file to enrich with Dbot score.

## Enrichment for Verdict

**Product:** Common Playbooks

**Kind:** playbook

This playbook checks prior alert closing reasons and performs enrichment and prevalence checks on different IOC types. It then returns the information needed to establish the alert's verdict

**Inputs:**

- `threshold`: The number of previous alerts that were closed as false positive alerts. This threshold establishes whether the Previous Verdict key will be marked as false positive.
- `query`: A query for the previous alerts search.Use free form query (Lucene syntax) as a filter. All other filters are ignored when this filter is used.
- `CloseReason`: The closing reason of the previous alerts to search for.Possible values are:- Resolved - Threat Handled- Resolved - True Positive- Resolved - False Positive- Resolved - Security Te
- `FileSHA256`: File SHA256 to enrich and give verdict.
- `IP`: IP address to enrich and give verdict.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges is: "172.16.0.0/12,10.0.0.0/
- `ResolveIP`: Determines whether to convert the IP address to a hostname using a DNS query (True/ False).
- `URL`: URL to enrich and give verdict.
- `User`: User to enrich and give verdict. (AWS IAM or Active Directory).
- `Domain`: Domain to enrich and give verdict.

**Dependencies:**

- Sub-playbooks: URL Enrichment - Generic v2, File Reputation, IP Enrichment - Generic v2, Account Enrichment - Generic v2.1, Get prevalence for IOCs, Domain Enrichment - Generic v2
- Scripts: Set, SearchIncidentsV2

## Entity Enrichment - Generic v2

**Product:** Common Playbooks

**Kind:** playbook

Enrich entities using one or more integrations

**Inputs:**

- `IP`: The IP addresses to enrich
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `MD5`: File MD5 to enrich
- `SHA256`: File SHA256 to enrich
- `SHA1`: File SHA1 to enrich
- `URL`: URL to enrich
- `Email`: The email addresses to enrich
- `Hostname`: The hostname to enrich
- `Username`: The Username to enrich
- `Domain`: The domain name to enrich

**Dependencies:**

- Sub-playbooks: File Enrichment - Generic v2, URL Enrichment - Generic v2, Endpoint Enrichment - Generic v2.1, Domain Enrichment - Generic v2, Account Enrichment - Generic v2.1, Email Address Enrichment - Generic v2.1, IP Enrichment - Generic v2

## Entity Enrichment - Generic v4

**Product:** Use Case Builder

**Kind:** playbook

Enrich entities using one or more integrations

**Inputs:**

- `IP`: The IP addresses to enrich
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The list should be provided in CIDR notation, separated by commas. An example of a list of ranges would be: "172.16.0.0/
- `MD5`: File MD5 to enrich
- `SHA256`: File SHA256 to enrich
- `SHA1`: File SHA1 to enrich
- `URL`: URL to enrich
- `Email`: The email addresses to enrich
- `Hostname`: The hostname to enrich
- `Username`: The username to enrich
- `Domain`: The domain name to enrich

**Dependencies:**

- Sub-playbooks: Email Address Enrichment - Generic v2.1, IP Enrichment - Generic v2, Endpoint Enrichment - Generic v2.1, CVE Enrichment - Generic v2, Account Enrichment - Generic v2.1, File Enrichment - Generic v2, Domain Enrichment - Generic v2, URL Enrichment - Generic v2

## File Enrichment - File reputation

**Product:** Common Playbooks

**Kind:** playbook

Gets a file's reputation using one or more integrations

**Inputs:**

- `MD5`: The MD5 hash to enrich.
- `SHA256`: The SHA256 hash to enrich.
- `SHA1`: The SHA1 hash to enrich.

**Dependencies:**

- Scripts: FileReputation

## File Enrichment - Generic v2

**Product:** Common Playbooks

**Kind:** playbook

Enrich a file using one or more integrations

**Inputs:**

- `MD5`: File MD5 hash to enrich.
- `SHA256`: The file SHA256 hash to enrich.
- `SHA1`: The file SHA1 hash to enrich.
- `UseReputationCommand`: Define if you would like to use the !file command.Note: This input should be used whenever there is no auto-extract enabled in the investigation flow.Possible values: True / False.

**Dependencies:**

- Sub-playbooks: File Enrichment - Virus Total (API v3)
- Commands: file, cylance-protect-get-threat

## File Reputation

**Product:** Common Playbooks

**Kind:** playbook

This playbook checks the file reputation and sets the verdict as a new context key. The verdict is composed by 3 main components: Note: a user can provide a list of trusted signers of his own using the playbook inputs

**Inputs:**

- `DetectionThreshold`: The minimum number of positive engines needed to mark file as malicious.
- `TrustedPublishers`: A list of trusted publishers
- `FileSHA256`: The file SHA256.

**Dependencies:**

- Scripts: Set, http, ParseJSON
- Commands: wildfire-report, wildfire-get-verdict, file

## Proactive Threat Hunting - Entity Enrichment

**Product:** Proactive Threat Hunting

**Kind:** playbook

This playbook will be executed from the "Proactive Threat Hunting" layout button with the objective of enriching information on hosts and users specified by the analyst

**Dependencies:**

- Sub-playbooks: Account Enrichment - Generic v2.1
- Scripts: Print, Set, DeleteContext, JsonToTable
- Commands: endpoint, xdr-get-alerts, setIncident

## DBot Indicator Enrichment - Generic

**Product:** Common Playbooks

**Kind:** playbook

Gets indicator's internal Dbot score

**Inputs:**

- `Email`: The email address to enrich with Dbot ccore.
- `URL`: The URL to enrich with Dbot score.
- `IP`: The IP address to enrich with Dbot score.
- `MD5`: The MD5 hash of the file to enrich with Dbot score.
- `SHA1`: The SHA1 hash of the file to enrich with Dbot score.
- `SHA256`: The SHA256 hash of the file to enrich with Dbot score.

## Enrichment for Verdict

**Product:** Common Playbooks

**Kind:** playbook

This playbook checks prior alert closing reasons and performs enrichment and prevalence checks on different IOC types. It then returns the information needed to establish the alert's verdict

**Inputs:**

- `threshold`: The number of previous alerts that were closed as false positive alerts. This threshold establishes whether the Previous Verdict key will be marked as false positive.
- `query`: A query for the previous alerts search.Use free form query (Lucene syntax) as a filter. All other filters are ignored when this filter is used.
- `CloseReason`: The closing reason of the previous alerts to search for.Possible values are:- Resolved - Threat Handled- Resolved - True Positive- Resolved - False Positive- Resolved - Security Te
- `FileSHA256`: File SHA256 to enrich and give verdict.
- `IP`: IP address to enrich and give verdict.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges is: "172.16.0.0/12,10.0.0.0/
- `ResolveIP`: Determines whether to convert the IP address to a hostname using a DNS query (True/ False).
- `URL`: URL to enrich and give verdict.
- `User`: User to enrich and give verdict. (AWS IAM or Active Directory).
- `Domain`: Domain to enrich and give verdict.

**Dependencies:**

- Sub-playbooks: URL Enrichment - Generic v2, File Reputation, IP Enrichment - Generic v2, Account Enrichment - Generic v2.1, Get prevalence for IOCs, Domain Enrichment - Generic v2
- Scripts: Set, SearchIncidentsV2

## Entity Enrichment - Generic v2

**Product:** Common Playbooks

**Kind:** playbook

Enrich entities using one or more integrations

**Inputs:**

- `IP`: The IP addresses to enrich
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `MD5`: File MD5 to enrich
- `SHA256`: File SHA256 to enrich
- `SHA1`: File SHA1 to enrich
- `URL`: URL to enrich
- `Email`: The email addresses to enrich
- `Hostname`: The hostname to enrich
- `Username`: The Username to enrich
- `Domain`: The domain name to enrich

**Dependencies:**

- Sub-playbooks: File Enrichment - Generic v2, URL Enrichment - Generic v2, Endpoint Enrichment - Generic v2.1, Domain Enrichment - Generic v2, Account Enrichment - Generic v2.1, Email Address Enrichment - Generic v2.1, IP Enrichment - Generic v2

## Entity Enrichment - Generic v4

**Product:** Use Case Builder

**Kind:** playbook

Enrich entities using one or more integrations

**Inputs:**

- `IP`: The IP addresses to enrich
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The list should be provided in CIDR notation, separated by commas. An example of a list of ranges would be: "172.16.0.0/
- `MD5`: File MD5 to enrich
- `SHA256`: File SHA256 to enrich
- `SHA1`: File SHA1 to enrich
- `URL`: URL to enrich
- `Email`: The email addresses to enrich
- `Hostname`: The hostname to enrich
- `Username`: The username to enrich
- `Domain`: The domain name to enrich

**Dependencies:**

- Sub-playbooks: Email Address Enrichment - Generic v2.1, IP Enrichment - Generic v2, Endpoint Enrichment - Generic v2.1, CVE Enrichment - Generic v2, Account Enrichment - Generic v2.1, File Enrichment - Generic v2, Domain Enrichment - Generic v2, URL Enrichment - Generic v2

## File Enrichment - File reputation

**Product:** Common Playbooks

**Kind:** playbook

Gets a file's reputation using one or more integrations

**Inputs:**

- `MD5`: The MD5 hash to enrich.
- `SHA256`: The SHA256 hash to enrich.
- `SHA1`: The SHA1 hash to enrich.

**Dependencies:**

- Scripts: FileReputation

## File Enrichment - Generic v2

**Product:** Common Playbooks

**Kind:** playbook

Enrich a file using one or more integrations

**Inputs:**

- `MD5`: File MD5 hash to enrich.
- `SHA256`: The file SHA256 hash to enrich.
- `SHA1`: The file SHA1 hash to enrich.
- `UseReputationCommand`: Define if you would like to use the !file command.Note: This input should be used whenever there is no auto-extract enabled in the investigation flow.Possible values: True / False.

**Dependencies:**

- Sub-playbooks: File Enrichment - Virus Total (API v3)
- Commands: file, cylance-protect-get-threat

## File Reputation

**Product:** Common Playbooks

**Kind:** playbook

This playbook checks the file reputation and sets the verdict as a new context key. The verdict is composed by 3 main components: Note: a user can provide a list of trusted signers of his own using the playbook inputs

**Inputs:**

- `DetectionThreshold`: The minimum number of positive engines needed to mark file as malicious.
- `TrustedPublishers`: A list of trusted publishers
- `FileSHA256`: The file SHA256.

**Dependencies:**

- Scripts: Set, http, ParseJSON
- Commands: wildfire-report, wildfire-get-verdict, file

## Proactive Threat Hunting - Entity Enrichment

**Product:** Proactive Threat Hunting

**Kind:** playbook

This playbook will be executed from the "Proactive Threat Hunting" layout button with the objective of enriching information on hosts and users specified by the analyst

**Dependencies:**

- Sub-playbooks: Account Enrichment - Generic v2.1
- Scripts: Print, Set, DeleteContext, JsonToTable
- Commands: endpoint, xdr-get-alerts, setIncident

## DBot Indicator Enrichment - Generic

**Product:** Common Playbooks

**Kind:** playbook

Gets indicator's internal Dbot score

**Inputs:**

- `Email`: The email address to enrich with Dbot ccore.
- `URL`: The URL to enrich with Dbot score.
- `IP`: The IP address to enrich with Dbot score.
- `MD5`: The MD5 hash of the file to enrich with Dbot score.
- `SHA1`: The SHA1 hash of the file to enrich with Dbot score.
- `SHA256`: The SHA256 hash of the file to enrich with Dbot score.

## Enrichment for Verdict

**Product:** Common Playbooks

**Kind:** playbook

This playbook checks prior alert closing reasons and performs enrichment and prevalence checks on different IOC types. It then returns the information needed to establish the alert's verdict

**Inputs:**

- `threshold`: The number of previous alerts that were closed as false positive alerts. This threshold establishes whether the Previous Verdict key will be marked as false positive.
- `query`: A query for the previous alerts search.Use free form query (Lucene syntax) as a filter. All other filters are ignored when this filter is used.
- `CloseReason`: The closing reason of the previous alerts to search for.Possible values are:- Resolved - Threat Handled- Resolved - True Positive- Resolved - False Positive- Resolved - Security Te
- `FileSHA256`: File SHA256 to enrich and give verdict.
- `IP`: IP address to enrich and give verdict.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges is: "172.16.0.0/12,10.0.0.0/
- `ResolveIP`: Determines whether to convert the IP address to a hostname using a DNS query (True/ False).
- `URL`: URL to enrich and give verdict.
- `User`: User to enrich and give verdict. (AWS IAM or Active Directory).
- `Domain`: Domain to enrich and give verdict.

**Dependencies:**

- Sub-playbooks: URL Enrichment - Generic v2, File Reputation, IP Enrichment - Generic v2, Account Enrichment - Generic v2.1, Get prevalence for IOCs, Domain Enrichment - Generic v2
- Scripts: Set, SearchIncidentsV2

## Entity Enrichment - Generic v2

**Product:** Common Playbooks

**Kind:** playbook

Enrich entities using one or more integrations

**Inputs:**

- `IP`: The IP addresses to enrich
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `MD5`: File MD5 to enrich
- `SHA256`: File SHA256 to enrich
- `SHA1`: File SHA1 to enrich
- `URL`: URL to enrich
- `Email`: The email addresses to enrich
- `Hostname`: The hostname to enrich
- `Username`: The Username to enrich
- `Domain`: The domain name to enrich

**Dependencies:**

- Sub-playbooks: File Enrichment - Generic v2, URL Enrichment - Generic v2, Endpoint Enrichment - Generic v2.1, Domain Enrichment - Generic v2, Account Enrichment - Generic v2.1, Email Address Enrichment - Generic v2.1, IP Enrichment - Generic v2

## Entity Enrichment - Generic v4

**Product:** Use Case Builder

**Kind:** playbook

Enrich entities using one or more integrations

**Inputs:**

- `IP`: The IP addresses to enrich
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The list should be provided in CIDR notation, separated by commas. An example of a list of ranges would be: "172.16.0.0/
- `MD5`: File MD5 to enrich
- `SHA256`: File SHA256 to enrich
- `SHA1`: File SHA1 to enrich
- `URL`: URL to enrich
- `Email`: The email addresses to enrich
- `Hostname`: The hostname to enrich
- `Username`: The username to enrich
- `Domain`: The domain name to enrich

**Dependencies:**

- Sub-playbooks: Email Address Enrichment - Generic v2.1, IP Enrichment - Generic v2, Endpoint Enrichment - Generic v2.1, CVE Enrichment - Generic v2, Account Enrichment - Generic v2.1, File Enrichment - Generic v2, Domain Enrichment - Generic v2, URL Enrichment - Generic v2

## File Enrichment - File reputation

**Product:** Common Playbooks

**Kind:** playbook

Gets a file's reputation using one or more integrations

**Inputs:**

- `MD5`: The MD5 hash to enrich.
- `SHA256`: The SHA256 hash to enrich.
- `SHA1`: The SHA1 hash to enrich.

**Dependencies:**

- Scripts: FileReputation

## File Enrichment - Generic v2

**Product:** Common Playbooks

**Kind:** playbook

Enrich a file using one or more integrations

**Inputs:**

- `MD5`: File MD5 hash to enrich.
- `SHA256`: The file SHA256 hash to enrich.
- `SHA1`: The file SHA1 hash to enrich.
- `UseReputationCommand`: Define if you would like to use the !file command.Note: This input should be used whenever there is no auto-extract enabled in the investigation flow.Possible values: True / False.

**Dependencies:**

- Sub-playbooks: File Enrichment - Virus Total (API v3)
- Commands: file, cylance-protect-get-threat

## File Reputation

**Product:** Common Playbooks

**Kind:** playbook

This playbook checks the file reputation and sets the verdict as a new context key. The verdict is composed by 3 main components: Note: a user can provide a list of trusted signers of his own using the playbook inputs

**Inputs:**

- `DetectionThreshold`: The minimum number of positive engines needed to mark file as malicious.
- `TrustedPublishers`: A list of trusted publishers
- `FileSHA256`: The file SHA256.

**Dependencies:**

- Scripts: Set, http, ParseJSON
- Commands: wildfire-report, wildfire-get-verdict, file

## Proactive Threat Hunting - Entity Enrichment

**Product:** Proactive Threat Hunting

**Kind:** playbook

This playbook will be executed from the "Proactive Threat Hunting" layout button with the objective of enriching information on hosts and users specified by the analyst

**Dependencies:**

- Sub-playbooks: Account Enrichment - Generic v2.1
- Scripts: Print, Set, DeleteContext, JsonToTable
- Commands: endpoint, xdr-get-alerts, setIncident

