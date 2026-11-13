# Integration and Automation Catalog - Threat Hunting

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## AppSentinels.ai

**Type:** integration  
**Product:** AppSentinels.ai  

Appsentinels.ai offers a platform for collecting, analyzing, and managing security events to provide comprehensive application protection. This is the default integration for this content pack when configured by the Data Onboarder in Cortex XSIAM

**Commands:**

- `appsentinels-get-events`: Retrieves a list of events from the AppSentinels.ai instance.


## Elasticsearch v2

**Type:** integration  
**Product:** Elasticsearch  

Elasticsearch_v2 integration is used to search for and analyze data in real time. Supports version 6 and later. This integration was integrated and tested with versions 6.6.2, 7.3, 8.4.1 of Elasticsearch

**Commands:**

- `es-search`: Queries an index.
- `search`: Searches an index.
- `get-mapping-fields`: Returns the schema of the index to fetch from. This commmand should be used for debugging purposes.
- `es-eql-search`: Search using EQL query
- `es-index`: Indexes a document into an Elasticsearch index.
- `es-integration-health-check`: Returns the health status of the integration. This commmand should be used for debugging purposes.
- `es-get-indices-statistics`: Returns Elasticsearch indices statistics and information. This command is not supported for client type OpenSearch.
- `es-esql-search`: Search using ES|QL query (Elasticsearch 8.11 and above).
- `es-kibana-alerting-health-get`: Retrieves the health of the Kibana alerting framework.
- `es-kibana-rule-types-list`: Retrieves all rule types available in Kibana.
- `es-kibana-rule-list`: Retrieves information about rules.
- `es-kibana-rule-enable`: Enable a rule.
- `es-kibana-rule-disable`: Disable a rule.
- `es-kibana-rule-update`: Update a rule.
- `es-kibana-rule-alert-mute`: Mute an alert, or mute all alerts for a rule.


## FortiSIEM v2

**Type:** integration  
**Product:** FortiSIEM  

Use FortiSIEM v2 to fetch and update incidents, search events and manage FortiSIEM watchlists. This integration was integrated and tested with FortiSIEMV2 version 6.3.2. Changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

**Commands:**

- `fortisiem-event-search`: Initiate search process on events. Events are retrieved according to a constraint determined either by the query argument or by the filtering arguments. When us
- `fortisiem-incident-update`: Update attributes of the specified incident. Only the provided attributes are overwritten.
- `fortisiem-cmdb-devices-list`: List CMDB (Centralized Management Database) devices with short information for each device. If you provide one of the exclude arguments, their values are exclud
- `fortisiem-cmdb-device-get`: Retrieve full information of the specified devices.
- `fortisiem-monitored-organizations-list`: List of monitored organizations in service provider deployments.
- `fortisiem-event-list-by-incident`: Lists events by the specified incident ID. Available for FortiSiem version 6.6 and earlier.
- `fortisiem-watchlist-list`: List all watchlists from FortiSIEM database.
- `fortisiem-watchlist-get`: Get watchlist by the specified watchlist or entry ID.
- `fortisiem-watchlist-add`: Add a watchlist group. You can also add an entry to the watchlist.
- `fortisiem-watchlist-entry-add`: Add watchlist entry to one or more watchlist groups.
- `fortisiem-watchlist-entry-update`: Update watchlist entry. This command overrides all existing values in the entry's attribute. Fill in all relevant arguments to avoid deletion of data.
- `fortisiem-watchlist-entry-delete`: Delete entry of watchlist.
- `fortisiem-watchlist-delete`: Delete watchlist.
- `fortisiem-watchlist-entry-get`: Get entry by the specified entry ID.
- `fortisiem-event-search-results`: The results of the specified search ID.


## ForwardAuditLogsToSplunkHEC

**Type:** script  
**Product:** Forward platform Audit Logs to Splunk HEC  

This Automation script uses the platform API to get the audit logs and pushes them to Splunk HEC. Dependencies: SlunkPy and Core REST API integrations

**Inputs:**

- `timeframe`: timeframe to fetch in hours


## FullHunt

**Type:** integration  
**Product:** FullHunt  

FullHunt is the attack surface database of the entire Internet. FullHunt enables companies to discover all of their attack surfaces, monitor them for exposure, and continuously scan them for the latest security vulnerabilities. All, in a single platform, and more

**Commands:**

- `fullhunt-get-account-status`: Get information about the user account such as company, email, credit, and usage
- `fullhunt-get-host`: Get host details
- `fullhunt-domain`: Get details about one specified domain
- `fullhunt-get-subdomain`: Get all subdomains from a given domain


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

- `hoxhunt-current-user-get`: Gets the current user information from Hoxhunt.
- `hoxhunt-incident-threats-get`: Gets threats from Hoxhunt.
- `hoxhunt-incident-note-add`: Add Incident note.
- `hoxhunt-incident-threats-remove`: Remove all threats that belong to an incident.
- `hoxhunt-incident-soc-feedback-send`: Send feedback to reporters of incident about whether the reported email was safe, spam or malicious.
- `hoxhunt-incident-set-sensitive`: Set incident to contain sensitive information.
- `hoxhunt-incident-set-soc-classification`: Set soc classification for an incident.
- `hoxhunt-incident-update-state`: Updates Incident state.
- `get-mapping-fields`: Get mapping fields from remote incident. Please note that this method will not update the current incident. It's here for debugging purposes.


