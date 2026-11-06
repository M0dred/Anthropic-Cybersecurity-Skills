# Integration and Automation Catalog - Threat Hunting

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## AppSentinels.ai

**Type:** integration  
**Product:** AppSentinels.ai  

Appsentinels.ai offers a platform for collecting, analyzing, and managing security events to provide comprehensive application protection. This is the default integration for this content pack when configured by the Data Onboarder in Cortex XSIAM

**Commands:**

- `None`: 


## Elasticsearch v2

**Type:** integration  
**Product:** Elasticsearch  

Elasticsearch_v2 integration is used to search for and analyze data in real time. Supports version 6 and later. This integration was integrated and tested with versions 6.6.2, 7.3, 8.4.1 of Elasticsearch

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


## FortiSIEM v2

**Type:** integration  
**Product:** FortiSIEM  

Use FortiSIEM v2 to fetch and update incidents, search events and manage FortiSIEM watchlists. This integration was integrated and tested with FortiSIEMV2 version 6.3.2. Changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

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


## ForwardAuditLogsToSplunkHEC

**Type:** script  
**Product:** Forward the platform Audit Logs to Splunk HEC  

This Automation script uses the the platform API to get the audit logs and pushes them to Splunk HEC. Dependencies: SlunkPy and Core REST API integrations

**Inputs:**

- `timeframe`: timeframe to fetch in hours


## FullHunt

**Type:** integration  
**Product:** FullHunt  

FullHunt is the attack surface database of the entire Internet. FullHunt enables companies to discover all of their attack surfaces, monitor them for exposure, and continuously scan them for the latest security vulnerabilities. All, in a single platform, and more

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## GaiatopForwardAuditLogsToSplunkHEC

**Type:** script  
**Product:** ForwardAuditLogsToSplunkHEC  

This automation fetches the Management Audit Logs and forwards it to be Splunk HEC

**Inputs:**

- `AuditLogCountList`: 
- `CoreRestInstanceName`: 
- `SplunkInstanceName`: 


## GrrGetHunt

**Type:** script  
**Product:** GRR  

Renders the hunts summary

**Inputs:**

- `hunt_id`: The hunt ID.


## GrrGetHunts

**Type:** script  
**Product:** GRR  

Renders the list of available hunts

**Inputs:**

- `offset`: The starting offset.
- `count`: The maximum number of items to fetch.
- `created_by`: Returns hunts created by a given user. If approved_by or/and description_contains are also supplied, then logical AND is applied to all the 
- `description_contains`: Returns hunts where the description contains a given substring (matching is case-insensitive).If created_by or/and approved_by are also supp
- `active_within`: Returns hunts that were active within given time duration.


## GrrSetHunts

**Type:** script  
**Product:** GRR  

Handles hunt creation requests

**Inputs:**

- `hunt_runner_args`: The hunt runner arguments.
- `hunt_args`: The hunt arguments.


## Hoxhunt v2

**Type:** integration  
**Product:** Hoxhunt  

Use the Hoxhunt integration to send feedback to reporters of incidents, set incident sensitivity, and apply SOC classification to incidents. This integration was integrated and tested with version August 2024 of Hoxhunt

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


## IBM QRadar v3

**Type:** integration  
**Product:** IBM QRadar  

IBM QRadar SIEM helps security teams accurately detect and prioritize threats across the enterprise, supports API versions 10.1 and above. Provides intelligent insights that enable teams to respond quickly to reduce the impact of incidents. This integration was integrated and tested with version 14-20 of QRadar v3

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


## IBM Security QRadar SOAR

**Type:** integration  
**Product:** IBM Security QRadar SOAR  

Case management that enables visibility across your tools for continual IR improvement

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


## IbmAddNote

**Type:** script  
**Product:** IBM Security QRadar SOAR  

Use this script to add a note with a tag (the "Note tag to IBM" defined in the instance configuration) as an entry in the platform, which will then be mirrored as a note to a IBM QRadar SOAR incident. This script should be run within an incident

