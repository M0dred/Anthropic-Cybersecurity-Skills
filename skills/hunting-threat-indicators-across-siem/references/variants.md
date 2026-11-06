# Vendor Variants - Hunting Threat Indicators Across Siem

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Autofocus - File Indicators Hunting

**Product:** AutoFocus by Palo Alto Networks

The playbook queries the PANW Autofocus session and samples log data for file indicators such as MD5, SHA256, and SHA1 hashes. A simple search mode is used to query Autofocus based on the file indicators specified in the playbook inputs. Advanced search mode queries can also be used with multiple query parameters, but require all field names, parameters, and operators (JSON format) to be specified. We recommended using the Autofocus UI to create an advanced query, exporting it, and pasting it into the relevant playbook inputs. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `FileHash`: One or more file hashes to search for in Autofocus simple mode search. Supports MD5, SHA1, and SHA256 file hashes. Separate multiple search values by commas only (without spaces or
- `Search Type`: Which Autofocus search types should be executed. Possible values are session, sample, tag, or all. Session and sample are the recommended search types for this playbook. Sample-bas
- `Scope`: Search scope for sample and session. Possible values are industry, organization, global, or all.
- `SampleQuery`: Use the Autofocus advanced search mode to leverage a variety of query options in a sample search. Advanced search requires you to specify all field names, parameters, and operators
- `Sample first seen`: Narrow down a sample-based search by specifying the timestamp samples were first uploaded to WildFire for analysis (indicators will be searched within samples after this timestamp)
- `Sample last modified`: Narrow down a sample-based search by specifying the timestamp samples were last modified (indicators will be searched within samples after this timestamp).Specify the time in ISO 8
- `SessionQuery`: Use the Autofocus advanced search mode to leverage a variety of query options in a session search. Advanced search requires you to specify all field names, parameters, and operator
- `Sessions time before`: Narrow down a session-based search by specifying the query end timestamp (indicators will be searched within sessions before this timestamp).Specify the time in ISO 8601 format, fo
- `Sessions time after`: Narrow down a session-based search by specifying the query start timestamp (indicators will be searched within sessions after this timestamp).Specify the time in ISO 8601 format, f
- `Wildfire Verdict`: Filter results by WildFire classification assigned to samples based on properties, behaviors, and activities observed for files or email links during static and dynamic analysis.Po

**Outputs:**

- `Autofocus.Samples.HuntingResults`
- `Autofocus.Samples.HuntingResults.Created`
- `Autofocus.Samples.HuntingResults.Finished`
- `Autofocus.Samples.HuntingResults.FileName`
- `Autofocus.Samples.HuntingResults.FileType`
- `Autofocus.Samples.HuntingResults.SHA1`
- `Autofocus.Samples.HuntingResults.SHA256`
- `Autofocus.Samples.HuntingResults.MD5`
- `Autofocus.Samples.HuntingResults.Region`
- `Autofocus.Samples.HuntingResults.Tags`

**Dependencies:**

- Sub-playbooks: Autofocus Query Samples, Sessions and Tags
- Scripts: SetAndHandleEmpty


## Autofocus - Hunting And Threat Detection

**Product:** AutoFocus by Palo Alto Networks

The playbook queries the PANW Autofocus session and samples log data for file and traffic indicators, such as SHA256, SHA1, MD5, IP addresses, URLs, and domains. A simple search mode queries Autofocus based on the indicators specified in the playbook inputs. Advanced queries can also use with multiple query parameters, but require all field names, parameters, and operators (JSON format) to be specified. We recommended using the Autofocus UI to create an advanced query, exporting it, and pasting it into the relevant playbook inputs. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: One or more IP addresses to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `URLDomain`: One or more URLs and/or domains to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `MD5`: One or more MD5 file hashes to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA256`: One or more SHA256 file hashes to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA1`: One or more SHA1 file hashes to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `Search Type`: Which Autofocus search types should be executed. Possible values are session, sample, tag, or all. Session and sample are the recommended search types for this playbook. Sample-bas
- `Scope`: Search scope for sample and session. Possible values are industry, organization, global, or all.
- `SampleQuery`: Use the Autofocus advanced search mode to leverage a variety of query options within a sample search. Advanced search requires you to specify all field names, parameters, and opera
- `Sample first seen`: Narrow down a sample-based search by specifying the timestamp samples were first uploaded to WildFire for analysis (indicators will be searched within samples after this timestamp)
- `Sample last modified`: Narrow down a sample-based search by specifying the timestamp samples were last modified (indicators will be searched within samples after this timestamp).Specify the time in ISO 8

**Outputs:**

- `Autofocus.Samples.HuntingResults`
- `Autofocus.Samples.HuntingResults.Created`
- `Autofocus.Samples.HuntingResults.Finished`
- `Autofocus.Samples.HuntingResults.FileName`
- `Autofocus.Samples.HuntingResults.FileType`
- `Autofocus.Samples.HuntingResults.SHA1`
- `Autofocus.Samples.HuntingResults.SHA256`
- `Autofocus.Samples.HuntingResults.MD5`
- `Autofocus.Samples.HuntingResults.Region`
- `Autofocus.Samples.HuntingResults.Tags`

**Dependencies:**

- Sub-playbooks: Autofocus - File Indicators Hunting, Autofocus - Traffic Indicators Hunting
- Scripts: IsIntegrationAvailable


## Autofocus - Traffic Indicators Hunting

**Product:** AutoFocus by Palo Alto Networks

The playbook queries the PANW Autofocus session and samples log data for traffic indicators such as URLs, IP addresses, and domains. A simple search mode queries Autofocus based on the traffic indicators specified in the playbook inputs. Advanced search mode queries can also be used with multiple query parameters, but require all field names, parameters, and operators (JSON format) to be specified. We recommended using the Autofocus UI to create an advanced query, exporting it, and pasting it into the relevant playbook inputs. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: One or more IP addresses to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `URLDomain`: One or more URLs and/or domains to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `Search Type`: Which Autofocus search types should be executed. Possible values are session, sample, tag, or all. Session and sample are the recommended search types for this playbook. Sample-bas
- `Scope`: Search scope for sample and session. Possible values are industry, organization, or global.
- `SampleQuery`: use the Autofocus advanced search mode to leverage a variety of query options within a sample search. Advanced search requires you to specify all field names, parameters, and opera
- `Sample first seen`: Narrow down a sample-based search by specifying the timestamp samples were first uploaded to WildFire for analysis (indicators will be searched within samples after this timestamp)
- `Sample last modified`: Narrow down a sample-based search by specifying the timestamp samples were last modified (indicators will be searched within samples after this timestamp).Specify the time in ISO 8
- `SessionQuery`: Use the Autofocus advanced search mode to leverage a variety of query options in a session search. Advanced search requires you to specify all field names, parameters, and operator
- `Sessions time before`: Narrow down a session-based search by specifying the query end timestamp (indicators will be searched within sessions before this timestamp).Specify the time in ISO 8601 format, fo
- `Sessions time after`: Narrow down a session-based search by specifying the query start timestamp (indicators will be searched within sessions after this timestamp).Specify the time in ISO 8601 format, f

**Outputs:**

- `Autofocus.Samples.HuntingResults`
- `Autofocus.Samples.HuntingResults.Created`
- `Autofocus.Samples.HuntingResults.Finished`
- `Autofocus.Samples.HuntingResults.FileName`
- `Autofocus.Samples.HuntingResults.FileType`
- `Autofocus.Samples.HuntingResults.SHA1`
- `Autofocus.Samples.HuntingResults.SHA256`
- `Autofocus.Samples.HuntingResults.MD5`
- `Autofocus.Samples.HuntingResults.Region`
- `Autofocus.Samples.HuntingResults.Tags`

**Dependencies:**

- Sub-playbooks: Autofocus Query Samples, Sessions and Tags
- Scripts: SetAndHandleEmpty


## Strata Logging Service - File Indicators Hunting

**Product:** Strata Logging Service by Palo Alto Networks

This playbook queries Strata Logging Service (SLS) for file indicators, including SHA256 hashes, file names, and file types. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `SHA256`: A single or multiple SHA256 file hashes to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Filename`: A single or multiple file names to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `time_range`: An alternative to the 'start_time' and 'end_time' inputs that indicates the timeframe for the search, e.g. 1 week, 1 day, 30 minutes.When the time_range input is specified, the 'st
- `start_time`: Specify the query start time at which to perform a search within Strata Logging Service.For example, start_time="2018-04-26 00:00:00"
- `end_time`: Specify the query end time at which to perform a search within Strata Logging Service.For example, end_time="2018-04-26 00:00:00"
- `limit`: The maximum number of logs to return. Default is 10.
- `fields`: Select the fields you wish to be included in the query results. Selection can be "all" (same as *) or a comma-separated list of specific fields in the table.Separate multiple searc
- `FirewallAction`: Filter network traffic logs that should be retrieved from Strata Logging Service based on firewall action.Separate multiple search values by commas only (without spaces or any spec
- `rule_matched`: Filter network traffic logs to be retrieved from Strata Logging Service based on security policy rule names that the network traffic matches.Separate multiple search values by comm

**Outputs:**

- `CDL.HuntingResults`
- `CDL.HuntingResults.TimeGenerated`
- `CDL.HuntingResults.LogTime`
- `CDL.HuntingResults.IngestionTime`
- `CDL.HuntingResults.App`
- `CDL.HuntingResults.AppCategory`
- `CDL.HuntingResults.RiskOfApp`
- `CDL.HuntingResults.CharacteristicOfApp`
- `CDL.HuntingResults.SanctionedStateOfApp`
- `CDL.HuntingResults.SessionID`

**Dependencies:**

- Integrations: Strata Logging Service
- Scripts: SetAndHandleEmpty
- Commands: cdl-query-file-data, cdl-query-threat-logs


## Strata Logging Service - Indicators Hunting

**Product:** Strata Logging Service by Palo Alto Networks

The playbook facilitates threat hunting and detection of IOCs within Strata Logging Service logs. The playbook and sub-playbooks query Strata Logging Service for files, traffic, HTTP requests, and execution flows indicators. Note that multiple search values should be separated by commas only (without spaces or any special characters). Supported IOCs for this playbook: Separate searches are conducted for each type of indicator in the playbook

**Inputs:**

- `IPAddresses`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination IP addresses.Separate multiple search values by commas only (wit
- `URLDomain`: Single or multiple URLs and/or domains to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Geolocation`: A single or multiple country names or codes to search for within Strata Logging Service. Used for both source and destination geolocations.Separate multiple search values by commas
- `PortNumber`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination ports.Separate multiple search values by commas only (without sp
- `SHA256`: A single or multiple SHA256 file hashes to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Filename`: A single or multiple file names to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Application`: Single or multiple application names or codes to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `URI`: A single or multiple URIs to search for within Strata Logging Service.By default, a 'LIKE' search is used.Separate multiple search values by commas only (without spaces or any spec
- `start_time`: Specify the query start time at which to perform a search within Strata Logging Service.For example, start_time="2018-04-26 00:00:00"

**Outputs:**

- `CDL.HuntingResults`
- `CDL.HuntingResults.TimeGenerated`
- `CDL.HuntingResults.LogTime`
- `CDL.HuntingResults.IngestionTime`
- `CDL.HuntingResults.App`
- `CDL.HuntingResults.AppCategory`
- `CDL.HuntingResults.RiskOfApp`
- `CDL.HuntingResults.CharacteristicOfApp`
- `CDL.HuntingResults.SessionID`
- `CDL.HuntingResults.Action`

**Dependencies:**

- Sub-playbooks: Strata Logging Service - File Indicators Hunting, Strata Logging Service - Traffic Indicators Hunting
- Integrations: Strata Logging Service
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty
- Commands: cdl-query-url-logs, cdl-query-file-data


## Strata Logging Service - Traffic Indicators Hunting

**Product:** Strata Logging Service by Palo Alto Networks

This playbook queries Strata Logging Service (SLS) for traffic indicators, including IP addresses, geolocations, URLs, domains, and ports. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddresses`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination IP addresses.Separate multiple search values by commas only (wit
- `URLDomain`: Single or multiple URLs and/or domains to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Geolocation`: A single or multiple country names or codes to search for within Strata Logging Service. Used for both source and destination geolocations.Separate multiple search values by commas
- `PortNumber`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination ports.Separate multiple search values by commas only (without sp
- `time_range`: An alternative to the 'start_time' and 'end_time' inputs that indicates the timeframe for the search, e.g. 1 week, 1 day, 30 minutes.When the time_range input is specified, the 'st
- `start_time`: Specify the query start time at which to perform a search within Strata Logging Service.For example, start_time="2018-04-26 00:00:00"
- `end_time`: Specify the query end time at which to perform a search within Strata Logging Service.For example, end_time="2018-04-26 00:00:00"
- `limit`: The maximum number of logs to return. Default is 10.
- `fields`: Select the fields you wish to be included in the query results. Selection can be "all" (same as *) or a comma-separated list of specific fields in the table.Separate multiple searc
- `FirewallAction`: Filter network traffic logs that should be retrieved from Strata Logging Service based on firewall action.Separate multiple search values by commas only (without spaces or any spec

**Outputs:**

- `CDL.HuntingResults`
- `CDL.HuntingResults.TimeGenerated`
- `CDL.HuntingResults.LogTime`
- `CDL.HuntingResults.IngestionTime`
- `CDL.HuntingResults.App`
- `CDL.HuntingResults.AppCategory`
- `CDL.HuntingResults.RiskOfApp`
- `CDL.HuntingResults.CharacteristicOfApp`
- `CDL.HuntingResults.SessionID`
- `CDL.HuntingResults.Action`

**Dependencies:**

- Integrations: Strata Logging Service
- Scripts: SetAndHandleEmpty
- Commands: cdl-query-file-data, cdl-query-threat-logs, cdl-query-traffic-logs, cdl-query-url-logs


## Darkfeed Threat hunting-research

**Product:** Sixgill Darkfeed - Annual Subscription

Automatically discover and enrich indicators with the same actor and source as the triggering IOC. Search for and isolate any compromised endpoints and proactively block IOCs from entering your network

**Inputs:**

- `File`: File hash (MD5, SHA-1, SHA-256) from Darkfeed
- `URL`: URL from Darkfeed
- `Maximum number of IOCs`: Set value to the maximum number of IOCs you would like returned in searches for items from the same source and same actor
- `Query time lookup`: Set value to the number of days back in searches for IOCs with the same source and same actor
- `IP`: IP address from Darkfeed
- `Is automated endpoint isolation activated?`: Set "yes" if you would like to automatically isolate endpoints on which malicious indicators were detected
- `Is automated blocking activated?`: Set "yes" if you would like to automatically block discovered malicious indicators.
- `Domain`: Domain from Darkfeed

**Dependencies:**

- Sub-playbooks: Search Endpoints By Hash - Generic V2, Block Indicators - Generic v2, Entity Enrichment - Generic v2, Isolate Endpoint - Generic V2
- Scripts: Set, SetAndHandleEmpty, SixgillSearchIndicators, ToTable
- Commands: associateIndicatorToIncident


## Trellix Email Security Cloud - Indicators Hunting

**Product:** Trellix Email Security - Cloud

This playbook queries Trellix Email Security - Cloud for indicators such as domains, IP addresses, sender and recipient email addresses. Separate searches are conducted for each type of indicator in the playbook. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: A single or multiple IP address to search for within Trellix Email Security - Cloud logs. Used for both source and destination IP addresses.Separate multiple search values by comma
- `Domain`: Single or multiple domains to search for within Trellix Email Security - Cloud logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (withou
- `EmailAddress`: A single or multiple email addresses to search for within Trellix Email Security - Cloud logs. Used for both recipient and sender email addresses.Separate multiple search values by
- `from_email_not_in`: List of sender email addresses to be excluded.The max limit of entries is 10.Separate multiple search values by commas only (without spaces or any special characters).
- `recipients_not_in`: List of recipient email addresses to be excluded (including "cc").The max limit of entries is 10.Separate multiple search values by commas only (without spaces or any special chara
- `has_attachments`: Boolean value filter to indicate if the message has attachments.Values can be only 'true' or 'false'.
- `max_message_size`: Select the message size (in KB) based on which you wish to retrieve messages from the Trellix Email Security - Cloud server.The default value is 20 and the maximum value is 100.
- `from_accepted_date_time`: The start date and time from which you would like to retrieve messages from the Trellix Email Security - Cloud server, e.g. 2017-10-24T10:48:51.000Z.For a complete date range, spec
- `to_accepted_date_time`: The end date and time specify the period of time in which messages should be retrieved from the Trellix Email Security - Cloud server, e.g. 2017-10-24T10:48:51.000Z.For a complete 
- `last_modified_date_time`: The last date and time messages were modified in order to retrieve them from the Trellix Email Security - Cloud server. Dates and times should be accompanied by one of the followin

**Outputs:**

- `FireEyeETP.HuntingResults`
- `FireEyeETP.HuntingResults.acceptedDateTime`
- `FireEyeETP.HuntingResults.lastModifiedDateTime`
- `FireEyeETP.HuntingResults.countryCode`
- `FireEyeETP.HuntingResults.domain`
- `FireEyeETP.HuntingResults.recipientHeader`
- `FireEyeETP.HuntingResults.recipients`
- `FireEyeETP.HuntingResults.senderHeader`
- `FireEyeETP.HuntingResults.sender`
- `FireEyeETP.HuntingResults.senderSMTP`

**Dependencies:**

- Integrations: Trellix Email Security - Cloud
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable
- Commands: fireeye-etp-search-messages


## MDE - Host Advanced Hunting For Network Activity

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook uses the Microsoft Defender For Endpoint Advanced Hunting feature to hunt for host network activity

**Inputs:**

- `DeviceName`: A comma-separated list of host names to hunt.
- `DeviceID`: A comma-separated list of device IDs to hunt.
- `FileSha256`: A comma-separated list of file SHA256 hashes to hunt.

**Outputs:**

- `MicrosoftATP.HuntNetworkConnections.Result`
- `MicrosoftATP.HuntNetworkConnections.Result.external_addresses`
- `MicrosoftATP.HuntNetworkConnections.Result.dns_query`
- `MicrosoftATP.HuntNetworkConnections.Result.encoded_commands`
- `MicrosoftATP.HuntLateralMovementEvidence.Result`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.network_connections`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.smb_connections`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.credential_dumping`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.management_connection`
- `MicrosoftATP.HuntPersistenceEvidence.Result`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Scripts: UnzipFile
- Commands: microsoft-atp-advanced-hunting-persistence-evidence, microsoft-atp-advanced-hunting-network-connections, setIncident, domain, microsoft-atp-advanced-hunting-lateral-movement-evidence, ip, microsoft-atp-live-response-get-file


## MDE - Host Advanced Hunting For Persistence

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook uses the Microsoft Defender For Endpoint Advanced Hunting feature to hunt for host persistence evidence

**Inputs:**

- `FileSha256`: A comma-separated list of file SHA256 hashes to hunt.
- `DeviceName`: A comma-separated list of host names to hunt.
- `FileName`: A comma-separated list of file names to hunt.
- `DeviceID`: A comma-separated list of a device IDs to hunt.

**Outputs:**

- `MicrosoftATP.HuntPersistenceEvidence.Result`
- `MicrosoftATP.HuntPersistenceEvidence.Result.scheduled_job`
- `MicrosoftATP.HuntPersistenceEvidence.Result.registry_entry`
- `MicrosoftATP.HuntPersistenceEvidence.Result.startup_folder_changes`
- `MicrosoftATP.HuntPersistenceEvidence.Result.new_service_created`
- `MicrosoftATP.HuntPersistenceEvidence.Result.service_updated`
- `MicrosoftATP.HuntPersistenceEvidence.Result.file_replaced`
- `MicrosoftATP.HuntPersistenceEvidence.Result.new_user`
- `MicrosoftATP.HuntPersistenceEvidence.Result.new_group`
- `MicrosoftATP.HuntPersistenceEvidence.Result.group_user_change`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Commands: setIncident, microsoft-atp-advanced-hunting-persistence-evidence


## MDE - Host Advanced Hunting For Powershell Executions

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook uses the Microsoft Defender For Endpoint Advanced Hunting feature to hunt for host PowerShell executions

**Inputs:**

- `DeviceName`: A comma-separated list of host names to hunt.
- `FileName`: A comma-separated list of file names to hunt.
- `DeviceID`: A comma-separated list of device IDs to hunt.
- `FileMd5`: A comma-separated list of file MD5 hashes to hunt.
- `FileSha256`: A comma-separated list of file SHA256 hashes to hunt.
- `FileSha1`: A comma-separated list of file SHA1 hashes to hunt.

**Outputs:**

- `MicrosoftATP.HuntProcessDetails.Result`
- `MicrosoftATP.HuntProcessDetails.Result.parent_process`
- `MicrosoftATP.HuntProcessDetails.Result.grandparent_process`
- `MicrosoftATP.HuntProcessDetails.Result.process_details`
- `MicrosoftATP.HuntProcessDetails.Result.beaconing_evidence`
- `MicrosoftATP.HuntProcessDetails.Result.powershell_execution_unsigned_files`
- `MicrosoftATP.HuntProcessDetails.Result.process_excecution_powershell`
- `MicrosoftATP.FileMachine.Machines`
- `MicrosoftATP.FileMachine.Machines.ID`
- `MicrosoftATP.FileMachine.Machines.ComputerDNSName`

**Dependencies:**

- Sub-playbooks: Command-Line Analysis
- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Commands: microsoft-atp-advanced-hunting-process-details, microsoft-atp-advanced-hunting-network-connections, microsoft-atp-get-file-related-machines, setIncident


## Microsoft 365 Defender - Threat Hunting Generic

**Product:** Microsoft 365 Defender

This playbook retrieves email data based on the URLDomain, SHA256, IPAddress, and MessageID inputs. The output is a unified object with all of the retrieved emails based on the following sub-playbooks outputs: Read the playbooks' descriptions in order to get the full details

**Inputs:**

- `URLDomain`: Domain or URL to search within emails. Can be a single domain or URL, or an array of domains or URLs to search.
- `SHA256`: The SHA256 hash file or an array of hashes to search within emails.
- `IPAddress`: The source or destination IP address to search. Can be a single address or an array of IP addresses.
- `MessageID`: Message ID of the email from which the URL was clicked. Note that this can be either of the following 2 values:- The value of the header "Message-ID".- The internal ID of the messa
- `Timeout`: The time limit in seconds for the HTTP request to run.
- `SearchTimeframe`: Number of days past to search.
- `ResultsLimit`: Number of retrieved entries. Enter -1 for unlimited query.
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

- Sub-playbooks: Microsoft 365 Defender - Get Email URL Clicks, Microsoft 365 Defender - Emails Indicators Hunt
- Scripts: SetAndHandleEmpty


## Palo Alto Networks - Hunting And Threat Detection

**Product:** Comprehensive Investigation by Palo Alto Networks

This is a multipurpose playbook used for hunting and threat detection. The playbook receives inputs based on hashes, IP addresses, or domain names provided manually or from outputs by other playbooks. The playbook leverages data received by PANW products including, Strata Logging Service and Pan-OS to search for IP addresses, host names and users related to the provided indicators. The output provided by the playbook enables you to find possibly affected IP addresses, users, and endpoints

**Inputs:**

- `SHA256`: SHA256 hash of the indicator to hunt.
- `MD5`: MD5 hash of the indicator to hunt.
- `SHA1`: SHA1 hash of the indicator to hunt.
- `IPAddresses`: List of IP addresses.
- `URLDomain`: List of domains or urls.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `InternalDomainName`: The organizations internal domain name. This is provided for the script IsInternalHostName that checks if the detected host names are internal or external if the hosts contain the 
- `InternalHostRegex`: This is provided for the script IsInternalHostName that checks if the detected host names are internal or external. Checks if the hosts match the organization's naming convention. 

**Outputs:**

- `PANWHunting.DetectedUsers`
- `PANWHunting.DetectedInternalIPs`
- `PANWHunting.DetectedExternalIPs`
- `PANWHunting.DetectedInternalHosts`
- `PANWHunting.DetectedExternalHosts`

**Dependencies:**

- Sub-playbooks: Convert file hash to corresponding hashes, PAN-OS Query Logs For Indicators
- Scripts: IsIPInRanges, IsIntegrationAvailable, IsInternalHostName, SetAndHandleEmpty
- Commands: cdl-query-threat-logs, cdl-query-traffic-logs, cdl-query-url-logs, prisma-cloud-network-search, xdr-get-alerts


## Carbon black Protection Rapid IOC Hunting

**Product:** Carbon Black Enterprise Protection

Hunts for endpoint activity involving hash and domain IOCs, using Carbon black Protection (Bit9)


## Proactive Threat Hunting - Execute Query

**Product:** Proactive Threat Hunting

This playbook will be executed from the "Proactive Threat Hunting" layout button with the objective of executing a query that will be provided by the analyst. The playbook supports executing a query using the following integrations

**Dependencies:**

- Scripts: JsonToTable, Print, DeleteContext
- Commands: xdr-xql-generic-query, setIncident, microsoft-atp-advanced-hunting


## QRadar Get Hunting Results

**Product:** IBM QRadar

This playbook is used to sort the QRadar search results to display the IP addresses, assets, and usernames that the search provided. In addition, the results allow you to differentiate between internal and external IP addresses as well as query the QRadar assets API in order to get the assets details from the IP addresses. You can provide the QRadar fields names and the organizations' IP ranges in order to properly sort the data. The end result of the playbook will be the internal and external IP addresses detected as well as the assets and users

**Inputs:**

- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `InvestigationIPFields`: The values of these QRadar fields will be used for the playbook IP addresses outputs.
- `InvestigationUserFields`: The values of these QRadar fields will be used for the playbook user name outputs.
- `SearchResults`: The search results of an AQL search.

**Outputs:**

- `QRadar.DetectedUsers`
- `QRadar.DetectedInternalIPs`
- `QRadar.DetectedExternalIPs`
- `QRadar.DetectedInternalHosts`
- `QRadar.DetectedExternalHosts`

**Dependencies:**

- Integrations: QRadar_v3
- Scripts: Set, IsIPInRanges, SetAndHandleEmpty
- Commands: qradar-assets-list


## QRadar Indicator Hunting V2

**Product:** IBM QRadar

The Playbook queries QRadar SIEM for indicators such as file hashes, IP addresses, domains, or urls

**Inputs:**

- `MD5`: MD5 hash file or an array of hashes to search.
- `QradarMD5Field`: MD5 field to search in QRadar. If none are specified, the search will use a payload contains filter.
- `SHA1`: SHA1 hash file or an array of hashes to search.
- `QradarSHA1Field`: SHA1 field to search in QRadar. If none are specified, the search will use a payload contains filter.
- `SHA256`: SHA256 hash file or an array of hashes to search.
- `QradarSHA256Field`: SHA256 field to search in QRadar. If none are specified, the search will use a payload contains filter.
- `IPAddress`: Source or destination IP to search. Can be a single address or an array of addresses.
- `QradarIPfield`: IP field to search in QRadar. If none are specified, the search will use sourceip or destinationip (combined).
- `URLDomain`: Domain or Url can be single or an array of domain/urls to search. By default the LIKE clause is used.
- `QradarURLDomainField`: URL/Domain field to search in QRadar. If none are specified, the search will use a payload contains filter.

**Outputs:**

- `QRadar.DetectedUsers`
- `QRadar.DetectedInternalIPs`
- `QRadar.DetectedExternalIPs`
- `QRadar.DetectedInternalHosts`
- `QRadar.DetectedExternalHosts`

**Dependencies:**

- Integrations: QRadar_v3
- Scripts: IsIPInRanges, Set, SetAndHandleEmpty
- Commands: qradar-assets-list, qradar-search-retrieve-events


## Splunk Indicator Hunting

**Product:** Splunk

Queries Splunk for indicators such as file hashes, IP addresses, domains, or urls. It outputs detected users, IP addresses, and hostnames related to the indicators

**Inputs:**

- `MD5`: The MD5 hash or an array of hashes for which to search.
- `SplunkMD5Field`: The name of the fields, in Splunk, in which to find the MD5 hash. You can enter multiple field names using a comma-separated format. If no field is specified, the search uses quick
- `SHA1`: The SHA1 hash or an array of hashes on which to search.
- `SplunkSHA1Field`: The name of the fields, in Splunk, in which to find the SHA1 field. You can enter multiple field names using a comma-separated format. If no field is specified, the search uses qui
- `SHA256`: The SHA256 hash or an array of hashes on which to search.
- `SplunkSHA256Field`: The name of the fields, in Splunk, in which to find the SHA256. You can enter multiple field names using a comma-separated format. If no field is specified, the search uses quick f
- `IPAddress`: The source or destination IP address on which to search. Can be a single address or an array of addresses.
- `SplunkIPField`: The name of the fields, in Splunk, in which to find the IP addresses. You can enter multiple field names using a comma-separated format. For example, sourceip,destinationip.
- `URLDomain`: The domain or URL can be single or an array of domain/urls to search. By default the LIKE clause is used.
- `SplunkURLDomainField`: The name of the fields, in Splunk, in which to find the URL/Domain. If no field is specified, the search uses quick filter. Only one field can be used in this parameter.

**Outputs:**

- `Splunk.DetectedUsers`
- `Splunk.DetectedInternalIPs`
- `Splunk.DetectedExternalIPs`
- `Splunk.DetectedInternalHosts`
- `Splunk.DetectedExternalHosts`

**Dependencies:**

- Scripts: commentsToContext, IsIPInRanges, SetAndHandleEmpty, IsInternalHostName, Set
- Commands: splunk-search


## Suspicious Domain Hunting Incident Handling

**Product:** Suspicious Domain Hunting

This playbook process "Suspicious Domain Hunting" incidents generated by the CertStream integration

**Inputs:**

- `similarityMaxThreshold`: The minimum threshold value for malicious verdict
- `similarityMinThreshold`: The minimum threshold value for suspicious verdict
- `contactEmail`: Email address to be used as contact email when sending a takedown request email

**Dependencies:**

- Sub-playbooks: Block Domain - Generic v2, Threat Hunting - Generic
- Scripts: HttpV2, HtmlDifflibCheck, Set, SetAndHandleEmpty, IsIntegrationAvailable, imagecompare
- Commands: domain, expireIndicators, whois, url, rasterize, setIndicators, closeInvestigation


## Threat Hunting - Chronicle

**Product:** Google SecOps

Use this playbook to investigate and remediate suspicious IOC domain matches with recent activity found in the enterprise. This playbook also creates indicators for the entities fetched, as well as investigating and enriching them. Supported Integrations

**Inputs:**

- `auto_block_entities`: Autoblock the detected suspicious Domain(s) and URL(s). You can set this as 'Yes' or 'No' manually here or you can set it into a custom incident field 'Chronicle Auto Block Entitie

**Dependencies:**

- Sub-playbooks: Domain Enrichment - Generic v2, Endpoint Enrichment - Generic v2.1, Block URL - Generic, URL Enrichment - Generic v2, IP Enrichment - Generic v2, PAN-OS - Block Domain - External Dynamic List
- Integrations: Chronicle, Whois
- Scripts: ExtractDomainFromIOCDomainMatchRes, Print, ConvertDomainToURLs, ChronicleAssetIdentifierScript
- Commands: domain, whois, gcb-assets, createNewIndicator, closeInvestigation


## TIE - IOC Hunt

**Product:** McAfee Threat Intelligence Exchange

Hunt for sightings of MD5, SHA1 and/or SHA256 hashes on endpoints, using McAfee TIE (requires ePO as well). Input: Output

**Inputs:**

- `Hash`: The Hash to hunt (Could be MD5,SHA1,SHA256).Default is set to all hashes

**Outputs:**

- `McAfee.ePO.Endpoint`

**Dependencies:**

- Integrations: McAfeeTIEV2, McAfee-TIE
- Scripts: Exists
- Commands: epo-find-system, tie-file-references


## Trend Micro CAS - Indicators Hunting

**Product:** TrendAI™ Cloud App Security

In this playbook, the 'trendmicro-cas-email-sweep' command is used to automatically hunt for and detect IOCs within email messages protected by Cloud App Security (CAS). Note that multiple search values should be separated by commas only (without spaces or any special characters). Supported IOCs for this playbook: Separate searches are conducted for each type of indicator in the playbook

**Inputs:**

- `IPAddress`: A single or multiple IP address to search for within TrendMicro CAS logs. Used for both source and destination IP addresses Separate multiple search values by commas only (without 
- `CIDR`: A single or multiple IP ranges to search for within TrendMicro CAS logs. Used for both source and destination IP addresses.Separate multiple search values by commas only (without s
- `URLDomain`: Single or multiple URLs and/or domains to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `FileName`: Single or multiple file names to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA1`: Single or multiple SHA1 file hashes to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `EmailAddress`: A single or multiple email addresses to search for within TrendMicro CAS logs. Used for both recipient and sender email addresses.Separate multiple search values by commas only (wi
- `subject`: Filter messages that should be retrieved from the TrendMicro CAS based on the email subject (string).Use double quotes to search for an exact phrase, for example, "messageA message
- `start`: The start date and time from which you would like to retrieve messages from TrendMicro CAS. Use ISO 8601 time format, e.g. 2020-08-01T02:31:20Z, or 'human-readable' data, such as 1
- `end`: The end date and time specify the period of time in which messages should be retrieved from TrendMicro CAS. Use ISO 8601 time format, e.g. 2020-08-01T02:31:20Z, or 'human-readable'

**Outputs:**

- `TrendMicroCAS.HuntingResults.value`
- `TrendMicroCAS.HuntingResults.value.mail_message_delivery_time`
- `TrendMicroCAS.HuntingResults.value.mail_message_id`
- `TrendMicroCAS.HuntingResults.value.mail_unique_id`
- `TrendMicroCAS.HuntingResults.value.mailbox`
- `TrendMicroCAS.HuntingResults.value.source_ip`
- `TrendMicroCAS.HuntingResults.value.source_domain`
- `TrendMicroCAS.HuntingResults.value.mail_urls`
- `TrendMicroCAS.HuntingResults.value.mail_message_subject`
- `TrendMicroCAS.HuntingResults.value.mail_message_sender`

**Dependencies:**

- Integrations: TrendMicro Cloud App Security
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty
- Commands: trendmicro-cas-email-sweep

## Autofocus - File Indicators Hunting

**Product:** AutoFocus by Palo Alto Networks

The playbook queries the PANW Autofocus session and samples log data for file indicators such as MD5, SHA256, and SHA1 hashes. A simple search mode is used to query Autofocus based on the file indicators specified in the playbook inputs. Advanced search mode queries can also be used with multiple query parameters, but require all field names, parameters, and operators (JSON format) to be specified. We recommended using the Autofocus UI to create an advanced query, exporting it, and pasting it into the relevant playbook inputs. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `FileHash`: One or more file hashes to search for in Autofocus simple mode search. Supports MD5, SHA1, and SHA256 file hashes. Separate multiple search values by commas only (without spaces or
- `Search Type`: Which Autofocus search types should be executed. Possible values are session, sample, tag, or all. Session and sample are the recommended search types for this playbook. Sample-bas
- `Scope`: Search scope for sample and session. Possible values are industry, organization, global, or all.
- `SampleQuery`: Use the Autofocus advanced search mode to leverage a variety of query options in a sample search. Advanced search requires you to specify all field names, parameters, and operators
- `Sample first seen`: Narrow down a sample-based search by specifying the timestamp samples were first uploaded to WildFire for analysis (indicators will be searched within samples after this timestamp)
- `Sample last modified`: Narrow down a sample-based search by specifying the timestamp samples were last modified (indicators will be searched within samples after this timestamp).Specify the time in ISO 8
- `SessionQuery`: Use the Autofocus advanced search mode to leverage a variety of query options in a session search. Advanced search requires you to specify all field names, parameters, and operator
- `Sessions time before`: Narrow down a session-based search by specifying the query end timestamp (indicators will be searched within sessions before this timestamp).Specify the time in ISO 8601 format, fo
- `Sessions time after`: Narrow down a session-based search by specifying the query start timestamp (indicators will be searched within sessions after this timestamp).Specify the time in ISO 8601 format, f
- `Wildfire Verdict`: Filter results by WildFire classification assigned to samples based on properties, behaviors, and activities observed for files or email links during static and dynamic analysis.Po

**Outputs:**

- `Autofocus.Samples.HuntingResults`
- `Autofocus.Samples.HuntingResults.Created`
- `Autofocus.Samples.HuntingResults.Finished`
- `Autofocus.Samples.HuntingResults.FileName`
- `Autofocus.Samples.HuntingResults.FileType`
- `Autofocus.Samples.HuntingResults.SHA1`
- `Autofocus.Samples.HuntingResults.SHA256`
- `Autofocus.Samples.HuntingResults.MD5`
- `Autofocus.Samples.HuntingResults.Region`
- `Autofocus.Samples.HuntingResults.Tags`

**Dependencies:**

- Sub-playbooks: Autofocus Query Samples, Sessions and Tags
- Scripts: SetAndHandleEmpty


## Autofocus - Hunting And Threat Detection

**Product:** AutoFocus by Palo Alto Networks

The playbook queries the PANW Autofocus session and samples log data for file and traffic indicators, such as SHA256, SHA1, MD5, IP addresses, URLs, and domains. A simple search mode queries Autofocus based on the indicators specified in the playbook inputs. Advanced queries can also use with multiple query parameters, but require all field names, parameters, and operators (JSON format) to be specified. We recommended using the Autofocus UI to create an advanced query, exporting it, and pasting it into the relevant playbook inputs. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: One or more IP addresses to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `URLDomain`: One or more URLs and/or domains to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `MD5`: One or more MD5 file hashes to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA256`: One or more SHA256 file hashes to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA1`: One or more SHA1 file hashes to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `Search Type`: Which Autofocus search types should be executed. Possible values are session, sample, tag, or all. Session and sample are the recommended search types for this playbook. Sample-bas
- `Scope`: Search scope for sample and session. Possible values are industry, organization, global, or all.
- `SampleQuery`: Use the Autofocus advanced search mode to leverage a variety of query options within a sample search. Advanced search requires you to specify all field names, parameters, and opera
- `Sample first seen`: Narrow down a sample-based search by specifying the timestamp samples were first uploaded to WildFire for analysis (indicators will be searched within samples after this timestamp)
- `Sample last modified`: Narrow down a sample-based search by specifying the timestamp samples were last modified (indicators will be searched within samples after this timestamp).Specify the time in ISO 8

**Outputs:**

- `Autofocus.Samples.HuntingResults`
- `Autofocus.Samples.HuntingResults.Created`
- `Autofocus.Samples.HuntingResults.Finished`
- `Autofocus.Samples.HuntingResults.FileName`
- `Autofocus.Samples.HuntingResults.FileType`
- `Autofocus.Samples.HuntingResults.SHA1`
- `Autofocus.Samples.HuntingResults.SHA256`
- `Autofocus.Samples.HuntingResults.MD5`
- `Autofocus.Samples.HuntingResults.Region`
- `Autofocus.Samples.HuntingResults.Tags`

**Dependencies:**

- Sub-playbooks: Autofocus - File Indicators Hunting, Autofocus - Traffic Indicators Hunting
- Scripts: IsIntegrationAvailable


## Autofocus - Traffic Indicators Hunting

**Product:** AutoFocus by Palo Alto Networks

The playbook queries the PANW Autofocus session and samples log data for traffic indicators such as URLs, IP addresses, and domains. A simple search mode queries Autofocus based on the traffic indicators specified in the playbook inputs. Advanced search mode queries can also be used with multiple query parameters, but require all field names, parameters, and operators (JSON format) to be specified. We recommended using the Autofocus UI to create an advanced query, exporting it, and pasting it into the relevant playbook inputs. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: One or more IP addresses to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `URLDomain`: One or more URLs and/or domains to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `Search Type`: Which Autofocus search types should be executed. Possible values are session, sample, tag, or all. Session and sample are the recommended search types for this playbook. Sample-bas
- `Scope`: Search scope for sample and session. Possible values are industry, organization, or global.
- `SampleQuery`: use the Autofocus advanced search mode to leverage a variety of query options within a sample search. Advanced search requires you to specify all field names, parameters, and opera
- `Sample first seen`: Narrow down a sample-based search by specifying the timestamp samples were first uploaded to WildFire for analysis (indicators will be searched within samples after this timestamp)
- `Sample last modified`: Narrow down a sample-based search by specifying the timestamp samples were last modified (indicators will be searched within samples after this timestamp).Specify the time in ISO 8
- `SessionQuery`: Use the Autofocus advanced search mode to leverage a variety of query options in a session search. Advanced search requires you to specify all field names, parameters, and operator
- `Sessions time before`: Narrow down a session-based search by specifying the query end timestamp (indicators will be searched within sessions before this timestamp).Specify the time in ISO 8601 format, fo
- `Sessions time after`: Narrow down a session-based search by specifying the query start timestamp (indicators will be searched within sessions after this timestamp).Specify the time in ISO 8601 format, f

**Outputs:**

- `Autofocus.Samples.HuntingResults`
- `Autofocus.Samples.HuntingResults.Created`
- `Autofocus.Samples.HuntingResults.Finished`
- `Autofocus.Samples.HuntingResults.FileName`
- `Autofocus.Samples.HuntingResults.FileType`
- `Autofocus.Samples.HuntingResults.SHA1`
- `Autofocus.Samples.HuntingResults.SHA256`
- `Autofocus.Samples.HuntingResults.MD5`
- `Autofocus.Samples.HuntingResults.Region`
- `Autofocus.Samples.HuntingResults.Tags`

**Dependencies:**

- Sub-playbooks: Autofocus Query Samples, Sessions and Tags
- Scripts: SetAndHandleEmpty


## Strata Logging Service - File Indicators Hunting

**Product:** Strata Logging Service by Palo Alto Networks

This playbook queries Strata Logging Service (SLS) for file indicators, including SHA256 hashes, file names, and file types. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `SHA256`: A single or multiple SHA256 file hashes to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Filename`: A single or multiple file names to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `time_range`: An alternative to the 'start_time' and 'end_time' inputs that indicates the timeframe for the search, e.g. 1 week, 1 day, 30 minutes.When the time_range input is specified, the 'st
- `start_time`: Specify the query start time at which to perform a search within Strata Logging Service.For example, start_time="2018-04-26 00:00:00"
- `end_time`: Specify the query end time at which to perform a search within Strata Logging Service.For example, end_time="2018-04-26 00:00:00"
- `limit`: The maximum number of logs to return. Default is 10.
- `fields`: Select the fields you wish to be included in the query results. Selection can be "all" (same as *) or a comma-separated list of specific fields in the table.Separate multiple searc
- `FirewallAction`: Filter network traffic logs that should be retrieved from Strata Logging Service based on firewall action.Separate multiple search values by commas only (without spaces or any spec
- `rule_matched`: Filter network traffic logs to be retrieved from Strata Logging Service based on security policy rule names that the network traffic matches.Separate multiple search values by comm

**Outputs:**

- `CDL.HuntingResults`
- `CDL.HuntingResults.TimeGenerated`
- `CDL.HuntingResults.LogTime`
- `CDL.HuntingResults.IngestionTime`
- `CDL.HuntingResults.App`
- `CDL.HuntingResults.AppCategory`
- `CDL.HuntingResults.RiskOfApp`
- `CDL.HuntingResults.CharacteristicOfApp`
- `CDL.HuntingResults.SanctionedStateOfApp`
- `CDL.HuntingResults.SessionID`

**Dependencies:**

- Integrations: Strata Logging Service
- Scripts: SetAndHandleEmpty
- Commands: cdl-query-file-data, cdl-query-threat-logs


## Strata Logging Service - Indicators Hunting

**Product:** Strata Logging Service by Palo Alto Networks

The playbook facilitates threat hunting and detection of IOCs within Strata Logging Service logs. The playbook and sub-playbooks query Strata Logging Service for files, traffic, HTTP requests, and execution flows indicators. Note that multiple search values should be separated by commas only (without spaces or any special characters). Supported IOCs for this playbook: Separate searches are conducted for each type of indicator in the playbook

**Inputs:**

- `IPAddresses`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination IP addresses.Separate multiple search values by commas only (wit
- `URLDomain`: Single or multiple URLs and/or domains to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Geolocation`: A single or multiple country names or codes to search for within Strata Logging Service. Used for both source and destination geolocations.Separate multiple search values by commas
- `PortNumber`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination ports.Separate multiple search values by commas only (without sp
- `SHA256`: A single or multiple SHA256 file hashes to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Filename`: A single or multiple file names to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Application`: Single or multiple application names or codes to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `URI`: A single or multiple URIs to search for within Strata Logging Service.By default, a 'LIKE' search is used.Separate multiple search values by commas only (without spaces or any spec
- `start_time`: Specify the query start time at which to perform a search within Strata Logging Service.For example, start_time="2018-04-26 00:00:00"

**Outputs:**

- `CDL.HuntingResults`
- `CDL.HuntingResults.TimeGenerated`
- `CDL.HuntingResults.LogTime`
- `CDL.HuntingResults.IngestionTime`
- `CDL.HuntingResults.App`
- `CDL.HuntingResults.AppCategory`
- `CDL.HuntingResults.RiskOfApp`
- `CDL.HuntingResults.CharacteristicOfApp`
- `CDL.HuntingResults.SessionID`
- `CDL.HuntingResults.Action`

**Dependencies:**

- Sub-playbooks: Strata Logging Service - File Indicators Hunting, Strata Logging Service - Traffic Indicators Hunting
- Integrations: Strata Logging Service
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty
- Commands: cdl-query-url-logs, cdl-query-file-data


## Strata Logging Service - Traffic Indicators Hunting

**Product:** Strata Logging Service by Palo Alto Networks

This playbook queries Strata Logging Service (SLS) for traffic indicators, including IP addresses, geolocations, URLs, domains, and ports. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddresses`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination IP addresses.Separate multiple search values by commas only (wit
- `URLDomain`: Single or multiple URLs and/or domains to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Geolocation`: A single or multiple country names or codes to search for within Strata Logging Service. Used for both source and destination geolocations.Separate multiple search values by commas
- `PortNumber`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination ports.Separate multiple search values by commas only (without sp
- `time_range`: An alternative to the 'start_time' and 'end_time' inputs that indicates the timeframe for the search, e.g. 1 week, 1 day, 30 minutes.When the time_range input is specified, the 'st
- `start_time`: Specify the query start time at which to perform a search within Strata Logging Service.For example, start_time="2018-04-26 00:00:00"
- `end_time`: Specify the query end time at which to perform a search within Strata Logging Service.For example, end_time="2018-04-26 00:00:00"
- `limit`: The maximum number of logs to return. Default is 10.
- `fields`: Select the fields you wish to be included in the query results. Selection can be "all" (same as *) or a comma-separated list of specific fields in the table.Separate multiple searc
- `FirewallAction`: Filter network traffic logs that should be retrieved from Strata Logging Service based on firewall action.Separate multiple search values by commas only (without spaces or any spec

**Outputs:**

- `CDL.HuntingResults`
- `CDL.HuntingResults.TimeGenerated`
- `CDL.HuntingResults.LogTime`
- `CDL.HuntingResults.IngestionTime`
- `CDL.HuntingResults.App`
- `CDL.HuntingResults.AppCategory`
- `CDL.HuntingResults.RiskOfApp`
- `CDL.HuntingResults.CharacteristicOfApp`
- `CDL.HuntingResults.SessionID`
- `CDL.HuntingResults.Action`

**Dependencies:**

- Integrations: Strata Logging Service
- Scripts: SetAndHandleEmpty
- Commands: cdl-query-file-data, cdl-query-threat-logs, cdl-query-traffic-logs, cdl-query-url-logs


## Darkfeed Threat hunting-research

**Product:** Sixgill Darkfeed - Annual Subscription

Automatically discover and enrich indicators with the same actor and source as the triggering IOC. Search for and isolate any compromised endpoints and proactively block IOCs from entering your network

**Inputs:**

- `File`: File hash (MD5, SHA-1, SHA-256) from Darkfeed
- `URL`: URL from Darkfeed
- `Maximum number of IOCs`: Set value to the maximum number of IOCs you would like returned in searches for items from the same source and same actor
- `Query time lookup`: Set value to the number of days back in searches for IOCs with the same source and same actor
- `IP`: IP address from Darkfeed
- `Is automated endpoint isolation activated?`: Set "yes" if you would like to automatically isolate endpoints on which malicious indicators were detected
- `Is automated blocking activated?`: Set "yes" if you would like to automatically block discovered malicious indicators.
- `Domain`: Domain from Darkfeed

**Dependencies:**

- Sub-playbooks: Search Endpoints By Hash - Generic V2, Block Indicators - Generic v2, Entity Enrichment - Generic v2, Isolate Endpoint - Generic V2
- Scripts: Set, SetAndHandleEmpty, SixgillSearchIndicators, ToTable
- Commands: associateIndicatorToIncident


## Trellix Email Security Cloud - Indicators Hunting

**Product:** Trellix Email Security - Cloud

This playbook queries Trellix Email Security - Cloud for indicators such as domains, IP addresses, sender and recipient email addresses. Separate searches are conducted for each type of indicator in the playbook. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: A single or multiple IP address to search for within Trellix Email Security - Cloud logs. Used for both source and destination IP addresses.Separate multiple search values by comma
- `Domain`: Single or multiple domains to search for within Trellix Email Security - Cloud logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (withou
- `EmailAddress`: A single or multiple email addresses to search for within Trellix Email Security - Cloud logs. Used for both recipient and sender email addresses.Separate multiple search values by
- `from_email_not_in`: List of sender email addresses to be excluded.The max limit of entries is 10.Separate multiple search values by commas only (without spaces or any special characters).
- `recipients_not_in`: List of recipient email addresses to be excluded (including "cc").The max limit of entries is 10.Separate multiple search values by commas only (without spaces or any special chara
- `has_attachments`: Boolean value filter to indicate if the message has attachments.Values can be only 'true' or 'false'.
- `max_message_size`: Select the message size (in KB) based on which you wish to retrieve messages from the Trellix Email Security - Cloud server.The default value is 20 and the maximum value is 100.
- `from_accepted_date_time`: The start date and time from which you would like to retrieve messages from the Trellix Email Security - Cloud server, e.g. 2017-10-24T10:48:51.000Z.For a complete date range, spec
- `to_accepted_date_time`: The end date and time specify the period of time in which messages should be retrieved from the Trellix Email Security - Cloud server, e.g. 2017-10-24T10:48:51.000Z.For a complete 
- `last_modified_date_time`: The last date and time messages were modified in order to retrieve them from the Trellix Email Security - Cloud server. Dates and times should be accompanied by one of the followin

**Outputs:**

- `FireEyeETP.HuntingResults`
- `FireEyeETP.HuntingResults.acceptedDateTime`
- `FireEyeETP.HuntingResults.lastModifiedDateTime`
- `FireEyeETP.HuntingResults.countryCode`
- `FireEyeETP.HuntingResults.domain`
- `FireEyeETP.HuntingResults.recipientHeader`
- `FireEyeETP.HuntingResults.recipients`
- `FireEyeETP.HuntingResults.senderHeader`
- `FireEyeETP.HuntingResults.sender`
- `FireEyeETP.HuntingResults.senderSMTP`

**Dependencies:**

- Integrations: Trellix Email Security - Cloud
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable
- Commands: fireeye-etp-search-messages


## MDE - Host Advanced Hunting For Network Activity

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook uses the Microsoft Defender For Endpoint Advanced Hunting feature to hunt for host network activity

**Inputs:**

- `DeviceName`: A comma-separated list of host names to hunt.
- `DeviceID`: A comma-separated list of device IDs to hunt.
- `FileSha256`: A comma-separated list of file SHA256 hashes to hunt.

**Outputs:**

- `MicrosoftATP.HuntNetworkConnections.Result`
- `MicrosoftATP.HuntNetworkConnections.Result.external_addresses`
- `MicrosoftATP.HuntNetworkConnections.Result.dns_query`
- `MicrosoftATP.HuntNetworkConnections.Result.encoded_commands`
- `MicrosoftATP.HuntLateralMovementEvidence.Result`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.network_connections`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.smb_connections`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.credential_dumping`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.management_connection`
- `MicrosoftATP.HuntPersistenceEvidence.Result`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Scripts: UnzipFile
- Commands: microsoft-atp-advanced-hunting-persistence-evidence, microsoft-atp-advanced-hunting-network-connections, setIncident, domain, microsoft-atp-advanced-hunting-lateral-movement-evidence, ip, microsoft-atp-live-response-get-file


## MDE - Host Advanced Hunting For Persistence

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook uses the Microsoft Defender For Endpoint Advanced Hunting feature to hunt for host persistence evidence

**Inputs:**

- `FileSha256`: A comma-separated list of file SHA256 hashes to hunt.
- `DeviceName`: A comma-separated list of host names to hunt.
- `FileName`: A comma-separated list of file names to hunt.
- `DeviceID`: A comma-separated list of a device IDs to hunt.

**Outputs:**

- `MicrosoftATP.HuntPersistenceEvidence.Result`
- `MicrosoftATP.HuntPersistenceEvidence.Result.scheduled_job`
- `MicrosoftATP.HuntPersistenceEvidence.Result.registry_entry`
- `MicrosoftATP.HuntPersistenceEvidence.Result.startup_folder_changes`
- `MicrosoftATP.HuntPersistenceEvidence.Result.new_service_created`
- `MicrosoftATP.HuntPersistenceEvidence.Result.service_updated`
- `MicrosoftATP.HuntPersistenceEvidence.Result.file_replaced`
- `MicrosoftATP.HuntPersistenceEvidence.Result.new_user`
- `MicrosoftATP.HuntPersistenceEvidence.Result.new_group`
- `MicrosoftATP.HuntPersistenceEvidence.Result.group_user_change`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Commands: setIncident, microsoft-atp-advanced-hunting-persistence-evidence


## MDE - Host Advanced Hunting For Powershell Executions

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook uses the Microsoft Defender For Endpoint Advanced Hunting feature to hunt for host PowerShell executions

**Inputs:**

- `DeviceName`: A comma-separated list of host names to hunt.
- `FileName`: A comma-separated list of file names to hunt.
- `DeviceID`: A comma-separated list of device IDs to hunt.
- `FileMd5`: A comma-separated list of file MD5 hashes to hunt.
- `FileSha256`: A comma-separated list of file SHA256 hashes to hunt.
- `FileSha1`: A comma-separated list of file SHA1 hashes to hunt.

**Outputs:**

- `MicrosoftATP.HuntProcessDetails.Result`
- `MicrosoftATP.HuntProcessDetails.Result.parent_process`
- `MicrosoftATP.HuntProcessDetails.Result.grandparent_process`
- `MicrosoftATP.HuntProcessDetails.Result.process_details`
- `MicrosoftATP.HuntProcessDetails.Result.beaconing_evidence`
- `MicrosoftATP.HuntProcessDetails.Result.powershell_execution_unsigned_files`
- `MicrosoftATP.HuntProcessDetails.Result.process_excecution_powershell`
- `MicrosoftATP.FileMachine.Machines`
- `MicrosoftATP.FileMachine.Machines.ID`
- `MicrosoftATP.FileMachine.Machines.ComputerDNSName`

**Dependencies:**

- Sub-playbooks: Command-Line Analysis
- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Commands: microsoft-atp-advanced-hunting-process-details, microsoft-atp-advanced-hunting-network-connections, microsoft-atp-get-file-related-machines, setIncident


## Microsoft 365 Defender - Threat Hunting Generic

**Product:** Microsoft 365 Defender

This playbook retrieves email data based on the URLDomain, SHA256, IPAddress, and MessageID inputs. The output is a unified object with all of the retrieved emails based on the following sub-playbooks outputs: Read the playbooks' descriptions in order to get the full details

**Inputs:**

- `URLDomain`: Domain or URL to search within emails. Can be a single domain or URL, or an array of domains or URLs to search.
- `SHA256`: The SHA256 hash file or an array of hashes to search within emails.
- `IPAddress`: The source or destination IP address to search. Can be a single address or an array of IP addresses.
- `MessageID`: Message ID of the email from which the URL was clicked. Note that this can be either of the following 2 values:- The value of the header "Message-ID".- The internal ID of the messa
- `Timeout`: The time limit in seconds for the HTTP request to run.
- `SearchTimeframe`: Number of days past to search.
- `ResultsLimit`: Number of retrieved entries. Enter -1 for unlimited query.
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

- Sub-playbooks: Microsoft 365 Defender - Get Email URL Clicks, Microsoft 365 Defender - Emails Indicators Hunt
- Scripts: SetAndHandleEmpty


## Palo Alto Networks - Hunting And Threat Detection

**Product:** Comprehensive Investigation by Palo Alto Networks

This is a multipurpose playbook used for hunting and threat detection. The playbook receives inputs based on hashes, IP addresses, or domain names provided manually or from outputs by other playbooks. The playbook leverages data received by PANW products including, Strata Logging Service and Pan-OS to search for IP addresses, host names and users related to the provided indicators. The output provided by the playbook enables you to find possibly affected IP addresses, users, and endpoints

**Inputs:**

- `SHA256`: SHA256 hash of the indicator to hunt.
- `MD5`: MD5 hash of the indicator to hunt.
- `SHA1`: SHA1 hash of the indicator to hunt.
- `IPAddresses`: List of IP addresses.
- `URLDomain`: List of domains or urls.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `InternalDomainName`: The organizations internal domain name. This is provided for the script IsInternalHostName that checks if the detected host names are internal or external if the hosts contain the 
- `InternalHostRegex`: This is provided for the script IsInternalHostName that checks if the detected host names are internal or external. Checks if the hosts match the organization's naming convention. 

**Outputs:**

- `PANWHunting.DetectedUsers`
- `PANWHunting.DetectedInternalIPs`
- `PANWHunting.DetectedExternalIPs`
- `PANWHunting.DetectedInternalHosts`
- `PANWHunting.DetectedExternalHosts`

**Dependencies:**

- Sub-playbooks: Convert file hash to corresponding hashes, PAN-OS Query Logs For Indicators
- Scripts: IsIPInRanges, IsIntegrationAvailable, IsInternalHostName, SetAndHandleEmpty
- Commands: cdl-query-threat-logs, cdl-query-traffic-logs, cdl-query-url-logs, prisma-cloud-network-search, xdr-get-alerts


## Carbon black Protection Rapid IOC Hunting

**Product:** Carbon Black Enterprise Protection

Hunts for endpoint activity involving hash and domain IOCs, using Carbon black Protection (Bit9)


## Proactive Threat Hunting - Execute Query

**Product:** Proactive Threat Hunting

This playbook will be executed from the "Proactive Threat Hunting" layout button with the objective of executing a query that will be provided by the analyst. The playbook supports executing a query using the following integrations

**Dependencies:**

- Scripts: JsonToTable, Print, DeleteContext
- Commands: xdr-xql-generic-query, setIncident, microsoft-atp-advanced-hunting


## QRadar Get Hunting Results

**Product:** IBM QRadar

This playbook is used to sort the QRadar search results to display the IP addresses, assets, and usernames that the search provided. In addition, the results allow you to differentiate between internal and external IP addresses as well as query the QRadar assets API in order to get the assets details from the IP addresses. You can provide the QRadar fields names and the organizations' IP ranges in order to properly sort the data. The end result of the playbook will be the internal and external IP addresses detected as well as the assets and users

**Inputs:**

- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `InvestigationIPFields`: The values of these QRadar fields will be used for the playbook IP addresses outputs.
- `InvestigationUserFields`: The values of these QRadar fields will be used for the playbook user name outputs.
- `SearchResults`: The search results of an AQL search.

**Outputs:**

- `QRadar.DetectedUsers`
- `QRadar.DetectedInternalIPs`
- `QRadar.DetectedExternalIPs`
- `QRadar.DetectedInternalHosts`
- `QRadar.DetectedExternalHosts`

**Dependencies:**

- Integrations: QRadar_v3
- Scripts: Set, IsIPInRanges, SetAndHandleEmpty
- Commands: qradar-assets-list


## QRadar Indicator Hunting V2

**Product:** IBM QRadar

The Playbook queries QRadar SIEM for indicators such as file hashes, IP addresses, domains, or urls

**Inputs:**

- `MD5`: MD5 hash file or an array of hashes to search.
- `QradarMD5Field`: MD5 field to search in QRadar. If none are specified, the search will use a payload contains filter.
- `SHA1`: SHA1 hash file or an array of hashes to search.
- `QradarSHA1Field`: SHA1 field to search in QRadar. If none are specified, the search will use a payload contains filter.
- `SHA256`: SHA256 hash file or an array of hashes to search.
- `QradarSHA256Field`: SHA256 field to search in QRadar. If none are specified, the search will use a payload contains filter.
- `IPAddress`: Source or destination IP to search. Can be a single address or an array of addresses.
- `QradarIPfield`: IP field to search in QRadar. If none are specified, the search will use sourceip or destinationip (combined).
- `URLDomain`: Domain or Url can be single or an array of domain/urls to search. By default the LIKE clause is used.
- `QradarURLDomainField`: URL/Domain field to search in QRadar. If none are specified, the search will use a payload contains filter.

**Outputs:**

- `QRadar.DetectedUsers`
- `QRadar.DetectedInternalIPs`
- `QRadar.DetectedExternalIPs`
- `QRadar.DetectedInternalHosts`
- `QRadar.DetectedExternalHosts`

**Dependencies:**

- Integrations: QRadar_v3
- Scripts: IsIPInRanges, Set, SetAndHandleEmpty
- Commands: qradar-assets-list, qradar-search-retrieve-events


## Splunk Indicator Hunting

**Product:** Splunk

Queries Splunk for indicators such as file hashes, IP addresses, domains, or urls. It outputs detected users, IP addresses, and hostnames related to the indicators

**Inputs:**

- `MD5`: The MD5 hash or an array of hashes for which to search.
- `SplunkMD5Field`: The name of the fields, in Splunk, in which to find the MD5 hash. You can enter multiple field names using a comma-separated format. If no field is specified, the search uses quick
- `SHA1`: The SHA1 hash or an array of hashes on which to search.
- `SplunkSHA1Field`: The name of the fields, in Splunk, in which to find the SHA1 field. You can enter multiple field names using a comma-separated format. If no field is specified, the search uses qui
- `SHA256`: The SHA256 hash or an array of hashes on which to search.
- `SplunkSHA256Field`: The name of the fields, in Splunk, in which to find the SHA256. You can enter multiple field names using a comma-separated format. If no field is specified, the search uses quick f
- `IPAddress`: The source or destination IP address on which to search. Can be a single address or an array of addresses.
- `SplunkIPField`: The name of the fields, in Splunk, in which to find the IP addresses. You can enter multiple field names using a comma-separated format. For example, sourceip,destinationip.
- `URLDomain`: The domain or URL can be single or an array of domain/urls to search. By default the LIKE clause is used.
- `SplunkURLDomainField`: The name of the fields, in Splunk, in which to find the URL/Domain. If no field is specified, the search uses quick filter. Only one field can be used in this parameter.

**Outputs:**

- `Splunk.DetectedUsers`
- `Splunk.DetectedInternalIPs`
- `Splunk.DetectedExternalIPs`
- `Splunk.DetectedInternalHosts`
- `Splunk.DetectedExternalHosts`

**Dependencies:**

- Scripts: commentsToContext, IsIPInRanges, SetAndHandleEmpty, IsInternalHostName, Set
- Commands: splunk-search


## Suspicious Domain Hunting Incident Handling

**Product:** Suspicious Domain Hunting

This playbook process "Suspicious Domain Hunting" incidents generated by the CertStream integration

**Inputs:**

- `similarityMaxThreshold`: The minimum threshold value for malicious verdict
- `similarityMinThreshold`: The minimum threshold value for suspicious verdict
- `contactEmail`: Email address to be used as contact email when sending a takedown request email

**Dependencies:**

- Sub-playbooks: Block Domain - Generic v2, Threat Hunting - Generic
- Scripts: HttpV2, HtmlDifflibCheck, Set, SetAndHandleEmpty, IsIntegrationAvailable, imagecompare
- Commands: domain, expireIndicators, whois, url, rasterize, setIndicators, closeInvestigation


## Threat Hunting - Chronicle

**Product:** Google SecOps

Use this playbook to investigate and remediate suspicious IOC domain matches with recent activity found in the enterprise. This playbook also creates indicators for the entities fetched, as well as investigating and enriching them. Supported Integrations

**Inputs:**

- `auto_block_entities`: Autoblock the detected suspicious Domain(s) and URL(s). You can set this as 'Yes' or 'No' manually here or you can set it into a custom incident field 'Chronicle Auto Block Entitie

**Dependencies:**

- Sub-playbooks: Domain Enrichment - Generic v2, Endpoint Enrichment - Generic v2.1, Block URL - Generic, URL Enrichment - Generic v2, IP Enrichment - Generic v2, PAN-OS - Block Domain - External Dynamic List
- Integrations: Chronicle, Whois
- Scripts: ExtractDomainFromIOCDomainMatchRes, Print, ConvertDomainToURLs, ChronicleAssetIdentifierScript
- Commands: domain, whois, gcb-assets, createNewIndicator, closeInvestigation


## TIE - IOC Hunt

**Product:** McAfee Threat Intelligence Exchange

Hunt for sightings of MD5, SHA1 and/or SHA256 hashes on endpoints, using McAfee TIE (requires ePO as well). Input: Output

**Inputs:**

- `Hash`: The Hash to hunt (Could be MD5,SHA1,SHA256).Default is set to all hashes

**Outputs:**

- `McAfee.ePO.Endpoint`

**Dependencies:**

- Integrations: McAfeeTIEV2, McAfee-TIE
- Scripts: Exists
- Commands: epo-find-system, tie-file-references


## Trend Micro CAS - Indicators Hunting

**Product:** TrendAI™ Cloud App Security

In this playbook, the 'trendmicro-cas-email-sweep' command is used to automatically hunt for and detect IOCs within email messages protected by Cloud App Security (CAS). Note that multiple search values should be separated by commas only (without spaces or any special characters). Supported IOCs for this playbook: Separate searches are conducted for each type of indicator in the playbook

**Inputs:**

- `IPAddress`: A single or multiple IP address to search for within TrendMicro CAS logs. Used for both source and destination IP addresses Separate multiple search values by commas only (without 
- `CIDR`: A single or multiple IP ranges to search for within TrendMicro CAS logs. Used for both source and destination IP addresses.Separate multiple search values by commas only (without s
- `URLDomain`: Single or multiple URLs and/or domains to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `FileName`: Single or multiple file names to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA1`: Single or multiple SHA1 file hashes to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `EmailAddress`: A single or multiple email addresses to search for within TrendMicro CAS logs. Used for both recipient and sender email addresses.Separate multiple search values by commas only (wi
- `subject`: Filter messages that should be retrieved from the TrendMicro CAS based on the email subject (string).Use double quotes to search for an exact phrase, for example, "messageA message
- `start`: The start date and time from which you would like to retrieve messages from TrendMicro CAS. Use ISO 8601 time format, e.g. 2020-08-01T02:31:20Z, or 'human-readable' data, such as 1
- `end`: The end date and time specify the period of time in which messages should be retrieved from TrendMicro CAS. Use ISO 8601 time format, e.g. 2020-08-01T02:31:20Z, or 'human-readable'

**Outputs:**

- `TrendMicroCAS.HuntingResults.value`
- `TrendMicroCAS.HuntingResults.value.mail_message_delivery_time`
- `TrendMicroCAS.HuntingResults.value.mail_message_id`
- `TrendMicroCAS.HuntingResults.value.mail_unique_id`
- `TrendMicroCAS.HuntingResults.value.mailbox`
- `TrendMicroCAS.HuntingResults.value.source_ip`
- `TrendMicroCAS.HuntingResults.value.source_domain`
- `TrendMicroCAS.HuntingResults.value.mail_urls`
- `TrendMicroCAS.HuntingResults.value.mail_message_subject`
- `TrendMicroCAS.HuntingResults.value.mail_message_sender`

**Dependencies:**

- Integrations: TrendMicro Cloud App Security
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty
- Commands: trendmicro-cas-email-sweep

## Autofocus - File Indicators Hunting

**Product:** AutoFocus by Palo Alto Networks

The playbook queries the PANW Autofocus session and samples log data for file indicators such as MD5, SHA256, and SHA1 hashes. A simple search mode is used to query Autofocus based on the file indicators specified in the playbook inputs. Advanced search mode queries can also be used with multiple query parameters, but require all field names, parameters, and operators (JSON format) to be specified. We recommended using the Autofocus UI to create an advanced query, exporting it, and pasting it into the relevant playbook inputs. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `FileHash`: One or more file hashes to search for in Autofocus simple mode search. Supports MD5, SHA1, and SHA256 file hashes. Separate multiple search values by commas only (without spaces or
- `Search Type`: Which Autofocus search types should be executed. Possible values are session, sample, tag, or all. Session and sample are the recommended search types for this playbook. Sample-bas
- `Scope`: Search scope for sample and session. Possible values are industry, organization, global, or all.
- `SampleQuery`: Use the Autofocus advanced search mode to leverage a variety of query options in a sample search. Advanced search requires you to specify all field names, parameters, and operators
- `Sample first seen`: Narrow down a sample-based search by specifying the timestamp samples were first uploaded to WildFire for analysis (indicators will be searched within samples after this timestamp)
- `Sample last modified`: Narrow down a sample-based search by specifying the timestamp samples were last modified (indicators will be searched within samples after this timestamp).Specify the time in ISO 8
- `SessionQuery`: Use the Autofocus advanced search mode to leverage a variety of query options in a session search. Advanced search requires you to specify all field names, parameters, and operator
- `Sessions time before`: Narrow down a session-based search by specifying the query end timestamp (indicators will be searched within sessions before this timestamp).Specify the time in ISO 8601 format, fo
- `Sessions time after`: Narrow down a session-based search by specifying the query start timestamp (indicators will be searched within sessions after this timestamp).Specify the time in ISO 8601 format, f
- `Wildfire Verdict`: Filter results by WildFire classification assigned to samples based on properties, behaviors, and activities observed for files or email links during static and dynamic analysis.Po

**Outputs:**

- `Autofocus.Samples.HuntingResults`
- `Autofocus.Samples.HuntingResults.Created`
- `Autofocus.Samples.HuntingResults.Finished`
- `Autofocus.Samples.HuntingResults.FileName`
- `Autofocus.Samples.HuntingResults.FileType`
- `Autofocus.Samples.HuntingResults.SHA1`
- `Autofocus.Samples.HuntingResults.SHA256`
- `Autofocus.Samples.HuntingResults.MD5`
- `Autofocus.Samples.HuntingResults.Region`
- `Autofocus.Samples.HuntingResults.Tags`

**Dependencies:**

- Sub-playbooks: Autofocus Query Samples, Sessions and Tags
- Scripts: SetAndHandleEmpty


## Autofocus - Hunting And Threat Detection

**Product:** AutoFocus by Palo Alto Networks

The playbook queries the PANW Autofocus session and samples log data for file and traffic indicators, such as SHA256, SHA1, MD5, IP addresses, URLs, and domains. A simple search mode queries Autofocus based on the indicators specified in the playbook inputs. Advanced queries can also use with multiple query parameters, but require all field names, parameters, and operators (JSON format) to be specified. We recommended using the Autofocus UI to create an advanced query, exporting it, and pasting it into the relevant playbook inputs. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: One or more IP addresses to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `URLDomain`: One or more URLs and/or domains to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `MD5`: One or more MD5 file hashes to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA256`: One or more SHA256 file hashes to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA1`: One or more SHA1 file hashes to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `Search Type`: Which Autofocus search types should be executed. Possible values are session, sample, tag, or all. Session and sample are the recommended search types for this playbook. Sample-bas
- `Scope`: Search scope for sample and session. Possible values are industry, organization, global, or all.
- `SampleQuery`: Use the Autofocus advanced search mode to leverage a variety of query options within a sample search. Advanced search requires you to specify all field names, parameters, and opera
- `Sample first seen`: Narrow down a sample-based search by specifying the timestamp samples were first uploaded to WildFire for analysis (indicators will be searched within samples after this timestamp)
- `Sample last modified`: Narrow down a sample-based search by specifying the timestamp samples were last modified (indicators will be searched within samples after this timestamp).Specify the time in ISO 8

**Outputs:**

- `Autofocus.Samples.HuntingResults`
- `Autofocus.Samples.HuntingResults.Created`
- `Autofocus.Samples.HuntingResults.Finished`
- `Autofocus.Samples.HuntingResults.FileName`
- `Autofocus.Samples.HuntingResults.FileType`
- `Autofocus.Samples.HuntingResults.SHA1`
- `Autofocus.Samples.HuntingResults.SHA256`
- `Autofocus.Samples.HuntingResults.MD5`
- `Autofocus.Samples.HuntingResults.Region`
- `Autofocus.Samples.HuntingResults.Tags`

**Dependencies:**

- Sub-playbooks: Autofocus - File Indicators Hunting, Autofocus - Traffic Indicators Hunting
- Scripts: IsIntegrationAvailable


## Autofocus - Traffic Indicators Hunting

**Product:** AutoFocus by Palo Alto Networks

The playbook queries the PANW Autofocus session and samples log data for traffic indicators such as URLs, IP addresses, and domains. A simple search mode queries Autofocus based on the traffic indicators specified in the playbook inputs. Advanced search mode queries can also be used with multiple query parameters, but require all field names, parameters, and operators (JSON format) to be specified. We recommended using the Autofocus UI to create an advanced query, exporting it, and pasting it into the relevant playbook inputs. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: One or more IP addresses to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `URLDomain`: One or more URLs and/or domains to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `Search Type`: Which Autofocus search types should be executed. Possible values are session, sample, tag, or all. Session and sample are the recommended search types for this playbook. Sample-bas
- `Scope`: Search scope for sample and session. Possible values are industry, organization, or global.
- `SampleQuery`: use the Autofocus advanced search mode to leverage a variety of query options within a sample search. Advanced search requires you to specify all field names, parameters, and opera
- `Sample first seen`: Narrow down a sample-based search by specifying the timestamp samples were first uploaded to WildFire for analysis (indicators will be searched within samples after this timestamp)
- `Sample last modified`: Narrow down a sample-based search by specifying the timestamp samples were last modified (indicators will be searched within samples after this timestamp).Specify the time in ISO 8
- `SessionQuery`: Use the Autofocus advanced search mode to leverage a variety of query options in a session search. Advanced search requires you to specify all field names, parameters, and operator
- `Sessions time before`: Narrow down a session-based search by specifying the query end timestamp (indicators will be searched within sessions before this timestamp).Specify the time in ISO 8601 format, fo
- `Sessions time after`: Narrow down a session-based search by specifying the query start timestamp (indicators will be searched within sessions after this timestamp).Specify the time in ISO 8601 format, f

**Outputs:**

- `Autofocus.Samples.HuntingResults`
- `Autofocus.Samples.HuntingResults.Created`
- `Autofocus.Samples.HuntingResults.Finished`
- `Autofocus.Samples.HuntingResults.FileName`
- `Autofocus.Samples.HuntingResults.FileType`
- `Autofocus.Samples.HuntingResults.SHA1`
- `Autofocus.Samples.HuntingResults.SHA256`
- `Autofocus.Samples.HuntingResults.MD5`
- `Autofocus.Samples.HuntingResults.Region`
- `Autofocus.Samples.HuntingResults.Tags`

**Dependencies:**

- Sub-playbooks: Autofocus Query Samples, Sessions and Tags
- Scripts: SetAndHandleEmpty


## Strata Logging Service - File Indicators Hunting

**Product:** Strata Logging Service by Palo Alto Networks

This playbook queries Strata Logging Service (SLS) for file indicators, including SHA256 hashes, file names, and file types. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `SHA256`: A single or multiple SHA256 file hashes to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Filename`: A single or multiple file names to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `time_range`: An alternative to the 'start_time' and 'end_time' inputs that indicates the timeframe for the search, e.g. 1 week, 1 day, 30 minutes.When the time_range input is specified, the 'st
- `start_time`: Specify the query start time at which to perform a search within Strata Logging Service.For example, start_time="2018-04-26 00:00:00"
- `end_time`: Specify the query end time at which to perform a search within Strata Logging Service.For example, end_time="2018-04-26 00:00:00"
- `limit`: The maximum number of logs to return. Default is 10.
- `fields`: Select the fields you wish to be included in the query results. Selection can be "all" (same as *) or a comma-separated list of specific fields in the table.Separate multiple searc
- `FirewallAction`: Filter network traffic logs that should be retrieved from Strata Logging Service based on firewall action.Separate multiple search values by commas only (without spaces or any spec
- `rule_matched`: Filter network traffic logs to be retrieved from Strata Logging Service based on security policy rule names that the network traffic matches.Separate multiple search values by comm

**Outputs:**

- `CDL.HuntingResults`
- `CDL.HuntingResults.TimeGenerated`
- `CDL.HuntingResults.LogTime`
- `CDL.HuntingResults.IngestionTime`
- `CDL.HuntingResults.App`
- `CDL.HuntingResults.AppCategory`
- `CDL.HuntingResults.RiskOfApp`
- `CDL.HuntingResults.CharacteristicOfApp`
- `CDL.HuntingResults.SanctionedStateOfApp`
- `CDL.HuntingResults.SessionID`

**Dependencies:**

- Integrations: Strata Logging Service
- Scripts: SetAndHandleEmpty
- Commands: cdl-query-file-data, cdl-query-threat-logs


## Strata Logging Service - Indicators Hunting

**Product:** Strata Logging Service by Palo Alto Networks

The playbook facilitates threat hunting and detection of IOCs within Strata Logging Service logs. The playbook and sub-playbooks query Strata Logging Service for files, traffic, HTTP requests, and execution flows indicators. Note that multiple search values should be separated by commas only (without spaces or any special characters). Supported IOCs for this playbook: Separate searches are conducted for each type of indicator in the playbook

**Inputs:**

- `IPAddresses`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination IP addresses.Separate multiple search values by commas only (wit
- `URLDomain`: Single or multiple URLs and/or domains to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Geolocation`: A single or multiple country names or codes to search for within Strata Logging Service. Used for both source and destination geolocations.Separate multiple search values by commas
- `PortNumber`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination ports.Separate multiple search values by commas only (without sp
- `SHA256`: A single or multiple SHA256 file hashes to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Filename`: A single or multiple file names to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Application`: Single or multiple application names or codes to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `URI`: A single or multiple URIs to search for within Strata Logging Service.By default, a 'LIKE' search is used.Separate multiple search values by commas only (without spaces or any spec
- `start_time`: Specify the query start time at which to perform a search within Strata Logging Service.For example, start_time="2018-04-26 00:00:00"

**Outputs:**

- `CDL.HuntingResults`
- `CDL.HuntingResults.TimeGenerated`
- `CDL.HuntingResults.LogTime`
- `CDL.HuntingResults.IngestionTime`
- `CDL.HuntingResults.App`
- `CDL.HuntingResults.AppCategory`
- `CDL.HuntingResults.RiskOfApp`
- `CDL.HuntingResults.CharacteristicOfApp`
- `CDL.HuntingResults.SessionID`
- `CDL.HuntingResults.Action`

**Dependencies:**

- Sub-playbooks: Strata Logging Service - File Indicators Hunting, Strata Logging Service - Traffic Indicators Hunting
- Integrations: Strata Logging Service
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty
- Commands: cdl-query-url-logs, cdl-query-file-data


## Strata Logging Service - Traffic Indicators Hunting

**Product:** Strata Logging Service by Palo Alto Networks

This playbook queries Strata Logging Service (SLS) for traffic indicators, including IP addresses, geolocations, URLs, domains, and ports. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddresses`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination IP addresses.Separate multiple search values by commas only (wit
- `URLDomain`: Single or multiple URLs and/or domains to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Geolocation`: A single or multiple country names or codes to search for within Strata Logging Service. Used for both source and destination geolocations.Separate multiple search values by commas
- `PortNumber`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination ports.Separate multiple search values by commas only (without sp
- `time_range`: An alternative to the 'start_time' and 'end_time' inputs that indicates the timeframe for the search, e.g. 1 week, 1 day, 30 minutes.When the time_range input is specified, the 'st
- `start_time`: Specify the query start time at which to perform a search within Strata Logging Service.For example, start_time="2018-04-26 00:00:00"
- `end_time`: Specify the query end time at which to perform a search within Strata Logging Service.For example, end_time="2018-04-26 00:00:00"
- `limit`: The maximum number of logs to return. Default is 10.
- `fields`: Select the fields you wish to be included in the query results. Selection can be "all" (same as *) or a comma-separated list of specific fields in the table.Separate multiple searc
- `FirewallAction`: Filter network traffic logs that should be retrieved from Strata Logging Service based on firewall action.Separate multiple search values by commas only (without spaces or any spec

**Outputs:**

- `CDL.HuntingResults`
- `CDL.HuntingResults.TimeGenerated`
- `CDL.HuntingResults.LogTime`
- `CDL.HuntingResults.IngestionTime`
- `CDL.HuntingResults.App`
- `CDL.HuntingResults.AppCategory`
- `CDL.HuntingResults.RiskOfApp`
- `CDL.HuntingResults.CharacteristicOfApp`
- `CDL.HuntingResults.SessionID`
- `CDL.HuntingResults.Action`

**Dependencies:**

- Integrations: Strata Logging Service
- Scripts: SetAndHandleEmpty
- Commands: cdl-query-file-data, cdl-query-threat-logs, cdl-query-traffic-logs, cdl-query-url-logs


## Darkfeed Threat hunting-research

**Product:** Sixgill Darkfeed - Annual Subscription

Automatically discover and enrich indicators with the same actor and source as the triggering IOC. Search for and isolate any compromised endpoints and proactively block IOCs from entering your network

**Inputs:**

- `File`: File hash (MD5, SHA-1, SHA-256) from Darkfeed
- `URL`: URL from Darkfeed
- `Maximum number of IOCs`: Set value to the maximum number of IOCs you would like returned in searches for items from the same source and same actor
- `Query time lookup`: Set value to the number of days back in searches for IOCs with the same source and same actor
- `IP`: IP address from Darkfeed
- `Is automated endpoint isolation activated?`: Set "yes" if you would like to automatically isolate endpoints on which malicious indicators were detected
- `Is automated blocking activated?`: Set "yes" if you would like to automatically block discovered malicious indicators.
- `Domain`: Domain from Darkfeed

**Dependencies:**

- Sub-playbooks: Search Endpoints By Hash - Generic V2, Block Indicators - Generic v2, Entity Enrichment - Generic v2, Isolate Endpoint - Generic V2
- Scripts: Set, SetAndHandleEmpty, SixgillSearchIndicators, ToTable
- Commands: associateIndicatorToIncident


## Trellix Email Security Cloud - Indicators Hunting

**Product:** Trellix Email Security - Cloud

This playbook queries Trellix Email Security - Cloud for indicators such as domains, IP addresses, sender and recipient email addresses. Separate searches are conducted for each type of indicator in the playbook. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: A single or multiple IP address to search for within Trellix Email Security - Cloud logs. Used for both source and destination IP addresses.Separate multiple search values by comma
- `Domain`: Single or multiple domains to search for within Trellix Email Security - Cloud logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (withou
- `EmailAddress`: A single or multiple email addresses to search for within Trellix Email Security - Cloud logs. Used for both recipient and sender email addresses.Separate multiple search values by
- `from_email_not_in`: List of sender email addresses to be excluded.The max limit of entries is 10.Separate multiple search values by commas only (without spaces or any special characters).
- `recipients_not_in`: List of recipient email addresses to be excluded (including "cc").The max limit of entries is 10.Separate multiple search values by commas only (without spaces or any special chara
- `has_attachments`: Boolean value filter to indicate if the message has attachments.Values can be only 'true' or 'false'.
- `max_message_size`: Select the message size (in KB) based on which you wish to retrieve messages from the Trellix Email Security - Cloud server.The default value is 20 and the maximum value is 100.
- `from_accepted_date_time`: The start date and time from which you would like to retrieve messages from the Trellix Email Security - Cloud server, e.g. 2017-10-24T10:48:51.000Z.For a complete date range, spec
- `to_accepted_date_time`: The end date and time specify the period of time in which messages should be retrieved from the Trellix Email Security - Cloud server, e.g. 2017-10-24T10:48:51.000Z.For a complete 
- `last_modified_date_time`: The last date and time messages were modified in order to retrieve them from the Trellix Email Security - Cloud server. Dates and times should be accompanied by one of the followin

**Outputs:**

- `FireEyeETP.HuntingResults`
- `FireEyeETP.HuntingResults.acceptedDateTime`
- `FireEyeETP.HuntingResults.lastModifiedDateTime`
- `FireEyeETP.HuntingResults.countryCode`
- `FireEyeETP.HuntingResults.domain`
- `FireEyeETP.HuntingResults.recipientHeader`
- `FireEyeETP.HuntingResults.recipients`
- `FireEyeETP.HuntingResults.senderHeader`
- `FireEyeETP.HuntingResults.sender`
- `FireEyeETP.HuntingResults.senderSMTP`

**Dependencies:**

- Integrations: Trellix Email Security - Cloud
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable
- Commands: fireeye-etp-search-messages


## MDE - Host Advanced Hunting For Network Activity

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook uses the Microsoft Defender For Endpoint Advanced Hunting feature to hunt for host network activity

**Inputs:**

- `DeviceName`: A comma-separated list of host names to hunt.
- `DeviceID`: A comma-separated list of device IDs to hunt.
- `FileSha256`: A comma-separated list of file SHA256 hashes to hunt.

**Outputs:**

- `MicrosoftATP.HuntNetworkConnections.Result`
- `MicrosoftATP.HuntNetworkConnections.Result.external_addresses`
- `MicrosoftATP.HuntNetworkConnections.Result.dns_query`
- `MicrosoftATP.HuntNetworkConnections.Result.encoded_commands`
- `MicrosoftATP.HuntLateralMovementEvidence.Result`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.network_connections`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.smb_connections`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.credential_dumping`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.management_connection`
- `MicrosoftATP.HuntPersistenceEvidence.Result`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Scripts: UnzipFile
- Commands: microsoft-atp-advanced-hunting-persistence-evidence, microsoft-atp-advanced-hunting-network-connections, setIncident, domain, microsoft-atp-advanced-hunting-lateral-movement-evidence, ip, microsoft-atp-live-response-get-file


## MDE - Host Advanced Hunting For Persistence

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook uses the Microsoft Defender For Endpoint Advanced Hunting feature to hunt for host persistence evidence

**Inputs:**

- `FileSha256`: A comma-separated list of file SHA256 hashes to hunt.
- `DeviceName`: A comma-separated list of host names to hunt.
- `FileName`: A comma-separated list of file names to hunt.
- `DeviceID`: A comma-separated list of a device IDs to hunt.

**Outputs:**

- `MicrosoftATP.HuntPersistenceEvidence.Result`
- `MicrosoftATP.HuntPersistenceEvidence.Result.scheduled_job`
- `MicrosoftATP.HuntPersistenceEvidence.Result.registry_entry`
- `MicrosoftATP.HuntPersistenceEvidence.Result.startup_folder_changes`
- `MicrosoftATP.HuntPersistenceEvidence.Result.new_service_created`
- `MicrosoftATP.HuntPersistenceEvidence.Result.service_updated`
- `MicrosoftATP.HuntPersistenceEvidence.Result.file_replaced`
- `MicrosoftATP.HuntPersistenceEvidence.Result.new_user`
- `MicrosoftATP.HuntPersistenceEvidence.Result.new_group`
- `MicrosoftATP.HuntPersistenceEvidence.Result.group_user_change`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Commands: setIncident, microsoft-atp-advanced-hunting-persistence-evidence


## MDE - Host Advanced Hunting For Powershell Executions

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook uses the Microsoft Defender For Endpoint Advanced Hunting feature to hunt for host PowerShell executions

**Inputs:**

- `DeviceName`: A comma-separated list of host names to hunt.
- `FileName`: A comma-separated list of file names to hunt.
- `DeviceID`: A comma-separated list of device IDs to hunt.
- `FileMd5`: A comma-separated list of file MD5 hashes to hunt.
- `FileSha256`: A comma-separated list of file SHA256 hashes to hunt.
- `FileSha1`: A comma-separated list of file SHA1 hashes to hunt.

**Outputs:**

- `MicrosoftATP.HuntProcessDetails.Result`
- `MicrosoftATP.HuntProcessDetails.Result.parent_process`
- `MicrosoftATP.HuntProcessDetails.Result.grandparent_process`
- `MicrosoftATP.HuntProcessDetails.Result.process_details`
- `MicrosoftATP.HuntProcessDetails.Result.beaconing_evidence`
- `MicrosoftATP.HuntProcessDetails.Result.powershell_execution_unsigned_files`
- `MicrosoftATP.HuntProcessDetails.Result.process_excecution_powershell`
- `MicrosoftATP.FileMachine.Machines`
- `MicrosoftATP.FileMachine.Machines.ID`
- `MicrosoftATP.FileMachine.Machines.ComputerDNSName`

**Dependencies:**

- Sub-playbooks: Command-Line Analysis
- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Commands: microsoft-atp-advanced-hunting-process-details, microsoft-atp-advanced-hunting-network-connections, microsoft-atp-get-file-related-machines, setIncident


## Microsoft 365 Defender - Threat Hunting Generic

**Product:** Microsoft 365 Defender

This playbook retrieves email data based on the URLDomain, SHA256, IPAddress, and MessageID inputs. The output is a unified object with all of the retrieved emails based on the following sub-playbooks outputs: Read the playbooks' descriptions in order to get the full details

**Inputs:**

- `URLDomain`: Domain or URL to search within emails. Can be a single domain or URL, or an array of domains or URLs to search.
- `SHA256`: The SHA256 hash file or an array of hashes to search within emails.
- `IPAddress`: The source or destination IP address to search. Can be a single address or an array of IP addresses.
- `MessageID`: Message ID of the email from which the URL was clicked. Note that this can be either of the following 2 values:- The value of the header "Message-ID".- The internal ID of the messa
- `Timeout`: The time limit in seconds for the HTTP request to run.
- `SearchTimeframe`: Number of days past to search.
- `ResultsLimit`: Number of retrieved entries. Enter -1 for unlimited query.
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

- Sub-playbooks: Microsoft 365 Defender - Get Email URL Clicks, Microsoft 365 Defender - Emails Indicators Hunt
- Scripts: SetAndHandleEmpty


## Palo Alto Networks - Hunting And Threat Detection

**Product:** Comprehensive Investigation by Palo Alto Networks

This is a multipurpose playbook used for hunting and threat detection. The playbook receives inputs based on hashes, IP addresses, or domain names provided manually or from outputs by other playbooks. The playbook leverages data received by PANW products including, Strata Logging Service and Pan-OS to search for IP addresses, host names and users related to the provided indicators. The output provided by the playbook enables you to find possibly affected IP addresses, users, and endpoints

**Inputs:**

- `SHA256`: SHA256 hash of the indicator to hunt.
- `MD5`: MD5 hash of the indicator to hunt.
- `SHA1`: SHA1 hash of the indicator to hunt.
- `IPAddresses`: List of IP addresses.
- `URLDomain`: List of domains or urls.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `InternalDomainName`: The organizations internal domain name. This is provided for the script IsInternalHostName that checks if the detected host names are internal or external if the hosts contain the 
- `InternalHostRegex`: This is provided for the script IsInternalHostName that checks if the detected host names are internal or external. Checks if the hosts match the organization's naming convention. 

**Outputs:**

- `PANWHunting.DetectedUsers`
- `PANWHunting.DetectedInternalIPs`
- `PANWHunting.DetectedExternalIPs`
- `PANWHunting.DetectedInternalHosts`
- `PANWHunting.DetectedExternalHosts`

**Dependencies:**

- Sub-playbooks: Convert file hash to corresponding hashes, PAN-OS Query Logs For Indicators
- Scripts: IsIPInRanges, IsIntegrationAvailable, IsInternalHostName, SetAndHandleEmpty
- Commands: cdl-query-threat-logs, cdl-query-traffic-logs, cdl-query-url-logs, prisma-cloud-network-search, xdr-get-alerts


## Carbon black Protection Rapid IOC Hunting

**Product:** Carbon Black Enterprise Protection

Hunts for endpoint activity involving hash and domain IOCs, using Carbon black Protection (Bit9)


## Proactive Threat Hunting - Execute Query

**Product:** Proactive Threat Hunting

This playbook will be executed from the "Proactive Threat Hunting" layout button with the objective of executing a query that will be provided by the analyst. The playbook supports executing a query using the following integrations

**Dependencies:**

- Scripts: JsonToTable, Print, DeleteContext
- Commands: xdr-xql-generic-query, setIncident, microsoft-atp-advanced-hunting


## QRadar Get Hunting Results

**Product:** IBM QRadar

This playbook is used to sort the QRadar search results to display the IP addresses, assets, and usernames that the search provided. In addition, the results allow you to differentiate between internal and external IP addresses as well as query the QRadar assets API in order to get the assets details from the IP addresses. You can provide the QRadar fields names and the organizations' IP ranges in order to properly sort the data. The end result of the playbook will be the internal and external IP addresses detected as well as the assets and users

**Inputs:**

- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `InvestigationIPFields`: The values of these QRadar fields will be used for the playbook IP addresses outputs.
- `InvestigationUserFields`: The values of these QRadar fields will be used for the playbook user name outputs.
- `SearchResults`: The search results of an AQL search.

**Outputs:**

- `QRadar.DetectedUsers`
- `QRadar.DetectedInternalIPs`
- `QRadar.DetectedExternalIPs`
- `QRadar.DetectedInternalHosts`
- `QRadar.DetectedExternalHosts`

**Dependencies:**

- Integrations: QRadar_v3
- Scripts: Set, IsIPInRanges, SetAndHandleEmpty
- Commands: qradar-assets-list


## QRadar Indicator Hunting V2

**Product:** IBM QRadar

The Playbook queries QRadar SIEM for indicators such as file hashes, IP addresses, domains, or urls

**Inputs:**

- `MD5`: MD5 hash file or an array of hashes to search.
- `QradarMD5Field`: MD5 field to search in QRadar. If none are specified, the search will use a payload contains filter.
- `SHA1`: SHA1 hash file or an array of hashes to search.
- `QradarSHA1Field`: SHA1 field to search in QRadar. If none are specified, the search will use a payload contains filter.
- `SHA256`: SHA256 hash file or an array of hashes to search.
- `QradarSHA256Field`: SHA256 field to search in QRadar. If none are specified, the search will use a payload contains filter.
- `IPAddress`: Source or destination IP to search. Can be a single address or an array of addresses.
- `QradarIPfield`: IP field to search in QRadar. If none are specified, the search will use sourceip or destinationip (combined).
- `URLDomain`: Domain or Url can be single or an array of domain/urls to search. By default the LIKE clause is used.
- `QradarURLDomainField`: URL/Domain field to search in QRadar. If none are specified, the search will use a payload contains filter.

**Outputs:**

- `QRadar.DetectedUsers`
- `QRadar.DetectedInternalIPs`
- `QRadar.DetectedExternalIPs`
- `QRadar.DetectedInternalHosts`
- `QRadar.DetectedExternalHosts`

**Dependencies:**

- Integrations: QRadar_v3
- Scripts: IsIPInRanges, Set, SetAndHandleEmpty
- Commands: qradar-assets-list, qradar-search-retrieve-events


## Splunk Indicator Hunting

**Product:** Splunk

Queries Splunk for indicators such as file hashes, IP addresses, domains, or urls. It outputs detected users, IP addresses, and hostnames related to the indicators

**Inputs:**

- `MD5`: The MD5 hash or an array of hashes for which to search.
- `SplunkMD5Field`: The name of the fields, in Splunk, in which to find the MD5 hash. You can enter multiple field names using a comma-separated format. If no field is specified, the search uses quick
- `SHA1`: The SHA1 hash or an array of hashes on which to search.
- `SplunkSHA1Field`: The name of the fields, in Splunk, in which to find the SHA1 field. You can enter multiple field names using a comma-separated format. If no field is specified, the search uses qui
- `SHA256`: The SHA256 hash or an array of hashes on which to search.
- `SplunkSHA256Field`: The name of the fields, in Splunk, in which to find the SHA256. You can enter multiple field names using a comma-separated format. If no field is specified, the search uses quick f
- `IPAddress`: The source or destination IP address on which to search. Can be a single address or an array of addresses.
- `SplunkIPField`: The name of the fields, in Splunk, in which to find the IP addresses. You can enter multiple field names using a comma-separated format. For example, sourceip,destinationip.
- `URLDomain`: The domain or URL can be single or an array of domain/urls to search. By default the LIKE clause is used.
- `SplunkURLDomainField`: The name of the fields, in Splunk, in which to find the URL/Domain. If no field is specified, the search uses quick filter. Only one field can be used in this parameter.

**Outputs:**

- `Splunk.DetectedUsers`
- `Splunk.DetectedInternalIPs`
- `Splunk.DetectedExternalIPs`
- `Splunk.DetectedInternalHosts`
- `Splunk.DetectedExternalHosts`

**Dependencies:**

- Scripts: commentsToContext, IsIPInRanges, SetAndHandleEmpty, IsInternalHostName, Set
- Commands: splunk-search


## Suspicious Domain Hunting Incident Handling

**Product:** Suspicious Domain Hunting

This playbook process "Suspicious Domain Hunting" incidents generated by the CertStream integration

**Inputs:**

- `similarityMaxThreshold`: The minimum threshold value for malicious verdict
- `similarityMinThreshold`: The minimum threshold value for suspicious verdict
- `contactEmail`: Email address to be used as contact email when sending a takedown request email

**Dependencies:**

- Sub-playbooks: Block Domain - Generic v2, Threat Hunting - Generic
- Scripts: HttpV2, HtmlDifflibCheck, Set, SetAndHandleEmpty, IsIntegrationAvailable, imagecompare
- Commands: domain, expireIndicators, whois, url, rasterize, setIndicators, closeInvestigation


## Threat Hunting - Chronicle

**Product:** Google SecOps

Use this playbook to investigate and remediate suspicious IOC domain matches with recent activity found in the enterprise. This playbook also creates indicators for the entities fetched, as well as investigating and enriching them. Supported Integrations

**Inputs:**

- `auto_block_entities`: Autoblock the detected suspicious Domain(s) and URL(s). You can set this as 'Yes' or 'No' manually here or you can set it into a custom incident field 'Chronicle Auto Block Entitie

**Dependencies:**

- Sub-playbooks: Domain Enrichment - Generic v2, Endpoint Enrichment - Generic v2.1, Block URL - Generic, URL Enrichment - Generic v2, IP Enrichment - Generic v2, PAN-OS - Block Domain - External Dynamic List
- Integrations: Chronicle, Whois
- Scripts: ExtractDomainFromIOCDomainMatchRes, Print, ConvertDomainToURLs, ChronicleAssetIdentifierScript
- Commands: domain, whois, gcb-assets, createNewIndicator, closeInvestigation


## TIE - IOC Hunt

**Product:** McAfee Threat Intelligence Exchange

Hunt for sightings of MD5, SHA1 and/or SHA256 hashes on endpoints, using McAfee TIE (requires ePO as well). Input: Output

**Inputs:**

- `Hash`: The Hash to hunt (Could be MD5,SHA1,SHA256).Default is set to all hashes

**Outputs:**

- `McAfee.ePO.Endpoint`

**Dependencies:**

- Integrations: McAfeeTIEV2, McAfee-TIE
- Scripts: Exists
- Commands: epo-find-system, tie-file-references


## Trend Micro CAS - Indicators Hunting

**Product:** TrendAI™ Cloud App Security

In this playbook, the 'trendmicro-cas-email-sweep' command is used to automatically hunt for and detect IOCs within email messages protected by Cloud App Security (CAS). Note that multiple search values should be separated by commas only (without spaces or any special characters). Supported IOCs for this playbook: Separate searches are conducted for each type of indicator in the playbook

**Inputs:**

- `IPAddress`: A single or multiple IP address to search for within TrendMicro CAS logs. Used for both source and destination IP addresses Separate multiple search values by commas only (without 
- `CIDR`: A single or multiple IP ranges to search for within TrendMicro CAS logs. Used for both source and destination IP addresses.Separate multiple search values by commas only (without s
- `URLDomain`: Single or multiple URLs and/or domains to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `FileName`: Single or multiple file names to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA1`: Single or multiple SHA1 file hashes to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `EmailAddress`: A single or multiple email addresses to search for within TrendMicro CAS logs. Used for both recipient and sender email addresses.Separate multiple search values by commas only (wi
- `subject`: Filter messages that should be retrieved from the TrendMicro CAS based on the email subject (string).Use double quotes to search for an exact phrase, for example, "messageA message
- `start`: The start date and time from which you would like to retrieve messages from TrendMicro CAS. Use ISO 8601 time format, e.g. 2020-08-01T02:31:20Z, or 'human-readable' data, such as 1
- `end`: The end date and time specify the period of time in which messages should be retrieved from TrendMicro CAS. Use ISO 8601 time format, e.g. 2020-08-01T02:31:20Z, or 'human-readable'

**Outputs:**

- `TrendMicroCAS.HuntingResults.value`
- `TrendMicroCAS.HuntingResults.value.mail_message_delivery_time`
- `TrendMicroCAS.HuntingResults.value.mail_message_id`
- `TrendMicroCAS.HuntingResults.value.mail_unique_id`
- `TrendMicroCAS.HuntingResults.value.mailbox`
- `TrendMicroCAS.HuntingResults.value.source_ip`
- `TrendMicroCAS.HuntingResults.value.source_domain`
- `TrendMicroCAS.HuntingResults.value.mail_urls`
- `TrendMicroCAS.HuntingResults.value.mail_message_subject`
- `TrendMicroCAS.HuntingResults.value.mail_message_sender`

**Dependencies:**

- Integrations: TrendMicro Cloud App Security
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty
- Commands: trendmicro-cas-email-sweep

## Autofocus - File Indicators Hunting

**Product:** AutoFocus by Palo Alto Networks

The playbook queries the PANW Autofocus session and samples log data for file indicators such as MD5, SHA256, and SHA1 hashes. A simple search mode is used to query Autofocus based on the file indicators specified in the playbook inputs. Advanced search mode queries can also be used with multiple query parameters, but require all field names, parameters, and operators (JSON format) to be specified. We recommended using the Autofocus UI to create an advanced query, exporting it, and pasting it into the relevant playbook inputs. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `FileHash`: One or more file hashes to search for in Autofocus simple mode search. Supports MD5, SHA1, and SHA256 file hashes. Separate multiple search values by commas only (without spaces or
- `Search Type`: Which Autofocus search types should be executed. Possible values are session, sample, tag, or all. Session and sample are the recommended search types for this playbook. Sample-bas
- `Scope`: Search scope for sample and session. Possible values are industry, organization, global, or all.
- `SampleQuery`: Use the Autofocus advanced search mode to leverage a variety of query options in a sample search. Advanced search requires you to specify all field names, parameters, and operators
- `Sample first seen`: Narrow down a sample-based search by specifying the timestamp samples were first uploaded to WildFire for analysis (indicators will be searched within samples after this timestamp)
- `Sample last modified`: Narrow down a sample-based search by specifying the timestamp samples were last modified (indicators will be searched within samples after this timestamp).Specify the time in ISO 8
- `SessionQuery`: Use the Autofocus advanced search mode to leverage a variety of query options in a session search. Advanced search requires you to specify all field names, parameters, and operator
- `Sessions time before`: Narrow down a session-based search by specifying the query end timestamp (indicators will be searched within sessions before this timestamp).Specify the time in ISO 8601 format, fo
- `Sessions time after`: Narrow down a session-based search by specifying the query start timestamp (indicators will be searched within sessions after this timestamp).Specify the time in ISO 8601 format, f
- `Wildfire Verdict`: Filter results by WildFire classification assigned to samples based on properties, behaviors, and activities observed for files or email links during static and dynamic analysis.Po

**Outputs:**

- `Autofocus.Samples.HuntingResults`
- `Autofocus.Samples.HuntingResults.Created`
- `Autofocus.Samples.HuntingResults.Finished`
- `Autofocus.Samples.HuntingResults.FileName`
- `Autofocus.Samples.HuntingResults.FileType`
- `Autofocus.Samples.HuntingResults.SHA1`
- `Autofocus.Samples.HuntingResults.SHA256`
- `Autofocus.Samples.HuntingResults.MD5`
- `Autofocus.Samples.HuntingResults.Region`
- `Autofocus.Samples.HuntingResults.Tags`

**Dependencies:**

- Sub-playbooks: Autofocus Query Samples, Sessions and Tags
- Scripts: SetAndHandleEmpty


## Autofocus - Hunting And Threat Detection

**Product:** AutoFocus by Palo Alto Networks

The playbook queries the PANW Autofocus session and samples log data for file and traffic indicators, such as SHA256, SHA1, MD5, IP addresses, URLs, and domains. A simple search mode queries Autofocus based on the indicators specified in the playbook inputs. Advanced queries can also use with multiple query parameters, but require all field names, parameters, and operators (JSON format) to be specified. We recommended using the Autofocus UI to create an advanced query, exporting it, and pasting it into the relevant playbook inputs. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: One or more IP addresses to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `URLDomain`: One or more URLs and/or domains to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `MD5`: One or more MD5 file hashes to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA256`: One or more SHA256 file hashes to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA1`: One or more SHA1 file hashes to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `Search Type`: Which Autofocus search types should be executed. Possible values are session, sample, tag, or all. Session and sample are the recommended search types for this playbook. Sample-bas
- `Scope`: Search scope for sample and session. Possible values are industry, organization, global, or all.
- `SampleQuery`: Use the Autofocus advanced search mode to leverage a variety of query options within a sample search. Advanced search requires you to specify all field names, parameters, and opera
- `Sample first seen`: Narrow down a sample-based search by specifying the timestamp samples were first uploaded to WildFire for analysis (indicators will be searched within samples after this timestamp)
- `Sample last modified`: Narrow down a sample-based search by specifying the timestamp samples were last modified (indicators will be searched within samples after this timestamp).Specify the time in ISO 8

**Outputs:**

- `Autofocus.Samples.HuntingResults`
- `Autofocus.Samples.HuntingResults.Created`
- `Autofocus.Samples.HuntingResults.Finished`
- `Autofocus.Samples.HuntingResults.FileName`
- `Autofocus.Samples.HuntingResults.FileType`
- `Autofocus.Samples.HuntingResults.SHA1`
- `Autofocus.Samples.HuntingResults.SHA256`
- `Autofocus.Samples.HuntingResults.MD5`
- `Autofocus.Samples.HuntingResults.Region`
- `Autofocus.Samples.HuntingResults.Tags`

**Dependencies:**

- Sub-playbooks: Autofocus - File Indicators Hunting, Autofocus - Traffic Indicators Hunting
- Scripts: IsIntegrationAvailable


## Autofocus - Traffic Indicators Hunting

**Product:** AutoFocus by Palo Alto Networks

The playbook queries the PANW Autofocus session and samples log data for traffic indicators such as URLs, IP addresses, and domains. A simple search mode queries Autofocus based on the traffic indicators specified in the playbook inputs. Advanced search mode queries can also be used with multiple query parameters, but require all field names, parameters, and operators (JSON format) to be specified. We recommended using the Autofocus UI to create an advanced query, exporting it, and pasting it into the relevant playbook inputs. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: One or more IP addresses to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `URLDomain`: One or more URLs and/or domains to search for in Autofocus simple mode search.Separate multiple search values by commas only (without spaces or any special characters).
- `Search Type`: Which Autofocus search types should be executed. Possible values are session, sample, tag, or all. Session and sample are the recommended search types for this playbook. Sample-bas
- `Scope`: Search scope for sample and session. Possible values are industry, organization, or global.
- `SampleQuery`: use the Autofocus advanced search mode to leverage a variety of query options within a sample search. Advanced search requires you to specify all field names, parameters, and opera
- `Sample first seen`: Narrow down a sample-based search by specifying the timestamp samples were first uploaded to WildFire for analysis (indicators will be searched within samples after this timestamp)
- `Sample last modified`: Narrow down a sample-based search by specifying the timestamp samples were last modified (indicators will be searched within samples after this timestamp).Specify the time in ISO 8
- `SessionQuery`: Use the Autofocus advanced search mode to leverage a variety of query options in a session search. Advanced search requires you to specify all field names, parameters, and operator
- `Sessions time before`: Narrow down a session-based search by specifying the query end timestamp (indicators will be searched within sessions before this timestamp).Specify the time in ISO 8601 format, fo
- `Sessions time after`: Narrow down a session-based search by specifying the query start timestamp (indicators will be searched within sessions after this timestamp).Specify the time in ISO 8601 format, f

**Outputs:**

- `Autofocus.Samples.HuntingResults`
- `Autofocus.Samples.HuntingResults.Created`
- `Autofocus.Samples.HuntingResults.Finished`
- `Autofocus.Samples.HuntingResults.FileName`
- `Autofocus.Samples.HuntingResults.FileType`
- `Autofocus.Samples.HuntingResults.SHA1`
- `Autofocus.Samples.HuntingResults.SHA256`
- `Autofocus.Samples.HuntingResults.MD5`
- `Autofocus.Samples.HuntingResults.Region`
- `Autofocus.Samples.HuntingResults.Tags`

**Dependencies:**

- Sub-playbooks: Autofocus Query Samples, Sessions and Tags
- Scripts: SetAndHandleEmpty


## Strata Logging Service - File Indicators Hunting

**Product:** Strata Logging Service by Palo Alto Networks

This playbook queries Strata Logging Service (SLS) for file indicators, including SHA256 hashes, file names, and file types. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `SHA256`: A single or multiple SHA256 file hashes to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Filename`: A single or multiple file names to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `time_range`: An alternative to the 'start_time' and 'end_time' inputs that indicates the timeframe for the search, e.g. 1 week, 1 day, 30 minutes.When the time_range input is specified, the 'st
- `start_time`: Specify the query start time at which to perform a search within Strata Logging Service.For example, start_time="2018-04-26 00:00:00"
- `end_time`: Specify the query end time at which to perform a search within Strata Logging Service.For example, end_time="2018-04-26 00:00:00"
- `limit`: The maximum number of logs to return. Default is 10.
- `fields`: Select the fields you wish to be included in the query results. Selection can be "all" (same as *) or a comma-separated list of specific fields in the table.Separate multiple searc
- `FirewallAction`: Filter network traffic logs that should be retrieved from Strata Logging Service based on firewall action.Separate multiple search values by commas only (without spaces or any spec
- `rule_matched`: Filter network traffic logs to be retrieved from Strata Logging Service based on security policy rule names that the network traffic matches.Separate multiple search values by comm

**Outputs:**

- `CDL.HuntingResults`
- `CDL.HuntingResults.TimeGenerated`
- `CDL.HuntingResults.LogTime`
- `CDL.HuntingResults.IngestionTime`
- `CDL.HuntingResults.App`
- `CDL.HuntingResults.AppCategory`
- `CDL.HuntingResults.RiskOfApp`
- `CDL.HuntingResults.CharacteristicOfApp`
- `CDL.HuntingResults.SanctionedStateOfApp`
- `CDL.HuntingResults.SessionID`

**Dependencies:**

- Integrations: Strata Logging Service
- Scripts: SetAndHandleEmpty
- Commands: cdl-query-file-data, cdl-query-threat-logs


## Strata Logging Service - Indicators Hunting

**Product:** Strata Logging Service by Palo Alto Networks

The playbook facilitates threat hunting and detection of IOCs within Strata Logging Service logs. The playbook and sub-playbooks query Strata Logging Service for files, traffic, HTTP requests, and execution flows indicators. Note that multiple search values should be separated by commas only (without spaces or any special characters). Supported IOCs for this playbook: Separate searches are conducted for each type of indicator in the playbook

**Inputs:**

- `IPAddresses`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination IP addresses.Separate multiple search values by commas only (wit
- `URLDomain`: Single or multiple URLs and/or domains to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Geolocation`: A single or multiple country names or codes to search for within Strata Logging Service. Used for both source and destination geolocations.Separate multiple search values by commas
- `PortNumber`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination ports.Separate multiple search values by commas only (without sp
- `SHA256`: A single or multiple SHA256 file hashes to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Filename`: A single or multiple file names to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Application`: Single or multiple application names or codes to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `URI`: A single or multiple URIs to search for within Strata Logging Service.By default, a 'LIKE' search is used.Separate multiple search values by commas only (without spaces or any spec
- `start_time`: Specify the query start time at which to perform a search within Strata Logging Service.For example, start_time="2018-04-26 00:00:00"

**Outputs:**

- `CDL.HuntingResults`
- `CDL.HuntingResults.TimeGenerated`
- `CDL.HuntingResults.LogTime`
- `CDL.HuntingResults.IngestionTime`
- `CDL.HuntingResults.App`
- `CDL.HuntingResults.AppCategory`
- `CDL.HuntingResults.RiskOfApp`
- `CDL.HuntingResults.CharacteristicOfApp`
- `CDL.HuntingResults.SessionID`
- `CDL.HuntingResults.Action`

**Dependencies:**

- Sub-playbooks: Strata Logging Service - File Indicators Hunting, Strata Logging Service - Traffic Indicators Hunting
- Integrations: Strata Logging Service
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty
- Commands: cdl-query-url-logs, cdl-query-file-data


## Strata Logging Service - Traffic Indicators Hunting

**Product:** Strata Logging Service by Palo Alto Networks

This playbook queries Strata Logging Service (SLS) for traffic indicators, including IP addresses, geolocations, URLs, domains, and ports. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddresses`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination IP addresses.Separate multiple search values by commas only (wit
- `URLDomain`: Single or multiple URLs and/or domains to search for within Strata Logging Service.Separate multiple search values by commas only (without spaces or any special characters).
- `Geolocation`: A single or multiple country names or codes to search for within Strata Logging Service. Used for both source and destination geolocations.Separate multiple search values by commas
- `PortNumber`: A single or multiple IP addresses to search for within Strata Logging Service. Used for both source and destination ports.Separate multiple search values by commas only (without sp
- `time_range`: An alternative to the 'start_time' and 'end_time' inputs that indicates the timeframe for the search, e.g. 1 week, 1 day, 30 minutes.When the time_range input is specified, the 'st
- `start_time`: Specify the query start time at which to perform a search within Strata Logging Service.For example, start_time="2018-04-26 00:00:00"
- `end_time`: Specify the query end time at which to perform a search within Strata Logging Service.For example, end_time="2018-04-26 00:00:00"
- `limit`: The maximum number of logs to return. Default is 10.
- `fields`: Select the fields you wish to be included in the query results. Selection can be "all" (same as *) or a comma-separated list of specific fields in the table.Separate multiple searc
- `FirewallAction`: Filter network traffic logs that should be retrieved from Strata Logging Service based on firewall action.Separate multiple search values by commas only (without spaces or any spec

**Outputs:**

- `CDL.HuntingResults`
- `CDL.HuntingResults.TimeGenerated`
- `CDL.HuntingResults.LogTime`
- `CDL.HuntingResults.IngestionTime`
- `CDL.HuntingResults.App`
- `CDL.HuntingResults.AppCategory`
- `CDL.HuntingResults.RiskOfApp`
- `CDL.HuntingResults.CharacteristicOfApp`
- `CDL.HuntingResults.SessionID`
- `CDL.HuntingResults.Action`

**Dependencies:**

- Integrations: Strata Logging Service
- Scripts: SetAndHandleEmpty
- Commands: cdl-query-file-data, cdl-query-threat-logs, cdl-query-traffic-logs, cdl-query-url-logs


## Darkfeed Threat hunting-research

**Product:** Sixgill Darkfeed - Annual Subscription

Automatically discover and enrich indicators with the same actor and source as the triggering IOC. Search for and isolate any compromised endpoints and proactively block IOCs from entering your network

**Inputs:**

- `File`: File hash (MD5, SHA-1, SHA-256) from Darkfeed
- `URL`: URL from Darkfeed
- `Maximum number of IOCs`: Set value to the maximum number of IOCs you would like returned in searches for items from the same source and same actor
- `Query time lookup`: Set value to the number of days back in searches for IOCs with the same source and same actor
- `IP`: IP address from Darkfeed
- `Is automated endpoint isolation activated?`: Set "yes" if you would like to automatically isolate endpoints on which malicious indicators were detected
- `Is automated blocking activated?`: Set "yes" if you would like to automatically block discovered malicious indicators.
- `Domain`: Domain from Darkfeed

**Dependencies:**

- Sub-playbooks: Search Endpoints By Hash - Generic V2, Block Indicators - Generic v2, Entity Enrichment - Generic v2, Isolate Endpoint - Generic V2
- Scripts: Set, SetAndHandleEmpty, SixgillSearchIndicators, ToTable
- Commands: associateIndicatorToIncident


## Trellix Email Security Cloud - Indicators Hunting

**Product:** Trellix Email Security - Cloud

This playbook queries Trellix Email Security - Cloud for indicators such as domains, IP addresses, sender and recipient email addresses. Separate searches are conducted for each type of indicator in the playbook. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: A single or multiple IP address to search for within Trellix Email Security - Cloud logs. Used for both source and destination IP addresses.Separate multiple search values by comma
- `Domain`: Single or multiple domains to search for within Trellix Email Security - Cloud logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (withou
- `EmailAddress`: A single or multiple email addresses to search for within Trellix Email Security - Cloud logs. Used for both recipient and sender email addresses.Separate multiple search values by
- `from_email_not_in`: List of sender email addresses to be excluded.The max limit of entries is 10.Separate multiple search values by commas only (without spaces or any special characters).
- `recipients_not_in`: List of recipient email addresses to be excluded (including "cc").The max limit of entries is 10.Separate multiple search values by commas only (without spaces or any special chara
- `has_attachments`: Boolean value filter to indicate if the message has attachments.Values can be only 'true' or 'false'.
- `max_message_size`: Select the message size (in KB) based on which you wish to retrieve messages from the Trellix Email Security - Cloud server.The default value is 20 and the maximum value is 100.
- `from_accepted_date_time`: The start date and time from which you would like to retrieve messages from the Trellix Email Security - Cloud server, e.g. 2017-10-24T10:48:51.000Z.For a complete date range, spec
- `to_accepted_date_time`: The end date and time specify the period of time in which messages should be retrieved from the Trellix Email Security - Cloud server, e.g. 2017-10-24T10:48:51.000Z.For a complete 
- `last_modified_date_time`: The last date and time messages were modified in order to retrieve them from the Trellix Email Security - Cloud server. Dates and times should be accompanied by one of the followin

**Outputs:**

- `FireEyeETP.HuntingResults`
- `FireEyeETP.HuntingResults.acceptedDateTime`
- `FireEyeETP.HuntingResults.lastModifiedDateTime`
- `FireEyeETP.HuntingResults.countryCode`
- `FireEyeETP.HuntingResults.domain`
- `FireEyeETP.HuntingResults.recipientHeader`
- `FireEyeETP.HuntingResults.recipients`
- `FireEyeETP.HuntingResults.senderHeader`
- `FireEyeETP.HuntingResults.sender`
- `FireEyeETP.HuntingResults.senderSMTP`

**Dependencies:**

- Integrations: Trellix Email Security - Cloud
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable
- Commands: fireeye-etp-search-messages


## MDE - Host Advanced Hunting For Network Activity

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook uses the Microsoft Defender For Endpoint Advanced Hunting feature to hunt for host network activity

**Inputs:**

- `DeviceName`: A comma-separated list of host names to hunt.
- `DeviceID`: A comma-separated list of device IDs to hunt.
- `FileSha256`: A comma-separated list of file SHA256 hashes to hunt.

**Outputs:**

- `MicrosoftATP.HuntNetworkConnections.Result`
- `MicrosoftATP.HuntNetworkConnections.Result.external_addresses`
- `MicrosoftATP.HuntNetworkConnections.Result.dns_query`
- `MicrosoftATP.HuntNetworkConnections.Result.encoded_commands`
- `MicrosoftATP.HuntLateralMovementEvidence.Result`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.network_connections`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.smb_connections`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.credential_dumping`
- `MicrosoftATP.HuntLateralMovementEvidence.Result.management_connection`
- `MicrosoftATP.HuntPersistenceEvidence.Result`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Scripts: UnzipFile
- Commands: microsoft-atp-advanced-hunting-persistence-evidence, microsoft-atp-advanced-hunting-network-connections, setIncident, domain, microsoft-atp-advanced-hunting-lateral-movement-evidence, ip, microsoft-atp-live-response-get-file


## MDE - Host Advanced Hunting For Persistence

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook uses the Microsoft Defender For Endpoint Advanced Hunting feature to hunt for host persistence evidence

**Inputs:**

- `FileSha256`: A comma-separated list of file SHA256 hashes to hunt.
- `DeviceName`: A comma-separated list of host names to hunt.
- `FileName`: A comma-separated list of file names to hunt.
- `DeviceID`: A comma-separated list of a device IDs to hunt.

**Outputs:**

- `MicrosoftATP.HuntPersistenceEvidence.Result`
- `MicrosoftATP.HuntPersistenceEvidence.Result.scheduled_job`
- `MicrosoftATP.HuntPersistenceEvidence.Result.registry_entry`
- `MicrosoftATP.HuntPersistenceEvidence.Result.startup_folder_changes`
- `MicrosoftATP.HuntPersistenceEvidence.Result.new_service_created`
- `MicrosoftATP.HuntPersistenceEvidence.Result.service_updated`
- `MicrosoftATP.HuntPersistenceEvidence.Result.file_replaced`
- `MicrosoftATP.HuntPersistenceEvidence.Result.new_user`
- `MicrosoftATP.HuntPersistenceEvidence.Result.new_group`
- `MicrosoftATP.HuntPersistenceEvidence.Result.group_user_change`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Commands: setIncident, microsoft-atp-advanced-hunting-persistence-evidence


## MDE - Host Advanced Hunting For Powershell Executions

**Product:** Microsoft Defender for Endpoint

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook uses the Microsoft Defender For Endpoint Advanced Hunting feature to hunt for host PowerShell executions

**Inputs:**

- `DeviceName`: A comma-separated list of host names to hunt.
- `FileName`: A comma-separated list of file names to hunt.
- `DeviceID`: A comma-separated list of device IDs to hunt.
- `FileMd5`: A comma-separated list of file MD5 hashes to hunt.
- `FileSha256`: A comma-separated list of file SHA256 hashes to hunt.
- `FileSha1`: A comma-separated list of file SHA1 hashes to hunt.

**Outputs:**

- `MicrosoftATP.HuntProcessDetails.Result`
- `MicrosoftATP.HuntProcessDetails.Result.parent_process`
- `MicrosoftATP.HuntProcessDetails.Result.grandparent_process`
- `MicrosoftATP.HuntProcessDetails.Result.process_details`
- `MicrosoftATP.HuntProcessDetails.Result.beaconing_evidence`
- `MicrosoftATP.HuntProcessDetails.Result.powershell_execution_unsigned_files`
- `MicrosoftATP.HuntProcessDetails.Result.process_excecution_powershell`
- `MicrosoftATP.FileMachine.Machines`
- `MicrosoftATP.FileMachine.Machines.ID`
- `MicrosoftATP.FileMachine.Machines.ComputerDNSName`

**Dependencies:**

- Sub-playbooks: Command-Line Analysis
- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Commands: microsoft-atp-advanced-hunting-process-details, microsoft-atp-advanced-hunting-network-connections, microsoft-atp-get-file-related-machines, setIncident


## Microsoft 365 Defender - Threat Hunting Generic

**Product:** Microsoft 365 Defender

This playbook retrieves email data based on the URLDomain, SHA256, IPAddress, and MessageID inputs. The output is a unified object with all of the retrieved emails based on the following sub-playbooks outputs: Read the playbooks' descriptions in order to get the full details

**Inputs:**

- `URLDomain`: Domain or URL to search within emails. Can be a single domain or URL, or an array of domains or URLs to search.
- `SHA256`: The SHA256 hash file or an array of hashes to search within emails.
- `IPAddress`: The source or destination IP address to search. Can be a single address or an array of IP addresses.
- `MessageID`: Message ID of the email from which the URL was clicked. Note that this can be either of the following 2 values:- The value of the header "Message-ID".- The internal ID of the messa
- `Timeout`: The time limit in seconds for the HTTP request to run.
- `SearchTimeframe`: Number of days past to search.
- `ResultsLimit`: Number of retrieved entries. Enter -1 for unlimited query.
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

- Sub-playbooks: Microsoft 365 Defender - Get Email URL Clicks, Microsoft 365 Defender - Emails Indicators Hunt
- Scripts: SetAndHandleEmpty


## Palo Alto Networks - Hunting And Threat Detection

**Product:** Comprehensive Investigation by Palo Alto Networks

This is a multipurpose playbook used for hunting and threat detection. The playbook receives inputs based on hashes, IP addresses, or domain names provided manually or from outputs by other playbooks. The playbook leverages data received by PANW products including, Strata Logging Service and Pan-OS to search for IP addresses, host names and users related to the provided indicators. The output provided by the playbook enables you to find possibly affected IP addresses, users, and endpoints

**Inputs:**

- `SHA256`: SHA256 hash of the indicator to hunt.
- `MD5`: MD5 hash of the indicator to hunt.
- `SHA1`: SHA1 hash of the indicator to hunt.
- `IPAddresses`: List of IP addresses.
- `URLDomain`: List of domains or urls.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `InternalDomainName`: The organizations internal domain name. This is provided for the script IsInternalHostName that checks if the detected host names are internal or external if the hosts contain the 
- `InternalHostRegex`: This is provided for the script IsInternalHostName that checks if the detected host names are internal or external. Checks if the hosts match the organization's naming convention. 

**Outputs:**

- `PANWHunting.DetectedUsers`
- `PANWHunting.DetectedInternalIPs`
- `PANWHunting.DetectedExternalIPs`
- `PANWHunting.DetectedInternalHosts`
- `PANWHunting.DetectedExternalHosts`

**Dependencies:**

- Sub-playbooks: Convert file hash to corresponding hashes, PAN-OS Query Logs For Indicators
- Scripts: IsIPInRanges, IsIntegrationAvailable, IsInternalHostName, SetAndHandleEmpty
- Commands: cdl-query-threat-logs, cdl-query-traffic-logs, cdl-query-url-logs, prisma-cloud-network-search, xdr-get-alerts


## Carbon black Protection Rapid IOC Hunting

**Product:** Carbon Black Enterprise Protection

Hunts for endpoint activity involving hash and domain IOCs, using Carbon black Protection (Bit9)


## Proactive Threat Hunting - Execute Query

**Product:** Proactive Threat Hunting

This playbook will be executed from the "Proactive Threat Hunting" layout button with the objective of executing a query that will be provided by the analyst. The playbook supports executing a query using the following integrations

**Dependencies:**

- Scripts: JsonToTable, Print, DeleteContext
- Commands: xdr-xql-generic-query, setIncident, microsoft-atp-advanced-hunting


## QRadar Get Hunting Results

**Product:** IBM QRadar

This playbook is used to sort the QRadar search results to display the IP addresses, assets, and usernames that the search provided. In addition, the results allow you to differentiate between internal and external IP addresses as well as query the QRadar assets API in order to get the assets details from the IP addresses. You can provide the QRadar fields names and the organizations' IP ranges in order to properly sort the data. The end result of the playbook will be the internal and external IP addresses detected as well as the assets and users

**Inputs:**

- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `InvestigationIPFields`: The values of these QRadar fields will be used for the playbook IP addresses outputs.
- `InvestigationUserFields`: The values of these QRadar fields will be used for the playbook user name outputs.
- `SearchResults`: The search results of an AQL search.

**Outputs:**

- `QRadar.DetectedUsers`
- `QRadar.DetectedInternalIPs`
- `QRadar.DetectedExternalIPs`
- `QRadar.DetectedInternalHosts`
- `QRadar.DetectedExternalHosts`

**Dependencies:**

- Integrations: QRadar_v3
- Scripts: Set, IsIPInRanges, SetAndHandleEmpty
- Commands: qradar-assets-list


## QRadar Indicator Hunting V2

**Product:** IBM QRadar

The Playbook queries QRadar SIEM for indicators such as file hashes, IP addresses, domains, or urls

**Inputs:**

- `MD5`: MD5 hash file or an array of hashes to search.
- `QradarMD5Field`: MD5 field to search in QRadar. If none are specified, the search will use a payload contains filter.
- `SHA1`: SHA1 hash file or an array of hashes to search.
- `QradarSHA1Field`: SHA1 field to search in QRadar. If none are specified, the search will use a payload contains filter.
- `SHA256`: SHA256 hash file or an array of hashes to search.
- `QradarSHA256Field`: SHA256 field to search in QRadar. If none are specified, the search will use a payload contains filter.
- `IPAddress`: Source or destination IP to search. Can be a single address or an array of addresses.
- `QradarIPfield`: IP field to search in QRadar. If none are specified, the search will use sourceip or destinationip (combined).
- `URLDomain`: Domain or Url can be single or an array of domain/urls to search. By default the LIKE clause is used.
- `QradarURLDomainField`: URL/Domain field to search in QRadar. If none are specified, the search will use a payload contains filter.

**Outputs:**

- `QRadar.DetectedUsers`
- `QRadar.DetectedInternalIPs`
- `QRadar.DetectedExternalIPs`
- `QRadar.DetectedInternalHosts`
- `QRadar.DetectedExternalHosts`

**Dependencies:**

- Integrations: QRadar_v3
- Scripts: IsIPInRanges, Set, SetAndHandleEmpty
- Commands: qradar-assets-list, qradar-search-retrieve-events


## Splunk Indicator Hunting

**Product:** Splunk

Queries Splunk for indicators such as file hashes, IP addresses, domains, or urls. It outputs detected users, IP addresses, and hostnames related to the indicators

**Inputs:**

- `MD5`: The MD5 hash or an array of hashes for which to search.
- `SplunkMD5Field`: The name of the fields, in Splunk, in which to find the MD5 hash. You can enter multiple field names using a comma-separated format. If no field is specified, the search uses quick
- `SHA1`: The SHA1 hash or an array of hashes on which to search.
- `SplunkSHA1Field`: The name of the fields, in Splunk, in which to find the SHA1 field. You can enter multiple field names using a comma-separated format. If no field is specified, the search uses qui
- `SHA256`: The SHA256 hash or an array of hashes on which to search.
- `SplunkSHA256Field`: The name of the fields, in Splunk, in which to find the SHA256. You can enter multiple field names using a comma-separated format. If no field is specified, the search uses quick f
- `IPAddress`: The source or destination IP address on which to search. Can be a single address or an array of addresses.
- `SplunkIPField`: The name of the fields, in Splunk, in which to find the IP addresses. You can enter multiple field names using a comma-separated format. For example, sourceip,destinationip.
- `URLDomain`: The domain or URL can be single or an array of domain/urls to search. By default the LIKE clause is used.
- `SplunkURLDomainField`: The name of the fields, in Splunk, in which to find the URL/Domain. If no field is specified, the search uses quick filter. Only one field can be used in this parameter.

**Outputs:**

- `Splunk.DetectedUsers`
- `Splunk.DetectedInternalIPs`
- `Splunk.DetectedExternalIPs`
- `Splunk.DetectedInternalHosts`
- `Splunk.DetectedExternalHosts`

**Dependencies:**

- Scripts: commentsToContext, IsIPInRanges, SetAndHandleEmpty, IsInternalHostName, Set
- Commands: splunk-search


## Suspicious Domain Hunting Incident Handling

**Product:** Suspicious Domain Hunting

This playbook process "Suspicious Domain Hunting" incidents generated by the CertStream integration

**Inputs:**

- `similarityMaxThreshold`: The minimum threshold value for malicious verdict
- `similarityMinThreshold`: The minimum threshold value for suspicious verdict
- `contactEmail`: Email address to be used as contact email when sending a takedown request email

**Dependencies:**

- Sub-playbooks: Block Domain - Generic v2, Threat Hunting - Generic
- Scripts: HttpV2, HtmlDifflibCheck, Set, SetAndHandleEmpty, IsIntegrationAvailable, imagecompare
- Commands: domain, expireIndicators, whois, url, rasterize, setIndicators, closeInvestigation


## Threat Hunting - Chronicle

**Product:** Google SecOps

Use this playbook to investigate and remediate suspicious IOC domain matches with recent activity found in the enterprise. This playbook also creates indicators for the entities fetched, as well as investigating and enriching them. Supported Integrations

**Inputs:**

- `auto_block_entities`: Autoblock the detected suspicious Domain(s) and URL(s). You can set this as 'Yes' or 'No' manually here or you can set it into a custom incident field 'Chronicle Auto Block Entitie

**Dependencies:**

- Sub-playbooks: Domain Enrichment - Generic v2, Endpoint Enrichment - Generic v2.1, Block URL - Generic, URL Enrichment - Generic v2, IP Enrichment - Generic v2, PAN-OS - Block Domain - External Dynamic List
- Integrations: Chronicle, Whois
- Scripts: ExtractDomainFromIOCDomainMatchRes, Print, ConvertDomainToURLs, ChronicleAssetIdentifierScript
- Commands: domain, whois, gcb-assets, createNewIndicator, closeInvestigation


## TIE - IOC Hunt

**Product:** McAfee Threat Intelligence Exchange

Hunt for sightings of MD5, SHA1 and/or SHA256 hashes on endpoints, using McAfee TIE (requires ePO as well). Input: Output

**Inputs:**

- `Hash`: The Hash to hunt (Could be MD5,SHA1,SHA256).Default is set to all hashes

**Outputs:**

- `McAfee.ePO.Endpoint`

**Dependencies:**

- Integrations: McAfeeTIEV2, McAfee-TIE
- Scripts: Exists
- Commands: epo-find-system, tie-file-references


## Trend Micro CAS - Indicators Hunting

**Product:** TrendAI™ Cloud App Security

In this playbook, the 'trendmicro-cas-email-sweep' command is used to automatically hunt for and detect IOCs within email messages protected by Cloud App Security (CAS). Note that multiple search values should be separated by commas only (without spaces or any special characters). Supported IOCs for this playbook: Separate searches are conducted for each type of indicator in the playbook

**Inputs:**

- `IPAddress`: A single or multiple IP address to search for within TrendMicro CAS logs. Used for both source and destination IP addresses Separate multiple search values by commas only (without 
- `CIDR`: A single or multiple IP ranges to search for within TrendMicro CAS logs. Used for both source and destination IP addresses.Separate multiple search values by commas only (without s
- `URLDomain`: Single or multiple URLs and/or domains to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `FileName`: Single or multiple file names to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA1`: Single or multiple SHA1 file hashes to search for within TrendMicro CAS logs.Separate multiple search values by commas only (without spaces or any special characters).
- `EmailAddress`: A single or multiple email addresses to search for within TrendMicro CAS logs. Used for both recipient and sender email addresses.Separate multiple search values by commas only (wi
- `subject`: Filter messages that should be retrieved from the TrendMicro CAS based on the email subject (string).Use double quotes to search for an exact phrase, for example, "messageA message
- `start`: The start date and time from which you would like to retrieve messages from TrendMicro CAS. Use ISO 8601 time format, e.g. 2020-08-01T02:31:20Z, or 'human-readable' data, such as 1
- `end`: The end date and time specify the period of time in which messages should be retrieved from TrendMicro CAS. Use ISO 8601 time format, e.g. 2020-08-01T02:31:20Z, or 'human-readable'

**Outputs:**

- `TrendMicroCAS.HuntingResults.value`
- `TrendMicroCAS.HuntingResults.value.mail_message_delivery_time`
- `TrendMicroCAS.HuntingResults.value.mail_message_id`
- `TrendMicroCAS.HuntingResults.value.mail_unique_id`
- `TrendMicroCAS.HuntingResults.value.mailbox`
- `TrendMicroCAS.HuntingResults.value.source_ip`
- `TrendMicroCAS.HuntingResults.value.source_domain`
- `TrendMicroCAS.HuntingResults.value.mail_urls`
- `TrendMicroCAS.HuntingResults.value.mail_message_subject`
- `TrendMicroCAS.HuntingResults.value.mail_message_sender`

**Dependencies:**

- Integrations: TrendMicro Cloud App Security
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty
- Commands: trendmicro-cas-email-sweep

## Abnormal Security Event Collector

**Product:** Abnormal Security

**Kind:** integration

Abnormal Security Event Collector integration for XSIAM. This integration was integrated and tested with version 01 of Abnormal Security Event Collector

**Commands:**

- `None`:

## Alibaba Action Trail Event Collector

**Product:** Alibaba Action Trail

**Kind:** integration

Alibaba log event collector integration for XSIAM. This integration was integrated and tested with API version 0.6 of Alicloud Log Service

**Commands:**

- `None`:

## Armis Event Collector

**Product:** Armis

**Kind:** integration

Collects alerts, devices and activities from Armis resources. This integration was integrated and tested with API V.1.8 of Armis API

**Commands:**

- `None`:

## AWS - GuardDuty Event Collector

**Product:** AWS - GuardDuty

**Kind:** integration

Amazon Web Services Guard Duty Service Event Collector integration for Cortex XSIAM

**Commands:**

- `None`:

## AWS Security Hub Event Collector

**Product:** AWS - Security Hub

**Kind:** integration

An XSIAM event collector for AWS Security Hub

**Commands:**

- `None`:

## BitSight Event Collector

**Product:** Bitsight

**Kind:** integration

Use this integration to fetch BitSight security findings as events in Cortex XSIAM. This is important for organizations that wish to integrate BitSight programmatically into their security operations. When configured as a fetching integration, it will continuously fetch new findings starting from the current day. The manual bitsight-get-events command fetches findings from the last 2 days (48 hours) by default, or from an explicit date range when start_date and/or end_date are provided

**Commands:**

- `None`:

## Box Event Collector

**Product:** Box

**Kind:** integration

Collect events from Box's logs

**Commands:**

- `None`: 
- `None`:

## Carbon Black Endpoint Standard Event Collector

**Product:** Carbon Black Endpoint Standard

**Kind:** integration

Endpoint Standard (formerly called Carbon Black Defense), a Next-Generation Anti-Virus + EDR. Collect Anti-Virus & EDR alerts and Audit Log Events

**Commands:**

- `None`:

## Cisco AMP Event Collector

**Product:** Cisco AMP

**Kind:** integration

This is the Cisco AMP event collector integration for Cortex XSIAM. This integration was integrated and tested with version v1 of CiscoAMPEventCollector

**Commands:**

- `None`:

## Cisco Webex Event Collector

**Product:** Cisco Webex Teams

**Kind:** integration

Cisco Webex Event Collector fetches Events and Admin Audit Events and Security Audit Events. This integration was integrated and tested with version 1 of CiscoWebex API

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

## Code42 Event Collector

**Product:** Code42

**Kind:** integration

Code42 Insider Risk software solutions provide the right balance of transparency, technology and training to detect and appropriately respond to data risk. Use the Code42EventCollector integration to fetch file events and audit logs

**Commands:**

- `None`:

## Cohesity Helios Event Collector

**Product:** Cohesity Helios

**Kind:** integration

This is the Cohesity Helios Event Collector integration for XSIAM

**Commands:**

- `None`:

## CyberArk EPM Event Collector

**Product:** CyberArk Endpoint Privilege Manager

**Kind:** integration

Collects policy audits, admin audits, and detailed (raw) events from CyberArk Endpoint Privilege Manager (EPM). This integration was integrated and tested with version 23.12.0 of CyberArk EPM

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`:

## CyberArk Identity Event Collector

**Product:** CyberArk Identity

**Kind:** integration

CyberArk Identity log event collector integration for Cortex XSIAM. This integration was integrated and tested with version 22.4 of CyberArk Identity Event Collector

**Commands:**

- `None`: 
- `None`:

## Darktrace Event Collector

**Product:** Darktrace

**Kind:** integration

Use this integration to fetch a list of model breaches, filtered by the specified parameters. This is important for organizations that wish to integrate Darktrace programmatically into their SOC environment. The integration was integrated and tested with version v5.2 API of Darktrace

**Commands:**

- `None`:

## DeCYFIR Event Collector

**Product:** DeCYFIR

**Kind:** integration

Collects event logs from DeCYFIR for ingestion into Cortex XSIAM. Once configured, the integration periodically fetches event logs from DeCYFIR’s APIs and sends them to Cortex XSIAM for ingestion and analysis

**Commands:**

- `None`:

## Digital Guardian ARC Event Collector

**Product:** Digital Guardian

**Kind:** integration

This is the Digital Guardian ARC event collector integration for Cortex XSIAM. This integration was integrated and tested with version 3.10.0 of DigitalGuardianARCEventCollector

**Commands:**

- `None`: 
- `None`:

## Dropbox Event Collector

**Product:** Dropbox

**Kind:** integration

Collect events from Dropbox's logs. This integration was integrated and tested with version 2 of Dropbox API

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`:

## Druva Event Collector

**Product:** Druva

**Kind:** integration

This is the Druva event collector integration for Cortex XSIAM

**Commands:**

- `None`:

## Duo Event Collector

**Product:** DUO Admin

**Kind:** integration

Collects Auth and Audit events for Duo using the API

**Commands:**

- `None`:

## Elasticsearch Event Collector

**Product:** Elasticsearch

**Kind:** integration

Elasticsearch Event Collector integration is used to search for and analyze data in real time. Supports version 6 and later

**Commands:**

- `None`:

## ExtraHop Reveal(x) Event Collector

**Product:** ExtraHop Reveal(x)

**Kind:** integration

ExtraHop Reveal(x) is a network detection and response solution that provides complete visibility of network communications at enterprise scale, real-time threat detections backed by machine learning, and guided investigation workflows that simplify response

**Commands:**

- `None`:

## Trellix Email Security - Cloud Event Collector

**Product:** Trellix Email Security - Cloud

**Kind:** integration

Use this integration to fetch email security incidents from Trellix Email Security - Cloud as XSIAM events

**Commands:**

- `None`:

## FireEye HX Event Collector

**Product:** FireEye HX

**Kind:** integration

Palo Alto Networks FireEye HX Event Collector integration for XSIAM

**Commands:**

- `None`:

## Forcepoint DLP Event Collector (Beta)

**Product:** Forcepoint DLP

**Kind:** integration

Use this integration to fetch security incidents from Forcepoint DLP as Cortex XSIAM events

**Commands:**

- `None`:

## Generic API Event Collector (Beta)

**Product:** GenericAPIEventCollector

**Kind:** integration

The Generic API Event Collector allows you to ingest data from any API endpoint into Cortex. By configuring this collector, you can gather data from various systems and bring it into the Cortex ecosystem for better analysis and correlation. Note: This pack is currently in Beta, and as such, it may be subject to future changes and may not work on all types of APIs and Authentication

**Commands:**

- `None`: 
- `None`:

## Genetec Security Center Event Collector

**Product:** Genetec Security Center

**Kind:** integration

Security Center is the foundation of our unified security portfolio. It lets you connect your security at your own pace, starting with a single core system. Even if you're only interested in upgrading your video surveillance or access control, taking the next step is easy

**Commands:**

- `None`:

## GitGuardian Event Collector

**Product:** GitGuardian

**Kind:** integration

This is the GitGuardian event collector integration for Cortex XSIAM. This integration was integrated and tested with version 1.0.0 of GitGuardianEventCollector

**Commands:**

- `None`:

## GitLab Event Collector

**Product:** GitLab

**Kind:** integration

An event collector for GitLab audit events using Gitlab's API. Audit events API documentation

## GitHub Event Collector

**Product:** GitHub

**Kind:** integration

**Commands:**

- `None`:

## HelloWorld Event Collector

**Product:** HelloWorld

**Kind:** integration

This is the Hello World event collector integration for XSIAM

**Commands:**

- `None`:

## HPE Aruba Central Event Collector

**Product:** HPE Aruba Central

**Kind:** integration

This is the Aruba Central event collector integration for Cortex XSIAM

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`:

## Infoblox BloxOne Threat Defense Event Collector

**Product:** Infoblox Threat Defense with DDI

**Kind:** integration

BloxOne Threat Defense is a hybrid cybersecurity solution that leverages DNS as the first line of defense to detect and block cyber threats

**Commands:**

- `None`:

## Ironscales Event Collector

**Product:** Ironscales Event Collector

**Kind:** integration

Use this integration to fetch email security incidents from Ironscales as XSIAM events

**Commands:**

- `None`:

## Jamf Protect Event Collector

**Product:** JamfProtect

**Kind:** integration

Use this integration to fetch audit logs events, alerts events and computers assets from Jamf Protect to Cortex XSIAM

**Commands:**

- `None`: 
- `None`:

## Jira Event Collector

**Product:** Atlassian Jira

**Kind:** integration

This integration was integrated and tested with version 3 of Jira Event Collector rest API

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`:

## KnowBe4 KSAT Event Collector

**Product:** KSAT

**Kind:** integration

Allows you to push and pull your external data to and from the KnowBe4 KSAT (Security Awareness Training) console. For subscription levels and pricing, see the KnowBe4 Security Awareness Training pricing page

**Commands:**

- `None`: 
- `None`:

## Microsoft Defender for Cloud Apps Event Collector

**Product:** Microsoft Defender for Cloud Apps

**Kind:** integration

Microsoft Defender for Cloud Apps Event Collector integration

**Commands:**

- `None`: 
- `None`:

## Microsoft Defender for Cloud Event Collector

**Product:** Microsoft Defender for Cloud

**Kind:** integration

XSIAM collector for Microsoft Defender for Cloud alerts

## Mimecast Event Collector v2

**Product:** Mimecast

**Kind:** integration

**Commands:**

- `None`:

## NetBox Event Collector

**Product:** NetBox

**Kind:** integration

This is the NetBox event collector integration for Cortex XSIAM. This integration was integrated and tested with version 3.0 and above of NetBox API

**Commands:**

- `None`: 
- `None`: 
- `None`:

## Netskope Event Collector v2

**Product:** Netskope

**Kind:** integration

**Commands:**

- `None`: 
- `None`:

## Okta Auth0 Event Collector

**Product:** Okta Auth0

**Kind:** integration

Okta Auth0 logs event collector integration for Cortex XSIAM. This integration was integrated and tested with version 2.0 of Okta Auth0. Please see the Okta Auth0 rate limit policy

**Commands:**

- `None`:

## Okta Event Collector

**Product:** Okta

**Kind:** integration

Collects the events log for authentication and Audit provided by Okta admin API

**Commands:**

- `None`:

## OneLogin Event Collector

**Product:** OneLogin

**Kind:** integration

Simple customer authentication and streamlined workforce identity operations

**Commands:**

- `None`:

## Oracle Cloud Infrastructure Event Collector

**Product:** Oracle Cloud Infrastructure (OCI)

**Kind:** integration

This integration fetches audit log events from an Oracle Cloud Infrastructure resources. Audit log events can be used for security audits, to track usage of and changes to Oracle Cloud Infrastructure resources, and to help ensure compliance with standards or regulations

## Orca Event Collector

**Product:** Orca

**Kind:** integration

Orca Security event collector integration for Cortex XSIAM. This integration was integrated and tested with version 0.1.0 of Orca Event Collector

**Commands:**

- `None`:

## Proofpoint Email Security Event Collector

**Product:** Proofpoint Email Security

**Kind:** integration

Collects events for Proofpoint using the streaming API. This integration was integrated and tested Proofpoint Email Security

**Commands:**

- `None`: 
- `None`:

## Proofpoint Threat Response Event Collector

**Product:** Proofpoint Threat Response

**Kind:** integration

Use the Proofpoint Threat Response integration to orchestrate and automate incident response

**Commands:**

- `None`:

## Recorded Future Event Collector

**Product:** Recorded Future Intelligence

**Kind:** integration

This integration fetches alerts from Recorded Future. This integration was integrated and tested with version 2 of the Recorded Future API

**Commands:**

- `None`:

## ReliaQuest GreyMatter DRP Event Collector

**Product:** ReliaQuest Digital Risk Protection

**Kind:** integration

ReliaQuest GreyMatter DRP Event Collector minimizes digital risk by identifying unwanted exposure and protecting against external threats. The award-winning SearchLight solution provides ongoing monitoring of a customer's unique assets and exposure across the open, deep, and dark web. This enables clients to detect data loss, brand impersonation, infrastructure risks, cyber threats, and much more. This integration fetches event items which can be either incident/alerts, for more information refer here

**Commands:**

- `None`:

## RunZero Event Collector

**Product:** RunZero

**Kind:** integration

This is the RunZero event collector integration for XSIAM. This integration was integrated and tested with version 3.3.0 of RunZero Event Collector

**Commands:**

- `None`:

## SaaS Security Event Collector

**Product:** SaaS Security by Palo Alto Networks

**Kind:** integration

SaaS Security is an integrated CASB (Cloud Access Security Broker) solution that helps Security teams like yours meet the challenges of

**Commands:**

- `None`: 
- `None`:

## Thales SafeNet Trusted Access Event Collector

**Product:** Thales SafeNet Trusted Access

**Kind:** integration

Retrieve access, authentication, and audit logs and stores them in a Security Information and Event Management (SIEM) system, local repository, or syslog file server. You can retrieve the logs only for the tenant that is associated with the API key, or for a direct or delegated child of that tenant

**Commands:**

- `None`: 
- `None`:

## SailPoint IdentityNow Event Collector

**Product:** SailPoint IdentityNow

**Kind:** integration

This is the SailPoint IdentityNow event collector integration for Cortex XSIAM. This integration was integrated and tested with version 3 of SailPoint API

**Commands:**

- `None`:

## SecurityScorecard Event Collector

**Product:** SecurityScorecard

**Kind:** integration

**Commands:**

- `None`: 
- `None`:

## ServiceNow Event Collector

**Product:** ServiceNow

**Kind:** integration

Use this integration to fetch audit, case, syslog transactions, and outbound HTTP logs from ServiceNow as Cortex XSIAM events. This integration was integrated and tested with Vancouver version of ServiceNow API

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

## Slack Event Collector

**Product:** Slack

**Kind:** integration

Slack logs event collector integration for XSIAM. This integration was integrated and tested with version v1 of Slack Audit Logs API

**Commands:**

- `None`: 
- `None`:

## Symantec Cloud Secure Web Gateway Event Collector

**Product:** Symantec Cloud Secure Web Gateway

**Kind:** integration

Palo Alto Networks Symantec Cloud Secure Web Gateway Event Collector integration for XSIAM

## Symantec CloudSOC Event Collector

**Product:** SymantecCloudSOC

**Kind:** integration

Gets Events from Symantec CloudSOC. This integration was integrated and tested with version 3.157 of Symantec CloudSOC

**Commands:**

- `None`:

## TeamViewer Event Collector

**Product:** TeamViewer

**Kind:** integration

TeamViewer event collector integration for Cortex XSIAM. This integration was integrated and tested with version 15.40 of TeamViewer. User access token scope: Event logging - Allow requesting all event logs. A Tensor license is required

**Commands:**

- `None`:

## Trend Micro Email Security Event Collector

**Product:** Trend Micro Email Security

**Kind:** integration

Palo Alto Networks Trend Micro Email Security Event Collector integration for XSIAM

**Commands:**

- `None`:

## TrendAI Vision One™ Event Collector

**Product:** TrendAI Vision One™

**Kind:** integration

Important: This integration is supported by Palo Alto Networks. Palo Alto Networks TrendAI Vision One™ Event Collector integration for Cortex XSIAM collects the Workbench, Observed Attack Techniques, Search Detections and Audit logs. TrendAI Vision One™ is a purpose-built threat defense platform that provides added value and new benefits beyond XDR solutions, allowing you to see more and respond faster. Providing deep and broad extended detection and response (XDR) capabilities that collect and automatically correlate data across multiple security layers—email, endpoints, servers, cloud workloads, and networks—TrendAI Vision One™ prevents the majority of attacks with automated protection

**Commands:**

- `None`:

## Vectra AI Event Collector

**Product:** Vectra AI

**Kind:** integration

Collects Vectra Detections and Audits into XSIAM Events. This integration was integrated and tested with version 2.2 of Vectra

**Commands:**

- `None`:

## VeloCloud Event Collector

**Product:** VeloCloud

**Kind:** integration

Collects events from the VeloCloud API. This integration was integrated and tested with VeloCloud as of 2025-10-06

**Commands:**

- `None`:

## WithSecure Event Collector

**Product:** WithSecure

**Kind:** integration

WithSecure event collector integration for Cortex XSIAM. This integration was integrated and tested with version 1.0 of WithSecure API

**Commands:**

- `None`: 
- `None`:

## Workday Event Collector

**Product:** Workday

**Kind:** integration

Use Workday Event Collector integration to get activity loggings from Workday. This integration was integrated and tested with API v1

**Commands:**

- `None`: 
- `None`:

## Workday Sign On Event Collector

**Product:** Workday

**Kind:** integration

Use the Workday Sign On Event Collector integration to get sign on logs from Workday. This integration was integrated and tested with version v37.0 of Workday Sign On Event Collector

**Commands:**

- `None`:

## Zoom Event Collector

**Product:** Zoom

**Kind:** integration

This is the Zoom event collector integration for Cortex XSIAM. This integration was integrated and tested with version 2.0.0 of Zoom

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`:

## Abnormal Security Event Collector

**Product:** Abnormal Security

**Kind:** integration

Abnormal Security Event Collector integration for XSIAM. This integration was integrated and tested with version 01 of Abnormal Security Event Collector

**Commands:**

- `None`:

## Alibaba Action Trail Event Collector

**Product:** Alibaba Action Trail

**Kind:** integration

Alibaba log event collector integration for XSIAM. This integration was integrated and tested with API version 0.6 of Alicloud Log Service

**Commands:**

- `None`:

## Armis Event Collector

**Product:** Armis

**Kind:** integration

Collects alerts, devices and activities from Armis resources. This integration was integrated and tested with API V.1.8 of Armis API

**Commands:**

- `None`:

## AWS - GuardDuty Event Collector

**Product:** AWS - GuardDuty

**Kind:** integration

Amazon Web Services Guard Duty Service Event Collector integration for Cortex XSIAM

**Commands:**

- `None`:

## AWS Security Hub Event Collector

**Product:** AWS - Security Hub

**Kind:** integration

An XSIAM event collector for AWS Security Hub

**Commands:**

- `None`:

## BitSight Event Collector

**Product:** Bitsight

**Kind:** integration

Use this integration to fetch BitSight security findings as events in Cortex XSIAM. This is important for organizations that wish to integrate BitSight programmatically into their security operations. When configured as a fetching integration, it will continuously fetch new findings starting from the current day. The manual bitsight-get-events command fetches findings from the last 2 days (48 hours) by default, or from an explicit date range when start_date and/or end_date are provided

**Commands:**

- `None`:

## Box Event Collector

**Product:** Box

**Kind:** integration

Collect events from Box's logs

**Commands:**

- `None`: 
- `None`:

## Carbon Black Endpoint Standard Event Collector

**Product:** Carbon Black Endpoint Standard

**Kind:** integration

Endpoint Standard (formerly called Carbon Black Defense), a Next-Generation Anti-Virus + EDR. Collect Anti-Virus & EDR alerts and Audit Log Events

**Commands:**

- `None`:

## Cisco AMP Event Collector

**Product:** Cisco AMP

**Kind:** integration

This is the Cisco AMP event collector integration for Cortex XSIAM. This integration was integrated and tested with version v1 of CiscoAMPEventCollector

**Commands:**

- `None`:

## Cisco Webex Event Collector

**Product:** Cisco Webex Teams

**Kind:** integration

Cisco Webex Event Collector fetches Events and Admin Audit Events and Security Audit Events. This integration was integrated and tested with version 1 of CiscoWebex API

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

## Code42 Event Collector

**Product:** Code42

**Kind:** integration

Code42 Insider Risk software solutions provide the right balance of transparency, technology and training to detect and appropriately respond to data risk. Use the Code42EventCollector integration to fetch file events and audit logs

**Commands:**

- `None`:

## Cohesity Helios Event Collector

**Product:** Cohesity Helios

**Kind:** integration

This is the Cohesity Helios Event Collector integration for XSIAM

**Commands:**

- `None`:

## CyberArk EPM Event Collector

**Product:** CyberArk Endpoint Privilege Manager

**Kind:** integration

Collects policy audits, admin audits, and detailed (raw) events from CyberArk Endpoint Privilege Manager (EPM). This integration was integrated and tested with version 23.12.0 of CyberArk EPM

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`:

## CyberArk Identity Event Collector

**Product:** CyberArk Identity

**Kind:** integration

CyberArk Identity log event collector integration for Cortex XSIAM. This integration was integrated and tested with version 22.4 of CyberArk Identity Event Collector

**Commands:**

- `None`: 
- `None`:

## Darktrace Event Collector

**Product:** Darktrace

**Kind:** integration

Use this integration to fetch a list of model breaches, filtered by the specified parameters. This is important for organizations that wish to integrate Darktrace programmatically into their SOC environment. The integration was integrated and tested with version v5.2 API of Darktrace

**Commands:**

- `None`:

## DeCYFIR Event Collector

**Product:** DeCYFIR

**Kind:** integration

Collects event logs from DeCYFIR for ingestion into Cortex XSIAM. Once configured, the integration periodically fetches event logs from DeCYFIR’s APIs and sends them to Cortex XSIAM for ingestion and analysis

**Commands:**

- `None`:

## Digital Guardian ARC Event Collector

**Product:** Digital Guardian

**Kind:** integration

This is the Digital Guardian ARC event collector integration for Cortex XSIAM. This integration was integrated and tested with version 3.10.0 of DigitalGuardianARCEventCollector

**Commands:**

- `None`: 
- `None`:

## Dropbox Event Collector

**Product:** Dropbox

**Kind:** integration

Collect events from Dropbox's logs. This integration was integrated and tested with version 2 of Dropbox API

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`:

## Druva Event Collector

**Product:** Druva

**Kind:** integration

This is the Druva event collector integration for Cortex XSIAM

**Commands:**

- `None`:

## Duo Event Collector

**Product:** DUO Admin

**Kind:** integration

Collects Auth and Audit events for Duo using the API

**Commands:**

- `None`:

## Elasticsearch Event Collector

**Product:** Elasticsearch

**Kind:** integration

Elasticsearch Event Collector integration is used to search for and analyze data in real time. Supports version 6 and later

**Commands:**

- `None`:

## ExtraHop Reveal(x) Event Collector

**Product:** ExtraHop Reveal(x)

**Kind:** integration

ExtraHop Reveal(x) is a network detection and response solution that provides complete visibility of network communications at enterprise scale, real-time threat detections backed by machine learning, and guided investigation workflows that simplify response

**Commands:**

- `None`:

## Trellix Email Security - Cloud Event Collector

**Product:** Trellix Email Security - Cloud

**Kind:** integration

Use this integration to fetch email security incidents from Trellix Email Security - Cloud as XSIAM events

**Commands:**

- `None`:

## FireEye HX Event Collector

**Product:** FireEye HX

**Kind:** integration

Palo Alto Networks FireEye HX Event Collector integration for XSIAM

**Commands:**

- `None`:

## Forcepoint DLP Event Collector (Beta)

**Product:** Forcepoint DLP

**Kind:** integration

Use this integration to fetch security incidents from Forcepoint DLP as Cortex XSIAM events

**Commands:**

- `None`:

## Generic API Event Collector (Beta)

**Product:** GenericAPIEventCollector

**Kind:** integration

The Generic API Event Collector allows you to ingest data from any API endpoint into Cortex. By configuring this collector, you can gather data from various systems and bring it into the Cortex ecosystem for better analysis and correlation. Note: This pack is currently in Beta, and as such, it may be subject to future changes and may not work on all types of APIs and Authentication

**Commands:**

- `None`: 
- `None`:

## Genetec Security Center Event Collector

**Product:** Genetec Security Center

**Kind:** integration

Security Center is the foundation of our unified security portfolio. It lets you connect your security at your own pace, starting with a single core system. Even if you're only interested in upgrading your video surveillance or access control, taking the next step is easy

**Commands:**

- `None`:

## GitGuardian Event Collector

**Product:** GitGuardian

**Kind:** integration

This is the GitGuardian event collector integration for Cortex XSIAM. This integration was integrated and tested with version 1.0.0 of GitGuardianEventCollector

**Commands:**

- `None`:

## GitLab Event Collector

**Product:** GitLab

**Kind:** integration

An event collector for GitLab audit events using Gitlab's API. Audit events API documentation

## GitHub Event Collector

**Product:** GitHub

**Kind:** integration

**Commands:**

- `None`:

## HelloWorld Event Collector

**Product:** HelloWorld

**Kind:** integration

This is the Hello World event collector integration for XSIAM

**Commands:**

- `None`:

## HPE Aruba Central Event Collector

**Product:** HPE Aruba Central

**Kind:** integration

This is the Aruba Central event collector integration for Cortex XSIAM

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`:

## Infoblox BloxOne Threat Defense Event Collector

**Product:** Infoblox Threat Defense with DDI

**Kind:** integration

BloxOne Threat Defense is a hybrid cybersecurity solution that leverages DNS as the first line of defense to detect and block cyber threats

**Commands:**

- `None`:

## Ironscales Event Collector

**Product:** Ironscales Event Collector

**Kind:** integration

Use this integration to fetch email security incidents from Ironscales as XSIAM events

**Commands:**

- `None`:

## Jamf Protect Event Collector

**Product:** JamfProtect

**Kind:** integration

Use this integration to fetch audit logs events, alerts events and computers assets from Jamf Protect to Cortex XSIAM

**Commands:**

- `None`: 
- `None`:

## Jira Event Collector

**Product:** Atlassian Jira

**Kind:** integration

This integration was integrated and tested with version 3 of Jira Event Collector rest API

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`:

## KnowBe4 KSAT Event Collector

**Product:** KSAT

**Kind:** integration

Allows you to push and pull your external data to and from the KnowBe4 KSAT (Security Awareness Training) console. For subscription levels and pricing, see the KnowBe4 Security Awareness Training pricing page

**Commands:**

- `None`: 
- `None`:

## Microsoft Defender for Cloud Apps Event Collector

**Product:** Microsoft Defender for Cloud Apps

**Kind:** integration

Microsoft Defender for Cloud Apps Event Collector integration

**Commands:**

- `None`: 
- `None`:

## Microsoft Defender for Cloud Event Collector

**Product:** Microsoft Defender for Cloud

**Kind:** integration

XSIAM collector for Microsoft Defender for Cloud alerts

## Mimecast Event Collector v2

**Product:** Mimecast

**Kind:** integration

**Commands:**

- `None`:

## NetBox Event Collector

**Product:** NetBox

**Kind:** integration

This is the NetBox event collector integration for Cortex XSIAM. This integration was integrated and tested with version 3.0 and above of NetBox API

**Commands:**

- `None`: 
- `None`: 
- `None`:

## Netskope Event Collector v2

**Product:** Netskope

**Kind:** integration

**Commands:**

- `None`: 
- `None`:

## Okta Auth0 Event Collector

**Product:** Okta Auth0

**Kind:** integration

Okta Auth0 logs event collector integration for Cortex XSIAM. This integration was integrated and tested with version 2.0 of Okta Auth0. Please see the Okta Auth0 rate limit policy

**Commands:**

- `None`:

## Okta Event Collector

**Product:** Okta

**Kind:** integration

Collects the events log for authentication and Audit provided by Okta admin API

**Commands:**

- `None`:

## OneLogin Event Collector

**Product:** OneLogin

**Kind:** integration

Simple customer authentication and streamlined workforce identity operations

**Commands:**

- `None`:

## Oracle Cloud Infrastructure Event Collector

**Product:** Oracle Cloud Infrastructure (OCI)

**Kind:** integration

This integration fetches audit log events from an Oracle Cloud Infrastructure resources. Audit log events can be used for security audits, to track usage of and changes to Oracle Cloud Infrastructure resources, and to help ensure compliance with standards or regulations

## Orca Event Collector

**Product:** Orca

**Kind:** integration

Orca Security event collector integration for Cortex XSIAM. This integration was integrated and tested with version 0.1.0 of Orca Event Collector

**Commands:**

- `None`:

## Proofpoint Email Security Event Collector

**Product:** Proofpoint Email Security

**Kind:** integration

Collects events for Proofpoint using the streaming API. This integration was integrated and tested Proofpoint Email Security

**Commands:**

- `None`: 
- `None`:

## Proofpoint Threat Response Event Collector

**Product:** Proofpoint Threat Response

**Kind:** integration

Use the Proofpoint Threat Response integration to orchestrate and automate incident response

**Commands:**

- `None`:

## Recorded Future Event Collector

**Product:** Recorded Future Intelligence

**Kind:** integration

This integration fetches alerts from Recorded Future. This integration was integrated and tested with version 2 of the Recorded Future API

**Commands:**

- `None`:

## ReliaQuest GreyMatter DRP Event Collector

**Product:** ReliaQuest Digital Risk Protection

**Kind:** integration

ReliaQuest GreyMatter DRP Event Collector minimizes digital risk by identifying unwanted exposure and protecting against external threats. The award-winning SearchLight solution provides ongoing monitoring of a customer's unique assets and exposure across the open, deep, and dark web. This enables clients to detect data loss, brand impersonation, infrastructure risks, cyber threats, and much more. This integration fetches event items which can be either incident/alerts, for more information refer here

**Commands:**

- `None`:

## RunZero Event Collector

**Product:** RunZero

**Kind:** integration

This is the RunZero event collector integration for XSIAM. This integration was integrated and tested with version 3.3.0 of RunZero Event Collector

**Commands:**

- `None`:

## SaaS Security Event Collector

**Product:** SaaS Security by Palo Alto Networks

**Kind:** integration

SaaS Security is an integrated CASB (Cloud Access Security Broker) solution that helps Security teams like yours meet the challenges of

**Commands:**

- `None`: 
- `None`:

## Thales SafeNet Trusted Access Event Collector

**Product:** Thales SafeNet Trusted Access

**Kind:** integration

Retrieve access, authentication, and audit logs and stores them in a Security Information and Event Management (SIEM) system, local repository, or syslog file server. You can retrieve the logs only for the tenant that is associated with the API key, or for a direct or delegated child of that tenant

**Commands:**

- `None`: 
- `None`:

## SailPoint IdentityNow Event Collector

**Product:** SailPoint IdentityNow

**Kind:** integration

This is the SailPoint IdentityNow event collector integration for Cortex XSIAM. This integration was integrated and tested with version 3 of SailPoint API

**Commands:**

- `None`:

## SecurityScorecard Event Collector

**Product:** SecurityScorecard

**Kind:** integration

**Commands:**

- `None`: 
- `None`:

## ServiceNow Event Collector

**Product:** ServiceNow

**Kind:** integration

Use this integration to fetch audit, case, syslog transactions, and outbound HTTP logs from ServiceNow as Cortex XSIAM events. This integration was integrated and tested with Vancouver version of ServiceNow API

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

## Slack Event Collector

**Product:** Slack

**Kind:** integration

Slack logs event collector integration for XSIAM. This integration was integrated and tested with version v1 of Slack Audit Logs API

**Commands:**

- `None`: 
- `None`:

## Symantec Cloud Secure Web Gateway Event Collector

**Product:** Symantec Cloud Secure Web Gateway

**Kind:** integration

Palo Alto Networks Symantec Cloud Secure Web Gateway Event Collector integration for XSIAM

## Symantec CloudSOC Event Collector

**Product:** SymantecCloudSOC

**Kind:** integration

Gets Events from Symantec CloudSOC. This integration was integrated and tested with version 3.157 of Symantec CloudSOC

**Commands:**

- `None`:

## TeamViewer Event Collector

**Product:** TeamViewer

**Kind:** integration

TeamViewer event collector integration for Cortex XSIAM. This integration was integrated and tested with version 15.40 of TeamViewer. User access token scope: Event logging - Allow requesting all event logs. A Tensor license is required

**Commands:**

- `None`:

## Trend Micro Email Security Event Collector

**Product:** Trend Micro Email Security

**Kind:** integration

Palo Alto Networks Trend Micro Email Security Event Collector integration for XSIAM

**Commands:**

- `None`:

## TrendAI Vision One™ Event Collector

**Product:** TrendAI Vision One™

**Kind:** integration

Important: This integration is supported by Palo Alto Networks. Palo Alto Networks TrendAI Vision One™ Event Collector integration for Cortex XSIAM collects the Workbench, Observed Attack Techniques, Search Detections and Audit logs. TrendAI Vision One™ is a purpose-built threat defense platform that provides added value and new benefits beyond XDR solutions, allowing you to see more and respond faster. Providing deep and broad extended detection and response (XDR) capabilities that collect and automatically correlate data across multiple security layers—email, endpoints, servers, cloud workloads, and networks—TrendAI Vision One™ prevents the majority of attacks with automated protection

**Commands:**

- `None`:

## Vectra AI Event Collector

**Product:** Vectra AI

**Kind:** integration

Collects Vectra Detections and Audits into XSIAM Events. This integration was integrated and tested with version 2.2 of Vectra

**Commands:**

- `None`:

## VeloCloud Event Collector

**Product:** VeloCloud

**Kind:** integration

Collects events from the VeloCloud API. This integration was integrated and tested with VeloCloud as of 2025-10-06

**Commands:**

- `None`:

## WithSecure Event Collector

**Product:** WithSecure

**Kind:** integration

WithSecure event collector integration for Cortex XSIAM. This integration was integrated and tested with version 1.0 of WithSecure API

**Commands:**

- `None`: 
- `None`:

## Workday Event Collector

**Product:** Workday

**Kind:** integration

Use Workday Event Collector integration to get activity loggings from Workday. This integration was integrated and tested with API v1

**Commands:**

- `None`: 
- `None`:

## Workday Sign On Event Collector

**Product:** Workday

**Kind:** integration

Use the Workday Sign On Event Collector integration to get sign on logs from Workday. This integration was integrated and tested with version v37.0 of Workday Sign On Event Collector

**Commands:**

- `None`:

## Zoom Event Collector

**Product:** Zoom

**Kind:** integration

This is the Zoom event collector integration for Cortex XSIAM. This integration was integrated and tested with version 2.0.0 of Zoom

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`:

## Abnormal Security Event Collector

**Product:** Abnormal Security

**Kind:** integration

Abnormal Security Event Collector integration for XSIAM. This integration was integrated and tested with version 01 of Abnormal Security Event Collector

**Commands:**

- `None`:

## Alibaba Action Trail Event Collector

**Product:** Alibaba Action Trail

**Kind:** integration

Alibaba log event collector integration for XSIAM. This integration was integrated and tested with API version 0.6 of Alicloud Log Service

**Commands:**

- `None`:

## Armis Event Collector

**Product:** Armis

**Kind:** integration

Collects alerts, devices and activities from Armis resources. This integration was integrated and tested with API V.1.8 of Armis API

**Commands:**

- `None`:

## AWS - GuardDuty Event Collector

**Product:** AWS - GuardDuty

**Kind:** integration

Amazon Web Services Guard Duty Service Event Collector integration for Cortex XSIAM

**Commands:**

- `None`:

## AWS Security Hub Event Collector

**Product:** AWS - Security Hub

**Kind:** integration

An XSIAM event collector for AWS Security Hub

**Commands:**

- `None`:

## BitSight Event Collector

**Product:** Bitsight

**Kind:** integration

Use this integration to fetch BitSight security findings as events in Cortex XSIAM. This is important for organizations that wish to integrate BitSight programmatically into their security operations. When configured as a fetching integration, it will continuously fetch new findings starting from the current day. The manual bitsight-get-events command fetches findings from the last 2 days (48 hours) by default, or from an explicit date range when start_date and/or end_date are provided

**Commands:**

- `None`:

## Box Event Collector

**Product:** Box

**Kind:** integration

Collect events from Box's logs

**Commands:**

- `None`: 
- `None`:

## Carbon Black Endpoint Standard Event Collector

**Product:** Carbon Black Endpoint Standard

**Kind:** integration

Endpoint Standard (formerly called Carbon Black Defense), a Next-Generation Anti-Virus + EDR. Collect Anti-Virus & EDR alerts and Audit Log Events

**Commands:**

- `None`:

## Cisco AMP Event Collector

**Product:** Cisco AMP

**Kind:** integration

This is the Cisco AMP event collector integration for Cortex XSIAM. This integration was integrated and tested with version v1 of CiscoAMPEventCollector

**Commands:**

- `None`:

## Cisco Webex Event Collector

**Product:** Cisco Webex Teams

**Kind:** integration

Cisco Webex Event Collector fetches Events and Admin Audit Events and Security Audit Events. This integration was integrated and tested with version 1 of CiscoWebex API

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

## Code42 Event Collector

**Product:** Code42

**Kind:** integration

Code42 Insider Risk software solutions provide the right balance of transparency, technology and training to detect and appropriately respond to data risk. Use the Code42EventCollector integration to fetch file events and audit logs

**Commands:**

- `None`:

## Cohesity Helios Event Collector

**Product:** Cohesity Helios

**Kind:** integration

This is the Cohesity Helios Event Collector integration for XSIAM

**Commands:**

- `None`:

## CyberArk EPM Event Collector

**Product:** CyberArk Endpoint Privilege Manager

**Kind:** integration

Collects policy audits, admin audits, and detailed (raw) events from CyberArk Endpoint Privilege Manager (EPM). This integration was integrated and tested with version 23.12.0 of CyberArk EPM

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`:

## CyberArk Identity Event Collector

**Product:** CyberArk Identity

**Kind:** integration

CyberArk Identity log event collector integration for Cortex XSIAM. This integration was integrated and tested with version 22.4 of CyberArk Identity Event Collector

**Commands:**

- `None`: 
- `None`:

## Darktrace Event Collector

**Product:** Darktrace

**Kind:** integration

Use this integration to fetch a list of model breaches, filtered by the specified parameters. This is important for organizations that wish to integrate Darktrace programmatically into their SOC environment. The integration was integrated and tested with version v5.2 API of Darktrace

**Commands:**

- `None`:

## DeCYFIR Event Collector

**Product:** DeCYFIR

**Kind:** integration

Collects event logs from DeCYFIR for ingestion into Cortex XSIAM. Once configured, the integration periodically fetches event logs from DeCYFIR’s APIs and sends them to Cortex XSIAM for ingestion and analysis

**Commands:**

- `None`:

## Digital Guardian ARC Event Collector

**Product:** Digital Guardian

**Kind:** integration

This is the Digital Guardian ARC event collector integration for Cortex XSIAM. This integration was integrated and tested with version 3.10.0 of DigitalGuardianARCEventCollector

**Commands:**

- `None`: 
- `None`:

## Dropbox Event Collector

**Product:** Dropbox

**Kind:** integration

Collect events from Dropbox's logs. This integration was integrated and tested with version 2 of Dropbox API

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`:

## Druva Event Collector

**Product:** Druva

**Kind:** integration

This is the Druva event collector integration for Cortex XSIAM

**Commands:**

- `None`:

## Duo Event Collector

**Product:** DUO Admin

**Kind:** integration

Collects Auth and Audit events for Duo using the API

**Commands:**

- `None`:

## Elasticsearch Event Collector

**Product:** Elasticsearch

**Kind:** integration

Elasticsearch Event Collector integration is used to search for and analyze data in real time. Supports version 6 and later

**Commands:**

- `None`:

## ExtraHop Reveal(x) Event Collector

**Product:** ExtraHop Reveal(x)

**Kind:** integration

ExtraHop Reveal(x) is a network detection and response solution that provides complete visibility of network communications at enterprise scale, real-time threat detections backed by machine learning, and guided investigation workflows that simplify response

**Commands:**

- `None`:

## Trellix Email Security - Cloud Event Collector

**Product:** Trellix Email Security - Cloud

**Kind:** integration

Use this integration to fetch email security incidents from Trellix Email Security - Cloud as XSIAM events

**Commands:**

- `None`:

## FireEye HX Event Collector

**Product:** FireEye HX

**Kind:** integration

Palo Alto Networks FireEye HX Event Collector integration for XSIAM

**Commands:**

- `None`:

## Forcepoint DLP Event Collector (Beta)

**Product:** Forcepoint DLP

**Kind:** integration

Use this integration to fetch security incidents from Forcepoint DLP as Cortex XSIAM events

**Commands:**

- `None`:

## Generic API Event Collector (Beta)

**Product:** GenericAPIEventCollector

**Kind:** integration

The Generic API Event Collector allows you to ingest data from any API endpoint into Cortex. By configuring this collector, you can gather data from various systems and bring it into the Cortex ecosystem for better analysis and correlation. Note: This pack is currently in Beta, and as such, it may be subject to future changes and may not work on all types of APIs and Authentication

**Commands:**

- `None`: 
- `None`:

## Genetec Security Center Event Collector

**Product:** Genetec Security Center

**Kind:** integration

Security Center is the foundation of our unified security portfolio. It lets you connect your security at your own pace, starting with a single core system. Even if you're only interested in upgrading your video surveillance or access control, taking the next step is easy

**Commands:**

- `None`:

## GitGuardian Event Collector

**Product:** GitGuardian

**Kind:** integration

This is the GitGuardian event collector integration for Cortex XSIAM. This integration was integrated and tested with version 1.0.0 of GitGuardianEventCollector

**Commands:**

- `None`:

## GitLab Event Collector

**Product:** GitLab

**Kind:** integration

An event collector for GitLab audit events using Gitlab's API. Audit events API documentation

## GitHub Event Collector

**Product:** GitHub

**Kind:** integration

**Commands:**

- `None`:

## HelloWorld Event Collector

**Product:** HelloWorld

**Kind:** integration

This is the Hello World event collector integration for XSIAM

**Commands:**

- `None`:

## HPE Aruba Central Event Collector

**Product:** HPE Aruba Central

**Kind:** integration

This is the Aruba Central event collector integration for Cortex XSIAM

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`:

## Infoblox BloxOne Threat Defense Event Collector

**Product:** Infoblox Threat Defense with DDI

**Kind:** integration

BloxOne Threat Defense is a hybrid cybersecurity solution that leverages DNS as the first line of defense to detect and block cyber threats

**Commands:**

- `None`:

## Ironscales Event Collector

**Product:** Ironscales Event Collector

**Kind:** integration

Use this integration to fetch email security incidents from Ironscales as XSIAM events

**Commands:**

- `None`:

## Jamf Protect Event Collector

**Product:** JamfProtect

**Kind:** integration

Use this integration to fetch audit logs events, alerts events and computers assets from Jamf Protect to Cortex XSIAM

**Commands:**

- `None`: 
- `None`:

## Jira Event Collector

**Product:** Atlassian Jira

**Kind:** integration

This integration was integrated and tested with version 3 of Jira Event Collector rest API

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`:

## KnowBe4 KSAT Event Collector

**Product:** KSAT

**Kind:** integration

Allows you to push and pull your external data to and from the KnowBe4 KSAT (Security Awareness Training) console. For subscription levels and pricing, see the KnowBe4 Security Awareness Training pricing page

**Commands:**

- `None`: 
- `None`:

## Microsoft Defender for Cloud Apps Event Collector

**Product:** Microsoft Defender for Cloud Apps

**Kind:** integration

Microsoft Defender for Cloud Apps Event Collector integration

**Commands:**

- `None`: 
- `None`:

## Microsoft Defender for Cloud Event Collector

**Product:** Microsoft Defender for Cloud

**Kind:** integration

XSIAM collector for Microsoft Defender for Cloud alerts

## Mimecast Event Collector v2

**Product:** Mimecast

**Kind:** integration

**Commands:**

- `None`:

## NetBox Event Collector

**Product:** NetBox

**Kind:** integration

This is the NetBox event collector integration for Cortex XSIAM. This integration was integrated and tested with version 3.0 and above of NetBox API

**Commands:**

- `None`: 
- `None`: 
- `None`:

## Netskope Event Collector v2

**Product:** Netskope

**Kind:** integration

**Commands:**

- `None`: 
- `None`:

## Okta Auth0 Event Collector

**Product:** Okta Auth0

**Kind:** integration

Okta Auth0 logs event collector integration for Cortex XSIAM. This integration was integrated and tested with version 2.0 of Okta Auth0. Please see the Okta Auth0 rate limit policy

**Commands:**

- `None`:

## Okta Event Collector

**Product:** Okta

**Kind:** integration

Collects the events log for authentication and Audit provided by Okta admin API

**Commands:**

- `None`:

## OneLogin Event Collector

**Product:** OneLogin

**Kind:** integration

Simple customer authentication and streamlined workforce identity operations

**Commands:**

- `None`:

## Oracle Cloud Infrastructure Event Collector

**Product:** Oracle Cloud Infrastructure (OCI)

**Kind:** integration

This integration fetches audit log events from an Oracle Cloud Infrastructure resources. Audit log events can be used for security audits, to track usage of and changes to Oracle Cloud Infrastructure resources, and to help ensure compliance with standards or regulations

## Orca Event Collector

**Product:** Orca

**Kind:** integration

Orca Security event collector integration for Cortex XSIAM. This integration was integrated and tested with version 0.1.0 of Orca Event Collector

**Commands:**

- `None`:

## Proofpoint Email Security Event Collector

**Product:** Proofpoint Email Security

**Kind:** integration

Collects events for Proofpoint using the streaming API. This integration was integrated and tested Proofpoint Email Security

**Commands:**

- `None`: 
- `None`:

## Proofpoint Threat Response Event Collector

**Product:** Proofpoint Threat Response

**Kind:** integration

Use the Proofpoint Threat Response integration to orchestrate and automate incident response

**Commands:**

- `None`:

## Recorded Future Event Collector

**Product:** Recorded Future Intelligence

**Kind:** integration

This integration fetches alerts from Recorded Future. This integration was integrated and tested with version 2 of the Recorded Future API

**Commands:**

- `None`:

## ReliaQuest GreyMatter DRP Event Collector

**Product:** ReliaQuest Digital Risk Protection

**Kind:** integration

ReliaQuest GreyMatter DRP Event Collector minimizes digital risk by identifying unwanted exposure and protecting against external threats. The award-winning SearchLight solution provides ongoing monitoring of a customer's unique assets and exposure across the open, deep, and dark web. This enables clients to detect data loss, brand impersonation, infrastructure risks, cyber threats, and much more. This integration fetches event items which can be either incident/alerts, for more information refer here

**Commands:**

- `None`:

## RunZero Event Collector

**Product:** RunZero

**Kind:** integration

This is the RunZero event collector integration for XSIAM. This integration was integrated and tested with version 3.3.0 of RunZero Event Collector

**Commands:**

- `None`:

## SaaS Security Event Collector

**Product:** SaaS Security by Palo Alto Networks

**Kind:** integration

SaaS Security is an integrated CASB (Cloud Access Security Broker) solution that helps Security teams like yours meet the challenges of

**Commands:**

- `None`: 
- `None`:

## Thales SafeNet Trusted Access Event Collector

**Product:** Thales SafeNet Trusted Access

**Kind:** integration

Retrieve access, authentication, and audit logs and stores them in a Security Information and Event Management (SIEM) system, local repository, or syslog file server. You can retrieve the logs only for the tenant that is associated with the API key, or for a direct or delegated child of that tenant

**Commands:**

- `None`: 
- `None`:

## SailPoint IdentityNow Event Collector

**Product:** SailPoint IdentityNow

**Kind:** integration

This is the SailPoint IdentityNow event collector integration for Cortex XSIAM. This integration was integrated and tested with version 3 of SailPoint API

**Commands:**

- `None`:

## SecurityScorecard Event Collector

**Product:** SecurityScorecard

**Kind:** integration

**Commands:**

- `None`: 
- `None`:

## ServiceNow Event Collector

**Product:** ServiceNow

**Kind:** integration

Use this integration to fetch audit, case, syslog transactions, and outbound HTTP logs from ServiceNow as Cortex XSIAM events. This integration was integrated and tested with Vancouver version of ServiceNow API

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

## Slack Event Collector

**Product:** Slack

**Kind:** integration

Slack logs event collector integration for XSIAM. This integration was integrated and tested with version v1 of Slack Audit Logs API

**Commands:**

- `None`: 
- `None`:

## Symantec Cloud Secure Web Gateway Event Collector

**Product:** Symantec Cloud Secure Web Gateway

**Kind:** integration

Palo Alto Networks Symantec Cloud Secure Web Gateway Event Collector integration for XSIAM

## Symantec CloudSOC Event Collector

**Product:** SymantecCloudSOC

**Kind:** integration

Gets Events from Symantec CloudSOC. This integration was integrated and tested with version 3.157 of Symantec CloudSOC

**Commands:**

- `None`:

## TeamViewer Event Collector

**Product:** TeamViewer

**Kind:** integration

TeamViewer event collector integration for Cortex XSIAM. This integration was integrated and tested with version 15.40 of TeamViewer. User access token scope: Event logging - Allow requesting all event logs. A Tensor license is required

**Commands:**

- `None`:

## Trend Micro Email Security Event Collector

**Product:** Trend Micro Email Security

**Kind:** integration

Palo Alto Networks Trend Micro Email Security Event Collector integration for XSIAM

**Commands:**

- `None`:

## TrendAI Vision One™ Event Collector

**Product:** TrendAI Vision One™

**Kind:** integration

Important: This integration is supported by Palo Alto Networks. Palo Alto Networks TrendAI Vision One™ Event Collector integration for Cortex XSIAM collects the Workbench, Observed Attack Techniques, Search Detections and Audit logs. TrendAI Vision One™ is a purpose-built threat defense platform that provides added value and new benefits beyond XDR solutions, allowing you to see more and respond faster. Providing deep and broad extended detection and response (XDR) capabilities that collect and automatically correlate data across multiple security layers—email, endpoints, servers, cloud workloads, and networks—TrendAI Vision One™ prevents the majority of attacks with automated protection

**Commands:**

- `None`:

## Vectra AI Event Collector

**Product:** Vectra AI

**Kind:** integration

Collects Vectra Detections and Audits into XSIAM Events. This integration was integrated and tested with version 2.2 of Vectra

**Commands:**

- `None`:

## VeloCloud Event Collector

**Product:** VeloCloud

**Kind:** integration

Collects events from the VeloCloud API. This integration was integrated and tested with VeloCloud as of 2025-10-06

**Commands:**

- `None`:

## WithSecure Event Collector

**Product:** WithSecure

**Kind:** integration

WithSecure event collector integration for Cortex XSIAM. This integration was integrated and tested with version 1.0 of WithSecure API

**Commands:**

- `None`: 
- `None`:

## Workday Event Collector

**Product:** Workday

**Kind:** integration

Use Workday Event Collector integration to get activity loggings from Workday. This integration was integrated and tested with API v1

**Commands:**

- `None`: 
- `None`:

## Workday Sign On Event Collector

**Product:** Workday

**Kind:** integration

Use the Workday Sign On Event Collector integration to get sign on logs from Workday. This integration was integrated and tested with version v37.0 of Workday Sign On Event Collector

**Commands:**

- `None`:

## Zoom Event Collector

**Product:** Zoom

**Kind:** integration

This is the Zoom event collector integration for Cortex XSIAM. This integration was integrated and tested with version 2.0.0 of Zoom

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 

