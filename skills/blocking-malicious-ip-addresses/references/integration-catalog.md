# Integration and Automation Catalog - Network Security

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## Autofocus Query Samples, Sessions and Tags

**Type:** playbook  
**Product:** AutoFocus by Palo Alto Networks  

This playbook is used for querying the PANW threat intelligence Autofocus system. The playbook accepts indicators such as IP's, hashes, domains to run basic queries or mode advanced queries that can leverage several query parameters. In order to run the more advanced queries its recommended to use the Autofocus UI  to created a query and than use the export search button. The result can be used as a playbook input. The playbook supports searching both the Samples API and the sessions API

**Inputs:**

- `Scope`: Scope can bePrivatePublicGlobal
- `SampleQuery`: Query needs to be provided in order to determine what to search for. Query is currently only in JSON format which can be extracted from the 
- `SessionQuery`: Query needs to be provided in order to determine what to search for. Query is currently only in JSON format which can be extracted from the 
- `IP`: IP to query
- `Hash`: Hash to query
- `URL`: URL to query
- `Domain`: Domain to query
- `Search Type`: Values can be session, sample, tag,all


## AutoFocusPolling

**Type:** playbook  
**Product:** AutoFocus by Palo Alto Networks  

Queries the PANW Autofocus Threat Intelligence System. This sub-playbook is the same as the generic polling sub-playbook besides that it provides outputs in the playbook. The reason for that is that in Autofocus its impossible to query the results of the same query more than once so the outputs have to be in the polling context. This playbook implements polling by continuously running the command in Step #2 until the operation completes. The remote action should have the following structure

**Inputs:**