**Inputs:**

- `note`: Note to be added to the IBM QRadar SOAR incident.
- `tags`: The note tag. Use the note entry tag (defined in your instance configuration) to mirror the note to IBM QRadar SOAR.


## IbmAddTask

**Type:** script  
**Product:** IBM Security QRadar SOAR  

Use this script to add a task to an IBM QRadar SOAR incident

**Inputs:**

- `name`: Task name.
- `description`: Task description.
- `instructions`: Textual instructions for the task. This will override the default instructions for the task.
- `due_date`: Task due date in ISO format e.g., "2020-02-02T19:00:00Z. Empty date indicates that the task has no assigned due date.
- `owner_id`: The owner of the task (ID or name as appears in IBM QRadar SOAR). Leave empty if the task has no owner.
- `phase`: Task to be added to the IBM QRadar incident.


## IbmConvertArtifactsToTable

**Type:** script  
**Product:** IBM Security QRadar SOAR  

This script is used to format IBM QRadar SOAR artifacts into a mark-down table


## IbmConvertAttachmentsToTable

**Type:** script  
**Product:** IBM Security QRadar SOAR  

This script is used to format IBM QRadar SOAR attachments into a mark-down table


## IbmConvertCommentsToTable

**Type:** script  
**Product:** IBM Security QRadar SOAR  

This script is used to format IBM QRadar SOAR notes into a mark-down table


## IbmConvertTasksToTable

**Type:** script  
**Product:** IBM Security QRadar SOAR  

This script is used to format IBM QRadar SOAR tasks into a markdown table


## IbmUpdateNote

**Type:** script  
**Product:** IBM Security QRadar SOAR  

Use this script to update a note in an IBM QRadar SOAR incident. This script should be run within an incident

**Inputs:**

- `note_id`: ID of the note to be updated.
- `note_body`: Note body.
- `tags`: The note tag. Use the note entry tag (defined in your instance configuration) to mirror the note to IBM QRadar SOAR.


## IbmUpdateTask

**Type:** script  
**Product:** IBM Security QRadar SOAR  

Use this script to update an IBM QRadar SOAR incident's task. This script should be run within an incident

**Inputs:**

- `task_id`: ID of task to update.
- `name`: Task name. Technically required, copy original task name if no changes are desired.
- `owner_id`: User ID of the new owner.
- `due_date`: Task due date in ISO format e.g. "2020-02-02T19:00:00Z. Empty date indicates that the task has no assigned due date.
- `phase`: The phase to which this task belongs.
- `status`: Changing the status field, completes or re-openes the task.


## IbmUploadAttachment

**Type:** script  
**Product:** IBM Security QRadar SOAR  

Use this script to upload an attachment to an IBM QRadar SOAR incident. This script should be run within an incident

**Inputs:**

- `entry_id`: EntryID of the file to upload.


## LogPoint SIEM Integration

**Type:** integration  
**Product:** LogPoint SIEM Integration  

Use this Content Pack to search logs, fetch incident logs from LogPoint, analyze them for underlying threats, and respond to these threats in real-time. This integration was integrated and tested with version 6.7.4 of LogPoint

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


## LogPoint SIEM Playbook

**Type:** playbook  
**Product:** LogPoint SIEM Integration  

LogPoint SIEM Playbook guides users on use cases like blocking IP and domain and disabling users using products like CheckPoint Firewall, Active Directory, and VirusTotal. The actions depicted in the playbook helps analysts create their playbooks based on actual requirements and products deployed. (Available from the platform.0.0)


## LogsignSiem

**Type:** integration  
**Product:** Logsign SIEM  

Logsign SIEM provides comprehensive visibility and control of your data lake by allowing security analysts to collect and store unlimited data, investigate and detect threats, and respond automatically. This integration was integrated and tested with version 4.6.x of Logsign SIEM

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Microsoft Sentinel

**Type:** integration  
**Product:** Microsoft Sentinel  