## IBM QRadar v3

**Type:** integration  
**Product:** IBM QRadar  

IBM QRadar SIEM helps security teams accurately detect and prioritize threats across the enterprise, supports API versions 10.1 and above. Provides intelligent insights that enable teams to respond quickly to reduce the impact of incidents. This integration was integrated and tested with version 14-20 of QRadar v3

**Commands:**

- `qradar-offenses-list`: Gets offenses from QRadar.
- `qradar-offense-update`: Updates an offense.
- `qradar-closing-reasons`: Retrieves a list of offense closing reasons.
- `qradar-offense-notes-list`: Retrieves a list of notes for an offense.
- `qradar-offense-note-create`: Creates a note on an offense.
- `qradar-rules-list`: Retrieves a list of rules.
- `qradar-rule-groups-list`: Retrieves a list of the rule groups.
- `qradar-assets-list`: Retrieves assets list.
- `qradar-saved-searches-list`: Retrieves a list of Ariel saved searches.
- `qradar-searches-list`: Retrieves the list of Ariel searches IDs. Search status and results can be polled by sending the search ID to the 'qradar-search-status-get' and 'qradar-search-
- `qradar-search-create`: Creates a new asynchronous Ariel search. Returns the search ID. Search status and results can be polled by sending the search ID to the 'qradar-search-status-ge
- `qradar-search-status-get`: Retrieves status information for a search, based on the search ID.
- `qradar-search-results-get`: Retrieves search results.
- `qradar-search-delete`: Deleted search from Qradar, based on the search ID.
- `qradar-reference-sets-list`: 


## IBM Security QRadar SOAR

**Type:** integration  
**Product:** IBM Security QRadar SOAR  

Case management that enables visibility across your tools for continual IR improvement

**Commands:**

- `rs-search-incidents`: Query for incidents
- `rs-update-incident`: Updates incidents.
- `rs-incidents-get-members`: Gets members of the incident.
- `rs-get-incident`: Gets an individual incident by ID.
- `rs-get-incident`: Gets an individual incident by ID.
- `rs-incident-artifacts`: Gets incident artifacts.
- `rs-incident-attachments`: Gets incident attachments.
- `rs-related-incidents`: Gets related incidents.
- `rs-incidents-get-tasks`: Gets tasks of incidents.
- `rs-add-note`: Add a note to an incident.
- `rs-add-artifact`: Add an artifact to an incident.
- `rs-delete-incidents`: Delete multiple incidents.
- `rs-list-incident-notes`: Gets all of the top-level comments for an incident.
- `rs-update-task`: Update an incident's task fields.
- `rs-add-custom-task`: Adds a custom task to the specified incident.


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

- `lp-get-incidents`: Displays incidents between the provided two Timestamps ts_from and ts_to. By default, this command will display first 50 incidents of the past 24 hours but limi
- `lp-get-incident-data`: Retrieves a Particular Incident's Data
- `lp-get-incident-states`: Displays incident states data between the provided two Timestamps ts_from and ts_to. By default, this command will display first 50 data of the past 24 hours bu
- `lp-add-incident-comment`: Add comments to the incidents
- `lp-assign-incidents`: Assigning/Re-assigning Incidents
- `lp-resolve-incidents`: Resolves the Incidents.
- `lp-close-incidents`: Closes the Incidents.
- `lp-reopen-incidents`: Re-opens the closed incidents
- `lp-get-users`: Gets Incident users and user groups.
- `lp-get-users-preference`: Gets LogPoint user's preference such as timezone, date format, etc.
- `lp-get-logpoints`: Gets user's LogPoints.
- `lp-get-repos`: Gets the list of LogPoint repos that can be accessed by the user.
- `lp-get-devices`: Gets devices associated with LogPoint.
- `lp-get-livesearches`: Gets live search results of the alerts and dashboards.
- `lp-get-searchid`: Gets the search ID based on the provided search parameters.


## LogPoint SIEM Playbook

**Type:** playbook  
**Product:** LogPoint SIEM Integration  

LogPoint SIEM Playbook guides users on use cases like blocking IP and domain and disabling users using products like CheckPoint Firewall, Active Directory, and VirusTotal. The actions depicted in the playbook helps analysts create their playbooks based on actual requirements and products deployed. (Available from the platform.0.0)


## LogsignSiem

**Type:** integration  
**Product:** Logsign SIEM  

Logsign SIEM provides comprehensive visibility and control of your data lake by allowing security analysts to collect and store unlimited data, investigate and detect threats, and respond automatically. This integration was integrated and tested with version 4.6.x of Logsign SIEM

**Commands:**

- `logsign-fetch-incidents`: Gets Incidents from Logsign SIEM
- `logsign-get-columns-query`: Gets column values based on your lucene query
- `logsign-get-count-query`: Gets count of column values.