- `Ids`: The list of IDs to poll.
- `PollingCommandName`: The name of the polling command to run.
- `PollingCommandArgName`: The argument name of the polling command.
- `Interval`: The frequency that the polling command will run (in minutes).
- `Timeout`: The amount of time to poll before declaring a timeout and resuming the playbook (in minutes).
- `dt`: The DT filter for polling IDs. Polling will stop when no results are returned. Use single quotes. For example, WildFire.Report(val.Status!==
- `AdditionalPollingCommandArgNames`: The Names of additional arguments for the polling command. For example, "arg1,arg2,...".
- `AdditionalPollingCommandArgValues`: The values of the additional arguments for the polling command. For example, "value1,value2,...".


## Bastille Networks

**Type:** integration  
**Product:** Bastille Networks  

RF monitoring for wireless intrusion detection and policy enforcement. Visit  for details. This integration was integrated and tested with Bastille Networks product version 1.5.0

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Calculate Severity - Cortex XDR Risky Assets

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

Calculates a severity for the incident based on the involvement of risky users or risky hosts in the incident, as determined by the Cortex XDR ITDR module

**Inputs:**

- `XDRRiskyUsers`: An object of risky users and their corresponding scores, as outputted by the "xdr-list-risky-users" command.
- `XDRRiskyHosts`: An object of risky hosts and their corresponding scores, as outputted by the "xdr-list-risky-hosts" command.


## CheckPoint Firewall v2

**Type:** integration  
**Product:** Check Point Firewall  
**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Cisco Secure Network Analytics (Stealthwatch)

**Type:** integration  
**Product:** Cisco Secure Network Analytics (Stealthwatch)  

Scalable visibility and security analytics. This integration was integrated and tested with version 7.2.1 of Cisco Secure Network Analytics (Stealthwatch). Due to changes in the product API, versions grater than 7.3.2 (including) are currently not supported

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## CombineSeverity

**Type:** script  
**Product:** Device Security by Palo Alto Networks  

Combines the severity and display_severity properties of the object passed in value into plain text, for example info / low. Missing or empty properties appear as N/A. Use this transformer in the incoming mapper to populate the Severity (raw / display) incident field. The value argument must be an object. The script returns a string and has no context outputs


## Cortex XDR - Check Action Status

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

Checks the action status of an action ID. \nEnter the action ID of the action whose status you want to know

**Inputs:**

- `action_id`: Action ID of the specific request.
- `timeout`: Amount of time to poll before declaring a timeout and resuming the playbook (in minutes).


## Cortex XDR - Display Risky Assets

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

This playbooks displays risky users and risky hosts, as detected by Cortex XDR's ITDR module. The data is displayed in incident fields in XDR incidents

**Inputs:**

- `XDRRiskyUsers`: A list of risky usernames, their scores, risk levels, and the reasons for the risk, as outputted from the "xdr-list-risky-users" command.
- `XDRRiskyHosts`: A list of risky hosts, their scores, risk levels, and the reasons for the risk, as outputted from the "xdr-list-risky-hosts" command.


## Cortex XDR - False Positive Incident Handling

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook handles false-positive incident closures for Cortex XDR - Malware investigation

**Inputs:**

- `Comment`: Add comment to close this incident.
- `Reason`: Choose From - "Unknown" / "TruePositive" / "FalsePositive"
- `AllowTag`: The approving tag name for found indicators.
- `AutoUnisolation`: Whether automatic unisolation is allowed.
- `HostID`: The ID of the host for running an un-isolation process.
- `FileSha256`: The File SHA256 you want to block.


## Cortex XDR - Get entity alerts by MITRE tactics

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

This playbook is part of the Cortex XDR by Palo Alto Networks’ pack. This playbook searches alerts related to specific entities from Cortex XDR, on a given timeframe, based on MITRE tactics. Note: The playbook's inputs enable manipulating the execution flow. Read the input descriptions for details

**Inputs:**

- `HuntReconnaissanceTechniques`: Set to True to hunt for identified alerts with MITRE Reconnaissance techniques.
- `HuntInitialAccessTechniques`: Set to True to hunt for identified alerts with MITRE Initial Access techniques.
- `HuntExecutionTechniques`: Set to True to hunt for identified alerts with MITRE Execution techniques.
- `HuntPersistenceTechniques`: Set to True to hunt for identified alerts with MITRE Persistence techniques.
- `HuntPrivilegeEscalationTechniques`: Set to True to hunt for identified alerts with MITRE Privilege Escalation techniques.
- `HuntDefenseEvasionTechniques`: Set to True to hunt for identified alerts with MITRE Defense Evasion techniques.
- `HuntDiscoveryTechniques`: Set to True to hunt for identified alerts with MITRE Discovery techniques.
- `HuntLateralMovementTechniques`: Set to True to hunt for identified alerts with MITRE Lateral Movement techniques.


## Cortex XDR - Get File Path from alerts by hash

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook assists in retrieving file paths from the Cortex XDR incident by hash

**Inputs:**

- `NonFoundHashes`: List of hashes to run against.


## Cortex XDR - Identity Analytics

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

The Cortex XDR - Identity Analytics playbook is designed to handle Cortex XDR Identity Analytics alerts and executes the following: Analysis: Verdict: Investigation: Verdict Handling: The playbook is used as a sub-playbook in ‘Cortex XDR Alerts Handling v2’

**Inputs:**

- `AlertName`: Alert name.
- `alert_id`: Alert ID.
- `IPAddress`: IP address from the XDR alert.
- `Username`: User name.
- `RelatedAlertsThreshold`: This is the minimum threshold for Cortex XDR related alerts, based on MITRE tactics used to identify malicious activity by the user in the l
- `FailedLogonThreshold`: This is the minimum threshold for user login failures within the last 1 day.For example: If this input is set to '30', and the 'Okta - User 
- `OktaSuspiciousActivitiesThreshold`: This is the minimum threshold for suspicious Okta activity events by the user in the last 1 day.For example: If this input is set to '5', an
- `AutoRemediation`: Whether to execute the remediation flow automatically.Possible values are: "True" and "False".


## Cortex XDR - Large Upload

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

The playbook investigates Cortex XDR incidents involving large upload alerts. The playbook is designed to run as a sub-playbook of ‘Cortex XDR Alerts Handling v2’. The playbook consists of the following procedures: This playbook supports the following Cortex XDR alert names

**Inputs:**

- `InternalIPRanges`: A list of IP ranges to check the IP against. The list should be provided in CIDR notation, separated by commas. An example of a list of rang
- `FurtherInvestigation`: Determines whether an incident should be further investigated if similar previous false positive incidents were found.Possible values:True/F
- `AutoBlockIndicators`: Determine whether the given indicators be automatically blocked, or if the user should be given the option to choose.Possible values:True/Fa
- `BlockIndicators_UserVerification`: Determine whether the blocking of any indicator requires the verification of the user.Possible values:True/False. Default: False.
- `EarlyContainment`: Whether early containment should be allowed when the IP address is known to be malicious.Possible values:True/False. Default: True.
- `AutoIsolateEndpoint`: Whether to isolate the initiating endpoint automatically if the investigation verdict is malicious.Possible values:True/False. Default: Fals
- `Alert_ID`: The Cortex XDR alert ID.
- `Transferred_Data _Threshold`: Specify the uploaded data threshold volume (in MB) from which large upload alerts should be investigated.By setting a threshold, you will be


## Cortex XDR - Possible External RDP Brute-Force

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

This playbook investigates a “Possible External RDP Brute Force” XDR Alert by gathering user, IP, and hostname information, and investigating if the following suspicious elements exists: Set verdict method

**Inputs:**

- `Username`: RDP connection username.
- `ExternalIP`: Source external IP address.
- `AutoRemediation`: Set this value to "true" to enable auto remediation (IP Block and User Block).
- `FinalThreshold`: The threshold number of suspicious elements required to determine a 'True Positive' verdict.
- `CriticalElement`: You can select a specific element that, if identified as suspicious, will automatically set the final verdict as true positive. The followin
- `UserEngagementThreshold`: The threshold number of suspicious elements that will trigger a user engagement. Set to 0 to disable user engagement.NOTICE: If this thresho
- `Hostname`: RDP connection destination hostname.
- `EndpointID`: RDP connection destination endpoint ID.


## Cortex XDR - Search And Block Software - XQL Engine

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

This playbook will search a file or process activity of a software by a given image file name using Cortex XDR XQL Engine. The analyst can then choose the files to block

**Inputs:**

- `Filename`: File name to search.
- `TimeFrame`: Time in relative date or range format (for example: "1 day", "3 weeks ago", "between 2021-01-01 12:34:56 +02:00 and 2021-02-01 12:34:56 +02:


## Cortex XDR - Search and Compare Process Executions - XDR Alerts

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

This playbook is a generic playbook that receives a process name and command-line argument. It uses the "Cortex XDR IR" integration to search for the given process executions inside Cortex XDR alerts and compares the command-line argument from the results to the command-line argument received from the playbook input. Note: Under the "Processes" input, the playbook should receive an array that contains the following keys

**Inputs:**

- `Processes`: Process name to search and command-line argument to compare. This input should receive an array that contains the following keys:- value: *p
- `HuntingTimeFrame`: Time in relative date or range format (for example: "1 day", "3 weeks ago", "between 2021-01-01 12:34:56 +02:00 and 2021-02-01 12:34:56 +02:
- `StringSimilarityThreshold`: StringSimilarity automation threshold. A number between 0 and 1, where 1 represents the most similar results of string comparisons. The auto
- `SearchXDRAlerts`: Set to "True" if you want to hunt for processes that are part of XDR alerts


## Cortex XDR - Search and Compare Process Executions - XQL Engine

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

This playbook is a generic playbook that receives a process name and a command-line argument. It uses the "Cortex XDR - XQL Engine" integration to search for the given process executions and compares the command-line argument from the results to the command-line argument received from the playbook input. Note: Under the "Processes" input, the playbook should receive an array that contains the following keys

**Inputs:**

- `Processes`: Process name to search and command-line argument to compare. This input should receive an array that contains the following keys:-value: *pr
- `HuntingTimeFrame`: Time in relative date or range format (for example: "1 day", "3 weeks ago", "between 2021-01-01 12:34:56 +02:00 and 2021-02-01 12:34:56 +02:
- `StringSimilarityThreshold`: StringSimilarity automation threshold. A number between 0 and 1, where 1 represents the most similar results of string comparisons. The auto


## Cortex XDR - True Positive Incident Handling

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook handles a true-positive incident closure for Cortex XDR - Malware Investigation

**Inputs:**

- `Comment`: Add comment to close this incident.
- `Classification`: Choose From - "Unknown" / "TruePositive"
- `BlockTag`: Specify the banning tag name for founded indicators.
- `AutoIsolation`: Indicates if automatic host isolation is allowed.True/False
- `TicketProjectName`: For ticketing systems such as Jira a project name is required.
- `TicketingSystemToUse`: The name of the ticketing system to use, for example Jira or ServiceNow
- `FileSha256`: Enter the File SHA256 you would like to block. Also, this input can be used in the Threat Hunting step.
- `HostID`: The ID of the host for running an isolation process.


## Cortex XDR - XQL Query Engine

**Type:** integration  
**Product:** Cortex XDR by Palo Alto Networks  

Cortex XDR - XQL Query Engine enables you to run XQL queries on your data sources. This integration was integrated and tested with version 3.0 of Cortex XDR - XQL Query Engine In order to access all of the datasets, make sure your api token role is set to at least 'investigator'. Investigation query view will provide you access to all of the datasets except endpoints and host_inventory. For additional information see Predefined User Roles for Cortex XDR

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Cortex XDR Alerts Handling v2

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

This playbook is used to loop over every alert in a Cortex XDR incident. Supported alert categories

**Inputs:**

- `incident_id`: Incident ID.
- `alert_id`: Alert ID.
- `InternalIPRanges`: A list of IP ranges to check the IP against. The list should be provided in CIDR notation, separated by commas. An example of a list of rang


## Cortex XDR disconnected endpoints

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

A Job to periodically query disconnected Cortex XDR endpoints with a provided last seen time range playbook input. The Collected data, if found will be generated to a CSV report, including a detailed list of the disconnected endpoints. The report will be sent to the recipient's provided email addresses in the playbook input. The playbook includes an incident type with a dedicated layout to visualize the collected data. To set the job correctly, you will need to.  The scheduled run time and the timestamp relative date should be identical, If the job is recurring every 7 days, the time range should be 7 days as well

**Inputs:**

- `LastSeenStartDate`: Last seen start date, in relative timestamp - "1 Day" or "7 days"
- `LastSeenEndDate`: Last seen end date, in relative timestamp - "1 Day" or "7 days" For the current day use "0 days"
- `Email`: Email addresses to send the disconnected endpoints report.
- `MessageBody`: Body for the report email message.


## Cortex XDR incident handling v3

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

This playbook is triggered by fetching a Palo Alto Networks Cortex XDR incident. The playbook syncs and updates new XDR alerts that construct the incident and triggers a sub-playbook to handle each alert by type. Then, the playbook performs enrichment on the incident’s indicators and hunts for related IOCs. Based on the severity, it lets the analyst decide whether to continue to the remediation stage or close the investigation as a false positive. After the remediation, if there are no new alerts, the playbook stops the alert sync and closes the XDR incident and investigation. For performing the bidirectional sync, the playbook uses the incoming and outgoing mirroring feature added in the platform version 6.0.0. After the Calculate Severity - Generic v2 sub-playbook’s run, the platform, and it will sync only from the platform, so manual changes for the severity field in XDR will not update in the the platform incident

**Inputs:**

- `LinkSimilarIncidents`: This input indicates whether the playbook will link similar incidents. To link similar incidents, specify Yes/No.
- `CriticalUsernames`: A comma-separated list of names of critical users in the organization.This will affect the calculated severity of the incident.
- `CriticalHostnames`: A comma-separated list of names of critical endpoints in the organization. This will affect the calculated severity of the incident.
- `CriticalADGroups`: A comma-separated list of DN names of critical Active Directory groups. This will affect the severity calculated for this incident.
- `incident_id`: Incident ID.
- `XDRDomain`: XDR instance domain
- `InternalRange`: A comma-separated list of internal IP ranges to check IP addresses against. The list should be provided in CIDR notation. For example: "172.
- `InternalDomainName`: The organizations internal domain name. This is provided for the IsInternalHostName script that checks if the detected host names are intern


## Cortex XDR IOCs - Disable expired IOCs in XDR

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

This is a sub-playbook of "Cortex XDR IOCs - Push new IOCs to XDR (Main)". This playbook disables indicators in Cortex XDR after they expire from the platform

**Inputs:**

- `batch_size`: This parameter will set the batch size to be pushed into Cortex XDR with every iteration of the loop.
- `query`: The query used to search for IOCs from the platform. This query must include `tags:xdr_pushed` in order to work properly.


## Cortex XDR IOCs - Push new IOCs to XDR

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

This is a sub-playbook of "Cortex XDR IOCs - Push new IOCs to XDR - Main" and should not be run on its own. This sub-playbook will retrieve IOCs according to the users query input (passed from the main playbook) and push them into Cortex XDR, and mark them as "xdr_pushed" or "xdr_not_processed" for further processing

**Inputs:**

- `batch_size`: This parameter will set the batch size to be pushed into Cortex XDR with every iteration of the loop.
- `query`: The query used to search for IOCs from the platform. This query must include `-tags:xdr_pushed and -tags:xdr_not_processed` in order to work


## Cortex XDR IOCs - Push new IOCs to XDR (Main)

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

This is the main playbook for Cortex XDR IOCs sync. The playbook will "sync" IOCs into Cortex XDR by pushing new IOCs in and disabling expired IOCs. The playbook utilizes the platform. The playbook will iterate over the IOCs pushing them in batches into Cortex XDR. In the second phase, the playbook will disable expired IOCs that were previously pushed into Cortex XDR. We recommend running this playbook as a job a few times a day after disabling the integration sync function

**Inputs:**

- `batch_size`: This parameter will set the batch size to be pushed into Cortex XDR with every iteration of the loop.
- `query`: The query used to search for IOCs from the platform. This query must include `-tags:xdr_pushed and -tags:xdr_not_processed` in order to work


## Cortex XDR Lite - Incident Handling

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

The Cortex XDR Lite - Incident Handling playbook is triggered by fetching a Palo Alto Networks Cortex XDR incident and executes the following: Analysis: Investigation: Verdict: Verdict Handling: To utilize this playbook as the default for handling XDR incidents, the classifier should be empty, and the selected incident type should be Cortex XDR - Lite. The selected Mapper (incoming) should be XDR - Incoming Mapper, and the selected Mapper (outgoing) should be Cortex XDR - Outgoing Mapper

**Inputs:**

- `Username`: Username.
- `incident_id`: Incident ID.
- `Hostname`: Hostname.
- `EndpointID`: XDR endpoint ID.
- `XDRDomain`: XDR instance domain.
- `InternalRange`: This input is used in the "Entity Enrichment - Generic v3" playbook.A list of internal IP ranges to check IP addresses against. The comma-se
- `XDRRelatedAlertsThreshold`: This is the minimum threshold for XDR-related alerts of medium severity or higher, based on MITRE tactics used to identify malicious activit
- `AutoBlockIndicators`: Possible values: True/False. Default: True.Should the given indicators be automatically blocked, or should the user be given the option to c


## Cortex XDR Remote PsExec with LOLBIN command execution alert

**Type:** playbook  
**Product:** Cortex XDR by Palo Alto Networks  

The "Remote PsExec-like LOLBIN Command Execution" playbook is designed to address and respond to alerts indicating suspicious activities related to remote PsExec-like LOLBIN command execution from an unsigned non-standard source. The playbook aims to efficiently: The playbook is designed to run as a sub-playbook in "Cortex XDR Incident Handling - v3 & Cortex XDR Alerts Handling". It depends on the data from the parent playbooks and cannot be used as a standalone version

**Inputs:**

- `SrcIPAddress`: The remote IP address that executed the process.
- `alerts_ids`: The IDs of the relevant alerts.
- `AutoRemediation`: Whether remediation will be run automatically or manually. If set to "True" - remediation will be automatic.
- `EndpointIDs`: The IDs of the victim endpoint.
- `HighAlertsThreshold`: The threshold number of additional high severity alerts.
- `CriticalAlertsThreshold`: The threshold number of additional critical severity alerts.


## CortexXDRAdditionalAlertInformationWidget

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

This script retrieves additional original alert information from the context


## CortexXDRCloudProviderWidget

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

This script returns an HTML result of the cloud providers in the incident. The result will be displayed in the following font colors: AWS - red, GCP - green, Azure - blue


## CortexXDRIdentityInformationWidget

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

This widget displays Cortex XDR identity information


## CortexXDRInvestigationVerdict

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

This script displays the incident verdict based on the 'Verdict' field


## CortexXDRRemediationActionsWidget

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

This widget displays Cortex XDR remediation action information


## DBotGroupXDRIncidents

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

Train clustering model on Cortex XDR incident type

**Inputs:**

- `returnWidgetType`: The type of the widget to return.
- `fromDate`: The start date by which to filter incidents. Date format will be the same as in the incidents query page, for example: "3 days ago", ""2019-
- `limit`: The maximum number of incidents to fetch
- `incidentType`: The Cortex XDR incident type
- `searchQuery`: Input search query from the dashboard
- `modelExpiration`: Period of time (in hours) before retraining the model. Default is "24".
- `forceRetrain`: Determines whether to force the model to re-train. Default is "False".
- `fieldsToDisplay`: Comma-separated list of additional incident fields to display, but which will not be taken into account when computing similarity.


## Detonate File From URL - WildFire

**Type:** playbook  
**Product:** WildFire by Palo Alto Networks  

Detonates one or more files using the Wildfire integration. This playbook returns relevant reports to the War Room and file reputations to the context data. The detonation supports the following file types: APK, JAR, DOC, DOCX, RTF, XLS, XLSX, PPT, PPTX, XML, PE32, PDF, DMG, PKG, RAR, 7Z. This playbook is deprecated. please use the Detonate File From URL - WildFire v2 instead

**Inputs:**

- `FileURL`: The URL of the web file to detonate. The FileUrl is taken from the context.
- `Interval`: The duration for executing the pooling (in minutes).
- `Timeout`: The duration after which to stop pooling and to resume the playbook (in minutes).
- `ReportFileType`: The resource type to download. The default is "pdf". XML is also possible.


## Detonate File From URL - WildFire v2

**Type:** playbook  
**Product:** WildFire by Palo Alto Networks  

Detonate one or more files using the Wildfire v2 integration. This playbook returns relevant reports to the War Room and file reputations to the context data. The detonation supports the following file types - APK, JAR, DOC, DOCX, RTF, XLS, XLSX, PPT, PPTX, XML, PE32, PDF, DMG, PKG, RAR, 7Z

**Inputs:**

- `FileURL`: URL of the web file to detonate. The FileUrl is taken from the context.
- `Interval`: Duration for executing the pooling (in seconds).
- `Timeout`: The duration after which to stop pooling and to resume the playbook (in seconds).
- `ReportFileType`: The resource type to download. Default is pdf. XML is also possible.


## Detonate URL - WildFire v2.1

**Type:** playbook  
**Product:** WildFire by Palo Alto Networks  

Detonate a webpage or remote file using the WildFire integration. This playbook returns relevant reports to the War Room and file reputations to the context data. The detonation supports the following file types: APK, JAR, DOC, DOCX, RTF, OOXLS, XLSX, PPT, PPTX, XML, PE32, PDF, DMG, PKG, RAR, 7Z, JS. This playbook is deprecated. please use the Detonate URL - WildFire v2.2 instead

**Inputs:**

- `URL`: URL of the webpage or file URL to detonate. The URL is taken from the context.
- `Interval`: Duration for executing the polling (in minutes).
- `Timeout`: The duration after which to stop polling and to resume the playbook (in minutes).
- `ReportFileType`: The resource type to download. Default is PDF. XML is also possible.


## Detonate URL - WildFire v2.2

**Type:** playbook  
**Product:** WildFire by Palo Alto Networks  

Detonate a webpage or remote file using the WildFire v2 integration. This playbook returns relevant reports to the War Room and file reputations to the context data. The detonation supports the following file types: APK, JAR, DOC, DOCX, RTF, OOXLS, XLSX, PPT, PPTX, XML, PE32, PDF, DMG, PKG, RAR, 7Z, JS

**Inputs:**

- `URL`: URL of the webpage or file url to detonate. The URL is taken from the context.
- `Interval`: Duration for executing the polling (in seconds).
- `Timeout`: The duration after which to stop polling and to resume the playbook (in seconds).
- `ReportFileType`: The resource type to download. Values: PDF (default), XML.


## Detonate URL - WildFire-v2

**Type:** playbook  
**Product:** WildFire by Palo Alto Networks  

Detonates a webpage or a remote file using the WildFire integration. This playbook returns relevant reports to the War Room and file reputations to the context data. The detonation supports the following file types: APK, JAR, DOC, DOCX, RTF, OOXLS, XLSX, PPT, PPTX, XML, PE32, PDF, DMG, PKG, RAR, 7Z

**Inputs:**

- `URL`: The URL of the webpage or the file URL to detonate. The URL is taken from the context.
- `Interval`: The duration for executing the pooling (in minutes).
- `Timeout`: The duration after which to stop pooling and to resume the playbook (in minutes).
- `ReportFileType`: The resource type to download. The default is pdf. XML is also possible.


## device-security-alert-post-processing

**Type:** script  
**Product:** Device Security by Palo Alto Networks  

Resolves the alert in the Device Security portal via the API. Designed to run as a post-processing script

**Inputs:**

- `close_reason`: The reason the alert was closed (either 'Resolved' or 'No Action Needed').


## device-security-check-servicenow

**Type:** script  
**Product:** Device Security by Palo Alto Networks  

Closes the the platform. This command should be run in a Job


## device-security-get-raci

**Type:** script  
**Product:** Device Security by Palo Alto Networks  

Calculates the responsible and informed parties for a Device Security incident by matching incident and device details against the Device Security configuration list

**Inputs:**

- `incident_name`: The name of the Device Security incident.
- `raw_type`: The raw type of the incident.
- `category`: The device category.
- `profile`: The device profile.
- `vendor`: The device vendor.
- `model`: The device model.
- `device_security_config_list_name`: The name of the list containing the Device Security configuration.


## device-security-vuln-post-processing

**Type:** script  
**Product:** Device Security by Palo Alto Networks  

Resolves the vulnerability incident in the Device Security portal via the API. Designed to run as a post-processing script


## DeviceSecurityHistorySection

**Type:** script  
**Product:** Device Security by Palo Alto Networks  

Displays the current vulnerability incident's Reason History JSON field as a Markdown table in the Detection & Resolution History layout section. The table includes timestamp, action, evidence type, user email, resolution and reopen types, system event, reason, and evidence. Empty history displays an informational message. Invalid JSON or a history value other than an object or list of objects returns an error. This script runs in the incident context and has no arguments or context outputs


## DeviceSecurityThreatFrameworkMappings

**Type:** script  
**Product:** Device Security by Palo Alto Networks  

Displays MITRE ATT&CK Enterprise and ICS technique mappings and IEC 62443 references in a dynamic incident layout section. The script reads the Device Security MITRE Mappings Raw (devicesecuritymitremappingsraw) and Device Security IEC References (devicesecurityiecreferences) incident fields. It accepts structured or JSON-encoded data, groups techniques by framework, and removes duplicate rows. Missing mappings or references display N/A. This script runs in the incident context and has no arguments or context outputs


## DLP - Get User Feedback

**Type:** playbook  
**Product:** Enterprise DLP by Palo Alto Networks  

Get the user feedback on a blocked file, whether it is false or true positive and if an exemption is needed

**Inputs:**

- `UserDisplayName`: The display name of the user.
- `MessageApp`: Choose the application to communicate with the users.Available options:- Slack - Microsoft Teams
- `SendMailInstance`: The name of the instance to be used when executing the "send-mail" command in the playbook. In case it will be empty, all available instance
- `UserEmail`: The user email address.
- `Detections`: Detected violation snippets.


## DLP - User Message App Check

**Type:** playbook  
**Product:** Enterprise DLP by Palo Alto Networks  

Check if the given message app exists and is configured and retrieve the user details from it

**Inputs:**

- `UserEmail`: The user email address that will be used through email communication in case both Slack and MS Teams are not enabled.
- `UserDisplayName`: The display name of the user. Will be used in case MS Teams or Email are the message app.
- `UserMessageApp`: The communication method with the user.Can be one of the following:- Slack- Microsoft Teams- EmailIf you choose to set "Email", it's also po


## DLP Incident Feedback Loop

**Type:** playbook  
**Product:** Enterprise DLP by Palo Alto Networks  

Collects feedback from user about blocked files

**Inputs:**

- `ApprovalTarget`: Can be either empty or one of the following:- Manager- <email_address>- Manual"Manager" - the user's manager details will be retrieved using
- `ActionOnApproverNotFound`: If the approver cannot be contacted via Slack or MS Teams, what should be the next action:- Deny- Approve- Manual
- `SendMailInstance`: This input is only relevant when the "UserMessageApp" or "ApproverMessageApp" are set to "Email".The name of the instance to be used when ex
- `UserMessageApp`: The communication method with the user.Can be one of the following:- Slack- Microsoft Teams- EmailIf you choose to set "Email", it's also po
- `ApproverMessageApp`: The communication method with the approver.Can be one of the following:- Slack- Microsoft Teams- Email- ManualIf you choose to set "Email", 
- `DenyMessage`: The message that users will receive when they are denied.


## DlpAskFeedback

**Type:** script  
**Product:** Enterprise DLP by Palo Alto Networks  

Sends a message via Slack to the user whose file upload violated DLP policies and triggered the incident

**Inputs:**

- `messenger`: The messenger to use for sending notification,
- `file_name`: The name of the file that triggered the incident.
- `data_profile_name`: The name of the DLP data profile that detected the violation.
- `app_name`: The application that performed the upload.
- `task`: A manual task that this task can close.
- `user_display_name`: The user name displayed in the Slack message.
- `user_id`: The user ID to identify the recipient in Slack.
- `snippets`: The snippets of the violation.


## EntryWidgetNumberHostsXDR

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

Entry widget that returns the number of hosts in a Cortex XDR incident


## EntryWidgetNumberRegionsXCLOUD

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

Entry widget that returns the number of regions in a Cortex XDR incident


## EntryWidgetNumberResourcesXCLOUD

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

Entry widget that returns the number of resources in a Cortex XDR incident


## EntryWidgetNumberUsersXDR

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

Entry widget that returns the number of users that participated in a specified Cortex XDR incident


## EntryWidgetPieAlertsXDR

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

Entry widget that returns a pie chart of alerts for a specified Cortex XDR incident by alert severity (low, medium, and high)


## EntryWidgetPortBasedRules

**Type:** script  
**Product:** PAN-OS Policy Optimizer (beta)  

Entry widget that returns the number of port based rules found by PAN-OS policy optimizer


## EntryWidgetUnusedApplications

**Type:** script  
**Product:** PAN-OS Policy Optimizer (beta)  

Entry widget that returns the number of rules with unused applications found by PAN-OS policy optimizer


## EntryWidgetUnusedRules

**Type:** script  
**Product:** PAN-OS Policy Optimizer (beta)  

Entry widget that returns the number of unused rules found by PAN-OS policy optimizer


## F5 Application Security Manager (WAF)

**Type:** integration  
**Product:** F5 firewall  

Use the F5 ASM integration to read information and to manage F5 firewall. This integration was integrated and tested with version 15.1.0 of F5 ASM

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## F5 firewall

**Type:** integration  
**Product:** F5 firewall  

Use the F5 Firewall integration to manage your F5 firewall rules

**Commands:**

- `None`: 


## Fidelis Elevate Network

**Type:** integration  
**Product:** Fidelis Elevate Network  

Automate Detection and Response to Network Threats and data leakage in your organization with Fidelis Elevate Network Integration. This integration was integrated and tested with version 9.2.4 of Fidelis Elevate Network

**Commands:**

- `None`: 


## FireEye NX

**Type:** integration  
**Product:** FireEye Network Security (NX)  

FireEye Network Security is an effective cyber threat protection solution that helps organizations minimize the risk of costly breaches by accurately detecting and immediately stopping advanced, targeted, and other evasive attacks hiding in internet traffic. This integration was integrated and tested with version 2.0.0 of FireEyeNX APIs

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Illusive - Incident Escalation

**Type:** playbook  
**Product:** Illusive Networks  

This playbook is used for creating an automatic analysis of the Illusive's incident details, in order to end up with a certain score or a set of insights that will enable automatic decisions and actions

**Inputs:**

- `proximity_threshold`: The maximum number of steps from crown jewel, or domain admin credentials to determine the proximity as high-risk
- `events_threshold`: The minimum number of associated events to determine this incident as a multiple-events incident
- `proximity_weight`: The unified score in case the proximity to a crown jewel and/ or the proximity to domain admin credentials is under the specified threshold
- `triggering_weight`: The unified score in case the triggering process has been found malicious and/ or the triggering deception is ransomware
- `events_weight`: The score in case the number of events in the inspected incident is above the specified threshold
- `rdp_weight`: The score in case there is an active RDP connection to the source host
- `illusive_incident_id`: The incident ID of the Illusive Networks Incident


## Illusive-Retrieve-Incident

**Type:** playbook  
**Product:** Illusive Networks  

This playbook is used for retrieving an extensive view over a detected incident by retrieving the incident details and a forensics timeline if and when forensics have been successfully collected

**Inputs:**

- `incident_id`: The desired incident ID to retrieve.
- `start_date`: The starting date of the forensics timeline.
- `end_date`: The last date of the forensics timeline.


## IllusiveNetworks

**Type:** integration  
**Product:** Illusive Networks  
**Commands:**

- `None`: 
- `None`: 


## iot-security-alert-post-processing

**Type:** script  
**Product:** IoT by Palo Alto Networks  

IoT alert post processing script to resolve the alert in IoT security portal using API

**Inputs:**

- `close_reason`: The reason the alert was closed (either 'Resolved' or 'No Action Needed').


## iot-security-check-servicenow

**Type:** script  
**Product:** IoT by Palo Alto Networks  

Close the the platform incident if the IoT ServiceNow ticket was closed. This command should be run in a Job


## iot-security-get-raci

**Type:** script  
**Product:** IoT by Palo Alto Networks  

IoT RACI model script

**Inputs:**

- `alert_name`: The name of the IoT alert.
- `raw_type`: The raw type of the incident.
- `category`: The device category.
- `profile`: The device profile.
- `vendor`: The device vendor.
- `model`: The device model.
- `iot_config_list_name`: The variable name for IOT_CONFIG.


## iot-security-vuln-post-processing

**Type:** script  
**Product:** IoT by Palo Alto Networks  

An IoT vulnerability post processing script to resolve the vulnerability incident in IoT security portal using the API


## List Cisco Stealthwatch Security Events

**Type:** playbook  
**Product:** Cisco Secure Network Analytics (Stealthwatch)  

This playbook lists security events and returns the results to the context

**Inputs:**

- `timeout`: The amount of time to wait before a timeout occurs (in minutes).
- `interval`: Polling frequency - how often the polling command should run (in minutes).
- `range`: Range of results to return (e.g., 0-20).
- `tenant_id`: Tenant ID represents the domain on Cisco Stealthwatch.
- `time_range`: 


## Manage Private App Segment - Netskope

**Type:** playbook  
**Product:** Netskope - Direct to Zero Trust  

Creates, modifies, or deletes a Netskope private application (ZTNA/NPA) "segment" (Netskope's own API models this as one Private App object: a host + its protocol/port entries + publishers, per /api/v2/steering/apps/private/{private_app_id} - there is no separate "segment" sub-resource in the API, so this playbook manages the whole private app object). Checks whether the Action input was provided, checks whether a Netskope integration instance is enabled (matching any brand name containing "Netskope"), then branches on Action: The playbook uses the modify operation for partial updates and supports adding or removing individual field values without replacing the whole object. For modify/delete, you can provide AppID directly, or leave it blank and provide AppName instead - netskopev2-list-private-apps has no name filter argument, so the playbook fetches every private app and resolves AppName to an ID itself (also handling the "[app_name]" bracket-wrapping Netskope applies in list responses). If no app or more than one app matches that name, the playbook stops with a clear error rather than guessing. Similarly, PublisherNames takes plain publisher names (e.g. "AWS-NPA") instead of requiring you to already know each publisher_id - netskopev2-list-publishers also has no name filter, so the playbook resolves each name and builds the {"publisher_id": ., "publisher_name": .} JSON array the create/update commands expect. Ports takes a comma-separated list of port numbers. The pla

**Inputs:**

- `Action`: Required. Must be create, modify, or delete. Any other value produces an explicit error and no Netskope command is run.
- `AppID`: ID of the existing private app to modify or delete. Optional for Action=modify/delete if AppName is provided instead - netskopev2-list-priva
- `AppName`: Name of the private app. Required for Action=create. For Action=modify, either leave blank to keep the current name, or use it (with AppID b
- `Host`: IP address or hostname of the private app segment - comma-separated for multiple hosts (e.g. "10.0.0.1,10.0.0.2" or "webserver.local,192.168
- `Ports`: Comma-separated port numbers (e.g. "443,8080,22"). The playbook builds the required protocol object array. Required for Action=create; optio
- `ProtocolType`: Transport protocol applied to every port in Ports (e.g. "tcp" or "udp") - all ports share this one type. Also used for any newly added ports
- `HostsToAdd`: Action=modify only. Comma-separated hosts to add to the app's existing host list (e.g. "10.0.0.5") without discarding the current ones. Unli
- `PortsToAdd`: Action=modify only. Comma-separated ports to add to the app's existing protocols (e.g. "8080") without discarding the current ones. Protocol


## Netskope (API v1)

**Type:** integration  
**Product:** Netskope  
**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Netskope (API v2)

**Type:** integration  
**Product:** Netskope  

Netskope API v2 provides a powerful interface for managing and monitoring Netskope deployments. It enables users to retrieve alerts and events, manage URL lists, and control clients. With Netskope API v2, organizations can proactively respond to security threats, enforce web access policies, and efficiently administer their Netskope environment. This integration was integrated and tested with version 2 of the Netskope API. To successfully instantiate an instance of the Netskope API v2 integration under the RBACv3 framework, follow the steps below. Note: Netskope has deprecated the legacy single-step API token generation process. All new and migrated tenants must use RBACv3 to create API tokens through Service Accounts. Follow the instructions under the section Create a New Service Account. Ensure the Service Account has access to the following functional areas: In total 4 sections need to be enabled: In the Administration section, select Function > Audit Log and grant it View rights. Under Users & Groups, select Manage: Functions that need to be set to view: Application Events, Page Events, Network Events, and Alerts. Select Access Control, for the Infrastructure function, grant View rights. For the URL List, set to Manage and Apply. For DLP Incident, set to View

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## NetskopeBuildProtocolsJson

**Type:** script  
**Product:** Netskope - Direct to Zero Trust  

Builds the JSON array that netskopev2-create-private-app/netskopev2-update-private-app expect for their protocols argument (e.g. [{"type": "tcp", "port": "443"}]) from a plain comma-separated port list, so callers don't need to hand-write JSON

**Inputs:**

- `ports`: The comma-separated port numbers (e.g. "443,8080,22"). Leave empty to leave protocols unset (e.g. when modifying a private app without chang
- `protocol_type`: The transport protocol applied to every port in "ports" (e.g. "tcp" or "udp"). Netskope private apps support one protocol type per value, so


## NetskopeFileHashSync

**Type:** script  
**Product:** Netskope - Direct to Zero Trust  

Searches the platform, in which case new hash indicators land under generic "File" instead - searching both covers either case), extracts valid MD5 (32 hex chars) / SHA256 (64 hex chars) hashes from either the indicator's value or its md5/sha256 CustomFields, and - since Netskope's v1 file hash list API has no read-back endpoint and every update replaces the full list - returns both the newly found hashes and the full merged set (existing_hashes plus new) ready to send as a full replace

**Inputs:**

- `tags`: The optional comma-separated indicator tags to further restrict the search (e.g. "malware"). If omitted, all File-type indicators are consid
- `skip_tags`: The optional comma-separated indicator tags to exclude. Any indicator carrying one of these tags is skipped.
- `indicator_query`: An additional the platform. The default selects active indicators with a Bad reputation.
- `existing_hashes`: The comma-separated list of hashes already tracked for this Netskope file hash list (from the NetskopeGetthe platformListContent script's ou
- `max_indicators`: The maximum number of File indicators to pull from the platform.


## NetskopeFileScanLabels

**Type:** script  
**Product:** Netskope - Direct to Zero Trust  

Builds the setIncident addLabels JSON string from a netskopev2-get-scan-report result (jobid, status, verdict, md5, sha256)

**Inputs:**

- `scan_result`: The Netskope.FileScanReport context output from netskopev2-get-scan-report (a dict, or a single-element list if the platform.FileScanReport}


## NetskopeGetthe platformListContent

**Type:** script  
**Product:** Netskope - Direct to Zero Trust  

Reads (and creates if missing) a the platform, since Netskope's v1 hash-list API has no read-back endpoint

**Inputs:**

- `listName`: The name of the the platform.


## NetskopeIndicatorSync

**Type:** script  
**Product:** Netskope - Direct to Zero Trust  

Pulls bounded Domain, URL, IP, and CIDR indicators from the platform. It skips values already present in the target profile. When profile_id is given, it appends the new values in batches of at most chunk_size and deploys only when deploy is explicitly enabled. Without profile_id, it only prepares the new-value list for a separate create-profile step

**Inputs:**

- `tags`: The optional comma-separated indicator tags to further restrict the search (e.g. "netskope-block"). If omitted, all indicators of the given 
- `skip_tags`: The optional comma-separated indicator tags to exclude - any indicator carrying one of these tags is skipped even if it matches tags/indicat
- `indicator_query`: An additional the platform. The default selects active indicators with a Bad reputation.
- `indicator_types`: The comma-separated indicator types to pull from the platform. Must be one or more of Domain, URL, IP, CIDR.
- `profile_id`: The ID of an existing Netskope Destination Profile to append the new values to (and deploy). If omitted, no append/deploy happens - the scri
- `existing_values`: The comma-separated list of values already in the target destination profile (from netskopev2-list-destination-profiles) - used to skip valu
- `max_indicators`: The maximum number of indicators to pull from the platform.
- `chunk_size`: The maximum number of values per append call, matching netskopev2-update-destination-profile-values' 1-10-per-call limit.


## NetskopeMergePrivateAppFields

**Type:** script  
**Product:** Netskope - Direct to Zero Trust  

Fetches a private app's current host, protocols, and tags, then applies the requested additions or removals without discarding the other values. This supports the Manage Private App Segment modify flow because netskopev2-update-private-app (PATCH) replaces host, protocols, and tags wholesale rather than merging them

**Inputs:**

- `app_id`: The ID of the private app to read current host/protocols/tags from. Required only if hosts_to_add, ports_to_add, hosts_to_remove, ports_to_r
- `host`: The direct-replace host value (from the Host input) - passed through unchanged unless hosts_to_add or hosts_to_remove is also provided, in w
- `protocols_json`: The direct-replace protocols JSON (from Netskope.BuiltProtocols.ProtocolsJson) - passed through unchanged unless ports_to_add or ports_to_re
- `tags`: The direct-replace comma-separated tags value (from the Tags input) - passed through unchanged unless tags_to_add or tags_to_remove is also 
- `hosts_to_add`: The comma-separated hosts to add to the app's existing host list (e.g. "10.0.0.5") - fetches the app's current host first and merges, dedupl
- `ports_to_add`: The comma-separated ports to add to the app's existing protocols (e.g. "8080") - fetches the app's current protocols first and merges, skipp
- `hosts_to_remove`: The comma-separated hosts to remove from the app's existing host list (e.g. "10.0.0.5") - fetches the app's current host first and removes j
- `ports_to_remove`: The comma-separated ports to remove from the app's existing protocols (e.g. "8080") - fetches the app's current protocols first and removes 


## NetskopeResolvePrivateAppId

**Type:** script  
**Product:** Netskope - Direct to Zero Trust  

Fetches all private apps and matches one by name to resolve its application ID. This is necessary because netskopev2-list-private-apps has no name filter argument and Netskope wraps app_name in brackets in list responses, for example, "[test server]"

**Inputs:**

- `app_id`: The app ID, if already known. If provided, used directly - no lookup happens.
- `app_name`: The app name to look up if app_id isn't provided. Matched case-insensitively against netskopev2-list-private-apps' app_name field (Netskope 


## NetskopeResolvePublishers

**Type:** script  
**Product:** Netskope - Direct to Zero Trust  

Fetches all publishers and resolves each requested name to its publisher_id, building the {publisher_id, publisher_name} JSON array that netskopev2-create-private-app and netskopev2-update-private-app expect for their publishers argument. This is necessary because netskopev2-list-publishers has no name filter argument

**Inputs:**

- `publisher_names`: The comma-separated publisher names to resolve to publisher_id (matched case-insensitively against netskopev2-list-publishers' publisher_nam


## NetskopeSetthe platformListContentWithRetry

**Type:** script  
**Product:** Netskope - Direct to Zero Trust  

Writes to a the platform, retrying a few times on a transient Elasticsearch version-conflict (409) error - used to track Netskope file hash list content between playbook runs

**Inputs:**

- `listName`: The name of the the platform.
- `listData`: The full content to save to the list.


## NetskopeURLLookupLabels

**Type:** script  
**Product:** Netskope - Direct to Zero Trust  

Builds the setIncident addLabels JSON string from a netskopev2-url-lookup result, joining nested categories/url_lists name arrays into flat comma-joined label values

**Inputs:**

- `lookup_result`: The Netskope.URLLookup context output (a list, or a single-element dict if the platform.URLLookup}.


## Nozomi Networks

**Type:** integration  
**Product:** Nozomi Networks  

The Nozomi Networks integration enables the collection of alert and asset information from Nozomi’s suite of products, including Guardian, CMC, and the cloud-based Vantage platform. These solutions provide comprehensive OT/IoT/IT network monitoring through asset discovery, network visualization, vulnerability assessment, risk monitoring, and threat detection — all within a unified platform. This integration is used to gather alert and asset information from Nozomi

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Palo Alto Networks AIOps

**Type:** integration  
**Product:** Palo Alto Networks AIOps  

Palo Alto Networks Best Practice Assessment (BPA) analyzes NGFW and Panorama configurations and compares them to the best practices. This integration was integrated and tested with version from March 2024 of PaloAltoNetworksAIOps

**Commands:**

- `None`: 


## Palo Alto Networks Automatic SLR

**Type:** integration  
**Product:** Automatic SLR by Palo Alto Networks  

Use the Palo Alto Networks NGFW API to automatically generate a Security Lifecycle Review (SLR) Report

**Commands:**

- `None`: 


## Palo Alto Networks Cortex XDR - Investigation and Response

**Type:** integration  
**Product:** Cortex XDR by Palo Alto Networks  

Cortex XDR is the world's first detection and response app that natively integrates network, endpoint, and cloud data to stop sophisticated attacks. This integration was integrated and tested with version 2.6.5 of Cortex XDR - IR. <~PLATFORM> Note: On the Cortex Platform, this integration is used to connect to a different Cortex XDR/XSIAM tenant. Configuring the Server URL parameter with the URL of the tenant this integration instance is running on is not supported - the integration will fail to run. For actions on the local tenant, use the built-in Cortex Platform commands instead. </~PLATFORM>

**Commands:**

- `None`: 


## Palo Alto Networks Device Security

**Type:** integration  
**Product:** Device Security by Palo Alto Networks  

Use the Palo Alto Networks Device Security integration to fetch alerts and vulnerabilities, retrieve device details, and resolve security incidents (previously Zingbox)

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Palo Alto Networks Enterprise DLP

**Type:** integration  
**Product:** Enterprise DLP by Palo Alto Networks  

Palo Alto Networks Enterprise DLP discovers and protects company data across every data channel and repository. Integrated Enterprise DLP enables data protection and compliance everywhere without complexity. This integration was integrated and tested with version 2.0 of Palo Alto Networks Enterprise DLP. Note: Incidents are fetched from every control point the tenant can see. Use the DLP Channels parameter to narrow the fetch to specific control points. Note: Starting from version 2.4.0, incidents are fetched from the Enterprise DLP v4 incident inventory API (/v4/api/incidents). This API returns a summary of each incident, so fetched incidents no longer include several attributes that the previous incident notifications API returned under incidentDetails. These include the URL, source and destination IP addresses, user name, email, department, location and manager, upload or download direction, asset size and hash, data patterns, device information and every data profile except the last one. The fields mapped by the default Data Loss Prevention mapper are still populated. If you mapped any of these attributes in a custom mapper, layout or playbook, they are now empty. You can still view these attributes in the incident details in Strata Cloud Manager. Go to the Settings tab on the DLP web interface. Choose Alerts on the left menu. Follow all the steps under Setup Instructions. Make sure the toggle at the bottom is switched on

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Palo Alto Networks IoT

**Type:** integration  
**Product:** IoT by Palo Alto Networks  

This is the Palo Alto Networks IoT integration (previously Zingbox). This integration was integrated and tested with the Banff release of Palo Alto Networks IoT

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Palo Alto Networks PAN-OS

**Type:** integration  
**Product:** PAN-OS by Palo Alto Networks  

This integration supports both Palo Alto Networks Panorama and Palo Alto Networks Firewall. You can create separate instances of each integration, and they are not necessarily related or dependent on one another. This integration enables you to manage the Palo Alto Networks Firewall and Panorama. For more information see the PAN-OS documentation. This integration was integrated and tested with versions 8.xx, 9.xx, 10.xx and 11.xx of Palo Alto Firewall and Palo Alto Panorama

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Palo Alto Networks Security Advisories (Beta)

**Type:** integration  
**Product:** Security Advisories by Palo Alto Networks  

Queries the public repository of PAN-OS CVEs. This integration was integrated and tested with the beta version 1 of the Palo Alto Networks Security Advisories API. The Palo Alto Networks Security Advisories API is a representation of the GUI

**Commands:**

- `None`: 
- `None`: 


## Palo Alto Networks WildFire Reports

**Type:** integration  
**Product:** WildFire by Palo Alto Networks  

Generates a Palo Alto Networks WildFire PDF report. This integration is set up by default on the platform.5+ with the Threat Intel Module (TIM). It is designed for internal use with the TIM Sample Analysis feature. To run ad hoc CLI commands to generate WildFire reports, use the Palo Alto Networks WildFire v2 integration instead. This integration was created and tested with version 10.1 of WildFire

**Commands:**

- `None`: 


## Palo Alto Networks WildFire v2

**Type:** integration  
**Product:** WildFire by Palo Alto Networks  

Use the Palo Alto Networks Wildfire integration to automatically identify unknown threats and stop attackers in their tracks by performing malware dynamic analysis

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## PAN-OS - Add Anti-Spyware Security Profile To Rule

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

This playbook is designed to enhance the security level in PAN-OS firewalls by safely adding an Anti-Spyware security profile to a security rule. The playbook provides control over the behavior when a rule: The output of the playbook is the Anti-Spyware profile configured for the rule upon playbook completion. This can be

**Inputs:**

- `RuleName`: The name of the rule to which the Security Profile should be added.
- `SecurityProfileName`: The name of the Security Profile that should be added to the rule. If it doesn't exit, one will be created with the name specified here.
- `OverwriteProfileIfExists`: Whether to overwrite an existing Anti-Spyware Security Profile.If an Anti-Spyware Security Profile is configured to the rule through a group


## PAN-OS - Add Domains EDL To Anti-Spyware

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

This playbook add domains EDL to Panorama Anti-Spyware. It assigns External Dynamic List URLs that contain domains to block to Panorama Anti-Spyware. You can create an External Dynamic List (EDL) and add domains to it using the the platform. We recommend using this playbook as a one-time job. Once EDL is created and assigned to anti-spyware, domains can be blocked by adding them to the EDL

**Inputs:**

- `EDL_URL`: The URL from which to pull the EDL.
- `Add_To_Existing_PAN-OS_EDL`: Set to "true" to use the existing PAN-OS EDL.
- `PAN-OS_EDL_Name`: PAN-OS EDL name to create/edit if it exists (depending on the value in Add_To_Existing_PAN-OS_EDL).
- `Device_Group`: The device group for which to return addresses for the EDL (Panorama instances).
- `Certificate_Profile`: The certificate profile name for the URL that was previously uploaded to PAN OS.
- `Anti_Spyware_Profile`: Name of the anti-spyware profile to create OR to edit if it exists (depending on the value in Use_Existing_AntiSpyware_Profile).
- `Use_Existing_AntiSpyware_Profile`: Set to "true" to create a new anti-spyware profile.


## PAN-OS - Add Static Routes

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

Accepts a PAN-OS static route configuration and creates it in the PAN-OS instance

**Inputs:**

- `virtual_router_name`: The name of the virtual router to configure the static routes for.
- `route_name`: The name to identify the static route (up to 31 characters). The name is case-sensitive and must be unique. The name can contain, letters, n
- `interface_name`: The interface name where the static route will be added.
- `destination`: The IP address and network mask in CIDR notation: ip_address/mask. For example, 192.168.2.0/24 for IPv4 or 2001:db8::/32 for IPv6.
- `nexthop_type`: The type for the nexthop. Can be, "ip-address", "next-vr", "fqdn" or "discard".
- `nexthop_value`: The next hop value.
- `AutoCommit`: Whether to auto-commit the configuration to PAN-OS. Can be, "Yes" or "No".


## PAN-OS - Block Destination Service

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

This playbook blocks a destination IP and service (TCP or UDP port) by creating a rule for a specific device group on PAN-OS

**Inputs:**

- `LogForwarding`: Panorama log forwarding object name.
- `IP`: IP address to block.
- `AutoCommit`: This input establishes whether to commit the configuration automatically.True - Commit automatically.False - Commit manually.
- `DeviceGroup`: Target Device Group.
- `Port`: Destination port to block.
- `Protocol`: Protocol
- `ServiceNamePrefix`: Prefix of the Service name to be created.
- `RuleNamePrefix`: Prefix of the Rule name to be created.


## PAN-OS - Configure DNS Sinkhole

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

This playbook creates a DNS sinkhole in a PAN-OS firewall. It does the following: Once the configuration is completed, the playbook will create a Tag object and tag the relevant security rules to indicate that sinkholing is configured. That tag will be checked in consecutive playbook runs in order to minimize the actions done on the firewall and time spent in the playbook execution. How it works: A DNS sinkhole can be used to identify infected hosts on a network where there is an internal DNS Server in-route to the firewall that causes the reference of the original source IP address of the host that first originated the query to be lost (the query is received by the internal DNS server, and the internal DNS server sources a new query if the name-to-IP resolution is not locally cached). This causes the firewall to report observations of malicious DNS queries in the Threat logs where the source IP of the malicious DNS query is the Internal DNS server, which would force the administrator to look into the DNS Server logs to try to trace down what was the infected host that originally sourced the malicious DNS query. After a security profile with a "sinkhole" action for domains that are listed in the DNS signature source is applied to a rule that allows DNS traffic from the internal server/s to the external one, the threat logs will show that requests from the internal DNS server/s were sinkholed. However, the compromised systems will not appear in those logs. In order to find the

**Inputs:**

- `DNSSignatureSource`: The name of the signature source that contains the domains to sinkhole. It is used by the security profile to check if DNS requests for thes
- `SecurityProfileName`: The name of the Anti-Spyware Security Profile that will be applied to the DNS related rule, in order to filter the malicious domains and fac
- `PrimaryInternalDNSServerIP`: The IP of the primary internal DNS server. Used to find a policy that matches the malicious DNS queries that go out from the internal DNS se
- `SecondaryInternalDNSServerIP`: Optional - the IP of the secondary internal DNS server. Used to find a policy that matches the malicious DNS queries that go out from the in
- `PublicDNSServerIP`: The IP of the public DNS server that the organization is using to resolve external domains. This is needed to find the rule that allows DNS 
- `RuleNameToAllowDNS`: Optional - the name of the security rule that will allow DNS traffic.If permission is granted and no other rule is currently allowing DNS, t
- `AutoCreateRuleToAllowDNS`: Determines whether the playbook can automatically create a rule that specifically allows DNS traffic from the internal DNS servers to the pu
- `NetworkAdminEmail`: Optional - the email of the person who should approve the creation of a new security policy rule in the firewall. If no rule allows internal


## PAN-OS - Create Or Edit Rule

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

Creates or edits a Panorama rule and moves it into the desired position

**Inputs:**

- `device-group`: The device group to work on. Exists only in panorama.
- `rule_name`: The name of the rule to update, or the name of the rule that will be created.
- `log-forwarding-object-name`: The server address to which to forward logs.
- `rule-position`: The position of the rule in the ruleset. Can be, "Top", "Bottom", "Before", or "After". The default is "Bottom".
- `relative-rule-name`: If the rule-position that is chosen is before or after, specify the rule name to which it is related.
- `inbound-or-outbound-rule`: Determines if the rule is inbound or outbound.
- `element-to-add`: The element to add to the rule.
- `action-type`: The action that will be defined in the rule. Can be, "allow", "deny", or "drop".


## PAN-OS - Delete Static Routes

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

Deletes a PAN-OS static route from the PAN-OS instance

**Inputs:**

- `virtual_router_name`: The name of the virtual router to configure the static routes for.
- `route_name`: The name to identify the static route (up to 31 characters). The name is case-sensitive and must be unique. Can include, letters, numbers, s
- `AutoCommit`: Whether to auto-commit the configuration to PAN-OS. Can be, "Yes" or "No".


## PAN-OS - Extract IPs From Traffic Logs To Sinkhole

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

This playbook searches for outgoing traffic to the sinkhole address in PAN-OS. It should be used after a DNS sinkhole was created using the "PAN-OS - Configure DNS Sinkhole" playbook. If a DNS sinkhole was created manually, you should verify in your PAN-OS firewall that there is an address object for the sinkhole FQDN "sinkhole.paloaltonetworks.com", and that there is a rule denying traffic to it from any source. You may specify the name of the deny rule if you know it, or you can let the playbook find the rule automatically

**Inputs:**

- `OutputLogsForDetectedIPs`: Whether to output full traffic logs for the infected IPs.If set to True, this will output the logs containing the traffic from the compromis
- `RuleNameToDenyToSinkhole`: The name of the rule that will be created to deny traffic to the sinkhole address. This is required so that traffic logs will reveal the end
- `TimeToWaitForTraffic`: The time in seconds that the playbook will wait for hosts to generate traffic to the sinkhole address.Waiting for long periods of time will 
- `ReturnErrorForIncompleteConfig`: Whether to return errors if the configuration for the sinkhole is incomplete.An incomplete configuration will result in no logs being return


## PAN-OS - Identify Unused Policy Rules

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

The playbook collects and analyzes Palo Alto Networks NGFW policy rule hitcount information and generates a summary of unused rules for potential clean-up. Policy rules are classified into three categories: For firewalls in HA pairs, rules are only considered unused if all members of the HA group have zero hits for it

**Inputs:**

- `Rulebase`: The firewall rulebase to analyze. Must be one of the following:security, nat, decryption, application-override, authentication, dos, network


## PAN-OS - Job - Add Malicious Domains To Sinkhole

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

This TIM playbook should be run as a job. The playbook runs on domain indicators and performs various checks to decide if they should be sinkholed. If a domain is related to a campaign or a threat actor, or if it resolves to a malicious IP or has malware-related tags, the playbook will add a new tag to it in order to sinkhole that domain. The playbook assumes that the user is exporting indicators with the sinkhole tag to an EDL (External Dynamic List) using the Export Generic Indicators Service integration in the platform. That EDL should be connected to PAN-OS. It also assumes that a DNS sinkhole is configured in the PAN-OS firewall. However, these are not required for the sole purpose of tagging the domains. Note: This playbook has inputs from both the "From context data" tab and the "From indicators" tab

**Inputs:**

- `Indicator Query`: All domain indicators. In the playbook, the domains will be filtered by those used for malicious communication, and tagged to be sinkholed.
- `SinkholeTagForEDL`: The tag that should be applied to the domain so that it will be exported to the EDL using the Generic Export Indicators Service integration 
- `EnrichUnknownDomains`: Whether to enrich unknown domains. Enriching domains can be useful to gain additional information regarding reputation for domains from your
- `EnrichSuspiciousDomains`: Whether to enrich suspicious domains. Enriching domains can be useful to gain additional information regarding reputation for domains from y


## PAN-OS - Job - Remove Malicious Domains From Sinkhole

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

This playbook should be run as a job. It is used to periodically remove the specified tag from domain indicators. It should be used in conjunction with the "PAN-OS - Job - Add Malicious Domains To Sinkhole" playbook, to stop domains from being sinkholed after a certain amount of time. The idea is that traffic to malicious domains will not be redirected to a sinkhole address forever, as malicious domains tend to lose their malicious properties (become inactive, get taken down, or the malware using them is no longer used or maintained)

**Inputs:**

- `SinkholeTag`: The tag that will be removed from the tagged domain indicators.This should be the tag that was used to export the domains to the EDL using t
- `DaysTaggedBeforeRemoval`: The "decay period" - how many days should pass since the domains were tagged, before removing the sinkhole tag from those domains.The value 


## PAN-OS - Run Security Configuration Hygiene Checks

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

This playbook executes hygiene check commands using the PAN-OS integration and identifies items configured in a manner that do not meet minimum security best practices. It looks for the following: NOTE: This playbook is intended for use with a single PAN-OS Integration Instance

**Inputs:**

- `targetDevice`: The serial number of a specific firewall to target (Used when connected to Panorama) [Optional].When connected to Panorama, leaving this bla


## PAN-OS - Security Advisories Vulnerability Check

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

Checks if any Palo Alto Networks firewalls in your environment have PAN-OS software versions or GlobalProtect client package versions that are vulnerable to a specific CVE ID, as published on the Palo Alto Networks Security Advisories page. The playbook accepts an optional target parameter to check a specific firewall by serial number. If a non-Palo Networks CVE is provided, the playbook returns an empty output

**Inputs:**

- `cve_id`: The CVE ID published on the Palo Alto Networks Security Advisories page to check if any firewalls are affected by it.
- `target`: The serial number of a specific firewall to check if the above mentioned CVE affects it.


## PAN-OS Commit Configuration v2

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

Commit the PAN-OS Panorama or Firewall configuration. If specified as Panorama, it also pushes the Policies to the specified Device Group in the instance

**Inputs:**

- `device-group`: The device group to work on. Exists only in panorama.


## PAN-OS DAG Configuration

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

This playbook utilizes the Dynamic Address Group (DAG) capability of PAN-OS. DAG enables analysts to create a rule one time, where the group is the source/destination, and adds IP addresses dynamically without the need to commit the configuration every time. The playbook checks if the given tag already exists. If the tag exists, then the IP address is added to the tag. If the tag does not exist, a new address group is created with the given tag and a matching rule, and the configuration is committed

**Inputs:**

- `tag_name`: The name of the tag to add to PAN-OS. This can be a single tag.
- `ip_list`: The list of the IP addresses to block.
- `address_group_name`: The name of the group that will be created if the tag does not exist.
- `rule_name`: The name of the rule to update, or the name of the rule that will be created.
- `auto_commit`: Whether the rule will be committed automatically.
- `log-forwarding-object-name`: The server address to which to forward logs.
- `rule-position`: The position of the rule in the ruleset. Valid values are: * Top * Bottom * Before * AfterThe default position is 'Top'
- `relative-rule-name`: If the rule-position that is chosen is before or after, specify the rule name to which it is related.


## PAN-OS Log Forwarding Setup And Configuration

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

Sets up and maintains log forwarding for the Panorama rulebase. It can be run when setting up a new instance, or as a periodic job to enforce log forwarding policy. You can either update all rules and override previous profiles, or update only rules that do not have a log forwarding profile configured. ​

**Inputs:**

- `log-forwarding-name`: The name of the log-forwarding object that will be attached to all of the rules.
- `auto_commit`: Whether the rule should be committed automatically or manually.
- `pre-post-rulebase`: Either the pre-rulebase or post-rulebase, depending on the rule structure.
- `device-group`: The device group to work on.
- `override-existing-profiles`: Whether the log-forwarding profiles that were already defined should be overrode.


## PAN-OS logging to Strata Logging Service - Action Required

**Type:** playbook  
**Product:** PAN-OS to Strata Logging Service Monitoring  

This Playbook initiates the steps needed to investigate the PAN-OS logging to Strata Logging Service problems


## PAN-OS Policy Optimizer (Beta)

**Type:** integration  
**Product:** PAN-OS Policy Optimizer (beta)  

Automate your AppID Adoption by using this integration together with your Palo Alto Networks Next-Generation Firewall or Panorama. This integration was integrated and tested with version 8 up to version 10.1.6 and version 10.2.0 of PAN-OS Policy Optimizer. Moved to beta due to the lack of a formal API

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## PAN-OS Query Logs For Indicators

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

Queries the following PAN-OS log types: traffic, threat, URL, data-filtering and wildfire. The playbook accepts inputs such as IP addresses, hash, and URL

**Inputs:**

- `url`: The URL. For example, "safebrowsing.googleapis.com".
- `filedigest`: The file hash (for WildFire logs only).
- `ip`: The source or destination address.


## PAN-OS Search for Post Quantum Crypto Vuln Sigs

**Type:** playbook  
**Product:** Post Quantum Crypto Hunting by Palo Alto Networks  

Search Vuln Sigs in Threat Logs for use of Post Quantum Crypto Signatures

**Inputs:**

- `notify_email`: Send email notification for new malware
- `log_source`: where should we poll for Log Events to investigatepanoscdlsiem
- `threat_ids`: threat ID to search for as CSV list
- `time_range_hours`: how many hours back to query for events in hours
- `num_logs`: how many logs to bring back


## PAN-OS to Strata Logging Service Monitoring - Cron Job

**Type:** playbook  
**Product:** PAN-OS to Strata Logging Service Monitoring  

This playbook verifies that your FWs sent logs to the Strata Logging Service in the last 12 hours. An email notification will be sent if it's not the case. This playbook is designed to run as a job

**Inputs:**

- `fw_serials`: A comma-separated list of FW serials to monitor. Only applicable if no Panorama integration specified.
- `panorama_integration`: Name of the Panorama integration to gather the list of monitored FWs. If none specified, the list of serials must be provided manually as "f
- `email_notification`: Email address to send a notification to in case detected problem.


## PAN-OS-AnalyzeRuleHitCounts

**Type:** script  
**Product:** PAN-OS by Palo Alto Networks  

Processes the context output from !pan-os-get-rulehitcounts and returns data about unused local rules, unused rules from Panorama, and rules from Panorama that have hits on some firewalls but not all


## PAN-OS-GetAvailablePANOSSoftware

**Type:** script  
**Product:** PAN-OS by Palo Alto Networks  

This script is a wrapper for the 'pano-os-platform-get-available-software' command, adding options to return only images newer than is currently installed to minimize amount of context data generated

**Inputs:**

- `device_filter_string`: The string by which to filter the results to only show specific hostnames or serial numbers.
- `target`: The target number of the firewall. Used only on a Panorama instance.
- `panos_instance_name`: The instance name of the PAN-OS Integration to use. Specify only one instance.
- `newer_images_only`: Whether to return only images newer than currently installed.


## PAN-OS-GetDeviceDiskSpace

**Type:** script  
**Product:** PAN-OS by Palo Alto Networks  

This script fetches disk space info from the target device and returns all information or a subset as specified in command arguments

**Inputs:**

- `target`: The serial number of the device to get disk space info from.
- `panos_instance_name`: The instance name of the PAN-OS Integration to use. Specify only one instance.
- `disk_space_units`: 


## PAN-OS_Security_Advisories_Enrichment

**Type:** script  
**Product:** PAN-OS by Palo Alto Networks  

This script enriches CVEs published by Palo Alto Networks with detailed vulnerability information from the official Palo Alto Networks Security Advisories website

**Inputs:**

- `cve_id`: CVE ID(s) or PAN-SA advisory ID(s) to enrich (array)


## Panorama Query Logs

**Type:** playbook  
**Product:** PAN-OS by Palo Alto Networks  

Queries Panorama Logs of types: traffic, threat, URL, data-filtering and WildFire

**Inputs:**

- `log_type`: The log type to query. Can be, "traffic", "threat", "wildfire", "url" or "data-filtering".
- `query`: The query string by which to match the criteria for the logs. This is similar to the query provided in the web interface under the Monitor t
- `time-generated`: The time the log was generated from the timestamp and prior to it. For example, "2019/08/11 01:10:44".
- `addr-src`: The source address.
- `addr-dst`: The destination address.
- `ip`: The source or destination IP address.
- `zone-src`: The source zone.
- `zone-dst`: The destination zone.


## PanoramaCVECoverage

**Type:** script  
**Product:** PAN-OS by Palo Alto Networks  

Check coverage given a list of CVEs

**Inputs:**

- `CVE_List`: A comma-separated list of CVEs to find.
- `Result_file`: Entry ID of the output file from the panorama command.
- `outputFormat`: Raw output of the panorama command into a file.


## PanoramaSecurityPolicyMatchWrapper

**Type:** script  
**Product:** PAN-OS by Palo Alto Networks  

A wrapper script for the panorama-security-policy-match command that receives multiple values for the source, destination, and destination port arguments and performs the policy match for each combination of the inputs

**Inputs:**

- `application`: The application name.
- `category`: The category name.
- `destination`: A comma-separated list of destination IP addresses.
- `from`: The from zone.
- `to`: The to zone.
- `protocol`: The IP protocol value.
- `source`: A comma-separated list of source IP addresses.
- `target`: Target number of the firewall. Use only on a Panorama instance.


## PANW Device Security Incident Handling with ServiceNow

**Type:** playbook  
**Product:** Device Security by Palo Alto Networks  

This playbook creates a ServiceNow ticket after the incident is enriched by Palo Alto Networks Device Security portal (previously Zingbox Cloud)

**Inputs:**

- `DeviceSecurityConfigListName`: The list name defined in the the platform Lists for the RACI and ServiceNow calculation.
- `CreateServiceNowTicket`: Determines if a ServiceNow ticket should be created based on the RACI calculation. Set to True to create an incident.


## PANW IoT Incident Handling with ServiceNow

**Type:** playbook  
**Product:** IoT by Palo Alto Networks  

This playbook creates a ServiceNow ticket after the incident is enriched by Palo Alto Networks IoT security portal (previously Zingbox Cloud)

**Inputs:**

- `IoTConfigListName`: The list name defined in the the platform Lists for the RACI and ServiceNow calculation.
- `CreateServiceNowTicket`: Determines if a ServiceNow ticket should be created based on the RACI calculation. Set to True to create an incident.


## PanwIndicatorCreateQueries

**Type:** script  
**Product:** Comprehensive Investigation by Palo Alto Networks  

The script accepts indicators as input and creates an indicator query in the relevant Palo Alto Networks products

**Inputs:**

- `ip`: A commma-separated list of IP addresses for which to create the query.
- `hash`: A commma-separated list of file hashes for which to create the query.
- `domain`: A commma-separated list of domains for which to create the query.


## Policy Optimizer - Add Applications to Policy Rules

**Type:** playbook  
**Product:** PAN-OS Policy Optimizer (beta)  

This playbook edits rules with unused applications or rules that are port based, and adds an application to the rule. It is used in PAN-OS - Policy Optimizer playbooks and includes communication tasks to get a rule name and the application to edit from the user

**Inputs:**

- `rules_list`: PAN-OS rules to edit using the playbook.


## Policy Optimizer - Generic

**Type:** playbook  
**Product:** PAN-OS Policy Optimizer (beta)  

This playbook is triggered by the Policy Optimizer incident type, and can execute any of the following sub-playbooks

**Inputs:**

- `slack_user`: Slack user to notify about unused rules.
- `email_address`: User email address to notify about unused rules.
- `auto_commit`: Specifies whether you want to auto-commit the configuration for the PAN-OS policy changes automatically (Yes/No).


## Policy Optimizer - Manage Port Based Rules

**Type:** playbook  
**Product:** PAN-OS Policy Optimizer (beta)  

This playbook migrates port-based rules to application-based allow rules to reduce the attack surface and safely enable applications on your network

**Inputs:**

- `slack_user`: Slack user to notify about port based rules.
- `email_address`: User email address to notify about port based rules.
- `auto_commit`: Specifies whether you want to auto-commit the configuration for the PAN-OS policy changes automatically (Yes/No).


## Policy Optimizer - Manage Rules with Unused Applications

**Type:** playbook  
**Product:** PAN-OS Policy Optimizer (beta)  

This playbook helps identify and remove unused applications from security policy rules. If you have application-based security policy rules that allow a large number of applications, you can remove unused applications (applications never seen on the rules) from those rules to allow only applications actually seen in the rule’s traffic. This strengthens your security posture by reducing the attack surface

**Inputs:**

- `slack_user`: Slack user to notify about port based rules.
- `email_address`: User email address to notify about port based rules.
- `auto_commit`: Specifies whether you want to auto-commit the configuration for the PAN-OS policy changes automatically (Yes/No).


## Policy Optimizer - Manage Unused Rules

**Type:** playbook  
**Product:** PAN-OS Policy Optimizer (beta)  

This playbook helps identify and remove unused rules that do not pass traffic in your environment

**Inputs:**

- `slack_user`: Slack user to notify about unused rules.
- `email_address`: User email address user to notify about unused rules.
- `auto_commit`: Specifies whether you want to auto-commit the configuration for the PAN-OS policy changes automatically (Yes/No).


## Query Cisco Stealthwatch Flows

**Type:** playbook  
**Product:** Cisco Secure Network Analytics (Stealthwatch)  

This playbook runs a query on Cisco Stealthwatch flows and return its results to the context

**Inputs:**

- `timeout`: The amount to wait before a timeout occurs (in minutes).
- `interval`: Polling frequency - how often the polling command should run (in minutes).
- `range`: Range of results to return (e.g., 0-20).
- `tenant_id`: Tenant ID represents the domain on Cisco Stealthwatch.
- `time_range`: 


## SaaS Security

**Type:** integration  
**Product:** SaaS Security by Palo Alto Networks  

Use the SaaS Security integration to protect against cloud‑based threats by

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Saas Security - Incident Processor

**Type:** playbook  
**Product:** SaaS Security by Palo Alto Networks  

This playbook notifies incidents owner and provides remediation options to Saas Security admin for resolving incidents

**Inputs:**

- `tenant_admin`: This is the tenant admin email.


## Saas Security - Take Action on the Incident

**Type:** playbook  
**Product:** SaaS Security by Palo Alto Networks  

This sub-playbook will send email notification to the Saas Security Admin for taking remediation action on the incident

**Inputs:**

- `email`: Admin Email
- `incident_id`: Prisma Saas Incident Id
- `asset_id`: Prisma Saas Asset Id
- `asset_name`: Prisma Saas Asset Name


## Sophos Firewall

**Type:** integration  
**Product:** Sophos XG Firewall  

On-Premise firewall by Sophos enables you to manage your firewall, respond to threats, and monitor what’s happening on your network

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Strata Logging Service the platform Connector

**Type:** integration  
**Product:** Strata Logging Service by Palo Alto Networks  
**Commands:**

- `None`: 


## Sync Threat Intel to Destination Profile - Netskope

**Type:** playbook  
**Product:** Netskope - Direct to Zero Trust  

Synchronizes bounded the platform. The profile name is required. Match type and indicator types have editable playbook defaults, and each input is validated independently before any Netskope command runs. Existing profiles are updated in batches of at most 10 values. New profiles are created as pending changes. Set Deploy to true to apply pending changes; it defaults to false so scheduled jobs cannot enforce changes without explicit authorization. The default indicator query selects active indicators with a Bad reputation and can be further restricted with tags

**Inputs:**

- `ProfileName`: Name of the Netskope Destination Profile to sync indicators into. No tenant-specific fallback is used.
- `MatchType`: Match type to use only when creating a profile. One of sensitive, insensitive, or regex. Defaults to regex.
- `IndicatorTypes`: Comma-separated the platform. One or more of Domain, URL, IP, and CIDR.
- `Tags`: Optional comma-separated indicator tags to further restrict which indicators are pulled (e.g. "netskope-block"). Leave empty to consider all
- `SkipTags`: Optional comma-separated indicator tags to exclude - any indicator carrying one of these tags is skipped even if it matches Tags. Leave empt
- `MaxIndicators`: Maximum number of indicators to pull from the platform. Bounds how much work a single scheduled run does.
- `IndicatorQuery`: Additional the platform. The default limits synchronization to active indicators with a Bad reputation.
- `Deploy`: Whether to deploy pending Destination Profile changes. Defaults to false.


## Threat Inspection - Netskope

**Type:** playbook  
**Product:** Netskope - Direct to Zero Trust  

Submits a file for Netskope's sandbox scan (netskopev2-submit-file-scan / netskopev2-get-scan-report) and polls for the result, since the scan is asynchronous and can take a while to complete. Only certain file types are accepted for inspection - this is enforced by netskopev2-submit-file-scan itself (not just this playbook), per the API spec: the file must be a password-protected .zip whose one member file is .exe, .pdf, .doc, .xls, .ppt, or .rtf. A plain .zip (the container format) is also accepted directly. Anything else is rejected with a clear error before an API call is even made. Checks whether the EntryID input was provided, checks whether a Netskope integration instance is enabled (matching any brand name containing "Netskope"), submits the file for scanning, then uses the standard GenericPolling sub-playbook to repeatedly call netskopev2-get-scan-report (every Interval minutes, up to Timeout minutes) until the scan's status stops being "InProgress". The final poll's result is what's left in the Netskope.FileScanReport context when this playbook finishes - no separate "final fetch" step is needed

**Inputs:**

- `EntryID`: Entry ID of the file to submit for sandbox scanning. Defaults to ${File.EntryID} - the file already attached to the incident (via the War Ro
- `Interval`: Minutes between each poll of the scan status.
- `Timeout`: Maximum minutes to keep polling before giving up and resuming the playbook (sandbox scans can take a while).


## URL Lookup - Netskope

**Type:** playbook  
**Product:** Netskope - Direct to Zero Trust  

Looks up a URL's categorization/reputation info via netskopev2-url-lookup and records the result as labels directly on the incident. netskopev2-url-lookup is a bulk API (up to 100 URLs per call), but this playbook only ever queries one URL at a time, matching the single URL input. Building the addLabels JSON string from the lookup result requires joining nested category/URL-list names into flat values, which isn't reliably expressible in plain playbook YAML templating (see NetskopeURLLookupLabels for why) - that script does the real work; this playbook just wires it together. netskopev2-url-lookup is a licensed feature on the Netskope side - if you get an error mentioning licensing/enablement, URL Lookup needs to be enabled for your tenant by Netskope support

**Inputs:**

- `URL`: The URL to look up.


## WildFire - Detonate file

**Type:** playbook  
**Product:** WildFire by Palo Alto Networks  

Detonate one or more files using the Wildfire integration. This playbook returns relevant reports to the War Room and file reputations to the context data. The detonation supports the following file types - APK, JAR, DOC, DOCX, RTF, XLS, XLSX, PPT, PPTX, OOXML, PE32, PE, PDF, DMG, PKG, RAR, 7Z, JS, ELF, HTA, LNK, VBS, PS1, PERL, PYTHON, SHELL. Note: Base64 encoded files are currently not supported This playbook is deprecated. please use the WildFire - Detonate file v2 instead

**Inputs:**

- `File`: File object of the file to detonate. The file is taken from the context.
- `Interval`: The duration for executing the polling (in minutes).
- `Timeout`: The duration after which to stop polling and to resume the playbook. (in minutes)
- `ReportFileType`: The resource type to download.


## WildFire - Detonate file v2

**Type:** playbook  
**Product:** WildFire by Palo Alto Networks  

Detonate one or more files using the Wildfire v2 integration. This playbook returns relevant reports to the War Room and file reputations to the context data. The detonation supports the following file types - APK, JAR, DOC, DOCX, RTF, XLS, XLSX, PPT, PPTX, OOXML, PE32, PE, PDF, DMG, PKG, RAR, 7Z, JS, ELF, HTA, LNK, VBS, PS1, PERL, PYTHON, SHELL, SWF, DEX, BAT, BZ, CSV, GZ, ISO, CLASS, JSE, WSF, JPG, MACHO, ZBUNDLE, FAT, ONE, SLK, IQY, ODS, ODT, PL, PNG, PY, TAR, VBE, ASP, ASPX, XML, HTML, EML, CMD, CHM, ZIP. Note: Base64 encoded files are currently not supported

**Inputs:**

- `File`: File object of the file to detonate. The file is taken from the context.
- `Interval`: The duration for executing the polling (in seconds).
- `Timeout`: The duration after which to stop polling and to resume the playbook. (in seconds)
- `ReportFileType`: The resource type to download.


## XCloudRegionsPieWidget

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

XCLOUD dynamic section, showing the top ten regions types in a pie chart


## XCloudResourcesPieWidget

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

XCLOUD dynamic section, showing the top ten resource types in a pie chart


## XDRConnectedEndpoints

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

The widget returns the number of the connected endpoints using xdr-get-endpoints command

**Inputs:**

- `from`: The start date by which to filter incidents. Date format will be the same as in the incidents query page, for example: "3 days ago", "2019-0
- `to`: The end date by which to filter incidents. Date format will be the same as in the incidents query page, for example: "3 days ago", "2019-01-
- `limit`: The maximum number of incidents to fetch. The default value is 100.


## XDRDisconnectedEndpoints

**Type:** script  
**Product:** Cortex XDR by Palo Alto Networks  

The widget returns the number of the disconnected endpoints using xdr-get-endpoints command

**Inputs:**

- `from`: The start date by which to filter incidents. Date format will be the same as in the incidents query page, for example: "3 days ago", "2019-0
- `to`: The end date by which to filter incidents. Date format will be the same as in the incidents query page, for example: "3 days ago", "2019-01-
- `limit`: The maximum number of incidents to fetch. The default value is 100.


## Zero Networks Segment

**Type:** integration  
**Product:** Zero Networks Segment  

This is the Zero Networks event collector integration for Cortex XSIAM

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## Zscaler Internet Access

**Type:** integration  
**Product:** Zscaler Internet Access  

Zscaler is a cloud security solution built for performance and flexible scalability. This integration enables you to manage URL and IP address allow lists and block lists, manage and update categories, get Sandbox reports, create, manage, and update IP destination groups and manually log in, log out, and activate changes in a Zscaler session. For the integration to work properly, the Zscaler user must have admin permissions. Category ID is the same as the category name, except all letters are capitalized and each word is separated with an underscore instead of spaces. For example, if the category name is Other Education, then the Category ID is OTHER_EDUCATION. A custom category ID has the format CUSTOM_01, which is not indicative of the category. Use the zscaler-get-categories command to get a custom category and its configured name

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Zscaler Internet Access via ZIdentity

**Type:** integration  
**Product:** Zscaler Internet Access  

This integration uses ZIdentity OAuth 2.0 client credentials to authenticate with Zscaler Internet Access (ZIA). It enables the management of denylists, allowlists, URL categories, IP destination groups, and users/groups, while also providing URL, IP, and domain classifications and sandbox reporting

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 