Use the Azure Sentinel integration to get and manage incidents and get related entity information for incidents. This integration was integrated and tested with version 2021-04-01 of Azure Sentinel

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


## MicrosoftSentinelConvertAlertsToTable

**Type:** script  
**Product:** Microsoft Sentinel  

This script is used to convert alerts to a table


## MicrosoftSentinelConvertCommentsToTable

**Type:** script  
**Product:** Microsoft Sentinel  

This script is used to convert comments to a table


## MicrosoftSentinelConvertEntitiesToTable

**Type:** script  
**Product:** Microsoft Sentinel  

This script is used to convert entities to a table


## MicrosoftSentinelConvertRelationsToTable

**Type:** script  
**Product:** Microsoft Sentinel  

This script is used to convert relations to a table


## MicrosoftSentinelSetOwner

**Type:** script  
**Product:** Microsoft Sentinel  

This script can be run from the War Room or used by a layout to set the Owner field in Microsoft Sentinel. Note: The Owner field in the platform

**Inputs:**

- `owner_email`: The owner email to set as the user principal name. If there is a user in Microsoft Sentinel for this email, they will be represented by thei
- `incident_id`: The ID of the remote incident to update. Relevant only when the script is called directly from the War Room.


## MicrosoftSentinelSubmitNewComment

**Type:** script  
**Product:** Microsoft Sentinel  

Use this script to add a comment which will then be mirrored as a comment to a Sentinal event. This script should be run within an incident. Note: Comments in the platform

**Inputs:**

- `new_comment`: The comment text to be added to the incident comments.
- `incident_id`: The ID of the incident to add the comment to. This argument is relevant only when the script is called directly from the War Room.


## QRadar - Get Offense Logs

**Type:** playbook  
**Product:** IBM QRadar  

Works for QRadar integration version 3, v1 and v2 are deprecated. Note: You can use the integration to fetch the events with the offense however it will fetch the events according to the specified limit defined in the instance settings. By using this playbook you can define an additional search to query a larger number of logs. Default playbook inputs use the QRadar incident fields such as idoffense, starttime. These fields can be replaced but need to point to relevant offense ID and starttime fields

**Inputs:**

- `MaxLogsCount`: Maximum number of log entires to query from QRadar (default: 50)
- `ID`: The QRadar offense ID. Uses the id offense incident field.
- `StartTime`: The QRadar offense start time
- `GetOnlyCREEvents`: If value "OnlyCRE" get only events made by CRE.Values can be "OnlyCRE", "OnlyNotCRE", "All".
- `Fields`: A comma-separated list of extra fields to get from each event.You can replace with different fields as well as rename the field names.
- `ApiVersion`: The API version for the timestamp format changes between versions


## QRadar Build Query and Search

**Type:** playbook  
**Product:** IBM QRadar  

The QRadar Build Query and Search playbook creates an AQL query for the QRadar SIEM using the QRadarCreateAQLQuery automation queries. Complex queries take into consideration several inputs and allow including or excluding each of the values as well as performing a full or partial search. Each of the values can be searched across several fields. The playbook supports 3 separate conditions to be evaluated. For example, in the first condition, inputs will evaluate several user names that may or may not exist in several fields. The second input, can for example, evaluate for IP addresses in several fields that may or may not exist in several fields, and a third value can search for an event ID that may or may not exist in several fields. The results of all of the inputs will create an AQL query that covers all of the inputs combining all of the different conditions. Each of the inputs is validated so in case the inputs are not set correctly, the user can review and run them again. Also, populated inputs will be combined, meaning by populating the first and second values the resulting AQL query will be a combination of all of the values and not 3 separate searches. In addition, make sure to populate the inputs in order according to the indexed fields in QRadar (indexed fields should be provided before non indexed ones)

**Inputs:**