## Microsoft Sentinel

**Type:** integration  
**Product:** Microsoft Sentinel  

Use the Azure Sentinel integration to get and manage incidents and get related entity information for incidents. This integration was integrated and tested with version 2021-04-01 of Azure Sentinel

**Commands:**

- `azure-sentinel-get-incident-by-id`: Gets a single incident from Azure Sentinel.
- `azure-sentinel-list-incidents`: Gets a list of incidents from Azure Sentinel.
- `azure-sentinel-list-watchlists`: Gets a list of watchlists from Azure Sentinel.
- `azure-sentinel-delete-watchlist`: Delete a watchlists from Azure Sentinel.
- `azure-sentinel-watchlist-create-update`: Create or update a watchlist in Azure Sentinel.
- `azure-sentinel-update-incident`: Updates a single incident in Azure Sentinel.
- `azure-sentinel-create-incident`: Creates a single incident in Azure Sentinel.
- `azure-sentinel-delete-incident`: Deletes a single incident in Azure Sentinel.
- `azure-sentinel-list-incident-comments`: Gets the comments of an incident from Azure Sentinel.
- `azure-sentinel-incident-add-comment`: Adds a comment to an incident in Azure Sentinel.
- `azure-sentinel-incident-delete-comment`: Deletes a comment from incident in Azure Sentinel.
- `azure-sentinel-list-incident-relations`: Gets a list of an incident's related entities from Azure Sentinel.
- `azure-sentinel-list-incident-entities`: Gets a list of an incident's entities from Azure Sentinel.
- `azure-sentinel-list-incident-alerts`: Gets a list of an incident's alerts from Azure Sentinel.
- `azure-sentinel-list-watchlist-items`: Get a single watchlist item or list of watchlist items.


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
- `UseCustomSeveritySettings`: Determines whether to use the default mapping in the QRadar generic mapper to set the platform incident severity, or set the severity using 


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

- `splunk-results`: Returns the results of a previous Splunk search. This command can be used in conjunction with the splunk-job-create command.
- `splunk-search`: Searches Splunk for events. For human readable output, the table command is supported in the query argument. For example, query=" * | table field1 field2 field3
- `splunk-submit-event`: Creates a new event in Splunk.
- `splunk-get-indexes`: Prints all Splunk index names.
- `splunk-notable-event-edit`: Update an existing notable event in Splunk ES.
- `splunk-job-create`: Creates a new search job in Splunk.
- `splunk-parse-raw`: Parses the raw part of the event.
- `splunk-submit-event-hec`: Sends events Splunk. if batch_event_data or entry_id arguments are provided then all arguments related to a single event are ignored.
- `splunk-job-status`: Returns the status of a job.
- `get-mapping-fields`: Gets one sample alert per alert type. Used only for creating a mapping with Select Schema.
- `splunk-kv-store-collection-create`: Creates a new KV store table.
- `splunk-kv-store-collection-config`: Configures the KV store fields.
- `splunk-kv-store-collection-add-entries`: Adds objects to a KV store utilizing the batch-save API.
- `splunk-kv-store-collections-list`: Lists all collections for the specified application.
- `splunk-kv-store-collection-data-list`: Lists all data within a specific KV store collection or collections.


## SplunkPy v2

**Type:** integration  
**Product:** Splunk  

Use the SplunkPy v2 integration to: Important: This integration is designed specifically for Splunk Enterprise Security version 8.2 and above. For Splunk ES versions prior to 8.2, please use the legacy SplunkPy integration. This integration was integrated and tested with Splunk Enterprise v10.0.0 and Enterprise Security v8.2.3

**Commands:**

- `splunk-results`: Returns the results of a previous Splunk search. This command can be used in conjunction with the splunk-job-create command.
- `splunk-search`: Searches Splunk for events. For human readable output, the table command is supported in the query argument. For example, query=" * | table field1 field2 field3
- `splunk-submit-event`: Creates a new event in Splunk.
- `splunk-get-indexes`: Prints all Splunk index names.
- `splunk-finding-event-edit`: Update an existing finding event in Splunk ES.
- `splunk-update-investigation`: Updates existing investigations in Splunk ES. Supports updating fields such as owner, status, urgency, disposition, name, and description, adding a note, and ap
- `splunk-job-create`: Creates a new search job in Splunk.
- `splunk-parse-raw`: Parses the raw part of the event.
- `splunk-submit-event-hec`: Sends events Splunk. if batch_event_data or entry_id arguments are provided then all arguments related to a single event are ignored.
- `splunk-job-status`: Returns the status of a job.
- `get-mapping-fields`: Gets one sample alert per alert type. Used only for creating a mapping with Select Schema.
- `splunk-kv-store-collection-create`: Creates a new KV store table.
- `splunk-kv-store-collection-config`: Configures the KV store fields.
- `splunk-kv-store-collection-add-entries`: Adds objects to a KV store utilizing the batch-save API.
- `splunk-kv-store-collections-list`: Lists all collections for the specified application.


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