- `BaseValuesToSearch`: The values of the first field to search. This can be a single value or a comma-separated list of values. For example, admin1,admin2
- `BaseFieldsToSearch`: The field names of the first field to search. This can be a single value or a comma-separated list of values. For example, username,user
- `BaseFieldState`: The state of the first field to search, meaning whether the values in the field be included or excluded. Valid options are include or exclud
- `BaseFieldMatch`: Whether the values of the first field should be an exact match or a partial match. Valid options are exact or partial. When choosing exact, 
- `FirstAdditionalValues`: The values of the second field to search. This can be a single value or a comma-separated list of values. For example admin1,admin2
- `FirstAdditionalFields`: The field names of the second field to search. This can be a single value or a comma-separated list of values. For example admin1,admin2
- `FirstAdditionalFieldState`: The state of the second field to search, meaning whether the values in the field should be included or excluded. Valid options are include o
- `FirstAdditionalFieldMatch`: Whether the values of the second field should be an exact match or a partial match. Valid options are exact or partial.


## QRadar Generic

**Type:** playbook  
**Product:** IBM QRadar  

The QRadar Generic playbook is executed for the QRadar Generic incident type. It performs all the common parts of the investigation, including notifying the SOC, enriching data for indicators and users, calculating severity, assigning incidents, and notifying the SIEM admin about false positives

**Inputs:**

- `Enrich`: Determines whether to enrich all indicators in the incident.
- `OnCall`: Set to true to assign only the user that is currently on shift. Requires the platform.5 or later.
- `SocEmailAddress`: The SOC team's email address.
- `SocMailSubject`: The subject of the email to send to the SOC.
- `SiemAdminEmailAddress`: The SIEM admin's email address.
- `UseCalculateSeverity`: Determines whether to use the Calculate Severity playbook to calculate the incident severity. If the playbook isn't used, the severity is de
- `SiemAdminMailSubject`: The subject of the email to send to the SIEM admin.
- `UseCustomSeveritySettings`: Determines whether to use the default mapping in the QRadar generic mapper to set the the platform incident severity, or set the severity us


## QRadarCreateAQLQuery

**Type:** script  
**Product:** IBM QRadar  

Build QRadar AQL Query. (Available from the platform.0.0)

**Inputs:**

- `base_values_to_search`: The values of the first field to search. This can be a single value or a comma-separated list of values. For example admin1,admin2.
- `base_fields_to_search`: The field names of the first field to search. This can be a single value or a comma-separated list of values. For example admin1,admin2.
- `base_field_state`: The state of the second field to search, meaning whether the values in the field should be included or excluded. Valid options are include o
- `base_field_match`: Whether the values of the second field should be an exact match or a partial match. Valid options are exact or partial.
- `select_fields`: The list of fields to select within the AQL query. The default fields are DATEFORMAT(devicetime,'dd-MM-yyyy hh:mm'),LOGSOURCENAME(logsourcei
- `time_frame`: Time frame as used in AQL examples can be LAST 7 DAYS START '2019-09-25 15:51' STOP '2019-09-25 17:51'. For more examples, view IBM's AQL do
- `first_additional_values`: The values of the second field to search. This can be a single value or a comma-separated list of values. For example admin1,admin2.
- `first_additional_fields`: The field names of the second field to search. This can be a single value or a comma-separated list of values. For example admin1,admin2.


## QRadarFetchedEventsSum

**Type:** script  
**Product:** IBM QRadar  

This script displays the amount of fetched events vs the total number of events in the offense


## QRadarMagnitude

**Type:** script  
**Product:** IBM QRadar  

This script applies colors to the field according to the magnitude based on the following scale: 1-3 green 4-7 yellow 8-10 red


## QRadarMirroringEventsStatus

**Type:** script  
**Product:** IBM QRadar  

This script displays the the mirroring events status in the offense


## QRadarPrintAssets

**Type:** script  
**Product:** IBM QRadar  

This script prints the assets fetched from the offense in a table format


## QRadarPrintEvents

**Type:** script  
**Product:** IBM QRadar  

This script prints the events fetched from the offense in a table format


## RapidBreachResponse-HuntingTasksCount-Widget

**Type:** script  
**Product:** Rapid Breach Response  

Rapid Breach Response dynamic section, will show the updated number of hunting tasks


## Splunk Generic

**Type:** playbook  
**Product:** Splunk  

This is a generic playbook to be executed for the Splunk Notable Generic incident type. The playbook performs all the common parts of the investigation, including notifying the SOC, enriching the data for indicators and users, calculating the severity, assigning the incident, notifying the SIEM admin for false positives and more

**Inputs:**

- `Enrich`: Determines whether to enrich all indicators in the incident. Default is True.
- `OnCall`: Set to true to assign only the user that is currently on shift. Default is False. Requires the platform.5 or later.
- `SocEmailAddress`: The SOC team's email address.
- `SocMailSubject`: The subject of the email to send to the SOC.
- `SiemAdminEmailAddress`: The SIEM admin's email address.
- `UseCalculateSeverity`: Determines whether to use the Calculate Severity playbook to calculate the incident severity. Default is True. If the playbook isn't used, t
- `SiemAdminMailSubject`: The subject of the email to send to the SIEM admin.


## Splunk_ShortID

**Type:** script  
**Product:** SplunkScripts  

Create Splunk Notable Event Short ID

**Inputs:**

- `event_id`: Splunk notable event id.


## SplunkAddComment

**Type:** script  
**Product:** Splunk  

Use this script to add a comment with a tag (the "Comment tag to Splunk" defined in the instance configuration) as an entry in the platform, which will then be mirrored as a comment to a Splunk issue. This script should be run within an incident

**Inputs:**

- `comment`: Comment to be added to the Splunk issue.
- `tag`: The comment tag. Use the comment entry tag (defined in your instance configuration) to mirror the comment to splunk.


## SplunkAddNote

**Type:** script  
**Product:** Splunk  

Use this script to add a note with a tag (the "Note tag to Splunk" defined in the instance configuration) as an entry in the platform, which will then be mirrored as a note to a Splunk finding. This script should be run within an incident

**Inputs:**

- `note`: Note to be added to the Splunk finding.
- `tag`: The note tag. Use the note entry tag (defined in your instance configuration) to mirror the note to splunk.


## SplunkCIMFields

**Type:** script  
**Product:** SplunkScripts  

Convert Splunk CIM Fields Dynamic Into Fields Value

**Inputs:**

- `value`: Input string from incident.
- `inc`: Incident field values from incident.


## SplunkConvertCommentsToTable

**Type:** script  
**Product:** Splunk  

This script is used to convert Splunk comments to a table


## SplunkConvertConsolidatedFindingsToMD

**Type:** script  
**Product:** Splunk  

Renders the Splunk Investigation consolidated_findings JSON payload as a Markdown summary (key/value table for scalar fields plus a transposed table for parallel array columns such as search_name, _time, dest, risk_score, severity, and src). Designed for use as a dynamic-section in the Splunk Investigation layout


## SplunkConvertNotesToTable

**Type:** script  
**Product:** Splunk  

This script converts Splunk notes into a table.```


## SplunkPy

**Type:** integration  
**Product:** Splunk  

Use the SplunkPy integration to: This integration was integrated and tested with Splunk Enterprise v9.4.3 and Enterprise Security v8.1.0

**Commands:**

- `None`: 


## SplunkPy v2

**Type:** integration  
**Product:** Splunk  

Use the SplunkPy v2 integration to: Important: This integration is designed specifically for Splunk Enterprise Security version 8.2 and above. For Splunk ES versions prior to 8.2, please use the legacy SplunkPy integration. This integration was integrated and tested with Splunk Enterprise v10.0.0 and Enterprise Security v8.2.3

**Commands:**

- `None`: 


## SplunkShowAsset

**Type:** script  
**Product:** Splunk  

Automation to display asset objects from Splunk


## SplunkShowDrilldown

**Type:** script  
**Product:** Splunk  

Automation to display drilldown search results from Splunk


## SplunkShowIdentity

**Type:** script  
**Product:** Splunk  

Automation to display identity objects from Splunk

