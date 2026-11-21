# Integration and Automation Catalog - Soc Operations

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## 1Password

**Type:** integration  
**Product:** OnePassword  

Fetch events about actions performed by 1Password users within a specific account, access and modifications to items in shared vaults, and user sign-in attempts. This integration was integrated and tested with V2 endpoints of the 1Password Events API

**Commands:**

- `one-password-get-events`: Fetch events from 1Password. This command is intended for development and debugging purposes and should be used with caution as it may create duplicate events.


## 1Touch.io's Inventa Connector

**Type:** integration  
**Product:** Inventa  

Use the Inventa integration to generate DSAR reports within Inventa instance and retrieve DSAR data for the platform This integration was integrated and tested with version 2.8.0 of Inventa

**Commands:**

- `inventa-get-datasubjects`: Get Data Subject full details
- `inventa-get-sources`: Retrieves data sources' details containing info about data subject
- `inventa-get-sources-piis`: Retrieves PII entities stored in data sources related to datasubject
- `inventa-get-dsar-transactions`: Retrieves data transactions' details containing info about data subject
- `inventa-get-dsar-files`: Retrieves details of files contatining info about data subject
- `inventa-get-dsar-databases`: Retrieves list of databases and tables containing info about data subject
- `inventa-get-datasubject-details`: Get datasubject name and email
- `inventa-get-dsar-dataassets`: Retrieves list of data assets containing info about data subject
- `inventa-get-dsar-piis`: Get list of PII categories related to the data subject
- `inventa-get-entities`: Retrieves list of PII entities described in Inventa
- `inventa-get-datasubject-id-from-ticket`: Retrieves ID of a data subject from Inventa's DSAR ticket
- `inventa-get-datasubject-id`: Retrieves ID of a data subject from passed constraints
- `inventa-create-ticket`: Creates Inventa ticket
- `inventa-validate-incident-inputs`: Validates Incident inputs


## 3CXDesktopApp Supply Chain Attack

**Type:** playbook  
**Product:** 3CXDesktopApp Supply Chain Attack  

On March 29, 2023, CrowdStrike released a blog discussing a supply chain attack involving a software-based phone application called 3CXDesktopApp. As of March 30, the 3CXDesktopApp installer hosted on the developer’s website will install the application with two malicious libraries included. The malicious libraries will ultimately run shellcode to load a backdoor on the system that allows actors to install additional malware on the victim machine. Between March 9-30, 2023, we observed activity at 127 Cortex XDR customers that involved the 3CXDesktopApp process attempting to run shellcode, which was blocked by the XDR Agent’s In-process Shellcode Protection Module. Due to blocking the shellcode, we were unable to obtain the secondary payload used in this attack, so we cannot determine its capabilities or any post-exploitation activities carried out by the threat actor. According to 3CX’s announcement, the supply chain attack involved 3CX’s Electron Windows App shipped in Update 7, version numbers 18.12.407 & 18.12.416 and Electron Mac App version numbers 18.11.1213, 18.12.402, 18.12.407 & 18.12.416. This playbook should be triggered manually or can be configured as a job. Please create a new incident and choose the 3CXDesktopApp Supply Chain Attack playbook and Rapid Breach Response incident type. The playbook includes the following tasks: Hunting: References: Threat Brief: 3CXDesktopApp Supply Chain Attack CrowdStrike Falcon Platform Detects and Prevents Active Intrusion Camp

**Inputs:**

- `PlaybookDescription`: The playbook description to be used in the Rapid Breach Response - Set Incident Info sub-playbook.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `QRadarTimeRange`: The time range to search for indicators in the Threat Hunting - Generic playbook.
- `SplunkEarliestTime`: The earliest time to search for indicators in the Threat Hunting - Generic playbook.
- `SplunkLatestTime`: The latest time to search for indicators in the Threat Hunting - Generic playbook.
- `XQLTimeRange`: The time range for the Cortex XDR XQL query.
- `excludeIndicators`: List of indicators to exclude.
- `elasticSearchIndex`: The index to search over using elastic query.


## A1000FinalClassification

**Type:** script  
**Product:** ReversingLabs A1000  

Calculates A1000 final classification based on A1000 classification and A1000 full reports

**Inputs:**

- `a1000_classification_report`: A1000 classification report
- `a1000_full_report`: A1000 full report


## Abnormal Security

**Type:** integration  
**Product:** Abnormal Security  

Abnormal Security detects the whole spectrum of email attacks, from vendor email compromise and spear-phishing to unwanted email spam and graymail. To stop these advanced attacks, Abnormal leverages the industry’s most advanced behavioral data science to baseline known good behavior and detects anomalies. This integration was integrated and tested with version 1.3.0 of Abnormal Security

**Commands:**

- `abnormal-security-check-case-action-status`: Check the status of an action requested on a case.
- `abnormal-security-check-threat-action-status`: Check the status of an action requested on a threat.
- `abnormal-security-download-threat-log-csv`: Download data from Threat Log in .csv format
- `abnormal-security-list-abuse-mailbox-campaigns`: Get a list of campaigns submitted to Abuse Mailbox
- `abnormal-security-list-abnormal-cases`: Get a list of Abnormal cases identified by Abnormal Security
- `abnormal-security-list-threats`: Get a list of threats
- `abnormal-security-get-threat`: Get details of a threat
- `abnormal-security-get-abnormal-case`: Get details of an Abnormal case
- `abnormal-security-get-abuse-mailbox-campaign`: Get details of an Abuse Mailbox campaign
- `abnormal-security-get-employee-identity-analysis`: Get employee identity analysis (Genome) data
- `abnormal-security-get-employee-information`: Get employee information
- `abnormal-security-get-employee-last-30-days-login-csv`: Get employee login information for last 30 days in csv format
- `abnormal-security-get-latest-threat-intel-feed`: DEPRECATED. Get the latest threat intel feed.
- `abnormal-security-manage-threat`: Manage a Threat identified by Abnormal Security
- `abnormal-security-manage-abnormal-case`: Manage an Abnormal Case.


## Absolute

**Type:** integration  
**Product:** Absolute  

Absolute is an adaptive endpoint security solution that delivers device security, data security, and asset management of endpoints. This integration was integrated and tested with the API version 1.7 of Absolute. Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `absolute-custom-device-field-list`: Returns a list of custom device fields associated with the given device_id, based on the authorization token.
- `absolute-custom-device-field-update`: Updates the value of the included custom device fields for the given device_id.
- `absolute-device-freeze-request`: Creates a new Freeze request for the devices specified in the device_ids argument.
- `absolute-device-remove-freeze-request`: Creates a new Remove Freeze request for one or more devices, regardless of their Freeze status. You can submit Remove Freeze requests to perform the following a
- `absolute-device-freeze-request-get`: Gets detailed information about the Freeze request specified by request_uid.
- `absolute-device-freeze-message-list`: Gets all the Freeze messages that are configured for the account by the given message_id. If message_id is not given all the messages will be returned.
- `absolute-device-freeze-message-create`: Creates a new Freeze message for the account.
- `absolute-device-freeze-message-update`: Updates the content of an existing Freeze message.
- `absolute-device-freeze-message-delete`: Deletes an existing Freeze message for the account.
- `absolute-device-unenroll`: Initiates an unenroll request on a list of eligible devices.
- `absolute-device-application-list`: Gets a list of device records and the corresponding software application data for each device on the account that you have access to or that meets the given fil
- `absolute-device-list`: Gets a list of device records and their corresponding data that meets the required filter for all devices in your account, based on your authorization token.
- `absolute-device-get`: Gets a list of device records and their corresponding data that meets the required fields for all devices in your account. Note that the command supports return
- `absolute-device-location-get`: Gets a list of devices geo locations records and their corresponding data that meets the required devices IDs.
- `absolute-device-get-events`: Retrieves a list of events from the Absolute device instance.


## AbuseIPDBPopulateIndicators

**Type:** script  
**Product:** AbuseIPDB  

Extracts IP addresses on block lists from AbuseIPDB, and populates indicators accordingly

**Inputs:**

- `days`: The time range to return reports for (in days). The default is 30.
- `limit`: The maximum number of IP addressess to retrieve. The default is 50
- `confidence`: The Minimum confidence required for the retrieved IPs. The default is 100.


## Acalvio ShadowPlex

**Type:** integration  
**Product:** Acalvio ShadowPlex  

Acalvio ShadowPlex is a comprehensive Autonomous Deception Platform that offers Advanced Threat Detection, Investigation and Response capabilities. This integration was integrated and tested with Acalvio ShadowPlex 5.x and ShadowPlex API 2.0

**Commands:**

- `acalvio-is-deception-host`: Check if its a Deception Host
- `acalvio-is-deception-user`: Check if its a Deception User
- `acalvio-is-deception-file`: Check if its a Deception File on the Endpoint
- `acalvio-mute-deception-host`: Mute a Deception Host
- `acalvio-unmute-deception-host`: Unmute a Deception Host
- `acalvio-mute-deception-on-endpoint`: Mute a Deception on Endpoint
- `acalvio-unmute-deception-on-endpoint`: Unmute a Deception on Endpoint


## Add Employees to Departing Employee Watchlist

**Type:** playbook  
**Product:** Code42  

Loops through stand-down tickets provided by the Departing Employee Auto-Add playbook and adds employees to the Departing Employee watchlist in Code42 Incydr

**Inputs:**

- `ticket_username`: The username (in email format) provided in a stand-down ticket from Jira, Zendesk, etc.
- `ticket_departure_date`: The departure date (in YYYY-MM-DD format) provided in a stand-down ticket from Jira, Zendesk, etc.


## Add IOCs - Cofense Vision

**Type:** playbook  
**Product:** Cofense Vision  

Add or update IOCs in Cofense Vision

**Inputs:**

- `source`: A single IOC source value, to fetch the IOCs added or modified by that particular source. The value for source can contain uppercase letters
- `threat_type`: Type of the IOC. Supported values: Domain, MD5, Sender, SHA256, Subject, or URL.
- `threat_value`: The actual value of the IOC match in the email.
- `threat_level`: The severity of the IOC.
- `created_at`: The UTC date and time, the IOC source included the IOC for the first time.
- `updated_at`: The UTC date and time, the IOC source last updated the IOC.
- `source_id`: The unique identifier assigned by the IOC source.
- `requested_expiration`: The expected UTC expiration date and time. The IOC repositorycalculates an expiration date and time for the new IOC by default 14 days after


## Admin By Request

**Type:** integration  
**Product:** Admin By Request  

AdminByRequest is a Privileged Access Management (PAM) solution that enables secure, temporary elevation to local admin rights

**Commands:**

- `adminbyrequest-get-events`: Retrieves a list of entries logs events from the AdminByRequest instance.
- `adminbyrequest-list-requests`: Lists requests from AdminByRequest.
- `adminbyrequest-request-deny`: Denies a request in AdminByRequest.
- `adminbyrequest-request-approve`: Approves a request in AdminByRequest.


## AfterRelativeDate

**Type:** script  
**Product:** Filters And Transformers  

Checks the given datetime has occurred after the provided relative time

**Inputs:**

- `left`: Date value to check - Can be any time format. ex. "2020-01-01T00:00:00"
- `right`: Relative time ex. "6 months ago"


## Aha

**Type:** integration  
**Product:** AHA  

Use the Aha! integration to list and manage the platform. This integration was integrated and tested with API version December 02, 2022 release of Aha

**Commands:**

- `aha-get-features`: Lists all features from service, unless a specific feature is specified.
- `aha-edit-feature`: You can edit the following fields in a feature: Name and Description.
- `aha-get-ideas`: Lists all ideas from service, unless a specific idea is specified.
- `aha-edit-idea`: Edit an idea status to Shipped.


## Akamai Prolexic

**Type:** integration  
**Product:** Akamai Prolexic  

Collects DDoS detection critical events and general events from Akamai Prolexic Analytics for Cortex XSIAM. This integration was integrated and tested with version v2 of the Akamai Prolexic Analytics API

**Commands:**

- `akamai-prolexic-get-events`: Gets events from Akamai Prolexic. This command is used for developing and debugging and is to be used with caution, as it can create duplicate events in the dat


## Akamai WAF

**Type:** integration  
**Product:** Akamai WAF  

Use the Akamai WAF integration to manage common sets of lists used by various Akamai security products and features. This is the modified version where a new command "akamai-update-network-list-elements" was added by the SA

**Commands:**

- `akamai-check-group`: Check an existing group within the context of your account.
- `akamai-create-group`: Create a new group under a parent GID.
- `akamai-create-enrollment`: Create a new enrollment.
- `akamai-list-enrollments`: List enrollments of a specific contract.
- `akamai-create-domain`: Create a domain with properties and domain controller (DC).
- `akamai-update-property`: Update a property for a specific domain.
- `akamai-get-change`: Get the CPS code.
- `akamai-update-change`: Update the certs and trust chains.
- `akamai-get-enrollment-by-cn`: Get enrollment by common name.
- `akamai-list-groups`: Lists groups of Akamai.
- `akamai-get-group`: Get group.
- `akamai-get-client-list`: Get a client list.
- `akamai-create-client-list`: Creates a new client list.
- `akamai-deprecate-client-list`: Deprecates a client list.
- `akamai-activate-client-list`: Activates a client list.


## Akamai WAF - Activate Network Lists

**Type:** playbook  
**Product:** Akamai WAF  

Activates network lists in Staging or Production on Akamai WAF. The playbook finishes running when the network list is active on the requested enviorment

**Inputs:**

- `network_list_ids`: The comma-separated list of network list IDs to activate. For example, "id_list1,id_list2".
- `env`: The enviorment type to activate the network list. Can be "STAGING" or "PRODUCTION".
- `comment`: The comment to log when activating the network lists.
- `notify`: The comma-separated list of email addresses to notify when the network lists are activated.


## AlgoSec

**Type:** integration  
**Product:** AlgoSec  

Algosec AppViz, Firewall Analyzer (AFA) and FireFlow(AFF)

**Commands:**

- `algosec-get-ticket`: Retrieves a FireFlow change request by its ID
- `algosec-create-ticket`: Creates a new FireFlow change request
- `algosec-get-applications`: Find applications containing network objects related to IP address using AppViz
- `algosec-get-network-object`: Find network objects related to IP address
- `algosec-query`: Performs a batch traffic simulation query using Firewall Analyzer


## AlgosecGetApplications

**Type:** script  
**Product:** AlgoSec  

Finds applications containing network objects related to IP address using AppViz

**Inputs:**

- `address`: The IP address/Subnet to search.
- `type`: The search method for the address.


## AlgosecGetNetworkObject

**Type:** script  
**Product:** AlgoSec  

Finds network objects related to the IP address

**Inputs:**

- `address`: The IP address/Subnet to search.
- `type`: The search method for the address. The default is INTERSECT.


## AlgosecQuery

**Type:** script  
**Product:** AlgoSec  

Performs a batch traffic simulation query using Firewall Analyzer

**Inputs:**

- `source`: The source(s) for the query. Multiple values must be comma-separated.
- `destination`: The destination(s) for the query. Multiple values must be comma-separated.
- `service`: The service(s) for the query. Multiple values must be comma-separated.
- `user`: The user for the query.
- `application`: The application for the query.


## AlphaVantage

**Type:** integration  
**Product:** AlphaVantage  

This is an API to get stock prices etc

**Commands:**

- `alphavantage-stock-data-get`: Gets data for a stock
- `alphavantage-stock-history-get`: Gets historical data for a stock


## Amazon DynamoDB

**Type:** integration  
**Product:** Amazon DynamoDB  

Amazon DynamoDB Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database, so that you don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling. With DynamoDB, you can create database tables that can store and retrieve any amount of data, and serve any level of request traffic. You can scale up or scale down your tables' throughput capacity without downtime or performance degradation, and use the AWS Management Console to monitor resource utilization and performance metrics. DynamoDB automatically spreads the data and traffic for your tables over a sufficient number of servers to handle your throughput and storage requirements, while maintaining consistent and fast performance. All of your data is stored on solid state disks (SSDs) and automatically replicated across multiple Availability Zones in an AWS region, providing built-in high availability and data durability. For more information regarding the AWS DynamoDB service, please visit the official documentation found here

**Commands:**

- `aws-dynamodb-batch-get-item`: The BatchGetItem operation returns the attributes of one or more items from one or more tables. You identify requested items by primary key. A single operation 
- `aws-dynamodb-batch-write-item`: The BatchWriteItem operation puts or deletes multiple items in one or more tables. A single call to BatchWriteItem can write up to 16 MB of data, which can comp
- `aws-dynamodb-create-backup`: Creates a backup for an existing table. Each time you create an on-demand backup, the entire table data is backed up. There is no limit to the number of on-dema
- `aws-dynamodb-create-global-table`: Creates a global table from an existing table. A global table creates a replication relationship between two or more DynamoDB tables with the same table name in
- `aws-dynamodb-create-table`: The CreateTable operation adds a new table to your account. In an AWS account, table names must be unique within each Region. That is, you can have two tables w
- `aws-dynamodb-delete-backup`: Deletes an existing backup of a table. You can call DeleteBackup at a maximum rate of 10 times per second.
- `aws-dynamodb-delete-item`: Deletes a single item in a table by primary key. You can perform a conditional delete operation that deletes the item if it exists, or if it has an expected att
- `aws-dynamodb-delete-table`: The DeleteTable operation deletes a table and all of its items. After a DeleteTable request, the specified table is in the DELETING state until DynamoDB complet
- `aws-dynamodb-describe-backup`: Describes an existing backup of a table. You can call DescribeBackup at a maximum rate of 10 times per second.
- `aws-dynamodb-describe-continuous-backups`: Checks the status of continuous backups and point in time recovery on the specified table. Continuous backups are ENABLED on all tables at table creation. If po
- `aws-dynamodb-describe-endpoints`: Returns the regional endpoint information.
- `aws-dynamodb-describe-global-table`: Returns information about the specified global table.
- `aws-dynamodb-describe-global-table-settings`: Describes Region-specific settings for a global table.
- `aws-dynamodb-describe-limits`: Returns the current provisioned-capacity limits for your AWS account in a Region, both for the Region as a whole and for any one DynamoDB table that you create 
- `aws-dynamodb-describe-table`: Returns information about the table, including the current status of the table, when it was created, the primary key schema, and any indexes on the table. If yo


## Amazon Security Lake

**Type:** integration  
**Product:** Amazon - Security Lake  

Amazon Security Lake is a fully managed security data lake service. This integration was integrated and tested with version 1.34.20 of AWS Security Lake SDK (boto3)

**Commands:**

- `aws-security-lake-query-execute`: Execute a new query, wait for the query to complete (using polling), and return query's execution information, and query's results (if successful). Either 'Outp
- `aws-security-lake-data-catalogs-list`: Lists the data catalogs in the current Amazon Web Services account.
- `aws-security-lake-databases-list`: Lists the databases in the specified data catalog.
- `aws-security-lake-table-metadata-list`: Lists the metadata for the tables in the specified data catalog database.
- `aws-security-lake-user-mfalogin-query`: Runs query that takes a provided username and queries the AWS Security Lake for MFA login attempts (Success/Failed) associated with the user's account, using AW
- `aws-security-lake-source-ip-query`: Runs a query that takes a provided source IP address and queries the AWS Security Lake for console login attempts (Success/Failed) associated with the IP addres
- `aws-security-lake-guardduty-activity-query`: This command is used to search for Guard Duty logs for any criticality level activity.
- `aws-security-lake-data-sources-list`: Retrieves a snapshot of the current region, including whether Amazon Security Lake is enabled for those accounts and which sources Security Lake is collecting d
- `aws-security-lake-data-lakes-list`: Retrieves the Amazon Security Lake configuration object for the specified Amazon Web Services Regions. In order to run this command the user must have 'security


## AMP

**Type:** integration  
**Product:** Cisco AMP  

Uses CISCO AMP Endpoint This integration was integrated and tested with API version v1 of AMP

**Commands:**

- `amp_get_computers`: Returns a list of computers on which agents are deployed. You can use filters (arguments) to narrow the search.
- `amp_get_computer_by_connector`: Returns information for the specified computer.
- `amp_get_computer_trajctory`: Returns a list of all activities associated with a particular computer. This is analogous to the Device Trajectory on the FireAMP Console. Use the Q argument to
- `amp_move_computer`: Moves a computer to a group with the corresponding connector_guid and group_guid, respectively.
- `amp_get_computer_activity`: This endpoint enables you to search all computers across your organization for any events or activities associated with a file or network operation, and returns
- `amp_get_events`: A general query interface for events. This is analogous to the Events view on the FireAMP Console.
- `amp_get_event_types`: Events are identified and filtered by a unique ID. This endpoint provides a human readable name and short description of each event (by ID).
- `amp_get_application_blocking`: Returns a list of application blocking file lists. You can filter this list by name
- `amp_get_file_list_by_guid`: Returns a particular file list for application blocking or simple custom detection. You need to specify the file_list_guid argument to retrieve information abou
- `amp_get_simple_custom_detections`: Returns a list of simple custom detection file lists. You can filter this list by detection name.
- `amp_get_file_list_files`: Returns a list of items for a particular file_list. You need to specify the file_list_guid argument to retrieve these items.
- `amp_get_file_list_files_by_sha`: Returns a particular item for a given file_list. You need to specify the sha256 argument and the file_list_guid argument to retrieve an item.
- `amp_set_file_list_files_by_sha`: Adds a SHA256 hash to a file list, using file_list_guid.
- `amp_delete_file_list_files_by_sha`: Deletes an item from a file_list using the SHA256 hash and file_list_guid.
- `amp_get_groups`: Returns basic information about groups in your organization. You can map group names to GUIDs for filtering on the events endpoint.


## Analyst1

**Type:** integration  
**Product:** Analyst1  
**Commands:**

- `domain`: Queries the Analyst1 REST API and enriches the given domain with Analyst1 Indicator data
- `email`: Queries the Analyst1 REST API and enriches the given email with Analyst1 indicator data.
- `ip`: Queries the Analyst1 REST API and enriches the given IP address with Analyst1 indicator data.
- `file`: Queries the Analyst1 REST API and enriches the given file with Analyst1 indicator data.
- `analyst1-enrich-string`: Queries the Analyst1 REST API and enriches the given string with Analyst1 indicator data
- `analyst1-enrich-ipv6`: Queries the Analyst1 REST API and enriches the given IP address with Analyst1 indicator data.
- `analyst1-enrich-mutex`: Queries the Analyst1 REST API and enriches the given mutex with Analyst1 indicator data.
- `analyst1-enrich-http-request`: Queries the Analyst1 REST API and enriches the given HTTP request with Analyst1 indicator data.
- `url`: Queries the Analyst1 REST API and enriches the given URL with Analyst1 indicator data.
- `analyst1-evidence-submit`: Submits an 'Evidence' to Analyst1. Submission can be any text or attachment (PDF, JSON,DOCX...). The a1Bot will extract all relevant context. The 'Evidence' can
- `analyst1-evidence-status`: Check on the status of the analyst1-evidence-submit action by using its output UUID.
- `analyst1-evidence-search`: Search for evidence in Analyst1 using filters and search terms.
- `analyst1-evidence-file-fetch`: Download an evidence file from Analyst1 by its ID.
- `analyst1-batch-check`: Queries the Analyst1 REST API for indicator enrichment data based on a CSV input of multiple indicator values.
- `analyst1-batch-check-post`: Similar to analyst1-batch-check, however the inputs can be more complex. The 'values' input is an option for a pre-formatted newline separated file. This allows


## Anomali Match

**Type:** integration  
**Product:** Anomali Enterprise  

Use Anomali Match to search indicators and enrich domains

**Commands:**

- `anomali-enterprise-retro-forensic-search`: Initiates a forensic search of the indicators.
- `anomali-enterprise-retro-forensic-search-results`: Retrieves the forensic search results.
- `anomali-enterprise-dga-domain-status`: The search domains Domain Generation Algorithm (DGA).
- `domain`: The search domains Domain Generation Algorithm (DGA). Includes DBotScore and domain information. There is no distinction between benign to unknown domains in An


## Anomali Security Analytics Alerts

**Type:** integration  
**Product:** Anomali Security Analytics  

The Anomali Security Analytics pack allows users to manage security alerts by interacting directly with the Anomali Security Analytics platform. It supports creating search jobs, monitoring their status, retrieving results, and updating alert statuses or comments, streamlining integration with Palo Alto platform. This integration was integrated and tested with version 1.0 of AnomaliSecurityAnalyticsAlerts

**Commands:**

- `anomali-security-analytics-search-job-create`: Create a new search job.
- `anomali-security-analytics-search-job-status`: Get the status of one or more search jobs.
- `anomali-security-analytics-search-job-results`: Get search job results.
- `anomali-security-analytics-alert-update`: Update various fields of an alert including status, comment, assignee, severity, and owner.


## Ansible ACME

**Type:** integration  
**Product:** Ansible Linux  

Automatic Certificate Management Environment on Linux hosts management using Ansible modules. This integration lets you manage certificate generation on Linux hosts with a CA supporting the ACME protocol, such as Let’s Encrypt. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the hosts by utilising SSH combined with Python. To use this integration, configure an instance of this integration. This will associate a credential to be used to access hosts when commands are run. The commands from this integration will take the Linux host address(es) as an input, and use the saved credential associated to the instance to execute. Create separate instances if multiple credentials are required. This integration was tested with Let's Encrypt and supports the ACME http-01, dns-01 and tls-alpn-01 challenges

**Commands:**

- `acme-account`: Create, modify or delete ACME accounts Further documentation available at https://docs.ansible.com/ansible/2.9/modules/acme_account_module.html
- `acme-account-info`: Retrieves information on ACME accounts Further documentation available at https://docs.ansible.com/ansible/2.9/modules/acme_account_info_module.html


## Ansible Automation Platform

**Type:** integration  
**Product:** Ansible Automation Platform  

Scale IT automation, manage complex deployments, and speed productivity. This integration was integrated and tested with version v3.8.0 of Ansible Automation Platform and with API version v2

**Commands:**

- `ansible-tower-inventories-list`: Retrieves the list of inventories.
- `ansible-tower-hosts-list`: Retrieves the list of hosts. If an inventory ID is specified, retrieve the host located under the specific inventory.
- `ansible-tower-host-create`: Creates a host under the specified inventory ID and with the specified name.
- `ansible-tower-host-delete`: Deletes the specified host.
- `ansible-tower-job-templates-list`: Retrieves the list of job templates.
- `ansible-tower-credentials-list`: Retrieves the list of credentials. If an ID is specified, retrieve the specific credential.
- `ansible-tower-job-launch`: Launches the job template.
- `ansible-tower-job-relaunch`: Relaunch a job.
- `ansible-tower-job-cancel`: Cancels a pending or running job.
- `ansible-tower-job-stdout`: Retrieves the standard output by running the provided job.
- `ansible-tower-job-status`: Retrieves the job status.
- `ansible-tower-job-events-list`: Retrieves the list of job events.
- `ansible-tower-adhoc-command-launch`: Creates new ad hoc commands.
- `ansible-tower-adhoc-command-relaunch`: Launch a new job to run the ad hoc command.
- `ansible-tower-adhoc-command-cancel`: Cancel a job of the specified ad hoc command.


## Ansible Cisco IOS

**Type:** integration  
**Product:** Ansible Cisco IOS  

This integration enables the management of Cisco IOS Switches and Routers directly from platform using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the hosts by utilising SSH. To use this integration, configure an instance of this integration. This will associate a credential to be used to access hosts when commands are run. The commands from this integration will take the IOS host address(es) as an input, and use the saved credential associated to the instance to execute. Create separate instances if multiple credentials are required

**Commands:**

- `ios-banner`: Manage multiline banners on Cisco IOS devices Further documentation available at https://docs.ansible.com/ansible/2.9/modules/ios_banner_module.html
- `ios-bgp`: Configure global BGP protocol settings on Cisco IOS. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/ios_bgp_module.html
- `ios-command`: Run commands on remote devices running Cisco IOS Further documentation available at https://docs.ansible.com/ansible/2.9/modules/ios_command_module.html
- `ios-l2-interfaces`: Manage Layer-2 interface on Cisco IOS devices. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/ios_l2_interfaces_module.html
- `ios-l3-interfaces`: Manage Layer-3 interface on Cisco IOS devices. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/ios_l3_interfaces_module.html
- `ios-lacp`: Manage Global Link Aggregation Control Protocol (LACP) on Cisco IOS devices. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/ios
- `ios-lacp-interfaces`: Manage Link Aggregation Control Protocol (LACP) on Cisco IOS devices interface. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/
- `ios-lag-interfaces`: Manage Link Aggregation on Cisco IOS devices. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/ios_lag_interfaces_module.html
- `ios-linkagg`: Manage link aggregation groups on Cisco IOS network devices Further documentation available at https://docs.ansible.com/ansible/2.9/modules/ios_linkagg_module.h
- `ios-lldp`: Manage LLDP configuration on Cisco IOS network devices. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/ios_lldp_module.html
- `ios-lldp-global`: Configure and manage Link Layer Discovery Protocol(LLDP) attributes on IOS platforms. Further documentation available at https://docs.ansible.com/ansible/2.9/mo
- `ios-lldp-interfaces`: Manage link layer discovery protocol (LLDP) attributes of interfaces on Cisco IOS devices. Further documentation available at https://docs.ansible.com/ansible/2
- `ios-logging`: Manage logging on network devices Further documentation available at https://docs.ansible.com/ansible/2.9/modules/ios_logging_module.html
- `ios-ntp`: Manages core NTP configuration. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/ios_ntp_module.html
- `ios-ping`: Tests reachability using ping from Cisco IOS network devices Further documentation available at https://docs.ansible.com/ansible/2.9/modules/ios_ping_module.htm


## Ansible Cisco NXOS

**Type:** integration  
**Product:** Ansible Cisco NXOS  

This integration enables the management of Cisco NXOS Switches and Routers directly from platform using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the hosts by utilising SSH. To use this integration, configure an instance of this integration. This will associate a credential to be used to access hosts when commands are run. The commands from this integration will take the NXOS host address(es) as an input, and use the saved credential associated to the instance to execute. Create separate instances if multiple credentials are required

**Commands:**

- `nxos-aaa-server`: Manages AAA server global configuration. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_aaa_server_module.html
- `nxos-aaa-server-host`: Manages AAA server host-specific configuration. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_aaa_server_host_module.html
- `nxos-acl-interface`: Manages applying ACLs to interfaces. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_acl_interface_module.html
- `nxos-banner`: Manage multiline banners on Cisco NXOS devices Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_banner_module.html
- `nxos-bfd-global`: Bidirectional Forwarding Detection (BFD) global-level configuration Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_bfd_glo
- `nxos-bfd-interfaces`: Manages BFD attributes of nxos interfaces. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_bfd_interfaces_module.html
- `nxos-bgp`: Manages BGP configuration. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_bgp_module.html
- `nxos-bgp-af`: Manages BGP Address-family configuration. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_bgp_af_module.html
- `nxos-bgp-neighbor`: Manages BGP neighbors configurations. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_bgp_neighbor_module.html
- `nxos-bgp-neighbor-af`: Manages BGP address-family's neighbors configuration. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_bgp_neighbor_af_modul
- `nxos-command`: Run arbitrary command on Cisco NXOS devices Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_command_module.html
- `nxos-evpn-vni`: Manages Cisco EVPN VXLAN Network Identifier (VNI). Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_evpn_vni_module.html
- `nxos-facts`: Gets facts about NX-OS switches Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_facts_module.html
- `nxos-gir`: Trigger a graceful removal or insertion (GIR) of the switch. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_gir_module.htm
- `nxos-gir-profile-management`: Create a maintenance-mode or normal-mode profile for GIR. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nxos_gir_profile_manag


## Ansible DNS

**Type:** integration  
**Product:** Ansible Linux  

This integration enables the management of DNS Records directly from platform using Dynamic DNS Updates from the NSUpdate Ansible Module. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the DNS server. The DNS master server being managed must be configured to accept Dynamic DNS updates using Transaction signatures as described in RFC2845

**Commands:**

- `dns-nsupdate`: Manage DNS records. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/nsupdate_module.html


## Ansible Microsoft Windows

**Type:** integration  
**Product:** Ansible Microsoft Windows  

This integration enables the management of Microsoft Windows hosts directly from platform using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the Windows hosts by utilising the Windows Remote Management (WinRM) API interface present in Windows 2008 and above combined with PowerShell. To use this integration, configure an instance of this integration. This will associate a credential to be used to access hosts when commands are run. The commands from this integration will take the Windows host address(es) as an input, and use the saved credential associated to the instance to execute. Create separate instances if multiple credentials are required. This integration uses NTLM for authentication. This ensures that actual credentials are never sent over the network, instead relying on hashing methods. By default, the initial authentication phase is performed unencrypted over HTTP, after which all communication is encrypted using a symmetric 256-bit key. If it is desired to use HTTPS from the onset, additional configuration on the Windows host is required. After WinRM is configured for HTTPS, update the port setting on the integration. Any port other than the default 5985 will use HTTPS communication

**Commands:**

- `win-gather-facts`: Gathers facts about remote hosts Further documentation available at https://docs.ansible.com/ansible/2.9/modules/gather_facts_module.html
- `win-acl`: Set file/directory/registry permissions for a system user or group Further documentation available at https://docs.ansible.com/ansible/2.9/modules/win_acl_modul
- `win-acl-inheritance`: Change ACL inheritance Further documentation available at https://docs.ansible.com/ansible/2.9/modules/win_acl_inheritance_module.html
- `win-audit-policy-system`: Used to make changes to the system wide Audit Policy Further documentation available at https://docs.ansible.com/ansible/2.9/modules/win_audit_policy_system_mod


## Ansible OpenSSL

**Type:** integration  
**Product:** Ansible Linux  

This integration enables the management of certificates on Linux hosts directly from platform using Ansible. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the hosts by utilising SSH combined with Python. To use this integration, configure an instance of this integration. This will associate a credential to be used to access hosts when commands are run. The commands from this integration will take the Linux host address(es) as an input, and use the saved credential associated to the instance to execute. Create separate instances if multiple credentials are required

**Commands:**

- `openssl-certificate`: Generate and/or check OpenSSL certificates Further documentation available at https://docs.ansible.com/ansible/2.9/modules/openssl_certificate_module.html
- `openssl-certificate-info`: Provide information of OpenSSL X.509 certificates Further documentation available at https://docs.ansible.com/ansible/2.9/modules/openssl_certificate_info_modul


## Ansible VMware

**Type:** integration  
**Product:** Ansible VMware  

This integration enables the management of VMware vCenter and ESXi hosts directly from platform using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the hosts by utilising VMware APIs

**Commands:**

- `vmware-about-info`: Provides information about VMware server to which user is connecting to Further documentation available at https://docs.ansible.com/ansible/2.9/modules/vmware_a


## Anthropic Claude

**Type:** integration  
**Product:** Anthropic Claude  

Designed to assist security professionals with security investigations, threat hunting, and anomaly detection, leveraging Anthropic Claude's natural language conversational capabilities

**Commands:**

- `claude-send-message`: Send a plain message to the selected Claude model and receive the generated response.
- `claude-check-email-header`: Checking email header for possible security issues. It is possible to keep asking questions on the provided info using 'claude-send-message'. Resets conversatio
- `claude-check-email-body`: Check email body for possible security issues. It is possible to keep asking questions on the provided info using 'claude-send-message'. Resets conversation con
- `claude-create-soc-email-template`: Create an email template out of the conversation context to be sent from the SOC.
- `claude-list-chats`: List chats metadata (Compliance API).
- `claude-list-groups`: List groups, or retrieve a single group when group_id is provided (Compliance API).
- `claude-get-events`: Manually retrieve Activity Feed events from the Anthropic Compliance API for testing and troubleshooting.
- `claude-list-roles`: List roles of an organization, or retrieve a single role when role_id is provided (Compliance API).
- `claude-list-projects`: List projects, or retrieve a single project when project_id is provided (Compliance API).
- `claude-list-project-attachments`: List the attachments of a project (Compliance API).
- `claude-list-organization-users`: List the users of an organization (Compliance API).
- `claude-list-role-permissions`: List the permissions of a role (Compliance API).
- `claude-list-group-members`: List the members of a group (Compliance API).
- `claude-get-project-document`: Retrieve a project document including its text content (Compliance API).
- `claude-list-organizations`: List the organizations under the parent organization (Compliance API).


## Anthropic Claude (Standard Connector)

**Type:** integration  
**Product:** Anthropic Claude (Standard Connector)  

This integration is configured automatically as part of the Anthropic Claude Standard Connector. Do not configure this integration directly — set it up from the connector page instead

**Commands:**

- `claude-chat-file-delete`: Permanently delete a Claude file (a conversation file or a project binary file) via the Compliance API. This is an irreversible hard delete, and it requires a C
- `claude-project-document-delete`: Permanently delete a Claude project document (a plain-text project_doc) via the Compliance API. This is an irreversible hard delete, and it requires a Complianc


## AnthropicClaudeApiModule

**Type:** script  

Common Anthropic Claude Compliance API code shared by: The module carries only what the two irreversible compliance delete commands (claude-chat-file-delete and claude-project-document-delete) need. The LLM client, the compliance list/get commands, and the event collector stay inline in the parent pack because they are not shared


## ANY.RUN Cloud Sandbox

**Type:** integration  
**Product:** ANY.RUN  

ANY.RUN is a cloud-based sandbox with interactive access

**Commands:**

- `anyrun-detonate-file-windows`: Perform File analysis using Windows VM.
- `anyrun-detonate-url-windows`: Perform URL analysis using Windows VM.
- `anyrun-detonate-file-linux`: Perform File analysis using Linux VM.
- `anyrun-detonate-url-linux`: Perform URL analysis using Linux VM.
- `anyrun-detonate-file-android`: Perform File analysis using Android VM.
- `anyrun-detonate-url-android`: Perform URL analysis using Android VM.
- `anyrun-get-user-limits`: Get user available limits to perform the Sandbox analysis.
- `anyrun-get-analysis-history`: Get analysis history.
- `anyrun-delete-task`: Deletes analysis task according to specified task uuid.
- `anyrun-get-analysis-report`: Returns the analysis report summary.
- `anyrun-download-analysis-pcap`: Returns the analysis network traffic dump.
- `anyrun-download-analysis-sample`: Returns the analysis file in zip archive. Archive password: infected.
- `anyrun-get-analysis-verdict`: Returns a threat level text. Possible values: No threats detected, Suspicious activity, Malicious activity.


## ANY.RUN TI Lookup

**Type:** integration  
**Product:** ANY.RUN  

TI Lookup is a searchable database of IOCs, IOAs, IOBs, and events for threat hunting and a service for browsing malicious files by their content

**Commands:**

- `anyrun-get-intelligence`: Perform threat intelligence using specified IOC
- `ip`: Check the IP address reputation.
- `domain`: Check the Domain name reputation.
- `url`: Check the URL reputation.
- `file`: Check the SHA256 hash reputation.


## AnyLlmAddResultsConvo

**Type:** script  
**Product:** Anything LLM  

Takes search results and adds them to the LLM conversation context. Adding these results to the context is done invisibly in platform, but is present in the LLM and will display in the conversation when the workspace is re-entered


## AnyLlmClearConvo

**Type:** script  
**Product:** Anything LLM  

Clears the current workspace conversation buffer stored in an platform field and deletes the LLM's workspace conversation thread. The next question starts a new conversation thread with empty LLM context


## AnyLlmClearResults

**Type:** script  
**Product:** Anything LLM  

Clears the current search results


## AnyLlmDocuments

**Type:** script  
**Product:** Anything LLM  

Queries the LLM for the list of documents that have been uploaded and copies it into an platform grid field for display and additional actions

**Inputs:**

- `documentsfield`: platform grid field name for the documents list.


## AnyLlmDocumentsUpdate

**Type:** script  
**Product:** Anything LLM  

When an action is requested in the documents grid field, executes the requested action (Embed or Delete) on a document in the LLM. "Delete" removes the document from the LLM's document catalog, and "Embed" adds the vector embedding of the document to the current workspace

**Inputs:**

- `new`: 
- `old`: 


## AnyLlmQuestion

**Type:** script  
**Product:** Anything LLM  

Sends a message to the LLM. If any search results have been added to the conversation, they are added to the LLM workspace thread's context just before the latest message is added. The pending search results buffer is then cleared

**Inputs:**

- `question`: The question or message to send to the LLM
- `mode`: "chat" mode uses the LLMs full training data and "query" mode requires some results found in the embedded documents in addition to the LLM's


## AnyLlmSaveConvo

**Type:** script  
**Product:** Anything LLM  

Saves the current conversation as a war room entry


## AnyLlmSearchDocument

**Type:** script  
**Product:** Anything LLM  

Full text search of a LLM document for a text pattern (regex) for more results as a companion to similarity search that returns a few top results. Currently supports only war room file entries, search results, and text that has been preprocessed in platform prior to uploading to the LLM. (See AnyLlmUploadText, AnyLlmUploadFileEntry and AnyLlmUploadDocument). Results are placed in the search results buffer for where they can be added to the LLM's conversation context

**Inputs:**

- `title`: title of the LLM document to search with the platform file entry ID. Example: "37@25496_anythingllm.txt"
- `pattern`: regex to search text for [ see re.findall() ]


## AnyLlmUploadDocument

**Type:** script  
**Product:** Anything LLM  

Uploads pre-processed text data to the LLM's document catalog. The document data must have been prepared by AnyLlmUploadText, AnyLlmUploadFileEntry, AnyLlmUploadResults. Text documentation processed and uploaded by this method can also be full text searched


## AnyLlmUploadFileEntry

**Type:** script  
**Product:** Anything LLM  

Processes a war room file entry for uploading as an LLM document by AnyLlmUploadDocument so that a full text search can also be performed on the document after uploading

**Inputs:**

- `name`: name of the file uploaded to the war room


## AnyLlmUploadResults

**Type:** script  
**Product:** Anything LLM  

Processes search results for uploading as an LLM document by AnyLlmUploadDocument so that a full text search can also be performed on the document after uploading

**Inputs:**

- `title`: title of the LLM document
- `author`: author of the LLM document
- `description`: description of the LLM document
- `source`: source of the LLM document


## AnyLlmUploadText

**Type:** script  
**Product:** Anything LLM  

Processes text data for uploading as an LLM document by AnyLlmUploadDocument and so that a full text search can also be performed on the document after uploading

**Inputs:**

- `text`: text content for the LLM document
- `title`: title of the LLM document
- `author`: author of the LLM document
- `description`: description of the LLM document
- `source`: source of the LLM document


## AnyLlmUploadWebLink

**Type:** script  
**Product:** Anything LLM  

Uploads a web link as a LLM document. Does not currently support full text search

**Inputs:**

- `link`: web link to upload as LLM document
- `title`: title of the LLM document
- `author`: author of the LLM document
- `description`: description of the LLM document
- `source`: source of the LLM document


## AnyLlmWorkspaceEmbeddings

**Type:** script  
**Product:** Anything LLM  

List the current LLM workspace's embedded documents in an platform grid field

**Inputs:**

- `workspace`: name of the LLM workspace.
- `embeddingfield`: platform grid field name for the documents list.


## AnyLlmWorkspaceEmbeddingsUpdate

**Type:** script  
**Product:** Anything LLM  

Executes the actions taken on an embedded document in the grid field. "Pin" adds the entire document to the LLM's conversation context. Care should be taken not to pin very large documents that may impact the conversation's context negatively. "Unpin" removes the pinning of the document to the workspace. "Remove" removes the document's embedding from the workspace

**Inputs:**

- `new`: field new value
- `old`: field old value


## AnyLlmWorkspaces

**Type:** script  
**Product:** Anything LLM  

Queries the LLM for a list of workspaces and copies it into an platform grid field were the user can select an active workspace

**Inputs:**

- `workspacegrid`: platform grid field name for the workspace list.


## AnyLlmWorkspaceUpdate

**Type:** script  
**Product:** Anything LLM  

Executes the action taken on a workspace listed in the grid field. "Current" makes the workspace the active workspace and any workspace setting changes are updated in the LLM

**Inputs:**

- `new`: field new value
- `old`: field old value


## AnyMatch

**Type:** script  
**Product:** Filters And Transformers  

This filter accepts two inputs, left and right, each of which can be either a single element of any type (e.g., string, int, etc.) or a list of elements. The filter iterates over each element in the left input and returns all elements that have a substring that is equal to an element from the right side. The matching process is case-insensitive, meaning it disregards letter case during the comparison. All inputs are treated either as a string or as a list of strings, if it contains a comma. A JSON is always treated as a string. Since the comparison treats all inputs as strings, integers and strings are considered equal during the evaluation

**Inputs:**

- `left`: Value to check if it has a substring that is equal to an element in the right side. Can be a single value or a comma-separated list.
- `right`: Value to check if it is equal to an element or to a substring of an element from the left. Can be a single value or a comma-separated list.


## ANYRUN Detonate File Android

**Type:** playbook  
**Product:** ANY.RUN  

This playbook submits a file extracted from an incident attachment to the ANY.RUN cloud sandbox for dynamic analysis in an Android environment. It helps to automate malware detonation and behavior observation on Android OS

**Inputs:**

- `Using`: The name of the ANY.RUN Cloud Sandbox integration instance to use for running commands in this playbook. If left empty, and more than one in
- `file`: The existing War Room file EntryID to submit for analysis.
- `env_locale`: The operating system language. Use locale identifier or country name (for example, "en-US" or "Brazil"). Case insensitive.
- `opt_network_connect`: Whether to enable network connection.
- `opt_network_fakenet`: Whether to enable the FakeNet feature.
- `opt_network_tor`: Whether to use TOR.
- `opt_network_geo`: The TOR geo location option, for example US, AU.
- `opt_network_mitm`: Whether to use the HTTPS MITM proxy.


## ANYRUN Detonate File Android for XDR

**Type:** playbook  
**Product:** ANY.RUN  

This playbook submits a file from a Cortex XDR issue to the ANY.RUN Cloud Sandbox for dynamic analysis in an Android environment and automates malware detonation and behavior observation on Android OS

**Inputs:**

- `Using`: The name of the ANY.RUN Cloud Sandbox integration instance to use for running commands in this playbook. If left empty, and more than one in
- `AutoAddIOCsToXDR`: Whether to automatically add malicious and suspicious ANY.RUN IOCs (Unknown reputation IOCs are always excluded) to Cortex XDR IOC rules. Se
- `file_entry_id`: The existing War Room file EntryID to submit to ANY.RUN Android analysis.
- `env_locale`: The operating system language. Use locale identifier or country name (for example, "en-US" or "Brazil"). Case insensitive.
- `opt_network_connect`: Whether to enable network connection.
- `opt_network_fakenet`: Whether to enable the FakeNet feature.
- `opt_network_tor`: Whether to use TOR.
- `opt_network_geo`: The TOR geo location option, for example US, AU.


## ANYRUN Detonate File Linux

**Type:** playbook  
**Product:** ANY.RUN  

This playbook submits a file extracted from an incident attachment to the ANY.RUN cloud sandbox for dynamic analysis in an Linux environment. It helps to automate malware detonation and behavior observation on Linux OS

**Inputs:**

- `Using`: The name of the ANY.RUN Cloud Sandbox integration instance to use for running commands in this playbook. If left empty, and more than one in
- `file`: The existing War Room file EntryID to submit for analysis.
- `run_as_root`: Whether to run the file with superuser privileges.
- `env_locale`: The operating system language. Use locale identifier or country name (for example, "en-US" or "Brazil"). Case insensitive.
- `env_os`: The operating system. Possible values: ubuntu, debian.
- `opt_network_connect`: Whether to enable network connection.
- `opt_network_fakenet`: Whether to enable the FakeNet feature.
- `opt_network_tor`: Whether to use TOR.


## ANYRUN Detonate File Linux for XDR

**Type:** playbook  
**Product:** ANY.RUN  

This playbook submits a file retrieved from a Cortex XDR endpoint to the ANY.RUN Cloud Sandbox for dynamic analysis in a Linux environment and automates malware detonation and behavior observation on Linux OS

**Inputs:**

- `Using`: The name of the ANY.RUN Cloud Sandbox integration instance to use for running commands in this playbook. If left empty, and more than one in
- `AutoAddIOCsToXDR`: Whether to automatically add malicious and suspicious ANY.RUN IOCs (Unknown reputation IOCs are always excluded) to Cortex XDR IOC rules. Se
- `file_entry_id`: The existing War Room file EntryID. If provided, endpoint retrieval is skipped and this file is submitted to ANY.RUN.
- `endpoint_id`: The Cortex XDR endpoint/agent ID. Used only when file_entry_id is not provided.
- `file_path`: The full Linux path to the file on the endpoint. Used for retrieval and filename matching when file_entry_id is not provided.
- `retrieve_timeout_seconds`: The timeout for Cortex XDR file retrieve polling.
- `retrieve_poll_interval_seconds`: The polling interval for Cortex XDR file retrieve action status checks.
- `env_locale`: The operating system language. Use locale identifier or country name (for example, "en-US" or "Brazil"). Case insensitive.


## ANYRUN Detonate File Windows

**Type:** playbook  
**Product:** ANY.RUN  

This playbook submits a file extracted from an incident attachment to the ANY.RUN cloud sandbox for dynamic analysis in an Windows environment. It helps to automate malware detonation and behavior observation on Windows OS

**Inputs:**

- `Using`: The name of the ANY.RUN Cloud Sandbox integration instance to use for running commands in this playbook. If left empty, and more than one in
- `file`: The existing War Room file EntryID to submit for analysis.
- `env_locale`: The operating system language. Use locale identifier or country name (for example, "en-US" or "Brazil"). Case insensitive.
- `env_bitness`: The bitness of the operating system. Supports: 32, 64.
- `env_version`: The version of the OS. Supports: 7, 10, 11.
- `env_type`: The environment preset type. You can select **development** env for OS Windows 10 x64. For all other cases, **complete** env is required.
- `opt_network_connect`: Whether to enable network connection.
- `opt_network_fakenet`: Whether to enable the FakeNet feature.


## ANYRUN Detonate File Windows for XDR

**Type:** playbook  
**Product:** ANY.RUN  

This playbook submits a file retrieved from a Cortex XDR endpoint to the ANY.RUN Cloud Sandbox for dynamic analysis in a Windows environment. It automates malware detonation and behavior observation on Windows OS

**Inputs:**

- `Using`: The name of the ANY.RUN Cloud Sandbox integration instance to use for running commands in this playbook. If left empty, and more than one in
- `AutoAddIOCsToXDR`: Whether to automatically add malicious and suspicious ANY.RUN IOCs (Unknown reputation IOCs are always excluded) to Cortex XDR IOC rules. Se
- `file_entry_id`: The existing War Room file EntryID. If provided, endpoint retrieval is skipped and this file is submitted to ANY.RUN.
- `endpoint_id`: The Cortex XDR endpoint/agent ID. Used only when file_entry_id is not provided.
- `file_path`: The full path to the file on the endpoint. Used for retrieval and for extracting the filename used to select the original file after unzip.
- `retrieve_timeout_seconds`: The timeout for Cortex XDR file retrieve polling.
- `retrieve_poll_interval_seconds`: The polling interval for Cortex XDR file retrieve action status checks.
- `env_locale`: The operating system language. Use locale identifier or country name (for example, "en-US" or "Brazil"). Case insensitive.


## ANYRUN Detonate Url Android

**Type:** playbook  
**Product:** ANY.RUN  

This playbook submits a URL extracted from an indicator to the ANY.RUN cloud sandbox for dynamic analysis in an Android environment. It automates the analysis of potentially malicious URLs on Android OS

**Inputs:**

- `Using`: The name of the ANY.RUN Cloud Sandbox integration instance to use for running commands in this playbook. If left empty, and more than one in
- `obj_url`: The target URL. Size range 5-512. Example: (http/https)://(your-link).
- `env_locale`: The operating system language. Use locale identifier or country name (for example, "en-US" or "Brazil"). Case insensitive.
- `opt_network_connect`: Whether to enable network connection.
- `opt_network_fakenet`: Whether to enable the FakeNet feature.
- `opt_network_tor`: Whether to use TOR.
- `opt_network_geo`: The TOR geo location option, for example US, AU.
- `opt_network_mitm`: Whether to use the HTTPS MITM proxy.


## ANYRUN Detonate URL Android for XDR

**Type:** playbook  
**Product:** ANY.RUN  

This playbook submits a URL from a Cortex XDR issue to the ANY.RUN Cloud Sandbox for dynamic analysis in an Android environment and automates malware detonation and behavior observation on an Android Environment

**Inputs:**

- `Using`: The name of the ANY.RUN Cloud Sandbox integration instance to use for running commands in this playbook. If left empty, and more than one in
- `AutoAddIOCsToXDR`: Whether to automatically add malicious and suspicious ANY.RUN IOCs (Unknown reputation IOCs are always excluded) to Cortex XDR IOC rules. Se
- `obj_url`: The target URL to submit to ANY.RUN. By default, this playbook uses the Cortex XDR normalized target URL field xdm.target.url (${issue.xdmta
- `env_locale`: The operating system language. Use locale identifier or country name (for example, "en-US" or "Brazil"). Case insensitive.
- `opt_network_connect`: Whether to enable network connection.
- `opt_network_fakenet`: Whether to enable the FakeNet feature.
- `opt_network_tor`: Whether to use TOR.
- `opt_network_geo`: The TOR geo location option, for example US, AU.


## ANYRUN Detonate Url Linux

**Type:** playbook  
**Product:** ANY.RUN  

This playbook submits a URL extracted from an indicator to the ANY.RUN cloud sandbox for dynamic analysis in an Linux environment. It automates the analysis of potentially malicious URLs on Linux OS

**Inputs:**

- `Using`: The name of the ANY.RUN Cloud Sandbox integration instance to use for running commands in this playbook. If left empty, and more than one in
- `obj_url`: The target URL. Size range 5-512. Example: (http/https)://(your-link).
- `env_locale`: The operating system language. Use locale identifier or country name (for example, "en-US" or "Brazil"). Case insensitive.
- `env_os`: The operating system. Possible values: ubuntu, debian.
- `opt_network_connect`: Whether to enable network connection.
- `opt_network_fakenet`: Whether to enable the FakeNet feature.
- `opt_network_tor`: Whether to use TOR.
- `opt_network_geo`: The TOR geo location option, for example US, AU.


## ANYRUN Detonate URL Linux for XDR

**Type:** playbook  
**Product:** ANY.RUN  

This playbook submits a URL from a Cortex XDR issue to the ANY.RUN Cloud Sandbox for dynamic analysis in a Linux environment. It helps to automate malware detonation and behavior observation on Linux OS

**Inputs:**

- `Using`: The name of the ANY.RUN Cloud Sandbox integration instance to use for running commands in this playbook. If left empty, and more than one in
- `AutoAddIOCsToXDR`: Whether to automatically add malicious and suspicious ANY.RUN IOCs (Unknown reputation IOCs are always excluded) to Cortex XDR IOC rules. Se
- `obj_url`: The target URL to submit to ANY.RUN. By default, this playbook uses the Cortex XDR normalized target URL field xdm.target.url (${issue.xdmta
- `env_locale`: The operating system language. Use locale identifier or country name (for example, "en-US" or "Brazil"). Case insensitive.
- `env_os`: The operating system. Possible values: ubuntu, debian.
- `opt_network_connect`: Whether to enable network connection.
- `opt_network_fakenet`: Whether to enable the FakeNet feature.
- `opt_network_tor`: Whether to use TOR.


## ANYRUN Detonate Url Windows

**Type:** playbook  
**Product:** ANY.RUN  

This playbook submits a URL extracted from an indicator to the ANY.RUN cloud sandbox for dynamic analysis in an Windows environment. It automates the analysis of potentially malicious URLs on Windows OS

**Inputs:**

- `Using`: The name of the ANY.RUN Cloud Sandbox integration instance to use for running commands in this playbook. If left empty, and more than one in
- `obj_url`: The target URL. Size range 5-512. Example: (http/https)://(your-link).
- `env_locale`: The operating system language. Use locale identifier or country name (for example, "en-US" or "Brazil"). Case insensitive.
- `env_bitness`: The bitness of the operating system. Supports: 32, 64.
- `env_version`: The version of the OS. Supports: 7, 10, 11.
- `env_type`: The environment preset type. You can select **development** env for OS Windows 10 x64. For all other cases, **complete** env is required.
- `opt_network_connect`: Whether to enable network connection.
- `opt_network_fakenet`: Whether to enable the FakeNet feature.


## ANYRUN Detonate URL Windows for XDR

**Type:** playbook  
**Product:** ANY.RUN  

This playbook submits a URL from a Cortex XDR issue to the ANY.RUN Cloud Sandbox for dynamic analysis in a Windows environment. It helps to automate malware detonation and behavior observation on Windows OS

**Inputs:**

- `Using`: The name of the ANY.RUN Cloud Sandbox integration instance to use for running commands in this playbook. If left empty, and more than one in
- `AutoAddIOCsToXDR`: Whether to automatically add malicious and suspicious ANY.RUN IOCs (Unknown reputation IOCs are always excluded) to Cortex XDR IOC rules. Se
- `obj_url`: The target URL to submit to ANY.RUN. By default, this playbook uses the Cortex XDR normalized target URL field xdm.target.url (${issue.xdmta
- `env_locale`: The operating system language. Use locale identifier or country name (for example, "en-US" or "Brazil"). Case insensitive.
- `env_bitness`: The bitness of the operating system. Supports: 32, 64.
- `env_version`: The version of the OS. Supports: 7, 10, 11.
- `env_type`: The environment preset type. You can select **development** env for OS Windows 10 x64. For all other cases, **complete** env is required.
- `opt_network_connect`: Whether to enable network connection.


## AnythingLLM

**Type:** integration  
**Product:** Anything LLM  

Retrieval Augmented Generation (RAG) with LLM and Vector DB that can be local for full data privacy or cloud-based for greater functionality

**Commands:**

- `anyllm-document-upload-file`: Uploads an platform file entry to the custom-documents folder.
- `anyllm-document-upload-link`: Uploads a web link to the custom-documents folder
- `anyllm-document-upload-text`: Upload text content as a document to the custom-documents folder
- `anyllm-workspace-new`: Creates a new workspace in AnythingLLM
- `anyllm-workspace-delete`: Deletes an AnythingLLM workspace
- `anyllm-workspace-list`: List all the workspaces in AnythingLLM
- `anyllm-workspace-get`: Get a specific workspace details
- `anyllm-workspace-settings`: Update workspace settings
- `anyllm-workspace-add-embedding`: Add a document to a workspace and create its vector embedding in the workspace
- `anyllm-workspace-delete-embedding`: Delete a document embedding from the workspace
- `anyllm-document-createfolder`: Create a new document folder
- `anyllm-document-move`: Move a document from a source folder to a destination folder
- `anyllm-document-delete`: Delete a document
- `anyllm-workspace-chat`: Send a chat message to a workspace (default thread). Query mode is based on embedded documents in chat, whereas chat mode is more general.
- `anyllm-workspace-stream-chat`: Send a stream chat message to a workspace (default thread). Query mode is based on embedded documents in chat, whereas chat mode is more general


## appNovi

**Type:** integration  
**Product:** AppNovi  

Search across meshed network, security, and business data in appNovi to make efficient informed security decisions for risk management and incident response. Gain immediate intelligence on assets, visualize risk and threats across your network, and undertake interactive investigations across the network to reduce MTTR for incident response. This integration was integrated and tested with appNovi v2.0

**Commands:**

- `search-appnovi-components`: Search for Components by name or value
- `search-appnovi-connected`: Search for Components connected to supplied identity
- `search-appnovi-cve`: Search for servers with matching CVE
- `search-appnovi-component-property`: Search for Components by property and value
- `search-appnovi-server-by-ip`: Search for servers using IP address


## appNovi-MAC-Address-Lookup

**Type:** playbook  
**Product:** AppNovi  

Lookup servers and IPs by MAC address

**Inputs:**

- `mac_address`: mac address


## AquatoneDiscoverV2

**Type:** script  
**Product:** Common Scripts  

Finds the targets nameservers and shuffle DNS lookups between them. If a lookup fails on the target domains nameservers, Aquatone Discover will use the Google public DNS servers to maximize discovery

**Inputs:**

- `domain`: The domain to discover.


## Arcanna.AI

**Type:** integration  
**Product:** ArcannaAI  

Arcanna integration for using the power of AI in SOC This integration was integrated and tested with version 1.45.1 of Arcanna.AI

**Commands:**

- `arcanna-get-jobs`: Get jobs list
- `arcanna-send-event`: Sends a raw event to Arcanna


## ArcannaFeedbackPostProcessing

**Type:** script  
**Product:** ArcannaAI  

This Script is a post-processing-script that can be used as a starter to send Arcanna.ai feedback when an analyst performs investigation. Script can also be used with Arcanna-Generic-Investigation-V2 playbook

**Inputs:**

- `closing_user`: username used to trigger script
- `closing_reason`: closing reasong used to trigger script
- `closing_notes`: closing notes used to trigger script


## ArcherCreateIncidentExample

**Type:** script  
**Product:** RSA Archer  

This script is an example script of how to create Incident in Archer. The script generates the created incident data in JSON format and execute the command archer-create-record

**Inputs:**

- `summary`: Incident summary
- `priority`: Incident priority
- `category`: Incident category


## Arcsight - Get events related to the Case

**Type:** playbook  
**Product:** ArcSight ESM  

Gets the case's Arcsight ResourceID from the FetchID field, or the "ID" label. If neither are there, it will ask the user for the ID. Uses the resource ID to get full data for the case, the correlated/aggregate events underneath it, and all base events underneath them


## ArcSight ESM v2

**Type:** integration  
**Product:** ArcSight ESM  

ArcSight ESM is a security information and event management (SIEM) product. It collects security log data from an enterprise’s security technologies, operating systems, applications and other log sources, and analyzes that data for signs of compromise, attacks or other malicious activity. The product generates cases to security administrators and analysts. ArcSight XML is no longer supported. Use the ArcSight ESM integration instead

**Commands:**

- `as-get-all-cases`: (Deprecated) Retrieves all case resource IDs.
- `as-get-case`: Gets information about a single case.
- `as-get-matrix-data`: Retrieves query viewer results (query viewer must be configured to be refreshed every minute, see documentation)
- `as-add-entries`: Adds new entries to the Active List.
- `as-clear-entries`: Deletes all entries in the Active List.
- `as-get-entries`: Returns all entries in the Active List
- `as-get-entries`: Returns up to 2000 entries.
- `as-get-security-events`: Returns the security event details
- `as-get-case-event-ids`: Returns all case event IDs.
- `as-update-case`: Updates a specific case.
- `as-get-all-query-viewers`: Returns all the query viewer IDs.
- `as-case-delete`: Deletes a case
- `as-get-query-viewer-results`: Retrieves query viewer results (query viewer must be configured to be refreshed every minute, see documentation)
- `as-fetch-incidents`: Fetches incidents
- `as-delete-entries`: Delete entries from the Active List.


## ArcusTeam

**Type:** integration  
**Product:** ArcusTeam  

The ArcusTeam API allows the user to inspect connected devices' attack surface. By feeding device identifiers and the software it runs: DeviceTotal will return a map of the device’s attack surface. DeviceTotal was built from the ground up in order to provide complete visibility into connected devices and mitigate 3rd party risk. DeviceTotal can continuously identify & predict such that the connected device security posture is being assessed, prioritized and mitigated effectively. This integration was integrated and tested with version 6.11.0 of ArcusTeam

**Commands:**

- `arcusteam-get-devices`: Find ArcusTeam Device


## Arduino

**Type:** integration  
**Product:** Arduino  

Connects to and controls an Arduino pin system using the network

**Commands:**

- `arduino-set-pin`: Requests that a pin be set
- `arduino-get-pin`: Requests the value of a pin
- `arduino-send-data`: Send arbitrary data to the Arduino


## Arkime

**Type:** integration  
**Product:** Arkime  

Arkime (formerly Moloch) is a large scale, open source, indexed packet capture and search tool. This integration was integrated and tested with version 3.4.1 (API v3) of Arkime. For older versions, see the Moloch pack (deprecated)

**Commands:**

- `arkime-connection-list`: Gets a list of nodes and links and returns them to the client.
- `arkime-connection-csv-get`: Gets a list of nodes and links in csv format and returns them to the client.
- `arkime-session-pcap-get`: Retrieve the raw session data in pcap format.
- `arkime-session-csv-get`: Gets a list of sessions and returns them as CSV to the client.
- `arkime-session-list`: Gets a list of sessions and returns them to the client.
- `arkime-unique-field-list`: Gets a list of unique field values (with or without counts) and sends them to the client.
- `arkime-multi-unique-field-list`: Gets an intersection of unique field values (with or without counts) and sends them to the client.
- `arkime-field-list`: Gets available database field objects pertaining to sessions.
- `arkime-spigraph-get`: Gets a list of values for a field with counts and graph data and returns them to the client.
- `arkime-spiview-get`: Gets a list of field values with counts and returns them to the client.
- `arkime-session-tag-add`: Add tag(s) to individual session(s) by id or by query.
- `arkime-session-tag-remove`: Removes tag(s) from individual session(s) by id or by query.
- `arkime-pcap-file-list`: Gets a list of PCAP files that Arkime knows about.


## Armis

**Type:** integration  
**Product:** Armis  

Use the Armis integration to search alerts and devices, tag and untag devices, and set alert statuses. This integration was integrated and tested with the latest version of Armis

**Commands:**

- `armis-search-alerts`: Search Armis Alerts.
- `armis-update-alert-status`: Updates the status for an alert.


## Armorblox

**Type:** integration  
**Product:** Armorblox  

Armorblox is an API-based platform that stops targeted email attacks, protects sensitive data, and automates incident response. This integration was integrated and tested with version 4.3.0 of Armorblox

**Commands:**

- `armorblox-check-remediation-action`: Check the recommended remediation action for any incident
- `fetch-incidents`: Gets a list of armorblox incidents


## Armorblox Needs Review

**Type:** playbook  
**Product:** Armorblox  

This playbook sends email alerts to admins for Armorblox incidents that need review

**Inputs:**

- `recipient_mail_address`: Receiver's mailing address.


## ArrayAnyMatch

**Type:** script  
**Product:** Filters And Transformers  

Returns true if an element is shared between two lists

**Inputs:**

- `left`: Left list.
- `right`: Right list.


## ArrayToCSV

**Type:** script  
**Product:** Common Scripts  

Converts a simple Array into a textual comma separated string

**Inputs:**

- `value`: An array of strings input


## Asimily Asset Info Enrich

**Type:** playbook  
**Product:** Asimily Insight  

Default playbook for Asimily Anomaly and CVE incidents. It enriches incidents by running asimily-get-asset-details to fetch related asset information


## Asimily Insight

**Type:** integration  
**Product:** Asimily Insight  

Integrate Asimily Insight to ingest security anomalies, CVEs, and leverage detailed asset data for streamlined incident investigation. Asimily Insight delivers comprehensive IoT/OT security and management by providing deep asset visibility, automated vulnerability prioritization, and actionable mitigation strategies aligned with MITRE ATT&CK. It analyzes device communication, calculates holistic risk scores, and enables targeted network segmentation. The platform detects anomalies, simplifies policy management, and automates forensic packet capture. Beyond security, Asimily optimizes asset utilization, tracks operational usage, and manages configuration drift. Its Risk Simulator improves efficiency, and centralized data streamlines IT/OT convergence while identifying unmanaged devices. This integration utilizes the Asimily Insight RESTful APIs to provide seamless access to comprehensive device data. Users can retrieve detailed information on IT, medical, and security parameters, as well as view known vulnerabilities (CVEs), detect asset anomalies, and maintain synchronized data—either on a regular schedule or on demand

**Commands:**

- `asimily-get-asset-details`: Fetch assets details from Asimily Insight. You can add argument filters.
- `asimily-get-asset-anomalies`: Fetch anomaly alerts from Asimily Insight. You can add argument filters.
- `asimily-get-asset-vulnerabilities`: Fetch device CVEs from Asimily Insight. You can add argument filters.


## AsimilyExtraAssetContextData

**Type:** script  
**Product:** Asimily Insight  

The script will be used for extracting asset information from context data from incidents. If playbook is applied to call asimily-get-asset-details for incidents to retrieve asset details, fetched information will be saved in incident's context data under Asimily->Asset


## Assess Wiz Issues

**Type:** playbook  
**Product:** Wiz  

Example basic Playbook to assess Wiz Issues


## Assess WizDefend Detections

**Type:** playbook  
**Product:** Wiz  

This playbook provides a structured workflow for assessing and investigating Wiz Detections that come from the WizDefend integration. The playbook includes built-in validation to ensure proper integration setup before execution and automatically retrieves associated threat information when available


## AssociateIndicatorsToIncident

**Type:** script  
**Product:** DomainTools Iris Investigate  

Associate Indicators to an Incident


## Ataya - Securely logging device access to network

**Type:** playbook  
**Product:** Ataya  

With this playbook, we can enable Identity-Aware Security Across Multiaccess Networks


## Ataya Harmony

**Type:** integration  
**Product:** Ataya  

Use the Ataya Harmony integration, we can achieve the security access control which assign the user through the api access token

**Commands:**

- `ataya-assign-user`: After assign the user on ataya harmony, user can successfully register to harmony


## Atlassian Confluence Server

**Type:** integration  
**Product:** Atlassian Confluence Server  

Atlassian Confluence Server API. This integration was integrated and tested with version 6.1 of Atlassian Confluence Server

**Commands:**

- `confluence-create-space`: Creates a new Confluence space.
- `confluence-create-content`: Creates Confluence content for a given space.
- `confluence-list-spaces`: Returns a list of all Confluence spaces.
- `confluence-get-content`: Returns Confluence content by space key and title.
- `confluence-get-page-as-pdf`: Returns Confluence Page as PDF by PageID.
- `confluence-delete-content`: Deletes Confluence content.
- `confluence-update-content`: Update (overwrite) the existing content of a Confluence page with new content.
- `confluence-search-content`: Fetches a list of content using the Confluence Query Language (CQL). For more information about CQL syntax, see https://developer.atlassian.com/server/confluenc


## Atlassian IAM

**Type:** integration  
**Product:** Atlassian IAM  

Note: This integration should be used as part of our IAM premium pack. For further details, visit our IAM pack documentation. For more information, please refer to the Identity Lifecycle Management article. Integrate with Atlassian's services to execute generic ILM management operations such as create, update, delete, etc, for employee lifecycle processes

**Commands:**

- `iam-create-user`: Creates a user.
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Disable an active user.


## Atlassian Jira Service Management

**Type:** integration  
**Product:** Atlassian Jira Service Management  

Use this integration to manage Jira objects and attach files to Jira objects from the platform. This integration was integrated and tested with version 5.4.15 of AtlassianJiraServiceManagement

**Commands:**

- `jira-asset-object-schema-list`: List all object schemas.
- `jira-asset-object-type-list`: List all object types.
- `jira-asset-object-type-attribute-list`: List all attributes for an object type.
- `jira-asset-object-create`: Create a new object of the specified object type ID. Either attributes or attributes_json must be provided.
- `jira-asset-object-update`: Updates an existing object of specified object type ID. Either attributes or attributes_json must be provided.
- `jira-asset-object-delete`: Deletes an existing object of the specified object ID.
- `jira-asset-object-get`: Retrieves the object with the specified object ID.
- `jira-asset-object-search`: Searches for objects of the specified object type.
- `jira-asset-attribute-json-create`: Utility command used to create a JSON file with all attributes of the specified object type. All that is left is to fill in the values of each attribute.
- `jira-asset-comment-create`: Creates a comment for the specified object.
- `jira-asset-connected-ticket-list`: Returns a list of all connected tickets for the specified object.
- `jira-asset-comment-list`: Returns a list of comments for the specified object.
- `jira-asset-attachment-add`: Uploads a file attachment to the specified object.
- `jira-asset-attachment-list`: Returns a list of attachments for the specified object. You can also download the files in a zipped format.
- `jira-asset-attachment-remove`: Removes an attachment from a specific object.


## Atlassian Jira v3

**Type:** integration  
**Product:** Atlassian Jira  

Use the Jira integration to manage issues and create the platform. From the platform.0 and above, the integration also mirrors issues to existing issue incidents in the platform. The integration now supports both OnPrem, and Cloud instances. This integration was integrated and tested with: Jira Cloud Platform V3 (for Cloud), Jira Software Cloud (for Cloud), Jira Server Platform 9.6.0 (for OnPrem), Jira Software Server 9.6.0 (for OnPrem). Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `jira-issue-get-attachment`: Download attachments for a specific issue (Will download a file to War Room).
- `jira-delete-issue`: Deletes an issue in Jira. Issue's sub-tasks will also be deleted if there are any.
- `jira-get-specific-field`: Gets specific fields from a Jira issue and adds it to context dynamically.
- `jira-issue-add-link`: Creates (or updates) an issue link.
- `jira-get-id-by-attribute`: Gets the account ID for a given user attribute.
- `jira-issue-query`: Queries Jira issues.
- `jira-get-id-offset`: Returns the ID offset, which is the ID of the first issue that was created in the current Jira instance, or the ID of the first issue with respect to the given 
- `jira-issue-add-comment`: Adds a new comment to an existing Jira issue.
- `jira-issue-upload-file`: Uploads a file attachment to an issue.
- `jira-issue-delete-file`: Delete an attachment from an issue.
- `jira-list-transitions`: Lists all possible transitions for a given ticket in its current status.
- `jira-edit-issue`: Modifies an issue in Jira. If the status or transition fields are given, then the other supplied fields should appear on the transition screen.
- `jira-issue-assign`: Assigns an assignee to an existing issue.
- `jira-create-issue`: Creates a new issue in Jira.
- `jira-get-issue`: Fetches an issue from Jira.


## AtlassianApiModule

**Type:** script  

This API module provides shared OAuth 2.0 authentication functionality for Atlassian products (Jira, Confluence), supporting both Cloud and On-Prem/Data Center instances


## AttackIQ Platform

**Type:** integration  
**Product:** AttackIQ Platform  

Use the AttackIQ integration to simulate a platform that provides validations for security controls, responses, and remediation exercises. This integration was integrated and tested with AttackIQ FireDrill v2.15.96

**Commands:**

- `attackiq-get-assessment-by-id`: Returns all assessment information by ID.
- `attackiq-list-assessments`: Returns all assessment details by page.
- `attackiq-activate-assessment`: Deprecated, without available replacement. Activates the assessment, which is required for execution.
- `attackiq-run-all-tests-in-assessment`: Runs all tests in the assessment.
- `attackiq-get-assessment-execution-status`: Returns an assessment execution status when running an on-demand execution only.
- `attackiq-get-test-execution-status`: Returns the status of the test.
- `attackiq-list-tests-by-assessment`: Returns a list of tests by an assessment.
- `attackiq-get-test-results`: Returns the test results of an assessment.
- `attackiq-list-assessment-templates`: Lists all available assessment templates.
- `attackiq-list-assets`: Lists all assets.
- `attackiq-create-assessment`: Creates a new assesment.
- `attackiq-add-assets-to-assessment`: Adds assets or asset groups to an assesment.
- `attackiq-delete-assessment`: Deletes an assessment.


## Augur Security

**Type:** integration  
**Product:** Augur Security  

Leverage Augur's preemptive threat intelligence for actionable data against persistent threat actors. Augur Security return a list which could include IP addresses, domains, URLs, and hash indicators which are updated daily

**Commands:**

- `augur-get-daily-indicators`: Get daily indicators from Augur.
- `augur-get-file-hash-context`: Get threat context of a file hash from the Augur API.
- `augur-get-host-context`: Get threat context of a host name from the Augur API.
- `augur-get-ip-context`: Get threat context of a ipv4 address from the Augur API.


## Automox

**Type:** integration  
**Product:** Automox  

Use the Automox integration to create device groups, update devices, run policies, and remediate vulnerabilities of devices through the Automox platform. This integration was integrated and tested as of 2022-03-21 with the Automox API

**Commands:**

- `automox-devices-list`: List all devices in Automox based on group and organization permissions.
- `automox-organizations-list`: List all Automox organizations based on user permissions.
- `automox-organization-users-list`: List all Automox users within an organization.
- `automox-vulnerability-sync-batch-action`: Perform an action on an Automox Vulnerability Sync batch.
- `automox-vulnerability-sync-task-action`: Perform an action on an Automox task.
- `automox-vulnerability-sync-batch-get`: Get details about a Vulnerability Sync batch.
- `automox-vulnerability-sync-batches-list`: Get a list of Vulnerability Sync batches.
- `automox-vulnerability-sync-tasks-list`: Get a list of Automox tasks.
- `automox-vulnerability-sync-file-upload`: Upload a vulnerability report to Automox Vulnerability Sync.
- `automox-policies-list`: Retrieve a list of Automox policies belonging to an organization.
- `automox-command-run`: Run a command on a device in Automox
- `automox-device-delete`: Delete a device from Automox
- `automox-device-update`: Update a device's information in Automox
- `automox-groups-list`: List all groups in Automox based on organization permissions.
- `automox-group-create`: Create a group in Automox


## Axonius

**Type:** integration  
**Product:** Axonius  

This integration is for fetching information about assets in Axonius. This integration was integrated and tested with version 3.9 of Axonius

**Commands:**

- `axonius-get-devices-by-savedquery`: Gather device info by saved query
- `axonius-get-devices-by-aql`: Gather devices info by AQL query
- `axonius-get-users-by-aql`: Gather users info by AQL query
- `axonius-get-users-by-savedquery`: Gather user info by saved query
- `axonius-get-users-by-mail`: Gather user info by email address
- `axonius-get-users-by-mail-regex`: Gather user info by email address using regex
- `axonius-get-users-by-username`: Gather user info by username
- `axonius-get-users-by-username-regex`: Gather user info by username using regex
- `axonius-get-devices-by-hostname`: Gather device info by hostname
- `axonius-get-devices-by-hostname-regex`: Gather device info by hostname using regex
- `axonius-get-devices-by-ip`: Gather device info by IP address
- `axonius-get-devices-by-ip-regex`: Gather device info by IP address using regex
- `axonius-get-devices-by-mac`: Gather device info by MAC address
- `axonius-get-devices-by-mac-regex`: Gather device info by MAC address using regex
- `axonius-add-note`: Add note to assets


## Barracuda Reputation Block List (BRBL)

**Type:** integration  
**Product:** Barracuda  

This integration enables reputation checks against IPs from Barracuda Reputation Block List (BRBL) This integration was integrated and tested with Barracuda Reputation Block List (BRBL)

**Commands:**

- `ip`: Get IP Reputation


## Base64Decode

**Type:** script  
**Product:** Filters And Transformers  

Decodes an input in Base64 format

**Inputs:**

- `value`: The value to decode in Base64 format.


## Base64Encode

**Type:** script  
**Product:** Common Scripts  

Encodes an input using Base64 format

**Inputs:**

- `input`: The input to encode in Base64 format.


## Base64EncodeV2

**Type:** script  
**Product:** Common Scripts  

Encode an input to Base64 format

**Inputs:**

- `input`: The input to encode using Base64 format.


## Base64ListToFile

**Type:** script  
**Product:** Common Scripts  

Converts Base64 file in a list to a binary file and upload to warroom

**Inputs:**

- `listname`: List Name of Base64 item (need to be a single file in list)
- `filename`: Optional Warroom Output Filename (default filename is list name)
- `isZipFile`: Is data compressed (zip format)?


## BaseContentApiModule

**Type:** script  

Base classes for building robust Cortex integrations with user-friendly validation, common connection settings, and centralized execution configuration


## BaseScript

**Type:** script  
**Product:** Starter  

Script description

**Inputs:**

- `dummy`: [Enter a description of the argument, including any important information users need to know, for example, default values.]


## BatchData

**Type:** script  
**Product:** Community Common Scripts  

This Automation takes in a string of comma separated items and returns a dictionary of with the defined chunk size

**Inputs:**

- `batch_size`: number of items that will be returned in each dictionary items (must be of type int)
- `data`: comma separated list of items
- `context_path`: This nest the path under BatchedData in context. If you are running this script multiple times/simultaneously in a playbook, your data will 


## BechtleDarkWebScan

**Type:** integration  
**Product:** Bechtle Dark Web Scan  

The dark web scan integration notifies you if login credentials to your company are being sold on the dark web

**Commands:**

- `darkwebscan-getcompanies`: Returns a list of all companies associated with your API key.
- `darkwebscan-getleaks`: Returns leaked credentials for a given company_id.
- `darkwebscan-getosint`: Returns OSINT information about the associated domain of a given company_id.
- `darkwebscan-getemailsecurity`: Returns information about the email security for the associated domain of a given company_id.
- `darkwebscan-getwaf`: Returns Web Application Firewall Status information about the associated domain of a given company_id.
- `darkwebscan-resetcontext`: Resets integration context for the DarkWebScan. May result in many alerts reappearing.


## BeforeRelativeDate

**Type:** script  
**Product:** Filters And Transformers  

Checks the given datetime has occurred before the provided relative time

**Inputs:**

- `left`: Date value to check - Can be any time format. ex. "2020-01-01T00:00:00"
- `right`: Relative time ex. "6 months ago"


## BetweenDates

**Type:** script  
**Product:** Filters And Transformers  

Whether value is within a date range

**Inputs:**

- `value`: Value to check
- `begin_date`: Lower date range
- `end_date`: Upper date range


## BetweenHours

**Type:** script  
**Product:** Filters And Transformers  

Checks whether the given value is within the specified time (hour) range

**Inputs:**

- `value`: The value to check.
- `begin_time`: The start time range in the format HH:MM:SS.
- `end_time`: The end time range in the format HH:MM:SS.


## BeyondTrust - Authorization Requests

**Type:** integration  
**Product:** BeyondTrust - Authorization Requests  

Use this integration to handle Beyond Trust authorization requests through platform. This integration was integrated and tested with version 2 of BeyondTrust - Authorization Requests

**Commands:**

- `bt-authorize-ticket`: approve or deny authorization requests for BT.
- `bt-get-ticket`: retrieves an existing ticket.


## BeyondTrust Privilege Management Cloud

**Type:** integration  
**Product:** BeyondTrust  
**Commands:**

- `beyondtrust-pm-cloud-get-events`: Retrieves events or activity audits from BeyondTrust PM Cloud. Use the event_type argument to switch between Events and Activity Audits.


## BeyondTrust Retrieve Credentials

**Type:** playbook  
**Product:** BeyondTrust Password Safe  

Playbook for retrieving credentials for BeyondTrust Password Safe


## Binalyze AIR

**Type:** integration  
**Product:** Binalyze AIR  
**Commands:**

- `binalyze-air-isolate`: Isolate an endpoint
- `binalyze-air-acquire`: Acquire evidence from an endpoint


## Binalyze AIR Extended

**Type:** integration  
**Product:** Binalyze AIR Extended  

Manage Binalyze AIR forensic acquisition, endpoint isolation, triage, cases, tasks, assets, repositories, and evidence artifacts from the platform. This integration was integrated and tested with Binalyze AIR Extended

**Commands:**

- `binalyze-air-isolate`: Isolate an endpoint or release endpoint isolation.
- `binalyze-air-acquire`: Start forensic evidence acquisition from an endpoint.
- `binalyze-air-create-case`: Create a Binalyze AIR case.
- `binalyze-air-get-case`: Get a Binalyze AIR case by ID.
- `binalyze-air-list-cases`: List Binalyze AIR cases.
- `binalyze-air-close-case`: Close a Binalyze AIR case.
- `binalyze-air-get-case-tasks`: Get tasks associated with a Binalyze AIR case.
- `binalyze-air-get-case-endpoints`: Get endpoints associated with a Binalyze AIR case.
- `binalyze-air-get-case-activities`: Get activity history associated with a Binalyze AIR case.
- `binalyze-air-list-assets`: List Binalyze AIR endpoints/assets with optional filters.
- `binalyze-air-get-asset`: Get a Binalyze AIR endpoint/asset by asset ID.
- `binalyze-air-get-asset-by-hostname`: Find a Binalyze AIR endpoint/asset by hostname and organization ID.
- `binalyze-air-get-asset-tasks`: Get tasks associated with an endpoint/asset.
- `binalyze-air-get-task`: Get task details and normalized terminal status flags for polling.
- `binalyze-air-list-tasks`: List Binalyze AIR tasks.


## BinarySearchPy

**Type:** script  
**Product:** Common Scripts  

Searches for a binary on an endpoint using Carbon Black


## Bitbucket

**Type:** integration  
**Product:** Bitbucket  

Bitbucket Cloud is a Git-based code and CI/CD tool optimized for teams using Jira. This integration was integrated and tested with version 7.21.0 of Bitbucket

**Commands:**

- `bitbucket-project-list`: If a project_key is given, returns the requested project. Else, returns a list of the projects in the workspace.
- `bitbucket-open-branch-list`: Returns a list of the open branches.
- `bitbucket-branch-get`: Returns the information of the requested branch.
- `bitbucket-branch-create`: Creates a new branch in Bitbucket.
- `bitbucket-branch-delete`: Deletes the given branch from Bitbucket.
- `bitbucket-commit-create`: Creates a new commit in Bitbucket.
- `bitbucket-commit-list`: Returns a list of the commit in accordance with the included and excluded branches.
- `bitbucket-file-delete`: Deletes the given file from Bitbucket.
- `bitbucket-raw-file-get`: Returns the content of the given file, along with the option to download it.
- `bitbucket-issue-create`: Deprecated. Issues are fully removed from Bitbucket Cloud by Atlassian as of Mid-August 2026. Use the jira-create-issue command in the Atlassian Jira v3 integra
- `bitbucket-issue-list`: Deprecated. Issues are fully removed from Bitbucket Cloud by Atlassian as of Mid-August 2026. Use the jira-get-issue command (for a single issue) or the jira-is
- `bitbucket-issue-update`: Deprecated. Issues are fully removed from Bitbucket Cloud by Atlassian as of Mid-August 2026. Use the jira-edit-issue command in the Atlassian Jira v3 integrati
- `bitbucket-pull-request-create`: Creates a pull request in Bitbucket.
- `bitbucket-pull-request-update`: Updates a pull request in Bitbucket.
- `bitbucket-pull-request-list`: Returns a list of the pull requests. If a state is provided than the list will contain only PRs with the wanted status. If a state is not provided, by default a


## Bitsight for Security Performance Management

**Type:** integration  
**Product:** Bitsight  

Use the "Bitsight for Security Performance Management" Integration to get company guid, details, and findings. This integration also allows to fetch the findings by using the fetch incidents capability. This integration was integrated and tested with version 01 of Bitsight for Security Performance Management

**Commands:**

- `bitsight-company-details-get`: Bitsight command to get company details based on the provided GUID. The details include rating details, rating history, and grades for individual risk vectors.
- `bitsight-company-findings-get`: Bitsight command to get company findings.
- `bitsight-companies-guid-get`: Bitsight command to get list of companies and GUID.


## Bitwarden Password Manager

**Type:** integration  
**Product:** Bitwarden Password Manager  

This integration collects event logs from Bitwarden Password Manager to Cortex XSIAM. This integration was integrated and tested with version 2024.6.2 of Bitwarden Password Manager

**Commands:**

- `bitwarden-get-events`: Gets events from Bitwarden.


## Block Indicator - Infoblox NIOS

**Type:** playbook  
**Product:** Infoblox NIOS  

This playbook blocks the given Indicator by creating or updating RP Zone rule in Infoblox NIOS platform

**Inputs:**

- `indicator`: The indicator to block.
- `target_rp_zone`: The target Response Policy Zone.


## block-domain

**Type:** script  
**Product:** Aggregated Scripts  

The script blocks a list of domain FQDNs in supported integrations. Currently only supports Palo Alto Networks Panorama

**Inputs:**

- `domain_list`: A comma-separated list of domain FQDNs to block. Wildcard entries (e.g. *.evil.com) are not supported and are skipped.
- `rule_name`: The name of the rule which will be created in the relevant products. Default: Cortex - Block Domain.
- `log_forwarding_name`: The Panorama log forwarding object name that specifies the Log Forwarding setting to apply to the PAN-OS custom rules.
- `address_group`: The name of the PAN-OS Panorama or Firewall address group used to hold the blocked domain FQDN objects. Default: Blocked Domains - Cortex.
- `auto_commit`: Whether to commit the new rule and push to the device group at the end of the run. Default: true.
- `tag`: The designated tag name for the domain FQDN object. Applied to every object the script creates. Default: cortex-blocked-domains.
- `brands`: A comma-separated list of integration brands to run the command for. If not provided, the command runs for all available integrations.
- `verbose`: Whether to retrieve a human-readable entry for every command or only the final result. True retrieves a human-readable entry for every comma


## block-external-ip

**Type:** script  
**Product:** Aggregated Scripts  

The script blocks a list of IP addresses in supported integrations

**Inputs:**

- `ip_list`: List of IPs to block.
- `rule_name`: The name of the rule which will be created in the relevant products.
- `log_forwarding_name`: Panorama log forwarding object name. Indicate what type of Log Forwarding setting will be specified in the PAN-OS custom rules.
- `address_group`: This input determines whether PANW Panorama or Firewall or Prisma SASE Address Groups are used. Specify the Address Group name for IPs list 
- `auto_commit`: Whether to commit the new rule.
- `tag`: The designated tag name for the IP.
- `brands`: Which integrations brands to run the command for. If not provided, the command will run for all available integrations.For multi-select prov
- `verbose`: Whether to retrieve a human-readable entry for every command or only the final result. True retrieves a human-readable entry for every comma


## block-url

**Type:** script  
**Product:** Aggregated Scripts  

Blocks a list of URLs in supported integrations

**Inputs:**

- `url_list`: A comma-separated list of URLs to block. The scheme is stripped before the URL is submitted to the firewall.
- `brands`: Which integration brands to run the command for. If not provided, the command will run for all available integrations.For multi-select provi
- `rule_name`: The name of the security rule which will be created in the relevant products.
- `url_category`: The name of the PAN-OS custom URL category which holds the blocked URLs.
- `url_filtering_profile`: The name of the PAN-OS URL Filtering security profile which blocks the custom URL category.
- `log_forwarding_name`: The Panorama log forwarding object name. Indicates what type of Log Forwarding setting will be specified in the PAN-OS custom rules.
- `tag`: The designated tag name for the objects the script creates.
- `auto_commit`: Whether to commit the new rule.


## BMC Helix ITSM

**Type:** integration  
**Product:** BMC Helix ITSM  

BMC Helix ITSM integration enables customers to manage service request, incident, change request, task, problem investigation, known error and work order tickets. This integration was integrated and tested with version 22.1.05 of BmcITSM

**Commands:**

- `bmc-itsm-user-list`: Retrieves a list of user profiles from BMC Helix ITSM. The records are retrieved by the query argument or by the filtering arguments. When using filtering argum
- `bmc-itsm-company-list`: Retrieves a list of companies from BMC Helix ITSM. The records are retrieved by the query argument or by the filtering arguments. When using filtering arguments
- `bmc-itsm-service-request-definition-list`: Retrieves a list of service request definitions. The records are retrieved by the query argument or by the filtering arguments. When using filtering arguments, 
- `bmc-itsm-ticket-list`: Retrieves a list of BMC Helix ITSM tickets. The records are retrieved by the query argument or by the filtering arguments. When using filtering arguments, each 
- `bmc-itsm-service-request-create`: Creates a new service request ticket. A service request ticket is the request record that is generated from the service request definition to manage and track t
- `bmc-itsm-service-request-update`: Updates the details of a service request ticket for a given request ID. User and company related arguments can be retrieved by executing the bmc-itsm-user-list 
- `bmc-itsm-incident-update`: Update incident ticket.
- `bmc-itsm-ticket-delete`: Deletes a ticket by its request ID. Only admin users can perform this command.
- `bmc-itsm-incident-create`: Creates a new incident ticket. An incident is any event that is not part of the standard operation of a service and that causes an interruption to or a reductio
- `bmc-itsm-change-request-create`: Creates a change request ticket in BMC Helix ITSM. The ticket is created by using a template or from scratch.
- `bmc-itsm-change-request-update`: Updates the details of change request ticket for the specified request ID.
- `bmc-itsm-task-create`: Creates a new task ticket. By splitting cases into individual tasks (assignments), you can focus on one assignment at a time to resolve cases more efficiently. 
- `bmc-itsm-task-update`: Updates the task ticket.
- `bmc-itsm-problem-investigation-create`: Creates a problem investigation ticket.
- `bmc-itsm-problem-investigation-update`: Updates The problem investigation ticket type.


## BMC Helix Remedyforce

**Type:** integration  
**Product:** Bmc Helix Remedyforce  

BMC Helix Remedyforce integration allows customers to create/update service requests and incidents. It also allows to update status, resolve service requests and incidents with customer notes. This integration exposes standard ticketing capabilities that can be utilized as part of automation & orchestration. This integration was integrated and tested with version 202002.79 of BMC Helix Remedyforce

**Commands:**

- `bmc-remedy-service-request-definition-get`: This command gets details of service request definitions with the help of service request definition name.
- `bmc-remedy-note-create`: This command creates notes for incidents and service requests.
- `bmc-remedy-service-request-update`: This command updates the details of a service request for a given service request number.
- `bmc-remedy-service-request-create`: This command allows the user to create a new service request. A service request is the request record that is generated from the service request definition to m
- `bmc-remedy-template-details-get`: This command helps to get template details for Incidents. Templates enable users to prepopulate commonly used fields in a form.
- `bmc-remedy-impact-details-get`: This command helps to get impact details for incidents and service requests. Impact helps to calculate priority of the incident or service request.
- `bmc-remedy-service-offering-details-get`: This command helps to get service offering details for incidents. Users can link a service offering of the associated service.
- `bmc-remedy-incident-create`: This command allows the user to create a new incident.
- `bmc-remedy-incident-update`: This command updates the details of an incident for a given incident number.
- `bmc-remedy-asset-details-get`: This command helps to get asset or configuration item details for incidents.
- `bmc-remedy-account-details-get`: This command helps to get account details for incidents and service requests.
- `bmc-remedy-status-details-get`: This command helps to get status details for incidents and service requests. Status is used to display the progress of the service request or incident through i
- `bmc-remedy-urgency-details-get`: This command helps to get urgency details for incidents and service requests. Urgency is used to determine the priority of the incident or service request.
- `bmc-remedy-category-details-get`: This command helps to get category details for incidents and service requests. Categories allow users to classify the incident or service request using standard
- `bmc-remedy-queue-details-get`: This command helps to get queue details for incidents and service requests. It accepts queue name and type as arguments.


## BMCHelixRemedyforceCreateIncident

**Type:** script  
**Product:** Bmc Helix Remedyforce  

This script is used to simplify the process of creating the incident in BMC Helix Remedyforce. The script will consider the ID over the name of the argument when both are provided. Example: client_id is considered when both client_id and client_user_name are provided

**Inputs:**

- `client_user_name`: User name of the client. Get the username using the 'bmc-remedy-user-details-get' command.
- `client_id`: The unique ID of the client. It helps to select a client for a particular service request. Get the client ID from the email using the 'bmc-r
- `category`: Classifies the service request using standard classifications to track the reporting purposes. Get the category name using the 'bmc-remedy-c
- `category_id`: The unique ID of the category. Categories allow users to classify the incident or service request using standard classifications to track th
- `queue`: Name of the queue owner. Ghe queue name using the 'bmc-remedy-queue-details-get' command.
- `queue_id`: The unique ID of the owner. Get the queue ID using the 'bmc-remedy-queue-details-get' command.
- `staff_user_name`: The user name of the staff. Get the username using the 'bmc-remedy-user-details-get' command.
- `staff_id`: The unique ID of the staff to whom the user wants to assign the record. Get the staff ID from the staff details using the 'bmc-remedy-user-d


## BMCHelixRemedyforceCreateServiceRequest

**Type:** script  
**Product:** Bmc Helix Remedyforce  

This script is used to simplify the process of creating a service request in BMC Helix Remedyforce. The script will consider ID over the name of the argument when both are provided. Example: client_id is considered when both client_id and client_user_name are provided

**Inputs:**

- `client_user_name`: User name of the client. Get the username using the 'bmc-remedy-user-details-get' command.
- `client_id`: The unique ID of the client. It helps to select a client for a particular service request. Get the client ID from the email using the 'bmc-r
- `category`: Classifies the service request using standard classifications to track the reporting purposes. Get the category name using the 'bmc-remedy-c
- `category_id`: The unique ID of the category. Categories allow users to classify the incident or service request using standard classifications to track th
- `queue`: Name of the queue owner. Get the queue name using the 'bmc-remedy-queue-details-get' command.
- `queue_id`: The unique ID of the queue owner. Get the queue ID using the 'bmc-remedy-queue-details-get' command.
- `staff_user_name`: The user name of the staff. Get the username using the 'bmc-remedy-user-details-get' command.
- `staff_id`: The unique ID of the staff to whom the user wants to assign the record. Get the staff ID from the staff details using the 'bmc-remedy-user-d


## Bonusly

**Type:** integration  
**Product:** Bonusly  
**Commands:**

- `bonusly-list-bonuses`: Get a list of bonuses based on a filter
- `bonusly-create-bonus`: Creates a bonusly bonus
- `bonusly-get-bonus`: Get a bonusly based on an ID
- `bonusly-update-bonus`: Update a bonus to bonusly
- `bonusly-delete-bonus`: Delete a bonus based on an ID like 24abcdef1234567890abcdef


## Bonusly - AutoGratitude

**Type:** playbook  
**Product:** Bonusly  

AutoGratitude is a playbook to give back a positive gratitude to security engineers and developers when they successfully complete an SLA

**Inputs:**

- `BonuslyLookupList`: Create a Lookup JSON List In The Lists Section Containing platform Email To Bonusly User


## Box v2

**Type:** integration  
**Product:** Box  

Manage Box users This integration was integrated and tested with API version 2.0 of Box v2

**Commands:**

- `box-search-content`: Searches for files, folders, web links, and shared files across the users content or across the entire enterprise.
- `box-find-file-folder-by-share-link`: Return the file represented by a shared link.
- `box-get-shared-link-by-file`: Gets the information for a shared link on a file.
- `box-create-file-share-link`: Adds a shared link to a file.
- `box-update-file-share-link`: Updates a shared link on a file.
- `box-remove-file-share-link`: Removes a shared link from a file.
- `box-get-shared-link-by-folder`: Gets the information for a shared link on a folder.
- `box-create-folder-share-link`: Adds a shared link to a folder.
- `box-update-folder-share-link`: Updates a shared link on a folder.
- `box-remove-folder-share-link`: Removes a shared link from a folder.
- `box-get-folder`: Retrieves details for a folder, including the first 100 entries in the folder.
- `box-list-folder-items`: Retrieves a page of items in a folder.
- `box-folder-create`: Creates a new empty folder within the specified parent folder.
- `box-file-delete`: Deletes a file, either permanently or by moving it to the trash.
- `box-list-users`: Returns a list of all users for the Enterprise along with their user_id, public_name, and login.


## BreachConfirmationHTML

**Type:** script  
**Product:** Common Scripts  

This Compliance content pack contains essential incidents fields that are used in the compliance-related packs. The script in this pack is used for a dynamic field in the HIPAA Breach Notification Incident layout and the US Breach Notification layout to indicate if a breach was confirmed. For more information, visit our the platform


## BreachRx

**Type:** integration  
**Product:** BreachRx  

Automate your privacy Incident Response workflow through the BreachRx platform. This integration was integrated and tested with version 1.20 of BreachRx

**Commands:**

- `breachrx-incident-create`: Create a privacy Incident on the BreachRx platform.
- `breachrx-incident-actions-get`: Fetch all actions for a BreachRx privacy Incident.
- `breachrx-incident-import`: Link a BreachRx privacy Incident with an platform Incident.
- `breachrx-incident-get`: Find a BreachRx privacy Incident on the connected BreachRx platform.


## BreachRx - Create Incident and get Active Tasks

**Type:** playbook  
**Product:** BreachRx  

This Playbook creates a privacy Incident on the BreachRx platform, and pulls in all tasks from that created privacy Incident into the the platform


## Bring Asset Data Back - Infoblox NIOS

**Type:** playbook  
**Product:** Infoblox NIOS  

This playbook brings asset data back that creates a host record using Infoblox NIOS integration

**Inputs:**

- `name`: The name of the host record.
- `ipv4_addresses`: The IPv4 addresses to create host record with. Example: [{"ipv4addr": "192.168.1.0"}], [{"ipv4addr": "192.168.1.1", "configure_for_dhcp": tr
- `ipv6_addresses`: The IPv6 addresses to create host record with. Example: [{"ipv6addr": "2001:db8::1"}], [{"ipv6addr": "2001:db8::2", "configure_for_dhcp": tr
- `view`: The DNS view in which the records are located.
- `comment`: The comment for this host record.
- `configure_for_dns`: Boolean value to decide whether to configure the host record for DNS. Default is True.


## Cado Response

**Type:** integration  
**Product:** Cado Response  

Automate data collection. Process data at cloud speed. Analyze with purpose. This integration was integrated and tested with version 1.2.0 of CadoResponse

**Commands:**

- `cado-create-project`: Create a project in Cado Response
- `cado-list-project`: Get a list of projects from Cado Response
- `cado-get-pipeline`: Get pipeline details from Cado Response
- `cado-list-ec2`: Get a list of EC2 instances in a region
- `cado-list-s3`: Get a list of S3 buckets
- `cado-trigger-ec2`: Trigger a disk acquisition and processing pipeline in Cado Response for a given EC2 instance
- `cado-trigger-s3`: Trigger a disk acquisition and processing pipeline in Cado Response for a given file in an S3 bucket


## Calculate Severity - GreyNoise

**Type:** playbook  
**Product:** GreyNoise  

Calculate and assign the incident severity based on the highest returned severity level from the following calculations

**Inputs:**

- `DBotScore`: Array of all indicators associated with the incident.
- `NetworkTrafficDirection`: The direction of network traffic event associated with the Incident(Egress/Ingress). If not supplied, Ingress is considered.


## Calculate Severity Highest DBotScore For Egress Network Traffic - GreyNoise

**Type:** playbook  
**Product:** GreyNoise  

Playbook to calculate the severity based on GreyNoise

**Inputs:**

- `DBotScore`: Array of all indicators associated with the incident.


## Calculate Severity Highest DBotScore For Ingress Network Traffic - GreyNoise

**Type:** playbook  
**Product:** GreyNoise  

Playbook to calculate the severity based on GreyNoise

**Inputs:**

- `DBotScore`: Array of all indicators associated with the incident.


## Caldera Operation

**Type:** playbook  
**Product:** MITRE Caldera  

This playbook is used to create a new Operation in Mitre Caldera


## Camlytics

**Type:** integration  
**Product:** Camlytics  

You can use this integration to automate different Camlytics surveillance analysis actions. This integration was integrated and tested with version 2.2.5 of Camlytics

**Commands:**

- `camlytics-get-channels`: Retrieve video channels
- `camlytics-get-events-totals-by-rule`: Retrieve video analytics events totals grouped by calibration rules, these rules can be defined using zones and lines to set areas where different camera events
- `camlytics-get-events-totals-by-type`: Retrieve video analytics events totals grouped by analytics event type. For example: ObjectAppear, Tailgating, Sabotage and TripwireCrossed.
- `camlytics-get-events`: Retrieve video analytics events ordered by event id.


## Cape Sandbox

**Type:** integration  
**Product:** Cape Sandbox  
**Commands:**

- `cape-file-submit`: Submits a file for analysis to CAPE Sandbox. This command supports PCAP files and automatically sets the pcap option to 1. The command polls the CAPE server unt
- `cape-file-view`: View detailed information about a file that has been analyzed by CAPE Sandbox. You must specify at least one identifier: Task ID, MD5 hash, or SHA256 hash.
- `cape-sample-download`: Download a sample file from a CAPE Sandbox task. You must specify at least one identifier: Task ID, MD5 hash, SHA1 hash, or SHA256 hash. The downloaded file wil
- `cape-url-submit`: Submit a URL for analysis to CAPE Sandbox. The command polls the CAPE server until the analysis task is reported as complete, and then returns the task view wit
- `cape-task-delete`: Delete a CAPE Sandbox analysis task by its Task ID.
- `cape-tasks-list`: Returns a list of CAPE Sandbox tasks. If a task_id is provided, the command returns the detailed information for that specific task.
- `cape-task-report-get`: Retrieve the analysis report associated with a specified CAPE Sandbox task ID. If zip=true, the report will be returned as a downloadable ZIP file.
- `cape-pcap-file-download`: Download the PCAP (Packet Capture) network dump file associated with a specific CAPE Sandbox task ID. The PCAP file contains all network traffic captured during
- `cape-task-screenshot-download`: Download screenshots captured during the analysis of a CAPE Sandbox task. Screenshots show the visual behavior of the analyzed file or URL. If a specific screen
- `cape-machines-list`: Returns a list of available analysis machines configured in CAPE Sandbox. If a machine_name is provided, the command returns detailed information for that speci
- `cape-cuckoo-status-get`: Returns the overall status of the CAPE/Cuckoo system in a human-readable format. This command provides a quick overview of the sandbox's operational status.


## CaseMgmtAnalystTools

**Type:** script  
**Product:** CaseManagement-Generic  

Dynamic display script to display a list of useful Analyst Tools on an Incident layout. Create an platform list called "Case Management Analyst Tools", and add a markdown table to provide your own list


## CaseMgmtDisplayLabels

**Type:** script  
**Product:** CaseManagement-Generic  

Dynamic section that will display the Labels for an Incident in a markdown table


## CaseMgmtIncidentTypesDisplay

**Type:** script  
**Product:** CaseManagement-Generic  

Restricts the Incident Types a user can create manually based on an platform list, and prevents changing the Incident Type manually once it is created. Requirements - Create an platform List called IncidentTypesFromList a list of comma separated Incident Types Incident Type 1,Incident Type 2, Incident Type 3


## CaseMgmtResponseProcess

**Type:** script  
**Product:** CaseManagement-Generic  

Dynamic display script to display a response process on an Incident layout. The response process display can change depending on the Incident Type


## Celonis

**Type:** integration  
**Product:** Celonis  

Celonis Event Collector is an integration that supports fetching audit log events. This integration was integrated and tested with version 4.0 of Celonis

**Commands:**

- `celonis-get-events`: Retrieves a list of audit logs events from the Celonis instance.


## Censys Platform

**Type:** integration  
**Product:** Censys  

Built on the industry’s most comprehensive Internet Map, the Censys Platform delivers unmatched visibility into global internet assets, adversary infrastructure, and evolving threats. This integration was integrated and tested with version 2.0 of Censys

**Commands:**

- `cen-view`: Returns detailed information for an IP address or SHA256 within the specified index.
- `cen-search`: Return previews of hosts matching a specified search query or a list of certificates that match the given query.
- `domain`: Return all related IPs as relationships.
- `ip`: Runs reputation on IPs.
- `cen-host-history-list`: Retrieve the event history for a host (IP address).
- `cen-rescan`: Initiate a live rescan for a known host service at a specific IP and port (ip:port) or hostname and port (hostname:port).
- `cen-related-infrastructure-list`: Initiate a CensEye (Related Infrastructure) pivot analysis job for a Host, Web Property, or SHA256 Certificate.


## Centrify Vault

**Type:** integration  
**Product:** Centrify Vault  

Leverage the Centrify Vault integration to create and manage Secrets

**Commands:**

- `centrify-retrieve-secrets`: Retrieves the secret from centrify vault based on folder name, set name or secret name. If folder name is not provided, all the secrets in the parent folder wil
- `centrify-retrieve-secret-by-secretid`: Retrieves the secret from centrify vault based on secret ID.
- `centrify-create-secretfolder`: Creates a folder in Centrify Vault
- `centrify-create-secret`: Creates a secret in Centrify Vault.
- `centrify-create-set`: Creates a set in Centrify Vault
- `centrify-retrieve-folders`: Fetch details of all folders in Centrify Vault
- `centrify-delete-folder`: Delete a folder from the Centrify Vault
- `centrify-delete-secret`: Delete Secret from the Centrify Vault. Please note: Enabling "recursiveDelete" to "Yes" will delete all secrets if there multiple secrets with same name in subf
- `centrify-delete-secret-by-secretid`: Delete Secret from the Centrify Vault based on the Secret ID provided
- `centrify-add-secret-to-set`: Adds/Moves a secret to a set for the provided secretID. Use "centrify-retrieve-secrets" to fetch secret ID's.
- `centrify-retrieve-sets`: Fetches the details of all sets in the Centrify Vault
- `centrify-delete-set`: Delete set from the Centrify Vault


## Change Management

**Type:** playbook  
**Product:** Change Management  

If you are using PAN-OS/Panorama firewall and Jira or ServiceNow as a ticketing system, this playbook will be a perfect match for your change management for firewall process. This playbook can be triggered by 2 different options - a fetch from ServiceNow or Jira - and will help you manage and automate your change management process

**Inputs:**

- `TicketSummary`: Provide a summary for your firewall change request.
- `SecurityTeamEmail`: The email of the security team that approves the firewall requests.
- `log_type`: Log type to query. Can be: traffic, threat, wildfire, url or data-filtering.
- `query`: The query string by which to match criteria for the logs. This is similar to the query provided in the web interface under the Monitor tab w
- `Query_logs`: By providing the value "Yes" to this input, the "Panorama Query Logs" playbook will be activated.
- `addr-src`: The source address for the change request.
- `addr-dst`: The destination address for the change request.
- `port-dst`: The destination ports for the change request.


## Check Point - Vulnerability Exploitation Monitoring

**Type:** playbook  
**Product:** Cyberint  

Enriches CVEs from a vulnerability-management incident with Cyberint vulnerability intelligence and prioritizes them based on real-world exploitation. For each CVE the playbook retrieves the Cyberint CVE score, CVSS, EPSS, CWE and active-exploitation evidence. When a CVE exceeds the configured risk thresholds or is being actively exploited, the incident is escalated and a patch-remediation ticket is opened; otherwise the CVE is tagged as monitored. Connect the remediation task to your ticketing system and CMDB to fully automate risk-based vulnerability management

**Inputs:**

- `CVE`: CVE identifiers to monitor. Defaults to CVE indicators extracted from the incident.
- `CyberintScoreThreshold`: The Cyberint CVE score (0-10) at or above which the incident is escalated. Default is 7.
- `CVSSThreshold`: The CVSS base score (0-10) at or above which the incident is escalated. Default is 7.
- `EPSSThreshold`: The EPSS probability score (0-1) at or above which the incident is escalated. Default is 0.5.


## Check Point EM Alerts

**Type:** integration  
**Product:** Cyberint  

Cyberint provides intelligence-driven digital risk protection. This integration will help your enterprise effectively consume actionable cyber alerts to increase your security posture

**Commands:**

- `cyberint-alerts-fetch`: List alerts according to parameters
- `cyberint-alerts-status-update`: Update the status of one or more alerts.
- `cyberint-alerts-get-attachment`: Get alert attachment.
- `cyberint-alerts-analysis-report`: Get alert analysis report.


## Check Point EM Takedowns

**Type:** integration  
**Product:** Cyberint  

Use the Cyberint Takedowns integration to manage takedowns requests

**Commands:**

- `cyberint-retrieve-takedowns`: Retrieve takedowns requests.
- `cyberint-takedown-url`: Submit takedown request.


## Check Point Harmony Endpoint

**Type:** integration  
**Product:** Check Point Harmony Endpoint  

Checkpoint Harmony Endpoint provides a complete endpoint security solution built to protect organizations and the remote workforce from today's complex threat landscape. This integration was integrated and tested with version 1 of CheckPointHarmonyEndpoint

**Commands:**

- `harmony-ep-job-status-get`: Retrieves the status and result (if any) of a given asynchronous operation. A job is a way to monitor the progress of an asynchronous operation while avoiding i
- `harmony-ep-ioc-list`: Gets a list of all Indicators of Compromise. Use the filter parameters to fetch specific IOCs.
- `harmony-ep-ioc-update`: Updates the given Indicators of Compromise with the given parameters.
- `harmony-ep-ioc-create`: Creates new Indicators of Compromise using the given parameters.
- `harmony-ep-ioc-delete`: Deletes the given Indicators of Compromise by their ID.
- `harmony-ep-policy-rule-assignments-get`: Gets all entities directly assigned to the given rule.
- `harmony-ep-policy-rule-assignments-add`: Assigns the specified entities to the given rule. Specified IDs that are already assigned to the rule are ignored.
- `harmony-ep-policy-rule-assignments-remove`: Removes the specified entities from the given rule's assignments. Specified IDs that are not assigned to the rule are ignored.
- `harmony-ep-policy-rule-install`: Installs all policies.
- `harmony-ep-policy-rule-modifications-get`: Gets information on modifications to a given rule. (Modifications are the additions or removal of assignments on a rule since it was last installed).
- `harmony-ep-policy-rule-metadata-list`: Gets the metadata of all rules or the given rule's metadata. (Metadata refers to all information relating to the rule except it's actual settings).
- `harmony-ep-push-operation-status-list`: Gets the current statuses of all remediation operations or if a specific ID is specified, retrieve the current status of the given remediation operation.
- `harmony-ep-push-operation-get`: Gets the results of a given Remediation Operation. Remediation Operations may produce results such a Forensics Report or yield status updates such as an anti-ma
- `harmony-ep-push-operation-abort`: Aborts the given remediation operation. Aborting an operation prevents it from being sent to further Harmony Endpoint Clients. Clients that have already receive
- `harmony-ep-anti-malware-scan`: Performs an anti-malware scan on computers matching the given query. Note that you must specify at least one of the following filter arguments: computer_ids, co


## Check Point Network Detection and Response (Infinity NDR)

**Type:** integration  
**Product:** Check Point Infinity NDR  

Collect network security events from Check Point Infinity NDR for your secured SaaS periodically This integration was integrated and tested with version 1.1.0 of CheckPointNDR

**Commands:**

- `check-point-ndr-fetch-insights`: Retrieve all NDR Insights


## Check Point XDR

**Type:** integration  
**Product:** Check Point XDR  

The Check Point XDR (Extended Detection and Response) integration allows you to connect to Check Point's CloudInfra platform to fetch and manage incidents. This integration enables you to retrieve incidents from Check Point XDR, convert them into the platform, and manage them effectively within your security operations workflows

**Commands:**

- `fetch-incidents`: Fetches incidents from Check Point XDR and converts them into the platform.
- `get-mapping-fields`: Returns the fields available for mapping incoming incidents to the platform.
- `update-remote-system`: Sends updates from the platform, such as status changes or ownership updates.


## Cherwell

**Type:** integration  
**Product:** Cherwell  

Cloud-based IT service management solution This integration was integrated and tested with version 10.1.1 of Cherwell

**Commands:**

- `cherwell-create-business-object`: Creates a business object.
- `cherwell-update-business-object`: Update a business object with the specified fields.
- `cherwell-delete-business-object`: Deletes a given business object.
- `cherwell-get-business-object`: Gets a business object by an ID.
- `cherwell-download-attachments`: Downloads imported attachements from a specified business object.
- `cherwell-upload-attachment`: Uploads an attachment to a specified business object.
- `cherwell-link-business-objects`: Links business objects that are related.
- `cherwell-unlink-business-objects`: Unlinks business objects that are linked and related.
- `cherwell-get-attachments-info`: Gets information for business object attachments.
- `cherwell-remove-attachment`: Remove the attachment from the specified business object.
- `cherwell-query-business-object`: Runs advanced queries to search in a specified business object.
- `cherwell-get-field-info`: Gets information for a field, by one of its properties (Name, Display Name, or id).
- `cherwell-run-saved-search`: Returns the results of a saved search.


## CherwellCreateIncident

**Type:** script  
**Product:** Cherwell  

This script is an example script of how to create an incident in Cherwell. The script wraps the create business object command in the cherwell integration. When writing your own script to create a business object, follow the instructions in the configuration part, but do not change the execution section

**Inputs:**

- `description`: Incident description.
- `priority`: Incident priority.
- `owned_by`: Incident owner.
- `service`: Service needed.
- `customer_display_name`: Requesting customer name.


## CherwellGetIncident

**Type:** script  
**Product:** Cherwell  

This script is an example script of how to retrieve an incident from Cherwell. The script wraps the cherwell-get-business-object command of the cherwell integration. When writing your own script to get a business object, follow the instructions found in the configuration section of the script, but do not change the execution section

**Inputs:**

- `id_type`: Type of ID.
- `id_value`: Public ID or record ID.


## CherwellIncidentOwnTask

**Type:** script  
**Product:** Cherwell  

This script is an example script of how to link an incident to a task in Cherwell. The script wraps the cherwell-link-business-object command of the cherwell integration. When writing your own script to link business objects, follow the instructions found in the configuration section of the script, but do not change the execution section

**Inputs:**

- `incident_record_id`: Incident record ID.
- `task_record_id`: Task record ID.


## CherwellIncidentUnlinkTask

**Type:** script  
**Product:** Cherwell  

This script is an example script of how to unlink a task from an incident in Cherwell. The script wraps the cherwell-unlink-business-object command of the cherwell integration. When writing your own script to unlink business objects, follow the instructions found in the configuration section of the script, but do not change the execution section

**Inputs:**

- `incident_record_id`: Incident record ID.
- `task_record_id`: Task record ID.


## CherwellQueryIncidents

**Type:** script  
**Product:** Cherwell  

This script is an example script of how to query incidents from Cherwell. The script wraps the cherwell-query-business-object command of the cherwell integration. When writing your own script to query business objects, follow the instructions found in the configuration section of the script, but do not change the execution section

**Inputs:**

- `query`: The query to run. The query is a list of comma-seperated filters such that each filter should be of the form: ["field_name","operator","valu


## CherwellUpdateIncident

**Type:** script  
**Product:** Cherwell  

This script is an example script of how to update an incident in Cherwell. The script wraps the update-business-object command of the cherwell integration. When writing your own script to update a business object, follow the instructions found in the configuration section of the script, but do not change the execution section

**Inputs:**

- `description`: Incident description.
- `priority`: Incident priority.
- `owned_by`: Incident owner.
- `service`: Service needed.
- `id_value`: Public ID or record ID.
- `id_type`: Type of ID.


## Chronicle

**Type:** integration  
**Product:** Google SecOps  
**Commands:**

- `gcb-list-iocs`: Lists the IOC Domain matches within your enterprise for the specified time interval. The indicator of compromise (IOC) domain matches lists for which the domain
- `gcb-assets`: Returns a list of the assets that accessed the input artifact (IP, domain, MD5, SHA1 and SHA256) during the specified time.
- `ip`: Checks the reputation of an IP address.
- `domain`: Checks the reputation of a domain.
- `gcb-ioc-details`: Accepts an artifact indicator and returns any threat intelligence associated with the artifact. The threat intelligence information is drawn from your enterpris
- `gcb-list-alerts`: List all the alerts tracked within your enterprise for the specified time range. Both the parsed alerts and their corresponding raw alert logs are returned.
- `gcb-list-events`: List all of the events discovered within your enterprise on a particular device within the specified time range. If you receive the maximum number of events you
- `gcb-list-detections`: Return the detections for the specified version of a rule, the latest version of a rule, all versions of a rule, or all versions of all rules.
- `gcb-list-rules`: List the latest versions of all Rules.
- `gcb-create-rule`: Creates a new rule. By default the live rule status will be set to disabled.
- `gcb-get-rule`: Retrieves the rule details of specified Rule ID or Version ID.
- `gcb-delete-rule`: Deletes the rule specified by Rule ID.
- `gcb-create-rule-version`: Creates a new version of an existing rule.
- `gcb-change-rule-alerting-status`: Updates the alerting status for a rule specified by Rule ID.
- `gcb-change-live-rule-status`: Updates the live rule status for a rule specified by Rule ID.


## ChronicleAssetEventsForHostnameWidgetScript

**Type:** script  
**Product:** Google SecOps  

Displays the list of events fetched for an asset identified as a "ChronicleAsset" type of indicator, when its hostname is passed as an asset identifier


## ChronicleAssetEventsForIPWidgetScript

**Type:** script  
**Product:** Google SecOps  

Displays the list of events fetched for an asset identified as a "ChronicleAsset" type of indicator, when its IP address is passed as an asset identifier


## ChronicleAssetEventsForMACWidgetScript

**Type:** script  
**Product:** Google SecOps  

Displays the list of events fetched for an asset identified as a "ChronicleAsset" type of indicator, when its MAC address is passed as an asset identifier


## ChronicleAssetEventsForProductIDWidgetScript

**Type:** script  
**Product:** Google SecOps  

Displays the list of events fetched for an asset identified as a "ChronicleAsset" type of indicator, when its product ID is passed as an asset identifier


## ChronicleAssetIdentifierScript

**Type:** script  
**Product:** Google SecOps  

Collect all asset identifiers - Hostname, IP address and MAC address in the context

**Inputs:**

- `artifact_identifiers`: Hostname, IP address or MAC address that can identify the asset.


## ChronicleDBotScoreWidgetScript

**Type:** script  
**Product:** Google SecOps  

Shows the DBot Score and reputation of the Domain


## ChronicleDomainIntelligenceSourcesWidgetScript

**Type:** script  
**Product:** Google SecOps  

Shows the details of sources in the Chronicle Domain Intelligence Sources section of the incident


## ChronicleIsolatedHostnameWidgetScript

**Type:** script  
**Product:** Google SecOps  

Notifies if the hostname associated with the ChronicleAsset is isolated or not


## ChronicleIsolatedIPWidgetScript

**Type:** script  
**Product:** Google SecOps  

Notifies if the IP address associated with the ChronicleAsset is isolated or not


## ChronicleListDeviceEventsByEventTypeWidgetScript

**Type:** script  
**Product:** Google SecOps  

Displays a pie chart of the number of events, categorized by its event type, fetched for all the identifiers of the ChronicleAsset


## ChroniclePotentiallyBlockedIPWidgetScript

**Type:** script  
**Product:** Google SecOps  

Notifies if the IP address associated with the ChronicleAsset is potentially blocked or not


## CIDRBiggerThanPrefix

**Type:** script  
**Product:** Filters And Transformers  

Checks if given CIDR prefix is bigger than the maximum given

**Inputs:**

- `right`: The prefix to set as maximum.
- `left`: A comma-separated list of CIDR to validate (IPv4 or IPv6).


## CimTrak - Example - Analyze Intrusion

**Type:** playbook  
**Product:** CimTrak - System Integrity Assurance  
**Inputs:**

- `Indicator Query`: Indicators matching the indicator query will be used as playbook input
- `lObjectDetailID`: 
- `lParentID`: 


## CimTrak - System Integrity Assurance

**Type:** integration  
**Product:** CimTrak - System Integrity Assurance  

CimTrak platform integration

**Commands:**

- `get-events`: 
- `file-analysis-by-hash`: 
- `file-analysis-by-objectdetail-id`: 
- `check-file-against-trusted-file-registry-by-hash`: 
- `promote-authoritative-baseline-files`: 
- `demote-authoritative-baseline-files`: 
- `update-task-disposition`: 
- `get-tickets`: 
- `get-ticket-tasks`: 
- `add-ticket`: 
- `update-ticket`: 
- `add-ticket-comment`: 
- `add-hash-allow-list`: 
- `add-hash-deny-list`: 
- `delete-hash-allow-list`: 


## CIRCL CVE Search

**Type:** integration  
**Product:** CIRCL  

Searches for CVE information using circl.lu

**Commands:**

- `cve-latest`: Deprecated. use NVD feed 2.0 instead. Returns the latest updated CVEs.
- `cve`: Returns CVE information by CVE ID.


## CircleCI

**Type:** integration  
**Product:** CircleCI  

Gets the details of the CircleCI workflows; including the details of the last runs and the jobs, and retrieves the artifacts of the jobs. This integration was integrated and tested with version v2 of CircleCI

**Commands:**

- `circleci-workflows-list`: Gets information on workflows.
- `circleci-artifacts-list`: Retrieves the artifacts list from the CircleCI job.
- `circleci-workflow-jobs-list`: Retrieves the jobs list from the CircleCI workflow.
- `circleci-workflow-last-runs`: Retrieves the jobs list from the CircleCI workflow.
- `circleci-trigger-workflow`: Triggers a new pipeline on the project.


## CIRCLEHashlookup

**Type:** integration  
**Product:** CIRCL hashlookup (hashlookup.circl.lu)  

CIRCL hash lookup is a public API to lookup hash values against known database of files. NSRL RDS database is included and many others are also included. The API is accessible via HTTP ReST API and the API is also described as an OpenAPI. The service is free and served as a best-effort basis. This integration was integrated and tested with online version of CIRCLEHashlookup

**Commands:**

- `circl-info`: Get information about the hash lookup database
- `circl-bulk-sha1`: Bulk search of SHA1 hashes
- `circl-top`: Return the top 100 of most queried values.


## Cisco AMP v2

**Type:** integration  
**Product:** Cisco AMP  

Cisco Advanced Malware Protection software is designed to prevent, detect, and help remove threats in an efficient manner from computer systems. Threats can take the form of software viruses and other malware such as ransomware, worms, Trojans, spyware, adware, and fileless malware. This integration was integrated and tested with version 1 of CiscoAMP

**Commands:**

- `cisco-amp-computer-list`: Fetch computers to shows information about them. Can be filtered by a variety of criteria.
- `cisco-amp-computer-trajectory-list`: Provides a list of all activities associated with a particular computer. This is analogous to the Device Trajectory on the FireAMP console.
- `cisco-amp-computer-user-activity-list`: Fetch a list of computers that have observed activity by given username.
- `cisco-amp-computer-user-trajectory-list`: Fetch a specific computer's trajectory with a given connector_guid and filter for events with user name activity.
- `cisco-amp-computer-vulnerabilities-list`: Provides a list of vulnerabilities observed on a specific computer. The vulnerabilities can be filtered to show only vulnerable applications observed for a spec
- `cisco-amp-computer-move`: Moves a computer to a group with a given connector_guid and group_guid.
- `cisco-amp-computer-delete`: Deletes a specific computer with given connector GUID.
- `cisco-amp-computer-activity-list`: Fetch a list of computers that have observed files with a given file name. Provides the ability to search all computers across an organization for any events or
- `cisco-amp-computer-isolation-feature-availability-get`: Performs a feature availability request on a computer. Isolation must be enabled within the computer's policy. This can be done through the instance. Log in to 
- `cisco-amp-computer-isolation-get`: Returns a fine-grained isolation status for a computer. The available flag is set to true if isolation can be performed on the computer. Status will be set to o
- `cisco-amp-computer-isolation-create`: Request isolation for a computer. Supports polling. Isolation must be enabled within the computer's policy. This can be done through the instance. Log in to you
- `cisco-amp-computer-isolation-delete`: Request isolation stop for a computer. Supports polling. Isolation must be enabled within the computer's policy. This can be done through the instance. Log in t
- `cisco-amp-event-list`: Fetch a list of events that can be filtered by a variety of criteria. Each criteria type is logically ANDed with the other criteria, each selection of a criteri
- `cisco-amp-event-type-list`: Fetches a list of event types. Events are identified and filtered by a unique ID.
- `cisco-amp-file-list-list`: Returns a particular file list for application blocking or simple custom detection. file_list_guid must be provided to retrieve information about a particular f


## Cisco AppDynamics

**Type:** integration  
**Product:** Cisco AppDynamics  

AppDynamics enables you to automate incident management, gain real-time performance metrics, and optimize applications to meet business needs

**Commands:**

- `cisco-appdynamics-get-events`: Retrieves a list of events from the cisappdynamics instance.


## Cisco ASA

**Type:** integration  
**Product:** Cisco ASA  

Use the Cisco Adaptive Security Appliance Software integration to manage interfaces, rules, and network objects. This integration was integrated and tested with version 9.16(3)23 of Cisco ASA

**Commands:**

- `cisco-asa-list-network-object-group`: Retrieve information about network object groups. Network object groups can contain multiple network objects as well as inline networks or hosts. Network object
- `cisco-asa-list-local-user-group`: Retrieve information about local user groups, which are collections of user accounts, either from the local database or imported from Active Directory, that man
- `cisco-asa-list-local-user`: Retrieve information about individual local user accounts within a network system. These local users can be part of local user groups and groups imported from A
- `cisco-asa-list-time-range`: Retrieve information about time range objects. A time range object defines a specific time consisting of a start time, an end time, and optional recurring entri
- `cisco-asa-list-security-object-group`: Retrieve information about security groups, which are collections of security groups or identifiers that manage access and permissions to network resources. The
- `cisco-asa-list-user-object`: Retrieve information about user definitions within the system. This helps in managing and configuring user access and permissions in a network security context.
- `cisco-asa-write-memory`: Saves the running configuration to the default location for the startup configuration.
- `cisco-asa-list-rules`: Gets a list all rules for the supplied interface.
- `cisco-asa-backup`: Creates a backup of the current settings (i.e., the backup.cfg file).
- `cisco-asa-get-rule-by-id`: Gets a specific rule by rule ID.
- `cisco-asa-create-rule`: Creates a rule.
- `cisco-asa-delete-rule`: Deletes a rule.
- `cisco-asa-edit-rule`: Updates an existing rule.
- `cisco-asa-list-network-objects`: Gets a list all configured network objects.
- `cisco-asa-create-network-object`: Creates a network object.


## Cisco ESA

**Type:** integration  
**Product:** Cisco Email Security Appliance (IronPort)  

The Cisco Email Security Appliance is an email security gateway product. It is designed to detect and block a wide variety of email-born threats, such as malware, spam and phishing attempts. This integration was integrated and tested with version 16.0 of Cisco Email Security Appliance

**Commands:**

- `cisco-esa-spam-quarantine-message-search`: Search messages in the spam quarantine.
- `cisco-esa-spam-quarantine-message-get`: Get spam quarantine message details.
- `cisco-esa-spam-quarantine-message-release`: Release quarantine emails.
- `cisco-esa-spam-quarantine-message-delete`: Delete quarantine emails.
- `cisco-esa-list-entry-get`: Get spam quarantine blocklist/safelist entry.
- `cisco-esa-list-entry-add`: Add spam quarantine blocklist/safelist entry.
- `cisco-esa-list-entry-append`: Append spam quarantine blocklist/safelist entry.
- `cisco-esa-list-entry-edit`: Edit spam quarantine blocklist/safelist entry. Using this command will override the existing value.
- `cisco-esa-list-entry-delete`: Delete spam quarantine blocklist/safelist entry.
- `cisco-esa-message-search`: Search tracking messages.
- `cisco-esa-message-details-get`: Get message details.
- `cisco-esa-message-amp-details-get`: Get message AMP summary details.
- `cisco-esa-message-dlp-details-get`: Get message DLP summary details.
- `cisco-esa-message-url-details-get`: Get message URL summary details.
- `cisco-esa-report-get`: Get statistics reports. Note that each report type is compatible with different arguments. Refer to Addendum for Cisco Secure Email Gateway ("Secure Email Repor


## Cisco ETD Connector

**Type:** integration  
**Product:** ETD platform Connector  

Fetches Cisco Email Threat Defense (ETD) message events and creates incidents. This integration was integrated and tested with of ETDConnector

**Commands:**

- `cisco-etd-move-message`: Reclassifies and remediates an ETD message.


## Cisco Firepower

**Type:** integration  
**Product:** Cisco Firepower  
**Commands:**

- `ciscofp-list-zones`: Retrieves a list of all security zone objects.
- `ciscofp-list-ports`: Retrieves a list of all port objects.
- `ciscofp-list-url-categories`: Retrieves a list of all URL category objects.
- `ciscofp-get-network-object`: Retrieves the network objects associated with the specified ID. If no ID is supplied, retrieves a list of all network objects.
- `ciscofp-create-network-object`: Creates a network object.
- `ciscofp-update-network-object`: Updates the specified network object.
- `ciscofp-get-network-groups-object`: Retrieves the groups of network objects and addresses associated with the specified ID. If no ID is supplied, retrieves a list of all network objects.
- `ciscofp-create-network-groups-objects`: Creates a group of network objects.
- `ciscofp-update-network-groups-objects`: Updates a group of network objects.
- `ciscofp-delete-network-groups-objects`: Deletes a group of network objects.
- `ciscofp-get-host-object`: Retrieves the groups of host objects associated with the specified ID. If no ID is passed, retrieves a list of all network objects.
- `ciscofp-create-host-object`: Creates a host object.
- `ciscofp-update-host-object`: Updates the specified host object.
- `ciscofp-delete-network-object`: Deletes the specified network object.
- `ciscofp-delete-host-object`: Deletes the specified host object.


## Cisco FirePower- Append network group object

**Type:** playbook  
**Product:** Cisco Firepower  

This playbook will append a network group object with new elements (IPs or network objects)

**Inputs:**

- `ID`: The ID of the network group object to append. This information can be retrieved using - !ciscofp-get-network-groups-object
- `Name`: The name of the network group.
- `Override`: Possible Value: True / False
- `IP`: Enter a comma-separated list of IPs that will be added to the list.
- `ObjectID`: You may add a group of IPs by using the Object ID. You can use !ciscofp-get-network-object for more details. For example, if you have certai


## Cisco Meraki v2

**Type:** integration  
**Product:** Cisco Meraki  

Cisco Meraki is a cloud-managed IT company that simplifies networking, security, communications, and endpoint management. Its platform offers centralized management for devices, networks, and security through an intuitive web interface. Key functionalities include managing organizations, networks, devices, and their licenses, as well as monitoring device statuses and client activities. This integration was integrated and tested with version MR 30.7 and MX 18.211.2 of Cisco Meraki v2. Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `meraki-organization-list`: List the organizations that the user has privileges on.
- `meraki-network-list`: List the networks that the user has privileges on in an organization.
- `meraki-organization-license-state-list`: List the license states overview of an organization.
- `meraki-organization-inventory-list`: List the device inventories for an organization.
- `meraki-device-claim`: Claim devices into a network. (Note: For recently claimed devices, it may take a few minutes for API requests against that device to succeed). This operation ca


## Cisco Secure Malware Analytics (Threat Grid) v2

**Type:** integration  
**Product:** Cisco Secure Malware Analytics  

Query and upload samples to Cisco threat grid. This integration was integrated and tested with version 2 of Cisco Secure Malware Analytics (Threat Grid)

**Commands:**

- `threat-grid-sample-list`: Search samples on the Threat Grid platform. Input parameters are ANDed together. Only finished samples can be searched (that is, the ones that are having a stat
- `threat-grid-sample-upload`: Submits a sample to threat grid for analysis. URL or file, not both.
- `threat-grid-submissions-search`: Search threat grid submissions
- `threat-grid-sample-summary-get`: Returns summary analysis information
- `threat-grid-who-am-i`: Get logged in user
- `threat-grid-rate-limit-get`: Get rate limit for a specific user name. ThreatGrid employs a simple rate limiting method for sample submissions by specifying the number of samples which can b
- `threat-grid-feed-specific-get`: Gets a specific threat feed
- `threat-grid-ip-search`: Search IPs. Please provide a single argument (only one) to use this command, as the API supports 1 filter at a time.
- `threat-grid-analysis-annotations-get`: Returns data regarding the annotations of the analysis
- `threat-grid-url-search`: Search urls. Please provide the URL in the format http://example.com:80/ (note that ThreatGrid only support '.com' domains).
- `threat-grid-feeds-artifact`: Get artifacts threat feed
- `threat-grid-feeds-domain`: Get domain threat feed
- `threat-grid-feeds-url`: Get url threat feed
- `threat-grid-feeds-ip`: Get ips threat feed
- `threat-grid-feeds-network-stream`: Get network stream threat feed


## Cisco Security Management Appliance

**Type:** integration  
**Product:** CiscoSMA  

The Security Management Appliance (SMA) is used to centralize services from Email Security Appliances (ESAs) and Web Security Appliances (WSAs). This integration was integrated and tested with version 12.0 of Cisco Security Management Appliance

**Commands:**

- `cisco-sma-spam-quarantine-message-search`: Search messages in the spam quarantine.
- `cisco-sma-spam-quarantine-message-get`: Get spam quarantine message.
- `cisco-sma-spam-quarantine-message-release`: Release spam quarantined message.
- `cisco-sma-spam-quarantine-message-delete`: Delete spam quarantined message.
- `cisco-sma-list-entry-get`: Get spam quarantine blocklist/safelist entry.
- `cisco-sma-list-entry-add`: Add spam quarantine blocklist/safelist entry.
- `cisco-sma-list-entry-append`: Append spam quarantine blocklist/safelist entry.
- `cisco-sma-list-entry-edit`: Edit the spam quarantine blocklist/safelist entry. Using this command will override the existing value.
- `cisco-sma-list-entry-delete`: Delete a spam quarantine blocklist/safelist entry.
- `cisco-sma-message-search`: Search tracking messages.
- `cisco-sma-message-details-get`: Get more details on the message.
- `cisco-sma-message-amp-details-get`: Get message AMP summary details.
- `cisco-sma-message-dlp-details-get`: Get message DLP summary details.
- `cisco-sma-message-url-details-get`: Get message URL summary details.
- `cisco-sma-report-get`: Get statistics reports. Note that each report type is compatible with different arguments. Refer to the following link ("ESA Reporting" section in the file) in 


## Cisco ThousandEyes

**Type:** integration  
**Product:** Cisco ThousandEyes  

This is the Cisco ThousandEyes event collector integration for Cortex XSIAM. This integration enables you to fetch events such as alerts and audit logs from Cisco ThousandEyes and process them within Cortex XSIAM. This integration was developed and tested with version 1.0.0 of Cisco ThousandEyes

**Commands:**

- `!cisco-thousandeyes-get-events`: Gets events from Cisco ThousandEyes.


## Cisco Umbrella Enforcement

**Type:** integration  
**Product:** Cisco Umbrella Enforcement  

Add and remove domains in Cisco OpenDNS. This integration was integrated and tested with version 1.0 of Cisco Umbrella Enforcement. Supported the platform.0.0 and later

**Commands:**

- `umbrella-domain-event-add`: Posts a malware event to the API for processing and optionally adding to a customer's domain lists.
- `umbrella-domains-list`: List of domains.
- `umbrella-domain-delete`: Delete domain.


## Cisco Umbrella Investigate

**Type:** integration  
**Product:** Cisco Umbrella Investigate  

Cisco Umbrella Investigate enable you to research domains, IPs, and URLs observed by the Umbrella resolvers. This integration was integrated and tested with version 2.0.0 of Cisco Umbrella Investigate

**Commands:**

- `umbrella-domain-categorization`: Get the status, security, and content categories for the domain.
- `umbrella-domain-search`: Search for newly seen domains that match a regular expression pattern.
- `umbrella-domain-co-occurrences`: List the co-occurences for the specified domain. A co-occurrence is when two or more domains are accessed by the same users within a small window of time. Co-oc
- `umbrella-domain-related`: List domain names that are frequently requested around the same time (up to 60 seconds before or after) as the given domain name, but that are not frequently as
- `umbrella-domain-security`: Get multiple scores or security features for a domain. You can use the scores or security features to determine relevant data points and build insights on the r
- `umbrella-get-domain-risk-score`: Get the domain risk score. The Umbrella Investigate Risk Score is based on an analysis of the lexical characteristics of the domain name, patterns in queries an
- `umbrella-list-resource-record`: List the Resource Record (RR) data for DNS responses, and categorization data, where the answer (or rdata) is the inserted value or list historical data from th
- `umbrella-list-domain-subdomain`: List sub-domains of a given domain.
- `umbrella-get-ip-bgp`: Get data about ASN and IP relationships, showing how IP addresses are related to each other and to the regional registries. You can find out more about the IP s
- `umbrella-get-asn-bgp`: Get BGP Route Information for ASN. Each hash reference contains two keys: geo and cidr. Geo is a hash reference with the country name and country code (the code
- `domain`: Get the WHOIS information for the specified domains.
- `umbrella-get-whois-for-domain`: Get the WHOIS information for the specified domains. You can search by multiple email addresses or multiple nameservers.
- `umbrella-get-domain-whois-history`: Get a WHOIS response record for a single domain with available historical WHOIS data returned in an object. The information displayed varies by registrant.
- `umbrella-get-nameserver-whois`: Get WHOIS information for the nameserver. A nameserver can potentially register hundreds or thousands of domains.
- `umbrella-get-email-whois`: Get WHOIS information for the email address. Returns the email address or addresses of the registrar for the domain or domains. The results include the total nu


## Cisco Umbrella Reporting

**Type:** integration  
**Product:** Cisco Umbrella Reporting  
**Commands:**

- `umbrella-reporting-destination-list`: List of destinations ordered by the number of requests made in descending order.
- `umbrella-reporting-category-list`: List of categories ordered by the number of requests made matching the categories in descending order.
- `umbrella-reporting-identity-list`: List of identities ordered by the number of requests made matching the categories in descending order.
- `umbrella-reporting-event-type-list`: List of event types ordered by the number of requests made for each type of event in descending order. The event types are: domain_security, domain_integration,
- `umbrella-reporting-file-list`: List of files within a time frame. Only returns proxy data.
- `umbrella-reporting-threat-list`: List of top threats within a time frame. Returns both DNS and Proxy data.
- `umbrella-reporting-activity-list`: List all activity entries (dns/proxy/firewall/ip/intrusion/amp) within the time frame.
- `umbrella-reporting-activity-get`: List all entries within a time frame based on the traffic type selected. Valid activity types are dns, proxy, firewall, intrusion, ip, amp. Only one activity ty
- `!umbrella-reporting-activity-get traffic_type=amp limit=2`: 
- `!umbrella-reporting-activity-get traffic_type=proxy limit=2`: 
- `!umbrella-reporting-activity-get traffic_type=firewall limit=2`: 
- `!umbrella-reporting-activity-get traffic_type=intrusion limit=2`: 
- `umbrella-reporting-summary-list`: Get the summary.
- `!umbrella-reporting-summary-list summary_type=category limit=1`: 
- `!umbrella-reporting-summary-list summary_type=destination limit=1`: 


## Cisco Webex Teams

**Type:** integration  
**Product:** Cisco Webex Teams  

Send messages, create rooms and more, via the Cisco Spark API. This integration was integrated and tested with version 6.2.0 of Cisco Spark

**Commands:**

- `cisco-spark-list-people`: List people
- `cisco-spark-create-person`: Create a new user account for a given organization. Only an admin can create a new user account.
- `cisco-spark-get-person-details`: Shows details for a person, by ID.
- `cisco-spark-update-person`: Update details for a person, by ID. Only an admin can update a person details.
- `cisco-spark-delete-person`: Remove a person from the system. Only an admin can remove a person.
- `cisco-spark-get-own-details`: Show the profile for the authenticated user.
- `cisco-spark-list-rooms`: List rooms.
- `cisco-spark-create-room`: Creates a room.
- `cisco-spark-get-room-details`: Shows details for a room, by ID.
- `cisco-spark-update-room`: Updates details for a room, by ID.
- `cisco-spark-delete-room`: Deletes a room, by ID. Deleted rooms cannot be recovered.
- `cisco-spark-list-memberships`: Lists all room memberships. Use either personId or personEmail to filter the results.
- `cisco-spark-create-membership`: Add someone to a room by Person ID or email address; optionally making them a moderator.
- `cisco-spark-get-membership-details`: Get details for a membership by ID.
- `cisco-spark-update-membership`: Updates properties for a membership by ID.


## Cisco WSA v2

**Type:** integration  
**Product:** Cisco WSA  

Cisco Secure Web Appliance protects your organization by automatically blocking risky sites and testing unknown sites before allowing users to click on them. This integration was integrated and tested with version 14.0.3-014 of Cisco WSA V2 Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `cisco-wsa-access-policy-list`: Retrieve access policies. Access policies contain allowed/blocked URL categories in the network.
- `cisco-wsa-access-policy-create`: Create an access policy. This command enables you to create the access policy object. To define more settings you can use the dependencies commands: cisco-wsa-a
- `cisco-wsa-access-policy-update`: Update the access policy.
- `cisco-wsa-access-policy-protocols-user-agents-update`: Update the Protocols and User Agents policy for access policy.
- `cisco-wsa-access-policy-url-filtering-update`: Update the URL filtering policy for access policy.
- `cisco-wsa-access-policy-applications-update`: Update applications policy for access policy. Only applicable for global_policy.
- `cisco-wsa-access-policy-objects-update`: Update objects policy for access policy.
- `cisco-wsa-access-policy-anti-malware-update`: Update the anti-malware policy for access policy.
- `cisco-wsa-access-policy-delete`: Delete access policy.
- `cisco-wsa-domain-map-list`: Retrieve domains mapping. Domain maps are DNS mappings of domain to IP addresses.
- `cisco-wsa-domain-map-create`: Create domain mapping for IP addresses.
- `cisco-wsa-domain-map-update`: Update the domain map.
- `cisco-wsa-domain-map-delete`: Delete domain map.
- `cisco-wsa-identification-profiles-list`: Retrieve identification profiles. Identification profiles are classifications of users, defining authentication requirements.
- `cisco-wsa-identification-profiles-create`: Create an identification profile.


## Citrix Cloud

**Type:** integration  
**Product:** Citrix  
**Commands:**

- `citrix-cloud-get-events`: Returns system log events extracted from Citrix.


## Citrix DaaS

**Type:** integration  
**Product:** Citrix  

Citrix DaaS simplifies the delivery and management of Citrix technologies

**Commands:**

- `citrix-daas-get-events`: Extracts Citrix configuration log events. Use with caution during development or debugging; this command may trigger event duplication or exceed API request lim


## Clarizen IAM

**Type:** integration  
**Product:** Clarizen IAM  

Integrate with Clarizen's Identity Access Management service to execute CRUD operations in the employee lifecycle processes. For more information, refer to the Identity Lifecycle Management article

**Commands:**

- `iam-create-user`: Creates a user.
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Disable an active user.


## clear-user-session

**Type:** script  
**Product:** Aggregated Scripts  

This script clears user sessions across multiple integrations for a list of usernames

**Inputs:**

- `user_name`: A list of usernames to run the session clearance operation for.
- `user_id`: A list of user ids to run the session clearance operation for.
- `brands`: Which integrations brands to run the command for. If not provided, the command will run for all available integrations. For multi-select pro
- `verbose`: Whether to retrieve human readable entry for every command or only the final result. True means to retrieve human readable entry for every c


## ClickSend

**Type:** integration  
**Product:** ClickSend  

This is the ClickSend integration for make a phonecall from platform made by Trustnet

**Commands:**

- `clicksend-text-to-voice`: Make phone call with you own text. Example: !clicksend-text-to-voice Message="Hi im here" phoneNumber=+972501234567 require_input=False voice=male
- `clicksend-voice-history`: Your calls history Example: !clicksend-voice-history


## Code42

**Type:** integration  
**Product:** Code42  

Use the Code42 integration to identify potential data exfiltration from insider threats while speeding investigation and response by providing fast access to file events and metadata across physical and cloud environments

**Commands:**

- `code42-file-events-search`: Search for Code42 Incydr File Events
- `code42-alert-get`: Retrieve alert details by alert ID
- `code42-alert-update`: Updates a Code42 Alert Session
- `code42-alert-resolve`: DEPRECATED. Use code42-alert-update instead.
- `code42-user-create`: Creates a Code42 user.
- `code42-user-block`: Blocks a user in Code42. A blocked user is not allowed to log in or restore files. Backups will continue if the user is still active.
- `code42-user-deactivate`: Deactivate a user in Code42; signing them out of their devices. Backups discontinue for a deactivated user, and their archives go to cold storage.
- `code42-user-unblock`: Removes a block, if one exists, on the user with the given user ID. Unblocked users are allowed to log in and restore.
- `code42-user-reactivate`: Reactivates the user with the given username.
- `code42-legalhold-add-user`: Adds a Code42 user to a legal hold matter.
- `code42-legalhold-remove-user`: Removes a Code42 user from a legal hold matter.
- `code42-download-file`: Downloads a file from Code42.
- `code42-download-file-by-xfc-id`: Downloads a file from Incydr using the XFC ID.
- `code42-watchlists-list`: List all existing watchlists in your environment.
- `code42-watchlists-add-user`: Add a user to a watchlist.


## Code42 Exfiltration Playbook

**Type:** playbook  
**Product:** Code42  

The Code42 Exfiltration playbook acts on Code42 Security Alerts, retrieves file event data, and allows security teams to remediate file exfiltration events by revoking access rights to cloud files or containing endpoints

**Inputs:**

- `JiraProject`: Jira Project for created incident ticket
- `JiraType`: Type of Jira ticket to create
- `JiraSummary`: Summary to use with Jira ticket creation
- `ContainHostsMax`: Maximum number of network hosts to contain.
- `platformInstanceURL`: URL of platform instance for emails.


## Code42 File Search

**Type:** playbook  
**Product:** Code42  

This playbook searches for files via Code42 security events by either MD5 or SHA256 hash. The data is output to the Code42.SecurityData context for use

**Inputs:**

- `MD5`: MD5 hash to search for
- `SHA256`: SHA256 hash to search for


## Code42 File Search v2

**Type:** playbook  
**Product:** Code42  

This playbook searches for files via Code42 security events by either MD5 or SHA256 hash. The data is output to the Code42.FileEvents context for use

**Inputs:**

- `MD5`: MD5 hash to search for
- `SHA256`: SHA256 hash to search for


## Code42 Security Alert

**Type:** playbook  
**Product:** Code42  

Retrieves Incydr alert details, assigns the alert to an analyst, and gathers employee and supervisor data from Active Directory, if applicable. Note: this playbook can be used as an alternate default to "Code42 Exfiltration Playbook" when the Code42 Incydr integration is set to "Fetch Incidents"


## Code42 Suspicious Activity Action v2

**Type:** playbook  
**Product:** Code42  

Take corrective actions against a Code42 user found to be exposing file data

**Inputs:**

- `action`: The comma-separated list of remediation actions to take on the user.
- `username`: Email id of the employee on whom action is to be taken
- `mattername`: The name of the legal hold matter.


## Code42 Suspicious Activity Review v2

**Type:** playbook  
**Product:** Code42  

Detects suspicious activities of a user and allows a recipient to assess the results. Afterward, the playbook takes action on the user such as adding them to legal hold

**Inputs:**

- `Username`: The username of the employee.
- `ReviewerEmail`: The email recipient to review potential suspicious activity related to the user, such as the user's manager.
- `LegalHoldMatterId`: The legal hold matter ID to add the user to if selecting ADD-TO-LEGAL-HOLD in the Decide Remediation Action task.


## Code42FileEventsToMarkdownTable

**Type:** script  
**Product:** Code42  

Formats Code42 File Events (both v1 and v2 event formats) to a markdown table for display in incident layout


## Cofense Triage v2

**Type:** integration  
**Product:** Cofense Triage  

Use the Cofense Triage integration to ingest reported phishing indicators. This integration was integrated and tested with version 1.20 of Cofense Triage v2

**Commands:**

- `cofense-search-reports`: Runs a query for reports.
- `cofense-search-reports`: Runs a query for reports from the inbox mailbox.
- `cofense-get-attachment`: Retrieves an attachment by the attachment ID number.
- `cofense-get-reporter`: Retrieves Email address of the reporter by ID
- `cofense-get-report-by-id`: Retrieves a report by the report ID number.
- `cofense-get-report-png-by-id`: Retrieves a report by the report ID number and displays as PNG
- `cofense-get-threat-indicators`: Threat Indicators that are designated by analysts as malicious, suspicious or benign


## Cofense Triage v3

**Type:** integration  
**Product:** Cofense Triage  

The Cofense Triage v3 integration uses the Cofense Triage v2 API (previous integrations were limited to Triage v1 API) that allows users to ingest phishing reports as incident alerts and execute commands. Security teams can ingest data from Triage such as email reporters, email reports and clusters, threat indicators, and rule matching to name a few. In addition, ingest and create threat indicators, categorize reports, and obtain second stage threat indicators from malicious emails. This integration was integrated and tested with version 1.22.0 of Cofense Triage. Some changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

**Commands:**

- `cofense-threat-indicator-list`: Retrieves the list of threat indicators based on the provided parameters. Threat indicators identify the threat level of an email's subject, sender, domains, UR
- `cofense-report-list`: Retrieves a report or a list of reports based on the filter values provided in the command arguments.
- `cofense-report-download`: Downloads the raw email for the report that matches the specified report ID.
- `cofense-report-categorize`: Categorizes a report into a specific category provided by the user.
- `cofense-report-attachment-payload-list`: Retrieves attachment payloads based on provided report id in the command arguments. Attachment payloads identify the MIME type and MD5 and SHA256 hash signature
- `cofense-report-attachment-list`: Retrieves attachments based on provided report id in the command arguments. For reported emails that contain attachments, Cofense Triage captures the attachment
- `cofense-report-attachment-download`: Downloads the attachment for the specified attachment ID.
- `cofense-category-list`: Retrieves categories based on the provided parameters. Categories are applied while processing the email to indicate the type of threat (or non-threat) that rep
- `cofense-rule-list`: Retrieves rules based on the filter values provided in the command arguments. Rules identify specific characteristics for categorizing the reported emails.
- `cofense-url-list`: Retrieves URLs based on the filter values provided in the command arguments. URLs are the threats (or non-threat) that are detected in the reported emails.
- `cofense-threat-indicator-create`: Creates a threat indicator based on the values provided in the command arguments.
- `cofense-reporter-list`: Retrieves the reporters that match the provided parameters. Reporters are employees of an organization who send, or report, suspicious emails to Cofense Triage.
- `cofense-integration-submission-get`: Retrieves integration submission based on the filter values provided in the command arguments.
- `cofense-attachment-payload-list`: Retrieves attachment payloads based on the filter values provided in the command arguments. Attachment payloads identify the MIME type and MD5 and SHA256 hash s
- `cofense-comment-list`: Retrieves comments based on the filter values provided in the command arguments.


## Cofense Vision

**Type:** integration  
**Product:** Cofense Vision  

The Cofense Vision integration provides commands to initiate advanced search jobs to hunt suspicious emails matching IOCs. It also contains commands to quarantine emails, download messages and their attachments, and aids to manage IOCs in the local repository to keep up with upcoming emerging threats. This integration was integrated and tested with version 4 of Cofense Vision and version 1 of Cofense IOC Repository

**Commands:**

- `cofense-message-token-get`: Retrieves a one-time token that can be used to get an email's content.
- `cofense-message-metadata-get`: Retrieves the full content of a message that matches the specified Internet message ID and recipient email address of an email.
- `cofense-message-get`: Fetches full content of an email and returns it as a zip file using a token.
- `cofense-message-attachment-get`: Fetches the full content of an email and returns a zip file.
- `cofense-quarantine-jobs-list`: Filters and returns a paginated list of matching quarantine jobs.
- `cofense-quarantine-job-create`: Creates a new quarantine job.
- `cofense-quarantine-job-delete`: Deletes the quarantine job identified by its unique ID.


## CofenseTriageReportDownload

**Type:** script  
**Product:** Cofense Triage  

Download all reports associated with the email address

**Inputs:**

- `email`: From address for which to download the report.


## CofenseTriageThreatEnrichment

**Type:** script  
**Product:** Cofense Triage  

Enhancement automation for type indicator, to enrich the value from Cofense Triage

**Inputs:**

- `threat_value`: Value to look up - Supports Email, Domain, URL, Hash, Hostname, SHA1, SHA256, MD5.


## Cognni

**Type:** integration  
**Product:** Cognni  

The Cognni connector offers a quick and simple integration with the platform. With Cognni, you can autonomously detect information-specific incidents based on contextual factors, and automatically compile insights to investigate how incidents occur. This intelligence provides the details you need to remediate incidents, fast enough to make a difference. This integration was integrated and tested with version 1.0 of Cognni

**Commands:**

- `cognni-get-event`: Fetches a single event by ID.
- `cognni-get-insight`: Fetches a single insight by ID.
- `cognni-fetch-insights`: Fetches insights according to severity.


## CohesityHelios

**Type:** integration  
**Product:** Cohesity Helios  

Integrate with Cohesity Helios services to fetch alerts and take remedial action. This integration was integrated and tested with version 08.01 of CohesityHelios

**Commands:**

- `cohesity-helios-get-ransomware-alerts`: Get Cohesity Helios ransomware alerts.
- `cohesity-helios-ignore-anomalous-object`: Ignore detected anomalous object by suppressing the alert.
- `cohesity-helios-restore-latest-clean-snapshot`: Restore the latest clean snapshot for the given object using incidence details.


## commentsToContext

**Type:** script  
**Product:** Common Scripts  

Use this script to take the comments of a given entry ID and stores them in the incident context, under a provided context key. In order to access the last executed task's comments, provide ${lastCompletedTaskEntries.[0]} as the value for the entryId input parameter

**Inputs:**

- `entryId`: The entry ID to get the comments from.
- `contextKey`: The context key to store comments into.
- `listSeperator`: If value is a list - provide a list seperator.


## CommitFiles

**Type:** script  
**Product:** platform CI/CD  

This script gets content files as input from the context, commits the files in the correct folder and creates the pull request text

**Inputs:**

- `files`: The files to commit.
- `branch`: The branch name to commit.
- `git_integration`: Which version control integration to use.
- `pack`: The name of the pack.
- `user`: The current user details from the command "getUsers".
- `comment`: Short description to add to the pull request text.
- `template`: Pull request description template.


## Common Server Python

**Type:** api  

Common functions that will be appended to the code of each integration/script before being executed


## CommonServerUserPowerShell

**Type:** script  

Common user-defined code that is merged into each script and integration during execution. You can use this script to define functions that are used by scripts and integrations. For example you can add a common error function for logging which wraps $platform.Error and includes extra environment information. Then you can call this function in custom integrations and scripts. Note: The code is not merged into system integrations. It is only merged into scripts (custom/system) and custom integrations. Server 6.5 and above: To disable merging the code into system scripts, set the content.oob.script.use_common_user advanced Server parameter to false


## CommonServerUserPython

**Type:** script  

Common user-defined code that is merged into each script and integrated during execution. You can use this script to define functions used by scripts and integrations. For example, you can add a common error function for logging that wraps platform.error and includes extra environment information. Then you can call this function in custom integrations and scripts. Note: The code is not merged into system integrations. It only merges into scripts (custom/system) and custom integrations. Since this code will get merged into system scripts, it is important that the syntax be compatible with both Python 2 and Python 3. Note: From October 1, 2025, Python 2 will no longer be supported. To disable merging the code into system scripts, set the content.oob.script.use_common_user advanced Server parameter to false


## CommonUserServer

**Type:** script  

Common user-defined code that is merged into each script and integration during execution. You can use this script to define functions that are used by scripts and integrations. For example you can add a common error function for logging which wraps logError and includes extra environment information. Then you can call this function in custom integrations and scripts. Note: The code is not merged into system integrations. It is only merged into scripts (custom/system) and custom integrations. Server 6.5 and above: To disable merging the code into system scripts, set the content.oob.script.use_common_user advanced Server parameter to false


## CompleteTaskOnTimerBreach

**Type:** script  
**Product:** CaseManagement-Generic  

This is an SLA breach script that will complete playbook tasks tagged with 'timerbreach' when the SLA breaches. This can be used to complete tasks waiting for manual input when a timer breaches its SLA, and move the playbook along


## Compromised Credentials Match - Flashpoint

**Type:** playbook  
**Product:** Flashpoint  

The Compromised Credentials Match playbook uses the details of the compromised credentials ingested from Flashpoint Ignite and authenticates using the Active Directory integration by providing the compromised credentials of the user. It then expires the credentials if it matches, and sends an email alert about the breach

**Inputs:**

- `username`: The username of the compromised credentials account.
- `password`: The password of the compromised credentials account.
- `sendEmailAsWarning`: Boolean input whether to send email or not.


## ConcatFormat

**Type:** script  
**Product:** Filters And Transformers  

Returns a string concatenated with given prefix & suffix which supports DT expressions

**Inputs:**

- `value`: The text to be concatenated with prefix &amp; suffix
- `prefix`: A prefix to concat to the start of the argument
- `suffix`: A prefix to concat to the end of the argument
- `ctx_data`: Context Data: Input . (single dot) on `From previous tasks` to enable to extract the context data.
- `ctx_inputs`: `inputs` context: Input 'inputs' (no quotation) on `From previous tasks` to enable ${inputs.} expression in DT.
- `ctx_inc`: `platform` context: Input 'incident' (no quotation) on `From previous tasks` to enable ${incident.} expression in DT.
- `variable_markers`: The pair of start and end markers to bracket a variable name
- `keep_symbol_to_null`: Set to true not to replace a value if the variable is null, otherwise false.


## ConcentricAI

**Type:** integration  
**Product:** ConcentricAI  

Concentric’s Semantic Intelligence™ solution discovers and protects business critical, unstructured data. We use deep learning to identify risky sharing, inappropriate third party access, assets in the wrong location, mis-classified documents, or lateral movement of data – all without rules or complex upfront configuration

**Commands:**

- `concentricai-get-file-details`: Get's file information
- `concentricai-get-users-overview`: Get overview of Users involved
- `concentricai-get-user-details`: Get's user details
- `concentricai-get-file-sharing-details`: Get's file sharing details


## ConcentricAI Demo Playbook

**Type:** playbook  
**Product:** ConcentricAI  

This playbook demonstrates how to handle a ConcentricAI risk incident. It fetches all relevant file details and user information for the owner of the flagged file

**Inputs:**

- `File Name`: File name to check.
- `Path Name`: The path of the file.
- `User Name`: The username (local part of the email) of the file owner.


## Configuration Setup

**Type:** playbook  
**Product:** platform CI/CD  

Playbook for the Cֹonfiguration Setup incident type

**Inputs:**

- `InstanceName`: Core REST API instance name to use.
- `GitlabInstanceName`: Gitlab instance name to use.


## ConfigureAzureApplicationAccessPolicy

**Type:** script  
**Product:** Microsoft Teams  

This script is grants a user the permissions needed to create a Teams meeting. It connects to MS Teams, creating an application access policy to a chosen application and then grants a user permissions. For more information, see Microsoft documentation - Allow applications to access online meetings on behalf of a user

**Inputs:**

- `username`: The login admin's username.
- `password`: The login admin's password.
- `identity`: The email of the user who will receive permissions to create a meeting.
- `app_id`: The relevant app's ID from the app studio.


## Confluera

**Type:** integration  
**Product:** Confluera  
**Commands:**

- `confluera-fetch-detections`: Fetches list of detections in confluera for past x hours.
- `confluera-fetch-progressions`: Fetches list of progressions in confluera for past x hours.
- `confluera-fetch-trail-details`: Fetches progression details of which provided trailId is a part of.


## ConflueraDetectionsCount

**Type:** script  
**Product:** Confluera  

!ConflueraDetectionsCount


## ConflueraDetectionsData

**Type:** script  
**Product:** Confluera  

!ConflueraDetectionsData


## ConflueraDetectionsDataWarroom

**Type:** script  
**Product:** Confluera  

!ConflueraDetectionsDataWarroom


## ConflueraDetectionsSummary

**Type:** script  
**Product:** Confluera  

!ConflueraDetectionsSummary


## ConflueraDetectionsSummaryWarroom

**Type:** script  
**Product:** Confluera  

!ConflueraDetectionsSummaryWarroom

**Inputs:**

- `N/A`: N/A


## ConflueraProgressionsCount

**Type:** script  
**Product:** Confluera  

!ConflueraProgressionsCount


## ConflueraProgressionsData

**Type:** script  
**Product:** Confluera  

!ConflueraProgressionsData


## ConflueraProgressionsDataWarroom

**Type:** script  
**Product:** Confluera  

!ConflueraProgressionsDataWarroom


## ContentClientApiModule

**Type:** script  

ContentClient is a drop-in replacement for BaseClient that provides enhanced reliability, observability, and developer experience features. It is designed to be fully backward compatible while offering powerful new capabilities for robust API integrations


## ContextContains

**Type:** script  
**Product:** Common Scripts  

Searches for a value in a context path

**Inputs:**

- `path`: The path in the context.
- `value`: The value to search for.


## ContextFilter

**Type:** script  
**Product:** Common Scripts  

Filters context keys by applying one of the various available manipulations and stores a new context key. The resulting context key will not be available automatically but you can still specify it as an option

**Inputs:**

- `data`: The data to apply the filter on.
- `filterType`: The type of filter to apply. Can be, "upper", "lower", "join", "split", "index", "substr", "trim", "regex", or "replace".
- `filter`: The data for the filter. Can be, "join" - the join string between elements (this is optional. The default is ','), "split" - the string on w
- `out`: The name of the context output parameter that should be written to.
- `additional`: The additional arguments to add to filter. For example, flags for regex. Flags, replace string for replace. Length for substr.


## ContextGetHashes

**Type:** script  
**Product:** Common Scripts  

Gets hashes (such as, MD5, SHA1, SHA256) from context

**Inputs:**

- `hash`: The type of hash to get. Can be, "MD5", "SHA1", "SHA256", or "all".


## ContextGetIps

**Type:** script  
**Product:** Common Scripts  

Gets all IP addresses in context, excluding ones given

**Inputs:**

- `excludedIps`: The IP addresses to exclude (comma-separated).


## ContextGetMACAddresses

**Type:** script  
**Product:** Lansweeper  

Gets all MAC addresses in context, excluding ones given

**Inputs:**

- `excludedMACAddress`: MAC addresses to exclude (separated by commas)


## ContextGetPathForString

**Type:** script  
**Product:** Common Scripts  

Searches for a string in context and returns the context path, it will return null if nothing is found

**Inputs:**

- `path`: The path in context to search the string in. If the path is not given, the search will be in the whole context.
- `str`: The string to search for in context.


## ContextReplica

**Type:** script  
**Product:** ContextReplica  

Extracts the current incident context or issue context, merges it with global contexts, and then downloads it as a flattened JSON file. This provides a replica of the JSON data seen in an Incident or Issue context in the UI


## ContextSearchForString

**Type:** script  
**Product:** Common Scripts  

Searches for a string in a path in context. If path is null, the string will be searched in full context

**Inputs:**

- `path`: The path in context to search the string in.
- `str`: The string to search for in context.


## ContextSetup

**Type:** script  
**Product:** Cortex Exposure Management  

This script simplifies how you add data to the platform. Use it to set static values or to map different values to existing context paths. Instead of a value you can enter TIMESTAMP to get the current timestamp in ISO format. For example: !ContextSetup keys=ip,src,timestamp val1=${AWS.EC2.Instances.NetworkInterfaces.PrivateIpAddress} val2="AWS" val3="TIMESTAMP" context_key="key"

**Inputs:**

- `keys`: A comma-separated list of columns for the context key.
- `val1`: A value for the 1st key. (Can be a string or context path or `TIMESTAMP` to get the current timestamp in ISO format.)
- `val2`: A value for the 2nd key. (Can be a string or context path or `TIMESTAMP` to get the current timestamp in ISO format.)
- `val3`: A value for the 3rd key. (Can be a string or context path or `TIMESTAMP` to get the current timestamp in ISO format.)
- `val4`: A value for the 4th key. (Can be a string or context path or `TIMESTAMP` to get the current timestamp in ISO format.)
- `val5`: A value for the 5th key. (Can be a string or context path or `TIMESTAMP` to get the current timestamp in ISO format.)
- `val6`: A value for the 6th key. (Can be a string or context path or `TIMESTAMP` to get the current timestamp in ISO format.)
- `val7`: A value for the 7th key. (Can be a string or context path or `TIMESTAMP` to get the current timestamp in ISO format.)


## COOCApiModule

**Type:** script  

To use the COOC API logic, run the following command to import the COOCApiModule. Then, the functionality of COOCApiModule will be available for usage. For examples, see the AWS or AZURE integrations


## Coralogix

**Type:** integration  
**Product:** Coralogix  
**Commands:**

- `coralogix-search`: Returns logs from your Coralogix account according to the specified Lucene query
- `coralogix-tag`: Allows you to tag an interesting point in time in Coralogix from the platform


## CoreXQLApiModule

**Type:** script  

To use the Core XQL API logic, run the following command to import the CoreXQLApiModule. Then, the functionality of CoreXQLApiModule will be available for usage. For examples, see the Cortex XDR - XQL Query Engine or XQL Query Engine integrations


## Cortex ASM - ASM Alert

**Type:** playbook  
**Product:** Cortex Attack Surface Management  

This playbook handles ASM alerts by enriching asset information and providing a means of remediating the issue directly or through contacting service owners

**Inputs:**

- `OwnerNotificationSubject`: Subject of the notification (email or ticket) sent to potential service owner.
- `OwnerNotificationBody`: Body of the notification (email or ticket) sent to potential service owner.
- `NotificationTicketType`: The ticket type used by ticketing systems. The default is "incident" because ticketing systems such as ServiceNow and Cherwell use it as def
- `RemediationNotificationSubject`: Subject of the notification (email or ticket) sent to the service owner after remediation.
- `RemediationNotificationHTMLBody`: Body of the notification (email or ticket) sent to the service owner after remediation.
- `BypassDevCheck`: Determine whether to bypass the Dev Check in automated remediation criteria: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex
- `AcceptedRiskIDs`: Comma-separated list of instance/VM IDs that are considered an accepted risk and that should be closed.
- `AcceptedRiskProjects`: Comma-separated list of projects numbers that are considered an accepted risk and that should be closed. For example, a list of GCP projects


## Cortex ASM - Decision

**Type:** playbook  
**Product:** Cortex Attack Surface Management  

This playbook returns "RemediationAction" options based on meeting "Automated Remediation Requirements" ( as well as whether ServiceNowV2 integration is set up. Possible return values are

**Inputs:**

- `ServiceNowv2Enabled`: ServiceNow v2 integration enabled.
- `AutoRemediationRequirements`: Meets automated remediation requirements (https://github.com/platform/content/tree/master/Packs/CortexAttackSurfaceManagement\#automated-rem


## Cortex ASM - Detect Service

**Type:** playbook  
**Product:** Cortex Attack Surface Management  

Playbook that checks to see if an existing ASM service ID is available. If it is available, it will begin a Cortex Xpanse Remediation Confirmation Scan

**Inputs:**

- `RemoteIP`: Remote IP address in the alert.
- `RemotePort`: Remote port number in the alert.
- `ASMRuleID`: Attack Surface Management Rule ID.


## Cortex ASM - Extract IP Indicator

**Type:** playbook  
**Product:** Cortex Attack Surface Management  

This playbook aims to extract the related IP address from ASM alert data and associated the newly created indicator with the alert

**Inputs:**

- `AlertName`: The formatted name of the alert


## Cortex ASM - Instant Message

**Type:** playbook  
**Product:** Cortex Attack Surface Management  

This playbook is used to create instant messages toward service owners to notify them of their internet exposures

**Inputs:**

- `OwnerNotificationBody`: Body of the notification (email or ticket) sent to the potential service owner.
- `InstantMessageChannel`: Channel to send instant messages for notification purposes. For Slack, this will be the channel ID.
- `RemediationGuidance`: Remediation Guidance of the Attack Surface Rule.


## Cortex ASM - Service Ownership

**Type:** playbook  
**Product:** Cortex Attack Surface Management  

Identifies and recommends the most likely owners of the service, additionally citing an explanation and ranking score for each


## Cortex ASM - SNMP Check

**Type:** playbook  
**Product:** Cortex Attack Surface Management  

Sub-playbook that performs an SNMP scan and checks if SNMP is enabled or not and obtains running versions

**Inputs:**

- `RemoteIP`: Remote IP address in an incident/alert.


## Cortex Attack Surface Management

**Type:** integration  
**Product:** Cortex Attack Surface Management  

Integration to pull assets and other ASM related information. This integration was integrated and tested with version 1.2.0 of Cortex Attack Surface Management

**Commands:**

- `asm-list-external-service`: Get a list of all your external services filtered by business units, externally detected providers, domain, externally inferred CVEs, active classifications, in
- `asm-get-external-service`: Get service details according to the service ID.
- `asm-list-external-ip-address-range`: Get a list of all your internet exposure filtered by business units and organization handles. Maximum result limit is 100 ranges.
- `asm-get-external-ip-address-range`: Get the external IP address range details according to the range IDs.
- `asm-list-asset-internet-exposure`: Get a list of all your internet exposure filtered by IP address, domain, type, asm id, IPv6 address, AWS/GCP/Azure tags, has XDR agent, Externally detected prov
- `asm-get-asset-internet-exposure`: Get internet exposure asset details according to the asset ID.
- `asm-list-remediation-rule`: Returns the list of remediation path rules. This command applies only to Expander v2.
- `asm-start-remediation-confirmation-scan`: Starts a new Remediation Confirmation Scan or gets an existing scan ID.
- `asm-get-remediation-confirmation-scan-status`: Get the status of an existing Remediation Confirmation Scan.
- `asm-get-attack-surface-rule`: Get information of an attack surface rule ID.


## Cortex EM - ServiceNow CMDB

**Type:** playbook  
**Product:** Cortex Exposure Management  

This playbook enriches ServiceNow CMDB data related to exposure issues by using provided indicators such as IPs, hostnames, and FQDNs

**Inputs:**

- `IPv4`: IPv4 address
- `IPv6`: IPv6 address
- `HostName`: Hostname
- `FQDN`: Fully Qualified Domain Name


## Cortex Platform - Core

**Type:** integration  
**Product:** Core  

This integration uses the Cortex API to access all the core services and capabilities of the Cortex platform

**Commands:**

- `core-get-asset-details`: Get asset information.
- `core-get-issues`: Returns a list of issues and their metadata, which you can filter by built-in arguments or use the custom_filter to input a JSON filter object. Multiple filter 
- `core-get-case-extra-data`: Get extra data fields of a specific case including issues and key artifacts.
- `core-get-cases`: Get case information based on the specified filters.
- `core-update-case`: Updates the properties of a case.
- `core-search-asset-groups`: Retrieve asset groups from the Cortex platform with optional filtering.
- `core-get-vulnerabilities`: Retrieves vulnerabilities based on specified filters.
- `core-search-assets`: Retrieves asset from the Cortex platform using optional filter criteria.
- `core-get-issue-recommendations`: Get comprehensive recommendations for an issue, including remediation steps, playbook suggestions, and recommended actions.
- `core-enable-scanners`: Enable or disable scanners with the specified configuration.
- `core-get-asset-coverage-histogram`: Calculates the distribution of values (counts and percentages) for specified categorical fields.
- `core-get-asset-coverage`: Retrieves a list of assets (e.g., Repositories, CI/CD Pipelines, Container Image Repositories) along with their scan coverage status.
- `core-create-appsec-policy`: Creates a new AppSec policy in Cortex Platform with defined conditions, scope, and triggers for application security governance.
- `core-update-issue`: Updates the properties of an issue. This command does not provide an explicit indication of success.
- `core-appsec-remediate-issue`: Create automated pull requests to fix multiple security issues in a single bulk operation.


## Cortex XDR - CVE-2025-31324 - SAP NetWeaver Visual Composer

**Type:** playbook  
**Product:** CVE-2025-31324 - SAP NetWeaver Visual Composer  

This playbook should be triggered manually or can be configured as a job. Please create a new incident and choose the Cortex XDR - CVE-2025-31324 - SAP NetWeaver Visual Composer playbook and Rapid Breach Response incident type. CVE-2025-31324 is a critical zero-day vulnerability affecting the Metadata Uploader component of SAP NetWeaver Visual Composer. The vulnerability arises from missing authorization checks, allowing unauthenticated attackers to upload malicious executable binaries. Exploitation of this flaw can lead to full remote code execution (RCE) on affected systems, posing a significant risk to confidentiality, integrity, and availability

**Inputs:**

- `SplunkEarliestTime`: The earliest time for Splunk query.
- `SplunkLatestTime`: The latest time for the Splunk search query.
- `QRadarTimeRange`: The time range for QRadar query.
- `PlaybookDescription`: The playbook description for the Rapid Breach Response layout.


## Cortex XDR - Get entity alerts by MITRE tactics CTF

**Type:** playbook  
**Product:** Capture The Flag - 01  

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


## Cortex XDR - IR CTF

**Type:** integration  
**Product:** Capture The Flag - 01  

This integration is a Mock customized only for the Capture The Flag challenge

**Commands:**

- `get-mapping-fields`: Gets mapping fields from remote incident. Note: This method will not update the current incident, it's here for debugging purposes.
- `xdr-get-incident-extra-data-ctf`: Returns additional data for the specified incident, for example, related alerts, file artifacts, network artifacts, and so on.
- `xdr-endpoint-isolate-ctf`: Isolates the specified endpoint.
- `xdr-file-retrieve-ctf`: Retrieves files from selected endpoints. You can retrieve up to 20 files, from no more than 10 endpoints. At least one endpoint ID and one file path are necessa
- `xdr-get-alerts-ctf`: Returns a list of alerts and their metadata, which you can filter by built-in arguments or use the custom_filter to input a JSON filter object. Multiple filter 


## Cortex XDR - Possible External RDP Brute-Force CTF

**Type:** playbook  
**Product:** Capture The Flag - 01  

This playbook investigates a “Possible External RDP Brute Force” XDR Alert by gathering user, IP, and hostname information, and investigating if the following suspicious elements exists: Set verdict method

**Inputs:**

- `Username`: RDP connection username.
- `ExternalIP`: Source external IP address.
- `AutoRemediation`: Set this value to "true" to enable auto remediation (IP Block and User Block).
- `FinalThreshold`: The threshold number of suspicious elements required to determine a 'True Positive' verdict.
- `CriticalElement`: You can select a specific element that, if identified as suspicious, will automatically set the final verdict as true positive. The followin
- `UserEngagementThreshold`: The threshold number of suspicious elements that will trigger a user engagement. Set 0 to disable user engagement.NOTICE: If this threshold 
- `Hostname`: RDP connection destination hostname.
- `EndpointID`: RDP connection destination endpoint ID.


## Cortex XDR Alerts Handling CTF

**Type:** playbook  
**Product:** Capture The Flag - 01  

This playbook is used to loop over every alert in a Cortex XDR incident. Supported alert categories

**Inputs:**

- `incident_id`: Incident ID.
- `alert_id`: Alert ID.


## Cortex XDR incident handling v3 CTF

**Type:** playbook  
**Product:** Capture The Flag - 01  

This playbook is triggered by fetching a Palo Alto Networks Cortex XDR incident. The playbook syncs and updates new XDR alerts that construct the incident and triggers a sub-playbook to handle each alert by type. Then, the playbook performs enrichment on the incident’s indicators and hunts for related IOCs. Based on the severity, it lets the analyst decide whether to continue to the remediation stage or close the investigation as a false positive. After the remediation, if there are no new alerts, the playbook stops the alert sync and closes the XDR incident and investigation. For performing the bidirectional sync, the playbook uses the incoming and outgoing mirroring feature added in platform version 6.0.0. After the Calculate Severity - Generic v2 sub-playbook’s run, the platform, and it will sync only from the platform, so manual changes for the severity field in XDR will not update in the platform incident

**Inputs:**

- `incident_id`: Incident ID.
- `LinkSimilarIncidents`: This input indicates whether the playbook will link similar incidents. To link similar incidents, specify Yes/No.
- `Hunting`: This input indicates whether the playbook will hunt for related IOCs. Specify Yes/No.
- `InternalRange`: A comma-separated list of internal IP ranges to check IP addresses against. The list should be provided in CIDR notation. An example of a li
- `CriticalUsernames`: A comma-separated list of names of critical users in the organization.This will affect the calculated severity of the incident.
- `CriticalHostnames`: A comma-separated list of names of critical endpoints in the organization. This will affect the calculated severity of the incident.
- `CriticalADGroups`: A comma-separated list of DN names of critical Active Directory groups. This will affect the severity calculated for this incident.
- `InternalHostRegex`: This is provided for the IsInternalHostName script that checks if the detected host names are internal or external if the hosts match the or


## Cortex Xpanse

**Type:** integration  
**Product:** Cortex Xpanse  

Integration to pull assets and other ASM related information. This integration was integrated and tested with version 2.0 of Cortex Expander

**Commands:**

- `asm-list-external-service`: Get a list of all your external services filtered by business units, externally detected providers, domain, externally inferred CVEs, active classifications, in
- `asm-get-external-service`: Get service details according to the service ID.
- `asm-list-external-ip-address-range`: Get a list of all your internet exposures filtered by business units and organization handles. Maximum result limit is 100 ranges.
- `asm-get-external-ip-address-range`: Get external IP address range details according to the range IDs.
- `asm-list-asset-internet-exposure`: Get a list of all your internet exposures filtered by IP address, domain, type, asm id, IPv6 address, AWS/GCP/Azure tags, has XDR agent, Externally detected pro
- `asm-get-asset-internet-exposure`: Get internet exposure asset details according to the asset ID.
- `asm-list-alerts`: Get a list of all your ASM alerts filtered by alert IDs, severity and/or creation time. Can also sort by creation time or severity. Maximum result limit is 100 
- `asm-get-attack-surface-rule`: Fetches attack surface rules related to how Cortex Xpanse does assessment.
- `asm-tag-asset-assign`: Assigns tags to a list of assets.
- `asm-tag-asset-remove`: Removes tags from a list of assets.
- `asm-tag-range-assign`: Assigns tags to a list of IP ranges.
- `asm-tag-range-remove`: Removes tags from a list of IP ranges.
- `asm-list-incidents`: Fetches ASM incidents that match provided filters. Incidents are an aggregation of related alerts. Note: Incident IDs may also be references as "Case IDs' elsew
- `asm-get-incident`: Returns additional details about a specific incident. Note: Incident IDs may also be references as "Case IDs" elsewhere in the API.
- `asm-update-incident`: Updates a given incident. Can be used to modify the status, severity, assignee, or add comments.


## CounterCraft Deception Director

**Type:** integration  
**Product:** CounterCraft Deception Director  
**Commands:**

- `countercraft-list-campaigns`: List all deception campaigns
- `countercraft-list-hosts`: Lists all deception hosts
- `countercraft-list-services`: List services currently deployed on deception hosts
- `countercraft-list-breadcrumbs`: List breadcrumbs in a campaign
- `countercraft-get-object`: Get information about an object (IoC)
- `countercraft-get-events`: Get full list of Events
- `countercraft-create-campaign`: Create a new deception campaign
- `countercraft-list-dsns`: List Deception Support Nodes (DSNs)
- `countercraft-list-providers`: List providers (providers for hosts or services i.e. AWS or Office365)
- `countercraft-create-host-machine`: Deploy a new deception host
- `countercraft-list-incidents`: List all incidents currently active
- `countercraft-manage-campaign`: Manage Campaign parameters
- `countercraft-manage-host`: Manage a deception host
- `countercraft-manage-service`: Manage a deception service
- `countercraft-manage-breadcrumb`: Manage breadcrumb


## CounterTack

**Type:** integration  
**Product:** CounterTack  

CounterTack empowers endpoint security teams to assure endpoint protection for Identifying Cyber Threats. Integrating a predictive endpoint protection platform

**Commands:**

- `countertack-get-endpoints`: Returns information for endpoints.
- `countertack-get-behaviors`: Returns information for all behaviors.
- `countertack-get-endpoint`: Get information on specific endpoint
- `countertack-get-behavior`: Gets information of a given behavior.
- `countertack-get-endpoint-tags`: Gets the tags of a given endpoint.
- `countertack-add-tags`: Adds tags to a given endpoint.
- `countertack-delete-tags`: Deletes the supplied tags from a given endpoint.
- `countertack-add-behavior-tags`: Adds tags to a given behavior.
- `countertack-delete-behavior-tags`: Deletes the supplied tags from a given behavior.
- `countertack-endpoint-quarantine`: Quarantines a given endpoint.
- `countertack-disable-quarantine`: Removes a given endpoint from quarantine.
- `countertack-extract-file`: Extracts a file from given endpoint.
- `countertack-delete-file`: Deletes a file from the given endpoint.
- `countertack-get-all-files`: Gets all extracted files for all endpoints.
- `countertack-get-endpoint-files`: Returns all extracted files from a given endpoint.


## Covalence For Security Providers

**Type:** integration  
**Product:** Covalence For Security Providers  

Triggers by any alert from endpoint, cloud, and network security monitoring, with mitigation steps where applicable. Query Covalence for more detail. This integration was integrated and tested with version 3.0 of Covalence For Security Providers

**Commands:**

- `cov-secpr-list-alerts`: Lists Covalence alerts
- `cov-secpr-list-sensors`: Lists Covalence sensors
- `cov-secpr-get-sensor`: Get sensor details when provided with the sensor id
- `cov-secpr-connections-summary-ip`: List summarized connections details by IP Address
- `cov-secpr-connections-summary-port`: List summarized connections details by Port
- `cov-secpr-list-dns-resolutions`: List summarized connections details by Port
- `cov-secpr-list-internal-networks`: List internal networks
- `cov-secpr-set-internal-networks`: Set internal networks
- `cov-secpr-list-endpoint-agents`: List endpoint agents
- `cov-secpr-find-endpoint-agents-by-user`: List endpoint agents where the last session user is the one provided as parameter
- `cov-secpr-find-endpoint-agents-by-uuid`: Find the endpoint agent with the UUID provided as parameter
- `cov-secpr-search-endpoint-process`: Search processes by name or advanced filter, at least one parameter is required
- `cov-secpr-search-endpoint-installed-software`: Search for endpoint installed software
- `cov-secpr-list-organizations`: List monitored organizations, only available in broker mode


## Covalence Managed Security

**Type:** integration  
**Product:** Covalence Managed Security  

Triggers by triaged alerts from endpoint, cloud, and network security monitoring. Contains event details and easy-to-follow mitigation steps. This integration was integrated and tested with version 1.1.10 of Covalence Managed Security

**Commands:**

- `cov-mgsec-get-aro`: Query FES Portal for ARO.
- `cov-mgsec-list-org`: List organizations.
- `cov-mgsec-transition-aro`: Transition an ARO.
- `cov-mgsec-transition-aro`: Transition an ARO.
- `cov-mgsec-broker-cloud-action-by-aro`: Broker - Cloud Action By ARO.
- `cov-mgsec-broker-endpoint-action-by-aro`: Broker - Endpoint Action By ARO.
- `cov-mgsec-broker-ping`: Broker - Ping.


## Create Jira Issue

**Type:** playbook  
**Product:** Atlassian Jira  

Create Jira issue allows you to open new issues. When creating the issue, you can decide to update based on on the issue's state, which will wait for the issue to resolve or close with StatePolling. Alternatively, you can select to mirror the Jira issue and incident fields. To apply either of these options, set the SyncTicket value in the playbook inputs to one of the following options: When creating Jira issues through platform, using the mirroring function, make sure that you exclude those issues when fetching incidents. To exclude these issues, tag the relevant issues with a dedicated label and exclude that label from the JQL query (Labels!=)

**Inputs:**

- `Summary`: Set the summary of the ticket.
- `Description`: Set the description of the ticket.
- `ProjectKey`: Jira Project Key
- `IssueTypeName`: TaskName
- `SyncTicket`: Set the value of the desired sync method with Jira Issue. you can choose one of three options:1. StatePolling2. Mirror 3. Blank for none Gen
- `PollingInterval`: Set interval time for the polling to run(In minutes)
- `PollingTimeout`: Set the amount of time to poll the status of the ticket before declaring a timeout and resuming the playbook.(In minutes)
- `AdditionalPollingCommandName`: In this use case, Additional polling commands are relevant when using StatePolling, and there is more than one Jira instance. It will specif


## Create list for PTH

**Type:** playbook  
**Product:** CertStream  

This playbook help analysts creating a new list of domains to monitor using CertStream integration

**Inputs:**

- `ResultsLimit`: Number of websites results to return
- `AuthenticationType`: The authentication type of the returned websites. default is all
- `LLMHomogrpahEnable`: Enable/Disable using LLM (default to chatGPT) to generate homographic permutations of the domain to hunt
- `DomainsListName`: The name for the list of domain homographs


## Create Test Incidents

**Type:** integration  
**Product:** Developer Tools  

CreateIncidents fetches incident created manually

**Commands:**

- `create-test-incident-from-file`: Creates incidents from JSON files provided, and stores them in the instance context.
- `create-test-incident-from-raw-json`: Creates incidents from a JSON file, and stores it in the instance context.


## Cribl Search

**Type:** integration  
**Product:** Cribl  

Cribl Search is a search solution that allows you to query, retrieve, and manage search jobs, datasets, and saved searches across your Cribl Cloud deployment. This integration was integrated and tested with version 4.17.0 of Cribl API

**Commands:**

- `cribl-search-query`: Runs a search query against Cribl Search and returns results.
- `cribl-search-status`: Retrieves the status of a specific search job.
- `cribl-search-result`: Retrieves the results of a completed search job.
- `cribl-search-job-create`: Creates a new search job in Cribl Search.
- `cribl-search-job-list`: Retrieves a list of search jobs or details of a specific search job.
- `cribl-search-job-update`: Updates a search job's status or privacy setting. At least one of status or is_private must be provided.
- `cribl-search-job-delete`: Deletes a specific search job.
- `cribl-search-dataset-list`: Retrieves a list of available datasets or details of a specific dataset.
- `cribl-saved-search-list`: Retrieves a list of saved searches or details of a specific saved search.


## Criminal_IP_Check_Malicious_Domain

**Type:** playbook  
**Product:** CriminalIP  

Performs Quick, Lite, and Full scans in sequence using the Criminal IP API to determine whether the input domain is malicious or not. If a determination cannot be made from the Quick scan, a Lite scan is performed. Similarly, if a determination cannot be made from the Lite scan, a Full scan is performed to make a determination. Additionally, if a Full scan is conducted, an overview report of notable findings is compiled through domain-full-scan-make-email-body and sent via email. For this purpose, the user needs to fill in the arguments for the #43 send-mail command

**Inputs:**

- `Domain`: Domain to determine whether it is malicious or not


## Criminal_IP_Micro_Asm

**Type:** playbook  
**Product:** CriminalIP  

This playbook accepts a list of domains as input and sequentially executes the sub-playbook ‘Criminal_IP_Run_Micro_Asm’ for each domain in the list. After processing all domains, it aggregates the individual Micro ASM results and sends a summary to the user via email. Accordingly, the user must configure the required parameters for the #4 send-mail command to enable email delivery. Additionally, this playbook can be registered as a scheduled job to fully automate the process

**Inputs:**

- `Domains`: A list of domains that require Micro ASM analysis. This must be provided as a list-type input.


## Criminal_IP_Run_Micro_Asm

**Type:** playbook  
**Product:** CriminalIP  

This playbook accepts a list of domains as input. For each individual domain, it performs a full domain scan (domain-full-scan). Once the scan is completed, it proceeds to execute Micro ASM on the scanned domain. The results of the Micro ASM analysis are stored in the playbook’s context. This playbook is intended to be used as a sub-playbook within the "Criminal_IP_Micro_Asm" playbook. For additional information, please refer to the documentation of the "Criminal_IP_Micro_Asm" playbook

**Inputs:**

- `Domain`: A single domain to be analyzed using micro-asm


## CriminalIP

**Type:** integration  
**Product:** CriminalIP  

Criminal IP is a comprehensive cyber threat intelligence solution that provides actionable insights into IP addresses, domains, and connected assets across the internet. It enables organizations to detect malicious indicators, assess asset reputation, and enhance threat detection by integrating enriched threat data directly into security operations via the platform interface. This integration was integrated and tested with version 1.0.0 of CriminalIP

**Commands:**

- `criminal-ip-ip-report`: Provides detailed information about an IP address using Criminal IP's API.
- `criminal-ip-check-malicious-ip`: Determines whether an IP is malicious or safe through CriminalIP Asset Search.
- `criminal-ip-check-last-scan-date`: Checks if the domain has been scanned within the last 7 days.
- `criminal-ip-domain-quick-scan`: Performs a Domain Quick Scan using CriminalIP's API.
- `criminal-ip-domain-lite-scan`: Initiates a Domain Lite Scan and returns a scan_id.
- `criminal-ip-domain-lite-scan-status`: Checks the progress of the Lite Scan.
- `criminal-ip-domain-lite-scan-result`: Returns the Lite Scan results for the given scan_id.
- `criminal-ip-domain-full-scan`: Initiates a Domain Full Scan and returns a scan_id.
- `criminal-ip-domain-full-scan-status`: Checks the progress of the Full Scan.
- `criminal-ip-domain-full-scan-result`: Returns the Full Scan results for the given scan_id.
- `criminal-ip-domain-full-scan-make-email-body`: Builds an email body summarizing notable findings from a completed Full Scan.
- `criminal-ip-micro-asm`: Performs a micro ASM-style summary for a domain with a completed Full Scan.


## CrowdSec

**Type:** integration  
**Product:** CrowdSec  

Identify Malicious IP addresses with the CrowdSec CTI API

**Commands:**

- `ip`: Check the specified IP Address against the CrowdSec CTI.


## CrowdStrikeApiModule

**Type:** script  

The CrowdStrike API handles the oauth2 authentication process and API requests. When developing a CrowdStrike integration, import the API module to the integration and the authentication process will occur automatically. To use the common CrowdStrike API logic, attach the from CrowdStrikeApiModule import * # noqa: E402 line of code in the following location to import it. After you import the module, the CrowdStrikeClient will be available for use. For examples, see the CrowdStrike Falcon Intel v2 integration


## CryptoCurrenciesFormat

**Type:** script  
**Product:** Cryptocurrency  

Verifies that a cryptocurrency address is valid and only returns the address if it is valid

**Inputs:**

- `input`: The Cryptocurrency address to check.


## Cryptocurrency

**Type:** integration  
**Product:** Cryptocurrency  

Cryptocurrency will help classify Cryptocurrency indicators as suspicious when ingested

**Commands:**

- `crypto`: Return Cryptocurrency reputation.


## Cryptosim

**Type:** integration  
**Product:** Cryptosim  

CRYPTOSIM meets the SIEM needs of corporations by its unique correlation engine works in memory, capable of hierarchical correlation, supports different correlation techniques, query structure that allows all kinds of data analytics, detects AI based algorithms behavioral anomalies and threat patterns that are not in rule sets. From the personal devices we use to the most critical governmental substructures, the awareness of the importance of cyber threats in every segment of the digitalized world and the fact that cyber security must be in all areas of our lives becomes more and more obvious. The massive attacks on the global scale have clearly demonstrated the importance of taking measures against cyber threats and increasing investments on this area. CRYPTTECH continues to work towards the goal with the mission of developing new, innovative and indigenous technology and products in the increasingly complex cyber security world. CRYPTTECH provides its unique in-memory correlation capability for its SIEM product with its strong correlation system. CRYPTOSIM collects all logs, detects behavioral differences & anomalies and automatically associates them. More over it can catch APT (Advanced Persistent Threats). CRYPTTECH achieves high performance values for the SIEM product with its NoSQL structure developed by itself. CRYPTOSIM has become one of the most strategic products for perception of threats with its unique correlation features working with rules and machine learning m

**Commands:**

- `cryptosim-get-correlation-alerts`: The command is used to get correlation alerts.


## CSCDomainManager

**Type:** integration  
**Product:** CSCDomainSecurity  

CSCDomainManager uses rules-based technology, customizable reporting, granular user management, and more—and is the world's first multilingual domain management tool, available in English, French, and German. This integration was integrated and tested with version 2.0.0 of CSCDomainManager

**Commands:**

- `csc-domains-search`: Gets the domains by the applied filters
- `csc-domains-availability-check`: Check registration availability for one or more domain names
- `csc-domains-configuration-list`: Get domains configuration information for owned domains with optional filtering
- `domain`: Get domain data by qualified domain name
- `csc-domains-configuration-search`: Get configuration information for owned domains with optional filtering.


## CSCFraudProtection

**Type:** integration  
**Product:** CSCDomainSecurity  

This is an anti fraud external api for organizations. This integration was integrated and tested with version v3 of the CSC Fraud Protection API

**Commands:**

- `csc-controldetectionflowbyeventidandaction`: Control detection flow by event ID and action
- `csc-fetchthephishkitdatawithticketid`: Fetch the phishkit data with ticketId
- `csc-fetchthescreenshotdatawithticketid`: Fetch the screenshot data with ticketId
- `csc-gethtmlsourcecodeforaticket`: Get HTML Source Code for a Ticket
- `csc-getlistofbrands`: Get list of Brands
- `csc-getlistoffraudtypes`: Get list of fraud types
- `csc-listofworklogsforticketid`: List of work logs for ticket id
- `csc-listtakedownevents`: List Takedown Events
- `csc-listtakedowneventswithfilters`: List Takedown events with filters
- `csc-performanactiononasingletarget`: Perform an action on a single target
- `csc-retrieveeventscreenshotwitheventid`: Retrieve event screenshot with eventId
- `csc-getfilteredlistofmonitoringresultsspecifiedtime`: Retrieve filtered list of monitoring results within specified timeframe
- `csc-retrievelistofdetectionswithinspecifiedtimeframe`: Retrieve list of detections within specified timeframe
- `csc-getlistofmonitoringresultsspecifiedtime`: Retrieve list of monitoring results within specified timeframe
- `csc-retrievephishkitwitheventid`: Retrieve phishkit with eventId


## CSCTakedowns

**Type:** integration  
**Product:** CSCDomainSecurity  

This is a CSCTakedowns api for organizations. This integration was integrated and tested with version v3 of the CSC Fraud Protection (Takedowns) API

**Commands:**

- `csctakedowns-fetchthephishkitdatawithticketid`: Fetch the phishkit data with ticketId
- `csctakedowns-fetchthescreenshotdatawithticketid`: Fetch the screenshot data with ticketId
- `csctakedowns-gethtmlsourcecodeforaticket`: Get HTML Source Code for a Ticket
- `csctakedowns-listofworklogsforticketid`: List of work logs for ticket id
- `csctakedowns-listtakedownevents`: List Takedown Events
- `csctakedowns-listtakedowneventswithfilters`: List Takedown events with filters
- `csctakedowns-updatetheactionwithticketid`: Update the action with ticketId


## CSVFeedApiModule

**Type:** script  

To use the common CSV Feed API logic, run the following: feed_main is the main execution of the Feed API module. It can be extended or overriden in the integration main function. Note that the module expectes a feed_url_to_config parameter to extract the indicators. This is similar to the configuration in minemeld. See the module class docstring for an example


## CTF 2 - Classify an incident - RDP Brute force

**Type:** playbook  
**Product:** Capture The Flag - 02  

Classify an RDP Brute Force Incident - Run this playbook and follow the questions


## CTF-X

**Type:** playbook  
**Product:** Capture The Flag - 02  

Not so easy. This Playbook has only one task and is part of the CTF challange


## CTM360 CyberBlindspot

**Type:** integration  
**Product:** CTM360  

Take action on incidents derived from CTM360 CBS threat intelligence that is directly linked to your organization. This integration was integrated and tested with version 1.0.0 of CTM360_CyberBlindspot

**Commands:**

- `ctm360-cbs-incident-list`: Get the list of incidents from CBS.
- `ctm360-cbs-incident-close`: Close a CBS incident.
- `ctm360-cbs-incident-request-takedown`: Request a takedown of the asset where the incident was found.
- `get-mapping-fields`: Returns the list of fields for an incident type.
- `ctm360-cbs-incident-details`: Fetch details of a single incident from the CyberBlindspot platform.
- `ctm360-cbs-incident-retrieve-screenshots`: Retrieves screenshot evidence if available.
- `get-remote-data`: Gets remote data from a remote incident. This method does not update the current incident, and should be used for debugging purposes.
- `get-modified-remote-data`: Gets the list of incidents that were modified since the last update time. Note that this method is here for debugging purposes. The get-modified-remote-data com
- `update-remote-system`: Updates the remote system with local changes.


## CTM360 HackerView

**Type:** integration  
**Product:** CTM360  

External Attack Surface Management platform, which combines automated asset discovery, issue identification / management, remediation guidelines, security ratings and third party risk management. Use Module To Use to select which HackerView data source this instance fetches: This integration was integrated and tested with version 1.0.0 of CTM360_HackerView

**Commands:**

- `ctm360-hv-incident-list`: Get the list of incidents from HV.
- `ctm360-hv-incident-status-change`: Change status of a HV incident and optionally add a comment.
- `get-mapping-fields`: Returns the list of fields for an incident type.
- `ctm360-hv-incident-details`: Fetch details of a single incident from the HackerView platform.
- `get-remote-data`: Gets remote data from a remote incident. This method does not update the current incident, and should be used for debugging purposes.
- `get-modified-remote-data`: Gets the list of incidents that were modified since the last update time. Note that this method is here for debugging purposes. The get-modified-remote-data com
- `update-remote-system`: Updates the remote system with local changes.


## CuckooDisplayReport

**Type:** script  
**Product:** Cuckoo Sandbox  

Displays the contents of a Cuckoo report file from a War Room entry

**Inputs:**

- `reportentryid`: The ID of the War Room entry containing the report file.
- `sections`: The sections to show (comma-separated). Can be, "info", "statistics", "network", "dropped", "suricata", "debug", "procmemory", "signatures",
- `reportfilepath`: The local file path to the report file.
- `reportdata`: The report to be parsed.


## CustomContentBundleWizardry

**Type:** script  
**Product:** platform - Simple Dev to Prod  

This automation accepts an platform custom content bundle, and either returns a list of file names, or the files you want to the war room

**Inputs:**

- `entry_id`: The EntryID of the custom content bundle from the war room.
- `action`: Whether to list the files in the bundle, or return the selected files to the war room.
- `file_names`: Array of file names to export, generated from the listfiles action.


## CustomIndicatorDemo

**Type:** integration  
**Product:** Developer Tools  

Custom Indicator Demo is a demo integration that demonstrates the usage of the CustomIndicator helper class

**Commands:**

- `test-custom-indicator`: This command demonstrates the usage of CustomIndicator.


## Cut

**Type:** script  
**Product:** Filters And Transformers  

Cuts a string by delimiter and returns specific fields. input: "A-B-C-D-E" delimiter: "-" fields: "1,5" return: "A-E"

**Inputs:**

- `value`: The value to split.
- `delimiter`: The delimiter to cut the string by. Pass '' to set delimiter to be empty string.
- `fields`: The comma-separated field numbers. For example, "1,5,7".


## CVE-2021-40444 - MSHTML RCE

**Type:** playbook  
**Product:** CVE-2021-40444 - MSHTML RCE  

CVE-2021-4044 refers to the MSHTML engine, that has been found vulnerable to arbitrary code execution by a specially crafted Microsoft Office document or rich text format file. Mitigations: Researchers have validated this attack triggered in Windows Explorer with “Preview Mode” enabled, even in just a rich-text format RTF file (not an Office file and without ActiveX). This indicates it can be exploited even without opening the file and this invalidates Microsoft’s workaround mitigation mentioned above. This playbook should be trigger manually and includes the following tasks: More information: Microsoft MSHTML Remote Code Execution Vulnerability Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `YaraRulesSource`: The source of the Yara rules
- `SigmaRulesSource`: The source of the Sigma rules
- `SplunkEarliestTime`: The earliest time for the Splunk search query.
- `SplunkLatestTime`: The latest time for the Splunk search query.
- `BlockIndicatorsAutomatically`: Whether to automatically block the indicators involved.
- `EDLDomainBlocklist`: The name of the EDL Domain Block List.
- `QRadarTimeRange`: The time range for the QRadar search query.


## CVE-2021-44228 - Log4j RCE

**Type:** playbook  
**Product:** CVE-2021-44228 - Log4j RCE  

Critical RCE Vulnerability: log4j - CVE-2021-44228 On Dec. 9, 2021, a remote code execution (RCE) vulnerability in Apache log4j 2 was identified being exploited in the wild. Public proof of concept (PoC) code was released and subsequent investigation revealed that exploitation was incredibly easy to perform. On Dec. 14 2021, another vulnerability was discovered related the log4j 0-day exploit known as CVE-2021-45046. On Dec 18 2021, yet another vulnerability was discovered related the log4j 0-day exploit known as CVE-2021-45105 that allows an attacker with control over Thread Context Map data to cause a denial of service when a crafted string is interpreted. This issue was fixed in Log4j 2.17.0 and 2.12.3. On Dec 28 2021, another RCE vulnerability was published for Apache Log4j2, versions 2.0-beta7 through 2.17.0 (excluding security fix releases 2.3.2 and 2.12.4). In order to exploit this vulnerability, an attacker with permission to modify the logging configuration file can construct a malicious configuration using a JDBC Appender with a data source referencing a JNDI URI which can execute remote code. This issue is fixed by limiting JNDI data source names to the java protocol in Log4j2 versions 2.17.1, 2.12.4, and 2.3.2. Affected Version Apache Log4j 2.x <= 2.17.0 This playbook should be triggered manually or can be configured as a job. Please create a new incident and choose the CVE-2021-44228 - Log4j RCE playbook and Rapid Breach Response incident type. The playbook inclu

**Inputs:**

- `SplunkIndex`: The Splunk index field to search in.Default is "*"
- `SplunkSourcetype`: The Splunk sourcetype field to search in.Default is "*"
- `SplunkEarliestTime`: The earliest time for Splunk query.
- `SplunkLatestTime`: The latest time for the Splunk search query.
- `XDRScriptExecution`: Whether to investigate automatically the endpoint logs "/var/log" using XDR Endpoint Script Execution or manually.
- `XDREndpointIDs`: The Endpoint IDs to search using XDR Endpoint Script Execution in a comma delimited format. If you would like the playbook to execute the co
- `PlaybookDescription`: The playbook description for Rapid Breach Response layout.
- `EDLDomainBlocklist`: The EDL domain blocklist name.


## CVE-2022-26134 - Confluence RCE

**Type:** playbook  
**Product:** CVE-2022-26134 - Confluence RCE  

Atlassian has been made aware of the current active exploitation of a critical severity unauthenticated remote code execution vulnerability in Confluence Data Center and Server. The OGNL injection vulnerability allows an unauthenticated user to execute arbitrary code on a Confluence Server or Data Center instance. All versions of Confluence Server and Data Center prior to the fixed versions listed above are affected by this vulnerability. Atlassian has released the following versions to address this issue: Released versions 7.4.17, 7.13.7, 7.14.3, 7.15.2, 7.16.4, 7.17.4, and 7.18.1 which contain a fix for this issue. This playbook includes the following tasks: More information: Threat Brief: Atlassian Confluence Remote Code Execution Vulnerability (CVE-2022-26134) Confluence Security Advisory 2022-06-02 Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `SplunkEarliestTime`: Splunk search earliest time.
- `SplunkLatestTime`: Splunk search latest time.
- `SplunkIndex`: The Splunk index field to search in.Default is "*"
- `EDLDomainBlocklist`: The EDL domain blocklist name.
- `BlockIndicatorsAutomatically`: Whether to block the indicators automatically or not.
- `QRadarTimeRange`: The time range for QRadar query.
- `ElasticIndex`: Elastic's index name in which to search.


## CVE-2022-30190 - MSDT RCE

**Type:** playbook  
**Product:** CVE-2022-30190 - MSDT RCE  

On May 27th, a new Microsoft Office Zero-Day was discovered by Nao_sec. The new Zero-Day is a remote code execution vulnerability that exists when MSDT is called using the URL protocol from a calling application such as Word. On May 30th, Microsoft assigned CVE-2022-30190 to the MSDT vulnerability, aka Follina vulnerability. This playbook includes the following tasks: More information: Guidance for CVE-2022-30190 Microsoft Support Diagnostic Tool Vulnerability Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `SplunkIndex`: Splunk's index name in which to search. Default is "*" - All.
- `SplunkEarliestTime`: Splunk's earliest time to search.
- `SplunkLatestTime`: Splunk's latest time to search.
- `ElasticIndex`: Elastic's index name in which to search.
- `QRadarTimeRange`: QRadar's query time range.
- `PlaybookDescription`: The playbook's description.
- `RunXQLHuntingQueries`: Whether to execute the XQL queries.
- `RelatedCVEs`: Follina vulnerability CVE reference.


## CVE-2022-3786 & CVE-2022-3602 - OpenSSL X.509 Buffer Overflows

**Type:** playbook  
**Product:** CVE-2022-3786 & CVE-2022-3602 - OpenSSL X.509 Buffer Overflows  

On November 1, OpenSSL released a security advisory describing two high severity vulnerabilities within the OpenSSL library, CVE-2022-3786 and CVE-2022-3602. OpenSSL versions from 3.0.0 - 3.0.6 are vulnerable, with 3.0.7 containing the patch for both vulnerabilities. OpenSSL 1.1.1 and 1.0.2 are not affected by this issue. The vulnerability described in CVE-2022-3602 allows an attacker to obtain a 4-byte overflow on the stack by crafting a malicious email address within the attacker-controlled certificate. The overflow will result in a crash (most likely scenario) or potentially remote code execution (much less likely). In CVE-2022-3786, an attacker can achieve a stack overflow of arbitrary length by crafting a malicious email address within the attacker-controlled certificate. Both vulnerabilities are “triggered through X.509 certificate verification, specifically, name constraint checking. Note that this occurs after certificate chain signature verification and requires either a CA to have signed the malicious certificate or for the application to continue certificate verification despite failure to construct a path to a trusted issuer.” The playbook includes the following tasks: Mitigations: More information: Unit42 Threat Brief: CVE-2022-3786 and CVE-2022-3602: OpenSSL X.509 Buffer Overflows NCSC-NL - OpenSSL overview Scanning software Note: This is a beta playbook that lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Upd

**Inputs:**

- `HuntLinuxOS`: Whether to search for relevant OpenSSL 3.x processes on Linux endpoints.
- `HuntWindowsOS`: Whether to search for relevant OpenSSL 3.x processes on Windows endpoints.
- `HuntMacOS`: Whether to search for relevant OpenSSL 3.x processes on Mac endpoints.
- `SplunkIndex`: Splunk index to search.Note that the input value should include the field name as well. e.g. "index=*"
- `SplunkEarliestTime`: Splunk earliest time to search.
- `SplunkLatestTime`: Splunk latest time to search.
- `PlaybookDescription`: The playbook's description.
- `RelatedCVEs`: CVE indicators.


## CVE-2023-23397 - Microsoft Outlook EoP

**Type:** playbook  
**Product:** CVE-2023-23397 - Microsoft Outlook EoP  

Microsoft Threat Intelligence discovered limited, targeted abuse of a vulnerability in Microsoft Outlook for Windows that allows for new technology LAN manager (NTLM) credential theft. Microsoft has released CVE-2023-23397 to address the critical elevation of privilege (EoP) vulnerability affecting Microsoft Outlook for Windows. We strongly recommend all customers update Microsoft Outlook for Windows to remain secure. All supported versions of Microsoft Outlook for Windows are affected. Other versions of Microsoft Outlook such as Android, iOS, Mac, as well as Outlook on the web and other M365 services are not affected. CVE-2023-23397 is a critical EoP vulnerability in Microsoft Outlook that is triggered when an attacker sends a message with an extended MAPI property with a UNC path to an SMB (TCP 445) share on a threat actor-controlled server. No user interaction is required. The threat actor is using a connection to the remote SMB server sends the user’s NTLM negotiation message, which the attacker can then relay for authentication against other systems that support NTLM authentication. This playbook should be triggered manually or can be configured as a job. Please create a new incident and choose the CVE-2023-23397 - Microsoft Outlook EoP playbook and Rapid Breach Response incident type. The playbook includes the following tasks: Hunting: Mitigations: References: Microsoft Mitigates Outlook Elevation of Privilege Vulnerability CVE-2023-23397 Audit & Eradication Script Neo2

**Inputs:**

- `PlaybookDescription`: The playbook description to be used in the Rapid Breach Response - Set Incident Info sub-playbook.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `QRadarTimeRange`: The time range to search for indicators in the Threat Hunting - Generic playbook.
- `SplunkEarliestTime`: The earliest time to search for indicators in the Threat Hunting - Generic playbook.
- `SplunkLatestTime`: The latest time to search for indicators in the Threat Hunting - Generic playbook.
- `XQLTimeRange`: The time range for the Cortex XDR XQL query.


## CVE-2023-36884 - Microsoft Office and Windows HTML RCE

**Type:** playbook  
**Product:** CVE-2023-36884 - Microsoft Office and Windows HTML RCE  
**Inputs:**

- `PlaybookDescription`: The playbook description to be used in the Rapid Breach Response - Set Incident Info sub-playbook.
- `autoBlockIndicators`: Wether to block the indicators automatically.
- `QRadarTimeRange`: The time range for the QRadar queries.
- `SplunkEarliestTime`: The time range for the Splunk queries.
- `ElasticEarliestTime`: The time range for the Elastic queries.
- `LogAnalyticsTimespan`: The time range for the Azure Log Analytics queries.
- `XQLTimeRange`: The time range for the XQL queries.
- `ElasticIndex`: The elastic index to search in.


## CVE-2024-47575 - FortiManager Authentication Bypass

**Type:** playbook  
**Product:** CVE-2024-47575 - FortiManager Authentication Bypass  

CVE-2024-47575, also known as FortiJump, is a critical zero-day vulnerability affecting FortiManager, a centralized management platform for Fortinet devices. The vulnerability arises due to missing authentication checks in specific FortiManager REST API endpoints. An unauthenticated attacker with network access to the FortiManager device can exploit this flaw to execute arbitrary code or commands, potentially leading to complete system compromise

**Inputs:**

- `rawIoCs`: FortiGuard Labs IoCs


## CVE-2024-6387 - OpenSSH RegreSSHion RCE

**Type:** playbook  
**Product:** CVE-2024-6387 - OpenSSH RegreSSHion RCE  

RegreSSHion Vulnerability (CVE-2024-6387) On July 1, 2024, a critical signal handler race condition vulnerability was disclosed in OpenSSH servers (sshd) on glibc-based Linux systems. This vulnerability, known as RegreSSHion and tracked as CVE-2024-6387, can result in unauthenticated remote code execution (RCE) with root privileges. This vulnerability has been rated High severity (CVSS 8.1). The vulnerability impacts the following OpenSSH server versions: The SSH features in PAN-OS are not affected by CVE-2024-6387. Collect, Extract and Enrich Indicators Threat Hunting Mitigations: This playbook should be triggered manually or can be configured as a job. Please create a new incident and choose the CVE-2024-6387 - OpenSSH RegreSSHion RCE playbook and Rapid Breach Response incident type. Reference: Threat Brief: CVE-2024-6387 OpenSSH RegreSSHion Vulnerability . Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `PlaybookDescription`: The playbook description to populate the layout with.
- `RunXQLHuntingQueries`: Whether to execute the XQL query.
- `ShouldSendMail`: Whether to notify the SOC by email.
- `SOCEmailAddress`: The email address to notify


## cve-enrichment

**Type:** script  
**Product:** Aggregated Scripts  

Enriches CVE indicators with reputation data from multiple integrations and outputs a consolidated CVEEnrichment object. This script exclusively supports indicators of type CVE and will automatically create the indicator in TIM if it is not already exists. Note: This script is supported in the platform.0 and later, and in Cortex XSIAM

**Inputs:**

- `cve_list`: A comma-separated list of CVEs to enrich.
- `external_enrichment`: Whether to call external integrations for enrichment.- 'true': enrich using enabled external integrations (e.g., CIRCL CVE Search, CVE Searc
- `verbose`: Whether to retrieve a human-readable entry for every command; if false, only the final result is summarized and error entries are suppressed
- `brands`: A list of integration brands to run enrichment against. Example: `"CIRCL CVE Search, CVE Search v2"`. - If provided, only the selected brand
- `additional_fields`: When set to true, the output will also include an `AdditionalFields` objectfor each of the indicator result. `AdditionalFields` contains all


## cvss_color

**Type:** script  
**Product:** Common Scripts  

## CybelAngel

**Type:** integration  
**Product:** CybelAngel  

CybelAngel receives reports from the CybelAngel platform, which specializes in external attack surface protection and management

**Commands:**

- `cybelangel-get-events`: Send events from CybelAngel to XSIAM. Used mainly for debugging.
- `cybelangel-report-status-update`: Update the status of one or multiple reports.
- `cybelangel-report-get`: Retrieve reports from CybelAngel.
- `cybelangel-report-remediation-request-create`: Create a remediation request for a report.
- `cybelangel-report-attachment-get`: Retrieve an attachment from a report.
- `cybelangel-archive-report-by-id-get`: Retrieve an archived report by ID as a ZIP file.
- `cybelangel-mirror-report-get`: Retrieve the mirror details for the specified report.
- `cybelangel-report-comment-create`: Create a new comment on a report.
- `cybelangel-report-list`: Retrieve reports from CybelAngel.
- `cybelangel-report-comments-get`: Retrieve comments from a report.


## CybelAngel EASM

**Type:** integration  
**Product:** CybelAngel  

This integration enables the platform, allowing security teams to monitor and respond to digital risk exposure incidents

**Commands:**

- `cybelangel-get-report-by-id`: Retrieves detailed information about a specific report.
- `cybelangel-get-report-attachment`: Downloads an attachment from a specified report.
- `cybelangel-remediate`: Creates a remediation request for a specific report.
- `cybelangel-get-comments`: Retrieves comments associated with a report.
- `cybelangel-post-comment`: Adds a comment to a specified report.
- `cybelangel-update-status`: Updates the status of a report.
- `cybelangel-get-report-pdf`: Downloads the PDF version of a report.


## CyberBlindspot Incident Management

**Type:** playbook  
**Product:** CTM360  

This playbook runs the incidents through indicator enrichment, then based on the mirroring settings, it can communicate with the remote server to assist the user in the next course of action (Whether it be closing the incident, initiating the takedown of an online asset or simply waiting for a process on the remote server to end) to take on the incident if any


## CyberBlindspot Incident Management V2

**Type:** playbook  
**Product:** CTM360  

This playbook runs the incidents through indicator enrichment, then based on the mirroring settings, it can communicate with the remote server to assist the user in the next course of action (Whether it be closing the incident, initiating the takedown of an online asset or simply waiting for a process on the remote server to end) to take on the incident if any


## CyberBlindspot Incident Management V3

**Type:** playbook  
**Product:** CTM360  

This playbook runs the incidents through indicator enrichment, then based on the mirroring settings, it can communicate with the remote server to assist the user in the next course of action (Whether it be closing the incident, initiating the takedown of an online asset or simply waiting for a process on the remote server to end) to take on the incident if any


## CyberBlindspot Retrieve Incident Screenshots

**Type:** playbook  
**Product:** CTM360  

This playbook retrieves screenshot evidence from the CyberBlindspot API and adds it to the incident


## CyberChef

**Type:** integration  
**Product:** CyberChef  

CyberChef is a web-application developed by GCHQ that's been called the “Cyber Swiss Army Knife”

**Commands:**

- `cyberchef-bake`: Bake you recipe!
- `cyberchef-magic`: CyberChef Magic function


## Cyberhaven

**Type:** integration  
**Product:** Cyberhaven  

Fetches DLP incidents from the Cyberhaven data security platform and enables investigation of events and data lineage. This integration was integrated and tested with version 2 of Cyberhaven API

**Commands:**

- `cyberhaven-incident-list`: List and search Cyberhaven DLP incidents with optional filters.
- `cyberhaven-incident-update`: Update the status, assignment, or close reason of a Cyberhaven incident.
- `cyberhaven-event-details-get`: Retrieves full details for one or more Cyberhaven events by ID.
- `cyberhaven-event-lineage-get`: Retrieves the data lineage chain between two Cyberhaven event IDs.


## CyberhavenIncidentRefresh

**Type:** script  
**Product:** Cyberhaven  

Updates only Cyberhaven custom fields and never modifies the auto-generated fields

**Inputs:**

- `incident_id`: Please provide the Cyberhaven incident ID.


## Cyberpion

**Type:** integration  
**Product:** Cyberpion  

Vulnerabilities management This integration was integrated and tested with version 1.0 of Cyberpion

**Commands:**

- `cyberpion-get-domain-action-items`: Retrieves domain's action items
- `cyberpion-get-domain-state`: Retrieves domain's info and current state


## Cyberpion Domain State

**Type:** playbook  
**Product:** Cyberpion  

Allows analyst to get basic information about the domain


## Cyberwatch

**Type:** integration  
**Product:** Cyberwatch  

Find, prioritize, and fix vulnerabilities on your IT & OT assets. This integration was integrated and tested with version 13.11 of Cyberwatch

**Commands:**

- `cyberwatch-list-cves`: Get a list of CVEs from Cyberwatch.
- `cyberwatch-fetch-cve`: Get all details for a CVE from Cyberwatch.
- `cyberwatch-list-assets`: Get a list of assets scanned by Cyberwatch.
- `cyberwatch-fetch-asset`: Get security details for an asset scanned by Cyberwatch.
- `cyberwatch-fetch-asset-fulldetails`: Get all details for an asset scanned by Cyberwatch, including packages, ports, services, metadata.
- `cyberwatch-list-securityissues`: Get a list of Security issues from Cyberwatch.
- `cyberwatch-fetch-securityissue`: Get all details for a Security issue from Cyberwatch.
- `cyberwatch-list-sysadmin-assets`: Get a list of assets from Cyberwatch Sysadmin (/assets/servers) view.
- `cyberwatch-fetch-sysadmin-asset`: Get details for a Sysadmin Asset from Cyberwatch (/assets/servers/<ID>).
- `cyberwatch-list-compliance-assets`: Get a list of assets from Cyberwatch Compliance (/compliance/assets) view.
- `cyberwatch-fetch-compliance-asset`: Get details for a Compliance Asset from Cyberwatch (/compliance/assets/<ID>).
- `cyberwatch-send-declarative-data-asset`: Upload Declarative Data (airgap) built from hostname + JSON to Cyberwatch (via /api/v2/cbw_scans/scripts). The command first checks that the hostname already ex
- `cyberwatch-get-declarative-data-asset`: Retrieve Declarative Data for a Cyberwatch server (GET /api/v3/servers/{id}/info). Returns the raw text blob.


## Cyble Vision Alert V2

**Type:** playbook  
**Product:** CybleEventsV2  

This is a playbook which will handle the alerts coming from the Cyble Events service


## CybleEvents v2

**Type:** integration  
**Product:** CybleEventsV2  

Cyble Events for Vision Users. Must have Vision API access to use the threat intelligence. This integration was integrated and tested with version 2.0 of cybleeventsv2

**Commands:**

- `cyble-vision-subscribed-services`: Get list of Subscribed services
- `cyble-vision-fetch-iocs`: Fetch the indicators in the given timeline.
- `cyble-vision-fetch-alerts`: Fetch alerts based on the given parameters. The alerts would have multiple events grouped into one, based on a specific service type. This way the user will see
- `cyble-vision-fetch-alert-groups`: Fetch incident event group
- `cyble-vision-update-alerts`: Update the status and/or severity of one or more alerts by ID.


## CyCognito

**Type:** integration  
**Product:** CyCognito  

The CyCognito integration fetches issues discovered by the CyCognito platform, thereby providing users with a view of their organization's internet-exposed attack surface. These issues include identification, prioritization, and recommendations for remediation of the risks faced by the organization. The integration contains commands to query assets and issues detected by the CyCognito platform, and includes a rich dashboard and layout with issue management capability. This integration was integrated and tested with CyCognito V1 API

**Commands:**

- `cycognito-issue-get`: Retrieves information about an issue associated with a particular instance based on the provided issue instance ID.
- `cycognito-asset-get`: Retrieves information about a specific asset according to the specified asset type and asset ID.
- `cycognito-asset-investigation-status-change`: Modifies the investigation status of the specified asset.
- `cycognito-issue-investigation-status-change`: Modifies the investigation status of the specified issue.
- `cycognito-issues-list`: Retrieves the list of the issues that meet the specified filter criteria.
- `cycognito-assets-list`: Retrieves the list of assets that meet specified filter criteria.


## CyCognitoGetEndpoints

**Type:** script  
**Product:** CyCognito  

Generates a deep link to the CyCognito platform using the incident context


## Cymptom

**Type:** integration  
**Product:** Cymptom  

Cymptom is a Breach and Attack Simulation solution that revolutionizes the existing approach by transforming attack simulation into a data analysis question. Cymptom agentless scanning brings real-time always-on visibility into the entire security posture. This integration was integrated and tested with version 0.3.4 of Cymptom

**Commands:**

- `cymptom-get-mitigations`: This command returns mitigations recommended by Cymptom
- `cymptom-get-users-with-cracked-passwords`: This command returns users with cracked password


## Cymulate

**Type:** integration  
**Product:** Cymulate  
**Commands:**

- `cymulate_get_incident_info`: This commands return full cymulate's incidents information
- `cymulate-get-incident-info`: This commands return full cymulate's incidents information


## Cymulate IOC Findings Mitigation

**Type:** playbook  
**Product:** Cymulate  

Cymulate IOC Findings Mitigation is a playbook that takes IOC (Indicator of Compromise) findings from the Cymulate Exposure Management platform and automates or guides mitigation actions to update controls and reduce security gaps quickly. It helps turn validated threat indicators into practical response steps within the platform


## Cyren Inbox Security

**Type:** integration  
**Product:** Cyren Inbox Security  

Cyren Inbox Security is an innovative solution that safeguards Office 365 mailboxes in your organization against evasive phishing, business email compromise (BEC), and fraud. This integration imports incidents from Cyren Inbox Security into platform, and includes a playbook for incident resolution. This integration was integrated and tested with version 1.0 of Cyren Inbox Security

**Commands:**

- `cyren-resolve-and-remediate`: resolve a case and remediate incidents
- `cyren-reset-sample-fetch`: resets integration to fetch a sample incident


## Cyren Inbox Security Default

**Type:** playbook  
**Product:** Cyren Inbox Security  

Processes Cyren Incidents, sets resolutions, and applies remediations to end-user mailboxes


## Cyren-Find-Similar-Incidents

**Type:** script  
**Product:** Cyren Inbox Security  

Finds similar incidents by Cyren Case ID

**Inputs:**

- `case_id`: the case id of incidents to return


## Cyren-Show-Threat-Indicators

**Type:** script  
**Product:** Cyren Inbox Security  

Displays threat indicators in readable format


## DamSensorDown

**Type:** script  
**Product:** McAfee DAM  

Ignores second notifications, but will process first notification into incidents. This is a pre-processing script for Emails from Mcafee DAM, about sensor disconnected


## Darkmon

**Type:** integration  
**Product:** Darkmon  

Stay ahead of cyber threats with Darkmon TIP - real-time threat intelligence from the Clear, Deep, and Dark Web tailored to your assets. Pack also helps with integration with the platform

**Commands:**

- `dmontip-global-search`: The dmontip-global-search command performs a comprehensive search across the Darkmon Threat Intelligence Platform. This command allows users to search for indic
- `ip`: Searches the Darkmon platform for intelligence related to a specific IP address. A focused interface for threat intelligence lookup of IP indicators.
- `url`: Searches for URL-specific threat intelligence across the Darkmon platform. Quickly identifies malicious or suspicious URLs and associated threat data.
- `domain`: Performs domain-focused threat intelligence searches in the Darkmon platform. Returns comprehensive information about potentially malicious domains.
- `email`: Searches for threat intelligence related to specific email addresses. Identifies compromised accounts or emails associated with malicious activities.
- `file`: Searches the Darkmon platform using file hash values (MD5, SHA-1, SHA-256). Identifies malware and provides associated threat intelligence data.
- `dmontip-get-compromised`: Retrieve compromised data of a given type from Darkmon - leaked accounts, leaked bank cards, combo lists, public breaches, or compromised employee accounts. Use
- `dmontip-get-vpn`: Retrieve known VPN exit-node IOCs with pagination, sorted newest first by firstSeen unless overridden.
- `dmontip-get-proxy`: Retrieve known open-proxy IOCs with pagination, sorted newest first by firstSeen unless overridden.
- `dmontip-get-cve`: Retrieve security vulnerabilities (CVEs) with severity, CVSS score, published/lastModified timestamps, source identifier, and tags.
- `dmontip-get-nrd`: Retrieve newly registered domains (NRD) recently observed by Darkmon, sorted newest first by timestamp unless overridden. Filters the IOC feed by classification
- `dmontip-get-tbf`: Retrieve telnet brute-force IOCs - sources observed attempting telnet brute-force attacks, sorted newest first by timestamp unless overridden. Filters the IOC f
- `dmontip-get-ransomware`: Retrieve ransomware articles or company-specific ransomware mentions with details such as victim name, threat actor, published date, and matched keywords. Sorte
- `dmontip-get-landscape`: Retrieve cybersecurity landscape news articles or company-specific landscape mentions with title, link, source, author, and matched keywords.
- `dmontip-get-boardprotection`: Lists the emails currently under board-leak protection (monitored) including request state, owner name, and tokens. Backed by the board-leak/request endpoint.


## Darkmon - Block IOC

**Type:** playbook  
**Product:** Darkmon  

Analyst-facing wrapper around Darkmon - Generic Block Indicator. Lets analysts paste an IOC into a War Room form and trigger a provider-routed block action

**Inputs:**

- `Indicator`: The indicator value to block.
- `Type`: ip | domain | url.
- `Reason`: Reason annotated on the block rule.


## Darkmon - Brand-Targeted NRD Watch

**Type:** playbook  
**Product:** Darkmon  

Daily sweep of newly-registered domains. Each candidate's root label is compared against the brand list via DarkmonLevenshtein; matches with distance <= 2 (configurable) open a 'Darkmon Typosquatting Threat' incident


## Darkmon - Compromised Credentials Sweep

**Type:** playbook  
**Product:** Darkmon  

Polls Darkmon for compromised credentials, filters to the customer's email/web domains, dedupes via state list, and creates a 'Darkmon Compromised Credential' incident per new account. Triggered on a 4-hour Job


## Darkmon - Compromised Employee Auto-Disable

**Type:** playbook  
**Product:** Darkmon  

Hourly poll of compromised employees. For each new entry, looks up the user in the configured directory and acts per the DisableMode playbook input

**Inputs:**

- `DisableMode`: Controls how the playbook reacts when a new compromised employee account is observed. Allowed values: notify-only (default, safe) - creates 


## Darkmon - Critical CVE Pipeline

**Type:** playbook  
**Product:** Darkmon  

Daily filter of new CVEs (CVSS >= 9) against the customer's tech-stack tags. Matches open a 'Darkmon Critical CVE' incident per match and ticket via Generic Notify


## Darkmon - Enrich Domain

**Type:** playbook  
**Product:** Darkmon  

Sub-playbook that calls the Darkmon !domain command and returns DBotScore + Common.Domain for the input Domain indicator. Designed to be invoked from a parent playbook; does not auto-run on indicator creation

**Inputs:**

- `Domain`: The Domain indicator value to enrich. Defaults to ${Domain.Name}.


## Darkmon - Enrich File

**Type:** playbook  
**Product:** Darkmon  

Sub-playbook that calls the Darkmon !file command and returns DBotScore + Common.File for the input File indicator. Designed to be invoked from a parent playbook; does not auto-run on indicator creation

**Inputs:**

- `File`: The File indicator value to enrich. Defaults to ${File.MD5}.


## Darkmon - Enrich IP

**Type:** playbook  
**Product:** Darkmon  

Sub-playbook that calls the Darkmon !ip command and returns DBotScore + Common.IP for the input IP indicator. Designed to be invoked from a parent playbook; does not auto-run on indicator creation

**Inputs:**

- `IP`: The IP indicator value to enrich. Defaults to ${IP.Address}.


## Darkmon - Enrich URL

**Type:** playbook  
**Product:** Darkmon  

Sub-playbook that calls the Darkmon !url command and returns DBotScore + Common.URL for the input URL indicator. Designed to be invoked from a parent playbook; does not auto-run on indicator creation

**Inputs:**

- `URL`: The URL indicator value to enrich. Defaults to ${URL.Data}.


## Darkmon - Generic Block Indicator

**Type:** playbook  
**Product:** Darkmon  

Provider-agnostic indicator-block dispatcher. Reads the "Darkmon - Block Provider" List for the configured block target (panos | fortinet | umbrella | cloudflare) and routes to the matching command. Falls back to logging the block intent in the War Room when no provider is configured

**Inputs:**

- `Indicator`: The indicator value (IP, domain, URL) to block.
- `Type`: One of ip | domain | url.
- `Reason`: Free-text reason annotated on the block rule.


## Darkmon - Generic User Action

**Type:** playbook  
**Product:** Darkmon  

Provider-agnostic user-action dispatcher (disable, reset password, revoke sessions). Reads the "Darkmon - Identity Provider" List for the configured directory (ad | okta | azuread) and routes to the matching command

**Inputs:**

- `Username`: The directory username (sAMAccountName / UPN / login) to act on.
- `Action`: One of disable | reset-password | revoke-sessions.
- `NewPassword`: Required only when Action is reset-password.


## DarkmonCreateIncidents

**Type:** script  
**Product:** Darkmon  

Creates one platform incident per item using a name_template and field_map (comma-separated 'field=path' pairs)

**Inputs:**

- `items`: Items to process.
- `id_field`: Field name to use as the dedup key.
- `seen_list`: Name of the platform List storing already-seen IDs.
- `domain_filter_list`: Optional - list of customer domains to filter username matches.
- `domain_match_field`: Field on each item to match against domain_filter_list.
- `allowlist`: Optional list of usernames/DNs that must NEVER be actioned.
- `allowlist_match_field`: Field to match against the allowlist.
- `incident_type`: Incident type for newly created incidents.


## DarkmonFilterCVEs

**Type:** script  
**Product:** Darkmon  

Filters CVEs by CVSS minimum and intersection with a tech-stack tag list

**Inputs:**

- `items`: Items to process.
- `id_field`: Field name to use as the dedup key.
- `seen_list`: Name of the platform List storing already-seen IDs.
- `domain_filter_list`: Optional - list of customer domains to filter username matches.
- `domain_match_field`: Field on each item to match against domain_filter_list.
- `allowlist`: Optional list of usernames/DNs that must NEVER be actioned.
- `allowlist_match_field`: Field to match against the allowlist.
- `incident_type`: Incident type for newly created incidents.


## DarkmonFilterUnseen

**Type:** script  
**Product:** Darkmon  

Filters items by ID against an platform List (state) and optionally by domain match or allowlist. Updates the List with new IDs. Outputs NewAccounts

**Inputs:**

- `items`: Items to process.
- `id_field`: Field name to use as the dedup key.
- `seen_list`: Name of the platform List storing already-seen IDs.
- `domain_filter_list`: Optional - list of customer domains to filter username matches.
- `domain_match_field`: Field on each item to match against domain_filter_list.
- `allowlist`: Optional list of usernames/DNs that must NEVER be actioned.
- `allowlist_match_field`: Field to match against the allowlist.
- `incident_type`: Incident type for newly created incidents.


## DarkmonLevenshtein

**Type:** script  
**Product:** Darkmon  

Computes the minimum Levenshtein edit distance between a domain's root label and a list of brand names. Used by Darkmon - Brand-Targeted NRD Watch to flag typosquatting candidates

**Inputs:**

- `domain`: The domain to compare (only the root label is used).
- `brands`: Comma-separated brand names to compare against.


## DarkmonScoreNRDs

**Type:** script  
**Product:** Darkmon  

For each NRD, calls DarkmonLevenshtein against the brands list and emits Typosquats with distance <= max_distance

**Inputs:**

- `items`: Items to process.
- `id_field`: Field name to use as the dedup key.
- `seen_list`: Name of the platform List storing already-seen IDs.
- `domain_filter_list`: Optional - list of customer domains to filter username matches.
- `domain_match_field`: Field on each item to match against domain_filter_list.
- `allowlist`: Optional list of usernames/DNs that must NEVER be actioned.
- `allowlist_match_field`: Field to match against the allowlist.
- `incident_type`: Incident type for newly created incidents.


## DarkmonVIPFanOut

**Type:** script  
**Product:** Darkmon  

For each protected email, calls dmontip-get-boardemails three times (accounts, combo-lists, public-breaches), filters new entries, creates incidents

**Inputs:**

- `items`: Items to process.
- `id_field`: Field name to use as the dedup key.
- `seen_list`: Name of the platform List storing already-seen IDs.
- `domain_filter_list`: Optional - list of customer domains to filter username matches.
- `domain_match_field`: Field on each item to match against domain_filter_list.
- `allowlist`: Optional list of usernames/DNs that must NEVER be actioned.
- `allowlist_match_field`: Field to match against the allowlist.
- `incident_type`: Incident type for newly created incidents.


## Darktrace Admin

**Type:** integration  
**Product:** Darktrace  

Darktrace is a Cyber AI platform for threat detection and response across cloud, email, industrial, and the network. This integration was integrated and tested with version 6.0.0 of Darktrace

**Commands:**

- `darktrace-get-external-endpoint-details`: Returns details collected by Darktrace about external IP addresses or hostnames.
- `darktrace-get-device-connection-info`: Returns the graphable data used in the "Connections Data" view for a specific device that can be accessed from the Threat Visualizer omnisearch in Darktrace. Da
- `darktrace-run-advanced-search-analysis`: Runs advanced search analysis queries.
- `darktrace-post-to-watched-list`: Posts hostnames and ips to the Darktrace Watched Domain List.
- `darktrace-get-tagged-devices`: Returns all Darktrace tagged devices
- `darktrace-get-tags-for-device`: Returns all tags present on a specified device.
- `darktrace-post-tag-to-device`: Posts a tag to a device


## Darktrace AI Analyst

**Type:** integration  
**Product:** Darktrace  

Darktrace is a Cyber AI platform for threat detection and response across cloud, email, industrial, and the network. This integration was integrated and tested with version 6.0.0 of Darktrace

**Commands:**

- `darktrace-get-ai-analyst-incident-event`: Returns all AI Analyst incident events
- `darktrace-get-comments-for-ai-analyst-incident-event`: Returns all Darktrace Comments for a given Incident Event
- `darktrace-post-comment-to-ai-analyst-incident-event`: Post comment to an AI Analyst Incident Event.
- `darktrace-acknowledge-ai-analyst-incident-event`: Acknowledges an AI Analyst Incident Event
- `darktrace-unacknowledge-ai-analyst-incident-event`: Unacknowledges an AI Analyst Incident Event
- `darktrace-get-ai-analyst-incident-group-from-eventId`: Pulls all linked events for a given event. Over time, events can become merged with one another. This happens when two sets of disparate activity are suddenly l


## Darktrace ASM

**Type:** integration  
**Product:** DarktraceASM  

Darktrace is a Cyber AI platform for threat detection and response across cloud, email, industrial, and the network. This integration was integrated and tested with version 6.0.0 of Darktrace

**Commands:**

- `darktrace-asm-get-risk`: Returns the Risk object associated with the given Risk ID.
- `darktrace-asm-get-asset`: Returns the Asset object associated with the given Asset ID. The output will depend on the type of Asset(IP Address, Netblock, FQDN or Application).
- `darktrace-asm-mitigate-risk`: Mitigates Risk within the Darktrace UI. Warning: Mitigating a Risk without taking action to resolve the Risk means you accept a Risk and it will no longer appea
- `darktrace-asm-post-comment`: Post a comment to a Risk or an Asset within the Darktrace UI.
- `darktrace-asm-edit-comment`: Edit an existing comment within the Darktrace UI.
- `darktrace-asm-delete-comment`: Delete an existing comment within the Darktrace UI.
- `darktrace-asm-create-tag`: Creat a new Tag within the Darktrace UI. Tags can be applied to Assets.
- `darktrace-asm-assign-tag`: Assign an existing Tag to an Asset within the Darktrace UI.
- `darktrace-asm-unassign-tag`: Unssign an existing Tag from an Asset within the Darktrace UI.


## Darktrace ASM Basic Risk Handler

**Type:** playbook  
**Product:** DarktraceASM  

Handles each fetched Darktrace ASM Risk by offering the user the ability to take comment on Risks and Actions and actions on Risks from platform to your Darktrace deployment


## Darktrace Basic AI Analyst Event Handler

**Type:** playbook  
**Product:** Darktrace  

Handles each fetched Darktrace AI Analyst Event by gathering additional detail about the activity through enrichment data from Darktrace and platform. Additionally, it offers the ability to take proactive actions from platform to your Darktrace deployment


## Darktrace Basic Model Breach Handler

**Type:** playbook  
**Product:** Darktrace  

Handles each fetched Darktrace model breach by gathering additional detail about the activity through enrichment data from Darktrace and platform. Additionally, it offers the ability to take proactive actions from platform to your Darktrace deployment


## Darktrace Model Breaches

**Type:** integration  
**Product:** Darktrace  

Darktrace is a Cyber AI platform for threat detection and response across cloud, email, industrial, and the network. This integration was integrated and tested with version 6.0.0 of Darktrace

**Commands:**

- `darktrace-get-model-breach`: darktrace-get-model-breach returns a model breach based on its model breach id (pbid)
- `darktrace-get-model-breach-comments`: Returns the comments on a model breach based on its model breach id (pbid)
- `darktrace-acknowledge-model-breach`: Acknowledge a model breach as specified by Model Breach ID
- `darktrace-unacknowledge-model-breach`: Unacknowledges a model breach as specified by Model Breach ID
- `darktrace-get-model-breach-connections`: Returns connections encountered by the device during a model breach.
- `darktrace-get-model`: Returns a model given a UUID
- `darktrace-get-model-component`: Returns the details of a component given a CID
- `darktrace-post-comment-to-model-breach`: Posts a specified comment to a model breach.


## DataBee

**Type:** integration  
**Product:** DataBee  

DataBee, from Comcast Technology Solutions, is a cloud-native security and compliance data fabric that ingests data from multiple disparate feeds and then aggregates, compresses, standardizes, enriches, correlates, and normalizes the data before transferring a full time-series dataset to your data lake of choice. This integration was integrated and tested with version 1.0 of DataBee

**Commands:**

- `databee-device-search`: Search for devices based on filters.
- `databee-user-search`: Search for users based on filters.
- `databee-finding-search`: Search for security findings based on filters.
- `endpoint`: Returns information about an endpoint.


## Databricks

**Type:** integration  
**Product:** Databricks  

Comprehensive integration with Databricks workspace APIs for managing clusters, jobs, SQL, pipelines, Unity Catalog, MLflow, IAM, and more. This integration was integrated and tested with the Databricks REST API

**Commands:**

- `databricks-cluster-get`: Retrieves information about a cluster by its ID.
- `databricks-cluster-list`: Lists all clusters in the workspace.
- `databricks-cluster-create`: Creates a new Databricks cluster.
- `databricks-cluster-edit`: Edits the configuration of an existing cluster.
- `databricks-cluster-delete`: Terminates a cluster.
- `databricks-cluster-permanent-delete`: Permanently deletes a cluster.
- `databricks-cluster-start`: Starts a previously terminated cluster.
- `databricks-cluster-restart`: Restarts a running cluster.
- `databricks-cluster-resize`: Resizes a cluster by changing the number of workers.
- `databricks-cluster-pin`: Pins a cluster to keep it visible in the cluster list.
- `databricks-cluster-unpin`: Unpins a cluster.
- `databricks-cluster-change-owner`: Changes the owner of a cluster.
- `databricks-cluster-list-zones`: Lists available availability zones for cluster deployment.
- `databricks-cluster-update`: Updates specific properties of a cluster.
- `databricks-cluster-policy-get`: Retrieves a cluster policy by its ID.


## Dataminr Pulse

**Type:** integration  
**Product:** Dataminr Pulse  
**Commands:**

- `dataminrpulse-watchlists-get`: Retrieves the Watchlists configured on the Dataminr platform.
- `dataminrpulse-alerts-get`: Retrieves the alerts as per the provided watchlist_ids or query or configured watchlist_names parameter in integration. Note: The "from" and "to" arguments shou
- `dataminrpulse-related-alerts-get`: Retrieves the alerts related to the provided Alert ID.


## Dataminr Pulse - ReGenAI

**Type:** integration  
**Product:** Dataminr Pulse  
**Commands:**

- `dataminrpulse-watchlists-get`: Retrieves the Watchlists configured on the Dataminr platform.
- `dataminrpulse-alerts-get`: Retrieves the alerts as per the provided watchlist_ids or query or configured watchlist_names parameter in integration.


## DataminrPulseCVSSColor

**Type:** script  
**Product:** Dataminr Pulse  

This dynamic automation parses the CVSS Score of a CVE and presents it in the layout with color


## DataminrPulseCyberDiscoveredEntities

**Type:** script  
**Product:** Dataminr Pulse  

This dynamic automation update the intel agents cyber discovered entities data to HTML and presents it in the layout in color according to theme


## DataminrPulseDisplayRelatedAlerts

**Type:** script  
**Product:** Dataminr Pulse  

## DataminrPulseEPSSScore

**Type:** script  
**Product:** Dataminr Pulse  

This dynamic automation parses the EPSS Score of a CVE and presents it in the layout


## DataminrPulseImpactedAssets

**Type:** script  
**Product:** Dataminr Pulse  

This dynamic automation update the impacted assets data to HTML and presents it in the layout


## DataminrPulseIntelAgents

**Type:** script  
**Product:** Dataminr Pulse  

This dynamic automation update the intel agents data to HTML and presents it in the layout in color according to theme


## DataminrPulseIntelAgentsCyberContext

**Type:** script  
**Product:** Dataminr Pulse  

This dynamic automation update the intel agents cyber context data to HTML and presents it in the layout in color according to theme


## DataminrPulseIntelAgentsPhysicalContext

**Type:** script  
**Product:** Dataminr Pulse  

This dynamic automation update the intel agents physical context data to HTML and presents it in the layout in color according to theme


## DataminrPulseLiveBrief

**Type:** script  
**Product:** Dataminr Pulse  

This dynamic automation update the live brief data to HTML and presents it in the layout in color according to theme


## DataminrPulsePhysicalDiscoveredEntities

**Type:** script  
**Product:** Dataminr Pulse  

This dynamic automation update the intel agents physical discovered entities data to HTML and presents it in the layout in color according to theme


## DataminrPulseShowOnMapWithLatLng

**Type:** script  
**Product:** Dataminr Pulse  

Returns a map entry with a marker on the given coordinates (lat, lng)


## DataminrPulseTransformExtractedIndicatorsToList

**Type:** script  
**Product:** Dataminr Pulse  

Script used to transform result received from the extractIndicators (Builtin) script from the dictionary of indicators to a list of indicators

**Inputs:**

- `ExtractedIndicators`: Response from extractIndicators (Builtin) script.


## DateStringToISOFormat

**Type:** script  
**Product:** Filters And Transformers  

This is a thin wrapper around the dateutil.parser.parse function. It will parse a string containing a date/time stamp and return it in ISO 8601 format

**Inputs:**

- `value`: Date value to convert.
- `dayfirst`: Whether to interpret the first value in an ambiguous 3-integer date (e.g. 01/05/09) as the day (``True``) or month (``False``). If ``yearfir
- `yearfirst`: Whether to interpret the first value in an ambiguous 3-integer date (e.g. 01/05/09) as the year. If ``True``, the first number is taken to b
- `fuzzy`: Whether to allow fuzzy parsing, allowing for string like "Today is January 1, 2047 at 8:21:00AM".
- `add_utc_timezone`: Whether to add UTC timezone to the date string returned in case offset-naive date was provided as input.


## DateTimeNowToEpoch

**Type:** script  
**Product:** Community Common Scripts  

Converts the current datetime to an epoch value for timestamp comparison operations


## DateTimeToADTime

**Type:** script  
**Product:** Community Common Scripts  

Converts unix time to AD Integer8 time. This is used in many AD date fields like pwdLastSet

**Inputs:**

- `days_ago`: Number of days before todays date.


## DateTimeToLDAPTime

**Type:** script  
**Product:** Community Common Scripts  

Converts the given time to a LDAP timestamp

**Inputs:**

- `value`: Date/Time String


## DB2

**Type:** integration  
**Product:** DB2  

Integration to provide connectivity to IBM DB2 using the python ibm_db2 library. This integration was integrated and tested with version 0.1 of DB2

**Commands:**

- `db2-query`: Running a DB2 query command


## DBotAverageScore

**Type:** script  
**Product:** Common Scripts  

The script calculates the average DBot score for each indicator in the context. The script will ignore '0' scores (which are for an 'unknown' reputation). If all scores for an indicator are '0', the indicator will receive a score of '0'. For more information regarding DBot Scores, refer to the official "Reputation and DBot Score" documentation


## DBotClosedIncidentsPercentage

**Type:** script  
**Product:** Common Scripts  

Populates the dashboard pie graph widget with the percentage of incidents closed by DBot vs. incidents closed by analysts


## DBotFindSimilarIncidents

**Type:** script  
**Product:** Base  

Find past similar incidents based on incident fields' similarity. Includes an option to also display indicators similarity. Note: For the similarity calculation, at least one field must be provided in one of the "similarTextField", "similarCategoricalField", or "similarJsonField" arguments

**Inputs:**

- `incidentId`: Incident ID to get the prediction of. If empty, predicts the the current incident ID.
- `similarTextField`: Comma-separated list of incident text fields to take into account when computing similarity. For example: commandline, URL. Note: In order t
- `similarCategoricalField`: Comma-separated list of incident categorical fields to take into account whe computing similarity. For example: IP, URL. Note: In order to c
- `similarJsonField`: Comma-separated list of incident JSON fields to take into account whe computing similarity. For example: CustomFields. Note: In order to cal
- `fieldsToDisplay`: Comma-separated list of additional incident fields to display, but which will not be taken into account when computing similarity.
- `fieldExactMatch`: Comma-separated list of incident fields that have to be equal to the current incident fields. This helps reduce the query size. These fields
- `useAllFields`: Whether to use a predefined set of fields and custom fields to compute similarity. If "True", it will ignore values in similarTextField, sim
- `fromDate`: The start date by which to filter incidents. Date format will be the same as in the incidents query page, for example, "3 days ago", ""2019-


## DBotFindSimilarIncidentsByIndicators

**Type:** script  
**Product:** Base  

Finds similar incidents based on indicators' similarity. Indicators' contribution to the final score is based on their scarcity

**Inputs:**

- `incidentId`: Incident ID to get the prediction of. If empty, predicts the current incident ID.
- `maxIncidentsInIndicatorsForWhiteList`: The maximum number of incidents that an indicator can be associated with to be retained. This helps to filter out indicators that appear in 
- `minNumberOfIndicators`: The minimum number of indicators related to the incident required before running the model.
- `threshold`: Threshold to similarity value which is between 0 and 1.
- `indicatorsTypes`: Type of indicators to take into account. If empty, uses all indicators types.
- `showActualIncident`: Whether to show the incident you are investigating.
- `maxIncidentsToDisplay`: The maximum number of incidents to display.
- `fieldsIncidentToDisplay`: Fields to add in the table of incident


## DBotPredictIncidentsBatch

**Type:** script  
**Product:** Machine Learning  

Apply a trained ML model on multiple incidents at once, to compare incidents how the incidents were labeled by analysts, to the predictions of the model. This script is aimed to help evaluate a trained model using past incidents

**Inputs:**

- `query`: Additional text by which to query incidents.
- `incidentTypes`: A comma-separated list of incident types by which to filter.
- `fromDate`: The start date by which to filter incidents. Date format will be the same as in the incidents query page (valid strings exaple: "3 days ago"
- `toDate`: The end date by which to filter incidents. Date format will be the same as in the incidents query page (valid strings exaple: "3 days ago", 
- `limit`: The maximum number of incidents to fetch.
- `tagField`: The field name with the label. Supports a comma-separated list, the first non-empty value will be taken.
- `hashSeed`: If non-empty, hash every word with this seed.
- `phishingLabels`: A comma-separated list of email tags values and mapping. The script considers only the tags specified in this field. You can map a label to 


## DBotPredictOutOfTheBoxV2

**Type:** script  
**Product:** Machine Learning  

Predict phishing incidents using the out-of-the-box pre-trained model

**Inputs:**

- `emailSubject`: Subject of the email.
- `emailBody`: Body of the email.
- `emailBodyHTML`: HTML body of the email. Only use this field if the emailBody argument is empty.
- `topWordsLimit`: Maximum number of positive/negative words to return for the model decision.
- `wordThreshold`: Threshold to determine word importance (range 0-1). Default is 0.05.
- `minTextLength`: Minimum number of characters for the prediction.
- `labelProbabilityThreshold`: The label probability threshold. Default is 0.
- `confidenceThreshold`: The confidence threshold. The model will provide predictions only if their confidence is above this threshold.


## DBotPreProcessTextData

**Type:** script  
**Product:** Base  

Pre-process text data for the machine learning text classifier

**Inputs:**

- `input`: The input file entry ID or the file content (as a string).
- `removeShortTextThreshold`: Sample text for which the total number words are less than or equal to this number will be ignored.
- `dedupThreshold`: Remove emails with similarity greater than this threshold, range 0-1, where 1 is completly identical.
- `textFields`: A comma-separated list of incident field names with the text to process. You can also use "|" if you want to choose the first non-empty valu
- `inputType`: The input type.
- `preProcessType`: Text pre-processing type. The default is "json".
- `cleanHTML`: Whether to remove HTML tags. Default is "true".
- `whitelistFields`: A comma-separate list of fields inside the JSON by which to filter.


## DBotShowClusteringModelInfo

**Type:** script  
**Product:** Base  

Show clustering model information - model summary and incidents in specific cluster

**Inputs:**

- `modelName`: The model name.
- `searchQuery`: The input query from the dashboard.
- `fromDate`: The start date by which to filter incidents. Date format will be the same as in the incidents query page, for example: "3 days ago", ""2019-
- `fieldsToDisplay`: Comma-separated list of additional incident fields to display, but which will not be taken into account when computing similarity.
- `returnType`: Return model summary or incidents in specific group according to the search query.


## DBotTrainClustering

**Type:** script  
**Product:** Base  

This script helps organizes and groups incidents based on their similarities using clustering algorithms. Clustering is a technique used to group data points (in this case, incidents) that are similar to each other into clusters. Used to automatically categorize a large number of incidents into meaningful groups

**Inputs:**

- `fieldsForClustering`: Comma-separated list of incident fields to take into account when training the clustering.
- `fieldForClusterName`: Incident field that represents the family name for each cluster created. The model determines how many incidents in the cluster have the sam
- `fromDate`: The start date by which to filter incidents. Date format will be the same as in the incidents query page, for example, "3 days ago", ""2019-
- `toDate`: The end date by which to filter incidents. Date format will be the same as in the incidents query page, for example, "3 days ago", ""2019-01
- `limit`: The maximum number of incidents to query.
- `query`: Argument for the query.
- `minNumberofIncidentPerCluster`: Minimum number of incidents a cluster should contain for it to be retained.
- `modelName`: Name of the model.


## DBotTrainTextClassifierV2

**Type:** script  
**Product:** Base  

Train a machine learning text classifier

**Inputs:**

- `input`: The input file entry ID or JSON string.
- `modelName`: The model name to store in the system.
- `storeModel`: Whether to store the model in the system.
- `overrideExistingModel`: Whether to override the existing model if a model with the same name exists. Default is "false".
- `targetAccuracy`: The target accuracy, between 0 and 1. Default is 0.8.
- `maxBelowThreshold`: Maximum nubmer of samples below the threshold (for the target accuracy).
- `tagField`: The field name with the label. Supports a comma-separated list, the first non-empty value will be taken.
- `textField`: The field name with the text to train.


## DeCYFIR

**Type:** integration  
**Product:** DeCYFIR  

DeCYFIR API's provides External Threat Landscape Management insights. This integration was integrated and tested with version v2 of decyfir

**Commands:**

- `decyfir-takedown-initiate`: Initiate a take down request.
- `decyfir-takedown-list`: Get take down list.


## DeCYFIR - v1

**Type:** playbook  
**Product:** DeCYFIR  

DeCYFIR API's provides External Threat Landscape Management insights


## Deep Instinct

**Type:** integration  
**Product:** DeepInstinct  
**Commands:**

- `deepinstinct-get-device`: get specific device by ID
- `deepinstinct-get-events`: Get all events. Max events in response can be 50, use first_event_id parameter to define first event id to get
- `deepinstinct-get-all-groups`: get all groups
- `deepinstinct-get-all-policies`: get all policies
- `deepinstinct-add-hash-to-blacklist`: add file hash to block list
- `deepinstinct-add-hash-to-whitelist`: add file hash to allow list
- `deepinstinct-remove-hash-from-blacklist`: remove file hash from block list
- `deepinstinct-remove-hash-from-whitelist`: remove file hash from allow list
- `deepinstinct-add-devices-to-group`: add multiple devices to group
- `deepinstinct-remove-devices-from-group`: remove list of devices from group
- `deepinstinct-delete-files-remotely`: delete multiple files remotely
- `deepinstinct-terminate-processes`: terminate list of processes
- `deepinstinct-close-events`: close list of events


## DeepInstinct v3

**Type:** integration  
**Product:** DeepInstinct  

Deep Instinct is a prevention-first approach to stopping ransomware and other malware using the world's first purpose-built, deep learning cybersecurity framework. This integration was integrated and tested with version 3.3.x of DeepInstinct v3

**Commands:**

- `deepinstinctv3-get-device`: Get device information from its ID
- `deepinstinctv3-get-events`: Get all events after given event ID
- `deepinstinctv3-get-suspicious-events`: Get all suspicious events after given event ID
- `deepinstinctv3-get-all-groups`: Get all groups
- `deepinstinctv3-get-all-policies`: Get list of all policies
- `deepinstinctv3-add-hash-to-deny-list`: Add file hash to Deny List
- `deepinstinctv3-add-hash-to-allow-list`: Add file hash to Allow List
- `deepinstinctv3-remove-hash-from-deny-list`: Remove hash from Deny List
- `deepinstinctv3-remove-hash-from-allow-list`: Remove hash from Allow List
- `deepinstinctv3-add-devices-to-group`: Add multiple devices to a group
- `deepinstinctv3-remove-devices-from-group`: Remove list of devices from groups
- `deepinstinctv3-delete-files-remotely`: Delete multiple files remotely
- `deepinstinctv3-terminate-processes`: Terminate list of processes
- `deepinstinctv3-close-events`: Close list of events
- `deepinstinctv3-disable-device`: Disable device at next check-in


## DeepL

**Type:** integration  
**Product:** DeepL  

This integration uses DeepL ( to translate text or files This integration was integrated and tested with DeepL

**Commands:**

- `deepl-usage`: Get current API key usage
- `deepl-translate-text`: Translates input text
- `deepl-submit-document`: Please note that with every submitted document of type .pptx, .docx or .pdf you are billed a minimum of 50'000 characters with the DeepL API plan, no matter how
- `deepl-check-document-status`: The status of the document translation process can be checked by sending a status request to the document specific status URL.
- `deepl-get-document`: Get the translated document


## Defang

**Type:** script  
**Product:** Community Common Scripts  

Defangs IP, Mail and URL address to prevent them from being recognized

**Inputs:**

- `input`: The input to be defanged.
- `defang_options`: Specify which IOC needs defanging.
- `mail_options`: Mail defang can be configured to merely defang . or @ or both.
- `url_options`: URL defang can be configured to merely defang . or https or :// or all.


## Default

**Type:** playbook  
**Product:** Default  

This playbook executes when no other playbook is associated with an incident. It enriches indicators in an incident using one or more integrations

**Inputs:**

- `Enrich`: Determines whether to enrich all indicators in the incident.
- `OnCall`: Set to true to assign only user that is currently on shift. Requires the platform.5 or later.


## DeHashed

**Type:** integration  
**Product:** DeHashed  

This integration allows you to check if your personal information such as your email, username, or password is being compromised

**Commands:**

- `dehashed-search`: Performs a search to check if information is compromised.
- `email`: Checks if an email address was compromised.


## Delete Custom Content

**Type:** playbook  
**Product:** platform CI/CD  

This playbook deletes custom content from the system. It deletes Playbooks, Scripts, Layouts, Classifiers, Mappers, Incident Types and Incident Fields

**Inputs:**

- `dry_run`: If true, will not actually delete any content entities.
- `instance_name`: Core REST API instance name to use.


## DelineaDSV

**Type:** integration  
**Product:** Delinea DevOps Secrets Vault  

Manage credentials for applications, databases, CI/CD tools, and services without causing friction in the development process. This integration was integrated and tested with version 1.37.0 of DelineaDSV

**Commands:**

- `dsv-secret-get`: Getting a secret fom DSV


## DelineaSS

**Type:** integration  
**Product:** Delinea Secret Server  

Secret Server and Platform is the fully featured Privileged Account Management (PAM) solution available both on premise and in the cloud. It empowers security and IT ops teams to secure and manage all types of privileged accounts and offers the fastest time to value of any PAM solution. This integration was integrated and tested with version 5.0 of Delinea

**Commands:**

- `delinea-secret-password-get`: Retrieved password from secret
- `delinea-secret-username-get`: Retrieved username from secret
- `delinea-secret-search-name`: Search ID secret by field name
- `delinea-secret-password-update`: Update password for secret
- `delinea-secret-checkout`: Check Out a secret
- `delinea-secret-checkin`: Check In a secret
- `delinea-folder-create`: Create a new secret folder
- `delinea-folder-search`: Search folder by name folder
- `delinea-secret-get`: Get secret object by ID secret
- `delinea-secret-search`: Search secret ID by multiply params
- `delinea-folder-update`: Update a single secret folder by ID
- `delinea-secret-create`: Create new object Secret
- `delinea-secret-delete`: Delete secret
- `delinea-secret-server-user-create`: Create a new Secret Server user
- `delinea-secret-server-user-search`: Search, filter, sort, and page Secret Server users


## Departing Employee Auto-Add

**Type:** playbook  
**Product:** Code42  

Queries stand-down tickets from a ticketing system and passes relevant employee data to the Add Employees to Departing Employee Watchlist playbook


## Departing Employee Clean-Up

**Type:** playbook  
**Product:** Code42  

Queries the Departing Employee watchlist in Code42 Incydr and passes relevant employee data to the Remove Employees from Departing Employee Watchlist playbook


## Detections Assessment - Vectra XDR

**Type:** playbook  
**Product:** Vectra XDR  

This playbook conducts a detection assessment and saves the result in context data

**Inputs:**

- `detection_id`: ID of the Detection.
- `detection_name`: Name of the Detection.


## Detonate File - ANYRUN

**Type:** playbook  
**Product:** ANY.RUN  

Detonates one or more files using the ANYRUN sandbox integration. Returns relevant reports to the War Room and file reputations to the context data. All file types are supported

**Inputs:**

- `File`: The file object of the file to detonate. The file is taken from the context.
- `Interval`: The duration for executing the pooling (in minutes).
- `Timeout`: The duration after which to stop pooling and to resume the playbook (in minutes).


## Detonate File - BitDam

**Type:** playbook  
**Product:** BitDam  

Detonates one or more files using BitDam integration. Returns verdict to the War Room and file reputations to the context data. Supported file types are mainly PDF & microsoft office software

**Inputs:**

- `File`: The file object of the file to detonate. The File is taken from the context.
- `Interval`: The duration for executing the pooling (in minutes).
- `Timeout`: The duration after which to stop pooling and to resume the playbook (in minutes).


## Detonate File - Cuckoo

**Type:** playbook  
**Product:** Cuckoo Sandbox  

Detonates a file with Cuckoo

**Inputs:**

- `File`: The file to detonate.
- `interval`: How often to poll for results.
- `timeout`: How long to wait before giving up waiting for results.


## Detonate File - FireEye AX

**Type:** playbook  
**Product:** FireEye (AX Series)  

Detonates one or more files using the FireEye AX integration. This playbook returns relevant reports to the War Room and file reputations to the context data. The detonation supports the following file types - PE32, EXE, DLL, JAR, JS, PDF, DOC, DOCX, RTF, XLS, PPT, PPTX, XML, ZIP, VBN, SEP, XZ, GZ, BZ2, TAR, MHTML, SWF, LNK, URL, MSI, JTD, JTT, JTDC, JTTC, HWP, HWT, HWPX, BAT, HTA, PS1, VBS, WSF, JSE, VBE, CHM

**Inputs:**

- `File`: The file object of the file to detonate.
- `Interval`: The polling frequency. How often the polling command should run (in minutes).
- `Timeout`: The time to wait before a timeout occurs (in minutes).


## Detonate File - Group-IB TDS Polygon

**Type:** playbook  
**Product:** Polygon  

Detonate file using Group-IB THF Polygon integration. This playbook returns relevant reports to the War Room and file reputations to the context data. The detonation supports the following file types: 7z, ace, ar, arj, bat, bz2, cab, chm, cmd, com, cpgz, cpl, csv, dat, doc, docm, docx, dot, dotm, dotx, eml, exe, gz, gzip, hta, htm, html, iqy, iso, jar, js, jse, lnk, lz, lzma, lzo, lzh, mcl, mht, msg, msi, msp, odp, ods, odt, ots, ott, pdf, pif, potm, potx, pps, ppsm, ppsx, ppt, pptm, pptx, ps1, pub, py, pyc, r, rar, reg, rtf, scr, settingcontent-ms, stc, svg, sxc, sxw, tar, taz, .tb2, .tbz, .tbz2, tgz, tlz, txz, tzo, txt, url, uue, vbe, vbs, wsf, xar, xls, xlsb, xlsm, xlsx, xml, xz, z, zip

**Inputs:**

- `file_id`: File EntryID to detonate
- `Interval`: Report requests frequency (minutes).
- `Timeout`: Report waiting timeout (minutes).
- `Password`: Password for the uploaded file.


## Detonate File - JoeSecurity

**Type:** playbook  
**Product:** Joe Security  

Detonates one or more files using the Joe Security - Joe Sandbox integration. Returns relevant reports to the War Room and file reputations to the context data. All file types are supported

**Inputs:**

- `File`: The file object of the file to detonate. The file is taken from the context.
- `Interval`: The duration for executing the pooling (in minutes).
- `Timeout`: The duration after which to stop pooling and to resume the playbook (in minutes).
- `Systems`: The operating system to run the analysis on (comma-separated). Supported values are: w7, w7x64, w7_1, w7_2, w7native, android2, android3, ma
- `Comments`: The comments for the analysis.
- `InternetAccess`: Whether to enable internet access (boolean). The default is "True". "True" means there is internet access. "False" means there is no interne
- `ReportFileType`: The resource type to download. The default is "HTML". The supported values are: html, lighthtml, executive, pdf, classhtml, xml, lightxml, c


## Detonate File - JoeSecurity V2

**Type:** playbook  
**Product:** Joe Security  

The Detonate File using Joe Sandbox Process is designed to streamline and enhance the security assessment of files. This automated system accepts a user-submitted file, sends it for in-depth analysis using Joe Sandbox technology, and returns comprehensive results as attachments to the user. The process is designed to be swift, efficient, and secure, providing users with valuable insights into potential threats and vulnerabilities within their files

**Inputs:**

- `File`: File object of the file to detonate. The File is taken from the context.
- `Timeout`: The default duration after which to stop polling and to resume the playbook (in seconds).
- `Systems`: Operating system to run the analysis on (comma-separated). Supported values are: w7, w7x64, w7_1, w7_2, w7native, android2, android3, mac1, 
- `Comments`: Comments for the analysis.
- `ReportFileType`: The resource type to download. Default is html. Supported values are: html, lighthtml, executive, pdf, classhtml, xml, lightxml, classxml, c


## Detonate File - Lastline

**Type:** playbook  
**Product:** Lastline  

Detonates a File using the Lastline sandbox. Lastline supports the following File Types: EXE, SYS, DLL, COM, SCR, CPL, OCX, CGI, DOC, DOTM, DOCX, DOTX, XLS, PPAM, XSLX, PPS, XLSB, PPSX, XLSM, PPSM, PPT, PPTX, PPTM, RTF, SHS, XLTM, SLDM, XLTX, SLDX, XLAM, THMX, DOCM, XAR, JTD, JTDC, PDF, SWF, GZ, 7Z, TGZ, MSI, ZIP, LZH, CAB, LZMA, APK, JAR, CLASS, JPEG, PNG, GIF, CMD, ACE, BAT, ARJ, VBS, CHM, XML, LNK, URL, MOF, HTM, OCX, HTML, POTM, EML, POTX, MSG, PS, |VB, REG, VBA, WSC, VBE, WSF, VBS, WSH

**Inputs:**

- `File`: The file to detonate. The file is taken from the context.
- `Interval`: The polling frequency. How often the polling command should run (in minutes).
- `Timeout`: How much time to wait before a timeout occurs (in minutes).


## Detonate File - Lastline v2

**Type:** playbook  
**Product:** Lastline  

Detonates a file using the Lastline sandbox. Lastline supports the following File Types: EXE, SYS, DLL, COM, SCR, CPL, OCX, CGI, DOC, DOTM, DOCX, DOTX, XLS, PPAM, XSLX, PPS, XLSB, PPSX, XLSM, PPSM, PPT, PPTX, PPTM, RTF, SHS, XLTM, SLDM, XLTX, SLDX, XLAM, THMX, DOCM, XAR, JTD, JTDC, PDF, SWF, GZ, 7Z, TGZ, MSI, ZIP, LZH, CAB, LZMA, APK, JAR, CLASS, JPEG, PNG, GIF, CMD, ACE, BAT, ARJ, VBS, CHM, XML, LNK, URL, MOF, HTM, OCX, HTML, POTM, EML, POTX, MSG, PS, |VB, REG, VBA, WSC, VBE, WSF, VBS, WSH

**Inputs:**

- `File`: The file to detonate. The file is taken from the context.
- `Interval`: The polling frequency. How often the polling command should run (in minutes).
- `Timeout`: The amount of time to wait before a timeout occurs (in minutes).


## Detonate File - OrionMalware

**Type:** playbook  
**Product:** OrionMalware  

Detonate a file through OrionMalware

**Inputs:**

- `file_entryid`: File entryID


## Detonate File - ReversingLabs A1000

**Type:** playbook  
**Product:** ReversingLabs A1000  

Upload sample to ReversingLabs A1000 appliance and automatically retrieve full & classification reports. Calculate final classification

**Inputs:**

- `EntryID`: The Entry ID.


## Detonate File - ReversingLabs TitaniumScale

**Type:** playbook  
**Product:** ReversingLabs TitaniumScale  

Upload sample to ReversingLabs TitaniumScale instance and retrieve the analysis report

**Inputs:**

- `EntryID`: The Entry ID.


## Detonate File - SecneurX Analysis

**Type:** playbook  
**Product:** SecneurX Analysis  

Detonates a file using the SecneurX Analysis Integration. Returns relevant reports to the War Room and file reputations to the context data

**Inputs:**

- `File`: File object of the file to detonate. The File is taken from the context.
- `Platform`: Operating system platform to run the analysis on. Supported values are: ["Windows7", "Windows10", "Android", "Ubuntu"].
- `Duration`: Analysis duration in seconds.
- `Priority`: Analysis priority. Possible values are "High" or "Normal".
- `Extension`: Extension of the submitted file. Supported values are: ["sh", "js", "7z", "py", "doc", "rtf", "xls", "ppt", "pps", "ps1", "bat", "eml", "exe
- `Reboot`: Reboot the system during analysis. The value should be "True" or "False".
- `FilePassword`: Password of the submitted file.
- `ReportFormat`: The resource type to download. Supported values are: ["json", "html"].


## Detonate File - ThreatGrid

**Type:** playbook  
**Product:** Cisco Secure Malware Analytics  

Detonates one or more files using the ThreatGrid integration. This playbook returns relevant reports to the War Room and file reputations to the context data. The detonation supports the following file types: EXE, DLL, JAR, JS, PDF, DOC, DOCX, RTF, XLS, PPT, PPTX, XML, ZIP, VBN, SEP, XZ, GZ, BZ2, TAR, MHTML, SWF, LNK, URL, MSI, JTD, JTT, JTDC, JTTC, HWP, HWT, HWPX, BAT, HTA, PS1, VBS, WSF, JSE, VBE, CHM

**Inputs:**

- `File`: The file object of the file to detonate.
- `FileName`: The name of the file to detonate.
- `VM`: The VM to use (string).
- `playbook`: The name of the Threat Grid playbook to apply to this sample run.
- `Private`: The sample is marked private if this is present, and set to any value other than false.
- `Source`: The string used for identifying the source of the detonation (user defined).
- `Tags`: The comma-separated list of tags applied to this sample.
- `Interval`: The polling frequency. How often the polling command should run (in minutes).


## Detonate File - ThreatGrid v2

**Type:** playbook  
**Product:** Cisco Secure Malware Analytics  

Detonate one or more files using the ThreatGrid integration. This playbook returns relevant reports to the War Room and file reputations to the context data. The detonation supports the following file types - EXE, DLL, JAR, JS, PDF, DOC, DOCX, RTF, XLS, PPT, PPTX, XML, ZIP, VBN, SEP, XZ, GZ, BZ2, TAR, MHTML, SWF, LNK, URL, MSI, JTD, JTT, JTDC, JTTC, HWP, HWT, HWPX, BAT, HTA, PS1, VBS, WSF, JSE, VBE, CHM

**Inputs:**

- `File`: File object of the file to detonate.


## Detonate File - Trend Micro Deep Discovery Analyzer Beta

**Type:** playbook  
**Product:** TrendAI™ Deep Discovery™ Analyzer  

Detonates a File using the TrendAI™ Deep Discovery™ Analyzer sandbox. Deep Discovery Analyzer(version 6.0.0) supports the following File Types: bat, cell, chm, class, cmd, dll, doc, docx, exe, gul, hta, htm, html, hwp, hwpx, jar, js, jse, jtd, lnk, mov, pdf, ppt, pptx, ps1, pub, rtf, slk, svg, swf, vbe, vbs, wsf, xls, xlsx, xml

**Inputs:**

- `File`: The file to detonate. File is taken from the context.
- `interval`: Polling frequency - how often the polling command should run (minutes)
- `timeout`: How much time to wait before a timeout occurs (minutes)


## Detonate File - VMRay

**Type:** playbook  
**Product:** VMRay Analyzer  

Detonates a file with VMRay

**Inputs:**

- `File`: The file to detonate.
- `interval`: The frequency in which to poll for results (minutes).
- `timeout`: The amount of time to wait before giving up waiting for results (minutes).
- `document_password`: The password if the file is a password-protected document.
- `archive_password`: The password if the file is a password-protected archive.
- `sample_type`: The sample type.
- `shareable`: Whether to make the file shareable.
- `max_jobs`: The maximum jobs to create in VMRay.


## Detonate File From URL - ANYRUN

**Type:** playbook  
**Product:** ANY.RUN  

Detonates one or more remote files using the ANYRUN sandbox integration. Returns relevant reports to the War Room and file reputations to the context data. This type of analysis works only for direct download links

**Inputs:**

- `URL`: The URL of the web file to detonate.
- `Interval`: The duration for executing the pooling (in minutes).
- `Timeout`: The duration after which to stop pooling and to resume the playbook (in minutes).


## Detonate File From URL - JoeSecurity

**Type:** playbook  
**Product:** Joe Security  

Detonates one or more remote files using the Joe Security sandbox integration. Returns relevant reports to the War Room and file reputations to the context data. This type of analysis is available for Windows only and works only for direct download links

**Inputs:**

- `FileURL`: The URL of the web file to detonate. The FileUrl is taken from the context.
- `Interval`: The duration for executing the pooling (in minutes).
- `Timeout`: The duration after which to stop pooling and to resume the playbook (in minutes).
- `Systems`: The operating system to run the analysis on (comma-separated). Supported values are: w7, w7x64, w7_1, w7_2, w7native, android2, android3, ma
- `Comments`: The comments for the analysis.
- `InternetAccess`: Whether internet access is enabled (boolean). The default is "True". "True" means there is internet access. False means there is no internet
- `ReportFileType`: The resource type to download. The default is "html". The spported values are, "html", "lighthtml", "executive", "pdf", "classhtml", "xml", 


## Detonate URL - ANYRUN

**Type:** playbook  
**Product:** ANY.RUN  

Detonates one or more URLs using the ANYRUN sandbox integration. Returns relevant reports to the War Room and URL reputations to the context data

**Inputs:**

- `URL`: The URL to detonate.
- `Interval`: The duration for executing the pooling (in minutes).
- `Timeout`: The duration after which to stop pooling and to resume the playbook (in minutes).


## Detonate URL - Cuckoo

**Type:** playbook  
**Product:** Cuckoo Sandbox  

Detonates a URL with Cuckoo

**Inputs:**

- `URL`: The URL to detonate.
- `interval`: How often to poll for results.
- `timeout`: How long to wait before giving up waiting for results.


## Detonate URL - FireEye AX

**Type:** playbook  
**Product:** FireEye (AX Series)  

Detonating URL with FireEye AX

**Inputs:**

- `URL`: URL to detonate
- `interval`: How often to poll for results.
- `timeout`: How long to wait before giving up waiting for results.
- `Info_Level`: This parameter specifies the level of information to be returned in the URL submission report. Information levels include concise (default),


## Detonate URL - Group-IB TDS Polygon

**Type:** playbook  
**Product:** Polygon  

Detonates one or more files using the Polygon integration. This playbook returns relevant reports to the War Room and file reputations to the context data

**Inputs:**

- `url`: The url object to detonate. The URL is taken from the context.
- `Interval`: The duration for executing the pooling (in minutes).
- `Timeout`: The duration after which to stop pooling and to resume the playbook (in minutes).


## Detonate URL - Hatching Triage

**Type:** playbook  
**Product:** Hatching Triage  

Detonating URL with Hatching Triage

**Inputs:**

- `URL`: URL to detonate.
- `interval`: How often to poll for results.
- `timeout`: How long to wait before giving up waiting for results.


## Detonate URL - Lastline

**Type:** playbook  
**Product:** Lastline  

Detonates a URL using the Lastline Sandbox integration

**Inputs:**

- `URL`: The URL to detonate.
- `Interval`: The polling frequency. How often the polling command should run (in minutes).
- `Timeout`: How much time to wait before a timeout occurs (in minutes).


## Detonate URL - Lastline v2

**Type:** playbook  
**Product:** Lastline  

Detonates a URL using the Lastline Sandbox integration

**Inputs:**

- `URL`: The URL to detonate.
- `Interval`: The polling frequency. How often the polling command should run (in minutes).
- `Timeout`: The amount of time to wait before a timeout occurs (in minutes).


## Detonate URL - SecneurX Analysis

**Type:** playbook  
**Product:** SecneurX Analysis  

Detonates a URL using the SecneurX Analysis integration. Returns relevant reports to the War Room and file reputations to the context data

**Inputs:**

- `URL`: URL to detonate.
- `Priority`: Analysis priority. Possible values are "High" or "Normal".
- `Duration`: Analysis duration in seconds.
- `Reboot`: Reboot the system during analysis. The value should be "True" or "False".
- `ReportFormat`: The resource type to download. Supported values are: ["json", "html"].
- `PollingInterval`: Duration for executing the pooling (in minutes).
- `Timeout`: The duration after which to stop pooling and to resume the playbook (in minutes).


## Detonate URL - ThreatGrid

**Type:** playbook  
**Product:** Cisco Secure Malware Analytics  

Detonates one or more URLs using the ThreatGrid integration. This playbook returns relevant reports to the War Room and URL reputations to the context data

**Inputs:**

- `URL`: The URL of the sites to detonate.
- `FileName`: The name of the file to detonate.
- `VM`: The VM to use (string).
- `Playbook`: The name of the Threat Grid playbook to apply to this sample run.
- `Private`: The sample is marked private if this is present. If it is set to any other value then it will not be private.
- `Source`: The string used for identifying the source of the detonation (user defined).
- `Tags`: A comma-separated list of tags applied to the sample.
- `Interval`: The polling frequency. How often the polling command should run (in minutes).


## Detonate URL - ThreatGrid v2

**Type:** playbook  
**Product:** Cisco Secure Malware Analytics  

Detonate one or more URLs using the ThreatGrid integration

**Inputs:**

- `URL`: URL of the sites to detonate.
- `timeout`: Indicates the time in seconds until the polling sequence times out. Default is 60.
- `interval`: Indicates the time in seconds to wait between command execution when 'polling' argument is true. Minimum value is 10 seconds. Default is 10.


## Detonate URL - Trend Micro Deep Discovery Analyzer Beta

**Type:** playbook  
**Product:** TrendAI™ Deep Discovery™ Analyzer  

Detonates a URL using the TrendAI™ Deep Discovery™ Analyzer sandbox

**Inputs:**

- `URL`: URL to detonate.
- `interval`: Polling frequency - how often the polling command should run (minutes)
- `timeput`: How much time to wait before a timeout occurs (minutes)


## Detonate URL - VMRay

**Type:** playbook  
**Product:** VMRay Analyzer  

Detonates a URL using the VMRay sandbox integration

**Inputs:**

- `URL`: The URL to detonate.
- `interval`: How often to poll for results (minutes).
- `timeout`: How long to wait before giving up waiting for results (minutes).


## Devo v2

**Type:** integration  
**Product:** Devo  
**Commands:**

- `devo-run-query`: Queries Devo based on the specified LINQ query.
- `devo-get-alerts`: Queries alerts in the specified timeframe.
- `devo-multi-table-query`: Queries multiple tables for a given token and returns relevant results.
- `devo-write-to-table`: Writes records to a specified Devo table.
- `devo-write-to-lookup-table`: Writes lookup table entry records to a specified Devo table.


## DFIRe

**Type:** integration  
**Product:** DFIRe  

DFIRe is a self-hosted Digital Forensics and Incident Response (DFIR) case management platform built for security professionals. It provides structured case management, evidence tracking with chain of custody, IOC indicator management, and incident response workflows aligned with the NIST Incident Response framework — all running on your own infrastructure with AES-256 encryption. This integration connects Cortex XSIAM and the platform, enabling automated case creation and updates, bi-directional IOC indicator synchronization, evidence item tracking, file attachment uploads, and timeline enrichment directly from playbooks

**Commands:**

- `dfire-search`: Searches across all DFIRe data (cases, indicators, notes, items). Supports AND, OR, NOT operators.
- `dfire-case-type-list`: Lists available case types and their IDs.
- `dfire-case-list`: Lists cases from DFIRe.
- `dfire-case-get`: Retrieves details of a specific case.
- `dfire-case-create`: Creates a new case in DFIRe.
- `dfire-case-update`: Updates an existing case in DFIRe.
- `dfire-case-delete`: Deletes a case from DFIRe.
- `dfire-case-note-list`: Lists notes for a case.
- `dfire-case-note-create`: Creates a note on a case.
- `dfire-indicator-list`: Lists indicators from the global IOC registry.
- `dfire-indicator-get`: Retrieves details of a specific indicator.
- `dfire-indicator-create`: Creates a new indicator in the global IOC registry.
- `dfire-indicator-update`: Updates an existing indicator.
- `dfire-indicator-delete`: Deletes an indicator from the global IOC registry.
- `dfire-item-type-list`: Lists available evidence item types and their IDs.


## Dig

**Type:** script  
**Product:** Common Scripts  

DNS lookup utility to provide 'A' and 'PTR' record

**Inputs:**

- `server`: The IP address or hostname of the name server to query. The default value will be taken from /etc/resolv.conf e.g. 8.8.8.8
- `name`: Name of the resource record to look up e.g. paloaltonetworks.com. For reverser lookup, provide IP address
- `reverseLookup`: Perform reverse lookup


## Digital Defense FrontlineVM

**Type:** integration  
**Product:** Digital Defense Frontline VM  

Use the Digital Defense Frontline VM to identify and evaluate the security and business risks of network devices and applications deployed as premise, cloud, or hybrid network-based implementations. This integration was integrated and tested with version 6.2.4 of Digital Defense FrontlineVM

**Commands:**

- `frontline-get-assets`: Retrieves the asset's information from Frontline VM.
- `frontline-scan-asset`: Performs a scan on the specified asset.


## Digital Defense FrontlineVM - Old Vulnerabilities Found

**Type:** playbook  
**Product:** Digital Defense Frontline VM  

This will query Frontline.Cloud's active view for any critical level vulnerabilities found to be older than 90 days

**Inputs:**

- `Days Older Than`: The inputed number of days from now in which to search if vulnerabilities exist.


## Digital Defense FrontlineVM - PAN-OS block assets

**Type:** playbook  
**Product:** Digital Defense Frontline VM  

Pulls Panorama queried threat logs and check for any correlating assets that are found to have a minimum of high level vulnerabilities. If so, it will block the the IP using Panorama's PAN-OS - Block IP and URL - External Dynamic List playbook


## Digital Guardian

**Type:** integration  
**Product:** Digital Guardian  

This integration was integrated and tested with version 2.11.0 of Digital Guardian ARC

**Commands:**

- `digitalguardian-add-watchlist-entry`: Add Watchlist Entry
- `digitalguardian-check-watchlist-entry`: Check Watchlist Entry
- `digitalguardian-remove-watchlist-entry`: Remove Watchlist Entry
- `digitalguardian-add-componentlist-entry`: Add Componentlist Entry
- `digitalguardian-check-componentlist-entry`: Check Componentlist Entry
- `digitalguardian-remove-componentlist-entry`: Remove Componentlist Entry


## Digital Guardian Demo Playbook

**Type:** playbook  
**Product:** Digital Guardian  

This playbook will show how to handle an exfiltration event through Digital Guardian by emailing a user's manager and adding the user to a DG Watchlist

**Inputs:**

- `User Name`: User Name to check
- `Watchlist Name`: The name of the DG watchlist to add the user to.
- `Incident Match`: The incident name should contain this string in order for the playbook to handle the event. The default is DLP1008 which is a USB Exfiltrati
- `Notify Manager`: Notify User's Manager


## disable-user

**Type:** script  
**Product:** Aggregated Scripts  

This script disables users for multiple services

**Inputs:**

- `user_id`: List of users IDs of the users to disable. At least one of "user_id", "user_name" or "user_email" is required.
- `user_name`: List of names of the users to disable. At least one of "user_id", "user_name" or "user_email" is required.
- `user_email`: List of emails of the users to disable. At least one of "user_id", "user_name" or "user_email" is required.
- `brands`: List of brands to disable users from.
- `verbose`: Whether to fetch a human-readable entry for each command or just the final result. If set to true, all commands will have human-readable ent


## DisableUserWrapper

**Type:** script  
**Product:** Common Scripts  

This script allows disabling a specified user using one or more of the following integrations: SailPointIdentityIQ, ActiveDirectoryQuery, Okta, MicrosoftGraphUser, and IAM

**Inputs:**

- `username`: The username of the user to disable.
- `approve_action`: Whether to run the command. This is used to prevent unwanted calls to the command.


## Discord

**Type:** integration  
**Product:** Discord  

This is the Discord integration for sending Messages from platform to Discord server made by Trustnet

**Commands:**

- `discord-send-message`: Send message to your channel
- `discord-get-message`: Get message details


## DNSOverHttps

**Type:** integration  
**Product:** DNSOverHttps  

Query dns names over https from Cloudflare or Google

**Commands:**

- `doh-resolve`: Resolve a name to IP over HTTPS


## Docker Engine API

**Type:** integration  
**Product:** DevSecOps  

The Engine API is an HTTP API served by Docker Engine. It is the API the Docker client uses to communicate with the Engine, so everything the Docker client can do can be done with the API. This integration was integrated and tested with version 20.10.17 (API Version 1.41) of Docker Engine API

**Commands:**

- `docker-build-prune`: Delete builder cache
- `docker-config-create`: Create a config
- `docker-config-inspect`: Inspect a config
- `docker-config-list`: List configs
- `docker-container-changes`: Get changes on a container’s filesystem
- `docker-container-create`: Create a container
- `docker-container-delete`: Remove a container
- `docker-container-inspect`: Inspect a container
- `docker-container-list`: List containers
- `docker-container-stats`: Get container stats based on resource usage
- `docker-container-top`: List processes running inside a container
- `docker-image-create`: Create an image by either pulling it from a registry or importing it.
- `docker-image-delete`: Remove an image, along with any untagged parent images that were referenced by that image. Images can't be removed if they have descendant images, are being use
- `docker-image-history`: Get the history of an image
- `docker-image-inspect`: Inspect an image


## DockerHardeningCheck

**Type:** script  
**Product:** Common Scripts  

Checks if the Docker container running this script has been hardened according to the recommended settings located in the Docker hardening guide (the platform.13) or Docker hardening guide (the platform.7 On-prem)

**Inputs:**

- `memory`: The amount of memory to check. This is specified in bytes or append MB/GB for Mega/Giga bytes. The default is 1 GB.
- `memory_check`: The memory check type to perform: cgroup - check memory cgroup configuration, allocate - try allocating actual memory and verify that the al
- `pids`: The maximum number of PIDs to check.
- `fds_soft`: The soft file descriptor limit to check.
- `fds_hard`: The hard file descriptor limit to check.
- `cpus`: The number of CPUs limit to check.
- `network_check`: The network check to perform. cloud_metadata - check that access is blocked to cloud metadata server, host_machine - check that access is bl


## Docusign

**Type:** integration  
**Product:** Docusign  

Docusign is a leading provider of electronic signature technology, allowing individuals and organizations to sign, send, and manage documents digitally. The Docusign Monitor API provides access to customer events, which are events that occur in your Docusign account. The Docusign Admin API provides access to user data, which is information about users in your Docusign account

**Commands:**

- `docusign-generate-consent-url`: Generates the Docusign admin consent URL based on configured parameters and environment.
- `docusign-auth-test`: Tests the full authentication flow and API connectivity by validating configuration, exchanging a JWT for an access token, and calling the /oauth/userinfo endpo
- `docusign-get-events`: Fetches events from Docusign. Used for debugging purposes on failures.
- `docusign-reset-access-token`: Resets the access token stored in the integration context.


## domain-enrichment

**Type:** script  
**Product:** Aggregated Scripts  

Enriches Domain indicators with reputation data from multiple integrations and outputs a consolidated DomainEnrichment object. This script exclusively supports indicators of type Domain and will automatically create the indicator in TIM if it is not already exists. Note: This script is supported in the platform.0 and later, and in Cortex XSIAM

**Inputs:**

- `domain_list`: Accepts a list of domains to enrich.- From CLI: Provide a comma-separated list. If a Domain contains a comma, wrap the domains in a JSON arr
- `external_enrichment`: Whether to call external integrations for enrichment: - 'true': enrich using enabled external integrations (e.g., VirusTotal (API v3), Alien
- `verbose`: Retrieve a human-readable entry for each command; if false, only the final result is summarized and errors are suppressed.
- `brands`: A list of integration brands to run enrichment against. Example: `"VirusTotal (API v3), AlienVault OTX v2"`.- If provided, only the selected
- `additional_fields`: When set to true, the output includes an `AdditionalFields` object for each of the indicator result. `AdditionalFields` contains all fields 


## DomainReputation

**Type:** script  
**Product:** Common Scripts  

A context script for domain entities

**Inputs:**

- `domain`: The domain to look up.


## DomainTools Associate Indicator to Incident

**Type:** playbook  
**Product:** DomainTools Iris Investigate  

## DomainTools Auto Pivots

**Type:** playbook  
**Product:** DomainTools Iris Investigate  
**Inputs:**

- `domains`: The domains to lookup.
- `dt_riskscore_threshold`: The minimum risk score threshold value to check.
- `should_wait_for_analyst_review`: Flags if users should wait for an analyst to review. Default is false. Value can be either true/false only.
- `dt_max_name_server_host_count`: The max nameserver host pivot count threshold
- `dt_max_registrant_contact_name_count`: The max registrant contact name pivot count threshold
- `dt_max_registrant_org_count`: The max registrant org pivot count threshold
- `dt_max_ssl_info_organization_count`: The max ssl info organization pivot count threshold
- `dt_max_ssl_info_hash_count`: The max ssl info hash pivot count threshold


## DomainTools Check Domain Risk Score By Iris Tags

**Type:** playbook  
**Product:** DomainTools Iris Investigate  
**Inputs:**

- `dt_min_riskscore_threshold`: The minimum risk score threshold value to check.
- `dt_monitored_iris_tags`: The Iris tags to lookup. Values should be a comma separated value. e.g. (tag1,tag2)
- `should_wait_for_analyst_review`: Flags if users should wait for an analyst to review. Default is false. Value can be either true/false only.


## DomainTools Check New Domains by Iris Hash

**Type:** playbook  
**Product:** DomainTools Iris Investigate  
**Inputs:**

- `iris_search_hash`: The Iris Investigate search hash to pivot.
- `should_wait_for_analyst_review`: Flags if users should wait for an analyst to review. Default is false. Value can be either true/false only.


## DomainTools Iris

**Type:** integration  
**Product:** DomainTools Iris Investigate  

Together, DomainTools and the platform, web crawl, SSL and infrastructure data. SOCs can create custom, automated workflows to trigger Indicator of Compromise (IoC) investigations, block threats based on connected infrastructure, and identify potentially malicious domains before weaponization. The DomainTools App for the platform, decision logic, ad-hoc investigations, and the ability to persist enriched intelligence. This integration was integrated and tested with version 1.0 of DomainTools Iris

**Commands:**

- `domain`: Provides data enrichment for domains.
- `domaintoolsiris-investigate`: Returns a complete profile of the domain (SLD.TLD) using Iris Investigate. If parsing of FQDNs is desired, see domainExtractAndInvestigate.
- `domaintoolsiris-enrich`: Returns a complete profile of the domain (SLD.TLD) using Iris Enrich. If parsing of URLs or FQDNs is desired, see domainExtractAndEnrich.
- `domaintoolsiris-analytics`: Displays DomainTools Analytic data in a markdown format table.
- `domaintoolsiris-threat-profile`: Displays DomainTools Threat Profile data in a markdown format table.
- `domaintoolsiris-pivot`: Pivot on connected infrastructure (IP, email, SSL), or import domains from Iris Investigate using a search hash. Retrieves up to 5000 domains at a time. Optiona
- `domaintools-whois-history`: The DomainTools Whois History API endpoint returns up to 100 historical Whois records associated with a domain name.
- `domaintools-hosting-history`: Hosting History will list IP address, name server and registrar history.
- `domaintools-reverse-whois`: The DomainTools Reverse Whois API provides a list of domain names that share the same Registrant Information. You can enter terms that describe a domain owner, 
- `domaintools-whois`: The DomainTools Parsed Whois API provides parsed information extracted from the raw Whois record. The API is optimized to quickly retrieve the Whois record, gro
- `domainRdap`: Returns the most recent Domain-RDAP registration record.
- `reverseNameServer`: Reverse nameserver lookup.
- `reverseIP`: Reverse loopkup of an IP address or a domain.


## DomainTools Iris Detect

**Type:** integration  
**Product:** DomainTools Iris Detect  

Iris Detect is an Internet infrastructure detection, monitoring, and enforcement tool built on the industry’s fastest and broadest domain discovery engine and the largest databases of domain data. Capturing key data on new domains and risk-scoring them within minutes of discovery, Detect is a game-changer for brand managers, digital risk and fraud prevention teams, and network defenders. Rapid Discovery of Infringing Domains Continuous Monitoring of Evolving Infrastructure Enforcement Actions for Dangerous Domains Iris Detect employs the most sophisticated and extensive new-domain discovery capabilities, across all TLDs globally. Domains are enriched with preliminary Whois, DNS, and Risk Score data. The Iris Detect for the platform, incidents containing mapped indicators of newly-discovered domains matching the monitored keywords. Through ad-hoc War-Room commands or on the incidents directly, domains of interest may be added to Iris Detect’s Watchlist, which triggers automatic daily updates, looking for hosting infrastructure or webpage changes. These changes can be consumed as their own incidents or sent to a separate workflow, giving you the ability to track evolving threat campaigns, classify, and identify which domains are most likely to do harm. Merely knowing about malicious infrastructure is not enough. Iris Detect offers impactful enforcement options: Block flagged domains from incidents directly or using ad-hoc

**Commands:**

- `domaintools-iris-detect-escalate-domains`: Reports a domain to Google's Safe Browsing API. After approval, their block list is picked up by Chrome and most modern browsers.
- `domaintools-iris-detect-blocklist-domains`: Mark a given domain as blocked, which allows a script against the Iris Detect API to pass these domains on to other teams or security controls within your organ
- `domaintools-iris-detect-watch-domains`: Mark a given domain as watched, which will trigger more frequent scanning by DomainTools automation. Changes to watched domains can trigger incidents if enabled
- `domaintools-iris-detect-ignore-domains`: Ignore a given domain, removing it from new and block lists, if applicable.
- `domaintools-iris-detect-get-monitors-list`: This command allows users to retrieve the list of monitored terms and respective IDs associated with your organization's Iris Detect account. New terms can only
- `domaintools-iris-detect-get-new-domains`: Manually retrieve new domains matching all of your monitored terms, or a specific term specified by a "monitor_id" that can be retrieved using the domaintools-i
- `domaintools-iris-detect-get-watched-domains`: Manually retrieve changes to domains that have been marked as "watched" by users of your organization, matching all of your monitored terms, or a specific term 
- `domaintools-iris-detect-get-ignored-domains`: Manually retrieve domains that your organization has marked as ignored, matching all of your monitored terms, or a specific term specified by a "monitor_id" tha
- `domaintools-iris-detect-get-escalated-domains`: Manually retrieve domains that your organization has escalated to Google Safe Browsing, matching all of your monitored terms, or a specific term specified by a 
- `domaintools-iris-detect-get-blocklist-domains`: Manually retrieve domains that your organization has marked as "blocklisted", matching all of your monitored terms, or a specific term specified by a "monitor_i
- `domaintools-iris-detect-reset-fetch-indicators`: This command will reset your fetch history.


## DomainTools Iris Risk Score

**Type:** playbook  
**Product:** DomainTools Iris Investigate  

This playbook retrieves the Domain Risk Score of the given domain and check if the risk score is over the threshold and throws an Alert for the Analyst to manually review the domain indicator

**Inputs:**

- `domains`: The domain(s) to query. Can lookup multiple domains using a comma-separated values. e.g mydomain1.com,mydomain2.com
- `dt_min_riskscore_threshold`: The minimum risk score threshold.
- `should_wait_for_analyst_review`: Flags if users should wait for an analyst to review. Default is true. Value can be either true/false only.


## DomainToolsIrisDetectStatusUpdate

**Type:** script  
**Product:** DomainTools Iris Detect  

Update the DomainTools Iris Detect Domain State


## Doppel

**Type:** integration  
**Product:** Doppel  

Doppel is a Modern Digital Risk Protection Solution, that detects the phishing and brand cyber attacks on the emerging channels. Doppel scans millions of channels online which includes, social media, domains, paid ads, dark web, emerging channels, etc. Doppel can identify the malicious content and cyber threats, and enables their customers to take down the digital risks proactively. The the platform. The pack also contains the commands to perform different operations on Doppel alerts

**Commands:**

- `doppel-get-alert`: Retrieves the alert details by ID or entity. Must include either ID or entity.
- `doppel-create-alert`: Creates an alert for a specified entity. This command requires the entity to be provided in the arguments.
- `doppel-update-alert`: Updates an alert in the Doppel platform. Either alert_id or entity must be specified.
- `doppel-create-abuse-alert`: Create an alert for the provided value to abuse box. Will fail if the alert value is invalid or is protected.
- `doppel-get-alert-screenshot`: Fetch the alert's current screenshot from Doppel and attach it to the incident as a War Room file entry. The image is downloaded immediately after the URL is si
- `doppel-get-alerts`: Retrieves a list of alerts. The result can be filtered by provided parameters.
- `get-mapping-fields`: Returns the list of fields for an incident type.
- `update-remote-system`: Pushes local changes to the remote system. If an platform Incident is closed, created via Doppel Integration, then on Doppel Portal the Alert status will be upd
- `get-remote-data`: Get remote data from a remote incident. This method does not update the current incident, and should be used for debugging purposes.
- `get-modified-remote-data`: Gets the list of incidents that were modified since the last update time. Note that this method is here for debugging purposes. The get-modified-remote-data com


## Doppel Screenshot Preview

**Type:** playbook  
**Product:** Doppel  

This playbook previews a screenshot URL from a Doppel alert in the incident War Room

**Inputs:**

- `screenshot_url`: The URL of the screenshot from Doppel alert


## DownloadAndArchivePythonLibrary

**Type:** script  
**Product:** Common Scripts  

The script downloads a Python library using PIP, archives it and return in to the war room

**Inputs:**

- `library_name`: The Python library you wish to download and archive.


## Dragos Worldview

**Type:** integration  
**Product:** Dragos Worldview  

Custom integration designed to pull in reports from the Dragos Worldview API as incidents This integration was integrated and tested with version 1.0 of Dragos Worldview

**Commands:**

- `dragos-get-indicators`: Get Indicators from the Dragos WorldView API


## DrawRelatedIncidentsCanvas

**Type:** script  
**Product:** Base  

Draw incidents and indicators on the canvas to map and visualize their connections

**Inputs:**

- `incidentID`: Incident ID of the incident with which to update the canvas. If not specified, updates the current incident.
- `relatedIncidentsIDs`: Incident IDs to draw on the canvas and relate to the main incident. The format can be a list of IDs or comma-separated values.
- `indicators`: Indicators to draw on the canvas. The format is a list of indicator objects.
- `layout`: The canvas layout. Can be "multipartite", "shell", "spring", "kamada_kawai", or "circular".
- `overrideUserCanvas`: Override the canvas if it exists.


## Drift

**Type:** integration  
**Product:** Drift  

Drift integration to fetch, modify, create and delete contacts within the Drift Plattform's Contact API. This integration was integrated and tested with version 1.7 of Drift

**Commands:**

- `drift-get-contact`: Retrieve a contact using their email address (for multiple) or ID (for single).
- `drift-update-contact`: Patch Contact Updates using contact ID
- `drift-delete-contact`: Delete Contact using contact ID
- `drift-post-contact`: Post New Contact using a new contact Email


## DropBox - Massive scale operations on files

**Type:** playbook  
**Product:** Dropbox  

This playbook investigates “Massive File Alterations” and “DropBox - Massive File Downloads” alerts by gathering user and IP information and performing remediation based on the information gathered and received from the user. Used Sub-playbooks: If you wish to link this playbook to the relevant alerts automatically, we recommend using the following filters when configuring the playbook triggers: Alert Source = Correlation Alert Name = DropBox - Massive File Alterations, DropBox - Massive File Downloads

**Inputs:**

- `InternalRange`: List of Internal IP ranges


## DSPM Re-run incident

**Type:** playbook  
**Product:** DSPM  

The "DSPM Re-run Incident" playbook is designed to automatically re-run DSPM incidents. It starts by executing the RerunDSPMIncidents task, which reinitiates the incidents for further investigation or processing. After completing this task, the playbook proceeds to close the current incident using the closeInvestigation script. This playbook ensures that DSPM incidents can be efficiently retried and closed upon completion


## DSPMCheckAndSetErrorEntries

**Type:** script  
**Product:** DSPM  

This script checks for error entries based on provided entry IDs and returns "yes" if any errors are found or "no" if no errors are present. If errors are detected, it sets the error messages in the platform context

**Inputs:**

- `entry_id`: Entry to check.


## DSPMExtractRiskDetails

**Type:** script  
**Product:** DSPM  

This script extracts risk details from an incident object, processes asset tags, and sets the user's Slack email for future notifications. It retrieves the incident details, including risk information, asset tags, and configuration details from the DSPM integration. If the asset owner's email is found, it is stored; otherwise, a default email is used.The extracted data is stored in the platform context and displayed in a readable markdown format

**Inputs:**

- `incident_object`: Incident data of a specific asset.
- `defaultSlackUser`: Default slack user provided by user.


## DSPMGetContianers

**Type:** script  
**Product:** DSPM  

This automation script takes asset file data as input, retrieves the container names from this data, and returns a list of all containers

**Inputs:**

- `asset_files`: Asset files data.


## DSPMIncidentList

**Type:** script  
**Product:** DSPM  

This automation script manages incidents in a list by adding or deleting incidents based on the provided action. For incidents older than the configured time limit (default is 48 hours), the script performs a cleanup by removing the incident from the list. Additionally, the script supports adding new incidents to the list if they do not already exist

**Inputs:**

- `incident_data`: Incident data of a specific asset.
- `action`: Action to perform on incident list i.e :- add or delete list.
- `incident_list`: DSPM Incident list data.
- `rerun_time`: Re-run time to be checked of an incident to delete or not.


## DSPMRerunIncidents

**Type:** script  
**Product:** DSPM  
**Inputs:**

- `time_duration`: Time Duration under which we are going to re-run the incident.
- `incident_list`: DSPM Incident list data.
- `rerun_time`: Re-run time to be checked of an incident to run.


## DT

**Type:** script  
**Product:** Filters And Transformers  

This automation allows the usage of DT scripts within playbooks transformers

**Inputs:**

- `value`: The value to perform the transformation on.
- `dt`: DT expression.


## DumpJSON

**Type:** script  
**Product:** Common Scripts  

Dumps a JSON from the context key input, and returns a JSON object string result

**Inputs:**

- `key`: The context path to the JSON object.


## DUO Admin

**Type:** integration  
**Product:** DUO Admin  

DUO for admins. Must have access to the admin api in order to use this. This integration was integrated and tested with version 4.4.0 of DUO Admin

**Commands:**

- `duoadmin-get-authentication-logs-by-user`: Returns authentication logs associated with a user. Limited to 30 at a time
- `duoadmin-dissociate-device-from-user`: Dissociates a device from a user
- `duoadmin-delete-u2f-token`: Delete a u2f token
- `duoadmin-get-users`: Return usernames and their user id
- `duoadmin-get-devices-by-user`: Return devices associated with a user
- `duoadmin-get-u2f-tokens-by-user`: Returns a list of U2F tokens associated with the given username
- `duoadmin-get-devices`: Returns all existing devices
- `duoadmin-associate-device-to-user`: Associates a device to a user
- `duoadmin-get-admins`: Returns administrator accounts
- `duoadmin-get-bypass-codes`: Retrieves the information from the bypass code table
- `duoadmin-modify-admin`: Modify the administrator user.
- `duoadmin-modify-user`: Modify the user account.


## DuoAuth

**Type:** integration  
**Product:** DuoAuth  

The Duo Auth API lets developers integrate with Duo Security's platform at a low level

**Commands:**

- `duoauth-push-notification`: Send push message to Duo user.


## DuoPush

**Type:** playbook  
**Product:** DuoAuth  

Send Duo Push message to enrolled user

**Inputs:**

- `Username`: Enrolled user in Duo
- `Pushinfo`: Message to user in Duo
- `TryAgain`: Try sending message Again for 1 more time, default is False.


## Edgescan

**Type:** integration  
**Product:** Edgescan  

Cloud-based continuous vulnerability management and penetration testing solution. This integration was integrated and tested with version 1.6 of Edgescan

**Commands:**

- `edgescan-host-get-hosts`: Get a list of all hosts
- `edgescan-host-get`: Get detailed information about a host.
- `edgescan-host-get-export`: Get a list of hosts in export format.
- `edgescan-host-get-query`: Get a list of hosts by query
- `edgescan-host-update`: Update a host
- `edgescan-asset-get-assets`: Get the full list of assets
- `edgescan-asset-get`: Get asset details
- `edgescan-asset-get-query`: Query the asset database
- `edgescan-asset-create`: Create an asset
- `edgescan-asset-update`: Update an asset
- `edgescan-asset-delete`: Delete an asset
- `edgescan-user-get-users`: Get the full user list
- `edgescan-user-get`: Get user details
- `edgescan-user-get-query`: Query for a user
- `edgescan-user-create`: Create a user


## EditServerConfig

**Type:** script  
**Product:** Common Scripts  

Edit the server configuration (under settings/troubleshooting). You can either add a new configuration or update and remove an existing one

**Inputs:**

- `action`: The action to make. If update is chosen and the key does not exist, a new key will be added.
- `key`: The key to set.
- `value`: The value to set.


## EDL Monitor

**Type:** integration  
**Product:** EDL Monitor  

This integration can monitor EDLs by emailing the content of an EDL as a zipped file to a specified user at an interval (when run with a job), and/or simply monitor the EDL for availability and email the user if the EDL is not available in other playbooks

**Commands:**

- `get-edl-contents`: Gets the current contents of an EDL
- `email-edl-contents`: Gets the current contents of an EDL and emails it to a specified email address
- `check-status`: Return the response code of the EDL


## Endace

**Type:** integration  
**Product:** Endace  

The EndaceProbe Analytics Platform provides 100% accurate, continuous packet capture on network links up to 100Gbps, with unparalleled depth of storage and retrieval performance. Coupled with the Endace InvestigationManager, this provides a central search and data-mining capability across a fabric of EndaceProbes deployed in a network. This integration uses Endace APIs to search, archive and download PCAP file from either a single EndaceProbe or many via the InvestigationManager and enables integration of full historical packet capture into security automation workflows. This integration was integrated and tested with version 6.5.7 & 7.0.0 of Endace

**Commands:**

- `endace-create-search`: Create a search task on EndaceProbe. Search is issued against all Rotation Files on EndaceProbe.
- `endace-get-search-status`: Get search status from EndaceProbe. This command can be polled in a loop until response is received or polling timer is over.
- `endace-delete-search-task`: Delete search task
- `endace-create-archive`: Create an archive task to archive packets of interest on EndaceProbe. Archived packets can later be downloaded from EndaceProbe as a PCAP file. Archived Files n
- `endace-get-archive-status`: get status of archived task
- `endace-delete-archive-task`: delete archive task
- `endace-download-pcap`: Download a copy of the PCAP file from EndaceProbe if PCAP file size is within the threshold value defined by filesizelimit.
- `endace-delete-archived-file`: Delete an archived file from EndaceProbe.


## Enrich Custom IOCs - Dataminr Pulse

**Type:** playbook  
**Product:** Dataminr Pulse  

This playbook will enrich the Dataminr Pulse ReGenAI Incident's IOCs using custom reputation commands

**Inputs:**

- `vulnerability_indicators`: List of Vulnerability indicators.
- `malware_indicators`: List of Malware indicators.
- `threat_actors_indicators`: List of threat actor indicators.


## Enrich DXL with ATD verdict v2

**Type:** playbook  
**Product:** McAfee DXL  

Uses McAfee ATD to push any malicious verdicts over DXL. Detonates a file in ATD and if malicious, pushes its MD5, SHA1 and SHA256 hashes to McAfee DXL


## Enrich McAfee DXL using 3rd party sandbox v2

**Type:** playbook  
**Product:** McAfee DXL  

Example of bridging DXL to a third party sandbox. Detonate a file in 3rd party sandbox and if malicious, push its MD5, SHA1 and SHA256 hashes to McAfee DXL


## Enrich ThinkstCanary Events

**Type:** playbook  
**Product:** Thinkst Canary  

Enrich events that are received as part of a ThinkstCanary incident


## enrich_exclude_button

**Type:** script  
**Product:** Common Scripts  

## Entra ID Applications

**Type:** integration  
**Product:** Microsoft Graph Applications  

Use the Entra ID Applications integration (formerly Azure Active Directory Applications) to manage authorized applications. This integration was integrated and tested with version v1.0 of Microsoft Graph Services API

**Commands:**

- `msgraph-apps-auth-start`: Run this command to start the authorization process and follow the instructions in the command results.
- `msgraph-apps-auth-complete`: Run this command to complete the authorization process. Should be used after running the msgraph-apps-auth-start command.
- `msgraph-apps-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `msgraph-apps-auth-test`: Tests connectivity to Microsoft.
- `msgraph-apps-service-principal-list`: Retrieves a list of applications.
- `msgraph-apps-service-principal-remove`: Removes an application from the directory.
- `msgraph-apps-service-principal-get`: Retrieve the properties and relationships of a servicePrincipal object.
- `msgraph-apps-service-principal-update`: Update the properties of servicePrincipal object.
- `msgraph-apps-service-principal-password-add`: Add a strong password or secret to a service principal.
- `msgraph-apps-service-principal-password-remove`: Remove a password from a service principal.
- `msgraph-apps-service-principal-unlock-configuration`: Unlock configuration of a service principal.
- `msgraph-apps-service-principal-lock-configuration`: Lock configuration of a service principal.


## Entra ID Users

**Type:** integration  
**Product:** Microsoft Graph User  

The Entra ID Users integration (formerly Azure Active Directory Users) is a Unified gateway to security insights - all from a unified Microsoft Graph User API

**Commands:**

- `msgraph-user-account-disable`: Disables a user from all Office 365 applications, and prevents sign in. Note: This command disables the user but does not terminate an existing session. Support
- `msgraph-user-unblock`: Unblock a user.
- `msgraph-user-update`: Updates the properties of a user object. Permissions: - User.ReadWrite (Delegated & Application) Permission For unblocking an admin/privileged user: User.Enable
- `msgraph-user-delete`: Deletes an existing user. Permissions: Directory.AccessAsUser.All (Delegated), User.ReadWrite.All (Application)
- `msgraph-user-create`: Creates a new user. Permissions: User.ReadWrite.All (Delegated & Application)
- `msgraph-user-get`: Retrieves the properties and relationships of a user object. For more information, visit: https://learn.microsoft.com/en-us/graph/api/user-get?view=graph-rest-1
- `msgraph-user-list`: Retrieves a list of user objects. Permissions: User.ReadBasic.All (Delegated), User.Read.All (Application)
- `msgraph-direct-reports`: Retrieves the direct reports for a user. Direct reports are the people who have that user configured as their manager.
- `msgraph-user-get-manager`: Retrieves the properties from the manager of a user.
- `msgraph-user-assign-manager`: Assigns a manager to the specified user. Permission: - User.ReadWrite (Delegated) or - User.ReadWrite (Application)
- `msgraph-user-change-password`: Changes the user password. Supported only in a self deployed app flow with the Permission: Directory.AccessAsUser.All(Delegated) Note: In order to change the pa
- `msgraph-user-test`: Tests connectivity to Microsoft Graph User.
- `msgraph-user-session-revoke`: Revoke a user session by invalidating all refresh tokens issued to applications for a user. This command requires an administrator role. Permission required: Di
- `msgraph-user-generate-login-url`: Generate the login url used for Authorization code flow.
- `msgraph-user-auth-reset`: Run this command if for some reason you need to rerun the authentication process.


## Envoy IAM

**Type:** integration  
**Product:** Envoy  

Integrate with Envoy Identity Access Management services to execute CRUD operations to employee lifecycle processes. This integration was integrated and tested with version v2 of Envoy SCIM API

**Commands:**

- `iam-create-user`: Creates a user.
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Disable an active user.


## EPOFindSystem

**Type:** script  
**Product:** McAfee ePO  

Returns system information

**Inputs:**

- `searchText`: The free text to search for. Can be, "hostname", "agent guid", etc.


## EvaluateContextValue

**Type:** script  
**Product:** Common Scripts  

The script is for use with GenericPolling, which checks the completion condition. It uses a DT to retrieve a value from the context data and evaluates it using another DT

**Inputs:**

- `id`: The ID to identify the output value.
- `dt_encoding`: The encoding scheme for the value_dt and eval_dt parameters. This can be useful for those parameters that contain special characters and req
- `value_dt`: The DT expression for retrieving a value from the context data.
- `eval_dt`: The DT expression for retrieving data for the evaluation from the value.
- `eval_key`: The key name that is associated with the value before it's passed to eval_dt. If this parameter is provided, eval_dt receives a key-value pa
- `playbook_id`: The sub-playbook ID to get its local context from the context data.


## EvaluateMLModllAtProduction

**Type:** script  
**Product:** Machine Learning  

Evaluates an ML model in production

**Inputs:**

- `incidentTypes`: A common-separated list of incident types by which to filter.
- `incidentsQuery`: The incident query to fetch the training data for the model.
- `emailTagKey`: The field name with the email tag. Supports a comma-separated list, the first non-empty value will be taken.
- `emailPredictionKey`: The field name with the model prediction.
- `emailPredictionProbabilityKey`: The field name with the model prediction probability.
- `modelTargetAccuracy`: The model target accuracy, between 0 and 1.
- `phishingLabels`: A comma-separated list of email tags values and mapping. The script considers only the tags specified in this field. You can map label to an
- `additionalFields`: A comma-separated list of incident field names to include in the results file.


## EWS Extension Online Powershell v3

**Type:** integration  
**Product:** Microsoft Exchange Online  

Use the EWS Extension Online Powershell v3 integration to get information about mailboxes and users in your organization. This integration was integrated and tested with version 3 of the Exchange Online PowerShell module (EXO V3). Note: This integration does not replace the O365 - EWS - Extension integration, but an additional EWS extension integration which utilizes the EXO v3 module

**Commands:**

- `ews-mailbox-list`: Displays mailbox objects and attributes, populate property pages, or supplies mailbox information to other tasks.
- `ews-cas-mailbox-list`: Displays Client Access settings that are configured on mailboxes.
- `ews-mailbox-permission-list`: Retrieves permissions on a mailbox.
- `ews-recipient-permission-list`: Displays information about SendAs permissions that are configured for users.
- `ews-recipient-list`: Displays existing recipient objects in your organization. This command returns all mail-enabled objects (for example, mailboxes, mail users, mail contacts, and 
- `ews-new-tenant-allow-block-list-items`: Add new items to the Tenant Allow/Block Lists. Uses PowerShell New-TenantAllowBlockListItems cmdlet.
- `ews-get-tenant-allow-block-list-items`: Retrieve current Tenant Allow/Block List items. Uses Get-TenantAllowBlockListItems cmdlet.
- `ews-get-tenant-allow-block-list-count`: Retrieve current count of defined Tenant Allow/Block List items. Uses Get-TenantAllowBlockListItems cmdlet.
- `ews-remove-tenant-allow-block-list-items`: Remove items from the Tenant Allow/Block Lists. You can delete items by their value or by unique ID. Uses PowerShell cmdlet Remove-TenantAllowBlockListItems cmd
- `ews-export-quarantinemessage`: Export quarantine messages.
- `ews-get-quarantinemessage`: Retrieve quarantine messages.
- `ews-release-quarantinemessage`: Releases the quarantined messages. Uses the PowerShell Release-QuarantineMessage cmdlet.
- `ews-junk-rules-get`: Gets junk rules for the specified mailbox.
- `ews-junk-rules-set`: Sets junk rules for the specified mailbox.
- `ews-global-junk-rules-set`: Sets junk rules in all managed accounts.


## EWS v2

**Type:** integration  
**Product:** Microsoft Exchange On-Premise  

Exchange Web Services (EWS) provides the functionality to enable client applications to communicate with the Exchange server. EWS provides access to much of the same data that is made available through Microsoft Office Outlook. The EWS v2 integration implants EWS leading services. The integration allows getting information on emails and activities in a target mailbox, and some active operations on the mailbox such as deleting emails and attachments or moving emails from folder to folder. Note: Starting from pack version 2.0.0 the EWS v2 integration requires the Exchange server to support TLS v1.2 and up in order to connect. Multi-Factor Authentication (MFA) EWS v2 does not support Multi-Factor Authentication (MFA). If using MFA, use EWS O365 (see  or if you have Graph Outlook use O365 Outlook Mail (Using Graph API) (see  or O365 Outlook Mail Single User (Using Graph API) (see

**Commands:**

- `ews-get-attachment`: Retrieves the actual attachments from an item (email message). To get all attachments for a message, only specify the item-id argument.
- `ews-delete-attachment`: Deletes the attachments of an item (email message).
- `ews-get-searchable-mailboxes`: Returns a list of searchable mailboxes. This command requires eDiscovery permissions to the Exchange Server. For more information, see the EWSv2 integration doc
- `ews-search-mailboxes`: Searches over multiple mailboxes or all Exchange mailboxes. Use either the mailbox-search-scope command or the email-addresses command to search specific mailbo
- `ews-move-item`: Move an item to different folder in the mailbox.
- `ews-delete-items`: Delete items from mailbox. This command requires eDiscovery permissions to the Exchange Server. For more information, see the EWSv2 integration documentation.
- `ews-search-mailbox`: Searches for items in the specified mailbox. Specific permissions are needed for this operation to search in a target mailbox other than the default.
- `ews-get-contacts`: Retrieves contacts for a specified mailbox.
- `ews-resolve-name`: This operation verifies aliases and matches display names to the correct mailbox user. It handles one ambiguous name at a time. If there are multiple potential 
- `ews-get-out-of-office`: Retrieves the out-of-office status for a specified mailbox.
- `ews-recover-messages`: Recovers messages that were soft-deleted.
- `ews-create-folder`: Creates a new folder in a specified mailbox.
- `ews-mark-item-as-junk`: Marks an item as junk. This is commonly used to block an email address. For more information, see the Microsoft documentation: https://msdn.microsoft.com/en-us/
- `ews-find-folders`: Retrieves information for folders for a specified mailbox. Only folders with read permissions will be returned. Your visual folders on the mailbox, such as "Inb
- `ews-get-items-from-folder`: Retrieves items from a specified folder in a mailbox. The items are order by the item created time, most recent is first.


## EWSApiModule

**Type:** script  

The EWS API Module handles generic logic for interacting with an EWS Server. It provides a client class for interacting with the EWS API as well as common methods for performing various EWS related operations such as getting or sending items, retrieving attachments, creating/updating/deleting folders, and more. To use the EWS API module, you'll need to follow these steps: For examples, see the EWSO365 and EWSv2 integrations


## Exabeam Advanced Analytics

**Type:** integration  
**Product:** Exabeam Advanced Analytics  

The Exabeam Security Management Platform provides end-to-end detection, User Event Behavioral Analytics and SOAR. This integration was integrated and tested with version 53.5 of Exabeam. There are 2 authentication methods: For additional information, refer to Exabeam Administration Guide

**Commands:**

- `exabeam-get-notable-users`: Returns notable users in a period of time.
- `exabeam-get-watchlists`: Returns all watchlist IDs and titles.
- `exabeam-get-peer-groups`: Returns all peer groups.
- `exabeam-get-user-info`: Returns user information data for the username.
- `exabeam-get-user-labels`: Returns all labels of the user.
- `exabeam-get-user-sessions`: Returns sessions for the given username and time range.
- `exabeam-delete-watchlist`: Deletes a watchlist.
- `exabeam-get-asset-data`: Returns asset data.
- `exabeam-get-session-info-by-id`: Returns session info data for the given ID.
- `exabeam-list-top-domains`: List top domains of a sequence.
- `exabeam-list-triggered-rules`: Gets all the triggered rules of a sequence.
- `exabeam-get-asset-info`: Returns asset information for given asset ID (hostname or IP address).
- `exabeam-list-asset-timeline-next-events`: Gets next events for a given asset.
- `exabeam-list-security-alerts-by-asset`: Gets security alerts for a given asset.
- `exabeam-search-rules`: Searches for rules by a keyword.


## Exabeam Data Lake

**Type:** integration  
**Product:** ExabeamDataLake  

Exabeam Data Lake provides a searchable log management system. Data Lake is used for log collection, storage, processing, and presentation. This integration was integrated and tested with version LMS-i40.3 of Exabeam Data Lake

**Commands:**

- `exabeam-data-lake-search`: Get events from Exabeam Data Lake.


## Exabeam Security Operations Platform

**Type:** integration  
**Product:** Exabeam Security Operations Platform  

Exabeam Security Operations Platform offers a centralized and scalable platform for log management. This integration was integrated and tested with version v1.0 of ExabeamSecOpsPlatform

**Commands:**

- `exabeam-platform-event-search`: Get events from Exabeam Security Operations Platform.
- `exabeam-platform-table-record-list`: Retrieve the records for a specific context table.
- `exabeam-platform-table-record-create`: Add one or more context records directly to an existing table.
- `exabeam-platform-alert-search`: Search for alerts that match one or more search criteria.
- `exabeam-platform-context-table-delete`: Delete a specific context table, including records and attributes.
- `exabeam-platform-table-record-list`: Retrieve metadata for all existing context tables, including source, operational status, and attribute mapping.
- `exabeam-platform-case-search`: Search for cases that match one or more search criteria. For example, you can search for cases that are associated with a specific caseId and that reference spe
- `exabeam-platform-get-events`: Get cases from Exabeam Security Operations Platform as Cortex XSIAM events. This command is supported in Cortex XSIAM only and is intended to be used for debugg
- `exabeam-get-threat-summary`: Retrieve the Copilot Threat Summary for an individual alert.
- `exabeam-update-case-details`: Update details for a specific case.
- `exabeam-platform-list-case-notes`: Retrieve a list of notes associated with the specified caseId.
- `exabeam-platform-create-case-note`: Add a new note to the specified case.


## Example-Delinea-Folder Operations

**Type:** playbook  
**Product:** Delinea Secret Server  

Example for usage integration REST API Folder object for Delinea Secret Server


## Example-Delinea-Retrieved Username and Password

**Type:** playbook  
**Product:** Delinea Secret Server  

Example for usage integration REST API for Delinea Secret Server. Methods retrieved username and password form secret

**Inputs:**

- `name`: Secret name field for search credentials


## Example-Delinea-Secret Object Operations

**Type:** playbook  
**Product:** Delinea Secret Server  

Example for usage integration REST API Secret object for Delinea Secret Server


## Example-Delinea-User object operations for Secret Server

**Type:** playbook  
**Product:** Delinea Secret Server  

Example for usage integration REST API User object for Delinea Secret Server


## ExampleJSScript

**Type:** script  
**Product:** Common Scripts  

Showcases how to use and write JavaScript scripts. (This is only an example script.)

**Inputs:**

- `ArgumentExample`: The example argument that will be passed into and used by the script.


## ExceedLMS IAM

**Type:** integration  
**Product:** Exceed LMS  

Note: This integration should be used as part of our Identity Lifecycle Management premium pack. For more information, please refer to the Identity Lifecycle Management article. This integration was integrated and tested with version v2 of ExceedLMS

**Commands:**

- `iam-create-user`: Creates a user.
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Disable an active user.


## ExifRead

**Type:** script  
**Product:** Common Scripts  

Reads an image file's metadata and provides Exif tags

**Inputs:**

- `EntryID`: The entry ID of the image file.


## Exists

**Type:** script  
**Product:** Common Scripts  

Checks if a given value exists in the context. The script will return "no" for an empty arrays. This script should be used mostly with DQ and selectors

**Inputs:**

- `value`: The value to check if it exists. It can handle arrays as well.


## Expire Inactive Detections - Vectra RUX

**Type:** playbook  
**Product:** Vectra RUX  

This playbook identifies incidents with inactive detections and updates their investigation status to "expired"

**Inputs:**

- `incident_type`: The platform incident type to search for inactive detections. Default is 'Vectra RUX Events Detection'.


## expire-password

**Type:** script  
**Product:** Aggregated Scripts  

This script expires users password for multiple services

**Inputs:**

- `user_id`: List of user IDs whose passwords will be expired. At least one of user_id, user_name, or user_email is required.
- `user_name`: List of user names whose passwords will be expired. At least one of user_id, user_name, or user_email is required.
- `user_email`: List of emails of the users to expire their password. At least one of user_id, user_name, or user_email is required.
- `brands`: List of brands to expire password from.
- `verbose`: Whether to fetch a human-readable entry for each command or just the final result. If set to true, all commands will have human-readable ent


## ExportAuditLogsToFile

**Type:** script  
**Product:** Common Scripts  

Uses the Core REST API integration to query the server audit trail logs, and return back a CSV or JSON file

**Inputs:**

- `days_back`: How many days back to fetch for, supports 1,2,3 or 7 days back.
- `output`: Type of File to return, either JSON, or CSV


## ExportContextToJSONFile

**Type:** script  
**Product:** Common Scripts  

Exports the Context for the current Incident to a JSON file in the war room

**Inputs:**

- `filename`: Name of the file to create in the war room, defaults to context.json.


## ExportIncidentsToCSV

**Type:** script  
**Product:** Common Scripts  

This automation uses the Core REST API Integration to batch export Incidents to CSV and return the resulting CSV file to the war room

**Inputs:**

- `query`: The query for the Incidents that you want to export. (e.g. status:closed -category:job). You can and should generate the query from the Inci
- `fetchdays`: The number of days back to fetch incidents. This argument acts as the primary time filter and is always applied, even when using the query a
- `columns`: Comma separated list of columns (fields) for the CSV. (Default is: id,name,type,severity,status,owner,roles,playbookId,occurred,created,modi


## ExportIndicatorsToCSV

**Type:** script  
**Product:** Common Scripts  

This automation uses the Core REST API Integration to batch export Indicators to CSV and return the resulting CSV file to the war room

**Inputs:**

- `query`: The query for the Indicators that you want to export. (e.g. type:IP and reputation:Bad and expirationStatus:active). You can and should gene
- `seenDays`: Indicator last seen days (default is 7). Needs to be a number.
- `columns`: Comma separated list of columns (fields) for the CSV. (Default is: id,indicator_type,value,source,score,relatedIncCount,setBy,sourceBrands,m


## ExportMLModel

**Type:** script  
**Product:** Machine Learning  

Exports an existing ML model to a file

**Inputs:**

- `modelName`: The name of the ML model to export to a file.


## ExportToCSV

**Type:** script  
**Product:** Common Scripts  

Export given array to csv file

**Inputs:**

- `fileName`: output filename
- `csvArray`: Array to export
- `headers`: Array to hold the file headers in order. Also excepts a comma separated list.
- `codec`: UTF-16-BOM to encode Non English characters. Default is: UTF-8


## ExportToXLSX

**Type:** script  
**Product:** Common Scripts  

Exports context data to a Microsoft Excel Open XML Spreadsheet (XLSX) file

**Inputs:**

- `file_name`: The output file name (for example "Report.xlsx").
- `data`: The data to export. Accepts a context key of a dictionary or a list of dictionaries for a single sheet file (${data}). Separate multiple she
- `sheet_name`: The sheet name. Separate multiple sheet names using a comma ",", for example, sheet1,sheet2.
- `headers`: A comma-separated list of headers. The order that you pass the headers determines how they display in the exported sheet(s). Separated multi
- `bold`: Whether table headers should be bold. If this argument is set to "true", table headers are bold. Default is "true".
- `border`: Whether borders should be added to table cells. If this argument is set to "true", borders are added to table cells. Default is "true".


## ExposeIncidentOwner

**Type:** script  
**Product:** Common Scripts  

Exposes the incident owner into IncidentOwner context key


## Exterro FTK

**Type:** integration  
**Product:** Exterro/AccessData  

Use the Exterro package to integrate with the Exterro FTK platform enabling the automation of case/evidence management and endpoint collection. Documentation for the integration was provided by FTK Connect

**Commands:**

- `exterro-ftk-trigger-workflow`: Triggers the automation job and returns a string.


## ExtFilter

**Type:** script  
**Product:** Community Common Scripts  

Filter values with complex conditions. You can make filters with comlex and combination conditions for the context data at any level of the tree

**Inputs:**

- `value`: The value to filter/transform.
- `path`: Context path to which to filter
- `operator`: The operation name to filter/transform.
- `filter`: The filter.
- `ctx_platform`: Enable to access the context data
- `ctx_inputs`: Enable to access the input parameters to sub playbooks and use ${inputs.}
- `ctx_lists`: Enable to access the list data and use ${list.}
- `ctx_incident`: Enable to access the incident context and use ${incident.}


## ExtraHop - CVE-2019-0708 (BlueKeep)

**Type:** playbook  
**Product:** ExtraHop Reveal(x)  

This server received a Remote Desktop Protocol (RDP) connection request that is consistent with a known vulnerability, also known as BlueKeep, in older versions of Microsoft Windows. This vulnerability allows an unauthenticated attacker to remotely run arbitrary code on an RDP server. The attacker can then tamper with data or install malware that could propagate to other Windows devices across the network. Investigate to determine if this server is hosting a version affected by CVE-2019-0708: Windows 7, Windows XP, Windows Vista, Windows Server 2003, and Windows Server 2008. MITIGATION OPTIONS

**Inputs:**

- `AutoBlockIp`: Enables the Block IP capability automatically, can be, "True" or "False". The Block IP sub-playbook will block the offender IP address in th


## ExtraHop - Default

**Type:** playbook  
**Product:** ExtraHop Reveal(x)  

Handles ticket tracking as well as triggeres specific playbooks based on the name of the ExtraHop Detection. Default playbook to run for all ExtraHop Detection incidents


## ExtraHop - Get Peers by Host

**Type:** playbook  
**Product:** ExtraHop Reveal(x)  

Retrieves the peer network devices that communicated with that host in a given time range, when given a host. In addition to a list of peers and protocols (sorted by bytes) the playbook returns a link to the ExtraHop Live Activity Map to visualize the peer relationships

**Inputs:**

- `name`: The name of the device. This searches for matches on all ExtraHop name fields (DHCP, DNS, NetBIOS, Cisco Discovery Protocol, etc.).
- `ip`: The IP address of the device.
- `mac`: The MAC address of the device.
- `from_time`: The beginning timestamp of the time range the playbook will use to search, expressed in seconds since the epoch.
- `until_time`: The ending timestamp of the time range the playbook will use to search, expressed in seconds since the epoch.


## ExtraHop Reveal(x)

**Type:** integration  
**Product:** ExtraHop Reveal(x)  

ExtraHop Reveal(x) for the platform, real-time threat detections backed by machine learning, and guided investigation workflows that simplify response

**Commands:**

- `extrahop-watchlist-get`: Get all devices on the advanced analysis watchlist in ExtraHop Reveal(x).
- `extrahop-peers-get`: Get all peers for a device from ExtraHop Reveal(x).
- `extrahop-devices-search`: Search for devices in ExtraHop Reveal(x).
- `extrahop-protocols-get`: Get all active network protocols for a device from ExtraHop Reveal(x).
- `extrahop-activity-map-get`: Get a link to a live activity map in ExtraHop Reveal(x).
- `extrahop-alert-rules-get`: Get all alert rules from ExtraHop Reveal(x).
- `extrahop-packets-search`: Search for specific packets in ExtraHop Reveal(x).
- `extrahop-devices-tag`: Add or remove a tag from devices in ExtraHop Reveal(x).
- `extrahop-alert-rule-create`: Create a new alert rule in ExtraHop Reveal(x).
- `extrahop-ticket-track`: Link an ExtraHop Reveal(x) detection to a the platform.
- `extrahop-alert-rule-edit`: Modify an alert rule in ExtraHop Reveal(x).
- `extrahop-watchlist-edit`: Add or remove devices from the advanced analysis watchlist in ExtraHop Reveal(x).
- `extrahop-metrics-list`: Get metrics for specified objects from ExtraHop Reveal(x).
- `extrahop-detections-list`: Get detections from ExtraHop Reveal(x).


## ExtraHopTrackIncidents

**Type:** script  
**Product:** ExtraHop Reveal(x)  

Links an incident investigation back to the ExtraHop Detection that created it


## F5 LTM

**Type:** integration  
**Product:** F5 LTM  

Manages F5 LTM This integration was integrated and tested with version 16.1.0 of F5LTM

**Commands:**

- `f5-ltm-get-pools`: Get a list of all pools
- `f5-ltm-get-pool`: Get pool details
- `f5-ltm-get-pool-members`: Get Pool Members
- `f5-ltm-get-nodes`: Get a list of all nodes
- `f5-ltm-get-node`: Get node details
- `f5-ltm-disable-node`: Disable a node
- `f5-ltm-enable-node`: Enable a node
- `f5-ltm-get-pool-member-stats`: Get Pool Member Stats
- `f5-ltm-get-node-stats`: Get Node Stats
- `f5-ltm-get-node-by-address`: Get node information by address
- `f5-ltm-get-pool-by-node`: Get pool information by node


## F5 Silverline

**Type:** integration  
**Product:** F5 Silverline  

F5 Silverline Threat Intelligence is a cloud-based service incorporating external IP reputation and reducing threat-based communications. By identifying IP addresses and security categories associated with malicious activity, this managed service integrates dynamic lists of threatening IP addresses with the Silverline cloud-based platform, adding context-based security to policy decisions

**Commands:**

- `f5-silverline-ip-objects-list`: Gets a dynamic list of threatening IP addresses by the given list type.
- `f5-silverline-ip-object-add`: Adds a new particular threatening IP address object by its IP address.
- `f5-silverline-ip-object-delete`: Deletes an existing particular threatening IP address object by its object ID or by its IP address.


## FailedInstances

**Type:** script  
**Product:** Common Scripts  

Executes a test for all integration instances available and returns a detailed table with information about any failed integration instances. The script runs on all enabled instances, regardless of whether the “Do not use by default in CLI” checkbox is selected


## Farsight DNSDB

**Type:** integration  
**Product:** Farsight DNSDB  

This integration uses Farsight Security’s DNSDB solution to interactively lookup rich, historical DNS information – either as playbook tasks or through API calls in the War Room – to access rdata and rrset records

**Commands:**

- `dnsdb-rdata`: Lookup rdata records
- `dnsdb-rrset`: Lookup rrser records


## Farsight DNSDB v2

**Type:** integration  
**Product:** Farsight DNSDB  

Farsight Security DNSDB® is the world’s largest DNS intelligence database that provides a unique, fact-based, multifaceted view of the configuration of the global Internet infrastructure. DNSDB leverages the richness of Farsight’s Security Information Exchange (SIE) data-sharing platform and is engineered and operated by leading DNS experts. Farsight collects Passive DNS data from its global sensor array. It then filters and verifies the DNS transactions before inserting them into the DNSDB, along with ICANN-sponsored zone file access download data. The end result is the highest-quality and most comprehensive DNS intelligence data service of its kind - with more than 100 billion DNS records since 2010. This integration uses Farsight Security’s DNSDB solution to interactively lookup rich, historical DNS information – either as playbook tasks or through API calls in the War Room – to access rdata and rrset records. It was integrated and tested with version 2 of the DNSDB API

**Commands:**

- `dnsdb-flex`: DNSDB flex search
- `dnsdb-rdata`: Lookup RData records
- `dnsdb-summarize-rdata`: Summarize RData records
- `dnsdb-rrset`: Lookup RRset records
- `dnsdb-summarize-rrset`: Lookup RRset records
- `dnsdb-rate-limit`: Retrieve service limits


## FeedIntegrationErrorWidget

**Type:** script  
**Product:** Common Widgets  

Returns a table widget of enabled feed integration instances that errors out on indicators fetch


## FeedRelatedIndicatorsWidget

**Type:** script  
**Product:** Common Scripts  

Widget script to view information about the relationship between an indicator, entity and other indicators and connect to indicators, if relevant. The script will be used in the Feed Related Indicators section in the indicators layouts


## Fidelis EDR

**Type:** integration  
**Product:** Fidelis Endpoint  
**Commands:**

- `fidelis-endpoint-list-alerts`: Returns all alerts in the system.
- `fidelis-endpoint-host-info`: Searches for endpoints based on an IP address or hostname.
- `fidelis-endpoint-file-search`: Searches for files on multiple hosts, using file hash, file extension, file size, and other search criteria.
- `fidelis-endpoint-file-search-status`: Gets the file search job status.
- `fidelis-endpoint-file-search-result-metadata`: Gets the job results metadata. The maximum is 50 results.
- `fidelis-endpoint-get-file`: Gets the file stream and download the file.
- `fidelis-endpoint-delete-file-search-job`: Removes the job to free up space on the server.
- `fidelis-endpoint-list-scripts`: Gets a list of all script packages.
- `fidelis-endpoint-get-script-manifest`: Gets the script manifest.
- `fidelis-endpoint-list-processes`: Gets a list all processes according to the OS system.
- `fidelis-endpoint-get-script-result`: Gets script job results.
- `fidelis-endpoint-kill-process`: Terminates the process that matches the required parameter's process ID.
- `fidelis-endpoint-delete-file`: Deletes a file at the specified path.
- `fidelis-endpoint-isolate-network`: Quarantines an endpoint. While isolated, the endpoint's network communication is restricted to only the allowed servers.
- `fidelis-endpoint-remove-network-isolation`: Removes the endpoint from isolation.


## File Analysis - ReversingLabs A1000

**Type:** playbook  
**Product:** ReversingLabs A1000  

Upload sample to ReversingLabs A1000 appliance and automatically retrieve full & classification reports. Calculate final classification

**Inputs:**

- `EntryID`: The Entry ID.
- `hash`: SHA1 hash of the file.


## File Enrichment - OrionMalware

**Type:** playbook  
**Product:** OrionMalware  

Get file information using the OrionMalware API integration

**Inputs:**

- `FileHash`: hash to be checked against OrionMalware database


## File Enrichment - VMRay

**Type:** playbook  
**Product:** VMRay Analyzer  

Get file information using the VMRay integration

**Inputs:**

- `MD5`: File MD5 to enrich
- `SHA256`: File SHA256 to enrich
- `SHA1`: File SHA1 to enrich


## file-enrichment

**Type:** script  
**Product:** Aggregated Scripts  

Enriches File indicators with reputation data from multiple integrations and outputs a consolidated FileEnrichment object. This script exclusively supports indicators of type File and will automatically create the indicator in TIM if it is not already exists. Note: The script runs core-get-hash-analytics-prevalence on SHA256 values only. Note: This script is supported in the platform.0 and later, and in Cortex XSIAM

**Inputs:**

- `file_hash`: A comma-separated list of File hashes to enrich. Supported types are: MD5, SHA1, SHA256, and SHA512.
- `external_enrichment`: "Whether to call external integrations for enrichment:- 'true': enrich using all enabled integrations (e.g., VirusTotal (API v3), AlienVault
- `verbose`: Retrieve a human-readable entry for each command; if false, only the final result is summarized.
- `brands`: A list of integration brands to run enrichment against. Example: `"AlienVault OTX v2", "WildFire-v2"`. - If provided, only the selected bran
- `additional_fields`: When set to true, the output includes an `AdditionalFields` objectfor each of the indicator results. `AdditionalFields` contains all fields 


## FileCreateAndUpload

**Type:** script  
**Product:** Common Scripts  

Creates a file using the given data input or entry ID, and uploads it to the current investigation's War Room

**Inputs:**

- `filename`: The name of the file to be created.
- `data`: The input data to write to file.
- `entryId`: The entry ID contents to write into file.


## FileCreateAndUploadV2

**Type:** script  
**Product:** Common Scripts  

Creates a file (using the given data input or entry ID) and uploads it to the current investigation War Room

**Inputs:**

- `filename`: The name of the file to be created.
- `data`: Input data to write to the file.
- `entryId`: Entry ID contents to write in the file.
- `data_encoding`: Encoding type of the input data or contents.


## FileOrbis

**Type:** integration  
**Product:** FileOrbis  

Manage FileOrbis operations. This integration was integrated and tested with version >10.0.0 of FileOrbis (You should see platform settings on management)

**Commands:**

- `fileorbis-change-user-status`: Changes user status


## FileReputation

**Type:** script  
**Product:** Common Scripts  

A context script for hash entities

**Inputs:**

- `file`: The file hash to look up. This supports, "MD5", "SHA1" and "SHA256".


## FileToBase64List

**Type:** script  
**Product:** Common Scripts  

Encode a file as base64 and store it in a platform list

**Inputs:**

- `entryId`: The file entry ID.
- `listName`: The list name in which to store the file. The list must exist in platform.
- `zipFile`: Whether to zip the file before storing it in the list.


## Find Detection State and Expire Inactive Detections - Vectra RUX

**Type:** playbook  
**Product:** Vectra RUX  

This playbook identifies the detection states of incidents and updates the investigation status of inactive detections to "expired"

**Inputs:**

- `incident_type`: The platform incident type to search for inactive detections. Default is 'Vectra RUX Events Detection'.


## FireEye Central Management

**Type:** integration  
**Product:** FireEye Central Management  

FireEye Central Management (CM Series) is the FireEye threat intelligence hub. It services the FireEye ecosystem, ensuring that FireEye products share the latest intelligence and correlate across attack vectors to detect and prevent cyber attacks This integration was integrated and tested with version 9.0.2 of FireEye Central Management

**Commands:**

- `fireeye-cm-get-alerts`: Searches and retrieves FireEye CM alerts based on several filters.
- `fireeye-cm-get-alert-details`: Searches and retrieves the details of a single alert.
- `fireeye-cm-alert-acknowledge`: Confirms that the alert has been reviewed.
- `fireeye-cm-get-artifacts-by-uuid`: Downloads malware artifacts data for the specified UUID as a zip file.
- `fireeye-cm-get-artifacts-metadata-by-uuid`: Gets artifacts metadata for the specified UUID.
- `fireeye-cm-get-events`: Retrieves information about existing IPS NX events. An IPS enabled appliance is a prerequisite to be able to retrieve IPS event data.
- `fireeye-cm-get-quarantined-emails`: Searches and retrieves quarantined emails.
- `fireeye-cm-release-quarantined-emails`: Releases and deletes quarantined emails. This is not available when Email Security is in Drop mode.
- `fireeye-cm-delete-quarantined-emails`: Deletes quarantined emails. This is not available when Email Security is in Drop mode.
- `fireeye-cm-download-quarantined-emails`: Download quarantined emails.
- `fireeye-cm-get-reports`: Returns reports on selected alerts.


## FireEye Endpoint Security (HX) v2

**Type:** integration  
**Product:** FireEye HX  

FireEye Endpoint Security is an integrated solution that detects what others miss and protects endpoint against known and unknown threats. This integration provides access to information about endpoints, acquisitions, alerts, indicators, and containment. Customers can extract critical data and effectively operate security operations automated playbook Some changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

**Commands:**

- `fireeye-hx-get-host-information`: Returns information on a host associated with an agent.
- `fireeye-hx-get-all-hosts-information`: Returns information on all hosts.
- `fireeye-hx-host-containment`: Applies containment for a specific host, so that it no longer has access to other systems. If the user does not have the necessary permissions, the command will
- `fireeye-hx-cancel-containment`: Releases a specific host from containment.
- `fireeye-hx-initiate-data-acquisition`: Initiates a data acquisition process to collect artifacts from the system disk and memory.
- `fireeye-hx-get-host-set-information`: Returns a list of all host sets known to your HX Series appliance.
- `fireeye-hx-list-policy`: Returns a list of all policies.
- `fireeye-hx-list-host-set-policy`: Returns a list of all policies for all host sets.
- `fireeye-hx-list-containment`: Fetches all containment states across known hosts.
- `fireeye-hx-search-list`: Fetches all enterprise searches.
- `fireeye-hx-search-stop`: Stops a specific running search.
- `fireeye-hx-search-result-get`: Fetches the results for a specific enterprise search.
- `fireeye-hx-search`: Searches endpoints to check all hosts or a subset of hosts for a specific file or indicator.
- `fireeye-hx-get-alert`: Get details of a specific alert.
- `fireeye-hx-suppress-alert`: Suppresses an alert by ID.


## FireEye Helix

**Type:** integration  
**Product:** FireEye Helix  

Use the FireEye Helix integration to integrate security tools and arguments with next-generation SIEM, orchestration and threat intelligence tools such as alert management, search, analysis, investigations and reporting. In order to configure this integration you must have a FireEye customer ID. Your customer ID will placed in the FireEye Helix URL of your FireEye Helix app after /helix/id/. e.g. for the following URL  the customer ID is "helixid". The API key can be found and generated in the API KEYS section. You can navigate to it from your FireEye Helix app home page by clicking on the user icon on the top right, and choosing HELIX Settings. You'll be redirected to the HELIX Settings page, where API KEYS can be found

**Commands:**

- `fireeye-helix-list-alerts`: Returns all alerts.
- `fireeye-helix-get-alert-by-id`: Returns alert details, by alert ID.
- `fireeye-helix-alert-create-note`: Creates an alert note.
- `fireeye-helix-get-events-by-alert`: Lists events alerts for a specific alert.
- `fireeye-helix-get-endpoints-by-alert`: Retrieves a specific alert from an helix endpoint.
- `fireeye-helix-get-cases-by-alert`: Returns cases of an alert.
- `fireeye-helix-get-lists`: Returns lists.
- `fireeye-helix-get-list-by-id`: Returns a specific list by list ID.
- `fireeye-helix-create-list`: Creates a list.
- `fireeye-helix-update-list`: Updates an existing list.
- `fireeye-helix-delete-list`: Deletes a single list by list ID.
- `fireeye-helix-list-sensors`: Fetches all sensors.
- `fireeye-helix-list-rules`: Returns all rules.
- `fireeye-helix-edit-rule`: Modifies an existing rule.
- `fireeye-helix-alert-get-notes`: Returns all notes related to an alert.


## FireEye Helix Archive Search

**Type:** playbook  
**Product:** FireEye Helix  

Creates an archive search in FireEye Helix, and fetch the results as events

**Inputs:**

- `Query`: The query to execute. This is the search clause in an MQL.
- `Start`: The start time of the event in date format yyyy-mm-dd or yyyy-mm.
- `Offset`: The offset of the result.
- `Groupby`: The unique values for the specified field. This input groups them together based on the specified frequency. For example, groupby="srcipv4 5
- `Sort_by`: Sorts the results by this field. The default is descending order. To change the default, the following command must be used: argument sort_o
- `Sort_order`: Controls the order of the results sorted by the sort_by argument. Can be, "ascending" or "descending".
- `Limit`: The number of events for which to search.
- `Timeout`: The amount of time for which to poll before declaring a timeout and resuming the playbook (in minutes).


## FireEyeApiModule

**Type:** script  

The FireEye API handles the API Key generation from the user/password authentication. To use the common FireEye API logic, attach the from FireEyeApiModule import * # noqa: E402 line of code in the following location to import it. After you import the module, the FireEyeClient will be available for use. For examples, see the FireEye Central Management integration


## FireEyeDetonateFile

**Type:** script  
**Product:** FireEye (AX Series)  

Detonates a file or URL through FireEye

**Inputs:**

- `file`: The file/entry ID to detonate.
- `profiles`: The FireEye profiles to use (comma-separated).
- `analysistype`: Specifies live or sandbox analysis mode. "Sandbox", analyzes suspected malware objects in a closed, protected environment. "Live", analyzes 
- `prefetch`: Whether to determine the file target based on an internal determination rather than browsing to the target location. Can be, "No" or "Yes".


## FireMon Pre Change Assessment

**Type:** playbook  
**Product:** FireMon Security Manager  

Validates and Return Pre Changes Assessment on Rules added as Requirement

**Inputs:**

- `domain_id`: Enter Domain Id (Integer)
- `device_group_id`: Enter Device Group Id (Integer)
- `destinations`: Enter List of Destinations
- `sources`: Enter List of Sources
- `services`: Enter List of Services
- `action`: Select an Action


## FireMon Security Manager

**Type:** integration  
**Product:** FireMon Security Manager  

FireMon Security Manager delivers comprehensive rule lifecycle management to help you manage and automate every stage of the change management process. Workflows can be customized and automated to conform to your security goals and standards, with tools at your disposal to evolve policy and protection over time

**Commands:**

- `firemon-user-authentication`: Returns authentication token
- `firemon-create-pp-ticket`: Creates a ticket in policy planner application
- `firemon-pca`: PCA- Pre-Change Assessment is process of showing impact of created devices changes in early stages before implementing changes to devices. We can check the PCA 
- `firemon-secmgr-secrule-search`: Searches for security rules using the SIQL language query (limit to 10k)


## FirstArrayElement

**Type:** script  
**Product:** Filters And Transformers  

Returns the first element of an array. If the value passed is not an array, it returns the original value that was passed

**Inputs:**

- `value`: An array for which to return the first element.


## Flashpoint Ignite

**Type:** integration  
**Product:** Flashpoint  

Use the Flashpoint Ignite integration to reduce business risk. Ignite allows users to ingest alerts and compromised credentials as incident alerts and executes commands such as search intelligence report, ip, url, get events, and more. This integration was integrated and tested with API v1 of Ignite. Both incident types Ignite Alert and Flashpoint Compromised Credentials support the auto extraction feature by default. This feature extracts indicators and enriches their reputations using commands and scripts defined for the indicator type (Refer to Indicator extraction (the platform.13) or Indicator extraction (the platform.7 On-prem) for more details). If you are upgrading from a Flashpoint integration, please refer to the Migration Guide for guidance

**Commands:**

- `flashpoint-ignite-intelligence-report-search`: Search for the Intelligence Reports using a keyword.
- `flashpoint-ignite-compromised-credentials-list`: Retrieves the compromised credentials based on the filter values provided in the command arguments.
- `flashpoint-ignite-event-list`: Searches for events within the specified time period, the Flashpoint report ID, or attack IDs.
- `flashpoint-ignite-event-get`: Retrieves the details of a single event using event FPID or UUID.
- `flashpoint-ignite-intelligence-report-get`: Get single report details using the report id.
- `flashpoint-ignite-intelligence-related-report-list`: List related reports for a particular report using the report ID.
- `flashpoint-ignite-alert-list`: Retrieves a list of alerts based on the filter values provided in the command arguments.
- `email`: Looks up the "Email" type indicator details. The reputation of Email is considered malicious if there's at least one IoC event in the Ignite database matching t
- `filename`: Looks up the "Filename" type indicator details. The reputation of Filename is considered malicious if there's at least one IoC event in the Ignite database matc
- `ip`: Looks up the "IP" type indicator details. The reputation of the IP address is decided from the indicator score if it is found in the Ignite IOC database. Altern
- `flashpoint-ignite-common-lookup`: Looks up details for indicators of types: "URL", "Domain", "File Hash", and "IP". The reputation of the indicator is decided from the indicator score if it is f
- `flashpoint-ignite-indicator-get`: Looks up details for indicators of types "URL", "Domain", "File Hash", and "IP" using their ID. The reputation of the indicator is decided from the indicator sc
- `url`: Looks up the "URL" type indicator details. The reputation of the URL is decided from the indicator score if it is found in the Ignite IOC database.
- `domain`: Looks up the "Domain" type indicator details. The reputation of the domain is decided from the indicator score if it is found in the Ignite IOC database.
- `file`: Looks up the "File" type indicator details. The reputation of the file is decided from the indicator score if it is found in the Ignite IOC database.


## FlashpointCreateThreatIntelReport

**Type:** script  
**Product:** Flashpoint  

Retrieves an Ignite intelligence report and creates the corresponding Executive Brief Threat Intel Report

**Inputs:**

- `report_id`: The ID of the Ignite report from which the Threat Intel Report is to be created.Note: The report ID can be retrieved from the output context


## FlashpointReportDetails

**Type:** script  
**Product:** Flashpoint  

Retrieves the full information of the report

**Inputs:**

- `report_id`: The ID of the report for which the details are to be fetched.Note: If not provided, the script will try to retrieve it from the incident con


## FlashpointVulnerabilityDetails

**Type:** script  
**Product:** Flashpoint  

Retrieves the CVE information for vulnerabilities present in the incident and updates the vulnerability details in the incident data


## Forcepoint Security Management Center

**Type:** integration  
**Product:** Forcepoint Security Management Center  

Forcepoint SMC provides unified, centralized management of all models of Forcepoint engines whether physical, virtual or cloud—across large, geographically distributed enterprise environments. This integration was integrated and tested with version 6.10 of Forcepoint Security Management Center

**Commands:**

- `forcepoint-smc-ip-list-create`: Creates an IP list.
- `forcepoint-smc-ip-list-update`: Updates an IP list.
- `forcepoint-smc-ip-list-list`: Lists the IP Lists in the system.
- `forcepoint-smc-ip-list-delete`: Deletes an IP list.
- `forcepoint-smc-host-list`: Lists the hosts in the system.
- `forcepoint-smc-host-create`: Creates a new host.
- `forcepoint-smc-host-update`: Updates a host.
- `forcepoint-smc-host-delete`: Deletes a host.
- `forcepoint-smc-domain-create`: Creates a new domain.
- `forcepoint-smc-domain-list`: Lists the domains in the system.
- `forcepoint-smc-domain-delete`: Deletes a domain.
- `forcepoint-smc-policy-template-list`: Lists the policy templates in the system.
- `forcepoint-smc-firewall-policy-list`: Lists the firewall policies in the system.
- `forcepoint-smc-firewall-policy-create`: Creates a firewall policy.
- `forcepoint-smc-firewall-policy-delete`: Deletes a firewall policy.


## Forescout EyeInspect

**Type:** integration  
**Product:** Forescout EyeInspect  
**Commands:**

- `forescout-ei-host-list`: Retrieves information about the hosts in the eyeInspect CC database.
- `forescout-ei-link-list`: Retrieves information about the links in the eyeInspect CC database.
- `forescout-ei-vulnerability-info-get`: Retrieves information about a specific vulnerability stored in the eyeInspect CC database.
- `forescout-ei-alert-list`: Retrieves information about the alerts inside eyeInspect CC.
- `forescout-ei-alert-pcap-get`: Retrieves the PCAP file associated to a given alert.
- `forescout-ei-sensor-list`: Retrieves information about the sensors associated to the eyeInspect CC.
- `forescout-ei-sensor-module-list`: Retrieves information about the modules of the specified sensor.
- `forescout-ei-sensor-module-update`: Changes the specified properties of the specified module.
- `forescout-ei-sensor-module-delete`: Deletes the specified module from the specified sensor and from the eyeInspect CC database.


## ForescoutEyeInspectButtonGetVulnerabilityInfo

**Type:** script  
**Product:** Forescout EyeInspect  

Get information of a CVE from Forescout EyeInspect CVEs DB

**Inputs:**

- `cve_id`: The unique ID of the vulnerability information record to be retrieved. The CVE ID can be retrieved from public vulnerability databases, such


## ForescoutEyeInspectButtonHostChangeLog

**Type:** script  
**Product:** Forescout EyeInspect  

Get change log of Forescout EyeInspect hosts


## Fortanix DSM

**Type:** integration  
**Product:** Fortanix DSM  

Manage Secrets and Protect Confidential Data using Fortanix Data Security Manager (DSM)

**Commands:**

- `fortanix-list-secrets`: List secrets from one or more specified group(s)
- `fortanix-get-secret-metadata`: Get the secret metadata without exposing its value
- `fortanix-fetch-secret`: Retrieve the secret value
- `fortanix-new-secret`: Import a new secret
- `fortanix-rotate-secret`: Update an existing secret, which will be rotated
- `fortanix-delete-secret`: Delete the secret
- `fortanix-invoke-plugin`: Invoke a Fortanix Plugin that is executed in a Confidential Computing enclave
- `fortanix-encrypt`: Protects data using key configured in Fortanix DSM
- `fortanix-decrypt`: Reveal data using key configured in Fortanix DSM


## FortiAuthenticator

**Type:** integration  
**Product:** FortiAuthenticator  

FortiAuthenticator provides centralized authentication services. Seamless secure two-factor/OTP authentication across the organization in conjunction with FortiToken. This integration was integrated and tested with versions 4.0 - 6.3.0 of FortiAuthenticator

**Commands:**

- `fortiauthenticator-get-user`: 
- `fortiauthenticator-update-user`: 


## FortiGate

**Type:** integration  
**Product:** FortiGate  

FortiGate provides flawless convergence that can scale to any location: remote office, branch, campus, data center, and cloud. FortiGate always delivered on the concept of hybrid mesh firewalls with FortiManager for unified management and consistent security across complex hybrid environments. The Fortinet FortiOS operating system provides deep visibility and security across a variety of form factors. This integration was integrated and tested with version 7.2.5 of FortiGate

**Commands:**

- `fortigate-list-firewall-address-ipv4s`: Retrieve firewall IPv4 addresses. Addresses define sources and destinations of network traffic and can be used in many functions such as firewall policies, ZTNA
- `fortigate-create-firewall-address-ipv4`: Create firewall IPv4 addresses. Addresses define sources and destinations of network traffic and can be used in many functions such as firewall policies, ZTNA, 


## FortiMail

**Type:** integration  
**Product:** Fortimail  

FortiMail is a comprehensive email security solution by Fortinet, offering advanced threat protection, data loss prevention, encryption, and email authentication to safeguard organizations against email-based cyber threats and protect sensitive information. This integration was integrated and tested with version 7.4 of fortimail

**Commands:**

- `fortimail-ip-group-create`: Create an IP group. IP group is a container that contains members of IP address that can be used when configuring access control rules (define the source IP gro
- `fortimail-ip-group-update`: Update the comment of an IP group.
- `fortimail-ip-group-delete`: Delete an IP group.
- `fortimail-ip-group-list`: List IP groups. if a name is given, the command will return the information about the specified IP group.
- `fortimail-ip-group-member-add`: Add an IP group member (IP/Netmask or IP range) to an IP group. An IP group member is an IP address that can be used when configuring access control rules (defi
- `fortimail-ip-group-member-replace`: Replace IP group members with new members. This command overwrites all the IP group members that was defined in the IP group.
- `fortimail-ip-group-member-delete`: Delete an IP group member from IP group.
- `fortimail-ip-group-member-list`: List IP group members. If an ip is given, the command will return the information about the specified IP group member.
- `fortimail-email-group-create`: Create an email group. An email group is a container for a list of email addresses, allowing you to use it in configuring access control rules (for defining the
- `fortimail-email-group-update`: Update the comment of an email group.
- `fortimail-email-group-delete`: Delete an email group.
- `fortimail-email-group-list`: List email groups. If a name is given, the command will return the information about the specified email group.
- `fortimail-email-group-member-add`: Add an email group member (email address) to an email group.
- `fortimail-email-group-member-replace`: Replace email group members with new members. This command overwrites all the email group members that were defined in the email group.
- `fortimail-email-group-member-delete`: Delete an email group member from an email group.


## FortiManager

**Type:** integration  
**Product:** FortiManager  

FortiManager is a single console central management system that manages Fortinet Devices. This integration was integrated and tested with version 6.2.2 of FortiManager

**Commands:**

- `fortimanager-devices-list`: List all devices in the ADOM instance.
- `fortimanager-device-groups-list`: List ADOM device groups.
- `fortimanager-address-list`: List ADOM firewall IPv4 addresses.
- `fortimanager-address-create`: Add a new IPv4 address.
- `fortimanager-address-update`: Add a new IPv4 address.
- `fortimanager-address-delete`: Delete an address.
- `fortimanager-address-group-list`: List ADOM IPv4 address groups.
- `fortimanager-address-group-create`: Create a new address group.
- `fortimanager-address-group-update`: Create a new address group.
- `fortimanager-address-group-delete`: Delete an address group.
- `fortimanager-service-categories-list`: List the ADOM service categories.
- `fortimanager-service-group-list`: List ADOM service groups.
- `fortimanager-service-group-create`: Creates a new service group.
- `fortimanager-service-group-update`: Create a new service group.
- `fortimanager-service-group-delete`: Delete a service group


## FortiSandbox - Loop for Job Submissions

**Type:** playbook  
**Product:** FortiSandbox  

Playbook used to retrieve job id for submissions of fortisandbox using the submission id

**Inputs:**

- `SubmissionIDs`: 


## FortiSandbox - Loop For Job Verdict

**Type:** playbook  
**Product:** FortiSandbox  

Playbook used to retrieve the verdict for a specific job id for a sample submitted to FortiSandbox

**Inputs:**

- `JobIds`: Job ID to get verdicts on


## FortiSandbox - Upload Multiple Files

**Type:** playbook  
**Product:** FortiSandbox  

Playbook used to upload files to FortiSandbox

**Inputs:**

- `FileEntryID`: 
- `FileSHA256`: 
- `ArchivePassword`: 
- `VM-CSV-List`: 
- `MalkPkg`: Default is 0
- `SkipSteps`: 


## FortiSandbox v2

**Type:** integration  
**Product:** FortiSandbox  

FortiSandbox is an advanced security tool that goes beyond standard sandboxing. It combines proactive mitigation, enhanced threat detection, and in-depth reporting, using Fortinet's dynamic antivirus technology, dual-level sandboxing, and FortiGuard cloud integration to counter advanced threats. It effectively detects viruses, Advanced Persistent Threats (APTs), and malicious URLs, integrating seamlessly with existing Fortinet devices like FortiGate and FortiMail for comprehensive network protection. This integration was integrated and tested with version 4.4.3 of FortiSandboxv2. Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `file`: Runs reputation on files.
- `url`: Runs reputation on URLs.
- `fortisandbox-submission-file-upload`: Scheduled command to upload any file type to be sandboxed. The system swiftly identifies and mitigates threats in files.


## Fortiweb VM

**Type:** integration  
**Product:** Fortinet Fortiweb  

Fortiweb VM integration allows to manage WAF policies and block cookies, URLs, and host names. This integration was integrated and tested with version 1 & 2 of fortiweb_vm

**Commands:**

- `fortiwebvm-protected-hostname-group-create`: Create protected host name group.
- `fortiwebvm-protected-hostname-group-update`: Update protected host name group.
- `fortiwebvm-protected-hostname-group-list`: List the Protected host name group.
- `fortiwebvm-protected-hostname-member-create`: Create protected host name member.
- `fortiwebvm-protected-hostname-member-update`: Update a protected host name member.
- `fortiwebvm-protected-hostname-member-list`: List all the protected host name members.
- `fortiwebvm-protected-hostname-member-delete`: Delete protected host name member.
- `fortiwebvm-protected-hostname-group-delete`: Delete a protected host name.
- `fortiwebvm-ip-list-group-create`: Create IP List.
- `fortiwebvm-ip-list-group-update`: Update an IP list.
- `fortiwebvm-ip-list-group-list`: Supports API versions 1 & 2.
- `fortiwebvm-ip-list-member-create`: Create an IP list member. Supports API versions 1 & 2.
- `fortiwebvm-ip-list-member-update`: Update IP list policy member.
- `fortiwebvm-ip-list-member-list`: List the IP list policy members.
- `fortiwebvm-ip-list-member-delete`: Delete an IP list policy member.


## FPDeleteRule

**Type:** script  
**Product:** Forcepoint Web Security  

Generates a password and allows various parameters to customize the properties of the password depending on the use case. For example, password complexity requirements. The default behavior is to generate a password of random length including all four character classes (upper, lower, digits, symbols) with at least five and at most ten characters per class. The min_* values all default to 0. This means that if the command is executed in this way: !GeneratePassword max_lcase=10. It is possible that a password of length zero could be generated. It is therefore recommended to always include a min_* parameter that matches. The debug parameter will print certain properties of the command into the War Room for easy diagnostics

**Inputs:**

- `min_lcase`: The minimum number of lower case characters to include in password.
- `max_lcase`: The maximum number of lower case characters to include in password.
- `min_ucase`: The minimum number of upper case characters to include in password.
- `max_ucase`: The maximum number of upper case characters to include in password.
- `min_digits`: The minimum number of digits to include in password.
- `max_digits`: The maximum number of digits to include in password.
- `min_symbols`: The minimum number of symbols to include in password.
- `max_symbols`: The maximum number of symbols to include in password.


## FPSetRule

**Type:** script  
**Product:** Forcepoint Web Security  

Adds (or updates an existing) rule in Forcepoint Triton. Preserves orders of rules and modifies policy in-place if a rule exists with the exact type and value

**Inputs:**

- `policy`: The policy/action assigned to the rule. Can be, "allow" or "deny" only.
- `type`: The Triton rule type. Can be, "dest_domain", "dest_ip", "dest_host" or "url_regex".
- `value`: The value to match for this rule. Can be, "domain", "regex", etc... depending on the type.
- `remoteaccessname`: If the Forcepoint Triton instance is configured as a RemoteAccess integration instance ‐ insert its name here. Replaces argument "tritonsyst
- `tritonsystem`: The system name of the linux host on which Forcepoint Triton is installed. Only use this if it is not working with Triton as a RemoteAccess 


## FraudWatch

**Type:** integration  
**Product:** FraudWatch PhishPortal  

Manage incidents via the Fraudwatch API. FraudWatch International provides a fully managed Enterprise Digital Brand Protection Suite, including online brand management & monitoring as well as providing other brand protection solutions that protect organizations and their customers around the world against online brand-related abuse. This integration was integrated and tested with version v1 of FraudWatch Phishportal

**Commands:**

- `fraudwatch-incidents-list`: Get a list of incidents from FraudWatch service.
- `fraudwatch-incident-report`: Report an incident to FraudWatch service.
- `fraudwatch-incident-update`: Updates the incident associated with the 'incident_id' with the specified argument values.
- `fraudwatch-incident-get-by-identifier`: Gets an incident from FraudWatch service by its reference ID or incident ID. Single values of 'reference_id' and 'incident_id' should be specified.
- `fraudwatch-incident-forensic-get`: Gets the forensic data of the incident associated with the specified incident ID.
- `fraudwatch-incident-contact-emails-list`: Provides a list of the messages related to the incident associated with the specified incident ID.
- `fraudwatch-incident-messages-add`: Add a new related message to the incident associated with the specified incident ID.
- `fraudwatch-incident-urls-add`: Adds additional URLs to the incident associated with the specified incident ID. Fails if one of the new urls already exists.
- `fraudwatch-incident-attachment-upload`: Adds a new file attachment to the incident associated with the specified incident ID.
- `fraudwatch-brands-list`: Gets a list of brands from FraudWatch service.


## Freshworks Freshservice

**Type:** integration  
**Product:** Freshworks Freshservice  

Freshservice is a service management solution that allows customers to manage service requests, incidents, change requests tasks, and problem investigation. This integration was integrated and tested with version 2 of FreshworksFreshservice

**Commands:**

- `freshservice-ticket-list`: Retrieve all existing tickets or a specific ticket by specifying the ticket ID. By default, only tickets that have been created within the past 30 days will be 
- `freshservice-ticket-create`: Create a new Ticket at the service desk. The default Ticket type is incident. Create ticket required one of the following: requester_id, phone, email. Ticket ty
- `freshservice-ticket-update`: Update an existing Ticket in Freshservice.
- `freshservice-ticket-delete`: Delete an existing Ticket in Freshservice.
- `freshservice-ticket-task-list`: Retrieve tasks list (or a specific task) on a Ticket with the given ID from Freshservice.
- `freshservice-ticket-task-create`: Create a new task on a Ticket request in Freshservice.
- `freshservice-ticket-task-update`: Update an existing task on an existing Ticket in Freshservice.
- `freshservice-ticket-task-delete`: Delete the task on a Ticket with the given ID from Freshservice.
- `freshservice-ticket-conversation-list`: Retrieve all Conversations of a Ticket. Conversations consist of replies as well as public and private notes added to a ticket. Notes are non-invasive ways of s
- `freshservice-ticket-conversation-reply-create`: Create a new reply for an existing Ticket Conversation.
- `freshservice-ticket-conversation-note-create`: Create a new note for an existing Ticket Conversation.
- `freshservice-ticket-conversation-update`: Update an existing Conversation on an existing Ticket in Freshservice.
- `freshservice-ticket-conversation-delete`: Delete the Conversation on a Ticket with the given ID from Freshservice.
- `freshservice-problem-list`: Retrieve a list of all Problems or a specific problem with the given ID from Freshservice.
- `freshservice-problem-create`: Create a new problem request in Freshservice. Creating a problem required one of the following- requester_id or email.


## FTP

**Type:** integration  
**Product:** FTP  

FTP integration to download or upload files to a remote FTP server. Please note that FTP transfer is insecure. Please use it with care

**Commands:**

- `ftp-ls`: List all the files under the current folder.
- `ftp-put`: Upload file to FTP server.
- `ftp-get`: Download file from FTP server.


## G Suite Auditor

**Type:** integration  
**Product:** GsuiteAuditor  

G Suite Auditor is an integration that receives audit logs from G Suite's different applications - admin, drive, calendar, and more

**Commands:**

- `gsuite-activity-search`: Retrieves a list of activities for a specific customer's account and application.


## G Suite Security Alert Center

**Type:** integration  
**Product:** G Suite Security Alert Center  

G Suite Security Alert Center allows users to fetch different alert types such as Suspicious login, Device compromised, Leaked password, and more. Users can delete or recover a single alert or a batch of alerts and retrieve the alert's metadata. This integration allows users to provide feedback for alerts and fetch existing feedback for a particular alert. This integration was integrated and tested with version v1beta1 dated Oct 15, 2018 of Google Workspace Alert Center. Supported the platform.0.0 and later

**Commands:**

- `gsac-alert-list`: Lists the alerts. Use the filter to filter the list by various alert types. Note: The alerts that have been marked for deletion in the past 30 days will still b
- `gsac-alert-get`: Gets the specified alert. Note: To get the alert_id, execute the gsac-alert-list command.
- `gsac-alert-feedback-create`: Creates new feedback for an alert.
- `gsac-alert-feedback-list`: Lists all the feedback for an alert.
- `gsac-alert-delete`: Performs delete operation on alerts. Note: The alerts that are marked for deletion will be removed from the Alert Center after 30 days.
- `gsac-alert-recover`: Performs a recover operation on alerts. Note: Recovers the alerts that were marked for deletion within the past 30 days.


## Gamma

**Type:** integration  
**Product:** Gamma  

Gamma Enterprise DLP provides 1-click automatic discovery and remediation of data loss instances across enterprise sanctioned SaaS applications (cloud and on-prem) such as: Slack, Github, GSuite (Gmail, GDrive), Atlassian Suite (Jira, Confluence), Microsoft Office 365 (Outlook, Teams, OneDrive), ServiceNow, ZenDesk and many more

**Commands:**

- `gamma-get-violation-list`: Fetch DLP violations found across SaaS applications monitored by Gamma
- `gamma-get-violation`: Fetches a single DLP violation. This command is the same as gamma-get-violation-list except that this command only returns the DLP violation details of the give
- `gamma-update-violation`: Updates a DLP violation status in Gamma


## GatewatcherAlertEngine

**Type:** script  
**Product:** Gatewatcher AionIQ  

Automation script for displaying engine fields on the Alert layout


## GCenter

**Type:** integration  
**Product:** Gatewatcher AionIQ  

This integration allows, via about twenty commands, to interact with the GCenter appliance via its API. This integration was integrated and tested with version v2.5.3.102 of GCenter. To simplify GCenter v2.5.3.102 is called GCenter in the Pack

**Commands:**

- `gw-get-alert`: Get an alert by it's uid
- `gw-es-query`: Get Elasticsearch data
- `gw-add-malcore-list-entry`: Add malcore whitelist/blacklist entry
- `gw-del-malcore-list-entry`: Delete malcore whitelist/blacklist entry
- `gw-add-dga-list-entry`: Add dga whitelist/blacklist entry
- `gw-del-dga-list-entry`: Delete dga whitelist/blacklist entry
- `gw-add-ignore-asset-name`: Ignore asset name
- `gw-add-ignore-kuser-ip`: Ignore kuser IP
- `gw-add-ignore-kuser-name`: Ignore kuser name
- `gw-add-ignore-mac-address`: Ignore mac address
- `gw-del-ignore-asset-name`: Delete an ignore asset ID
- `gw-del-ignore-kuser-ip`: Delete an ignore kuser IP ID
- `gw-del-ignore-kuser-name`: Delete an ignore kuser name ID
- `gw-del-ignore-mac-address`: Delete an ignore mac address ID
- `gw-send-malware`: Send malware


## GCenter 103

**Type:** integration  
**Product:** Gatewatcher AionIQ  

This integration fetch events generated by the GCenter appliance. This integration was integrated and tested with version 2.5.3.103 of GCenter 103

**Commands:**

- `gcenter103-alerts-list`: List all alerts.
- `gcenter103-alerts-get`: Get an alert with its UUID (corresponds to event.id field) or the GCenter ID of the alert.
- `gcenter103-alerts-note-add`: Add or update a note to an alert.
- `gcenter103-alerts-note-remove`: Delete the note of an alert.
- `gcenter103-alerts-tags-get`: Get the tags of an alert.
- `gcenter103-alerts-tags-add`: Add or update tags of an alert.
- `gcenter103-alerts-tags-remove`: Remove tags from an alert.
- `gcenter103-alerts-status-update`: Update status of an alert.
- `gcenter103-raw-alerts-get`: Get a raw alert with its UUID.
- `gcenter103-raw-alerts-file-get`: Get a file attached to an alert with its UUID.
- `gcenter103-file-scan`: Scan a file on a selected engine. You must upload the file to scan before execution.
- `gcenter103-file-scan-result-get`: Retrieve previous scan by its ID.
- `gcenter103-assets-list`: List all assets.
- `gcenter103-assets-alerts-get`: Retrieve alerts of a given asset.
- `gcenter103-assets-get`: Retrieve specific asset data.


## Gem

**Type:** integration  
**Product:** Gem  

Use Gem alerts as a trigger for the platform, to automate response to specific TTPs

**Commands:**

- `gem-list-threats`: List all threats detected in Gem.
- `gem-get-threat-details`: Get details about a specific threat.
- `gem-get-alert-details`: Get details about a specific alert.
- `gem-list-inventory-resources`: List inventory resources in Gem.
- `gem-get-resource-details`: Get details about a specific resource.
- `gem-list-ips-by-entity`: List all source IP addresses used by an entity in a specific timeframe. The results are sorted by activity volume.
- `gem-list-services-by-entity`: List all services accessed by an entity in a specific timeframe. The results are sorted by activity volume.
- `gem-list-events-by-entity`: List all events performed by an entity in a specific timeframe. The results are sorted by activity volume.
- `gem-list-accessing-entities`: List all entities that accessed an entity in a specific timeframe. The results are sorted by activity volume.
- `gem-list-using-entities`: List all entities that used an entity in a specific timeframe. The results are sorted by activity volume.
- `gem-list-events-on-entity`: List all events performed on an entity in a specific timeframe. The results are sorted by activity volume.
- `gem-list-accessing-ips`: List all source IP addresses that accessed an entity in a specific timeframe. The results are sorted by activity volume.
- `gem-update-threat-status`: Set a threat's status to open, in progress or resolved.
- `gem-run-action`: Run an action on an entity.
- `gem-add-timeline-event`: Add a timeline event to a threat.


## Gem Handle ec2

**Type:** playbook  
**Product:** Gem  

Gem playbook to handle an alert involving an ec2 instance

**Inputs:**

- `User`: Slack user to send message for


## Gem Validate triggering event

**Type:** playbook  
**Product:** Gem  

Get the triggering events of a Gem Alert and send a validation Slack message to the dev team. The response will be added to the Gem Timeline

**Inputs:**

- `User`: Extra Slack user to send validation to


## Generic Export Indicators Service

**Type:** integration  
**Product:** Generic Export Indicators Service  

Use the Generic Export Indicators Service integration to provide an endpoint with a list of indicators as a service for the system indicators. The Generic Export Indicators Service integration is a long-running integration. For more information about long-running integrations, see the the platform, the platform

**Commands:**

- `export-indicators-list-update`: Updates values stored in the List (only available On-Demand).


## Generic MCP

**Type:** integration  
**Product:** Generic MCP  

Use this integration to connect to an MCP server and automatically discover its available tools

**Commands:**

- `generic-mcp-generate-login-url`: Generate an authentication login URL.
- `generic-mcp-auth-test`: Test the authentication configuration with the MCP server.


## Generic SQL

**Type:** integration  
**Product:** GenericSQL  

Generic SQL integration for the Databases: MySQL, PostgreSQL, Microsoft SQL Server, Oracle, Teradata and Trino

**Commands:**

- `query`: Running a sql query
- `sql-command`: Running a sql query


## Genians

**Type:** integration  
**Product:** Genians  

Use the Genian NAC integration to block IP addresses using the assign tag. Genian NAC network sensing technology powered by Device Platform Intelligence (DPI) discovers and presents all detected devices’ business contextual and risk-related information along with their technical information without disturbing existing network infrastructure. The resulting intelligence enhances visibility and allows operators to detect and respond to any non-compliant or compromised devices in real time. With the result of comprehensive network visibility, Genian NAC can ensure compliance from all connected devices by leveraging Virtual In-Line Packet Inspection which operates at Layer 2. This technology has complete control over endpoint device traffic over TCP and UDP by eliminating the need for complex configurations and network changes

**Commands:**

- `genians-assign-ip-tag`: Assigns a tag to the Node specified.
- `genians-unassign-ip-tag`: Removes the tag(s) from the Node specified.


## Get Code42 Employee Information

**Type:** playbook  
**Product:** Code42  

Receives usernames from a Code42 Incydr alert and queries Active Directory for employee and supervisor information, if applicable

**Inputs:**

- `user`: The username to query in Active Directory.
- `incidentid`: The Palo Alto platform incident ID that receives the employee information (optional).


## Get RaDark Detailed Items

**Type:** playbook  
**Product:** KELA RaDark  

Enriches RaDark incident with detailed items


## GitHub

**Type:** integration  
**Product:** GitHub  
**Commands:**

- `GitHub-create-issue`: Deprecated. Use github-create-issue instead.


## GitHub IAM

**Type:** integration  
**Product:** GitHub  

Note: This integration should be used as part of our IAM premium pack. For further details, visit our IAM pack documentation. GitHub Integration consists of a set of API endpoints that enable you to automate provisioning of GitHub organization membership. This integration was integrated and tested with version v2 of GitHub IT Admin. For more information, please refer to the Identity Lifecycle Management article

**Commands:**

- `iam-create-user`: Creates a user.
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Deletes an active user.
- `iam-enable-user`: Create a deprovisioned user.


## Gitlab - Guest user permission change

**Type:** playbook  
**Product:** GitLab  

This playbook investigates a "User Permissions Changed” alert by gathering user and IP information and performs remediation based on the information gathered and received from the user. To link this playbook to the relevant alerts automatically, we recommend using the following filters when configuring the playbook triggers: Alert Source = Correlation AND Alert Name = Gitlab - Permission change from guest to owner Used Sub-playbooks

**Inputs:**

- `InternalRange`: List of Internal IP ranges
- `UserVerification`: Whether to provide user verification for blocking those IPs. False - No prompt will be displayed to the user.True - The server will ask the 


## GitLab v2

**Type:** integration  
**Product:** GitLab  
**Commands:**

- `gitlab-version-get`: Retrieve version information for this GitLab instance.
- `gitlab-file-get`: Allows to receive information about file in repository like name, size, content.
- `gitlab-file-create`: This allows you to create a single file. File path or entry_id must be specified.
- `gitlab-file-delete`: Editing existing file in repository.
- `gitlab-issue-list`: Get a list of a project's issues.


## GLIMPS Detect

**Type:** integration  
**Product:** GLIMPS Detect  

Use the GLIMPS Detect Integration to send files to GLIMPS Malware and get results from it This integration was integrated and tested with version 0.2.0 of gdetect client

**Commands:**

- `gdetect-send`: send file to gDetect API.


## GLPI

**Type:** integration  
**Product:** GLPI  

GLPI open source ITSM solution This integration was integrated and tested with version 9.5.5 of GLPI

**Commands:**

- `glpi-create-user`: Create a new GLPI user
- `glpi-delete-user`: Delete GLPI user
- `glpi-disable-user`: Disable GLPI user
- `glpi-enable-user`: Enable GLPI user
- `get-mapping-fields`: Return the list of fields for an incident type
- `get-modified-remote-data`: Mirroring feature, use only for debug
- `glpi-get-username`: Get username by user ID
- `glpi-delete-ticket`: Delete GLPI ticket
- `glpi-get-ticket`: Get ticket details by ticket ID
- `glpi-create-ticket`: Create a GLPI ticket
- `glpi-search`: Search GLPI items
- `glpi-add-comment`: Add comment to ticket ID
- `glpi-upload-file`: Upload document
- `glpi-get-item`: Get item details by item type and item ID
- `glpi-update-ticket`: Update a GLPI ticket


## GLPIIncidentStatus

**Type:** script  
**Product:** GLPI  

populates the value of the GLPI Ticket State field and display it in a layout widget


## Gmail

**Type:** integration  
**Product:** Gmail  

Use the Gmail integration to search and process emails in your organization's Gmail mailboxes. This integration replaces the Gmail functionality in the GoogleApps API and G Suite integration. You need to do the following in Google before configuring your integration instance in the platform. Both the Gmail API and the Admin SDK API are required to use this integration.  To revoke or fetch a user role, you need an Immutable Google Apps ID

**Commands:**

- `gmail-delete-user`: Deletes a Gmail user.
- `gmail-get-tokens-for-user`: Lists all tokens associated with a specified user.
- `gmail-get-user`: Gets information for a specified user.
- `gmail-get-user-roles`: Retrieves a list of all Google roles for a specified user.
- `gmail-get-attachments`: Retrieves attachments from a sent Gmail message.
- `gmail-get-mail`: Retrieves the Gmail message sent to a specified user.
- `gmail-search`: Searches for Gmail records for a specific Google user.
- `gmail-search-all-mailboxes`: Searches the Gmail records for all Google users.
- `gmail-list-users`: Lists all Google users in a domain.
- `gmail-list-labels`: Lists all labels in the user's mailbox.
- `gmail-revoke-user-role`: Revokes a role for a specified Google user.
- `gmail-create-user`: Creates a new Gmail user.
- `gmail-delete-mail`: Deletes an email in the user's mailbox.
- `gmail-get-thread`: Returns all messages in a thread.
- `gmail-move-mail`: Moves an email to a different folder.


## Gmail Single User

**Type:** integration  
**Product:** Gmail Single User  

Use the Gmail Single User integration to send emails and fetch emails as incidents to the platform. Note: Use this integration if you only want to fetch and send emails from a single user's mailbox. If you need to access multiple user mailboxes, use the GMail Integration

**Commands:**

- `send-mail`: Sends an email using Gmail.
- `gmail-auth-link`: Starts the OAuth2 process. Gets a link to use to authenticate to Gmail.


## Google Chat via Webhook

**Type:** integration  
**Product:** Google Chat via Webhook  

Integration for sending notifications to a Google Chat space via Incoming Webhook

**Commands:**

- `send-google-chat-message`: Send a message to Google Chat Space via Incoming Webhook.
- `send-google-chat-custom-card`: Send a customizable card to Google Chat Space via Incoming Webhook


## Google Docs

**Type:** integration  
**Product:** Google Docs  

Use the Google Docs integration to create and modify Google Docs documents

**Commands:**

- `google-docs-get-document`: Returns the document that matches the specified document ID.
- `google-docs-create-document`: Creates a document.
- `google-docs-update-document`: Updates the document with the specified document ID.


## Google Dorking

**Type:** integration  
**Product:** Google Dorking  

Automate the process of google dorking searches in order to detect leaked data

**Commands:**

- `google-dorking-search`: Use the google search engine to search a query.


## Google Dorking File Processing

**Type:** playbook  
**Product:** Google Dorking  

This playbook processes files fetched by the Google Dorking integration. The SOC will track the file owner and classify the exposed data and users in order to contained the leaked data

**Inputs:**

- `ExclusionListName`: An platform list to exclude files by hash
- `SeverityMapping`: 
- `ComplianceMailAddress`: 
- `ITMailAddress`: 


## Google Drive

**Type:** integration  
**Product:** Google Drive  

Google Drive allows users to store files on their servers, synchronize files across devices, and share files. This integration helps you to create a new drive, query past activity, and view change logs performed by the users. This integration was integrated and tested with version 1.31.0 of GoogleDrive

**Commands:**

- `google-drive-create`: Deprecated. Use the google-drive-drive-create command instead.
- `google-drive-drive-create`: Creates a new Team Drive. The name argument specifies the name of the Team Drive. The specified user will be the first organizer. This shared drive/team drive f
- `google-drive-changes-list`: Lists the changes for a user or shared drive.
- `google-drive-activity-list`: Query past activity in Google Drive.
- `google-drive-drives-list`: Lists the user's shared drives.
- `google-drive-drive-get`: Gets a user shared drives.
- `google-drive-drive-delete`: Deletes a shared drive.
- `google-drive-files-list`: Lists the user's shared drives.
- `google-drive-file-get`: Get a single file.
- `google-drive-file-upload`: Creates a new file.
- `google-drive-file-download`: Download a single file.
- `google-drive-file-replace-existing`: Updates a file's content.
- `google-drive-file-delete`: Permanently deletes a file owned by the user without moving it to the trash. If the file belongs to a shared drive the user must be an organizer on the parent. 
- `google-drive-file-permissions-list`: Lists a file's or shared drive's permissions.
- `google-drive-file-permission-create`: Creates a permission for a file or shared drive.


## Google Drive (Standard Connector)

**Type:** integration  
**Product:** Google Drive (Standard Connector)  

Google Drive allows users to store files on their servers, synchronize files across devices, and share files. This integration helps you to create a new drive, query past activity, and view change logs performed by the users. This integration was integrated and tested with version 1.31.0 of GoogleDrive

**Commands:**

- `google-drive-create`: Deprecated. Use the google-drive-drive-create command instead.
- `google-drive-drive-create`: Creates a new Team Drive. The name argument specifies the name of the Team Drive. The specified user will be the first organizer. This shared drive/team drive f
- `google-drive-changes-list`: Lists the changes for a user or shared drive.
- `google-drive-activity-list`: Query past activity in Google Drive.
- `google-drive-drives-list`: Lists the user's shared drives.
- `google-drive-drive-get`: Gets a user shared drives.
- `google-drive-drive-delete`: Deletes a shared drive.
- `google-drive-files-list`: Lists the user's shared drives.
- `google-drive-file-get`: Get a single file.
- `google-drive-file-upload`: Creates a new file.
- `google-drive-file-download`: Download a single file.
- `google-drive-file-replace-existing`: Updates a file's content.
- `google-drive-file-delete`: Permanently deletes a file owned by the user without moving it to the trash. If the file belongs to a shared drive the user must be an organizer on the parent. 
- `google-drive-file-permissions-list`: Lists a file's or shared drive's permissions.
- `google-drive-file-permission-create`: Creates a permission for a file or shared drive.


## Google Gemini

**Type:** integration  
**Product:** Google Gemini  

This integration provides access to Google Gemini's large language models for AI-powered analysis and chat capabilities in the platform. Supports both Google AI Studio (API key) and Google Cloud Vertex AI (service account) authentication

**Commands:**

- `google-gemini-send-message`: Send a chat message to the Gemini AI model.


## Google Key Management Service

**Type:** integration  
**Product:** Google Key Management Service  

Use the Google Key Management Service API for CryptoKey management and encrypt/decrypt functionality

**Commands:**

- `google-kms-create-key`: Creates a new CryptoKey within a KeyRing.
- `google-kms-symmetric-decrypt`: Decrypts data that was protected by Encrypt.
- `google-kms-symmetric-encrypt`: Encrypts data, so it can only be recovered by a call to Decrypt.
- `google-kms-get-key`: Returns metadata for a given CryptoKey, and its primary CryptoKeyVersion.
- `google-kms-update-key`: Updates a CryptoKey.
- `google-kms-destroy-key`: Schedules a CryptoKeyVersion for destruction.
- `google-kms-restore-key`: Restores a CryptoKeyVersion in the DESTROY_SCHEDULED state.
- `google-kms-disable-key`: Disables a CryptoKeyVersion of a given CryptoKey.
- `google-kms-enable-key`: Enables a CryptoKeyVersion of a given CryptoKey.
- `google-kms-list-keys`: Lists all keys in key ring.
- `google-kms-asymmetric-encrypt`: Encrypts data using a asymmetric CryptoKey
- `google-kms-asymmetric-decrypt`: Decrypts data using an asymmetric CryptoKey.
- `google-kms-list-key-rings`: Lists all KeyRings in a given location.
- `google-kms-list-all-keys`: Lists all CryptoKeys across all KeyRings in a given location.
- `google-kms-get-public-key`: Returns the public key from a given CryptoKey.


## Google Maps

**Type:** integration  
**Product:** Google Maps  

Use the Google Maps API. This integration was integrated and tested with version 3.43 of the Google Maps API. This integration always uses the latest API version

**Commands:**

- `google-maps-geocode`: Returns the coordinates of the given physical address. Only the first result is returned (the most relevant, according to Google Maps).


## Google Safe Browsing v2

**Type:** integration  
**Product:** Google Safe Browsing  

Search Safe Browsing v4

**Commands:**

- `url`: Check URL Reputation


## Google SecOps Cases

**Type:** integration  
**Product:** Google SecOps  

Use the Google SecOps Cases integration to retrieve Cases as Incidents. This integration also provides commands to manage the Cases lifecycle. This integration was integrated and tested with version v1 Alpha of Google SecOps API

**Commands:**

- `gcb-case-list`: Retrieve the list of cases.
- `gcb-case-get`: Retrieve a specific case by its ID.
- `gcb-case-update`: Update the properties of a case.
- `gcb-case-tag-add`: Add the specified tags to the cases.
- `gcb-case-tag-remove`: Remove the specified tag from a case.
- `gcb-case-priority-change`: Change the priority of the specified cases.
- `gcb-case-stage-definition-list`: Retrieve the list of case stage definitions configured in the instance.
- `gcb-case-stage-change`: Change the workflow stage of the specified cases.
- `gcb-case-reopen`: Reopen the specified cases.
- `gcb-case-close-definition-list`: Retrieve the list of case close definitions configured in the instance.
- `gcb-case-close`: Close the specified cases.
- `gcb-case-assign`: Assign the specified cases to a specific analyst or SOC role.
- `gcb-case-comment-list`: Retrieve the list of comments associated with the specified case.
- `gcb-case-comment-create`: Add a comment to the specified case.
- `gcb-case-sla-pause`: Pause the SLA timer for the specified case.


## Google SecOps v1 Alpha

**Type:** integration  
**Product:** Google SecOps  

Use the Google SecOps integration to retrieve IOC Domain matches as Incidents. This integration also provides reputation and threat enrichment of indicators observed in the enterprise. This integration was integrated and tested with version v1 Alpha of GoogleSecOps. Note: The commands will do up to 3 internal retries with a gap of 15, 30, and 60 seconds (exponentially) between the retries. If you are upgrading from a Google Chronicle Backstory integration, please refer to the Migration Guide for guidance

**Commands:**

- `gcb-list-iocs`: Lists the IOC Domain matches within your enterprise for the specified time interval. The indicator of compromise (IOC) domain matches lists for which the domain
- `ip`: Checks the reputation of an IP address.
- `domain`: Checks the reputation of a domain.
- `gcb-ioc-details`: Accepts an artifact indicator and returns any threat intelligence associated with the artifact. The threat intelligence information is drawn from your enterpris
- `gcb-list-events`: List all of the events discovered within your enterprise on a particular device within the specified time range. If you receive the maximum number of events you
- `gcb-list-detections`: Return the detections for the specified version of a rule, the latest version of a rule, all versions of a rule, or all versions of all rules.
- `gcb-list-rules`: List the latest versions of all Rules.
- `gcb-create-rule`: Creates a new rule. By default the live rule status will be set to disabled.
- `gcb-get-rule`: Retrieves the rule details of specified Rule ID or Version ID.
- `gcb-delete-rule`: Deletes the rule specified by Rule ID.
- `gcb-create-rule-version`: Creates a new version of an existing rule.
- `gcb-change-rule-alerting-status`: Updates the alerting status for a rule specified by Rule ID.
- `gcb-change-live-rule-status`: Updates the live rule status for a rule specified by Rule ID.
- `gcb-start-retrohunt`: Initiate a retrohunt for the specified rule.
- `gcb-get-retrohunt`: Get retrohunt for a specific version of rule.


## Google Sheets

**Type:** integration  
**Product:** Google Sheets  

Google Sheets is a spreadsheet program that is part of the free web-based Google applications to create and format spreadsheets. Use this integration to create and modify spreadsheets. This integration was integrated and tested with version 4 of Google Sheets API

**Commands:**

- `google-sheets-spreadsheet-create`: Create a new spreadsheet.
- `google-sheets-spreadsheet-get`: Returns the spreadsheet of the given ID. If include_grid_data is set to true and no ranges given, will defaultly return the first 500 rows and 20 columns of the
- `google-sheets-sheet-create`: Adds a new sheet. When a sheet is added at a given index, all subsequent sheet indexes are incremented.
- `google-sheets-sheet-duplicate`: Duplicates the contents of a sheet.
- `google-sheets-sheet-copy-to`: Copies a single sheet from a spreadsheet to another spreadsheet.
- `google-sheets-sheet-delete`: Delete a sheet from a spreadsheet by ID.
- `google-sheets-sheet-clear`: Clears values from a spreadsheet. The caller must specify the spreadsheet ID and range. Only values are cleared. All other properties of the cell (such as forma
- `google-sheets-range-delete`: Deletes a range of cells, shifting other cells into the deleted area.
- `google-sheets-dimension-delete`: Deletes the dimensions from the sheet. Note that the indexing starts from 0.
- `google-sheets-data-paste`: Inserts data into the spreadsheet starting at the specified coordinate.
- `google-sheets-find-replace`: Finds and replaces data in cells over a range, sheet, or all sheets.
- `google-sheets-value-update`: Sets values in a range of a spreadsheet. The caller must specify the spreadsheet ID, range, and a valueInputOption.
- `google-sheets-value-append`: Appends values to a spreadsheet. The input range is used to search for existing data and find a "table" within that range. Values will be appended to the next r
- `google-sheets-spreadsheet-update`: This is a custom update command, used to apply any of the Google Sheets API options. Applies one or more updates to the spreadsheet. Each request is validated b


## Google Vault - Display Results

**Type:** playbook  
**Product:** Google Vault  

Ques and displays vault search result

**Inputs:**

- `pollInterval`: The interval in which to check the export status (in minutes).
- `pollTimeout`: The timeout to terminate the poll (in minutes).
- `maxResultForDisplay`: The maximum number of result to be displayed.
- `downloadFile`: Whether the export file created will be downloaded into the War Room. "True" means it will.
- `ExportID`: The export ID.
- `MatterID`: The matter ID.
- `SearchtType`: The type of Search. Can be, "Drive", "Groups" or "Mail".


## Google Vault - Search Drive

**Type:** playbook  
**Product:** Google Vault  

Performs a Google Vault search in Drive accounts and displays the results

**Inputs:**

- `matterID`: The ID of the matter.
- `exportName`: The name of the exported file.
- `dataScope`: The choice of the search scope.
- `searchMethod`: The choice of search method. The default is: "Specific Accounts" - which requires emails argument. 'Organizational Unit' - requires ou argum
- `emails`: Whether the search method is set to specific accounts (separated by comma).
- `ou`: Whether the search method is set to specific accounts (separated by comma).
- `teamDrive`: Whether the search method is set to team drives.
- `includeTeamDrives`: Include/Exclude team drives.


## Google Vault - Search Groups

**Type:** playbook  
**Product:** Google Vault  

Performs a Google Vault search in Drive accounts and display the results

**Inputs:**

- `matterID`: The ID of the matter.
- `exportName`: The name of the exported file.
- `dataScope`: The choice of the search scope.
- `searchMethod`: The choice of Search method. The default is, "Specific Accounts", this requires emails argument. "Organizational Unit" this requires ou argu
- `emails`: Whether the search method is set to Specific Accounts (separated by comma).
- `ou`: Whether the search method is set to Specific Accounts (separated by comma).
- `teamDrive`: Whether the search method is set to team drives.
- `includeTeamDrives`: Include/Exclude team drives.


## Google Vault - Search Mail

**Type:** playbook  
**Product:** Google Vault  

Performs a Google Vault search in Drive accounts and display the results

**Inputs:**

- `matterID`: The ID of the matter.
- `exportName`: The name of the exported file.
- `dataScope`: The choice of Search scope.
- `searchMethod`: The choice of Search method. The default is: "Specific Accounts", this requires the emails argument. "Organizational Unit", this requires ou
- `emails`: Whether the search method is set to "Specific Accounts" (separated by comma).
- `ou`: Whether the search method is set to "Specific Accounts" (separated by comma).
- `teamDrive`: Whether the search method is set to "Team Drives".
- `includeTeamDrives`: Include/Exclude team drives.


## Google Vision AI

**Type:** integration  
**Product:** Google Vision AI  

Image processing with Google Vision API

**Commands:**

- `google-vision-detect-logos`: Detects brand logos in the given image.


## Google Workspace Admin

**Type:** integration  
**Product:** G Suite Admin  

G Suite or Google Workspace Admin is an integration to perform an action on IT infrastructure, create users, update settings, and more administrative tasks. This integration was integrated and tested majorly with G Suite Basic edition

**Commands:**

- `gsuite-mobile-update`: Takes an action that affects a mobile device. For example, remotely wiping a device.
- `gsuite-mobile-delete`: Removes a mobile device. Note that this does not break the device's sync, it simply removes it from the list of devices connected to the domain. If the device s
- `gsuite-user-alias-add`: Adds an alias.
- `gsuite-user-create`: Creates a user.
- `gsuite-group-create`: Creates a group with a group name and its description.
- `gsuite-role-assignment-list`: Retrieves a paginated list of all role assignments.
- `gsuite-role-assignment-create`: Creates a role assignment.
- `gsuite-role-create`: Creates a new role.
- `gsuite-token-revoke`: Delete all access tokens issued by a user for an application.
- `gsuite-user-signout`: Signs a user out of all web and device sessions and reset their sign-in cookies.
- `gsuite-datatransfer-list`: Lists the transfers for a customer by source user, destination user, or status.
- `gsuite-custom-user-schema-create`: Creates a custom user schema to add custom fields to user profiles. Note: field_raw_json has higher precedence when both field_raw_json and field_json_entry_id 
- `gsuite-custom-user-schema-update`: Updates a custom user schema. Note: field_raw_json has higher precedence when both field_raw_json and field_json_entry_id are provided.
- `gsuite-datatransfer-request-create`: Inserts a data transfer request.
- `gsuite-user-update`: Updates a user.


## GoogleApps API and G Suite

**Type:** integration  

Use the GoogleApps API and G Suite integration to help administrators migrate to G Suite, create custom usage reports, and manage users, groups, and devices. NOTE: The googleapps-gmail commands are deprecated, to execute Gmail commands, use the Gmail integration

**Commands:**

- `googleapps-chrome-device-action`: Performs one of several actions on a Google Chrome device.
- `googleapps-device-action`: Performs one of several actions on a Google device.
- `googleapps-get-chrome-devices-for-user`: Lists all Google Chrome devices associated with a specified Google user.
- `googleapps-get-devices-for-user`: Lists all devices associated with a specified Google user.
- `googleapps-get-tokens-for-user`: Lists all tokens associated with a specified Google user.
- `googleapps-get-user`: Retrieves information for a specified Google user.
- `googleapps-get-user-roles`: Lists all available Google roles for a specified Google user.
- `googleapps-gmail-get-attachment`: Retrieves a Gmail attachment sent to a specified Google user.
- `googleapps-gmail-get-mail`: Retrieves a Gmail message sent to a specified Google user.
- `googleapps-gmail-search`: Searches the Gmail records of a specified Google user.
- `googleapps-list-users`: Lists all Google users.
- `googleapps-revoke-user-role`: Revokes roles for a specified Google users.


## GoogleDriveApiModule

**Type:** script  

To use the common Google Drive integration logic, run the following command to import the GoogleDriveApiModule. Then, the run_google_drive_integration entry point and the GSuiteClient (re-exported from GSuiteApiModule) will be available for usage. For the canonical consumer, see the Google Drive integration


## GoogleSecOpsSyncCaseInformation

**Type:** script  
**Product:** Google SecOps  

Syncs the latest case information, related alerts and alert entities from Google SecOps and updates the the platform

**Inputs:**

- `case_id`: Specify the ID of the Google SecOps Case to sync.Note: If not provided, the script will try to retrieve it from the incident context.
- `alert_page_size`: Specify the maximum number of alerts to retrieve.Note: Maximum value is 1000.
- `entity_page_size`: Specify the maximum number of entities to retrieve per alert.Note: Maximum value is 1000.


## GRAAlertAnalyticalFeatureDisplay

**Type:** script  
**Product:** Gurucul Risk Analytics  

Displays GRA alert analytical features in a markdown table


## GRAAlertClassifierDisplay

**Type:** script  
**Product:** Gurucul Risk Analytics  

Displays GRA alert classifier details in a markdown table


## GRAAlertHistoryDisplay

**Type:** script  
**Product:** Gurucul Risk Analytics  

Displays GRA alert update history in a markdown table


## GRAAnalyticalFeatureDisplay

**Type:** script  
**Product:** Gurucul Risk Analytics  

Display GRA analytical feature on the layout


## GRAAnomaliesDisplay

**Type:** script  
**Product:** Gurucul Risk Analytics  

Retrieve anomalies for specified case id from GRA and update in platform


## GRACase

**Type:** playbook  
**Product:** Gurucul Risk Analytics  

Playbook for fetching cases associated to high risk users


## Grafana

**Type:** integration  
**Product:** Grafana  

Grafana alerting service. This integration was integrated and tested with version 8.0.0 of Grafana

**Commands:**

- `grafana-alerts-list`: Gets alerts.
- `grafana-alert-pause`: Pauses an alert by ID.
- `grafana-alert-unpause`: Unpauses an alert by ID.
- `grafana-users-search`: Gets users.
- `grafana-user-teams-get`: Gets the user's teams by user ID.
- `grafana-user-orgs-get`: Gets user's organizations by user ID.
- `grafana-user-update`: Updates a user by user ID. Login or email is mandatory. If you change your own login information, you won't be able to continue querying as your username (login
- `grafana-annotation-create`: Creates an annotation in the Grafana database. The dashboard_id and panel_id fields are optional. If they are not specified, a global annotation is created and 
- `grafana-teams-search`: Gets teams.
- `grafana-team-members-list`: Gets a list of all team members by team ID.
- `grafana-user-add-to-team`: Adds a user to a team.
- `grafana-user-remove-from-team`: Removes a user from a team.
- `grafana-team-add`: Creates a new team.
- `grafana-team-delete`: Deletes a team.
- `grafana-org-create`: Creates an organization.


## GRAIncidentAnomaliesDisplay

**Type:** script  
**Product:** Gurucul Risk Analytics  

Displays and refreshes GRA incident anomaly details


## GraphQL

**Type:** integration  
**Product:** GraphQL  

Generic GraphQL client to interact with any GraphQL server API

**Commands:**

- `graphql-query`: Execute a query request to the GraphQL server.
- `graphql-mutation`: Execute a mutation request to the GraphQL server.


## GRAUpdateAlertStatus

**Type:** script  
**Product:** Gurucul Risk Analytics  

Updates GRA alert status when the Cortex incident is closed

**Inputs:**

- `closeNotes`: The close notes.
- `closeReason`: The close reason.


## GRAUpdateCaseStatus

**Type:** script  
**Product:** Gurucul Risk Analytics  

GRA Update Case Status

**Inputs:**

- `closeNotes`: Close Note
- `closeReason`: Close reason


## GRAUpdateIncidentStatus

**Type:** script  
**Product:** Gurucul Risk Analytics  

Updates GRA incident status when the Cortex incident is closed

**Inputs:**

- `closeNotes`: The close notes.
- `closeReason`: The close reason.


## GravityZone

**Type:** integration  
**Product:** GravityZone  

GravityZone provides secure access to incident and endpoint data and enables remediation actions through its APIs. This integration was integrated and tested with version 6.6 of GravityZone

**Commands:**

- `fetch-incidents`: Retrieves incidents from GravityZone Cloud.
- `gz-endpoint-list`: Retrieves the list of managed endpoints.
- `gz-endpoint-get`: Retrieves endpoint details by endpoint ID.
- `gz-endpoint-download-investigation-package`: Collects and downloads an investigation package from an endpoint.
- `gz-endpoint-download-file`: Downloads a file from an endpoint.
- `gz-endpoint-isolate`: Isolates an endpoint from the network.
- `gz-endpoint-deisolate`: Restores an isolated endpoint to the network.
- `gz-endpoint-kill-process`: Terminates a process on an endpoint by process ID.
- `gz-endpoint-run-command`: Runs a command on the endpoint. The applied policy must have Remote Shell enabled for this action to work.
- `gz-endpoint-upload-file`: Uploads a file to an endpoint.
- `gz-endpoint-list-by-running-process-hash`: Retrieves endpoints that are running processes with a specified hash. The API key and the applied policy must allow Live Search. Endpoints must be online. The c
- `gz-endpoint-get-process-tree-by-hash`: Retrieves the process tree on an endpoint for a specified process hash. The applied policy must allow Live Search, and the endpoint must be online.
- `gz-incident-get`: Retrieves incident details by ID.
- `gz-incident-list`: Retrieves incidents within the last three days from all endpoints or a specific endpoint.
- `gz-incident-add-note`: Adds a note to one or more incidents.


## Graylog

**Type:** integration  
**Product:** Graylog  

Integration with Graylog to search for logs and events This integration was integrated and tested with version 3.3.6 of Graylog

**Commands:**

- `graylog-cluster-status`: Get Cluster nodes status
- `graylog-cluster-node-jvm`: Get JVM status of a node in cluster
- `graylog-cluster-inputstates`: Get input states of the cluster
- `graylog-cluster-processing-status`: Shows the processing status of the cluster
- `graylog-indexer-cluster-health`: Get health of the indexer
- `graylog-search`: Search for messages in a relative timerange, specified as seconds from now. Example: 300 means search from 5 minutes ago to now.
- `graylog-events-search`: Events overview and search
- `graylog-search-absolute`: Search with absolute times


## GreaterCidrNumAddresses

**Type:** script  
**Product:** Filters And Transformers  

Check if number of availble addresses in IPv4 or IPv6 CIDR is greater than given number

**Inputs:**

- `left`: IP/CIDR, e.g. 192.168.0.0/24
- `right`: The number of addresses to be greater from.


## GreatHorn

**Type:** integration  
**Product:** GreatHorn  

The only cloud-native security platform that stops targeted social engineering and phishing attacks on cloud email platforms like Office 365 and G Suite. This integration was integrated and tested with version 2.0 of GreatHorn

**Commands:**

- `gh-get-message`: Return message details for the specified event
- `gh-search-message`: Search for message based on filtering input
- `gh-remediate-message`: Perform the specified remediation action on message
- `gh-revert-remediate-message`: Revert the specified remediation action on the given message
- `gh-get-policy`: Retrieve details about the policy specified
- `gh-set-policy`: Retrieve details about the policy specified.


## GreyNoise

**Type:** integration  
**Product:** GreyNoise  

GreyNoise is a cybersecurity platform that collects and analyzes Internet-wide scan and attack traffic. With this integration, users can contextualize existing alerts, filter false-positives, identify compromised devices, and track emerging threats. This integration was integrated and tested with version 3.0.0 of the GreyNoise SDK. Supported the platform.0.0 and later

**Commands:**

- `ip`: Runs reputation on IPs.
- `greynoise-ip-quick-check`: Check whether a given IP address is "Internet background noise", or has been observed scanning or attacking devices across the Internet. Note: It checks against
- `greynoise-query`: Get the information of IP based on the providence filters.
- `greynoise-stats`: Get aggregate statistics for the top organizations, actors, tags, ASNs, countries, classifications, and operating systems of all the results of a given GNQL que
- `greynoise-riot`: Identifies IPs from known benign services and organizations that commonly cause false positives in network security and threat intelligence products. The collec
- `greynoise-context`: Identifies IPs that have been observed mass-scanning the internet.
- `greynoise-similarity`: Identify IPs with a similar internet scanning profile.
- `greynoise-timeline`: Get timeline activity for an IP address.
- `cve`: Queries GreyNoise for CVE Vuln Intelligence.


## GreyNoise Community

**Type:** integration  
**Product:** GreyNoise  

GreyNoise tells security analysts what not to worry about. We do this by curating data on IPs that saturate security tools with noise. This unique perspective helps analysts confidently ignore irrelevant or harmless activity, creating more time to uncover and investigate true threats. The Action allows IP enrichment via the GreyNoise Community API. The GreyNoise Integration should be used by customers with a paid subscription to GreyNoise with the exception of the IP command, which is available with limit results to free users. This integration was integrated and tested with version 3.0.0 of GreyNoise Python SDK. Supported the platform.0.0 and later

**Commands:**

- `ip`: Queries IPs in the GreyNoise Community API.


## GridFieldSetup

**Type:** script  
**Product:** Common Scripts  

Automation used to more easily populate a grid field. This is necessary when you want to assign certain values as static or if you have context paths that you will assign to different values as well. Instead of a value you can enter TIMESTAMP to get the current timestamp in ISO format. For example: !GridFieldSetup keys=ip,src,timestamp val1=${AWS.EC2.Instances.NetworkInterfaces.PrivateIpAddress} val2="AWS" val3="TIMESTAMP" gridfiled="gridfield"

**Inputs:**

- `keys`: columns for the grid field in comma separated format
- `val1`: A value for the 1st key. (Can be a string or context path or TIMESTAMP to get the current timestamp in ISO format.)
- `val2`: A value for the 2nd key. (Can be a string or context path or TIMESTAMP to get the current timestamp in ISO format.)
- `val3`: A value for the 3rd key. (Can be a string or context path or TIMESTAMP to get the current timestamp in ISO format.)
- `val4`: A value for the 4th key. (Can be a string or context path or TIMESTAMP to get the current timestamp in ISO format.)
- `val5`: A value for the 5th key. (Can be a string or context path or TIMESTAMP to get the current timestamp in ISO format.)
- `val6`: A value for the 6th key. (Can be a string or context path or TIMESTAMP to get the current timestamp in ISO format.)
- `val7`: A value for the 7th key. (Can be a string or context path or TIMESTAMP to get the current timestamp in ISO format.)


## Group

**Type:** script  
**Product:** Community Common Scripts  

Splits a list into group. e.g. [1,2,3,4] -> ["1,2", "3,4"]

**Inputs:**

- `input`: An input list.
- `chunk`: Size of each group.
- `type`: Group as list or string.
- `delimiter`: Separate elements using delimiter (If type is String).


## Group-IB THF Polygon

**Type:** integration  
**Product:** Polygon  

THF Polygon is a Malware Detonation & Research platform designed for deep dynamic analysis and enhanced indicators extraction. THF Polygon analyzes submitted files and urls and extracts deep IOCs that appear when malicious code is triggered and executed. Polygon could be used either for application-level tasks (like smtp-based mail filtering) and analytical purposes (files/urls analysis for verdict, report and indicators). This integration was integrated and tested with version 3.1 of Group-IB THF Polygon

**Commands:**

- `polygon-upload-file`: Upload file for analysis
- `polygon-upload-url`: Upload URL for analysis.
- `polygon-analysis-info`: Get THF Polygon analysis info
- `polygon-export-report`: Export an archive with THF Polygon report to War Room
- `polygon-export-pcap`: Network activity dump export
- `polygon-export-video`: Screen activity video export
- `file`: Check file reputation


## GrrGetFiles

**Type:** script  
**Product:** GRR  

Downloads files from a specified machine without requiring approval

**Inputs:**

- `hostname`: The target host. Can be, "FQDN" or "client ID".
- `paths`: Fetches the number of elements, an array of path strings.
- `max_file_size`: The maximum size of the file that will download.
- `action`: The action to apply to the found files. Can be, "STAT", "HASH" or "DOWNLOAD".
- `pathtype`: The path type to glob in. Can be, "UNSET", "OS", "TSK", "REGISTRY", "MEMORY", or "TMPFILE".


## GrrGetFlows

**Type:** script  
**Product:** GRR  

Lists flows launched on a given client

**Inputs:**

- `client_id`: The ID of the client.
- `offset`: The starting offset.
- `count`: The maximum number of flows to fetch.


## GrrSetFlows

**Type:** script  
**Product:** GRR  

Starts a flow on a given client with given parameters

**Inputs:**

- `client_id`: The ID of the client.
- `flow`: The JSON string of the flow to set.


## GSuiteApiModule

**Type:** script  

To use the common GSuite API logic (authentication and API requests), run the following command to import the GSuiteApiModule. Then, the GSuiteClient will be available for usage. For examples, see the G Suite Admin or Google Drive or Google Calendar integrations


## GuardiCore v2

**Type:** integration  
**Product:** Akamai GuardiCore  

The GuardiCore v2 integration provides access to incident and endpoint (asset) information via the GuardiCore API. This integration was integrated and tested with version 3.0.0 of the GuardiCore API

**Commands:**

- `guardicore-search-asset`: Display information about assets.
- `guardicore-get-incident`: Display information about an incident.
- `guardicore-get-incidents`: Display information about incidents.
- `endpoint`: Endpoint command (uses guardicore-search-asset internally).


## Gurucul-GRA

**Type:** integration  
**Product:** Gurucul Risk Analytics  

Gurucul Risk Analytics (GRA) is a data science backed cloud native platform that predicts, detects and prevents breaches. It ingests and analyzes massive amounts of data from the network, IT systems, cloud platforms, EDR, applications, IoT, HR and much more to give you a comprehensive contextual view of user and entity behaviors. This integration fetches GRA Incidents or Alerts into Cortex and exposes War Room commands for investigation and actions. Workflows can be configured in Cortex based on the commands provided by GRA. Please make sure you look at the integration source code and comments

**Commands:**

- `gra-fetch-users`: Retrieve List of All Users (Identities)
- `!gra-fetch-active-resource-accounts`: Retrieve List of All Active Accounts for a Given Resource.
- `gra-fetch-active-datasource-accounts`: Retrieve list of all active accounts for a specified data source.
- `gra-fetch-user-accounts`: Retrieve List of All Active Accounts and Details for a Given User.
- `gra-fetch-resource-highrisk-accounts`: Retrieve High Risk Accounts for a Given Resource
- `!gra-fetch-hpa`: Retrieve List of All High Risk Privileged Accounts.
- `gra-fetch-resource-hpa`: Retrieve all High Privileged Accounts for a Given Resource.
- `gra-fetch-orphan-accounts`: Retrieve List of All Orphan / Rogue Accounts.
- `gra-fetch-resource-orphan-accounts`: Retrieve All Orphan / Rogue Accounts for a Given Resource.
- `gra-fetch-datasource-highrisk-accounts`: Retrieve high risk accounts for a specified data source.
- `gra-fetch-datasource-hpa`: Retrieve high privileged accounts for a specified data source.
- `gra-fetch-datasource-orphan-accounts`: Retrieve orphan / rogue accounts for a specified data source.
- `gra-user-activities`: Retrieve activity for a specified user.
- `gra-fetch-users-details`: get details of the user.
- `gra-highRisk-users`: Retrieve list of all high risk users.


## GZipFile

**Type:** script  
**Product:** GZip  

GZip a file and upload to war room

**Inputs:**

- `entryID`: CSV list of entry ids for the files to gzip.


## HackerOne

**Type:** integration  
**Product:** HackerOne  

HackerOne integration allows users to fetch reports by using the fetch incidents capability. It also provides commands to retrieve all the reports and programs. This integration was integrated and tested with API version v1 of HackerOne

**Commands:**

- `hackerone-report-list`: Retrieves all the reports based on program handle and provided arguments.
- `hackerone-program-list`: Retrieves information about the programs in which the user is a member.


## HackerView Incident Management

**Type:** playbook  
**Product:** CTM360  

This playbook runs the incidents through indicator enrichment, then based on the mirroring settings, it can communicate with the remote server to track the progress of the investigation


## HackerView Incident Management V2

**Type:** playbook  
**Product:** CTM360  

This playbook runs the incidents through indicator enrichment, then based on the mirroring settings, it can communicate with the remote server to track the progress of the investigation. When the remote HackerView ticket status becomes inactive, the playbook automatically closes the local incident (Close Incident Locally → closeInvestigation). The HackerView Incident type runs this playbook with autorun enabled, so that auto-close path does not wait for analyst input

**Inputs:**

- `closeReason`: The reason recorded when the playbook closes the local incident after the remote HackerView ticket becomes inactive.


## Hackuity

**Type:** integration  
**Product:** Hackuity  

From a war-room, query your Hackuity cockpit in order to seamlessly retrieve information related to your vulnerability stock. This integration was integrated and tested with version 1.25.0 of Hackuity

**Commands:**

- `hackuity-search-findings`: Search for findings in Hackuity.
- `hackuity-search-vulndb-vulnerabilities`: Search for vulndb vulnerabilities in Hackuity.
- `hackuity-search-provider-vulnerabilities`: Search for provider vulnerabilities in Hackuity.
- `hackuity-dashboard-widgets`: List the widgets in the default dashboard of the user.
- `hackuity-dashboard-data`: Get the data of a dashboard widget


## Halcyon

**Type:** integration  
**Product:** Halcyon  

Halcyon is a device management platform that helps organizations monitor, control, and secure their network of devices. It provides centralized tools for overseeing hardware and software inventory, deploying updates, enforcing security policies, and ensuring compliance across device environments. This integration fetches alerts and events from the Halcyon platform and ingests them into Cortex XSIAM

**Commands:**

- `halcyon-get-events`: This command is used for developing/debugging and is to be used with caution, as it can create events, leading to events duplication and API request limitation 


## Handle Darktrace Model Breach

**Type:** playbook  
**Product:** Darktrace  

Handles each fetched Darktrace model breach by gathering additional detail about the activity and device, providing enrichment data from Darktrace and platform, linking similar incidents, and giving the ability to acknowledge the model breach and close the incident


## Handle Hello World Alert

**Type:** playbook  
**Product:** HelloWorld  

This is playbook that will handle the alerts coming from Hello World service

**Inputs:**

- `AlertID`: Alert ID to retrieve details for. By default retrieves from the HelloWorld ID custom field in the HelloWorld incident type


## Handle Shadow IT Incident

**Type:** playbook  
**Product:** Shadow IT  

This playbook is used to handle a Shadow IT incident. A Shadow IT incident occurs when a resource attributed to the organization that is not sanctioned by IT nor protected by the InfoSec team is found. This playbook handles the incident by helping the analyst find the owner of the resource based on existing evidence. The playbook also marks the service indicators (IP or FQDN) with a Shadow IT tag. The possible owner and their manager are notified and onboarding of the asset on Prisma Cloud is triggered through a manual process. Supported the platform.0.0 and later

**Inputs:**

- `Notify Manager`: Notify user's manager
- `ShadowITIndicatorTags`: Tags to add to indicators to identify potential Shadow IT assets
- `ManagerNotificationSubjectPrefix`: This input is added as prefix to the owner name to build the subject of the email sent to the owner's manager.
- `ManagerNotificationBody`: Body of the email to send to the owner's manager.


## HashiCorp Terraform

**Type:** integration  
**Product:** HashiCorp Terraform  

Hashicorp Terraform provide infrastructure automation to provision and manage resources in any cloud or data center with Terraform. This integration was integrated and tested with version v1.4.4 of HashicorpTerraform

**Commands:**

- `terraform-runs-list`: List runs in a workspace.
- `terraform-run-action`: Perform an action on a Terraform run. The available actions are: apply, cancel, discard, force-cancel, force-execute.
- `terraform-plan-get`: Get the plan JSON file or the plan meta data.
- `terraform-policies-list`: List the policies for an organization or get a specific policy.
- `terraform-policy-set-list`: List the policy sets for an organization or get a specific policy set.
- `terraform-policies-checks-list`: List the policy checks for a Terraform run.
- `terraform-get-events`: Retrieves Terraform audit trail events. This command is supported in Cortex XSIAM only and is intended for development and debugging purposes, as it may produce


## HashiCorp Vault

**Type:** integration  
**Product:** HashiCorp Vault  

Secure, store, and tightly control access to tokens, passwords, certificates, and encryption keys for protecting secrets and other sensitive data using HashiCorp Vault. This integration fetches credentials. For more information, see Managing Credentials. This integration was integrated and tested with version 1.12.2 of HashiCorp Vault

**Commands:**

- `hashicorp-list-secrets-engines`: List all secrets engines that exist in HashiCorp Vault.
- `hashicorp-list-secrets`: List secrets (names) for a specified KV engine.
- `hashicorp-get-secret-metadata`: Returns information about a specified secret in a specified KV V2 engine.
- `hashicorp-delete-secret`: Deletes the data under a specified secret given the secret path. Performs a soft delete that allows you to run the hashicorp-undelete-secret command if necessar
- `hashicorp-undelete-secret`: Undeletes (restores) a secret on HashiCorp (for KV V2 engine).
- `hashicorp-destroy-secret`: Permanently deletes a secret (for KV V2 engine).
- `hashicorp-disable-engine`: When a secrets engine is no longer needed, it can be disabled. All secrets under the engine are revoked and the corresponding vault data and configurations are 
- `hashicorp-enable-engine`: ***!hashicorp-disable-engine path=secret Enables a new secrets engine at the specified path.
- `hashicorp-list-policies`: Lists all configured policies.
- `hashicorp-get-policy`: Get information for a policy.
- `hashicorp-seal-vault`: If you suspect your data has been compromised, you can seal your vault to prevent access to your secrets.
- `hashicorp-unseal-vault`: Use a single master key share to unseal the vault. If the master key shares threshold is met, the key will attempt to unseal the vault. Otherwise, this API must
- `hashicorp-configure-engine`: Configure a secrets engine to fetch secrets from.
- `hashicorp-reset-configuration`: Reset the engine configuration.
- `hashicorp-create-token`: Create a new authentication token.


## Hatching Triage

**Type:** integration  
**Product:** Hatching Triage  

Submit a high volume of samples to run in a sandbox and view reports This integration was integrated and tested with version 0 of Hatching Triage

**Commands:**

- `triage-query-samples`: Get a list of all samples either private or public
- `triage-submit-sample`: Submits a file or url for analysis
- `triage-get-sample`: Pulls back basic information about the sample id given
- `triage-get-sample-summary`: Gets a summary report of the sample id provided
- `triage-delete-sample`: Deletes a sample from the sandbox
- `triage-set-sample-profile`: When a sample is in the static_analysis status, a profile should be selected in order to continue.
- `triage-get-static-report`: Get the static analysis of a sample
- `triage-get-report-triage`: Retrieves the generated Triage behavioral report for a single task
- `triage-get-kernel-monitor`: Retrieves the output of the kernel monitor
- `triage-get-pcap`: Retrieves the PCAP of the analysis for further manual analysis
- `triage-get-dumped-file`: Retrieves files dumped by the sample. The names can be found under the "dumped" section from the triage report output
- `triage-get-users`: Return all users within the company as a paginated list. Returns a single user if a userID is provided
- `triage-create-user`: Creates a new user and returns it. The user will become a member of the company the requesting user is a member of
- `triage-delete-user`: Delete a user and all associated data, invalidating any sessions and removing their API keys. Any samples submitted by this user are kept
- `triage-create-api-key`: Creates a new key can be used to make API calls on behalf of the specified user. The user should have been granted the access_api permission beforehand


## Have I Been Pwned? v2

**Type:** integration  
**Product:** Pwned  
**Commands:**

- `pwned-email`: Checks if an email address was compromised.
- `pwned-domain`: Checks if a domain was compromised.
- `email`: Checks if an email address was compromised.
- `domain`: Checks if a domain was compromised.
- `pwned-username`: Checks if a username was compromised.


## HealthCheck

**Type:** playbook  
**Product:** System Diagnostics and Health Check  

New version for HealthCheck main playbook

**Inputs:**

- `ChangeThresholdsRequired`: 


## HealthCheck-xsiam

**Type:** playbook  
**Product:** System Diagnostics and Health Check  

New version for HealthCheck main playbook

**Inputs:**

- `ChangeThresholdsRequired`: 


## HealthCheckAPIvalidation

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckCollectData

**Type:** script  
**Product:** System Diagnostics and Health Check  

This README contains the full documentation for your script. You auto-generate this README file from your script YML file using the platform-sdk generate-docs command. For more information see the documentation article


## HealthCheckCommonIndicators

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckContainersStatus

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckCPU

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckDiskUsage

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckDiskUsageLine

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckExportSummaryData

**Type:** script  
**Product:** System Diagnostics and Health Check  

This README contains the full documentation for your script. You auto-generate this README file from your script YML file using the platform-sdk generate-docs command. For more information see the documentation article


## HealthCheckFields

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckIncidentsCreatedDaily

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckIncidentsCreatedMonthly

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckIncidentsCreatedWeekly

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckIncidentTypes

**Type:** script  
**Product:** System Diagnostics and Health Check  

Identify custom and detached system incidents type Checking if 'Auto Extraction' is turned on for: Extract from all Extract from specific indicators doesn't have any settings


## HealthCheckInsightsEndpointManagement

**Type:** script  
**Product:** System Diagnostics and Health Check  

This README contains the full documentation for your script. You auto-generate this README file from your script YML file using the platform-sdk generate-docs command. For more information see the documentation article


## HealthCheckIntegrations

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckMemory

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckNumberOfDroppedIncidents

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckParseResults

**Type:** script  
**Product:** System Diagnostics and Health Check  

This README contains the full documentation for your script. You auto-generate this README file from your script YML file using the platform-sdk generate-docs command. For more information see the documentation article


## HealthCheckPlaybookAnalysis

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckServerConfiguration

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckStart

**Type:** script  
**Product:** System Diagnostics and Health Check  

## HealthCheckSystemDiagnostics

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## HealthCheckWorkers

**Type:** script  
**Product:** System Diagnostics and Health Check  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## Hello World IAM

**Type:** integration  
**Product:** Hello World IAM  

This README contains the full documentation for your integration. You auto-generate this README file from your integration YML file using the platform-sdk generate-docs command. For more information see the integration documentation. An Identity and Access Management integration template

**Commands:**

- `iam-create-user`: Creates a user.
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Disable an active user.
- `get-mapping-fields`: Retrieves a User Profile schema, which holds all of the user fields within the application. Used for outgoing-mapping through the Get Schema option.


## Hello World v2

**Type:** integration  
**Product:** HelloWorld  
**Commands:**

- `helloworld-say-hello`: Prints hello to a specified name.


## HelloWorld

**Type:** integration  
**Product:** HelloWorld  

This is the Hello World integration for getting started

**Commands:**

- `helloworld-say-hello`: Hello command - prints hello to anyone.


## Hey

**Type:** script  
**Product:** Developer Tools  

Use rakyll/hey to test a web application with a load of requests

**Inputs:**

- `url`: URL to query.
- `requests_number`: Number of requests to run. Default is 200.
- `timeout`: Timeout for each request in seconds. Default is 20, use 0 for infinite.
- `concurrency`: Number of workers to run concurrently.
- `duration`: Duration of application to send requests (in seconds).
- `method`: HTTP method.
- `headers`: Custom HTTP header. Comma separated list of "key=value". e.g. Type=IP,Size=100.
- `disable_compression`: Disable compression.


## hideFieldsOnNewIncident

**Type:** script  
**Product:** Common Scripts  

Hides incident fields for new incidents (post application of the script), and displays it in edit mode

**Inputs:**

- `incident`: The incident object.
- `field`: The field definition object.


## HighlightWords

**Type:** script  
**Product:** Base  

Highlights words inside a given text

**Inputs:**

- `text`: The input text to highlight the words in.
- `terms`: Terms to highlight in the text. Can be words or sentences (without commas ","). Note: if you use a sentences and word, the word shouldn't be


## Host Lookup - Infoblox NIOS

**Type:** playbook  
**Product:** Infoblox NIOS  

This playbook looks up hosts info using Infoblox NIOS integration

**Inputs:**

- `hosts`: The optional comma-separated list of hosts to lookup.


## HostIo

**Type:** integration  
**Product:** HostIo  

Use the HostIo integration to enrich domains using the Host.io API. This integration was integrated and tested with version 1.0 of HostIo

**Commands:**

- `hostio-domain-search`: Returns a list of domains associated with a specific field, and the total number of these domains.
- `domain`: Returns Domain information.


## HPE Aruba ClearPass

**Type:** integration  
**Product:** HPE Aruba Clearpass  

Aruba ClearPass Policy Manager provides role and device-based network access control for employees, contractors, and guests across any multi-vendor wired, wireless, and VPN infrastructure. This integration was integrated and tested with version 6.9 of HPE Aruba ClearPass

**Commands:**

- `aruba-clearpass-endpoints-list`: Get a list of endpoints. An endpoint device is an Internet-capable hardware device on a TCP/IP network (e.g. laptops, smart phones, tablets, etc.)
- `aruba-clearpass-endpoint-update`: Updates some fields of an endpoint.
- `aruba-clearpass-attributes-list`: Get a list of attributes. Attributes allows you to specify unique sets of criteria for local users, guest users, endpoints, and devices. If no arguments were gi
- `aruba-clearpass-attribute-create`: Create a new attribute.
- `aruba-clearpass-attribute-update`: Update some fields of an attribute by the attribute's ID.
- `aruba-clearpass-attribute-delete`: Delete an attribute.
- `aruba-clearpass-active-sessions-list`: Get a list of active sessions.
- `aruba-clearpass-active-session-disconnect`: Disconnect active session.


## HtmlDifflabDynamic

**Type:** script  
**Product:** Suspicious Domain Hunting  
**Inputs:**

- `html1`: First HTML to compare.
- `html2`: Second HTML to compare.


## HtmlDifflibCheck

**Type:** script  
**Product:** Suspicious Domain Hunting  
**Inputs:**

- `html1`: First HTML to compare.
- `html2`: Second HTML to compare.


## HTMLtoMD

**Type:** script  
**Product:** Common Scripts  

Converts HTML to Markdown

**Inputs:**

- `html`: HTML to convert to Markdown.
- `escape_misc`: When set to False, will skip escaping of miscellaneous punctuation characters such as &, +, -.


## http

**Type:** script  
**Product:** Common Scripts  

Sends a HTTP request and returns the response as JSON

**Inputs:**

- `method`: The method for the http request.
- `body`: The body for the http request.
- `url`: The URL for the http request.
- `headers`: The headers for the http request, in the format of "key1:value1,key2:value2, ...".
- `insecure`: Trust any certificate (not secure).
- `unsecure`: Trust any certificate (not secure).
- `proxy`: Use the system proxy settings.
- `username`: The user for the http request.


## HTTPFeedApiModule

**Type:** script  

To use the common HTTP Feed API logic, run the following: feed_main is the main execution of the Feed API module. It can be extended or overriden in the integration main function. Note that the module expectes a feed_types parameter to extract the indicator. This is similar to the configuration in minemeld. See the module class docstring for an example


## HTTPListRedirects

**Type:** script  
**Product:** Common Scripts  

List the redirects for a given URL

**Inputs:**

- `url`: The URL to follow
- `useHead`: Should we use HEAD instead of GET. Safer but might not be the same response.
- `use_system_proxy`: Use system proxy settings
- `trust_any_certificate`: Trust any certificate (not secure)


## HttpV2

**Type:** script  
**Product:** Common Scripts  

Sends a HTTP request with advanced capabilities

**Inputs:**

- `url`: Specify where the request should be sent. Include the URI scheme ('http' or 'https').
- `method`: Specify the HTTP method to use.
- `headers`: Specify a hash of headers to send with the request.Headers can be of string type but need to be formatted in the following ways:`{"key1": "v
- `body`: Specify the body of the request.
- `request_content_type`: Specify the Content-Type header for the request.Shorthands are provided for the following common content types:json (application/json)xml (t
- `response_content_type`: Specify the Accept header for the request - the response content type.Shorthands are provided for the following common content types:json (a
- `parse_response_as`: Specify how you would like to parse the response.
- `auth_credentials`: Basic authorization. Please set values in the format: username,password. For Bearer token please use the headers.


## Hudsonrock

**Type:** integration  
**Product:** Hudsonrock  

Integration with Hudsonrock OSINT tools to check IP, Email or username usage

**Commands:**

- `ip`: Send IP reputation query.
- `email`: Send Email reputation query.
- `hudsonrock-get-username`: Send username reputation query.


## Humio

**Type:** integration  
**Product:** Humio  

Integration with Humio

**Commands:**

- `humio-query`: Query the data from Humio
- `humio-query-job`: Issue a query job to Humio
- `humio-poll`: Issue poll command to Humio
- `humio-delete-job`: Issue a job delete command to Humio
- `humio-list-alerts`: List alerts from Humio
- `humio-get-alert-by-id`: list alerts by id from Humio
- `humio-create-alert`: Create an alert in Humio
- `humio-list-notifiers`: List all notifiers in Humio
- `humio-delete-alert`: Delete alert in Humio
- `humio-get-notifier-by-id`: Get notifier from Humio by id


## Humio QueryJob Poll

**Type:** playbook  
**Product:** Humio  

Run and poll a Humio Query Job

**Inputs:**

- `Query`: The Humio Query to run
- `Interval`: The interval in minutes to poll the query job
- `Timeout`: The number of minutes before timing out
- `Repository`: The repository to query
- `Start`: The beginning of the interval to query
- `End`: The end of the interval to query
- `timeZoneOffsetMinutes`: The timezone offset in minutes between the platform and Humio server (usually 0)


## HYAS Insight

**Type:** integration  
**Product:** HYAS Insight  

HYAS Insight is a threat investigation and attribution solution that uses exclusive data sources and non-traditional mechanisms to improve visibility and productivity for analysts, researchers, and investigators while increasing the accuracy of findings. HYAS Insight connects attack instances and campaigns to billions of indicators of compromise to deliver insights and visibility. With an easy-to-use user interface, transforms, and API access, HYAS Insight combines rich threat data into a powerful research and attribution solution. HYAS Insight is complemented by the HYAS Intelligence team that helps organizations to better understand the nature of the threats they face on a daily basis. Use the HYAS Insight integration to interactively lookup PassiveDNS, DynamicDNS, WHOIS, Sample Malware Records, C2 Attribution, Passive Hash, SSL Certificate, Open Source Indicators, Device Geo, Sinkhole, Malware Sample Information

**Commands:**

- `hyas-get-passive-dns-records-by-indicator`: Returns PassiveDNS records for the provided indicator value.
- `hyas-get-dynamic-dns-records-by-indicator`: Returns DynamicDNS records for the provided indicator value.
- `hyas-get-whois-records-by-indicator`: Returns WHOIS records for the provided indicator value.
- `hyas-get-whois-current-records-by-domain`: Returns WHOIS Current records for the provided indicator value.
- `hyas-get-malware-samples-records-by-indicator`: Returns Malware Sample records for the provided indicator value.
- `hyas-get-c2attribution-records-by-indicator`: Return C2 Attribution records for the provided indicator value.
- `hyas-get-passive-hash-records-by-indicator`: Return passive hash records for the provided indicator value.
- `hyas-get-ssl-certificate-records-by-indicator`: Return SSL certificate records for the provided indicator value.
- `hyas-get-opensource-indicator-records-by-indicator`: Return Open Source intel records for the provided indicator value.
- `hyas-get-device-geo-records-by-ip-address`: Returns a list of mobile geolocation information
- `hyas-get-sinkhole-records-by-ipv4-address`: Returns sinkhole information.
- `hyas-get-malware-sample-information-by-hash`: Returns malware information.
- `hyas-get-associated-ips-by-hash`: Returns associated IP's for the provided hash value.
- `hyas-get-associated-domains-by-hash`: Returns associated Domain's for the provided hash value.


## IAMApiModule

**Type:** script  

To use the common IAM API logic, run the following command to import the IAMApiModule. Then, the IAMApiModule will be available for usage. For examples, see the Workday IAM or Okta IAM integrations. The IAMApiModule contains the following classes


## IBM MaaS360 Security

**Type:** integration  
**Product:** IBM MaaS360 Security  

This is the IBM MaaS360 Security integration for Cortex XSIAM

**Commands:**

- `ibm-maas360-security-get-events`: Gets events from IBM MaaS360 Security.


## IBM Security Guardium

**Type:** integration  
**Product:** IBM Guardium  

IBM Security Guardium is a comprehensive data security platform that provides visibility and protection for sensitive data across databases, data warehouses, big data platforms, and cloud environments. This integration enables the collection of security events from IBM Guardium Data Security Center

**Commands:**

- `ibm-guardium-get-events`: Manual command to fetch and display events.


## IBM Security Verify

**Type:** integration  
**Product:** IBM Security Verify  

IBM Security Verify provides a secure and scalable solution for collecting and managing security events from IBM Security Verify, offering advanced threat detection and response capabilities for protecting identities, applications, and data

**Commands:**

- `ibm-security-verify-get-events`: Retrieves events from IBM Security Verify.


## IBM X-Force Exchange v2

**Type:** integration  
**Product:** IBM X-Force Exchange  

IBM X-Force Exchange lets you receive threat intelligence about applications, IP addresses, URls and hashes

**Commands:**

- `ip`: IP to check
- `url`: Check the given URL reputation
- `file`: Check file reputation
- `domain`: Check domain reputation
- `cve-search`: Search for details about the given CVE
- `cve-latest`: Return the latest vulnerabilities found
- `xfe-whois`: Gets information about the given host address
- `xfe-search-cves`: Gets list of all vulnerabilities associated with the search term.


## iboss

**Type:** integration  
**Product:** iboss  

Manage block lists, manage allow lists, and perform domain, IP, and/or URL reputation and categorization lookups. This integration was integrated and tested with version 9.8.38.245 of iboss Zero Trust Secure Service Edge

**Commands:**

- `iboss-add-entity-to-allow-list`: Adds domains, IPs, and/or URLs to an allow list.
- `iboss-add-entity-to-block-list`: Adds domains, IPs, and/or URLs to a block list.
- `domain`: Lookup reputation for domain names.
- `ip`: Lookup reputation data for IP addresses.
- `iboss-remove-entity-from-allow-list`: Removes domains, IPs, and/or URLs from an allow list
- `iboss-remove-entity-from-block-list`: Removes domains, IPs, and/or URLs to a block list.
- `url`: Lookup reputation data for URLs.
- `iboss-add-entity-to-policy-layer-list`: Add entity to policy layer list.
- `iboss-remove-entity-from-policy-layer-list`: Remove entity from policy layer list.


## If-Elif

**Type:** script  
**Product:** Filters And Transformers  

The If-Elif transformer simulates a python "if elif else" tree using a JSON provided in the conditions argument. The JSON should be a list of dictionaries where all have the keys "condition", which holds a boolean expression, and "return", which holds the value to return if "condition" is evaluated to be true. To return a default value if all "condition"s were false, the last dictionary should have only the key "default" holding the valid JSON value. If this is not provided an empty string will be returned as a default. In order to prevent injections, context values should be retrieved from the value entered in the value (Get) of the transformer with the hash-curly brackets #{.} syntax. This syntax has the same behavior as the classic platform ${.} syntax and uses the the platform. To provide the full context to the transformer, use ${.} as the value (Get) argument. Note: when used as a "return" value, this syntax should not be surrounded by quotes. Comparison operators work like Python operators: Note: If a comparison is incomparable by nature (e.g., 'a' < 3), it will evaluate to false. Logical operators also follow the Python syntax: Regular expressions are implemented with the "regex_match" function, in the format: regex_match('pattern', 'string'). The behavior of the function is controlled with the flags argument. Literal strings should preferably be surrounded by single quotes. Do not use #{.} in a string, instead, use the + operator. For examp

**Inputs:**

- `value`: The object from which to grab values. For the full context use "${.}".
- `conditions`: A JSON formatted list, where all but the last items are dictionaries with the keys "condition" (holding a boolean expression) and "return" (
- `flags`: Flags to control comparison and regular expression behavior. Possible values are: case_insensitive, list_compare, regex_dot_all, regex_multi


## If-Then-Else

**Type:** script  
**Product:** Filters And Transformers  

A transformer for simple if-then-else logic

**Inputs:**

- `value`: The value to evaluate
- `equals`: (Deprecated) If value equals this
- `then`: Return this value if 'condition' is true
- `else`: Return this value if 'condition' is false
- `condition`: The condition expression to evaluate such as lhs==rhs or lhs!=rhs. Will evaluate as value==rhs if left empty for backward compatibility.
- `lhs`: The value to compare in the condition (left hand side)
- `rhs`: The value to compare in the condition (right hand side)
- `options`: Option flags (comma separated list): available options are `case_insensitive`, `regex_dot_all`, `regex_multiline`, `regex_full_match`, `inpu


## IgnoreFieldsFromJson

**Type:** script  
**Product:** Filters And Transformers  

A transformer to remove selected fields from the JSON object

**Inputs:**

- `value`: The primary value of the JSON object
- `fields`: Comma-separated fields/keys (without any whitespaces) that needs to be ignored from the JSON object.


## iLert

**Type:** integration  
**Product:** iLert  

iLert is a modern uptime platform with advanced on-call and alerting features. Alert and notify users using iLert. This integration was integrated and tested with API version 1 of iLert

**Commands:**

- `ilert-submit-event`: Creates a new event/incident in iLert (in order to use this command you have to enter the Integration Key in the integration settings)
- `iLert-acknowledge-event`: Acknowledges an existing event in iLert
- `ilert-resolve-event`: Resolves an existing event in iLert


## Image OCR

**Type:** integration  
**Product:** Image OCR  

Use the Image OCR integration to extract text from images. The integration utilizes the open-source tesseract OCR engine

**Commands:**

- `image-ocr-list-languages`: Lists supported languages for which the integration can extract text.


## imagecompare

**Type:** script  
**Product:** Suspicious Domain Hunting  
**Inputs:**

- `org_image`: Provide the Entry ID.
- `sec_image`: Provide the Entry ID.


## Impartner

**Type:** integration  
**Product:** Impartner  

Impartner is the fastest-growing, most award-winning channel management solution provider on the market. This integration was integrated and tested with version v1 of Impartner Objects API

**Commands:**

- `impartner-get-account-list`: Get account IDs from Impartner
- `impartner-get-account-id`: Get account details from Impartner


## Imperva Incapsula

**Type:** integration  
**Product:** Imperva Incapsula  

Uses incapsula to manage sites and IPs

**Commands:**

- `incap-add-managed-account`: Use this operation to add a new account that should be managed by the account of the API client (the parent account). The new account will be configured accordi
- `incap-list-managed-accounts`: Use this operation to get the list of accounts that are managed by account of the API client (the parent account).
- `incap-add-subaccount`: Use this operation to add a new sub account to be managed by the account of the API client (the parent account).
- `incap-list-subaccounts`: Use this operation to get a list of sub accounts that are managed by the account of the API client (the parent account).
- `incap-get-account-status`: Use this operation to get information about the account of the API client or one of its managed accounts.
- `incap-modify-account-configuration`: Use this operation to change the configuration of the account of the API client or one of its managed accounts.
- `incap-set-account-log-level`: Use this operation to change the account log configuration.
- `incap-test-account-s3-connection`: Use this operation to check that a connection can be created with your Amazon S3 bucket.
- `incap-test-account-sftp-connection`: Use this operation to check that a connection can be created with your SFTP storage.
- `incap-set-account-s3-log-storage`: Use this operation to configure your Amazon cloud storage. Once configured, Incapsula logs will be uploaded to the selected location.
- `incap-set-account-sftp-log-storage`: Use this operation to configure your SFTP server storage. Once configured, Incapsula logs will be uploaded to the selected location.
- `incap-set-account-default-log-storage`: Use this operation to have your logs saved on Incapsula servers. Once configured, the logs can be retrieved by API calls.
- `incap-get-account-login-token`: Tokens are used instead of user/password based authentication to log in to the Incapsula management console. Use this operation to generate a token for an accou
- `incap-delete-managed-account`: Use this operation to delete an account.
- `incap-delete-subaccount`: Use this operation to delete a sub account.


## Imperva Skyfence

**Type:** integration  
**Product:** Imperva Skyfence  

The Imperva Skyfence Cloud Gateway is a Cloud Access Security Broker (CASB) that provides visibility and control over sanctioned and unsanctioned cloud apps to enable their safe and productive use. This integration was integrated and tested with version 1.0.8 of Imperva Skyfence

**Commands:**

- `imp-sf-list-endpoints`: Returns a list of, and basic details for, all managed and un-managed endpoints.
- `imp-sf-set-endpoint-status`: Updates the status (enroll or revoke) of an endpoint. You can run this command on an endpoint with any status, but the most common use case is endpoints with a 


## Imperva WAF

**Type:** integration  
**Product:** Imperva WAF  

Use the Imperva WAF integration to manage IP groups and Web security policies in Imperva WAF. This integration was integrated and tested with version 14.2 of Imperva WAF and based on Imperva On-Premises WAF (SecureSphere) REST API

**Commands:**

- `imperva-waf-ip-group-list`: Get a list of existing IP Group names.
- `imperva-waf-ip-group-list-entries`: Get a list of the entries in the requested IP group.
- `imperva-waf-ip-group-remove-entries`: Remove all the entries from an IP Group indicated by group name.
- `imperva-waf-sites-list`: Returns a list of the names of all sites in the system.
- `imperva-waf-server-group-list`: Returns a list of all server group names under the site.
- `imperva-waf-server-group-list-policies`: Get server groups applied web security policies.
- `imperva-waf-web-service-custom-policy-list`: Returns a list of names of all Web Application Custom Policies in the system.
- `imperva-waf-web-service-custom-policy-get`: Returns a Web Application Custom Policy indicated by policy name.
- `imperva-waf-ip-group-create`: Create an IP Group.
- `imperva-waf-ip-group-update-entries`: Add or remove rows in an IP Group indicated by ip Group Name.
- `imperva-waf-ip-group-delete`: Delete a IP Group indicated by group name.
- `imperva-waf-web-service-custom-policy-create`: Create a Web Service Custom Policy.
- `imperva-waf-web-service-custom-policy-update`: Update a Web Service Custom Policy.
- `imperva-waf-web-service-custom-policy-delete`: Delete a Web Service Custom Policy indicated by policy name.


## ImportMLModel

**Type:** script  
**Product:** Machine Learning  

Imports a file that contains an ML model

**Inputs:**

- `entryID`: ID of the entry that contains the ML model to import.
- `modelName`: The model name in which the ML model will be saved.
- `modelStoreType`: The method for storing the imported model.


## ImpSfListEndpoints

**Type:** script  
**Product:** Imperva Skyfence  

Enables a clients application to receive a list of all managed and unmanaged endpoints, with their basic details. This list can then be externally filtered or searched by the application to identify individual endpoints that might require action. For any such endpoint, the application can obtain fuller details (see Endpoint Details Request below) and if relevant change its enrollment status


## ImpSfRevokeUnaccessedDevices

**Type:** script  
**Product:** Imperva Skyfence  

Gets all of a devices data from the server. If a device hasen't been accessed in two months or more (and is still managed), the script will send the corresponding user a warning mail. If the device hasn't been accessed to in over three months, the script will revoke the device credentials and notify the user by mail


## ImpSfScheduleTask

**Type:** script  
**Product:** Imperva Skyfence  

Creates a schedule task that's called ImpSfRevokeUnaccessedDevices. Gets all of a device's data from the server. If a device hasn't been accessed in over two months (and is still managed), the script will send the corresponding user a warning mail. If the device hasn't been accessed in over three months, the script will revoke the device credentials and notify the user by mail

**Inputs:**

- `cron`: The interval between each check (in cron format).
- `times`: The number of times to execute the check.


## ImpSfSetEndpointStatus

**Type:** script  
**Product:** Imperva Skyfence  

Enables a clients application to enroll an endpoint or revoke its enrollment. This is usually relevant for endpoints with pending status but can be applicable to endpoints with any current status. The endpoint needs to be specified by its ID, which have been received from an endpoint list request, from a new endpoint notification, or from any other implemented manual or automated input

**Inputs:**

- `endpointId`: The ID of the endpoint.
- `action`: Whether to "enroll" or "revoke".


## IncapGetAppInfo

**Type:** script  
**Product:** Imperva Incapsula  

Retrieves a list of all the clients applications


## IncapListSites

**Type:** script  
**Product:** Imperva Incapsula  

Lists the sites for an account

**Inputs:**

- `account_id`: The numeric identifier of the account to operate on. If this is not specified, the operation will be performed on the account identified by 
- `page_size`: The number of objects to return in the response. The default is 50.
- `page_num`: The page to return starting from 0. The default is 0.


## IncapScheduleTask

**Type:** script  
**Product:** Imperva Incapsula  

Periodically runs the IncapWhitelistCompliance script, which queries the Incapsula monitored websites for white-list compliance (see script for further details). The script then saves the new periodic ID into incident context under the ScheduleTaskID key for later use

**Inputs:**

- `SSHValidationServer`: The name of the non-allow listed server RemoteAccess instance.
- `cron`: The interval between each check (in cron format).
- `times`: The number of times to execute the check.


## IncapWhitelistCompliance

**Type:** script  
**Product:** Imperva Incapsula  

Get all sites from Incapsula. For each site, the script, through a ssh server (one that should NOT be in the allow list), make sure the site is compliant ( allow list is being enforced ). If not, a warning mail will be sent to the domain owner

**Inputs:**

- `SSHValidationServer`: Name of the non-allow list SSH server instance


## IncidentAddSystem

**Type:** script  
**Product:** Common Scripts  

Adds a remote system (such as a desktop under investigation) to an investigation. This allows you to install an agent on the system

**Inputs:**

- `name`: The unique name that will be used in the investigation. (default)
- `username`: The user name in the remote system.
- `host`: The host IP address or network identifiable name. (mandatory)
- `workgroup`: The workgroup or domain of the user.
- `password`: The users password used to log in to the remote system. By default you will be prompted to enter the password once you hit enter. However, t
- `credentialSet`: The credentials to be chosen to apply to the system (instead of username & password).
- `dmbPort`: The non-standard SMB port to be chosen.
- `sshPort`: The non-standard SSH port to be chosen. The default is 22.


## IncidentFields

**Type:** script  
**Product:** Common Scripts  

Returns a dict of all incident fields that exist in the system

**Inputs:**

- `exclude_system_fields`: Whether to only return non-system fields. If "true", will only output non-system fields. The default value is "false".
- `short_names`: Whether to shorten the incident field names. If "true", will cause output to use shortened field names. The default value is "true".


## IncidentsCheck-NumberofIncidentsNoOwner

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Health Check dynamic section, showing the number of unassigned incidents


## IncidentsCheck-NumberofIncidentsWithErrors

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Health Check dynamic section, showing the number of failed incidents


## IncidentsCheck-NumberofTotalEntriesErrors

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Health Check dynamic section, showing the total number of errors in failed incidents


## IncidentsCheck-PlaybooksFailingCommands

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Health Check dynamic section, showing the top ten commands of the failed incidents in a pie chart


## IncidentsCheck-PlaybooksHealthNames

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Health Check dynamic section, showing the top ten playbook names of the failed incidents in a bar chart


## IncidentsCheck-Widget-CommandsNames

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Data output script for populating the dashboard pie graph widget with the top failing incident commands


## IncidentsCheck-Widget-CreationDate

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Data output script for populating the dashboard line graph widget with the creation date of failing incidents


## IncidentsCheck-Widget-IncidentsErrorsInfo

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Data output script for populating the dashboard table graph widget with the information about failing incidents


## IncidentsCheck-Widget-NumberFailingIncidents

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Data output script for populating dashboard number graph widget with the number of failing incident


## IncidentsCheck-Widget-NumberofErrors

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Data output script for populating the dashboard number graph widget with the number of entries ID errors


## IncidentsCheck-Widget-PlaybookNames

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Data output script for populating the dashboard bar graph widget with the top failing playbooks name


## IncidentsCheck-Widget-UnassignedFailingIncidents

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Data output script for populating the dashboard number graph widget with the number of unassigned failing incidents


## IncidentState

**Type:** script  
**Product:** Change Management  

This script is used as dynamic section to desplay in the layout one of the incident state below: 1 - Request Was Approved 2 - Request Was Submitted 3 - Awaiting Request Owner Validation 4 - FW Policy Was Updated 5 - Request Was Rejected


## IncOwnerToBonuslyUser

**Type:** script  
**Product:** Bonusly  

This script gets the email address of the incident owner and then returns the incident owner username in Bonusly

**Inputs:**

- `json`: Enter JSON STRING like {'email@company':'@bonuslyuser'}
- `owner`: The username of the the platform. This will look up the incident owner's email address.


## IncreaseIncidentSeverity

**Type:** script  
**Product:** Common Scripts  

Optionally increases the incident severity to the new value if it is greater than the existing severity

**Inputs:**

- `severity`: The incident severity to increase the incident to. Can be "Unknown", "Informational", "Low", "Medium", "High", "Critical", "0", "0.5", "1", 


## Indeni

**Type:** integration  
**Product:** Indeni  
**Commands:**

- `indeni-get-device-info`: get the device information
- `indeni-get-alert-info`: get detailed alert info
- `indeni-get-alert-summary`: gets summary of given alert type for all devices
- `indeni-post-note`: Post a note to a given issue id
- `indeni-archive-issue`: Archive an issue for the given alert id
- `indeni-unarchive-issue`: Unarchive an existing issue
- `indeni-get-notes`: Gets the notes from issue


## Indicator Enrichment - Censys

**Type:** playbook  
**Product:** Censys  

This playbook enriches the IP addresses, domains, and SHA256 file hashes indicators with Censys threat intelligence data

**Inputs:**

- `ip_addresses`: Specify the IP address(es) to enrich.
- `domains`: Specify the domain(s) to enrich.
- `file_hashes`: Specify the SHA256 file hash(es) to enrich.


## Indicator Pivoting - DomainTools Iris

**Type:** playbook  
**Product:** DomainTools Iris Investigate  

Gathers data through pivots that share a common attribute with a domain. For instance, pivoting on an IP address will give you back all domains related to that IP address

**Inputs:**

- `IPAddress`: The IP address to pivot.
- `EmailAddress`: The Email address for which to pivot.
- `NameServerIPAddress`: The name server IP address for which to pivot.
- `SSLHash`: The SSL Hash for which to pivot.
- `NameServerHostName`: The name server host name for which to pivot.
- `MailServerHostName`: The mail server host name for which to pivot.
- `IPAddressCount`: The number of matches for the IP address.
- `EmailAddressCount`: The number of matches for the email address.


## indicator-enrichment

**Type:** script  
**Product:** Aggregated Scripts  

Enriches indicators from a provided list or a block of free text. This script detects the indicator type and runs the correct underlying enrichment script. Currently supports: IP, URL, Domain, CVE, and File

**Inputs:**

- `indicator_list`: Accepts a list of indicators to enrich.- From CLI: Provide a comma-separated list. If an indicator contains a comma, wrap the indicators in 
- `text`: Free text to be parsed for indicators. The script will run !extractIndicators to retrieve the underlying indicators within the text.
- `external_enrichment`: Whether to call external integrations for enrichment: - 'true': enrich using enabled external integrations (e.g., VirusTotal (API v3), Alien
- `brands`: A comma separated list of integration brands to run enrichment against. Example: `"VirusTotal (API v3), AlienVault OTX v2"`.- If provided, o
- `additional_fields`: When set to true, the output for each enrichment command includes an `AdditionalFields` object for each of the indicator results. `Additiona
- `raw_context`: If true, will also append the underlying enrichment command outputs to the context. (For backwards compatibility).
- `ignore_indicator_limit`: By default, the script enforces a 100 indicator limit to maintain performance. If more than 100 unique indicators are found, the script will


## IndicatorMaliciousRatioCalculation

**Type:** script  
**Product:** Common Scripts  

Returns indicators that appear under resolved incidents, and resolved incident IDs

**Inputs:**

- `maxIncidents`: The maximum number of incidents to query.
- `maxIndicators`: The maximum number of indicators to query.
- `appearsInMinNumberOfIncidents`: The indicator that appears in the minimum number of incidents.
- `query`: The query to fetch the indicators from. The incident which are "bad".
- `maxDisplayResults`: The maximum number of results (indicators) to display as output.
- `fileResult`: The generate file result.
- `fromDate`: The start date by which to filter incidents.


## Indicators detection

**Type:** integration  
**Product:** Core  

The Cortex Core - IOCs integration uses the Cortex API for detection and response, by natively integrating network, endpoint, and cloud data to stop sophisticated attacks

**Commands:**

- `core-iocs-sync`: Sync your IOC with Cortex and delete the previous version.
- `core-iocs-push`: Push modified IOCs to Cortex.
- `core-iocs-set-sync-time`: Set sync time manually (Do not use this command unless you unredstandard the consequences).
- `core-iocs-create-sync-file`: Creates the sync file for the manual process. Run this command when instructed by the Cortex support team.
- `core-iocs-enable`: Enables IOCs in the Cortex tenant.
- `core-iocs-disable`: Disables IOCs in the Cortex tenant.


## Indicators-type

**Type:** script  
**Product:** RDPCacheHunting  

Indicator's Types dynamic section, showing the top ten types of IOCs found in the RDP session's cache


## InferWhetherServiceIsDev

**Type:** script  
**Product:** Cortex Attack Surface Management  

Identify whether the service is a "development" server. Development servers have no external users and run no production workflows. These servers might be named "dev", but they might also be named "qa", "pre-production", "user acceptance testing", or use other non-production terms. This automation uses both public data visible to anyone (active_classifications as derived by Xpanse ASM) as well as checking internal data for AI-learned indicators of development systems (asm_tags as derived from integrations with non-public systems)

**Inputs:**

- `asm_tags`: Array of key-value objects. Each object within the array must contain the keys "Key" and "Value" to be considered. The values associated wit
- `active_classifications`: Array of strings representing the Xpanse ASM "active classifications" for the service. Example: ["RdpServer", "SelfSignedCertificate"].
- `hierarchy_info`: Infrastructure hierarchy information to include CSPs (such GCP folder, AWS account and Azure subscription names, which can indicate the envi
- `provider`: Provider of the asset as returned by Xpanse.


## Infinipoint

**Type:** integration  
**Product:** Infinipoint  
**Commands:**

- `infinipoint-get-vulnerable-devices`: Get Vulnerable Devices
- `infinipoint-get-assets-programs`: infinipoint get assets programs
- `infinipoint-get-cve`: infinipoint get cve
- `infinipoint-get-device`: get device
- `infinipoint-get-tag`: get tag
- `infinipoint-get-networks`: get networks
- `infinipoint-get-assets-devices`: get assets hardware
- `infinipoint-get-assets-cloud`: get assets cloud
- `infinipoint-get-assets-users`: get assets users
- `infinipoint-get-action-results`: get action
- `infinipoint-get-queries`: get queries
- `infinipoint-execute-action`: run queries
- `infinipoint-get-non-compliance`: get non compliance devices
- `infinipoint-get-device-details`: get device details
- `infinipoint-get-compliance-status`: get compliance status


## Infoblox NIOS

**Type:** integration  
**Product:** Infoblox NIOS  

Infoblox NIOS enables you to receive metadata about IPs in your network and manages the DNS Firewall by configuring RPZs. It defines RPZ rules to block DNS resolution for malicious or unauthorized hostnames, or redirect clients to a walled garden by substituting responses. This integration was integrated and tested with version V2 of Infoblox

**Commands:**

- `infoblox-get-ip`: Get IP information.
- `infoblox-search-related-objects-by-ip`: Searches IP related objects by a given IP.
- `infoblox-list-response-policy-zone-rules`: Lists all response policy rules that belong to the given response policy zone.
- `infoblox-list-response-policy-zones`: List all response policy zones.
- `infoblox-create-response-policy-zone`: Creates a response policy zone.
- `infoblox-create-rpz-rule`: Creates a response policy rule.
- `infoblox-create-a-substitute-record-rule`: Creates a substitute record rule.
- `infoblox-create-aaaa-substitute-record-rule`: Creates a substitute rule for an AAAA record.
- `infoblox-create-mx-substitute-record-rule`: Creates a substitute rule for the MX record.
- `infoblox-create-naptr-substitute-record-rule`: Creates a substitute rule for a NAPTR record.
- `infoblox-create-ptr-substitute-record-rule`: Creates a substitute rule of the PTR record.
- `infoblox-create-srv-substitute-record-rule`: Creates a substitute rule of a SRV record.
- `infoblox-create-txt-substitute-record-rule`: Create a substitute rule for a txt record.
- `infoblox-create-ipv4-substitute-record-rule`: Create a substitute rule for an IPv4 rule.
- `infoblox-create-ipv6-substitute-record-rule`: Creates a substitute of the IPv6 record rule.


## Infocyte

**Type:** integration  
**Product:** Infocyte  

Infocyte can pivot off incidents to automate triage, validate events with forensic data and enabling dynamic response actions against any or all host using both agentless or agented endpoint access. This integration was integrated and tested with version 3008.0.1.2800 of Infocyte

**Commands:**

- `infocyte-scan-host`: Kicks off a Scan (forensic collection) against an endpoint
- `infocyte-isolate-host`: Isolates a host to only communicate to Infocyte and other security tools
- `infocyte-restore-host`: Restore an isolated host
- `infocyte-kill-process`: Kills a process on target endpoint
- `infocyte-run-response`: Runs the named Infocyte extension on target host. Extensions are Infocyte script modules that run against a host or set of hosts to either collect additional da
- `infocyte-get-taskstatus`: Gets status of an Infocyte task (scan, response action, etc.)
- `infocyte-get-scanresult`: Retrieve metadata and results for a scan against multiple hosts
- `infocyte-get-hostscanresult`: Retrieve results for a scan on a target host
- `infocyte-get-responseresult`: Gets the results of a response action.
- `infocyte-get-alerts`: Retrieve alert by alertId, since a lastAlertId, since LastRun (if no arguments provided)


## InRange

**Type:** script  
**Product:** Filters And Transformers  

Checks if the left side is in range of the right side (from,to anotation). Example - InRange left=4right=1,8 will return true

**Inputs:**

- `left`: The value to check, if it is in range. For example, 4.
- `right`: The range to check against with the form of from,to. For example, 2,8.


## InstancesCheck-FailedCategories

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Health Check dynamic section, showing the top ten categories of the failed integrations in a pie chart


## InstancesCheck-NumberofEnabledInstances

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Health Check dynamic section, showing the total number of checked integrations


## InstancesCheck-NumberofFailedInstances

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Health Check dynamic section, showing the total number of failed integrations


## IntegrationsCheck-Widget-IntegrationsCategory

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Data output script for populating the dashboard pie graph widget with the failing integrations


## IntegrationsCheck-Widget-IntegrationsErrorsInfo

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Data output script for populating the dashboard table graph widget with the information about failing integrations


## IntegrationsCheck-Widget-NumberChecked

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Data output script for populating the dashboard number graph widget with the number of checked integrations


## IntegrationsCheck-Widget-NumberFailingInstances

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Data output script for populating the dashboard number graph widget with the number of failing integrations


## Intezer - Analyze Uploaded file

**Type:** playbook  
**Product:** Intezer  

Uploads a file to Intezer Analyze to analyze and enrich the file reputation. (up to 150 MB)

**Inputs:**

- `File`: The file object of the file to detonate.
- `Interval`: How often the polling command should run (in minutes).
- `Timeout`: The amount of time to wait before a timeout occurs (in minutes).


## Intezer v2

**Type:** integration  
**Product:** Intezer  

Use the Intezer v2 integration to detect and analyze malware, based on code reuse

**Commands:**

- `intezer-analyze-by-hash`: Checks file reputation of the given hash, supports SHA256, SHA1 and MD5
- `intezer-get-latest-report`: Checks file reputation of the given hash, supports SHA256, SHA1 and MD5 by looking at the latest available report
- `intezer-analyze-by-file`: Checks file reputation for uploaded file (up to 150MB)
- `intezer-get-endpoint-analysis-result`: Check the endpoint analysis status and get analysis result, supports polling.
- `intezer-get-url-analysis-result`: Check the url analysis status and get analysis result, supports polling.
- `intezer-get-file-analysis-result`: Check the file analysis status and get analysis result, supports polling.
- `intezer-get-analysis-result`: Check the analysis status and get analysis result, support file and endpoint analysis
- `intezer-get-sub-analyses`: Get a list of the analysis sub analyses
- `intezer-get-family-info`: Get family information from Intezer Analyze
- `intezer-get-analysis-code-reuse`: Get All code reuse report for an analysis or sub analysis To get the code reuse results of a sub analysis you also must specify the "parent analysis",
- `intezer-get-analysis-metadata`: Get metadata for an analysis or sub analysis To get the metadata of a sub analysis you also must specify the "parent analysis",
- `intezer-get-analysis-iocs`: Gets the list of network and files IOCs of a specific analysis id.
- `intezer-submit-alert`: Submit a new alert, including the raw alert information, to Intezer for processing.
- `intezer-submit-suspected-phishing-email`: Submit a suspicious phishing email in a raw format (.MSG or .EML) to Intezer for processing.
- `intezer-get-alert-result`: Get an ingested alert triage and response information using alert ID.


## IntezerRunScanner

**Type:** script  
**Product:** Intezer  

Runs the Intezer Endpoint Analysis scanner

**Inputs:**

- `api_key`: The Intezer API key.
- `endpoint_analysis_id`: The endpoint analysis ID.


## IntezerScanHost

**Type:** script  
**Product:** Intezer  

Runs the Intezer Endpoint Analysis scanner

**Inputs:**

- `intezer_api_key`: The Intezer API key.
- `hosts`: Computer name.
- `os`: OS.


## InvertEveryTwoItems

**Type:** script  
**Product:** Community Common Scripts  

This transformer will invert every two items in an array. Example: ["A", "B", "C", "D"] Result: ["B", "A", "D", "C"] If the total of items in the array is an odd number the last item will be removed Example: ["A", "B", "C", "D", "E"] Result: ["B", "A", "D", "C"] If the item is not an array the output will be same passed object

**Inputs:**

- `value`: 


## Investigation & Response

**Type:** integration  
**Product:** Core  

The Cortex Core IR integration uses the Cortex API for detection and response, by natively integrating network, endpoint, and cloud data to stop sophisticated attacks

**Commands:**

- `core-isolate-endpoint`: Isolates the specified endpoint.
- `core-unisolate-endpoint`: Reverses the isolation of an endpoint.
- `core-get-endpoints`: Gets a list of endpoints, according to the passed filters. If there are no filters, all endpoints are returned. Filtering by multiple fields will be concatenate
- `core-get-distribution-versions`: Gets a list of all the agent versions to use for creating a distribution list.
- `core-create-distribution`: Creates an installation package. This is an asynchronous call that returns the distribution ID. This does not mean that the creation succeeded. To confirm that 
- `core-get-distribution-url`: Gets the distribution URL for downloading the installation package.
- `core-get-create-distribution-status`: Gets the status of the installation package.
- `core-get-audit-management-logs`: Gets management logs. You can filter by multiple fields, which will be concatenated using the AND condition (OR is not supported). Maximum result set size is 10
- `core-get-audit-agent-reports`: Gets agent event reports. You can filter by multiple fields, which are combined using an AND condition (OR is not supported). The maximum result set size is 100
- `core-blocklist-files`: Blocks requested files that are not already on the block list or the allow list.
- `core-allowlist-files`: Adds requested files to the allow list if they are not already on the block list or the allow list.
- `core-quarantine-files`: Quarantines a file on selected endpoints. You can select up to 1000 endpoints.
- `core-get-quarantine-status`: Retrieves the quarantine status of a selected file.
- `core-restore-file`: Restores a quarantined file on the requested endpoints.
- `core-endpoint-scan`: Runs a scan on a selected endpoint. To scan all endpoints, use the argument all=true. Scanning all endpoints may affect performance and cause latency.


## InvestigationDetailedSummaryParse

**Type:** script  
**Product:** Malware Investigation and Response  

This script parses attacks from context and shows them according to the MITRE technique they use. The MITRE ATT&CK v2 pack (v1.1.0 or newer) is required for this automation to run properly


## InvestigationDetailedSummaryToTable

**Type:** script  
**Product:** Malware Investigation and Response  

This script shows InvestigationDetailedSummaryParse results as a Markdown table. NOTE: This script assumes the results of InvestigationDetailedSummaryParse are stored in the malwaredetailedinvestigationsummary incident field


## InvestigationSummaryParse

**Type:** script  
**Product:** Malware Investigation and Response  

Retrieves information from previously run reputation commands and aggregates their results


## InvestigationSummaryToTable

**Type:** script  
**Product:** Malware Investigation and Response  

Creates a human readable table from context results of InvestigationSummaryParse


## IP Lookup - Infoblox NIOS

**Type:** playbook  
**Product:** Infoblox NIOS  

This playbook looks up IP addresses using Infoblox NIOS integration

**Inputs:**

- `ip_addresses`: The optional comma-separated list of IP addresses to lookup.


## IP Reputation-GreyNoise

**Type:** playbook  
**Product:** GreyNoise  

Playbook for the ip reputation command Supported the platform.0.0 and later

**Inputs:**

- `IP`: The IP address to get reputation of.


## ip-enrichment

**Type:** script  
**Product:** Aggregated Scripts  

Enriches IP indicators with reputation data from multiple integrations and outputs a consolidated IPEnrichment object. This script exclusively supports indicators of type IPv4 (IPv6 is not supported) and will automatically create the indicator in TIM if it is not already exists. Note: If enabled, get-endpoint-data is executed only for internal IP addresses. Note: This script is supported in the platform.0 and later, and in Cortex XSIAM

**Inputs:**

- `ip_list`: A comma-separated list of IPv4 addresses to enrich.
- `external_enrichment`: Whether to call external integrations for enrichment: - 'true': enrich using enabled external integrations (e.g., VirusTotal (API v3), Alien
- `verbose`: Retrieve a human-readable entry for each command; if false, only the final result is summarized and errors are suppressed.
- `brands`: A list of integration brands to run enrichment against. Example: `"VirusTotal (API v3), AlienVault OTX v2"`.- If provided, only the selected
- `additional_fields`: When set to true, the output includes an `AdditionalFields` objectfor each of the indicator result. `AdditionalFields` contains all fields r


## IP2LocationIO

**Type:** integration  
**Product:** IP2LocationIO  

IP2Location.io integration to query IP geolocation data

**Commands:**

- `ip`: Return IP information and reputation


## IPCalcCheckSubnetCollision

**Type:** script  
**Product:** Community Common Scripts  

An automation script to return subnet collision result

**Inputs:**

- `subnet_one`: First subnet
- `subnet_two`: Second subnet


## IPCalcReturnAddressBinary

**Type:** script  
**Product:** Community Common Scripts  

An automation script to return address in binary format

**Inputs:**

- `ip_address`: Address to use


## IPCalcReturnAddressIANAAllocation

**Type:** script  
**Product:** Community Common Scripts  

An automation script to return address IANA information

**Inputs:**

- `ip_address`: Address to use


## IPCalcReturnSubnetAddresses

**Type:** script  
**Product:** Community Common Scripts  

An automation script to return subnet addresses

**Inputs:**

- `subnet`: Subnet to use


## IPCalcReturnSubnetBroadcastAddress

**Type:** script  
**Product:** Community Common Scripts  

An Automation Script to return subnet broadcast address

**Inputs:**

- `subnet`: Subnet to use


## IPCalcReturnSubnetNetwork

**Type:** script  
**Product:** Community Common Scripts  

An Automation Script to return subnet network ID

**Inputs:**

- `subnet`: Subnet to use


## IPinfo v2

**Type:** integration  
**Product:** Ipinfo  

Use the IPinfo.io API to get data about an IP address

**Commands:**

- `ip`: Check IP reputation (when information is available, returns a JSON with details). Uses all configured Threat Intelligence feeds.


## IPNetwork

**Type:** script  
**Product:** Common Scripts  

Gather information regarding CIDR -

**Inputs:**

- `cidr`: IP/CIDR, e.g. 192.168.0.0/24


## IPReputation

**Type:** script  
**Product:** Common Scripts  

A context script for IP address entities

**Inputs:**

- `ip`: The IP address to look up.


## ipstack

**Type:** integration  
**Product:** Ipstack  

One of the leading IP to geolocation APIs and global IP database services

**Commands:**

- `ip`: Queries an IP address in ipstack.


## IPToHost

**Type:** script  
**Product:** Common Scripts  

Gets the hostname correlated with the inputed IP address

**Inputs:**

- `ip`: The IP address to check.


## IPv4Blacklist

**Type:** script  
**Product:** Filters And Transformers  

Transformer that returns a filtered list of IPv4 addresses, based on whether they do not match a comma-separated list of IPv4 ranges. Useful for filtering out internal IP address space

**Inputs:**

- `value`: Array or comma-separated list of IPv4 addresses to filter.
- `cidr_ranges`: Array or comma-separated list of IPv4 ranges, in CIDR notation, against which to match the IPv4 addresses.


## IPv4Whitelist

**Type:** script  
**Product:** Filters And Transformers  

Transformer that returns a filtered list of IPv4 addresses, based on whether they match a comma-separated list of IPv4 ranges. Useful for filtering in internal IP address space

**Inputs:**

- `value`: Array or comma-separated list of IPv4 Addresses to filter.
- `cidr_ranges`: Array or comma-separated list of IPv4 ranges, in CIDR notation, against which to match the IPv4 addresses.


## IQ-HUB Automation

**Type:** playbook  
**Product:** Confluera  

This playbook simulates data fetching process from Confluera's IQ-Hub portal, using "Confluera" integration


## IqHubLog

**Type:** script  
**Product:** Confluera  

!IqHubLog


## IRIS DFIR

**Type:** integration  
**Product:** IRIS DFIR  

IRIS is a collaborative platform aiming to help incident responders to share technical details during investigations. It's free and open-source. This integration was integrated and tested with version v2.3.6 of IRIS DFIR

**Commands:**

- `iris-get-last-case-id`: IRIS Command to get the last case information
- `iris-get-all-cases`: Return a list of all IRIS DFIR cases
- `iris-close-case-id`: Close a specific case by ID.
- `iris-reopen-case-id`: Reopen a specific case by ID.
- `iris-change-case-state`: Change case state status
- `iris-create-notes-group`: Creates notes group
- `iris-add-new-note-to-group`: Add a new note to an existing group.
- `iris-get-list-of-groups-and-notes`: Get a list of the notes and groups.
- `iris-get-list-of-iocs`: Returns a list of IOCs as well as any existing linked with other cases.
- `iris-get-ioc-content`: Fetch the content of an ioc.


## Ironscales

**Type:** integration  
**Product:** Ironscales  

IRONSCALES, a self-learning email security platform integration

**Commands:**

- `ironscales-get-incident`: Get incident data by ID.
- `ironscales-classify-incident`: Classify incident by ID.
- `ironscales-get-open-incidents`: Get open incident ids.


## Ironscales-Classify-Incident

**Type:** playbook  
**Product:** Ironscales  

## IsMalicious

**Type:** integration  
**Product:** IsMalicious  

Enrich IP, domain, URL and file-hash indicators with IsMalicious reputation, evidence and data-trust context. This integration uses the public IsMalicious REST API contract. Local validation uses synthetic provider responses and the real CommonServerPython framework; no production the platform. API checks consume the applicable account quota. Unknown hashes, delisted indicators and absent supported verdicts remain DBotScore 0; risk and confidence are separate fields. See the pack README for evidence interpretation and limits

**Commands:**

- `ip`: Enrich ip indicators with IsMalicious evidence. At most 50 values per command.
- `domain`: Enrich domain indicators with IsMalicious evidence. At most 50 values per command.
- `url`: Enrich url indicators with IsMalicious evidence. At most 50 values per command.
- `file`: Enrich MD5, SHA1 or SHA256 hashes with IsMalicious evidence. At most 50 values per command.


## Ivanti Heat

**Type:** integration  
**Product:** Ivanti Heat  

Ivanti Heat service manager This integration was integrated and tested with version 2020.1.0.20200313 of Ivanti Heat

**Commands:**

- `ivanti-heat-objects-list`: Fetches business object records based on the defined filter values.
- `ivanti-heat-object-update`: Update details of a business object such as a change, problem, or incident.
- `ivanti-heat-object-delete`: Delete a business object such as a change, problem, or incident by its Record ID.
- `ivanti-heat-object-attachment-download`: Get attachments from business objects by attachment ID.
- `ivanti-heat-object-attachment-upload`: Upload attachments to business objects.
- `ivanti-heat-object-perform-action`: Performs quick actions for a business object. For example, close, clone or resolve an incident or a problem.
- `ivanti-heat-object-create`: create business objects available out-of-the-box, such as a Change, Problem, Incident, or any custom defined business object of your choice.


## IvantiHeatCloseIncidentExample

**Type:** script  
**Product:** Ivanti Heat  

This is a sample script that demonstrates how to close an incident in Ivanti Heat. The script generates data of the closed incident in JSON format and writes it to the IvantiHeat.CloseIncidentJSON context path

**Inputs:**

- `rec_id`: Incident object ID.


## IvantiHeatCreateIncidentExample

**Type:** script  
**Product:** Ivanti Heat  

This is a sample script that demonstrates how to create an incident in Ivanti Heat. The script generates data of the created incident in JSON format and writes it to the IvantiHeat.CreateIncidentJSON context path

**Inputs:**

- `category`: Incident category.
- `service`: Incident service.
- `owner`: Incident owner.
- `team`: Incident owner team.
- `summary`: Incident subject.
- `description`: Incident description.
- `customer`: Incident customer.


## IvantiHeatCreateProblemExample

**Type:** script  
**Product:** Ivanti Heat  

This is a sample script that demonstrates how to create a problem in Ivanti Heat. The script generates data of the created problem in JSON format and writes it to the IvantiHeat.CreateProblemJSON context path

**Inputs:**

- `owner`: Problem owner.
- `source`: Problem source.
- `status`: Problem status.
- `category`: Problem category.
- `subject`: Problem subject.
- `description`: Problem description.


## iZOOlogic

**Type:** integration  
**Product:** iZOOlogic  

Fetches and manages incidents from iZOOlogic, enabling automated ingestion, incident creation, and advanced filtering for brand protection and threat management

**Commands:**

- `izoologic-get-events`: Gets events from iZOOlogic. Use this command for development and debugging only, as it may produce duplicate events, exceed API rate limits, or disrupt the fetc
- `izoologic-incident-create`: Creates a new security incident in iZOOlogic.
- `izoologic-incident-fetch`: Fetches incidents from iZOOlogic based on specified filters including date range, brand, incident type, and other criteria.


## Ja3er

**Type:** integration  
**Product:** Ja3er  

Query the ja3er API for MD5 hashes of JA3 fingerprints

**Commands:**

- `ja3-search`: Search for "User-Agents" matching an MD5 hash of a JA3 fingerprint.


## JAMF v2

**Type:** integration  
**Product:** Jamf  

Enterprise Mobility Management (EMM) for Apple devices (Mac, iPhone, Apple TV, iPad). Can be used to control various configurations via different policies, install and uninstall applications, lock devices, smart groups searches, and more. This integration was integrated and tested with version 10.28.0 of jamf v2 JAMF classic API:  JAMF Pro API:  Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `jamf-get-computers`: Returns a list of all computers with their associated IDs. By default, returns the first 50 computers to the context (ID + name). This command is a replacement 
- `jamf-get-computers-basic-subset`: Returns the “basic” subset for all of the computers. The “basic” subset includes: MAC address, model, UDID, name, department, building, serial number, username,
- `jamf-get-computer-by-id`: Returns the "general" subset of a specific computer, e.g.: name, MAC address, IP, serial number, UDID, etc.
- `jamf-get-computer-by-match`: Matches computers by specific characteristics using a filter query and returns general data on each of the computers.
- `jamf-get-computer-general-subset`: Returns the general subset for a specific computer according to the given arguments.
- `jamf-get-computer-location-subset`: Returns the location subset for a specific computer according to the given arguments.
- `jamf-get-computer-purchasing-subset`: Returns the purchasing subset for a specific computer according to the given arguments.
- `jamf-get-computer-peripherals-subset`: This command is deprecated and has no replacement.
- `jamf-get-computer-hardware-subset`: Returns the hardware subset for a specific computer according to the given arguments.
- `jamf-get-computer-certificates-subset`: Returns the certificates subset for a specific computer according to the given arguments.
- `jamf-get-computer-security-subset`: Returns the security subset for a specific computer according to the given arguments.
- `jamf-get-computer-software-subset`: Returns the software subset for a specific computer according to the given arguments.
- `jamf-get-computer-extension-attributes-subset`: Returns the extension attributes subset for a specific computer according to the given arguments.
- `jamf-get-computer-groups-accounts-subset`: Returns the groups accounts subset for a specific computer according to the given arguments.
- `jamf-get-computer-iphones-subset`: This command is deprecated and has no replacement.


## JARM

**Type:** integration  
**Product:** JARM  

Active TLS fingerprinting using JARM

**Commands:**

- `jarm-fingerprint`: Calculate JARM fingerprint by scanning host with multiple TLS packets.


## Jira Change Management

**Type:** playbook  
**Product:** Change Management  

If you are using PAN-OS/Panorama firewall and Jira as a ticketing system, this playbook will be a perfect match for your change management for firewall process. This playbook is triggered by fetch from Jira and will help you manage and automate your change management process

**Inputs:**

- `TicketSummary`: Provide a summary for your firewall request.
- `SecurityTeamEmail`: The email of the security team that approves the firewall requests.
- `log_type`: Log type to query. Can be: traffic, threat, wildfire, url or data-filtering.
- `query`: The query string by which to match criteria for the logs. This is similar to the query provided in the web interface under the Monitor tab w
- `addr-src`: Source address.
- `addr-dst`: Destination address.
- `port-dst`: Destination port.
- `TestConfigurations`: By providing YES to this input, the requested firewall rule will be tested in your test environment.


## JiraAddComment

**Type:** script  
**Product:** Atlassian Jira  

Use this script to add a comment with a tag (the "Comment tag to Jira" defined in the instance configuration) as an entry in platform, which will then be mirrored as a comment to a Jira issue. This script should be run within an incident

**Inputs:**

- `comment`: comment to be added to the Jira issue.
- `tags`: The comment tag. Use the comment entry tag (defined in your instance configuration) to mirror the comment to Jira.


## JiraChangeStatus

**Type:** script  
**Product:** Atlassian Jira  

This script changes the status field of a Jira incident. It gets the new Jira status of the remote Jira issue and updates the the platform


## JiraCreateIssue-example

**Type:** script  
**Product:** Atlassian Jira  

This script is used to simplify the process of creating a new Issue in Jira. You can specify custom fields using the customFields argument

**Inputs:**

- `summary`: Summary of the issue, a mandatory field
- `projectKey`: Project key to associate the issue
- `issueTypeName`: Choose issue type by name - e.g. Problem
- `issueTypeId`: Choose issue type by its numeric ID
- `projectName`: Project name to associate the issue
- `description`: Issue description
- `labels`: comma separated list of labels
- `priority`: priority name, e.g. High/Medium.


## JiraListStatus

**Type:** script  
**Product:** Atlassian Jira  

This script lists all possible statuses for a given Jira issue. Works only for Jira v3


## JIRAPrintIssue

**Type:** script  
**Product:** Atlassian Jira  

Pretty prints a JIRA issue into the incident War Room

**Inputs:**

- `issueId`: The JIRA issue ID. For example, "SOC-24".


## JiraV3ConvertAttachmentsToTable

**Type:** script  
**Product:** Atlassian Jira  

This script is used to convert Jira attachments to a table


## JiraV3ConvertCommentsToTable

**Type:** script  
**Product:** Atlassian Jira  

This script is used to convert Jira comments to a table


## JiraV3ConvertSubtasksToTable

**Type:** script  
**Product:** Atlassian Jira  

This script is used to convert Jira subtasks to a table


## JizoM

**Type:** integration  
**Product:** JizoM  

This integration ensures interaction with the JizoM API. This integration was integrated and tested with version 12.3 of JizoM

**Commands:**

- `jizo-m-protocols-get`: Get the list of alerts sorted by protocols.
- `jizo-m-peers-get`: Get list of IP addresses connected to a specific one.
- `jizo-m-query-records-get`: Retrieve all information available on Jizo M, mainly alerts.


## jmespath

**Type:** script  
**Product:** Filters And Transformers  

Performs a JMESPath search on an input JSON format, when using a transformer

**Inputs:**

- `expression`: JMESPath expression
- `value`: Original input value


## JobCreator

**Type:** script  
**Product:** platform CI/CD  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## Joe Security v2

**Type:** integration  
**Product:** Joe Security  

Access the full set of possibilities the Joe Sandbox Cloud provides via RESTful Web API v2. This integration was integrated and tested with version 3.18.0 of jbxapi. Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `joe-is-online`: Check if the Joe Sandbox analysis server is online or in maintenance mode.
- `joe-analysis-info`: Get information about an analysis.
- `joe-list-analysis`: Lists all analyses.
- `joe-download-report`: Download a resource belonging to a report. This can be the full report, dropped binaries, etc. See the integration README for the full list of supported report 
- `joe-download-sample`: Download a sample.
- `file`: Retrieves files information from Joe Security.
- `url`: Retrieves URL information from Joe Security.
- `joe-list–lia-countries`: Retrieve a list of localized internet anonymization countries.
- `joe-list-lang-locales`: Retrieve a list of available language and locale combinations.
- `joe-get-account-quota`: Retrieve the account quota.
- `joe-submission-info`: Retrieve the submission info.
- `joe-submit-sample`: Notice: Submitting indicators using this command might make the indicator data publicly available. See the vendor’s documentation for more details.
- `joe-submit-url`: Notice: Submitting indicators using this command might make the indicator data publicly available. See the vendor’s documentation for more details.


## jq

**Type:** script  
**Product:** Community Common Scripts  

Run JQ Query. Check these links

**Inputs:**

- `value`: JSON String
- `query`: JQ compatible query


## JSON Sample Incident Generator

**Type:** integration  
**Product:** JSON Sample Incident Generator  

A utility for testing incident fetching with mock JSON data

**Commands:**

- `json-sample-incident-generator-command`: Read the provided JSON and return the results to the Context and Warroom. Can use key and value arg to change a JSON values if desired.


## Json2HtmlTable

**Type:** script  
**Product:** Community Common Scripts  

Converts JSON objects to HTML tables

**Inputs:**

- `value`: The JSON object that should be converted to a HTML table.


## JSONDiff

**Type:** script  
**Product:** Common Scripts  

This script compares two JSON files and returns their differences, such as added, removed, or changed fields, in a structured format

**Inputs:**

- `old_json`: The first JSON object to compare.
- `new_json`: The second JSON object to compare.


## JSONFeedApiModule

**Type:** script  

To use the common JSON feed API logic, run the following command to import the JSONFeedApiModule. The module expects the feed to be configured with the following parameters: Per sub-feed name: See the below example


## JSONFileToCSV

**Type:** script  
**Product:** Common Scripts  

Script to convert a War Room output JSON File to a CSV file

**Inputs:**

- `entryid`: Entry ID of json
- `filename`: Output CSV filename
- `delimiter`: CSV delimiter.


## JSONtoCSV

**Type:** script  
**Product:** Common Scripts  

Convert a JSON War Room output via EntryID to a CSV file

**Inputs:**

- `entryid`: Entry id of json
- `delimiter`: CSV Delimiter.
- `filename`: If provided will output CSV to file. Default output is to War Room.


## JsonToTable

**Type:** script  
**Product:** Filters And Transformers  

Accepts a json object and returns a markdown

**Inputs:**

- `value`: The json to transform to a markdown table.
- `title`: The markdown title.
- `headers`: A comma-separated list of table header values. Default will include all available table headers.
- `is_auto_json_transform`: Try to auto json transform.
- `json_transform_properties`: A json to transform the value to strings. The syntax is: `{"header_key": {"keys": [&lt;item1&gt;, ...], "is_nested": true/false}}`
- `url_keys`: Comma-separated list of keys in the given JSON table that should be turned into a clickable URL.


## JsonUnescape

**Type:** script  
**Product:** Common Scripts  

Recursively un-escapes JSON data if escaped JSON is found

**Inputs:**

- `value`: JSON object


## JsonWhoIs

**Type:** integration  
**Product:** JsonWhoIs  

Use the JsonWhoIs integration to enrich domain indicators

**Commands:**

- `whois`: Returns enriched data for Domains, URLs, and IP addresses.


## JWT

**Type:** integration  
**Product:** JWT Token Generator  

JSON Web Token (JWT) is a compact, URL-safe means of representing claims to be transferred between two parties. This Integration can be used to Generate New JWT Tokens, Encode and Decode Existing Ones. This integration was integrated and tested with generic JWT authentication service

**Commands:**

- `jwt-generate-access-token`: Generates a JWT authorization token with an optional scope and queries the API for an access token and then returns the received API access token
- `jwt-generate-authentication-payload`: Generates a JWT authorization request payload by encoding the provided claims.
- `jwt-decode-token`: A command to decode JWT tokens


## Kafka v3

**Type:** integration  
**Product:** Kafka  

Use the Kafka integration to manage messages and partitions and to fetch Kafka messages to create incidents in the platform. This integration was integrated and tested with version 2.7.1 of Kafka. This integration is fully compatible with the Kafka v2 integration

**Commands:**

- `kafka-print-topics`: Prints all topics and their partitions.
- `kafka-publish-msg`: Publishes a message to Kafka.
- `kafka-consume-msg`: Consumes a single Kafka message.
- `kafka-fetch-partitions`: Fetches partitions for a topic.


## Kaspersky Security Center (Beta)

**Type:** integration  
**Product:** Kaspersky Security Center  

The administration console for controlling all Kaspersky Lab security solutions and system administration tools. This integration was integrated and tested with version 12 of Kaspersky Security Center. Note: The integration is in beta because it only covers a subset of the endpoints and API use cases

**Commands:**

- `ksc-hosts-list`: Returns a list of hosts.
- `ksc-host-get`: Returns details of a host
- `ksc-groups-list`: Returns a list of groups.
- `ksc-group-add`: Create new administration group.
- `ksc-group-delete`: Deletes an administrative group.
- `ksc-software-applications-list`: Returns limited attributes for all software applications.
- `ksc-software-patches-list`: Returns limited attributes for all software application updates.
- `ksc-host-software-applications-list`: Retrieve software applications for a host.
- `ksc-host-software-patches-list`: Retrieves patches for a host.
- `ksc-policies-list`: Returns policies located in specified group.
- `ksc-policy-get`: Retrieves data for specified policy.


## Keeper Secrets Manager

**Type:** integration  
**Product:** Keeper Secrets Manager  

Manage Secrets and Protect Sensitive Data through Keeper Vault. This integration was integrated and tested with version 16.3.5 of Keeper Secrets Manager

**Commands:**

- `ksm-find-files`: Search for records by full or partial file name match.
- `ksm-find-records`: Search for records by full or partial title match.
- `ksm-get-field`: Use this command to get field value from Keeper record.


## Keeper Security

**Type:** integration  
**Product:** Keeper Security  

Use this integration to fetch audit logs from Keeper Security Admin Console as XSIAM events. This integration was integrated and tested with version 16.11.8 of Keeper Commander

**Commands:**

- `keeper-security-register-start`: Use this command to start the registration process.
- `keeper-security-register-complete`: Use this command to complete the registration process.
- `keeper-security-register-test`: Use this command to test the connectivity of the instance.


## Kenna - Search and Handle Asset Vulnerabilities

**Type:** playbook  
**Product:** Kenna  

This playbook accepts an asset, then searches for vulnerabilities on that asset using the Kenna integration. If a vulnerability exists, it looks for relevant patches, lets the analyst deploy them and then generates an investigation summary report

**Inputs:**

- `hostname`: Hostname to search.
- `host_id`: Kenna host ID to search.


## Kenna v2

**Type:** integration  
**Product:** Kenna  

Use the Kenna v2 integration to search and update vulnerabilities, schedule a run connector, and manage tags and attributes. This integration was integrated and tested with version 1.0 of Kenna

**Commands:**

- `kenna-search-vulnerabilities`: Searches for vulnerabilities in Kenna.
- `kenna-run-connector`: Executes a run of the specified connector. If file based, it will use the most recently uploaded data file.
- `kenna-search-fixes`: Filters fixes by a given set of vulnerability and asset parameters and returns the filtered fixes.
- `kenna-update-asset`: Updates the attributes of a single asset.
- `kenna-update-vulnerability`: Updates the attributes of a single vulnerability.
- `kenna-get-connectors`: Returns all connectors.
- `kenna-search-assets`: Searches for assets.
- `kenna-get-asset-vulnerabilities`: Gets vulnerabilities of the specified asset.
- `kenna-add-tag`: Adds a tag to the specified asset.
- `kenna-delete-tag`: Deletes tags from the specified asset.
- `kenna-get-connector-runs`: Returns JSON data on all the runs of a given connector.
- `kenna-search-assets-by-external-id`: Search assets by external ID.


## KeylightCreateIssue

**Type:** script  
**Product:** Lockpath Keylight  

Use this script to simplify the process of creating or updating a record in Keylight (v2). You specify custom arguments for which to populate the components. The arguments in this documentation are meant as examples only

**Inputs:**

- `task_id`: The task ID (task name) of the task to create. This is not a lookup field.
- `project`: The project name to create. This is a lookup field.


## Kibana

**Type:** integration  
**Product:** Kibana  

Use the Kibana integration to manage Elastic Security cases, detection alerts, rules, and value lists for security operations. This integration was tested with Elasticsearch versions 6.6.2, 7.3, 8.4.1, and 9.3.1

**Commands:**

- `kibana-cases-find`: Lists cases in Kibana.
- `kibana-case-alerts-find`: Returns information on the alerts of the input case in Kibana.
- `kibana-alert-status-update`: Updates the status of an input alert.
- `kibana-case-status-update`: Updates the status of an input case.
- `kibana-user-spaces-find`: Gets the list of user spaces in Kibana.
- `kibana-case-comments-find`: Finds comments for an input case ID.
- `kibana-case-delete`: Deletes a case in Kibana based on case ID.
- `kibana-rule-delete`: Deletes a rule in Kibana based on the input rule ID.
- `kibana-rule-details-search`: Retrieves details about a detection rule in Kibana based on the input KQL filter.
- `kibana-case-comment-add`: Adds a comment to a case in Kibana. The case ID and owner can be obtained from the "kibana-cases-find" command.
- `kibana-user-list-get`: Searches for the list of users in Kibana and returns the users' UIDs.
- `kibana-alert-assign`: Assigns an alert in Kibana to a user via user ID input.
- `kibana-detection-alerts-list`: Searches for detection alerts in Kibana.
- `kibana-alert-note-add`: Adds a note to an alert in Kibana.
- `kibana-alerting-health-get`: Retrieves the health status of the Kibana alerting framework.


## KillProcessWrapper

**Type:** script  
**Product:** Malware Investigation and Response  

A cross-vendor wrapper script that triggers a process kill command - i.e executes the proper kill process command according to the vendor: CrowdstrikeFalcon or Cortex XDR. The script will only fail when the kill process action fails for both vendors

**Inputs:**

- `endpoint_id`: The Endpoint ID in which you would like to kill the given process.
- `process_id`: The ID of the process to kill. Either the process_id or the process_name must be specified.
- `process_name`: The name of the process to kill. Either the process_id or the process_name must be specified.
- `approve_action`: Are you sure you want to kill this process?


## KnowBe4 KSAT

**Type:** integration  
**Product:** KSAT  

KnowBe4's KSAT Console is a security awareness training and simulated phishing console that you can use to improve your organization's overall security. This integration pack allows you to push and pull your external data to and from your KSAT console. For KnowBe4 subscription levels and pricing, see the KnowBe4 Security Awareness Training pricing page

**Commands:**

- `kmsat-account-info-list`: 
- `kmsat-account-risk-score-history`: 
- `kmsat-groups-list`: 
- `kmsat-account-risk-score-history`: 
- `kmsat-groups-risk-score-history`: 
- `kmsat-groups-members`: 
- `kmsat-users-risk-score-history`: 
- `kmsat-phishing-security-tests`: 
- `kmsat-phishing-security-tests-recipients`: 
- `kmsat-phishing-security-tests-failed-recipients`: 
- `kmsat-phishing-campaign-security-tests`: 
- `kmsat-training-campaigns`: 
- `kmsat-training-enrollments`: 
- `kmsat-user-event-list`: 
- `kmsat-user-events-list`: 


## KOI

**Type:** integration  
**Product:** KOI  
**Commands:**

- `koi-get-events`: Gets events from KOI. This command is used for developing/debugging. Use with caution, as it can create events, leading to event duplication and exceeding API r
- `koi-blocklist-get`: Retrieves all items in the blocklist.
- `koi-allowlist-get`: Retrieves all items in the allowlist.
- `koi-inventory-search`: Searches inventory items using advanced query builder filters. Provide a filter via the 'filter_json' argument (inline JSON string) or the 'filter_raw_json_entr
- `koi-policy-list`: Retrieves a list of all policies. Use the 'page' and 'page_size' arguments to fetch a specific page, or use the 'limit' argument to auto-paginate and collect up
- `koi-inventory-item-get`: Retrieves comprehensive details for a specific software item, extension, or package using its unique identifier, marketplace, and version.
- `koi-blocklist-items-add`: Adds one or more items to the global blocklist. Provide either the 'item_id' and 'marketplace' arguments for a single item, or the 'items_list_raw_json_entry_id
- `koi-policy-status-update`: Enables or disables a policy by ID.
- `koi-inventory-list`: Retrieves a paginated list of items installed across your organization's endpoints. Supports extensive filtering by marketplace, platform, risk level, publisher
- `koi-inventory-item-endpoints-list`: Retrieves a paginated list of endpoints that have a specific item installed.
- `koi-blocklist-items-remove`: Removes one or more items from the global blocklist. Provide either the 'item_id' and 'marketplace' arguments for a single item, or the 'items_list_raw_json_ent
- `koi-allowlist-items-remove`: Removes one or more items from the global allowlist. Provide either the 'item_id' and 'marketplace' arguments for a single item, or the 'items_list_raw_json_ent
- `koi-allowlist-items-add`: Adds one or more items to the global allowlist. Provide either the 'item_id' and 'marketplace' arguments for a single item, or the 'items_list_raw_json_entry_id


## Koodous

**Type:** integration  
**Product:** Koodous  

Check Android app samples (APK) against Koodous API

**Commands:**

- `k-check-hash`: Check APK sample.


## Lacework

**Type:** integration  
**Product:** Lacework  

Lacework provides end-to-end cloud security automation for AWS, Azure, and GCP with a comprehensive view of risks across cloud workloads and containers. This integration was integrated and tested with version 2 of the Lacework APIs

**Commands:**

- `lw-get-alert-details`: Fetch details for a specific Alert in Lacework.
- `lw-get-aws-compliance-assessment`: Fetch the latest AWS compliance data from Lacework.
- `lw-get-azure-compliance-assessment`: Fetch the latest Azure compliance data from Lacework.
- `lw-get-gcp-compliance-assessment`: Fetch the latest GCP compliance data from Lacework.
- `lw-get-gcp-projects-by-organization`: Fetch a list of GCP projects that are under an organization.
- `lw-get-compliance-report`: Fetch a specified compliance report from Lacework.
- `lw-get-container-vulnerabilities`: Fetch container vulnerability information from Lacework.
- `lw-get-host-vulnerabilities`: Fetch host vulnerability information from Lacework.


## LanguageDetect

**Type:** script  
**Product:** Common Scripts  

Detects language based on Google's language-detection

**Inputs:**

- `text`: The text to analyse for language detection.


## Lansweeper

**Type:** integration  
**Product:** Lansweeper  

The Lansweeper integration allows users to retrieve the asset details. This integration was integrated and tested with version 2.0 of Lansweeper

**Commands:**

- `ls-site-list`: Retrieve a list of all sites to which an application has access.
- `ls-ip-hunt`: Return a list of all assets associated with a given site and IP address.
- `ls-mac-hunt`: Return a list of all assets associated with a given site and MAC address.


## LastArrayElement

**Type:** script  
**Product:** Filters And Transformers  

Returns the last element of an array. If the value passed is not an array, it returns the original value that was passed

**Inputs:**

- `value`: An array for which to return the last value.


## LastInfoSec

**Type:** integration  
**Product:** LastInfoSec  

This integration allow to interact with the Gatewatcher LastInfoSec product via API. This integration was integrated and tested with version 2 of LastInfoSec

**Commands:**

- `gw-lis-get-by-minute`: Retrieve the data from Gatewatcher CTI feed by minute. Max 1440 minutes.
- `gw-lis-get-by-value`: Allows you to search for an IOC (url, hash, host) or a vulnerability in the Gatewatcher CTI database. If the data is known, only the IOC corresponding to the va
- `gw-lis-leaked-email-by-domain`: Allows you to search for leaked emails via a domain in Gatewatcher's CTI database. If the data is found, a list of emails is returned. otherwise, nothing is ret
- `gw-lis-is-email-leaked`: Allows you to search if a specific email was leaked in Gatewatcher's CTI database. If the data is found, the email is returned. otherwise, nothing is returned.
- `url`: search IOCs for URLs in Gatewatcher's CTI database.
- `file`: search IOCs for file hashes in Gatewatcher's CTI database.
- `domain`: search IOCs for domains in Gatewatcher's CTI database.


## Launch Adhoc Command Generic - Ansible Automation Platform

**Type:** playbook  
**Product:** Ansible Automation Platform  

Generic polling playbook for runing ad hoc commands. Ad-hoc commands in Ansible allows you to execute simple tasks at the command line against one or all of your hosts. This playbook first launchrd an ad hoc command, then reportd the status of the task when it finishes running, and at the end returns the output of the task

**Inputs:**

- `credentials_id`: Select credentials that allows Tower to access the nodes this job will be run against (if needed).
- `Inventory_id`: Select the inventory containing the hosts you want this job to manage (if needed).
- `module_name`: Modules are discrete units of code that can be used from the command line or in a playbook task. Ansible ships with a number of modules that
- `module_args`: Module arguments
- `show_output`: Print output from the ad hoc command that is running.
- `Interval`: Polling frequency. How often the polling command should run (in minutes).
- `Timeout`: How much time (in minutes) to wait before a timeout occurs.


## Launch Job - Ansible Automation Platform

**Type:** playbook  
**Product:** Ansible Automation Platform  

Generic polling playbook to launch a specific job template. Returns the job status when the job finishes running

**Inputs:**

- `job_template_id`: The job template id to launch.
- `credentials_id`: Select the credentials that allows Tower to access the nodes this job will be run against (if needed).
- `Inventory_id`: Select the inventory containing the hosts you want this job to manage (if needed).
- `extra_variables`: Pass extra command line variables to the playbook (if needed).
- `show_output`: Print output from the job that is running.
- `Interval`: Polling frequency - how often the polling command should run (in minutes)
- `Timeout`: How much time (in minutes) to wait before a timeout occurs.
- `return_job_events`: Choose if you want to return the job's raw events


## LDAP Authentication

**Type:** integration  
**Product:** LDAP Authentication  
**Commands:**

- `ad-authenticate`: Performs a simple bind operation on the LDAP server.
- `ad-groups`: Fetches LDAP groups under a given base DN.
- `ad-authenticate-and-roles`: Performs a simple bind operation on the LDAP server and returns the authenticated user's groups.
- `ad-entries-search`: A generic LDAP search command.


## LessThanPercentage

**Type:** script  
**Product:** Common Scripts  

Checks if one percentage is less than another. Returns less: if firstPercentage < secondPercentage. Returns more: if firstPercentage >= secondPercentage. Returns an exception if one of the inputs is not a float

**Inputs:**

- `firstPercentage`: The first percentage.
- `secondPercentage`: The second percentage.


## LGTM

**Type:** integration  
**Product:** DevSecOps  

An Integration with LGTM API This integration was integrated and tested with version 1.0 of LGTM

**Commands:**

- `lgtm-add-project`: Add a project to LGTM


## LinkIncidentsButton

**Type:** script  
**Product:** Common Scripts  

Incident action button script to link or unlink Incidents from an Incident

**Inputs:**

- `linkedIncidentIDs`: Incident ID to link to, or a comma separated list of related Incident IDs.
- `action`: Action to perform - Link or Unlink Incidents


## LinkIncidentsWithRetry

**Type:** script  
**Product:** Common Scripts  

Avoids DB version errors when simultaneously running multiple linked incidents

**Inputs:**

- `linkedIncidentIDs`: The CSV list of related incident IDs.
- `retryLimit`: The number of retries to perform after a failure.


## Linkshadow

**Type:** integration  
**Product:** Linkshadow  
**Commands:**

- `Linkshadow-fetch-entity-anomalies`: Linkshadow returns the full incident details referenced by timeframe (default = 60min) in an API response. Use of this command will return the JSON structure of


## Linux

**Type:** integration  
**Product:** Ansible Linux  

This integration enables the management of Linux hosts directly from platform using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the hosts by utilising SSH combined with Python. To use this integration, configure an instance of this integration. This will associate a credential to be used to access hosts when commands are run. The commands from this integration will take the Linux host address(es) as an input, and use the saved credential associated to the instance to execute. Create separate instances if multiple credentials are required

**Commands:**

- `linux-alternatives`: Manages alternative programs for common commands Further documentation available at https://docs.ansible.com/ansible/2.9/modules/alternatives_module.html
- `linux-at`: Schedule the execution of a command or script file via the at command Further documentation available at https://docs.ansible.com/ansible/2.9/modules/at_module.
- `linux-authorized-key`: Adds or removes an SSH authorized key Further documentation available at https://docs.ansible.com/ansible/2.9/modules/authorized_key_module.html
- `linux-capabilities`: Manage Linux capabilities Further documentation available at https://docs.ansible.com/ansible/2.9/modules/capabilities_module.html
- `linux-cron`: Manage cron.d and crontab entries Further documentation available at https://docs.ansible.com/ansible/2.9/modules/cron_module.html


## List Device Events - Chronicle

**Type:** playbook  
**Product:** Google SecOps  

This playbook receives ChronicleAsset identifier information and provides a list of events related to each one of them. Supported integration: Chronicle, Google SecOps

**Inputs:**

- `chronicleasset_hostname`: The hostname associated with the ChronicleAsset.
- `chronicleasset_ip`: The IP address associated with the ChronicleAsset.
- `chronicleasset_mac`: The MAC address associated with the ChronicleAsset.
- `chronicleasset_product_id`: The product ID associated with the ChronicleAsset.


## LoadJSON

**Type:** script  
**Product:** Common Scripts  

Loads a JSON from a string input, and returns a JSON object result

**Inputs:**

- `input`: The input string to transform to a JSON object.


## LoadJSONFileToContext

**Type:** script  
**Product:** Common Scripts  

Loads a JSON file from the war room to context

**Inputs:**

- `entryID`: The Entry ID of the JSON file to load into context.
- `contextKey`: The context key to put the loaded JSON under, default is JSON.


## Lockpath KeyLight v2

**Type:** integration  
**Product:** Lockpath Keylight  

Use the LockPath KeyLight integration to manage GRC tickets in the Keylight platform. This integration was integrated and tested with version 5.5.018.10 of Lockpath KeyLight

**Commands:**

- `kl-get-component`: Retrieves a component specified by ID or alias. If no parameters are specified, all components will be retrieved.
- `kl-get-field-list`: Retrieves a detail field listing for a component specified by ID.
- `kl-get-field`: Retrieves details for a field specified by ID.
- `kl-get-record`: Returns the complete set of fields for a given record within a component.
- `kl-get-records`: Retrieves the title/default field for a set of records within a chosen component. Filters may be applied to retrieve only the records meeting the selected crite
- `kl-get-record-count`: Get the number of records for a specific component and filter.


## Logrhythm - Search query

**Type:** playbook  
**Product:** LogRhythm  

This playbook used generic polling to gets query result using the command: lr-execute-search-query

**Inputs:**

- `number_of_days`: Number of days to search.
- `source_type`: Log source type.
- `host_name`: Impacted host name.
- `username`: Username.
- `subject`: Email subject.
- `sender`: Email sender.
- `recipient`: Email recipient.
- `hash`: Hash.


## LogRhythmRest

**Type:** integration  
**Product:** LogRhythm  

LogRhythm security intelligence. This integration was integrated and tested with version 7.4.6 of LogRhythmRest

**Commands:**

- `lr-execute-query`: Executes a query for logs that match the query parameters.
- `lr-get-hosts-by-entity`: Retrieves a list of hosts for a given entity, or an empty list if none is found.
- `lr-add-host`: Add a new host to an entity.
- `lr-update-host-status`: Updates an host status.
- `lr-get-persons`: Retrieves a list of LogRhythm persons.
- `lr-get-networks`: Retrieves a list of networks.
- `lr-get-hosts`: Returns a list of hosts.
- `lr-get-alarm-data`: Returns data for an alarm.
- `lr-get-alarm-events`: Returns a list of events, by alarm ID.
- `lr-get-case-evidence`: Execute evidence query for a specific case ID.
- `lr-execute-search-query`: Execute search query to LogRhythm log database.
- `lr-get-query-result`: Get search query result with task ID output from lr-execute-search-query command
- `lr-get-users`: Returns a list of users
- `lr-get-logins`: Returns a list of logins
- `lr-get-privileges`: Returns the privileges of a given user.


## LogRhythmRest v2

**Type:** integration  
**Product:** LogRhythm  

LogRhythm security intelligence. This integration was integrated and tested with version 7.7 of LogRhythm Rest API. Previous versions that have been declared EOL by the vendor, are not supported. Some changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

**Commands:**

- `lr-alarms-list`: Gets the details of the alarms using the filter criteria.
- `lr-alarm-update`: Updates the alarm status and RBP based on the alarm ID supplied. alarm_status or rbp are required.
- `lr-alarm-add-comment`: Updates the Alarm History table with comments in the Comments column based on the alarm ID supplied.
- `lr-alarm-history-list`: Gets the alarm history details by ID and filter criteria.
- `lr-alarm-events-list`: Gets a list of events for the specified alarm ID. Note: Currently, this command does not work as expected on LogRhythm's side. It always returns a list of one i
- `lr-alarm-summary`: Get the alarm summary by the specified alarm ID.
- `lr-alarm-drilldown`: Gets the drill-down logs per rule block for a specific alarm Id that fired associated with an AIE alarm.
- `lr-get-alarm-details`: Get the details of an alarm by the specified alarm ID.
- `lr-cases-list`: Get cases details using filter criteria.
- `lr-case-create`: Create a new case.
- `lr-case-update`: Update case information. For example, the case name, priority, and due date.
- `lr-case-status-change`: Update the status of a case.
- `lr-case-evidence-list`: Return a list of evidence summaries for a case.
- `lr-case-alarm-evidence-add`: Add multiple alarms as evidence on a case.
- `lr-case-note-evidence-add`: Add a note as evidence on a case.


## LogRhythmRestV2 - Search query

**Type:** playbook  
**Product:** LogRhythm  

This playbook used generic polling to get query results using the command: lr-execute-search-query

**Inputs:**

- `number_of_days`: Number of days to search.
- `search_name`: Name of the search.
- `source_type`: Log source type.
- `host_name`: Impacted host name.
- `username`: Username.
- `subject`: Email subject.
- `sender`: Email sender.
- `recipient`: Email recipient.


## Logz.io

**Type:** integration  
**Product:** Logz.io  
**Commands:**

- `logzio-search-logs`: Returns logs from your Logz.io Operations account by Lucene query
- `logzio-get-logs-by-event-id`: Fetches the logs that triggered a security event in Logz.io Cloud SIEM


## Lost / Stolen Device Playbook

**Type:** playbook  
**Product:** Lost / Stolen Device  

Initial incident details should be the name of the reporting person, or ID of the SIEM alert/incident, and description of the lost device. Labels


## LowerCidrNumAddresses

**Type:** script  
**Product:** Filters And Transformers  

Check if number of availble addresses in IPv4 CIDR is lower than given number

**Inputs:**

- `left`: IPv4/CIDR, e.g. 192.168.0.0/24
- `right`: The number of addresses to lower from.


## LSASS Credential Dumpin

**Type:** playbook  
**Product:** LSASS Credential Dumping  

This playbook is focused on detecting Credential Dumping attack as researched by Accenture Security analysts and engineers


## Luminar IOCs & leaked credentials

**Type:** integration  
**Product:** Luminar IOCs & leaked credentials  

Cognyte is a global leader in security analytics software that empowers governments and enterprises with Actionable Intelligence for a safer world. Our open software fuses, analyzes and visualizes disparate data sets at scale to help security organizations find the needles in the haystacks. Over 1,000 government and enterprise customers in more than 100 countries rely on Cognyte’s solutions to accelerate security investigations and connect the dots to successfully identify, neutralize, and prevent threats to national security, business continuity and cyber security. Luminar is an asset-based cybersecurity intelligence platform that empowers enterprise organizations to build and maintain a proactive threat intelligence operation that enables to anticipate and mitigate cyber threats, reduce risk and enhance security resilience. Luminar enables security teams to define a customized, dynamic monitoring plan to uncover malicious activity in its earliest stages on all layers of the Web. This connector allows integration of intelligence-based IOC data and customer-related leaked records identified by Luminar

**Commands:**

- `luminar-get-indicators`: Gets Luminar Indicators
- `luminar-get-leaked-records`: Gets Luminar Leaked Records
- `luminar-reset-fetch-indicators`: WARNING: This command will reset your fetch history.


## Lumu

**Type:** integration  
**Product:** Lumu  

SecOps operations - Reflect and manage the Lumu Incidents either from platform Cortex or viceversa using the mirroring integration flow,  This integration was integrated and tested with version 20230215 of Lumu

**Commands:**

- `lumu-retrieve-labels`: Get a paginated list of all the labels created for the company and its details such as id, name and business relevance. The items are sorted by the label id in 
- `lumu-retrieve-a-specific-label`: Get details such as id, name and business relevance from a specific label.
- `lumu-retrieve-incidents`: Get a paginated list of incidents for the company. The items are listed by the most recent.
- `lumu-retrieve-a-specific-incident-details`: Get details of a specific Incident.
- `lumu-retrieve-a-specific-incident-context`: Get details of a specific Incident.
- `lumu-comment-a-specific-incident`: Get a paginated list of open incidents for the company. The items are listed by the most recent.
- `lumu-retrieve-open-incidents`: Get a paginated list of open incidents for the company. The items are listed by the most recent.
- `lumu-retrieve-muted-incidents`: Get a paginated list of muted incidents for the company. The items are listed by the most recent.
- `lumu-retrieve-closed-incidents`: Get a paginated list of closed incidents for the company. The items are listed by the most recent.
- `lumu-retrieve-endpoints-by-incident`: Get a paginated summary of the endpoints affected by a specified incident.
- `lumu-mark-incident-as-read`: This transaction does not require any additional body parameters.
- `lumu-mute-incident`: To associate a specific user to this transaction, include the header Lumu-User-Id with the user id as a value. Read more.
- `lumu-unmute-incident`: To associate a specific user to this transaction, include the header Lumu-User-Id with the user id as a value. Read more.
- `lumu-consult-incidents-updates-through-rest`: Lumu provides an endpoint to consult real-time updates on incident operations through REST when Websocket is not available.
- `lumu-close-incident`: To associate a specific user to this transaction, include the header Lumu-User-Id with the user id as a value. Read more.


## Lumu Secops

**Type:** integration  
**Product:** Lumu  

SecOps operations for the new Lumu Defender API. Fetch, investigate, and manage Lumu incidents from the platform. This integration was integrated and tested with new Lumu Defender SecOps API

**Commands:**

- `lumusecops-retrieve-labels`: Gets a paginated list of all the labels created for the company and its details such as ID, name, and business relevance. The items are sorted by the label ID i
- `lumusecops-retrieve-a-specific-label`: Gets details such as id, name and business relevance from a specific label.
- `lumusecops-get-all-incidents`: Gets a paginated list of all incidents.
- `lumusecops-get-open-incidents`: Gets a paginated list of open incidents.
- `lumusecops-get-muted-incidents`: Gets a paginated list of muted incidents.
- `lumusecops-get-closed-incidents`: Gets a paginated list of closed incidents.
- `lumusecops-get-incident-events-groupings`: Retrieves event groupings for a specific incident.
- `lumusecops-get-incident-details`: Gets details for a specific incident.
- `lumusecops-mark-incident-as-read`: Marks an incident as read.
- `lumusecops-begin-incident-work`: Begins work on an incident.
- `lumusecops-comment-incident`: Adds a comment to an incident.
- `lumusecops-mute-incident`: Mutes an incident.
- `lumusecops-unmute-incident`: Unmutes an incident.
- `lumusecops-close-incident`: Closes an incident.
- `lumusecops-consult-incidents-updates`: Obtains real-time updates on incident operations.


## MAC Lease Lookup - Infoblox NIOS

**Type:** playbook  
**Product:** Infoblox NIOS  

This playbook looks up MAC Leases using Infoblox NIOS integration

**Inputs:**

- `mac_addresses`: The optional comma-separated list of MAC addresses to lookup.


## MAC Vendors

**Type:** integration  
**Product:** MAC Vendors  

Query MAC Vendors for vendor names when providing a MAC address. MAC Vendors maintains a list of vendors provided directly from the IEEE Standards Association and is updated multiple times each day. The IEEE is the registration authority and provides data on over 16,500 registered vendors. This integration was integrated and tested with the latest verison of MAC Vendors API as of 31st January 2022

**Commands:**

- `macvendors-lookup-mac`: Resolves a MAC address to a vendor name.


## Magnet Automate Beta

**Type:** integration  
**Product:** Magnet Forensics  

Magnet Automate is an orchestration and automation platform that accelerates your digital forensics investigations by automating workflows and integrating with various forensic tools. This integration was integrated and tested with version 0.2.0 of Magnet Automate API

**Commands:**

- `mf-automate-custom-fields-list`: Retrieves a list of custom fields for cases and evidence sources.
- `mf-automate-case-create`: Creates a new case in Magnet Automate. Use mf-automate-custom-fields-list to get all available custom fields.
- `mf-automate-cases-list`: Retrieves a list of all cases or information about a specific case.
- `mf-automate-case-delete`: Deletes a specific case from Magnet Automate.
- `mf-automate-case-cancel`: Cancels an ongoing case in Magnet Automate.
- `mf-automate-workflow-run-start`: Starts a new workflow run and associates it with a specific case.
- `mf-automate-workflow-run-list`: Retrieves a list of all workflow runs for a specific case or details of a specific run.
- `mf-automate-workflow-run-delete`: Deletes a specific workflow run from a case.
- `mf-automate-workflow-run-cancel`: Cancels a specific workflow run.
- `mf-automate-merge-workflow-run-start`: Starts a merge workflow run for multiple existing workflow runs.
- `mf-automate-workflow-list`: Retrieves a list of all available workflows.
- `mf-automate-workflow-delete`: Deletes a specific workflow from Magnet Automate.
- `mf-automate-workflow-get`: Retrieves detailed information and export data for a specific workflow. Use mf-automate-workflow-list to get all available workflows.
- `mf-automate-node-create`: Creates a new node (agent) in Magnet Automate.
- `mf-automate-nodes-list`: Retrieves a list of all available nodes (agents).


## Mail Listener v2

**Type:** integration  
**Product:** Mail Listener  
**Commands:**

- `mail-listener-list-emails`: Fetch mails according to the configuration
- `mail-listener-get-email`: Fetches an email by email ID
- `mail-listener-get-email-as-eml`: Fetches an email by message ID and download it's eml file


## Malcore alert related file

**Type:** playbook  
**Product:** Gatewatcher AionIQ  

This playbook fetch a malcore alert from a GCenter and retrieves the associated suspicious file


## MaliciousRatioReputation

**Type:** script  
**Product:** Common Scripts  

Sets the indicators reputation to "suspicious" when the malicious ratio is above the threshold. The malicious ratio is the ration between the number of "bad" incidents to the total number of incidents the indicator appears in

**Inputs:**

- `input`: The value of the indicator.
- `threshold`: The malicious ratio threshold to set the indicator as suspicious.


## Maltiverse

**Type:** integration  
**Product:** Maltiverse  

Analyze suspicious hashes, URLs, domains and IP addresses This integration was integrated and tested with version 1.1 of Maltiverse

**Commands:**

- `ip`: Checks the reputation of an IP address
- `domain`: Checks the reputation of a Domain
- `url`: Checks the reputation of an URL
- `file`: Check the reputation of a file


## Malware SIEM Ingestion - Get Incident Data

**Type:** playbook  
**Product:** Malware Investigation and Response  

This playbook handles incident ingestion from a SIEM. The user provides which EDR system to use, the field containing the incident ID or detection ID, and the field indicating whether the ingested item is an incident or detection

**Inputs:**

- `EDRProductToUse`: The EDR to get data from when ingesting endpoint alerts using a SIEM. Values can be CrowdStrike or MDE.
- `playbookInputQuery:`: 
- `SIEMincidentFieldForType`: The name of the field specifying the alert type. For example, for CrowdStrike this field specifies a detection or an incident.
- `SIEMincidentFieldForID`: The name of the field that provides the external ID of the alert or incident in the EDR.
- `OverrideSIEMSeverity`: Whether to set the severity according to the EDR severity scale and its mapping to the platform.


## MalwareBazaar

**Type:** integration  
**Product:** MalwareBazaar  

MalwareBazaar is a project from abuse.ch with the goal of sharing malware samples with the Infosec community, AV vendors, and threat intelligence providers. This integration was integrated and tested with version 1 of MalwareBazaar

**Commands:**

- `file`: Check if a particular malware sample is known to MalwareBazaar.
- `malwarebazaar-download-sample`: Download a malware sample from MalwareBazaar. Any malware sample downloaded from MalwareBazaar is zipped and password protected using the password "infected" (w
- `malwarebazaar-comment-add`: Add a comment for a malware sample.
- `malwarebazaar-samples-list`: Retrieves a list of recent malware samples (maximum 1000) associated with a specific sample type. Note that you can either use the limit argument or the page an


## ManageEngine

**Type:** integration  
**Product:** ManageEngine  

ManageEngine Endpoint Central is a Unified Endpoint Management solution that helps in managing thousands of servers, desktops, laptops and mobile devices from a single console. This integration serves as an Event Collector for Cortex XSIAM, enabling fetching AuditLogs from Endpoint Central. Endpoint Central cloud is hosted at multiple data centers, and therefore available on different domains. There are several domains for Endpoint Central Cloud APIs, so you can use the one that is applicable to you. The APIs on this page are intended for organizations hosted on the .com domain. If your organization is on a different domain, replace “.com” with the appropriate domain for the API endpoints before using them. Note: You can also find out which domain you’re accessing by checking the URL while logged in to Endpoint Central

**Commands:**

- `manage-engine-test`: Tests connectivity of the server.
- `manage-engine-get-events`: Manual command to fetch events and display them.


## ManageEngine PAM360

**Type:** integration  
**Product:** ManageEngine_PAM360  

Use ManageEngine PAM360, a privileged access management solution to manage critical enterprise data such as privileged resources and accounts and secure credentials from the platform

**Commands:**

- `pam360-create-resource`: Creates a new resource.
- `pam360-create-account`: Creates a new account under a specified resource.
- `pam360-update-resource`: Updates the attributes of a resource such as name, type, URL, and description.
- `pam360-update-account`: Updates the attributes an account such as name, password policy, and notes if applicable.
- `pam360-list-all-resources`: Lists all resources owned by you and shared to you by other users.
- `pam360-list-all-accounts`: Lists all accounts belonging to the resource.
- `pam360-fetch-account-details`: Fetches the details of an account using the corresponding account ID.
- `pam360-fetch-resource-account-id`: Fetches the IDs of the resources and accounts.
- `pam360-fetch-password`: Fetches the account password using the Resource and Account IDs.
- `pam360-update-account-password`: Updates the account password.


## ManageOOOusers

**Type:** script  
**Product:** Shift Management  

Adds or removes an analyst from the out-of-office list in platform. When used with the AssignAnalystToIncidentOOO automation, prevents incidents from being assigned to an analyst who is out of office

**Inputs:**

- `option`: Add or remove an analyst from the out-of-office list. Possible values are "Add" and "Remove".
- `daysoff`: Number of days the analyst will be off. Default is 7.
- `listname`: A list to use in place of the out-of-office list. If the name of the list that you pass does not begin with OOO, the script automatically pr
- `username`: The name of the analyst to add to the list. The default is the current analyst. Must be provided when running as part of a playbook.


## Mandiant Attack Surface Management

**Type:** integration  
**Product:** Mandiant Advantage Attack Surface Management  

Integrate with Mandiant Advantage Attack Surface Management to import "issues" as Incidents. This integration was integrated and tested with version 1 of AttackSurfaceManagement

**Commands:**

- `attacksurfacemanagement-get-projects`: Retrieve a list of all accessible ASM projects.
- `attacksurfacemanagement-get-collections`: Retrieve a list of collections for a specified project
- `fetch-incidents`: Fetch Incidents
- `get-remote-data`: Update a specific incident
- `update-remote-system`: Update issue in Mandiant Advantage ASM


## Mandiant Automated Defense (Formerly Respond Software)

**Type:** integration  
**Product:** Mandiant Automated Defense  

Disclaimer: Respond Software was recently acquired by FireEye and has rebranded from the Respond Analyst to the Mandiant Defense Engine. These terms refer to the same product. Most of this integration was written prior to rebranding, and primarily includes references to Respond. This will be updated in the future, at which point this disclaimer will be removed. Mandiant Defense is the cybersecurity investigation automation solution that connects the dots across disparate cybersecurity data to find real incidents fast. The Mandiant Defense engine is built to accelerate investigations for security operations teams in defense agencies, government bodies, universities, large enterprises, and leading managed service providers to get investigation power at machine speed. Mandiant Defense works with the broadest range of vendors, sensors, threat intelligence and data repositories in the industry to improve detection and response while raising security analyst productivity. This pack provides a set of commands which can be executed against an instance of the Respond Analyst. The commands allow users to retrieve information from Respond and modify incidents from within platform. Additionally, this integration supports bi-directional mirroring (for platform v6 and above) of When fetch incidents is enabled, the pack will pull all open incidents from Respond into platform. Each incident in platform will follow the naming convention <Respond Tenant Id>:<Respond Incident Id> It is worth noting that th

**Commands:**

- `mad-get-incident`: pull data for a specific incident from MAD. This command will only return an output of the incident data. it does not create a new incident
- `mad-close-incident`: close an incident in Respond and provide feedback on that incident. If the incident is already closed, feedback can still be updated. Additional comments and an
- `mad-assign-user`: assign a user to a Respond incident
- `mad-remove-user`: unassign a user from a Respond incident
- `mad-get-escalations`: Get escalation data associated with incident. In Respond, an 'escalation' is a specific event derived from a cybersecurity telemetry. Escalations are compiled t


## MapPattern

**Type:** script  
**Product:** Filters And Transformers  

This transformer will take in a value and transform it based on multiple condition expressions (wildcard, regex, etc) defined in a JSON dictionary structure. The key:value pair of the JSON dictionary should be: "condition expression": "desired outcome" For example: The transformer will return the value matched to a pattern following to the priority. When unmatched or the input value is structured (dict or list), it will simply return the input value

**Inputs:**

- `value`: The value to modify.
- `mappings`: A JSON dictionary or list of it that contains key:value pairs that represent the "Condition":"Outcome".
- `algorithm`: The default algorithm for pattern match. Available algorithm: literal, wildcard, regex, regmatch and dt.
- `caseless`: Set to true for caseless comparison, false otherwise.
- `priority`: The option to choose which value matched to return. Available options: first_match (default) and last_match.
- `context`: The context: Input . (single dot) on `From previous tasks` to enable to extract the context data.
- `flags`: The comma separated flags for pattern matching in regex. dotall (s), multiline (m), ignorecase (i) and unicode (u) are supported. This will 
- `compare_fields`: Set to true if you want pattern matching for each field, otherwise false.


## MapRaDarkIncidentDetails

**Type:** script  
**Product:** KELA RaDark  

Map details to an RaDark incident

**Inputs:**

- `itemDetails`: Detailed items as a dictionary.


## MapRangeValues

**Type:** script  
**Product:** Filters And Transformers  

This script converts an input value into another value using two lists. The input value or range is searched in the first list (map_from). If it exists, the value at the same index from the second list (map_to) is returned. If there is no match, the original value is returned. This script supports mapping from either ranges of float numbers or text strings. Example 1: map_from = "1,2,3,4" map_to = "4,3,2,1" value = 3 Output is "2" Example 2: map_from = "1-3,4" map_to = "5,1" value = 3 Output is "5" map_from = "0,0.5,1,2,3,4" map_to = "Unknown,Informational,Low,Medium,High,Critical" value = 3 Output is "High" map_from = "Unknown,Informational,Low,Medium,High,Critical" map_to = "0,0.5,1,2,3,4" value = Informational Output is "0.5"

**Inputs:**

- `map_from`: A comma-separated list of values to map from.
- `map_to`: A comma-separated list of values to map to.
- `sep`: The separator between the start and end of range values.
- `value`: the input value to map.


## MapValues

**Type:** script  
**Product:** Common Scripts  

Maps the given values to the translated values. If given values: "a,b,c" and translated: 1,2,3 then input "a" will return a 1

**Inputs:**

- `values`: The values that should be translated.
- `translated`: The translated values to be used to replace the values.
- `input`: The value to compare and replace.


## MapValuesTransformer

**Type:** script  
**Product:** Filters And Transformers  

This transformer script takes the input value and translates it based on two list arguments. The script that takes two arguments: input_values and mapped_values Both arguments are comma-separated values. The total number of values for each input must be the same. For example: input_values = "1,2,3,4" mapped_values = "4,3,2,1" If the length of each list is not the same, the script will error. value = "3" (not specified by the user) input_values = "1,2,3,4" mapped_values = "4,3,2,1" The resulting output would be "2". The mapping looks up the value in the input_values and returns the value in mapped_values at the same index. value = {"testkey1": "testvalue1", "testkey2": "testvalue2"} (not specified by the user) input_values = "key1: value1, testkey2: testvalue2" mapped_values = "value1changed,testvalue2changed" The resulting output would be {"key1": "value1", "key2": "testvalue2changed"}. Because the input_values can be parsed as a JSON dictionary, it will match the key: value pair, but only alter the value in the pair


## MarkAsEvidenceBySearch

**Type:** script  
**Product:** UpdateEntriesBySearch  

Search entries in the war room for the pattern text, and mark them as evidence

**Inputs:**

- `incident_id`: The incident ID to search entries from. If not given, the current incident is used.
- `tags`: The list of tags to set
- `description`: Evidence description
- `filter_categories`: The list of categories of source entries
- `filter_options`: The options to filter entries
- `filter_tags`: The tags to filter entries
- `filter_entry_types`: The list of entry type of source entries
- `filter_entry_formats`: The list of entry format of source entries


## MarkAsEvidenceByTag

**Type:** script  
**Product:** Common Scripts  

Mark entries as evidence if they are tagged with given tag

**Inputs:**

- `tag`: Entries with the given tag will be marked as evidence
- `description`: Description for the Evidence item


## MarkAsNoteBySearch

**Type:** script  
**Product:** UpdateEntriesBySearch  

Search entries in the war room for the pattern text, and mark as note to the entries found

**Inputs:**

- `incident_id`: The incident ID to search entries from. If not given, the current incident is used.
- `mark`: false if you un-mark entries as note, otherwise mark entries
- `filter_categories`: The list of categories of source entries
- `filter_options`: The options to filter entries
- `filter_tags`: The tags to filter entries
- `filter_entry_types`: The list of entry type of source entries
- `filter_entry_formats`: The list of entry format of source entries
- `algorithm`: The pattern matching algorithm


## MarkAsNoteByTag

**Type:** script  
**Product:** Common Scripts  

Marks entries as notes if they are tagged with a given tag

**Inputs:**

- `tag`: The entries with the given tag will be marked as notes.


## MarkdownToHTML

**Type:** script  
**Product:** Community Common Scripts  

Converts Markdown to HTML

**Inputs:**

- `text`: Markdown Text to transform.
- `convertOnlyMarkdown`: If True - The markdown text will be converted to HTML without a Full HTML structure.
- `prettifyHTML`: If True - The resulted HTML will be nicely formatted as a Unicode string, with a separate line for each tag and each string.


## MarkRelatedIncidents

**Type:** script  
**Product:** Common Scripts  

Marks given incidents as related, to the current incident

**Inputs:**

- `related`: The list of related incident IDs to be marked.


## MatchRegexV2

**Type:** script  
**Product:** Common Scripts  

Extracts regex data from a given text. This supports groups and looping as well

**Inputs:**

- `data`: The text date to extract the regex from.
- `regex`: The regex to match and extract. Take into account that data taken from context data contains special characters which are not visible, such 
- `group`: The matching group to return. If nothing is provided the full match will be returned. The group value should start at 1.
- `contextKey`: The context key to populate with the result.
- `flags`: The regex flags to match. The default is "-gim".


## MathUtil

**Type:** script  
**Product:** Common Scripts  

Runs the provided mathematical action on 2 provided values and produce a result. The result can be stored on the context using the contextKey argument

**Inputs:**

- `lh`: The left hand parameter.
- `rh`: The right hand parameter.
- `action`: The math expression (+, -, >, <, ==, *, /, %).
- `rhRegex`: The regex used to filter only a specific part of the right hand argument.
- `lhRegex`: The regex used to filter only a specific part of the left hand argument.
- `lhRadix`: The radix for the left hand value. The default is 10.
- `rhRadix`: Radix for right hand value, defaults to 10
- `contextKey`: The path to store the result.


## Mattermost v2

**Type:** integration  
**Product:** Mattermost  

Mattermost is an open-source, self-hostable online chat service with file sharing, search, and integrations. It is designed as an internal chat for organizations and companies. This integration was integrated and tested with version 4.0.0 of Mattermost API. Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `mattermost-get-team`: Gets a team's details.
- `mattermost-list-channels`: Lists channels.
- `mattermost-list-private-channels-for-user`: Get all the private channels on a team for a user.
- `mattermost-create-channel`: Creates a channel.
- `mattermost-add-channel-member`: Adds a channel member.
- `mattermost-remove-channel-member`: Removes a channel member.
- `mattermost-list-users`: Lists users.
- `mattermost-send-file`: Sends a file.
- `send-notification`: Send a message using a chatbot app.
- `mattermost-close-channel`: Closes a channel.
- `close-channel`: Closes a mirrored MatterMost channel. If not provided, the mirrored investigation channel is archived (if the channel exists).
- `mirror-investigation`: Mirrors the investigation between Mattermost and the the platform.
- `close-channel`: Closes a mirrored Mattermost channel. If not provided, the mirrored investigation channel is archived (if the channel exists).
- `mattermost-mirror-investigation`: Mirrors the investigation between Mattermost and the the platform.
- `mattermost-list-groups`: Lists groups. Groups are available on Enterprise and Professional plans. Minimum server version: 5.11


## MattermostAskUser

**Type:** script  
**Product:** Mattermost  

Ask a user a question on Mattermost and expect a response. The response can also close a task (might be conditional) in a playbook

**Inputs:**

- `user`: The Mattermost user to ask. Can be either an email or Mattermost username.
- `message`: The message to ask the user.
- `option1`: First option for a user reply. "yes" is the default.
- `option2`: Second option for the user reply. "no" is the default.
- `task`: Which task should we close with the reply. If none, then no playbook tasks will be closed.
- `replyEntriesTag`: Tag to add on email reply entries.
- `persistent`: Indicates whether to use one-time entitlement or a persistent one.
- `reply`: The reply to send to the user. Use the templates {user} and {response} to incorporate these in the reply. (i.e., "Thank you **{user}**. You 


## MaxList

**Type:** script  
**Product:** Community Common Scripts  

Gets the maximum value from list e.g. ["25", "10", "25"] => "25"

**Inputs:**

- `value`: A list for which to sum the list values.


## McAfee DAM

**Type:** integration  
**Product:** McAfee DAM  

Use McAfee Database Activity Monitoring (DAM) Integration to fetch Alerts (incidents) and query Alerts. This integration was integrated and developed with version 4.6.x of McAfee DAM

**Commands:**

- `dam-get-alert-by-id`: Gets a DAM alert from McAfee Database Activity Monitoring by alert ID.
- `dam-get-latest-by-rule`: Gets the latest DAM alerts by rule name.


## McAfee DXL

**Type:** integration  
**Product:** McAfee DXL  

Use the McAfee DXL integration to connect and optimize security actions across multiple vendor products

**Commands:**

- `dxl-send-event`: Sends the specified event to the DXL fabric.
- `dxl-push-ip`: Pushes an IP address to the DXL fabric.
- `dxl-push-url`: Pushes the URL to the DXL fabric.
- `dxl-push-domain`: Pushes a domain to the DXL fabric
- `dxl-push-hash`: Pushes a file hash to the DXL fabric.


## McAfee ePO Endpoint Connectivity Diagnostics Playbook v2

**Type:** playbook  
**Product:** McAfee ePO  

Perform a check on ePO endpoints to see if any endpoints are unmanaged or lost connectivity with ePO and take steps to return to a valid state


## McAfee ePO v2

**Type:** integration  
**Product:** McAfee ePO  

McAfee ePolicy Orchestrator This integration was integrated and tested with version 5.3.2 and 5.10 of McAfee ePO

**Commands:**

- `epo-help`: Displays help (information) for ePO commands. If no command argument is specified, returns all ePO commands.
- `epo-get-latest-dat`: Checks the latest available DAT file version in the public McAfee repository.
- `epo-get-current-dat`: Checks the existing DAT file version in the ePO repository.
- `epo-command`: Executes the ePO command. Receives the mandatory 'command' argument, and other optional arguments. Run the 'epo-help' command to get a list of available command
- `epo-update-client-dat`: Runs a client task to update the DAT file on the given endpoints.
- `epo-update-repository`: Triggers a server task in specific ePO servers to retrieve the latest signatures from the updated server.
- `epo-get-system-tree-group`: Returns a system tree group.
- `epo-find-systems`: Finds computers within a specified group in the McAfee ePO system tree.
- `epo-find-system`: Finds systems in the McAfee ePO system tree.
- `epo-wakeup-agent`: Wakes up an agent.
- `epo-apply-tag`: Applies a tag to the specified host names.
- `epo-clear-tag`: Clears a tag from the specified host names.
- `epo-list-tag`: List tags that contain the searchText. If no searchText is specified, list all tags available in the ePO system.
- `epo-get-tables`: Returns the ePO table of the table argument that is specified. If no table argument is specified, returns all ePO tables.
- `epo-query-table`: Queries an ePO table.


## McAfee ESM v2

**Type:** integration  
**Product:** McAfee ESM  

Run queries and receive alarms from Trellix (McAfee) ESM. This integration was tested with version 11.6 of McAfee ESM v2. Versions earlier than 11.6 are not supported, as they reached Trellix end-of-life. Starting with ESM 11.6.11, the login API requires the username and password to be AES-encrypted. Enter the version number of your ESM instance in the Version parameter — the integration applies AES encryption automatically for versions 11.6.11 and later; no manual encryption is required

**Commands:**

- `esm-fetch-fields`: Gets all fields that can be used in query filters, including type information for each field
- `esm-search`: Perform a query against Mcafee ESM SIEM
- `esm-fetch-alarms`: Retrieves a list of triggered alarms.
- `esm-get-case-list`: Gets a list of cases from McAfee ESM.
- `esm-add-case`: Adds a case to the system.
- `esm-edit-case`: Edit the details of an existing case.
- `esm-get-case-statuses`: Gets a list of valid case statuses from the system.
- `esm-edit-case-status`: Edits the status of a case.
- `esm-get-case-detail`: Gets the details of an existing case.
- `esm-get-case-event-list`: Gets case event details.
- `esm-add-case-status`: Adds a status to the specified case.
- `esm-delete-case-status`: Deletes the status of a case.
- `esm-get-organization-list`: Gets a case organization.
- `esm-get-user-list`: Gets a list of all users.
- `esm-acknowledge-alarms`: Marks triggered alarms as acknowledged.


## McAfee NSM v2

**Type:** integration  
**Product:** McAfee NSM  

McAfee Network Security Manager gives you real-time visibility and control over all McAfee intrusion prevention systems deployed across your network. This integration was integrated and tested with version 9.1 of McAfeeNSMv2 Some changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

**Commands:**

- `nsm-list-domain-firewall-policy`: Gets the list of firewall policies defined in a particular domain.
- `nsm-get-firewall-policy`: Gets the firewall policy details.
- `nsm-create-firewall-policy`: Adds a new firewall policy and access rules. You have to provide at lease one of the source/destination rule objects. If you provide the id or type of the sourc
- `nsm-update-firewall-policy`: Updates the firewall policy details. If the argument is_overwrite=true, the new values of the provided addresses will replace the existing values, otherwise the
- `nsm-delete-firewall-policy`: Deletes the specified firewall policy.
- `nsm-list-domain-rule-object`: Gets the list of rule objects defined in a particular domain.
- `nsm-get-rule-object`: Gets the details of a rule object.
- `nsm-create-rule-object`: Adds a new rule object.
- `nsm-update-rule-object`: Updates a Rule object. In case of address rule update:
- `nsm-delete-rule-object`: Deletes a rule object.
- `nsm-get-alerts`: Retrieves the alerts.
- `nsm-get-alert-details`: Retrieves the relevant alert details.
- `nsm-get-attacks`: If an attack is given, the command returns the details for the specific attack. Otherwise, gets all available attack definitions in the Manager UI. This command
- `nsm-get-domains`: If a domain ID is given, the command returns the details of the specific domain. Otherwise, gets all available domains.
- `nsm-get-sensors`: Gets the list of sensors available in the specified domain. If the domain is not specified, details of all the sensors in all ADs will be provided.


## MCPApiModule

**Type:** script  

Common Model Context Protocol (MCP) code that will be appended into each MCP integration when it's deployed


## MDR Escalation Process - Vectra XDR

**Type:** playbook  
**Product:** Vectra XDR  

This playbook retrieves the MDR ticket number associated with the given entity by parsing its notes. It then collects the entity's active detections, performs a detection assessment, and sends the results to the designated recipient via email

**Inputs:**

- `entity_id`: The ID of the entity.
- `entity_type`: The type of the entity.
- `recipient_email`: The recipient email address for MDR escalation process.
- `detection_assessment_limit`: The number of the active detection to be assessed.


## Menlo Security

**Type:** integration  
**Product:** Menlo Security  

The cloud-based Menlo Security Isolation Platform (MSIP) eliminates the possibility of malware reaching user devices via compromised or malicious Web sites, Email or documents. This integration collects logs from the MSIP Logging API and sends them to Cortex

**Commands:**

- `menlo-security-get-events`: Manually fetch events from the Menlo Security Isolation Platform.


## Micro Focus Service Manager

**Type:** integration  
**Product:** Micro Focus Service Manager  

Service Manager By Micro Focus (Formerly HPE Software)

**Commands:**

- `hpsm-update-incident`: Updates existing incident (beta).
- `hpsm-create-incident`: Creates a new incident.
- `hpsm-list-incidents`: Returns all incidents.
- `hpsm-get-incident-by-id`: Returns a single incident by ID. If no incident exists with the specified ID, an error will be returned.
- `hpsm-create-resource`: Updates the existing resource (beta).
- `hpsm-update-resource`: Creates a new resource.
- `hpsm-list-resources`: Returns all resources (beta).
- `hpsm-get-resource-by-id`: Returns a single resource by ID. If no resource exists with the specified ID, an error will be returned (beta).
- `hpsm-list-devices`: Returns a list of devices, filtered according to query.
- `hpsm-get-device`: Find and return a device by ID.
- `hpsm-create-request`: Creates a new service request


## MicroFocus SMAX

**Type:** integration  
**Product:** MicroFocus SMAX  

Fetch SMAX incidents, requests and automate different SMAX case management actions This integration was integrated and tested with version 2021.08 of MicroFocus SMAX

**Commands:**

- `microfocus-smax-get-entity`: Get any entity details
- `microfocus-smax-query-entities`: Query entities' details using a collection query filter
- `microfocus-smax-create-entities`: Create new entities
- `microfocus-smax-update-entities`: Update entities
- `microfocus-smax-create-incident`: Create a new incident
- `microfocus-smax-update-incident`: Update an incident
- `microfocus-smax-create-request`: Create a new request
- `microfocus-smax-update-request`: Update a request


## Microsoft Endpoint Configuration Manager

**Type:** integration  
**Product:** Microsoft Endpoint Configuration Manager  
**Commands:**

- `ms-ecm-user-last-log-on`: Gets the name of the last user who logged in to a given device.
- `ms-ecm-collection-list`: Gets a Configuration Manager collection.
- `ms-ecm-device-list`: Lists a Configuration Manager device.
- `ms-ecm-script-list`: Gets Configuration Manager PowerShell scripts.
- `ms-ecm-script-create`: Creates a new Powershell script.
- `ms-ecm-script-invoke`: Invokes a script in the Configuration Manager.
- `ms-ecm-script-approve`: Approves a Configuration Manager PowerShell script.
- `ms-ecm-device-collection-create`: Creates a Configuration Manager collection.
- `ms-ecm-device-collection-members-add`: Adds a direct rule membership to a device collection.
- `ms-ecm-device-collection-include`: Adds an include collections membership rule to a device collection.
- `ms-ecm-device-collection-exclude`: Adds an exclude membership rule to one or more Configuration Manager device collections.
- `ms-ecm-device-collection-members-by-query-add`: Adds a query membership rule to one or more Configuration Manager device collections.
- `ms-ecm-service-start`: Starts a service on a device or collection. (Implemented by creating and invoking the platform StartService script.)
- `ms-ecm-service-restart`: Restarts a service on a device or collection. (Implemented by creating and invoking the platform RestartService script.)
- `ms-ecm-service-stop`: Stops a service on a device or collection. (Implemented by creating and invoking the platform StopService script.)


## Microsoft Endpoint Manager (Intune)

**Type:** integration  
**Product:** Microsoft Graph Device Management  

Microsoft Intune is a Microsoft cloud-based management solution that provides for mobile device and operating system management

**Commands:**

- `msgraph-get-managed-device-by-id`: Get managed devices Note: physicalMemoryInBytes will return 0 by default since Microsoft hasn't updated the v1.0 schema with that information yet
- `msgraph-sync-device`: Check the device with Intune, immediately receive pending actions and policies
- `msgraph-device-disable-lost-mode`: Disable the lost mode of the device
- `msgraph-locate-device`: Gets the GPS location of a device (iOS only)
- `msgraph-device-reboot-now`: Immediately reboots the device
- `msgraph-device-shutdown`: Immideately shuts down the device
- `msgraph-device-bypass-activation-lock`: Removes the activation lock (iOS devices only)
- `msgraph-device-retire`: Remove the device from intune management
- `msgraph-device-reset-passcode`: Resets the passcode for the device
- `msgraph-device-remote-lock`: Lock the device, to unlock the user will have to use the passcode
- `msgraph-device-request-remote-assistance`: Request a remote access via TeamViewer
- `msgraph-device-recover-passcode`: Recovers the passcode from the device
- `msgraph-logout-shared-apple-device-active-user`: logs out the current user on a shared iPad device
- `msgraph-delete-user-from-shared-apple-device`: deletes a user that you select from the local cache on a shared iPad device
- `msgraph-windows-device-defender-update-signatures`: Forece update windows defender signatures


## Microsoft Graph Mail Single User

**Type:** integration  
**Product:** Microsoft Graph Mail  

Microsoft Graph grants the platform. This integration was integrated and tested with version 1.0 of Microsoft Graph Mail Single User Note: This integration operates against a single user mailbox — the one specified in the Email address to associate for this integration. configuration parameter. Because it uses delegated permissions, it cannot access other users' mailboxes. For multi-mailbox or cross-tenant access, use the Microsoft Graph Mail (multi-tenant) integration

**Commands:**

- `msgraph-mail-create-draft`: Creates a draft message in the specified user's mailbox.
- `reply-mail`: Replies to an email using Graph Mail Single User.
- `send-mail`: Sends an email using Microsoft Graph.
- `msgraph-mail-reply-to`: The replies to the recipients of a message.
- `msgraph-mail-send-draft`: Sends a draft email using Microsoft Graph.
- `msgraph-mail-test`: Tests connectivity of the email.
- `msgraph-mail-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `msgraph-mail-list-emails`: Gets the properties of returned emails. Typically shows partial results, use the "page_size" and "pages_to_pull" arguments to get all results. This command list
- `msgraph-mail-list-attachments`: Lists all attachments of an email.
- `msgraph-mail-get-attachment`: Gets an attachment from the email.
- `msgraph-mail-get-email-as-eml`: Retrieves an email message by message ID and uploads the content as an EML file.
- `msgraph-update-email-status`: Update the status of an email to read / unread.
- `msgraph-mail-generate-login-url`: Generate the login url used for Authorization code flow.
- `msgraph-mail-create-folder`: Creates a new folder under the specified folder (parent).
- `msgraph-mail-move-email`: Move a message to another folder. This operation creates a new copy of the message in the destination folder and deletes the original message. As a result, the 


## Microsoft Graph Search

**Type:** integration  
**Product:** Microsoft Graph Search  

Use the Microsoft Search API in Microsoft Graph to search content stored in OneDrive or SharePoint: files, folders, lists, list items, or sites

**Commands:**

- `msgraph-search-test`: Tests connectivity.
- `msgraph-search-content`: Use the Microsoft Search API in Microsoft Graph to search content stored in OneDrive or SharePoint: files, folders, lists, list items, or sites.
- `msgraph-search-generate-login-url`: Generate the login url used for Authorization code flow.


## Microsoft Graph Security

**Type:** integration  
**Product:** Microsoft Graph Security  
**Commands:**

- `msg-auth-test`: Tests connectivity to Microsoft Graph Security.
- `msg-search-alerts`: List alerts (security issues) within a customer's tenant that Microsoft or partner security solutions have identified.
- `msg-get-alert-details`: Get details for a specific alert.


## Microsoft Graph Teams (Standard Connector)

**Type:** integration  
**Product:** Microsoft Graph Teams (Standard Connector)  

This integration is configured automatically as part of the Microsoft 365 Standard Connector. Do not configure this integration directly — set it up from the connector page instead

**Commands:**

- `msgraph-teams-message-update-policy-violation`: Applies a data loss prevention (DLP) policy violation to a Microsoft Teams message. Targets a chat message, a channel message, or a channel reply.


## Microsoft Teams

**Type:** integration  
**Product:** Microsoft Teams  

Use the Microsoft Teams integration to send messages, notifications, and create meetings. This integration was tested with version 1.0 of Microsoft Teams. This document includes the following sections to help you understand, set up, and use the integration effectively: Data is exchanged between Microsoft Teams and the platform. A webhook (that you will configure) receives the data from Teams and passes it to the messaging endpoint. The web server on which the integration runs in the platform. You can use an engine for communication between Teams and the the platform. To mirror messages from Teams into the platform, the bot must be explicitly mentioned in the message using the '@' symbol. The web server for the integration runs within a long-running Docker container. the platform, to the host port (to which Teams posts messages). For more information, see long-running integrations documentation and Docker documentation. Note: The information in this video is for the platform. Refer to the Prerequisites section for the latest instructions

**Commands:**

- `send-notification`: Sends a message to the specified teams. To mention a user in the message, add a semicolon ";" at the end of the user mention. For example: @Bruce Willis;.
- `mirror-investigation`: Mirrors the the platform. Supports only standard channels.
- `close-channel`: Deletes the specified Microsoft Teams channel.
- `microsoft-teams-integration-health`: Returns real-time and historical data on the integration status.
- `microsoft-teams-ring-user`: Rings a user's Teams account. Note: This is a ring only! no media will play in case the generated call is answered.
- `microsoft-teams-add-user-to-channel`: Adds a member (user) to a private/shared channel. For a comparison of Teams features for each channel type, see the Microsoft documentation: Channel feature com
- `microsoft-teams-create-channel`: Creates a new channel in a Microsoft Teams team. For more information about the channels types, see the Microsoft documentation: standard, private, or shared ch
- `microsoft-teams-create-meeting`: Creates a new meeting in Microsoft Teams.
- `microsoft-teams-user-remove-from-channel`: Removes a member (user) from a private/shared channel.
- `microsoft-teams-channel-user-list`: Retrieves a list of members from a channel.
- `microsoft-teams-chat-create`: Creates a new chat.
- `microsoft-teams-message-send-to-chat`: Sends a new chat message in the specified chat.
- `microsoft-teams-chat-add-user`: Adds a member (user) to a group chat.
- `microsoft-teams-chat-member-list`: Retrieves a list of members from a chat.
- `microsoft-teams-chat-list`: Retrieves a list of chats that the consent user is a member of. If 'chat' is specified - retrieves this chat only.


## Microsoft Teams Management

**Type:** integration  
**Product:** Microsoft Teams  

Manage teams and members in Microsoft Teams

**Commands:**

- `microsoft-teams-auth-test`: Tests the connectivity to Microsoft.
- `microsoft-teams-auth-start`: Run this command to start the authorization process and follow the instructions in the command results.
- `microsoft-teams-auth-complete`: Run this command to complete the authorization process. Should be used after running the microsoft-teams-auth-start command.
- `microsoft-teams-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `microsoft-teams-team-create`: Creates a new team.
- `microsoft-teams-team-create-from-group`: Create a new team under a group. In order to create a team, the group must have a least one owner and the group cannot be of type Security.
- `microsoft-teams-teams-list`: Returns all the groups that have teams in an organization.
- `microsoft-teams-team-get`: Retrieve the properties and relationships of the specified team.
- `microsoft-teams-team-update`: Update the properties of the specified team.
- `microsoft-teams-team-delete`: Deletes a group. Note: it might take time for the team to disappear from the teams list.
- `microsoft-teams-members-list`: Returns the members of the specified team.
- `microsoft-teams-member-get`: Gets a member of a team.
- `microsoft-teams-member-add`: Add a user to be a team member.
- `microsoft-teams-member-remove`: Remove a member from the team.
- `microsoft-teams-member-update`: Updates a team member.


## Microsoft Teams via Webhook

**Type:** integration  
**Product:** Microsoft Teams  

Integration for sending notifications to a Microsoft Teams channel via workflow. This integration was integrated and tested with version 6.8 of Microsoft Teams via Webhook

**Commands:**

- `ms-teams-message`: Send a message to Microsoft Teams via Incoming Webhook.


## MicrosoftApiModule

**Type:** script  

To use the common Microsoft API logic (authentication and API requests), run the following command to import the MicrosoftApiModule. Then, the MicrosoftClient will be available for usage. For examples, see the Microsoft Graph Listener or Microsoft Graph Mail integrations


## MicrosoftAzureStorageApiModule

**Type:** script  

To use the common Microsoft Azure Storage API logic , run the following command to import the MicrosoftAzureStorageApiModule. Then, the MicrosoftStorageClient will be available for usage. For examples, see the Azure Storage Queue or Azure Storage Table integrations


## MicrosoftGraphFilesApiModule

**Type:** script  

To use the common Microsoft Graph Files integration logic, run the following command to import the MicrosoftGraphFilesApiModule. Then, the run_microsoft_graph_files_integration entry point and MsGraphClient class will be available for usage. For the canonical consumer, see the Microsoft Graph Files integration


## MicrosoftGraphMailApiModule

**Type:** script  

To use the common Microsoft Graph Mail API logic (authentication and API requests), run the following command to import the MicrosoftGraphMailApiModule. Then, the MsGraphMailBaseClient will be available for usage. For examples, see the Microsoft Graph Listener or Microsoft Graph Mail integrations


## MinIO

**Type:** integration  
**Product:** DevSecOps  

An Integration with MinIO Object Storage This integration was integrated and tested with RELEASE.2020-12 of MinIO

**Commands:**

- `minio-make-bucket`: Create a new bucket.
- `minio-remove-bucket`: Remove an existing bucket.
- `minio-list-buckets`: List All MinIO Buckets
- `minio-list-objects`: Lists object information of a bucket.
- `minio-get-object`: Gets data from offset to length of an object.
- `minio-stat-object`: Get object information and metadata of an object.
- `minio-remove-object`: Remove an object.
- `minio-fput-object`: Uploads data from a file to an object in a bucket.
- `minio-put-object`: Uploads data from a stream to an object in a bucket.
- `minio-get-tags`: Get tags configuration of an object.
- `minio-set-tag`: Set tags configuration to an object.
- `minio-copy-object`: Create an object by server-side copying data from another object.


## MinList

**Type:** script  
**Product:** Community Common Scripts  

Gets the minimum value from list e.g. ["25", "10", "25"] => "10"

**Inputs:**

- `value`: A list for which to sum the list values.


## MISP v3

**Type:** integration  
**Product:** MISP  

Malware information sharing platform and threat sharing. Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `misp-search-events`: Search for events in MISP. This search command will return only information about the matched events. To get information about attributes, use the misp-search-a
- `domain`: Checks the reputation of the given domain.
- `email`: Checks the reputation of the given email address.
- `file`: Checks the file reputation of the given hash.
- `url`: Checks the reputation of the given URL.
- `ip`: Checks the reputation of an IP address.
- `misp-create-event`: Creates a new MISP event.


## MissingElements

**Type:** script  
**Product:** Community Common Scripts  

Returns the list of missing elements from an input list of integers. e.g. [12,14,16] -> [13,15]

**Inputs:**

- `value`: An input list of integers.
- `start`: Start of the range.
- `end`: End of the range.


## Mitre Attack - Extract Technique Information From ID

**Type:** playbook  
**Product:** MITRE ATT&CK  

This playbook accepts as input MITRE techniques IDs. It returns the MITRE technique name and full technique data using the MITRE integration

**Inputs:**

- `TechniqueID`: Accepts a single MITRE technique ID or array of technique IDs, for example: T1210


## MitreCaldera

**Type:** integration  
**Product:** MITRE Caldera  

Mitre Caldera can be used to test endpoint security solutions and assess a network's security posture against the common post-compromise adversarial techniques contained in the ATT&CK model. CALDERA leverages the ATT&CK model to identify and replicate adversary behaviors as if a real intrusion is occurring. This integration was integrated and tested with version 4.0.0 of MitreCaldera

**Commands:**

- `caldera-create-fact`: Create a Fact
- `caldera-create-fact-source`: Create a Fact Source.
- `caldera-create-adversary`: Create a new adversary
- `caldera-create-agent`: Create a new agent
- `caldera-create-operation`: Create a new CALDERA operation record
- `caldera-create-objective`: Create a new objective
- `caldera-create-relationship`: Create a Relationship
- `caldera-create-ability`: Creates a new ability.
- `caldera-create-potential-link`: Creates a potential Link
- `caldera-create-schedule`: Create Schedule
- `caldera-delete-agent`: Delete an Agent
- `caldera-delete-fact-source`: Delete an existing Fact Source.
- `caldera-delete-operation`: Delete an operation by operation id
- `caldera-delete-facts`: Delete One or More Facts
- `caldera-delete-relationships`: Delete One or More Relationships


## MITREIndicatorsByOpenIncidentsV2

**Type:** script  
**Product:** MITRE ATT&CK  

This is a widget script returning MITRE indicators information for top indicators shown in incidents


## MITRENameByID_Formatter

**Type:** script  
**Product:** Common Scripts  

Get a MITRE ATT&CK object name by its ID. The script is using TIMs IOCs to find the correct name. (MITRE ATT&CK IOCs must exist in the Threat Intel data)

**Inputs:**

- `input`: The MITRE ATT&CK object ID.


## mnemonic MDR - Argus Managed Defence

**Type:** integration  
**Product:** mnemonic MDR  

Rapidly detect, analyse and respond to security threats with mnemonic’s leading Managed Detection and Response (MDR) service. This integration was integrated and tested with version 5.1.1 argus-toolbelt (PyPi)

**Commands:**

- `argus-add-attachment Add attachment to case (Max 50 MB, should be an archive)`: Fetch specific attachment metadata
- `argus-add-case-tag`: Adds a key, value tag to an Argus case
- `argus-list-case-tags`: List tags attached to an Argus case
- `argus-add-comment`: Add comment to an Argus case
- `argus-list-case-comments`: List the comments of an Argus case
- `argus-advanced-case-search`: Returns cases matching the defined case search criteria
- `argus-close-case`: Close an Argus case
- `argus-create-case`: Create Argus case
- `argus-delete-case`: Mark existing case as deleted
- `argus-delete-comment`: Mark existing comment as deleted
- `argus-edit-comment`: Edit existing comment
- `argus-get-case-metadata-by-id`: Returns the basic case descriptor for the case identified by ID
- `argus-list-case-attachments`: List attachments for an existing case
- `argus-remove-case-tag-by-id`: Remove existing tag by tag ID
- `argus-remove-case-tag-by-key-value`: Remove existing tag with key, value matching


## MobileIronCLOUD

**Type:** integration  
**Product:** MobileIron-UEM  
**Commands:**

- `mobileiron-cloud-get-devices-data`: Gets all the devices based on a particular filter query. The command might execute multiple API calls depending on the amount of devices that would be returned.
- `mobileiron-cloud-get-device-by-mac`: Gets a single device matching the provided mac address.
- `mobileiron-cloud-get-device-by-serial`: Gets a single device matching the provided value for the device serial number.
- `mobileiron-cloud-unlock-device`: Sends an unlock action to the device.
- `mobileiron-cloud-retire-device`: Sends a retire action to the device.
- `mobileiron-cloud-wipe-device`: Sends a wipe action to the device. This is a potentially destructive action as it will completely wipe the device.
- `mobileiron-cloud-force-check-in`: Forces a check in to the particular device based on the device ID.
- `mobileiron-cloud-send-message`: Sends a message to the device.
- `mobileiron-cloud-get-device-by-id`: Returns the data for a particular device based on the device ID.


## MobileIronCORE

**Type:** integration  
**Product:** MobileIron-UEM  

This integration was created and tested with version 11.0.0 of MobileIronCORE

**Commands:**

- `mobileiron-core-send-message`: Sends a message to the particular device based on the device ID.
- `mobileiron-core-update-os`: Updates the operating system on the particular device based on the device ID.
- `mobileiron-core-unlock-device-only`: Unlocks the particular device based on the device ID.
- `mobileiron-core-enable-voice-roaming`: Enables voice roaming on the particular device based on the device ID.
- `mobileiron-core-disable-voice-roaming`: Disables voice roaming on the particular device based on the device ID.
- `mobileiron-core-enable-data-roaming`: Enables data roaming on the particular device based on the device ID.
- `mobileiron-core-disable-data-roaming`: Disables data roaming on the particular device based on the device ID.
- `mobileiron-core-enable-personal-hotspot`: Enables a personal hotspot on the particular device based on the device ID.
- `mobileiron-core-disable-personal-hotspot`: Disables a personal hotspot on the particular device based on the device ID.
- `mobileiron-core-unlock-app-connect-container`: Unlocks an app connect container on the particular device based on the device ID.
- `mobileiron-core-retire-device`: Retires a device based on the device ID.
- `mobileiron-core-wipe-device`: Wipes a device based on the device ID.
- `mobileiron-core-force-checkin`: Forces check in to the device based on the device ID.
- `mobileiron-core-get-devices-data`: Gets a list of devices matching the provided query.
- `mobileiron-core-get-device-by-uuid`: Gets a single device based on the device UUID.


## MockPlaybook

**Type:** playbook  
**Product:** Content Testing  

## MockSubplaybook

**Type:** playbook  
**Product:** Content Testing  
**Inputs:**

- `one`: 
- `two`: 


## Modify EDL

**Type:** playbook  
**Product:** Generic Export Indicators Service  

Adds indicators to or removes indicators from an external dynamic list (EDL) by adding or removing an indicator tag. The EDL itself is generated by using the the platform. Incident fields that control the behavior of this playbook


## ModifyDateTime

**Type:** script  
**Product:** Filters And Transformers  

Takes a date or time input and adds or subtracts a determined amount of time. Returns a string in date or time in ISO Format

**Inputs:**

- `value`: Input date or time in a format that is supported by the dateparser.parse() function as outlined here- https://dateparser.readthedocs.io/en/l
- `variation`: Variation of time (for example: 'in 1 day', or '3 months ago'). Must be supported by the dateparser.parse() function here - https://datepars


## MondayEventCollector

**Type:** integration  
**Product:** Monday  

Collects Monday.com audit logs and activity events for Cortex XSIAM

**Commands:**

- `monday-generate-login-url`: Generate the login url used for Authorization code flow.
- `monday-auth-test`: Run this command to test the connectivity to Monday.


## MongoDB

**Type:** integration  
**Product:** MongoDB  
**Commands:**

- `mongodb-get-entry-by-id`: Get an entry from database by ID
- `mongodb-query`: Searches for items by using the specified JSON query. Search by regex is supported.
- `mongodb-insert`: Inserts an entry to the database
- `mongodb-update`: Updates an entry in a collection
- `mongodb-delete`: Deletes an entry from the database
- `mongodb-list-collections`: Lists all collections in database
- `mongodb-create-collection`: Creates a collection
- `mongodb-drop-collection`: Drops a collection from the database
- `mongodb-pipeline-query`: Searches for items by the specified JSON pipleline query.
- `mongodb-bulk-update`: Bulk updates entries in a collection.


## MongoDB Atlas

**Type:** integration  
**Product:** MongoDB Atlas  

MongoDB Atlas is an integration that supports fetching and managing alerts and events within Cortex XSIAM. This integration was integrated and tested with version 2.0 of MongoDB Atlas

**Commands:**

- `mongo-db-atlas-get-events`: Retrieves a list of events from the MongoDB Atlas instance.


## MongoDB Key Value Store

**Type:** integration  
**Product:** MongoDB  
**Commands:**

- `mongodb-write-key-value`: Adds a key/value record for the incident. If the key exists, the existing value is overwritten.*
- `mongodb-get-key-value`: Returns the value of the specified name/key of an incident.
- `mongodb-list-key-values`: Lists the keys and their values for the specified incident.
- `mongodb-delete-key`: Deletes the key/value record for an incident.
- `mongodb-purge-entries`: Purges all keys/values for an incident. A common use case for this command is when closing an incident. This command clears the entries for the closed incident 
- `mongodb-get-keys-number`: Returns the number of key/value pairs for an incident.
- `mongodb-list-incidents`: Lists all incidents in the collection.


## MongoDB Log

**Type:** integration  
**Product:** MongoDB  
**Commands:**

- `mongodb-read-log`: Returns all log entries.
- `mongodb-write-log`: Adds a log entry.
- `mongodb-logs-number`: Returns the number of log entries.


## MS-ISAC

**Type:** integration  
**Product:** MS-ISAC  

This API queries alerts and alert data from the MS-ISAC API to enrich and query alerts from the platform This integration was integrated and tested with version 1.2 (7/1/25) of the MS-ISAC API

**Commands:**

- `msisac-get-alert`: Retrieve alert data by its ID
- `msisac-retrieve-cases`: Retrieves a list of MS-ISAC cases created since the given timestamp.


## MSEScoreWidget

**Type:** script  
**Product:** Suspicious Domain Hunting  

This dynamic automation parses the CVSS score of a CVE and presents it in the layout in color according to its score


## MyToDoTasksWidget

**Type:** script  
**Product:** Common Widgets  

A script that creates a table of all the ToDo tasks assigned to the current user


## NCSCReportDetails

**Type:** script  
**Product:** NCSC Cyber Asssessment Framework  

This script generates the report details used in the final report. This automation runs using the default Limited User role, unless you explicitly change the permissions. For more information, see the section about permissions here: For the platform, see the  for the platform, see the  for the platform, see the


## NCSCReportDetails_A

**Type:** script  
**Product:** NCSC Cyber Asssessment Framework  

This script generates the report details for the individual CAF Section


## NCSCReportDetails_B

**Type:** script  
**Product:** NCSC Cyber Asssessment Framework  

This script generates the report details for the individual CAF Section


## NCSCReportDetails_C

**Type:** script  
**Product:** NCSC Cyber Asssessment Framework  

This script generates the report details for the individual CAF Section


## NCSCReportDetails_D

**Type:** script  
**Product:** NCSC Cyber Asssessment Framework  

This script generates the report details for the individual CAF Section


## NCSCReportOverview

**Type:** script  
**Product:** NCSC Cyber Asssessment Framework  

This script generates the report details for the individual CAF Section


## Ncurion

**Type:** integration  
**Product:** Ncurion  

This is the Ncurion integration for getting started. This integration was integrated and tested with version 1 of Ncurion

**Commands:**

- `ncurion-get-log-list`: 


## Neosec

**Type:** integration  
**Product:** Neosec  

Neosec is reinventing application security. Its pioneering SaaS platform gives security professionals visibility into behavior across their entire API estate. Built for organizations that expose APIs to partners, suppliers, and users, Neosec discovers all your APIs, analyzes their behavior, and stops threats lurking inside

**Commands:**

- `neosec-alert-status-set`: Set alert status(Open, Closed)


## Netcraft

**Type:** integration  
**Product:** Netcraft  

Netcraft takedown, submission and screenshot management

**Commands:**

- `netcraft-attack-report`: Report a new attack or authorize an existing attack in the Takedown Service. If a takedown for the attack already exists in the Netcraft system it will be autho
- `netcraft-takedown-list`: Get a list of takedown objects. Netcraft has a limit of 1,000,000 objects returned within a 24 hour period (moving time window) per email address.
- `netcraft-takedown-update`: Update one or more fields related to a takedown.
- `netcraft-takedown-escalate`: Escalate an automated takedown to a managed takedown. Only attacks that are in an authorized state can be escalated. The minimum access level required to escala
- `netcraft-takedown-note-create`: Add a new note to an existing takedown.
- `netcraft-takedown-note-list`: Retrieve details of notes that have been added to takedowns.
- `netcraft-attack-type-list`: Get information on the attack types that are available under a given region.
- `netcraft-submission-list`: Get basic information about a submissions.
- `netcraft-file-report-submit`: Report files to Netcraft for analysis.
- `netcraft-submission-file-list`: Get basic information about a submission's files. When a submission is archived this command will return an error with the message "this submission has been arc
- `netcraft-file-screenshot-get`: Get a screenshot for a file associated with a submission.
- `netcraft-email-report-submit`: Report email messages to Netcraft for analysis. The email will be examined for malicious attachments and URLs. Optionally, emails can be encrypted before upload
- `netcraft-submission-mail-get`: Get basic information about a submission's email. When a submission is archived this command will return an error with the message "this submission has been arc
- `netcraft-mail-screenshot-get`: Get a screenshot for the email associated with a submission.
- `netcraft-url-report-submit`: Report URLs to Netcraft for analysis.


## NetQuest OMX

**Type:** integration  
**Product:** NetQuest OMX  

NetQuest’s products are high-capacity service nodes that help security teams access and analyze network traffic. Powerful packet and flow processing features assist security tools in detecting and mitigating security threats as cost effectively as possible. This integration was integrated and tested with version 3.7.5a of NetQuest OMX

**Commands:**

- `netquest-address-list-upload`: Uploads a .txt file with the address list to the appliance. The appliance temporarily stores the file until it is saved to the Library and replaces any previous
- `netquest-address-list-optimize`: Optimizes the updated address list. If the traffic elements are IP addresses, the integration will optimize the list by compressing IP addresses into CIDR group
- `netquest-address-list-create`: Creates a new address list. This list will replace and override the old list entity.
- `netquest-address-list-rename`: Renames an address list. This is only meant to change the name of the list. If you try to give the value of the new_name argument to an existing address list, t
- `netquest-address-list-delete`: Deletes the address list of the name provided.
- `get-events`: Gets events from NetQuest OMX. Each event is a report for the specified statistic type. Available only for Cortex XSIAM.


## Netscout Arbor Edge Defense

**Type:** integration  
**Product:** Netscout Arbor Edge Defense - AED  

The Netscout Arbor Edge Defense (AED) integration enables you to block and allow outbound and inbound traffic

**Commands:**

- `na-ed-outbound-blacklisted-countries-list`: Gets the countries on the outbound block list. By default, 10 block listed countries are returned.
- `na-ed-country-code-list`: Gets a country or list of countries (country name and ISO-standardized country code).
- `na-ed-outbound-blacklisted-countries-add`: Adds one or more countries to the outbound block list.
- `na-ed-outbound-blacklisted-countries-remove`: Removes one or more countries from the outbound block list.
- `na-ed-inbound-blacklisted-countries-list`: Gets the inbound block listed countries. By default, 10 block listed countries are returned. To return block listed countries for specific protection groups, sp
- `na-ed-inbound-blacklisted-countries-add`: Adds one or more countries to the inbound block list by pgid or cid.
- `na-ed-inbound-blacklisted-countries-remove`: Removes one or more countries from the block list for a specific protection group or for all protection groups.
- `na-ed-outbound-blacklisted-hosts-list`: Gets the outbound block listed hosts. By default, 10 block listed hosts are returned.
- `na-ed-outbound-blacklisted-hosts-add`: Adds one or more hosts to the outbound block list.
- `na-ed-outbound-blacklisted-hosts-replace`: Replaces all the hosts on the outbound block listed list.
- `na-ed-outbound-blacklisted-hosts-remove`: Removes one or more hosts or CIDRS from the outbound block list.
- `na-ed-outbound-whitelisted-hosts-list`: Gets the outbound allow listed hosts. By default, 10 hosts on allow list are returned.
- `na-ed-outbound-whitelisted-hosts-add`: Adds one or more hosts to the outbound allow listed list.
- `na-ed-outbound-whitelisted-hosts-replace`: Replaces all the hosts on the outbound allow listed list.
- `na-ed-protection-groups-update`: Updates the settings for one or more protection groups.


## Netscout Arbor Sightline (Peakflow)

**Type:** integration  
**Product:** Netscout Arbor Sightline  

DDoS protection and network visibility. This integration was integrated and tested with version 9.3 of Netscout Arbor Sightline

**Commands:**

- `na-sightline-alert-annotation-list`: Lists the collection of annotations for a given alert.
- `na-sightline-alert-list`: List all alerts. When an alert ID is given, only the relevant alert will be fetched.
- `na-sightline-mitigation-list`: List all mitigations. When a mitigation ID is given, only the relevant mitigation will be fetched.
- `na-sightline-mitigation-create`: Add a TMS or flowspec mitigation with the attributes and relationships passed in the JSON sub_object.
- `na-sightline-mitigation-delete`: Delete a given mitigation.
- `na-sightline-mitigation-template-list`: Get a list of available mitigation templates.
- `na-sightline-router-list`: Get a list of available routers.
- `na-sightline-managed-object-list`: Get a list of available managed objects.
- `na-sightline-tms-group-list`: Get a list of available TMS groups.


## NetwitnessQuery

**Type:** script  
**Product:** RSA NetWitness  

Performs a query against the meta database

**Inputs:**

- `id1`: The starting meta ID. To run the query from the most recent to the oldest meta, make ID1 larger than ID2. (uint64, optional)
- `id2`: The ending meta ID. (uint64, optional)
- `size`: The maximum number of entries to return, or just stream back all results if zero. (uint32, optional)
- `query`: The query string to use. (string, optional)
- `flags`: The flags to use for the query. Can be, "number" (bitwise mask), or "comma-separated-values" like query-log. (string, optional)
- `threshold`: Queries the optimization to stop processing results after the threshold is reached. This is useful with select aggregate functions. Zero mea


## NetwitnessSAAddEventsToIncident

**Type:** script  
**Product:** RSA NetWitness Security Analytics  

Adds new events to an existing NetWitness SA incident

**Inputs:**

- `incidentId`: The existing incident ID. (string)
- `eventList`: The list of event IDs separated by a comma (,), this must not include spaces in it. In order to get list of events you can use nw-get-events
- `alertSummary`: The short summary of the alert that will be attached to incident. (string)
- `severity`: The severity of the incident. For example, 50. (number)
- `deviceId`: The ID of the device/component. For example, Concentrator, Log Decoder, Packet Decoder, etc... from which the events are. The list of device
- `incidentManagementId`: The ID of the NetWitness INCIDENT_MANAGEMENT device/component ID. It can be received by running nw-get-component command. If this argument i


## NetwitnessSACreateIncident

**Type:** script  
**Product:** RSA NetWitness Security Analytics  

Creates an incident inside NetWitness SA from a set of NetWitness events

**Inputs:**

- `alertSummary`: The short summary of the alert which will be attached to incident. (string)
- `severity`: The severity level. The default set to "50". (optional string)
- `name`: The name of the incident. (string)
- `assigned`: Sets the assignee login name if the assignee has changed. You can execute nw-get-available-assignees to get the list of users. For example, 
- `eventList`: The list of event IDs separated by comma (,). This must not include spaces in it. In order to get the list of events you can should use the 
- `deviceId`: The ID of the device/component (Concentrator, Log Decoder, Packet Decoder, etc.) from which the events are retrieved. The list of devices ca
- `priority`: The priority of the incident.
- `summary`: The summary of the incident.


## NetwitnessSAGetAvailableAssignees

**Type:** script  
**Product:** RSA NetWitness Security Analytics  

Returns the available NetWitness SA users to be assigned to incidents


## Nexthink

**Type:** integration  
**Product:** Nexthink  

Nexthink helps IT teams deliver on the promise of the modern digital workplace. Nexthink is the only solution to provide enterprises with a way to visualize, act and engage across the entire IT ecosystem to lower IT cost and improve digital employee experience. This integration was integrated and tested with version 1.0.1 of Nexthink

**Commands:**

- `nt-compliance-check`: Verify antivirus/antispyware status.
- `nt-endpoint-details`: Get endpoint details.


## NGFW Remove Offline TS Agent

**Type:** playbook  
**Product:** NGFW TS Agent Deployment  

Check if TS Agent server is offline and deregister it from the NGFW

**Inputs:**

- `TSAgent`: The TSAgent Object


## NGINXApiModule

**Type:** script  

Common NGINX code that will be appended into each NGINX based integration when it's deployed


## Nist NVD

**Type:** integration  
**Product:** Nist NVD  

National Vulnerability Database

**Commands:**

- `nvd-get-vulnerability`: You can get latest vulnerabilities with given time from National Vulnerability Database.
- `nvd-search-keyword`: The keyword parameter allows your application to retrieve records where a word or phrase is found in the vulnerability description or reference links.
- `nvd-search-cvss`: CVSS refers to the scoring system used by NIST to assess the severity of vulnerabilities, https://www.first.org/cvss/. NVD provides base scores using the CVSS v
- `nvd-search-cwe`: CWE refers to the classification of vulnerabilities at https://cwe.mitre.org/. NIST staff associate one or more CWE to each vulnerability during the analysis pr
- `nvd-search-cpe`: NVD analysts identify which product or products are affected by each vulnerability. The set of associated products is known as the applicability statement of th
- `nvd-search-cve`: Search specific CVE


## nmap

**Type:** integration  
**Product:** Nmap  

Run nmap scans with the given parameters. This integration was integrated and tested with version 7.70 of nmap. The nmap binary is shipped with the integration Docker. You can see the options available for running an nmap scan here:  Some scan options require root access for using raw packet scanning techniques. See here for detailed scanning techniques. If you've configured the server to run Docker images with a non-root internal user and you want to use raw packet scanning (for example via the -sS option for SYN/ACK scan), make sure to exclude the platform/nmap Docker image as documented For the platform. For the platform. For the platform.7 On-prem here

**Commands:**

- `nmap-scan`: Scan targets with the given parameters.


## NMAP - Banner Check

**Type:** playbook  
**Product:** Nmap  

Sub-playbook that performs an Nmap scan and compares the results against a regular expression for a match. This could be used to look for OpenSSH versions or other OS information found in the banner

**Inputs:**

- `RemoteIP`: Remote IP address in an incident/alert.
- `RemotePort`: Remote port number in incident/alert
- `Regex`: Regular expression to compare against the banner for a match.
- `NMAPOptions`: Options to be used for the Nmap scan. (We do "--script=banner -p\<RemotePort>" by default and recommend using "-Pn" to skip the ping check.)


## NodeZero

**Type:** integration  
**Product:** NodeZero  

Integrates with the NodeZero autonomous penetration testing platform to fetch weaknesses discovered during pentest operations. Automatically ingests HIGH and CRITICAL severity weaknesses as incidents for tracking and remediation

**Commands:**

- `nodezero-get-weaknesses`: Retrieves HIGH and CRITICAL weaknesses discovered by NodeZero pentests.


## NodeZero MCP

**Type:** integration  
**Product:** NodeZero MCP  

Use the NodeZero MCP integration to connect to the NodeZero MCP server and automatically discover its available pentesting tools. This integration uses OAuth 2.0 Dynamic Client Registration (DCR). It registers itself as a public OAuth client with the NodeZero OAuth proxy, so no pre-issued Client ID or Client Secret is required. Authentication flows through the NodeZero portal

**Commands:**

- `list-tools`: Retrieves a list of available tools on the NodeZero MCP server.
- `call-tool`: Calls a specific tool on the NodeZero MCP server with optional input parameters.
- `nodezero-mcp-generate-login-url`: Registers this integration with your NodeZero portal and generates a login URL. To authenticate through the NodeZero portal, follow the instructions that the co
- `nodezero-mcp-auth-test`: Tests the OAuth authentication configuration with the NodeZero MCP server.


## NotInContextVerification

**Type:** script  
**Product:** Common Scripts  

Executes the given command and verifies that the specified field is not in the context after execution

**Inputs:**

- `cmdToRun`: The command or automation script to execute each while loop iteration.
- `cmdArguments`: The comma-separated list of command/automation arguments and values to run. For example, "key=val,key=val,key=val".
- `keyToWatch`: The key to watch, if it is equal to value argument (${key}==value) then exit while loop, otherwise continue to the next loop iteration. The 


## Nutanix Hypervisor

**Type:** integration  
**Product:** Nutanix Hypervisor  

Nutanix Hypervisor abstracts and isolates the VMs and their programs from the underlying server hardware, enabling a more efficient use of physical resources, simpler maintenance and operations, and reduced costs. This integration was integrated and tested with version v2 of Nutanix

**Commands:**

- `nutanix-hypervisor-hosts-list`: Gets the list of physical hosts configured in the cluster.
- `nutanix-hypervisor-vms-list`: Gets a list of virtual machines.
- `nutanix-hypervisor-vm-powerstatus-change`: Sets the power state of a virtual machine. If the virtual machine is being powered on and no host is specified, the host with the most available CPU and memory 
- `nutanix-hypervisor-task-results-get`: Returns the results of given tasks. If a task is not ready, its status will be returned.
- `nutanix-hypervisor-alerts-list`: Gets the list of alerts generated in the cluster that matches the filters. Nutanix fetches the latest alerts created if there are more than the defined maximum 
- `nutanix-hypervisor-alert-acknowledge`: Acknowledges the alert with the specified alert_id.
- `nutanix-hypervisor-alert-resolve`: Resolves the alert with the specified alert_id. Alert ID is the 'id' field returned for alerts by command 'nutanix-hypervisor-alerts-list'
- `nutanix-hypervisor-alerts-acknowledge-by-filter`: Acknowledges alerts using a filter.
- `nutanix-hypervisor-alerts-resolve-by-filter`: Resolves alerts using a filter.


## O365 File Management (Onedrive/Sharepoint/Teams)

**Type:** integration  
**Product:** Microsoft Graph Files  

Use the O365 File Management (Onedrive/Sharepoint/Teams) integration to enable your app to get authorized access to files in OneDrive, SharePoint, and MS Teams across your entire organization. This integration requires admin consent

**Commands:**

- `msgraph-delete-file`: Deletes an item from OneDrive.
- `msgraph-upload-new-file`: Uploads a file from the platform.
- `msgraph-replace-existing-file`: Replaces the content of the file in the specified MS Graph resource.
- `msgraph-create-new-folder`: Creates a new folder in a drive with the specified parent item or path.
- `msgraph-list-drives-in-site`: Returns the list of document libraries (drives) available for a target site.
- `msgraph-list-drive-content`: Returns a list of files and folders in the specified drive.
- `msgraph-list-sharepoint-sites`: Returns a list of the tenant sites.
- `msgraph-download-file`: Downloads the file contents of the drive item.
- `msgraph-list-site-permissions`: List of apps with permissions for the site. If permission_id is provided, it will return the details of that permission.
- `msgraph-create-site-permissions`: Create a new application permission for a site.
- `msgraph-update-site-permissions`: Updates an existing permission for a site.
- `msgraph-delete-site-permissions`: Deletes an app permission from a site.
- `msgraph-files-auth-test`: Tests connectivity to Microsoft.
- `msgraph-files-generate-login-url`: Generate the login URL used for Authorization code flow.
- `msgraph-files-auth-reset`: Run this command if for some reason you need to rerun the authentication process.


## O365 File Management (Onedrive/Sharepoint/Teams) (Standard Connector)

**Type:** integration  
**Product:** Microsoft Graph Files (Standard Connector)  

Use the O365 File Management (Onedrive/Sharepoint/Teams) integration to enable your app to get authorized access to files in OneDrive, SharePoint, and MS Teams across your entire organization. This integration requires admin consent

**Commands:**

- `msgraph-delete-file`: Deletes an item from OneDrive.
- `msgraph-upload-new-file`: Uploads a file from the platform.
- `msgraph-replace-existing-file`: Replaces the content of the file in the specified MS Graph resource.
- `msgraph-create-new-folder`: Creates a new folder in a drive with the specified parent item or path.
- `msgraph-list-drives-in-site`: Returns the list of document libraries (drives) available for a target site.
- `msgraph-list-drive-content`: Returns a list of files and folders in the specified drive.
- `msgraph-list-sharepoint-sites`: Returns a list of the tenant sites.
- `msgraph-download-file`: Downloads the file contents of the drive item.
- `msgraph-list-site-permissions`: List of apps with permissions for the site. If permission_id is provided, it will return the details of that permission.
- `msgraph-create-site-permissions`: Create a new application permission for a site.
- `msgraph-update-site-permissions`: Updates an existing permission for a site.
- `msgraph-delete-site-permissions`: Deletes an app permission from a site.
- `msgraph-files-auth-test`: Tests connectivity to Microsoft.
- `msgraph-files-generate-login-url`: Generate the login URL used for Authorization code flow.
- `msgraph-files-auth-reset`: Run this command if for some reason you need to rerun the authentication process.


## O365 Message Trace

**Type:** integration  
**Product:** Microsoft Exchange Online  

Message Trace enables tenant administrators to track the lifecycle of an email, determine its delivery status (delivered, pending, failed, or quarantined), and understand the actions applied to it. This integration was integrated and tested with the Graph-based Message Trace API (v1.0/admin/exchange/tracing/messageTraces)

**Commands:**

- `o365-message-trace-generate-login-url`: Generates the login URL for the authorization code flow.
- `o365-message-trace-auth-test`: Tests connectivity to Microsoft.
- `o365-message-trace-auth-reset`: Clears the saved access token / refresh token from the integration context, so on the next run a fresh authorization code (or client-credentials token) is reque
- `o365-message-trace-get-events`: Retrieves Exchange Online Message Trace events. Use this command for development and debugging only, as it may produce duplicate events, exceed API rate limits,


## O365 Outlook Mail (Using Graph API)

**Type:** integration  
**Product:** Microsoft Graph Mail  

Microsoft Graph lets your app get authorized access to a user's Outlook mail data in a personal or organization account. This integration was integrated and tested with version v1 of Microsoft Graph

**Commands:**

- `msgraph-mail-list-emails`: Gets the properties of returned emails. Typically shows partial results, use the "page_size" and "pages_to_pull" arguments to get all results.
- `msgraph-mail-get-email`: Returns the properties of an email.
- `msgraph-mail-delete-email`: Deletes an email.
- `msgraph-mail-list-attachments`: Lists all of the attachments of given email
- `msgraph-mail-get-attachment`: Gets an attachment from the email.
- `msgraph-mail-list-folders`: Returns the mail folder list directly under the root folder.
- `msgraph-mail-list-child-folders`: Returns the folder list under the specified folder.
- `msgraph-mail-create-folder`: Creates a new folder under the specified folder (parent).
- `msgraph-mail-update-folder`: Updates the properties of the specified folder.
- `msgraph-mail-delete-folder`: Deletes the specified mail folder.
- `msgraph-mail-move-email`: Moves a message to a different folder.
- `msgraph-mail-get-email-as-eml`: Retrieves an email message by message ID and uploads the content as an EML file.
- `msgraph-mail-create-draft`: Creates a draft message in the specified user's mailbox.
- `send-mail`: Sends an email using Microsoft Graph. Note: The from argument needs to be specified when the Email address from which to fetch incidents parameter is missing.
- `msgraph-mail-reply-to`: The replies to the recipients of a message.


## O365 Teams (Using Graph API)

**Type:** integration  
**Product:** MicrosoftGraphTeams  

Microsoft Graph lets your app get authorized access to a user's Teams app in a personal or organization account. This is a long-running integration. For more information about long-running integrations, see the the platform, the platform

**Commands:**

- `msgraph-teams-list-chats`: Retrieve the list of chats that the user is part of.
- `msgraph-teams-create-chat`: Create a new chat.
- `msgraph-teams-get-chat`: Retrieve a single chat (without its messages).
- `msgraph-teams-update-chat`: Update the properties of a chat object.
- `msgraph-teams-list-members`: List all conversation members in a chat.
- `msgraph-teams-add-member`: Add a conversationMember to a chat.
- `msgraph-teams-list-messages`: Retrieve the list of messages in a chat.
- `msgraph-teams-send-message`: Send a new message in a chat.
- `msgraph-teams-test`: Tests connectivity to Microsoft Graph Teams.
- `msgraph-teams-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `msgraph-teams-generate-login-url`: Generate the login url used for Authorization code flow.


## OctoxLabs

**Type:** integration  
**Product:** OctoxLabs  

Octox Labs Cyber Security Asset Management platform This integration was integrated and tested with version 4.5.0 of OctoxLabs

**Commands:**

- `octoxlabs-get-adapters`: Fetch octoxlabs all adapters
- `octoxlabs-get-connections`: Fetch octoxlabs connections
- `octoxlabs-get-discoveries`: Fetch octoxlabs discoveries
- `octoxlabs-get-last-discovery`: Get last success discovery
- `octoxlabs-search-devices`: Search in your devices
- `octoxlabs-get-device`: Fetch your device
- `octoxlabs-get-queries`: Fetch your queries
- `octoxlabs-get-query-by-id`: Fetch your queries by id
- `octoxlabs-get-query-by-name`: Fetch your queries by id
- `octoxlabs-get-user-by-username`: Fetch your Users by username
- `octoxlabs-get-groups`: Fetch your Groups
- `octoxlabs-get-companies`: Fetch your Companies
- `octoxlabs-get-domain-by-domain-name`: Fetch your Domain by Domain name.
- `octoxlabs-get-company-by-id`: Fetch your Company by id.
- `octoxlabs-get-permissions`: Fetch your Permissions


## OktaApiModule

**Type:** script  

Common Okta client code that will be appended into each Okta based integration when it's deployed


## OktaIAMApiModule

**Type:** script  

Common Okta IAM code that will be appended into the Okta IAM integrations when it's deployed. This module holds the shared implementation behind the Okta IAM integrations: Both integrations are thin shims that call run_okta_iam_integration(). The module imports IAMApiModule internally, so the vendor-neutral IAM primitives (IAMUserProfile, IAMActions, IAMErrors) remain available to the Okta IAM code without adding Okta-specific symbols to the shared IAMApiModule


## Oletools

**Type:** script  
**Product:** Oletools  

This is an automation to run oletools malware analysis for office files. Oletools is a tool for analyzing Microsoft OLE2 files, such as Microsoft Office documents or Outlook messages, mainly for malware analysis, forensics, and debugging. Note that oletools is open source code and is subject to change

**Inputs:**

- `ole_command`: The OLE command to activate.- oleid - to analyze OLE files to detect specific characteristics usually found in malicious files.- oleobj - to
- `entryID`: The file to activate the oletools analysis on.
- `decode`: Display all the obfuscated strings with their decoded content (Hex, Base64, StrReverse, Dridex, VBA). Note that this works only with the ole
- `password`: If encrypted office files are encountered, try decryption with this password. May be repeated.


## Ollama

**Type:** integration  
**Product:** Ollama  

Integrate with open source LLMs using Ollama. With an instance of Ollama running locally you can use this integration to have a conversation in an Incident, download models, and create new models

**Commands:**

- `ollama-list-models`: Get a list of all available models
- `ollama-model-pull`: Pull a model
- `ollama-model-delete`: Delete a model
- `ollama-conversation`: General chat command that tracks the conversation history in the Incident.
- `ollama-model-info`: Show information for a specific model.
- `ollama-model-create`: Create a new model from a Modelfile.
- `ollama-generate`: Generate a response for a given prompt with a provided model. Conversation history IS NOT tracked.


## OnboardingIntegration

**Type:** integration  
**Product:** OnboardingIntegration  

Creates mock email incidents using one of two randomly selected HTML templates. Textual content is randomly generated and defined to include some text (100 random words) and the following data (at least 5 of each data type): IP addresses, URLs, SHA-1 hashes, SHA-256 hashes, MD5 hashes, email addresses, domain names

**Commands:**

- `demo-ip`: Gets the simulated reputation of the IP address.
- `demo-url`: Gets the simulated reputation of the URL address.
- `demo-domain`: Gets the simulated reputation of the domain.
- `demo-file`: Gets the simulated reputation of the file hash.
- `demo-email`: Gets the simulated reputation of the email address.


## OpenAI GPT

**Type:** integration  
**Product:** OpenAI  
**Commands:**

- `gpt-send-message`: Send a message as a prompt to the GPT model.
- `gpt-check-email-body`: Check email body for possible security issues.
- `gpt-check-email-header`: Check email body for possible security issues.
- `gpt-analyze-email-header`: Analyze email headers for potential security issues using the OpenAI Responses API. This command uses the Responses API which is recommended for all new project
- `gpt-analyze-email-body`: Analyze email body for potential security risks using the OpenAI Responses API. This command uses the Responses API which is recommended for all new projects (i
- `gpt-create-soc-email-template`: Create an email template out of the conversation context to be sent from the SOC.
- `gpt-draft-soc-email`: Draft a SOC email template using the OpenAI Responses API. This command uses the Responses API which is recommended for all new projects (instead of gpt-create-
- `openai-get-events`: Manually fetch a bounded batch of Audit and/or Compliance events for development/debugging. Does NOT advance the persisted last_run cursor, so it is safe to run
- `gpt-create-response`: Sends a message to the OpenAI Responses API and receives the generated response. This command uses the Responses API which is recommended for all new projects (
- `gpt-list-models`: Lists all models available to the configured API key. Lets users discover models per their actual API-key tier without redeploying the integration when OpenAI s
- `gpt-create-moderation`: Runs text or an image through the OpenAI Moderations API and returns per-category flagging results. Exactly one of text, entry_id, or image_url must be provided


## OpenCVE

**Type:** integration  
**Product:** OpenCVE  

Ingests CVEs from an instance of OpenCVE

**Commands:**

- `opencve-latest`: Returns the latest updated CVEs from your reports.
- `cve`: Returns CVE information by CVE ID.
- `opencve-get-my-vendors`: List the vendors subscriptions of the authenticated user.
- `opencve-get-my-products`: List the products subscriptions of the authenticated user.
- `opencve-get-vendor-cves`: Get vendor CVEs.
- `opencve-get-product-cves`: Get product CVEs.
- `opencve-get-reports`: List the reports of the authenticated user or get a specific report.
- `opencve-get-alerts`: List the alerts of a report or get the details of a specific alert.
- `opencve-get-products`: List the products associated to a vendor or get a specific one.
- `opencve-get-vendors`: List the products associated to a vendor or get a specific product of a vendor by specifying its name.


## OPNSense

**Type:** integration  
**Product:** OPNSense  

Manage OPNsense Firewall. For more information see OPNsense documentation. OPNsense is an open source, easy-to-use and easy-to-build HardenedBSD based firewall and routing platform. This integration was integrated and tested with version 22.1 of OPNSense

**Commands:**

- `opnsense-alias-list`: Get aliases list
- `opnsense-alias-add`: Create new alias
- `opnsense-alias-del`: Delete alias with uuid
- `opnsense-alias-mod`: Modify an existing alias
- `opnsense-alias-mod-additem`: Add item into existing alias
- `opnsense-alias-mod-delitem`: Del item into existing alias
- `opnsense-alias-get`: Get alias details
- `opnsense-alias-get-uuid`: Get alias UUID
- `opnsense-interfaces-list`: Get interfaces list
- `opnsense-category-list`: Get categories list
- `opnsense-category-add`: Create new category
- `opnsense-category-del`: Delete category with uuid
- `opnsense-category-get`: Get category details
- `opnsense-category-mod`: Modify an axisting category
- `opnsense-rule-list`: Get rules list


## OpsGenie v3

**Type:** integration  
**Product:** OpsGenie  

Integration with Atlassian OpsGenie. OpsGenie is a cloud-based service that enables operations teams to manage alerts generated by monitoring tools to ensure the right people are notified, and the problems are addressed in a timely manner. This integration was integrated and tested with OpsGenie. Some changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

**Commands:**

- `opsgenie-create-alert`: Create an alert in Opsgenie.
- `opsgenie-get-alerts`: List the current alerts from OpsGenie.
- `opsgenie-delete-alert`: Delete an alert from OpsGenie.
- `opsgenie-ack-alert`: Acknowledge an alert in OpsGenie.
- `opsgenie-close-alert`: Close an alert in OpsGenie.
- `opsgenie-assign-alert`: Assign an OpsGenie alert.
- `opsgenie-add-responder-alert`: Add a responder to an OpsGenie alert.
- `opsgenie-get-escalations`: Get escalations from OpsGenie.
- `opsgenie-escalate-alert`: Escalate an OpsGenie alert.
- `opsgenie-add-alert-tag`: Add tag to the OpsGenie alert.
- `opsgenie-remove-alert-tag`: Remove a tag from the OpsGenie alert.
- `opsgenie-get-alert-attachments`: Get the attachments of the alert.


## Oracle IAM

**Type:** integration  
**Product:** Oracle IAM  

Integrate with Oracle Identity Access Management service to execute CRUD (create, read, update, and delete) operations for employee lifecycle processes

**Commands:**

- `iam-create-user`: Creates a user.
- `iam-get-user`: Retrieves a single user resource.
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-disable-user`: Disable an active user.
- `iam-create-group`: Creates an empty group
- `iam-get-group`: Retrieves the group information including members
- `iam-delete-group`: Permanently removes a group.
- `iam-update-group`: Updates an existing group resource. This command allows individual (or groups of) users to be added or removed from the group with a single operation. A maximum


## Orca

**Type:** integration  
**Product:** Orca  

Agentless, Workload-Deep, Context-Aware Security and Compliance for AWS, Azure, and GCP. This integration was integrated and tested with Orca

**Commands:**

- `orca-get-alerts`: Get the alerts on cloud assets


## OrionMalware

**Type:** integration  
**Product:** OrionMalware  

This is the Orion Malware integration. Analyzes hash and files with static and dynamic analysis This integration was integrated and tested with version 5.3.0 of OrionMalware

**Commands:**

- `hash-scan`: Check hash value against Orion Malware database
- `file-scan`: Detonate file in Orion Malware


## OSQueryBasicQuery

**Type:** script  
**Product:** OS Query  

Returns the results from a basic OSQuery query on a remote Linux machine. For more information read this documentation

**Inputs:**

- `system`: The system to remote execute on. This can be a list of systems.
- `query`: The osquery query to execute on the remote system.


## Osxcollector

**Type:** script  
**Product:** OSX Collector  

Execute OSXcollector on a machine. This can run only on OSX

**Inputs:**

- `section`: Asks OSXCollector for a specific section.
- `timeout`: The timeout period for the OSXCollector execution to complete. If omitted, the default wil be 10 minutes.


## OutOfOfficeListCleanup

**Type:** script  
**Product:** Shift Management  

Removes any users from the out-of-office list whose 'off until day' is in the past

**Inputs:**

- `listname`: The name of the out-of-office list. Default is "OOO List".


## PadZeros

**Type:** script  
**Product:** Filters And Transformers  

Adds zeros (0) to the beginning of the string, until the string reaches the specified length

**Inputs:**

- `value`: String to pad with zeros.
- `length`: The desired length of the string. The value specified in the "value" argument will be padded with zeros until the string reaches this length


## PagerDuty v2

**Type:** integration  
**Product:** PagerDuty  

Use the PagerDuty integration to manage schedules and on-call users. This integration was integrated and tested with PagerDuty API v2

**Commands:**

- `PagerDuty-get-all-schedules`: Receive all schedules from PagerDuty.
- `PagerDuty-get-users-on-call`: Returns the names and details of on call users at a certain time or by specific schedule.
- `PagerDuty-get-users-on-call-now`: Returns the names and details of current on call personnel.
- `PagerDuty-incidents`: Shows incidents in PagerDuty. Default status parameters are triggered,acknowledged.
- `PagerDuty-submit-event`: Creates a new event/incident in PagerDuty(In order to use this command you have to enter the Service Key in the integration settings).
- `PagerDuty-get-contact-methods`: Get the contact methods of a given user.
- `PagerDuty-get-users-notification`: Get the users notification rules.
- `PagerDuty-resolve-event`: Resolves an existing event in PagerDuty.
- `PagerDuty-acknowledge-event`: Acknowledges an existing event in PagerDuty.
- `PagerDuty-get-incident-data`: Get data about a incident from PagerDuty.
- `PagerDuty-get-service-keys`: Get Service keys for each of the services configured in the PagerDuty instance.
- `PagerDuty-add-responders`: Add responders to an incident.
- `PagerDuty-run-response-play`: Run a response play on PagerDuty (based on its UUID).


## PagerDutyAlertOnIncident

**Type:** script  
**Product:** PagerDuty  

Sends incident details to pagerduty

**Inputs:**

- `author`: The email address of the user to be alerted about the incident.


## PagerDutyAssignOnCallUser

**Type:** script  
**Product:** PagerDuty  

Assigns the first on-call user to an investigation by default. All incidents in the investigation will be owned by the on call user

**Inputs:**

- `escalation_policy_ids`: The comma-separated escalation policy IDs from which choose the oncall user.
- `schedule_ids`: The comma-separated schedule IDs from which to choose the oncall user.


## PAN-OS create or edit policy

**Type:** playbook  
**Product:** Change Management  

This playbook will automate the process of creating or editing a policy. The first task in the playbook checks whether there is a security policy that matches the playbook inputs. If there is no security policy that matches, a new policy will be created. If there is a security policy that matches, the user will be able to modify the existing policy or create a new hardened policy

**Inputs:**

- `Destination`: Destination.
- `Source`: Source.
- `Protocol`: The IP protocol number
- `Action`: Action for the rule (allow, deny, drop)
- `Application`: A comma-separated list of application object names for the rule to create.
- `Destination_zone`: A comma-separated list of destination zones.
- `Log_forwarding`: Log forwarding profile.
- `Profile_setting`: A profile setting group.


## PAN-OS edit policy

**Type:** playbook  
**Product:** Change Management  

This playbook guides the user in the process of editing existing policy. The playbook sends a data collection form to retrieve the relevant parameters for editing the existing rule

**Inputs:**

- `SecurityTeamEmail`: The email of the relevant security team for firewall change management approval.
- `rulename`: The name of the relevant policy.


## PAN-OS EDL Service Configuration

**Type:** playbook  
**Product:** Generic Export Indicators Service  

This single-run playbook enables the platform, and configures PAN-OS EDL objects and the respective firewall policy rules. The EDLs will continuously update for each indicator that matches the query syntax inputted in the playbook (in order to validate to which indicators the query applies, you need to enter the query syntax from the indicator tab at the top of the playbook inputs window as well). If both the IP and URL indicator types exist in the query, it sorts the indicators into two EDLs, IP and URL. If only one indicator type exists in the query, only one EDL is created. The playbook then creates EDL objects directed to the indicator lists and firewall policy rules in PAN-OS

**Inputs:**

- `ip-edl-object-name`: Set a name for the EDL object that will be configured on pan-os. This value is used to set the rule name as well.
- `url-edl-object-name`: Set a name for the EDL object that will be configured on pan-os. This value is used to set the rule name as well.
- `EDLServiceURL`: The EDL service provides serval access methods to the EDL instance. By default, it uses a unique port, configured in the EDL Service integra
- `InstanceName`: Name of the instance as configured in EDL Service integration. Only needed when accessing EDL Service by instance name. Refer to the EDL Ser
- `InstancePort`: Instance name port as configured in EDL Service integration. Only needed when accessing EDL Service by URL and Port. Refer to the EDL Servic
- `IndicatorQuery`: The query to run to create the EDL. When no query is entered, EDLs will contain all IP and URL indicators. The query should be inserted in t
- `AutoCommit`: This input establishes whether to commit the configuration automatically.Yes - Commit automatically.No - Commit manually.
- `RulePosition`: The position of the rule in the ruleset. Valid values are: * top * bottom * before * afterThe default position is 'top'.


## Panorays Findings API

**Type:** integration  
**Product:** Panorays  

Retrieve and monitor internal security findings for your organization, and critical findings across your supplier (third-party) portfolio, from the Panorays platform to automate incident response within the platform. This integration was integrated and tested with version v2 of PanoraysFindingsAPI

**Commands:**

- `panorays-finding-list`: Lists your own organization's findings as detected by Panorays.
- `panorays-supplier-finding-list`: Lists the findings detected by Panorays for a specific supplier (third party).
- `panorays-supplier-list`: Lists the suppliers (third parties) in your Panorays portfolio.


## PanoraysCheckOlderDuplicate

**Type:** script  
**Product:** Panorays  

Checks whether an older open/pending "Panorays Finding" incident already exists for the same Finding ID, by calling getIncidents server-side and returning a single explicit boolean output. Used by the Panorays Finding - Triage and Response playbook to avoid a race where two incidents created at nearly the same time could each see the other as already-open and both close as Duplicate - only the newer incident (higher ID) is ever told a duplicate exists

**Inputs:**

- `finding_id`: The Panorays Finding ID to search for.
- `incident_id`: The current incident's ID. Only other incidents with a lower ID are considered a match.


## PANW NGFW TS Agent Deployment

**Type:** playbook  
**Product:** NGFW TS Agent Deployment  

Deploy the PANW NGFW TS Agent to a Windows server

**Inputs:**

- `Host`: The host to perform the deployment on
- `Path`: The path to the TS Agent msi installer
- `Name`: The name of the TS Agent in NGFW console
- `StartSize`: The agent StartSize
- `MaxSize`: The agent MaxSize
- `StartPort`: The agent StartPort
- `EndPort`: The agent EndPort
- `FreePortBlockDelay`: The agent FreePortBlockDelay


## PAT HelpdeskAdvanced

**Type:** integration  
**Product:** PAT Helpdesk Advanced  

Improve the effectiveness of your service provision and resources, and the quality of your IT department. This integration was integrated and tested with version 11.2.3 of PATHelpdeskAdvanced

**Commands:**

- `hda-create-ticket`: Create a new ticket.
- `hda-list-tickets`: List tickets.
- `hda-add-ticket-attachment`: Add an attachment to a ticket.
- `hda-list-ticket-attachments`: List attachments for a ticket.
- `hda-add-ticket-comment`: Add a comment to a ticket.
- `hda-list-ticket-statuses`: List ticket statuses.
- `hda-change-ticket-status`: Change the status of a ticket.
- `hda-list-ticket-priorities`: List ticket priorities.
- `hda-get-ticket-history`: Get ticket history.
- `hda-list-users`: List users.
- `hda-list-groups`: List groups.


## PDFUnlocker

**Type:** script  
**Product:** Common Scripts  

Removes the password protection from a PDF file and adds a new file entry with the unlocked PDF

**Inputs:**

- `entryID`: The entry ID with the PDF file.
- `password`: The password for the PDF file.


## Penfield

**Type:** integration  
**Product:** PenfieldAI  

The penfield-get-assignee command takes in necessary context data, and returns the analyst that Penfield believes the incident should be assigned to based on Penfield's models of skill and process. The test command verfies that the endpoint is reachable. This integration was integrated and tested with version 0.1.4 of Penfield

**Commands:**

- `penfield-get-assignee`: Calls the Penfield API and returns the analyst Penfield recommends assigning the incident to. This information is saved in the output, but the incident will not


## Penfield Assign

**Type:** playbook  
**Product:** PenfieldAI  

Invokes Penfield.AI backend to assign the incident to an online analyst


## PenfieldAssign

**Type:** script  
**Product:** PenfieldAI  

PenfieldAssign will use the PenfieldGetAssignee integration to determine who an incident should be assigned to, then print the selected analyst to the War Room and overwrite the owner property

**Inputs:**

- `assign`: Whether this script should actually assign the incident by overwriting owner. Defaults to yes.


## Pentera

**Type:** integration  
**Product:** Pentera  
**Commands:**

- `pentera-run-template-by-name`: Run a specific template by its name. Please add the template name in the parameters
- `pentera-get-task-run-status`: Get the status of a task run by its task run id
- `pentera-get-task-run-full-action-report`: Get the full action report of a task run


## Pentera Filter And Create Incident

**Type:** playbook  
**Product:** Pentera  

Sub-playbook to select specific entries from the Pentera action report and create incidents for each of the selected entries

**Inputs:**

- `Filter password cracking`: Filter all password cracking operation types
- `Filter BlueKeep vulnerability`: Filter all BlueKeep operation types
- `Filter Minimum Severity`: Filters actions according to given value.
- `Will not filter anything if got zero (0) as value.`: 0
- `FullActionReport`: Pentera Full Action Report is the summary of the given TaskName in a CSV format, that contains all the actions that Pentera performed during
- `The value will be provided from Pentera Run Scan and Create Incidents playbook.`: 
- `Filter MS17-010 vulnerability`: Filter all MS17-010 operation types
- `Filter network device default password usage`: Filter all network device default password operation types


## PerformActionOnCampaignIncidents

**Type:** script  
**Product:** Phishing Campaign  

Perform user actions such as link, close, etc., on selected incidents from a campaign

**Inputs:**

- `similarity`: The incident similarity parameter (High or Low) to take from the context.


## PerimeterX BotDefender

**Type:** integration  
**Product:** PerimeterX  

Gathers PerimeterX related data

**Commands:**

- `ip`: Gets the PerimeterX DBotScore decision for a particular IP


## Perplexity AI

**Type:** integration  
**Product:** Perplexity AI  

Perplexity AI is a web search engine that uses a large language model to process queries and synthesize responses based on web search results. With a conversational approach, Perplexity AI allows users to ask follow-up questions and receive answers with citations to its sources from the internet

**Commands:**

- `deepresearch-chat`: Send a chat message. You may need to increase the command timeout in "advanced settings" from the default 5 minutes.


## PFXAnalyzer

**Type:** script  
**Product:** Common Scripts  

This Python script is designed to analyze a PFX (Personal Information Exchange) file for various suspicious or noteworthy characteristics from a security perspective

**Inputs:**

- `fileEntryId`: The ID of the file entry from the incident context that contains the PFX file.
- `pfxPassword`: Password for the PFX file (if encrypted).


## PHash

**Type:** script  
**Product:** Community Common Scripts  

Script to create a perceptual hash of an image (or file) stored in the incident. Wrapps

**Inputs:**

- `image`: EntryID of image


## PICUS NG - Simulation Validation Automation

**Type:** playbook  
**Product:** PicusNGAutomation  

Picus NG Simulation Validation Automation


## Picus Security NG

**Type:** integration  
**Product:** PicusNGAutomation  

This integration was integrated and tested with Picus NG

**Commands:**

- `picus-get-access-token`: OAuth2 protocol is used to authorize Refresh/Access tokens. To obtain the API, you should generate a refresh token and then request an access token using this c
- `picus-get-agent-list`: This command returns the simulation agent list with agent name, id, status, agent type and platform information as in Picus platform > Agents.
- `picus-get-agent-detail`: This command returns agent name, status, agent type, platform and also mitigation devices and attack modules using the agent ID.
- `picus-create-simulation`: This command creates and runs a simulation as requested; scheduled or instant. You can create a simulation by giving your simulation a name and adding the templ
- `picus-get-template-list`: This command returns template list that contains template name, id, description, content type, category as in Picus Platform> Threat Templates.
- `picus-get-integration-agent-list`: This command returns the agent name, id, status, agent installation information and the token expiration information.
- `picus-get-simulation-list`: This command returns the list of you latest simulation result overview as in Picus Platform > Simulations tab. Latest simulation run results are included.
- `picus-simulate-now`: This command runs the existing simulation using the Simulation ID.
- `picus-get-simulation-detail`: This command returns the information about a specific simulation.
- `picus-get-latest-simulation-result`: This command returns detailed information about simulation results including Prevention and Detection result details for the latest simulation run.
- `picus-get-simulation-result`: This command returns detailed information about simulation results including Prevention and Detection result details for a specific simulation run with run id.
- `picus-get-simulation-threats`: This command returns simulation result based on threats. Threat result includes threat id and name, prevention result and action count.
- `picus-get-simulation-actions`: This command returns simulation result based on action list using threat ID, simulation ID and simulation run ID.
- `picus-get-mitigation-devices`: This command returns mitigation device information as obtained under Picus platform > Mitigation > Vendor Based Mitigations. Vendor based mitigation devices can
- `picus-get-signature-list`: This command returns action based signature suggestions.


## PiHole

**Type:** integration  
**Product:** PiHole  

Pi-hole is a network-level advertisement and Internet tracker blocking application which acts as a DNS sinkhole and optionally a DHCP server, intended for use on a private network. This integration was integrated and tested with version FTL5.2 of PiHole

**Commands:**

- `pihole-get-version`: Returns the version of the API
- `pihole-get-type`: Returns the backend used by the API (either PHP or FTL)
- `pihole-get-summaryraw`: Gives statistics in raw format (no number formatting applied)
- `pihole-get-overtimedata10mins`: Data needed for generating the domains/ads over time graph on the Pi-hole web dashboard
- `pihole-get-topitems`: Data needed for generating the Top Domain and Top Advertisers Lists
- `pihole-get-topclients`: Data needed for generating the Top Clients list
- `pihole-get-forward-destinations`: Shows number of queries that have been forwarded and the target
- `pihole-get-query-types`: Shows number of queries that the Pi-hole’s DNS server has processed
- `pihole-get-all-queries`: Get DNS queries data
- `pihole-status`: Show status of pihole action (enabled - disabled)
- `pihole-enable`: Enable Pi-hole ad blocking
- `pihole-disable`: used to disable pihole for certain amount of time
- `pihole-get-versions`: Show versions of all components
- `pihole-get-topclientsblocked`: Shows the top clients being blocked
- `pihole-get-cache-info`: Show cache info


## PiHole v6

**Type:** integration  
**Product:** PiHole  

PiHole v6 integration using the new REST API. PiHole is a network-level advertisement and Internet tracker blocking application which acts as a DNS sinkhole and optionally a DHCP server, intended for use on a private network. This integration was integrated and tested with PiHole v6.0 API

**Commands:**

- `pihole-get-summary`: Get overview of PiHole activity including query stats, client counts, and gravity info.
- `pihole-get-top-domains`: Get top permitted or blocked domains.
- `pihole-get-top-clients`: Get top clients by query count.
- `pihole-get-upstreams`: Get metrics about upstream DNS destinations.
- `pihole-get-query-types`: Get breakdown of DNS query types.
- `pihole-get-recent-blocked`: Get most recently blocked domain(s).
- `pihole-get-history`: Get activity graph data (queries over time).
- `pihole-get-history-clients`: Get per-client activity graph data.
- `pihole-get-queries`: Get DNS query log with optional filtering.
- `pihole-get-blocking-status`: Get current PiHole blocking status.
- `pihole-set-blocking`: Enable or disable PiHole blocking, optionally with a timer.
- `pihole-get-domains`: Get domains from allow/deny lists. Filter by type and kind.
- `pihole-add-domain`: Add a domain to allow/deny list.
- `pihole-delete-domain`: Delete a domain from allow/deny list.
- `pihole-get-version`: Get PiHole component versions.


## Ping

**Type:** script  
**Product:** Common Scripts  

Pings an IP or url address, to verify it's up. Note - On the platform, the script can run only on a custom engine

**Inputs:**

- `address`: Address to ping


## PingCastle

**Type:** integration  
**Product:** PingCastle  

This integration will run a server that will listen for PingCastle XML reports. This integration was integrated and tested with version 6.0.0 of PingCastle. PingCastle is a long-running integration. For more information about long-running integrations, see the the platform, the platform

**Commands:**

- `pingcastle-get-report`: Get the Currently saved Ping Castle Report


## Pipl

**Type:** integration  
**Product:** Pipl  

Pipl provides a reputation for email addresses and identity solutions

**Commands:**

- `pipl-search`: Search for required query
- `email`: Searches for information regarding given email address


## Polar Security

**Type:** integration  
**Product:** Polar Security  

Polar Security, an innovator in technology that helps companies discover, continuously monitor and secure cloud and software-as-a-service (SaaS) application data – and addresses the growing shadow data problem

**Commands:**

- `polar-list-linked-vendors`: Get a list of all 3rd party vendors connected to your cloud workloads
- `polar-list-data-stores`: List observed data stores
- `polar-data-stores-summary`: Summarize your data stores by storage type, service provider, cloud location, etc.
- `polar-list-vendors-data-stores`: Get a list of all data stores a specific 3rd party vendor can access. See whether they have sensitivities and with what role the access is made possible.
- `polar-get-data-store`: Get a specific data store by its ID. Doesn't return anything above and beyond the polar-list-data-stores command, so no need to run it again if you've already r
- `polar-list-vendor-accessible-data-stores`: List all data stores accessible by 3rd party vendors, along with which vendors have access.
- `polar-apply-label`: Add or update a custom label to a data store


## PolySwarm

**Type:** integration  
**Product:** PolySwarm  

Real-time threat intelligence from a crowd-sourced network of security experts and antivirus companies

**Commands:**

- `polyswarm-get-report`: Returns a report using the UUID.
- `file`: Queries PolySwarm for file reputation information.
- `ip`: Queries PolySwarm for IP reputation information.
- `url`: Queries PolySwarm for URL reputation information.
- `domain`: Queries PolySwarm to retrieve domain reputation information.
- `url-scan`: Uploads a URL to PolySwarm and retrieves the analysis results.
- `file-rescan`: Rescans the uploaded artifact by hash.
- `get-file`: Downloads a file hash from PolySwarm.
- `file-scan`: Uploads a file to PolySwarm and retrieves the analysis results.


## Popular News

**Type:** integration  
**Product:** Popular Cybersecurity News  

How to use this integration ? This integration was integrated and tested with version 1.0.0 of Popular News

**Commands:**

- `get-news-KrebsOnSecurity`: Get News from KrebsOnSecurity
- `get-news-TheHackerNews`: Get News from TheHackerNews


## PopulateCriticalAssets

**Type:** script  
**Product:** Common Scripts  

Populates critical assets in a grid field that has the section headers "Asset Type" and "Asset Name"

**Inputs:**

- `critical_assets`: A list of all critical assets. Received as output from "Calculate Severity - Critical Assets v2" playbook.


## PortListenCheck

**Type:** script  
**Product:** Common Scripts  

Checks whether a port was open on a given host

**Inputs:**

- `host`: The hostname to check.
- `port`: The port to check.


## PositiveDetectionsVSDetectionEngines

**Type:** script  
**Product:** Common Scripts  

Shows a bar chart of the number of Positive Detections out of overall detections

**Inputs:**

- `indicator`: Indicator with detections custom fields


## Postmark Spamcheck

**Type:** integration  
**Product:** Postmark Spamcheck  

Postmark's spam API, Spamcheck, is a RESTfull interface to the Spam filter tool SpamAssassin

**Commands:**

- `postmark-spamcheck`: Check the spamscore of your email message


## Prepare your CTF

**Type:** playbook  
**Product:** Capture The Flag - 01  

This playbook aims to assit in configuring you env for the Capture The Flag (CTF) game


## PrepareArcannaRawJson

**Type:** script  
**Product:** ArcannaAI  

Transform a string into a json and escape it for Arcanna to use it in send_event


## PreProcessImage

**Type:** script  
**Product:** Common Scripts  

This script pre-processes an image file by preforming one of the following actions: Each action can also resize the image when given the width and height

**Inputs:**

- `action`: The action to perform on the image.
- `image_resize_width`: The desired width for resizing the image to.
- `image_resize_height`: The desired height for resizing the image to.
- `file_entry_id`: The entryID of the file to process.


## PrettyPrint

**Type:** script  
**Product:** Common Scripts  

Pretty-print data using Python's pprint library. This is useful for seeing the structure of incident and context data. Here's how to use it: !PrettyPrint value=${incident}

**Inputs:**

- `value`: The value to pretty-print.


## Prisma Cloud DSPM

**Type:** integration  
**Product:** DSPM  

The Prisma Cloud DSPM(Data Security Posture Management) integration enhances the management and remediation of DSPM risks. The integration provides users with actionable data, insights and a seamless workflow for addressing potential security threats

**Commands:**

- `dspm-list-risk-findings`: Retrieves risk findings matching the input criteria.
- `dspm-get-risk-finding-by-id`: Retrieves the details of a risk for the provided risk ID.
- `dspm-list-assets`: Retrieves a list of assets for the company.
- `dspm-get-asset-details`: Retrieves details for the specified asset ID.
- `dspm-get-asset-files-by-id`: Retrieves file details for the specified asset ID.
- `dspm-get-list-of-asset-fields-by-id`: Return list of fields for structured assets such as RDS, Aurora, and BigQuery.


## PrismaAirsApiModule

**Type:** script  

Provides shared Prisma AIRS code (OAuth2 client, plane routing, and scanner transport) that each Prisma AIRS integration reuses


## ProductJoin

**Type:** script  
**Product:** Filters And Transformers  

Returns the product of two lists, joined by a separator, as a list of strings

**Inputs:**

- `value`: The first list (or CSV string).
- `list2`: The second list (or CSV string).
- `join`: Separator


## Prometheus

**Type:** integration  
**Product:** Prometheus  

Query Prometheus via its HTTP API (/api/v1/query). Supports a pipe-separated metric list (e.g., "co2|solar|load") which is converted to a metric-name regex on name. Returns a tidy table plus machine-readable outputs under Prometheus.Metrics. This integration was integrated and tested with version 2.55 of Prometheus

**Commands:**

- `prometheus-query`: Query Prometheus instant vectors by metric name using a pipe-separated "fields" list. Builds {name=~"..."} (anchored by default) and calls /api/v1/query.
- `prometheus-raw`: Run any raw Prometheus instant query string against /api/v1/query.


## ProvidesCommand

**Type:** script  
**Product:** Common Scripts  

Finds which integrations implement a specific platform command. The results will be returned as comma-separated values (CSV). The "Core REST API" integration must first be enabled

**Inputs:**

- `command`: The integration command to find
- `enabled`: Filters results to integrations that are enabled or disabled. 'true' or 'false'. Will return both types by default. False means that an inte


## PublishEntriesToContext

**Type:** script  
**Product:** Common Scripts  

Publishes entries to the incident's context

**Inputs:**

- `ids`: The entry IDs to publish. This will accept comma-separated IDs or a list of strings.
- `out`: The name of the context key. The default is "entries".


## Pulsedive

**Type:** integration  
**Product:** Pulsedive  

Enrich and analyze any domain, URL, or IP. Pivot to search on data points and linked indicators to investigate risky properties. This integration was integrated and tested with version 5.1.15 of Pulsedive

**Commands:**

- `ip`: Return IP information and reputation
- `domain`: Returns Domain information and reputation.
- `url`: Returns URL information and reputation.
- `pulsedive-scan`: Scan an indicator (IP/URL/Domain)
- `pulsedive-scan-result`: Retrieve the Result


## QR Code Reader - goqr.me

**Type:** integration  
**Product:** QR Code Reader  

Read QR Code from image file. This integration was integrated and tested with version 1.0.0 of QR Code Reader - goqr.me

**Commands:**

- `goqr-read-qr-code-from-file`: Upload a PNG, GIF or JP(E)G image which is smaller than 1 MiB via the entry_id of the image file.


## qrcodereader

**Type:** script  
**Product:** QR Code Reader  

Decodes an QR Code offline using opencv, returns the value to Context or False

**Inputs:**

- `entry_id`: Image file entry ID


## quarantine-file

**Type:** script  
**Product:** Aggregated Scripts  

This script executes the 'quarantine-file' command on a specified file via the appropriate agent. This script is used to isolate files identified as suspicious

**Inputs:**

- `endpoint_id`: List of endpoint IDs.
- `file_hash`: The hash of the file to quarantine. Supported types are: SHA256, SHA1.
- `file_path`: The path of the file to quarantine.
- `timeout`: The polling timeout in seconds for the quarantine commands. The default is 300.
- `brands`: Brands for which to execute the 'quarantine-file' command. If not specified, all available instances will run.
- `verbose`: Whether to retrieve a human-readable entry for every command. When set to false, human-readable will only summarize the final result.


## Query using Sigma rules

**Type:** playbook  
**Product:** Sigma  

An example playbook on how to query Sigma rules from within TIM and query a SIEM/EDR

**Inputs:**

- `Query`: 


## Query.AI

**Type:** integration  
**Product:** QueryAI  
**Commands:**

- `queryai-run-query`: Returns response for the query being run on Query.AI.


## Quest KACE Systems Management Appliance (Beta)

**Type:** integration  
**Product:** Quest Kace  

This is the Quest KACE integration. This integration was integrated and tested with version v10.0.290 of QuestKace

**Commands:**

- `kace-machines-list`: Returns a list of all machines in system.
- `kace-assets-list`: Returns a list of all assets in Quest KACE.
- `kace-queues-list`: Returns a list of all queues in Quest KACE.
- `kace-tickets-list`: Returns a list of all tickets in Quest KACE.
- `kace-ticket-create`: Creates a new ticket to the system.
- `kace-ticket-update`: Updates a ticket in the system.
- `kace-ticket-delete`: Deletes the specified ticket.


## QutteraWebsiteMalwareScanner

**Type:** integration  
**Product:** Quttera Website Malware Scanner  

Quttera Website Malware Scanner This integration was integrated and tested with version v3 of QutteraWebsiteMalwareScanner

**Commands:**

- `quttera-scan-start`: Start to scan a given domain
- `quttera-rescan-status`: Retrieve status of submitted domain
- `quttera-scan-report`: Retrieve report of submitted domain
- `quttera-report-malware`: Retrieve url blacklist and reputation
- `quttera-status-blacklist`: Retrieve domain blacklist and reputation


## RaDark

**Type:** integration  
**Product:** KELA RaDark  

This integration enables you to fetch incidents and manage your RaDark monitor from the platform. This integration was integrated and tested with version 2 of RaDark

**Commands:**

- `radark-incident-get-items`: Fetch all items for an incident by the given incident ID.
- `radark-email-enrich`: Search a specific email address to get all exposed leaked credentials collected by RaDark.
- `radark-item-handle`: Mark item as handled on RaDark.


## RankRemediationOwners

**Type:** script  
**Product:** Cortex Exposure Management  

This script determines the most likely remediation owners from those surfaced by other enrichments

**Inputs:**

- `owners`: List of potential remediation owners.
- `system_ids`: System IDs or names associated with the compute instance.
- `ownerrelatedfield`: The alert or issue field for the remediation owners.
- `tenantcommand`: For alerts (False), use !setAlert, for issues (True), use !setIssue.


## RankServiceOwners

**Type:** script  
**Product:** Cortex Attack Surface Management  

Recommend most likely service owners from those surfaced by Cortex ASM Enrichment

**Inputs:**

- `owners`: List of potential service owners
- `asmsystemids`: System IDs or names associated with the compute instance
- `owners`: List of potential service owners.
- `ownerrelatedfield`: The field of the alert or issue that owners should be stored.
- `tenantcommand`: False will use !setAlert, True will use !setIssue.


## Rasterize

**Type:** integration  
**Product:** Rasterize  

Converts URLs, PDF files, and emails to an image file or PDF file

**Commands:**

- `rasterize`: Converts the contents of a URL to an image file or a PDF file.
- `rasterize-email`: Converts the body of an email to an image file or a PDF file.
- `rasterize-image`: Converts an image file to a PDF file.
- `rasterize-pdf`: Converts a PDF file to an image file.
- `rasterize-html`: Converts an html file to a PDF or PNG file.


## RasterizeImageOriginal

**Type:** script  
**Product:** Suspicious Domain Hunting  

## RasterizeImageSuspicious

**Type:** script  
**Product:** Suspicious Domain Hunting  

## RCSScan

**Type:** script  
**Product:** Cortex Attack Surface Management  

This script starts an RCS scan and sets the scan ID in context

**Inputs:**

- `service_id`: This is the ASM Service ID.
- `attack_surface_rule_id`: This is the ASM attack surface rule ID.
- `alert_internal_id`: This is the ASM alert ID.


## RDAP

**Type:** integration  
**Product:** RDAP  

## Reco

**Type:** integration  
**Product:** Reco  

Reco is the leader in SaaS & AI Security — securing AI sprawl across SaaS apps and agents. This integration connects Reco's SaaS & AI Security platform to the platform, enabling real-time threat response, posture management, AI governance, and identity risk workflows. This integration was integrated and tested with Reco External API v1

**Commands:**

- `reco-add-comment-to-alert`: Add a comment to an alert in Reco.
- `reco-update-incident-timeline`: Add a comment to an incident timeline in Reco.
- `reco-resolve-visibility-event`: Resolve an event in a Reco Finding.
- `reco-get-risky-users`: List all accounts flagged as risky (auto-paginates all results).
- `reco-add-risky-user-label`: Tag a user as risky in Reco.
- `reco-add-leaving-org-user-label`: Tag a user as a departing employee in Reco.
- `reco-get-assets-user-has-access-to`: List files a user has access to.
- `reco-get-sensitive-assets-by-name`: Find sensitive assets by name.
- `reco-get-sensitive-assets-by-id`: Find sensitive assets by ID.
- `reco-get-assets-by-id`: Find any asset by ID.
- `reco-get-link-to-user-overview-page`: Generate a deep link to the Reco UI overview page for an entity.
- `reco-get-3rd-parties-accessible-to-data-list`: List third-party domains that have access to sensitive data.
- `reco-get-sensitive-assets-with-public-link`: List sensitive assets exposed via a public link.
- `reco-get-files-shared-with-3rd-parties`: List files shared with a specific third-party domain.
- `reco-change-alert-status`: Update the status of a Reco alert.


## Reco - Reduce Risk - Google Publicly Exposed Files

**Type:** playbook  
**Product:** Reco  

Reco Google Drive - Reduce Publicly Exposed Sensitive Files Risk

**Inputs:**

- `admin_email_address`: Email address of the admin in google to get shared drives


## Reco Build String Message

**Type:** playbook  
**Product:** Reco  

Reco Build String Message

**Inputs:**

- `Reco`: Finding Json Object from Reco


## Reco Google Drive Automation

**Type:** playbook  
**Product:** Reco  

Reco Google Drive Automation

**Inputs:**

- `Reco`: Finding Json Object from Reco


## Reco-Google-Drive-Revoke-Permissions

**Type:** playbook  
**Product:** Reco  

Reco Google Drive Revoke Permissions

**Inputs:**

- `Reco`: Finding Json Object from Reco


## redactindicator

**Type:** script  
**Product:** Community Common Scripts  
**Inputs:**

- `indicator`: 
- `searchkey`: 


## Redmine

**Type:** integration  
**Product:** Redmine  

A project management and issue tracking system that provides a web-based platform for managing projects, tracking tasks, and handling various types of project-related activities. This integration was integrated and tested with version 5.1.2 of Redmine

**Commands:**

- `redmine-issue-create`: 
- `redmine-issue-list`: Display a list of issues
- `redmine-issue-update`: Update an existing issue. When attaching a file to an issue, include the entry ID in the request as file_entry_id=entry ID. To create a custom field, navigate t
- `redmine-issue-get`: Show an issue by id
- `redmine-issue-delete`: Delete an issue by its ID
- `redmine-issue-watcher-add`: Add a watcher to the specified issue
- `redmine-issue-watcher-remove`: Remove a watcher of an issue
- `redmine-project-list`: Retrieve a list of all projects, including both public and private ones that the user has access to.
- `redmine-custom-field-list`: Retrieve a list of all custom fields.
- `redmine-user-id-list`: 
- `redmine-priority-id-list`: Returns a list of priorities (priority_name to priority_id).
- `redmine-status-id-list`: Returns a list of statuses (status_name to status_id).
- `redmine-tracker-id-list`: Returns a list of trackers (tracker_name to tracker_id).


## RegexExpand

**Type:** script  
**Product:** Filters And Transformers  

Extract the strings matched to the patterns by doing backslash substitution on the template string. This transformer allow to specify multiple regex patterns and multiple match targets, and those can be given in the input value and the argument parameters

**Inputs:**

- `value`: List of regex or text for the pattern match.
- `regex`: A regex pattern to search (in Python).
- `text`: A match target text.
- `template`: The template text that will be returned for the output by doing backslash substitution to the patterns matched.
- `template_type`: The data type of the template.
- `value_takes`: Which type of value takes from the value argument, 'text' (match target) or 'regex'.
- `flags`: The comma separated flags for pattern matching in regex. "dotall" (s), "multiline" (m), "ignorecase" (i) and "unicode" (u) are supported.
- `search_limit`: The maximum limit for scanning patterns. (0 means unlimited)


## RegexExtractAll

**Type:** script  
**Product:** Filters And Transformers  

Extraction of all matches from a specified regular expression pattern from a provided string. Returns an array of results. This differs from RegexGroups in several ways

**Inputs:**

- `value`: Text to match against, e.g., The quick brown fox.
- `regex`: Regex pattern to search (in Python), e.g., (The)\s(quick).*(fox).
- `multi_line`: Process value in multiline mode. See more information on re.MULTILINE, see https://docs.python.org/3/library/re.html.
- `ignore_case`: Whether character matching will be case-insensitive. Default is "false".
- `period_matches_newline`: Whether to make the '.' character also match a new line. Default is "false".
- `error_if_no_match`: Only set to 'true' if used in a playbook task and you want that failure will return an error.
- `unpack_matches`: Whether to unpack the tuple values of results. Default is "false".


## RegexReplace

**Type:** script  
**Product:** Filters And Transformers  

Format patterns matched with regex. If the regex does not match any pattern, the original value is returned. Example 1: value: user=john regex: user=(.*) output_format: name=\1 -> output value: name=john Example 2: value: xxx=yyy regex: user=(.*) output_format: name=\1 -> output value: xxx=yyy

**Inputs:**

- `value`: Text to match against
- `regex`: Regex pattern to search
- `output_format`: Template string to format patterns matched with regex
- `ignore_case`: Whether character matching will be case-insensitive. Default is "false".
- `multi_line`: Process value in multiline mode. See more information on re.MULTILINE, see https://docs.python.org/3/library/re.html.
- `period_matches_newline`: Whether to make the '.' character also match a new line. Default is "false".
- `action_dt`: The last action for each matched value to transform


## RelayShield

**Type:** integration  
**Product:** RelayShield  

RelayShield real-time identity-compromise and agent-security threat intelligence. This integration implements the generic domain, ip, and email reputation commands, which are automatically invoked by any existing enrichment playbook that calls generic reputation commands, with no playbook changes needed. It adds three RelayShield-specific commands for MCP server registry risk, certificate expiry, and supply-chain vendor risk. This integration was integrated and tested with version 1.0 of the RelayShield API

**Commands:**

- `domain`: Check a domain for phishing-lookalike/typosquat risk, presence in RelayShield's criminal IOC corpus, and set a DBotScore.
- `ip`: Check an IP address for reputation, malicious/suspicious votes, and set a DBotScore.
- `email`: Check an email address for breach exposure and active stolen-session risk, and set a DBotScore.
- `relayshield-mcp-registry-risk`: Assess an MCP server URL or package name for typosquat/supply-chain/registry risk before an agent connects to it.
- `relayshield-cert-expiry`: Check a domain's TLS certificate expiry risk.
- `relayshield-supply-chain`: Check up to 10 vendor domains (or emails) for combined breach/infostealer risk.


## RemediationPathRuleEvaluation

**Type:** script  
**Product:** Cortex Attack Surface Management  

For a given alert and remediation path rules that are defined for that alert's attack surface rule, this script takes each remediation path rule and looks at the rule criteria to see if the rule matches for the given alert. If multiple rules match, it will return the most recently created rule. This assumes that the rules passed in are filtered to correlate with the alert's attack surface rule

**Inputs:**

- `severity`: Alert's Severity.
- `ip`: Alert's Remote IP.
- `development_environment`: Is this in a development environment?
- `cloud_managed`: Is this cloud managed?
- `service_owner_identified`: Has a service owner been identified?
- `tags`: Includes Cloud and Xpanse tags
- `providers`: Externally Detected Providers
- `remediation_path_rules`: List of remediation path rules for the alert's attack surface rule.


## RemoteExec

**Type:** script  
**Product:** Common Scripts  

Executes a command on a remote machine (without installing a D2 agent)

**Inputs:**

- `system`: The name of system on which to run the command.
- `cmd`: The command to run.


## Remove Employees from Departing Employee Watchlist

**Type:** playbook  
**Product:** Code42  

Loops through Departing Employee watchlist entries from Code42 Incydr and removes employees based on specified criteria

**Inputs:**

- `incydr_username`: The username (in email format) provided by Code42 Incydr.
- `look_back`: Number of days to compare the departure date against and check for post-departure activity (e.g. "30", "7", etc.). Default is 30.


## ReplaceMatchGroup

**Type:** script  
**Product:** Common Scripts  

Returns a string with all matches of a regex pattern groups replaced by a replacement

**Inputs:**

- `value`: An array of email addresses to be filtered by domain.
- `regex`: A regex pattern who's groups to be replaced by the replaceWith argument.
- `replace_with`: The replacement string.


## RepopulateFiles

**Type:** script  
**Product:** Common Scripts  

After running DeleteContext, this script can repopulate all the file entries in the ${File} context key


## Resecurity Monitoring

**Type:** integration  
**Product:** Resecurity  

This package allows retrieving asset monitoring results from monitoring tasks that can be configured in Resecurity® CTI and Resecurity® DRM platforms. This integration was integrated and tested with version 1.01 of ResecurityMonitoring

**Commands:**

- `resecurity-get-task-monitor-results-data-breaches`: Retrieve monitoring results from a specific monitor task


## ResolveGemAlert

**Type:** script  
**Product:** Gem  

Post Processing Script that will close linked Incidents when the Incident is closed. Will set the same close code as the parent, and add closing notes from the parent


## ResolveShortenedURL

**Type:** script  
**Product:** Common Scripts  

This script resolves the original URL from a given shortened URL and places the resolved URL in the playbook context and output. Disclaimer

**Inputs:**

- `url`: The URL to resolve.
- `redirect_limit`: A maximum number of recursions to run in case of nested shortened-URLs. Use 0 for unlimited (not recommended).
- `insecure`: Trust any certificate (not secure).


## RestartFailedTasks

**Type:** script  
**Product:** Integrations & Incidents Health Check  

Use this Script to re-run failed tasks. Run in the same incident after running GetFailedTasks for restarting all of the failed tasks or some of them

**Inputs:**

- `playbook_exclusion`: Comma Separated list of failed tasks to exclude from restart based on playbook string match
- `sleep_time`: Sleep between restarting batch task (seconds)
- `incident_limit`: Limit of number of incidents to restart tasks on
- `group_size`: Integer of how many tasks you want to be restarted at a time (grouping) before a sleep period (as to not overwhelm the system)


## Retrieve Alerts For IOCs - Dataminr Pulse

**Type:** playbook  
**Product:** Dataminr Pulse  

This playbook is used to fetch alerts from Dataminr Pulse, which will be based on the given input text. First, it will extract indicators from the input text, then it will use extracted indicators to retrieve alerts from Dataminr Pulse. After that, it will store related alerts in the context

**Inputs:**

- `text`: Text to enrich (default will be entire incident context).
- `num`: The number of alerts to retrieve.
- `use_configured_watchlist_names`: A Boolean indicating that it should use configured watchlist names. Provide "yes " or "no" as value. Default will be "yes".


## Retrieve Asset Details - Lansweeper

**Type:** playbook  
**Product:** Lansweeper  

Get contextual information of asset based on IP/MAC from Lansweeper


## Retrieve Related Alerts - Dataminr Pulse

**Type:** playbook  
**Product:** Dataminr Pulse  

This playbook is used to fetch related alerts for Dataminr Pulse. The information required to fetch related alerts will be used from the incident s alert ID for which the playbook is going to run. After that, it will store them in the context

**Inputs:**

- `include_related_alerts`: Boolean value indicating whether to include related alerts. If set to "true", it includes related alerts; otherwise, it does not.


## RetrievePlaybookDependencies

**Type:** script  
**Product:** Community Common Scripts  

Retrieves all Playbook (and Sub-Playbook) names, Integrations, Automation Scripts, Commands and Lists for a provided Playbook name

**Inputs:**

- `playbook_name`: Name of Playbook


## ReverseList

**Type:** script  
**Product:** Filters And Transformers  

Reverses a list. For example, ["Mars", "Jupiter", "Saturn"] => ["Saturn", "Jupiter", "Mars"]. This is an example for an entire-list transformer. It operates the argument as a list (note the entirelist tag)

**Inputs:**

- `value`: The list to reverse.


## ReversingLabs A1000 v2

**Type:** integration  
**Product:** ReversingLabs A1000  

ReversingLabs A1000 advanced Malware Analysis Platform

**Commands:**

- `reversinglabs-a1000-get-results`: Retrieve sample analysis results


## ReversingLabs TitaniumScale

**Type:** integration  
**Product:** ReversingLabs TitaniumScale  
**Commands:**

- `reversinglabs-titaniumscale-upload-sample-and-get-results`: Upload sample to TitaniumScale and retrieve analysis report.


## RiskSense

**Type:** integration  
**Product:** RiskSense  
**Commands:**

- `risksense-get-hosts`: Gets details of the supplied host. The host details can be searched based on input parameters like fieldname (Host Name, IP Address, Criticality, etc), operator
- `risksense-get-host-detail`: Gets in-depth details of a single host. This command accepts either hostname or host ID as an argument.
- `risksense-get-unique-cves`: Looks up vulnerability details for the supplied host finding with its base score.
- `risksense-get-unique-open-findings`: Finds unique open host findings.The open findings can be searched based on input parameters like fieldname (Severity, Title, Source etc), operator (EXACT, IN, L
- `risksense-get-host-findings`: A detailed host finding view with the severity level. Displays vulnerability information like CVE, Threats associated with current findings and origin of findin
- `risksense-get-apps`: Looks up the application details. The application details can be searched based on input parameters like fieldname (Name, Network, Address), operator (EXACT, IN
- `risksense-get-host-finding-detail`: Gets in-depth details of a single host finding. The command accepts the host finding ID as an argument.
- `risksense-get-app-detail`: Gets in-depth details of a single application. The command accepts an application ID as an argument.
- `risksense-apply-tag`: Apply the new or existing tag to the asset, creates a new tag if it does not exist in RiskSense.


## Roksit DNS Security (DNSSense)

**Type:** integration  
**Product:** Roksit DNS Security  

This integration provides adding selected domains to the Roksit Secure DNS's Blacklisted Domain List through API . This integration was integrated and tested with version 1.0.0 of Roksit DNS Security (DNSSense)

**Commands:**

- `Roksit-add-to-blacklist`: This command adds a given domain to tha Roksit blacklist.


## RSA Archer v2

**Type:** integration  
**Product:** RSA Archer  

The RSA Archer GRC platform provides a common foundation for managing policies, controls, risks, assessments and deficiencies across lines of business

**Commands:**

- `archer-search-applications`: Gets application details or list of all applications.
- `archer-get-application-fields`: Gets all application fields by application ID.
- `archer-get-field`: Returns a mapping from list value name to list value ID.
- `archer-get-mapping-by-level`: Returns a mapping of fields by level ID.
- `archer-get-record`: Gets information about a content record in the given application.
- `archer-create-record`: Creates a new content record in the given application.
- `archer-delete-record`: Deletes an existing content record in the given application.
- `archer-update-record`: Updates an existing content record in the given application. Note: When updating a record, make sure the values are sent through the fieldsToValues argument pro
- `archer-execute-statistic-search-by-report`: Performs statistic search by report GUID.
- `archer-get-reports`: Gets all reports from Archer.
- `archer-get-search-options-by-guid`: Returns search criteria by report GUID.
- `archer-reset-cache`: Resets Archer's integration cache. This cache is maintained in platform based on previous search results and must be cleared when field mappings no longer make 
- `archer-get-valuelist`: Returns a list of values for a specified field, for example, fieldID=16114. This command is applicable only to value list fields (type 4) and will attempt to fe
- `archer-upload-file`: Uploads a file to Archer. You can associate the file to a record by providing all of the following arguments:
- `archer-get-file`: Downloads a file from Archer to the platform.


## RSA NetWitness Security Analytics

**Type:** integration  
**Product:** RSA NetWitness Security Analytics  

RSA Security Analytics is a distributed and modular system that enables highly flexible deployment architectures that scale with the needs of the organization. Security Analytics allows administrators to collect two types of data from the network infrastructure, packet data and log data. This integraitons should work with RSA Netwitness older than v11. For versions v11 and above use the integration RSA NetWitness v11.1

**Commands:**

- `nw-login`: Logins to the system and returns valid sessionId
- `fetch-incidents`: Simulates fetching incidents. Returns array of incidents from NetWitness.
- `netwitness-im-list-incidents`: Fetches incidents by filter
- `netwitness-im-login`: Logins to the system and returns valid sessionId
- `netwitness-im-get-components`: Returns all the components in the system
- `netwitness-im-get-events`: Returns all the events in defined time range
- `netwitness-im-get-available-assignees`: Returns the available users to be assigned to incidents
- `netwitness-im-create-incident`: Creating new incident
- `netwitness-im-add-events-to-incident`: This command will add new events to existing incident
- `netwitness-im-update-incident`: Updates incident
- `netwitness-im-get-alerts`: Return all the alerts filtered by filter.
- `netwitness-im-get-alert-details`: Return single alert by id
- `netwitness-im-get-event-details`: Returns two entries. One is event details json and the second is
- `netwitness-im-get-incident-details`: Returns incident json by id
- `netwitness-im-get-alert-original`: Returns the original events which this alert contains


## RSA_DisplayMetasEvents

**Type:** script  
**Product:** NetWitness  

Use this script to display meta events inside the layout


## RSA_GetRawLog

**Type:** script  
**Product:** NetWitness  

Use this script to get RAW log. Each RSA NetWitness log contains the eventsource meta that contains an IP address that can be requested using RSA NetWitness Packets and Logs. This log is after set in the field rsarawlogslist


## RSANetWitness v11.5

**Type:** integration  
**Product:** NetWitness  

RSA NetWitness Platform provides systems Logs, Network, and endpoint visibility for real-time collection, detection, and automated response with the platform Enterprise platform. This integration was integrated and tested with version 12.2 of RSANetWitness. The integration supports version 11.5 and higher

**Commands:**

- `rsa-nw-list-incidents`: Retrieves a single incident by ID or multiple incidents by the date and time they were created using the start time ('since') or end time ('until'). You can lim
- `rsa-nw-update-incident`: Updates incident status and assignee.
- `rsa-nw-remove-incident`: Remove a single incident using the incident’s unique identifier.
- `rsa-nw-incident-add-journal-entry`: Add a journal entry to an existing incident.
- `rsa-nw-incident-list-alerts`: Retrieves all the alerts that are associated with an incident based on the incident ID. You can limit the results using the limit argument.
- `rsa-nw-services-list`: Retrieves a list of all services, or filter by name.
- `rsa-nw-hosts-list`: Lists all host information from a specific endpoint server. Filter the results using the supplied arguments (can be a list) or use the 'filter' argument. You ca
- `endpoint`: Retrieves host information for a specific endpoint. To use this command, service ID must be set in the integration configuration.
- `rsa-nw-snapshots-list-for-host`: Retrieve a list os snapshot IDs for a given host.
- `rsa-nw-snapshot-details-get`: Provides snapshot details of the given host for the specified snapshot time. It is recommended to use categories to filter the results since this command return
- `rsa-nw-files-list`: Lists all related file information from a specific endpoint server. You can limit the results using the limit argument or the page size argument.
- `rsa-nw-scan-request`: Starts a scan for the host with the specified agent ID. Each scan produces a snapshot, the full details can be seen using the 'rsa-nw-snapshot-details-get' comm
- `rsa-nw-scan-stop-request`: Stop a scan for the host with the specified agent ID.
- `rsa-nw-host-alerts-list`: Gets all alerts triggered for a given host.
- `rsa-nw-file-alerts-list`: Gets all alerts triggered for a given file.


## RSSWidget

**Type:** script  
**Product:** Common Widgets  

There are no outputs for this script. !RSSWidget url= Article Title #1 Posted June 25, 2021 3:35 PM by Timor Article #1 Summary Article Title #2 Posted June 18, 2021 3:35 PM by Shai Article #2 Summary


## RSSWidget_LC

**Type:** script  
**Product:** platform Summary Dashboard  

Script Widget - RSS Feed

**Inputs:**

- `limit`: Maximum number of entries to return.


## Rundeck

**Type:** integration  
**Product:** Rundeck  

Rundeck is a runbook automation for incident management, business continuity, and self-service operations. The integration enables you to install software on a list of machines or perform a task periodically. Can be used when there is a new attack and you want to perform an update of the software to block the attack. This integration was integrated and tested with version 24 of Rundeck

**Commands:**

- `rundeck-projects-list`: Gets all existing projects on the server.
- `rundeck-jobs-list`: Gets a list of all the jobs that exist in a project.
- `rundeck-job-execute`: Executes a new job.
- `rundeck-job-retry`: Retry running a failed execution
- `rundeck-job-executions-query`: Gets all executions based on the job or execution details.
- `rundeck-job-execution-output`: Gets the metadata associated with the workflow step state.
- `rundeck-job-execution-abort`: Aborts an active execution.
- `rundeck-adhoc-command-run`: Executes shell commands in nodes.
- `rundeck-adhoc-script-run`: Runs a script from file.
- `rundeck-adhoc-script-run-from-url`: Runs a script downloaded from a URL.
- `rundeck-webhooks-list`: Gets a list of all existing webhooks
- `rundeck-webhook-event-send`: Send webhook event


## Rundeck-job-execute-Generic

**Type:** playbook  
**Product:** Rundeck  

This playbook executes a job and exits when it successfully finishes

**Inputs:**

- `job_id`: ID of the job to execute.


## RunZero

**Type:** integration  
**Product:** RunZero  

RunZero is a network discovery and asset inventory platform that uncovers every network in use and identifies every device connected – without credentials. Scan your network and build your asset inventory in minutes. This integration was integrated and tested with version 3.3.0 of RunZero

**Commands:**

- `runzero-asset-search`: Get assets.
- `runzero-asset-delete`: Bulk delete assets.
- `runzero-service-search`: Get services.
- `runzero-service-delete`: Delete a service.
- `runzero-comment-add`: Add a comment or override an existing asset comment.
- `runzero-tag-add`: Add tag or tags to the asset.
- `runzero-quota-get`: Get information about the API key used. Type, Limit, usage etc.
- `runzero-tag-delete`: Delete tags for specific asset.
- `runzero-wireless-lan-search`: Get all wireless LANs.
- `runzero-wireless-lan-delete`: Remove a wireless LAN.


## SafeBreach

**Type:** integration  
**Product:** SafeBreach - Breach and Attack Simulation platform  

For enterprises using SafeBreach and platform, integrating this package streamlines operations by allowing you to operate SafeBreach through platform, making SafeBreach an integral part of the enterprise workflows. This integration includes commands for managing tests, insight indicators, simulators and deployments, users, API keys, integration issues, and more. This integration was integrated and tested with version 2024Q1.4 of Safebreach

**Commands:**

- `safebreach-approve-simulator`: This command approves the simulator with the specified simulator_id.
- `safebreach-generate-api-key`: This command creates an API key with the name and optionally the description provided. The API key created will be shown on the Settings > API Keys page of Safe
- `safebreach-create-deployment`: This command creates a deployment, grouping the list of simulators provided with a name and optionally a description.
- `safebreach-create-user`: This command creates a user, including credentials and permissions.
- `safebreach-delete-api-key`: This command deletes the API key with the name as specified in SafeBreach Management. It is not case sensitive.
- `safebreach-delete-deployment`: This command deletes a deployment with the deployment_id (retrieved using the get-all-deployments command).
- `safebreach-clear-integration-issues`: This command deletes connector-related errors and warnings for the specified connector_id (retrieved using the get-all-integration-issues command).
- `safebreach-delete-scheduled-scenarios`: This command deletes the scheduled scenario with the specified schedule_id.
- `safebreach-delete-simulator`: The provided command facilitates the deletion of a simulator identified by its unique ID.To obtain the respective simulator ID, execute the "safebreach-get-all-
- `safebreach-delete-test-with-id`: This command deletes tests with given test ID.
- `safebreach-delete-user`: This command deletes a user with given data.
- `safebreach-get-integration-issues`: This command gives all integrations related issues and warning. this will show the integrations error and warnings which are generally displayed in installed in
- `safebreach-get-running-simulations`: This command gets simulations which are in running or queued state.
- `safebreach-get-running-tests`: This command gets tests which are in running state.
- `safebreach-get-available-simulator-details`: This command to get all available simulators. if details is set to true then it retrieves simulator details like name, hostname, internal and external ips, type


## SafeNet Trusted Access - Add to Unusual Activity Group

**Type:** playbook  
**Product:** Thales SafeNet Trusted Access  

This playbook adds the user to a group that was created to identify unusual activity. SafeNet Trusted Access policies can be configured to take this into account and provide stronger protection when handling access events from users who are members of the group. The user is added to this group for a configurable period of time

**Inputs:**

- `UserName`: Username of the user.
- `UnusualActivityGroup`: Name of the Unusual Activity Group.
- `InstanceName`: Name of the SafeNet Trusted Access integration instance.
- `Time`: Amount of time for which the user will remain in the Unusual Activity Group.


## SafeNet Trusted Access - Terminate User SSO Sessions

**Type:** playbook  
**Product:** Thales SafeNet Trusted Access  

This playbook terminates user SSO sessions so that upon the next login attempt following the unlocking of the account, authentication is required

**Inputs:**

- `UserName`: Username of the user.
- `InstanceName`: Name of the SafeNet Trusted Access integration instance.


## Safewalk Management

**Type:** integration  
**Product:** Altipeak  

Safewalk server integration This integration was integrated and tested with version 3 of SafewalkManagement

**Commands:**

- `safewalk-get-transactionlog`: Display transaction log.
- `safewalk-get-users`: Search local users.
- `safewalk-get-ldap-users`: Search LDAP users
- `safewalk-get-ldaps`: Get LDAP configuration.
- `safewalk-get-user-personalinformation`: Get users personal information.
- `safewalk-set-user-personalinformation`: Set user personal information.
- `safewalk-get-user-accessattempts`: Get user access attempts
- `safewalk-delete-user-accessattempts`: Delete user access attempts
- `safewalk-get-user-tokens`: Get user tokens
- `safewalk-delete-user-token`: Delete user token.
- `safewalk-send-user-virtualtoken`: Send user virtual token.
- `safewalk-get-user-settings`: Get user settings.
- `safewalk-get-user-group`: Get user group.
- `safewalk-add-user-group`: Add user group.
- `safewalk-remove-user-group`: Remove user group.


## Safewalk Reports

**Type:** integration  
**Product:** Altipeak  

Safewalk server integration This integration was integrated and tested with version 3 of SafewalkReports

**Commands:**

- `safewalk-get-associated-users`: safewalk-get-associated-users
- `safewalk-get-authentication-methods-distribution`: safewalk-get-authentication-methods-distribution
- `safewalk-get-authentication-rate-per-device`: safewalk-get-authentication-rate-per-device
- `safewalk-get-least-active-users`: safewalk-get-least-active-users
- `safewalk-get-licenses-inventory`: safewalk-get-licenses-inventory
- `safewalk-get-licenses-usage`: safewalk-get-licenses-usage
- `safewalk-get-most-active-users`: safewalk-get-most-active-users
- `safewalk-get-physical-tokens-inventory`: safewalk-get-physical-tokens-inventory
- `safewalk-get-registered-devices-distribution`: safewalk-get-registered-devices-distribution
- `safewalk-get-registration`: safewalk-get-registration
- `safewalk-get-users-associations-indicators`: safewalk-get-users-associations-indicators


## Salesforce Fusion IAM

**Type:** integration  
**Product:** Salesforce Fusion  

Integrate with Salesforce Fusion Identity Access Management service to execute CRUD (create, read, update, and delete) operations for employee lifecycle processes. For more information, refer to the Identity Lifecycle Management article

**Commands:**

- `iam-create-user`: Creates a user.
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Disable an active user.


## Salesforce IAM

**Type:** integration  
**Product:** Salesforce  

Integrate with Salesforce's services to perform Identity Lifecycle Management operations. For more information, please refer to the Identity Lifecycle Management article

**Commands:**

- `iam-create-user`: Creates a user with specific settings and permissions in Salesforce, according to the configuration of the Salesforce integration and mapper - as explained in t
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Disable an active user.
- `get-mapping-fields`: Retrieves a User Profile schema which holds all of the user fields within the application. Used for outgoing-mapping through the Get Schema option.


## Salesforce v2

**Type:** integration  
**Product:** SalesforceV2  

CRM Services

**Commands:**

- `salesforce-search`: Search records that contain values with the defined pattern.
- `salesforce-query`: Queries Salesforce in SOQL format.
- `salesforce-get-object`: Returns an object by its path.
- `salesforce-update-object`: Updates object fields.
- `salesforce-create-object`: Creates a new object.
- `salesforce-push-comment`: Adds a comment to Chatter.
- `salesforce-get-case`: Returns information on a case. All arguments are optional, but you must specify at least one argument for the command to execute successfully.
- `salesforce-create-case`: Creates a new case.
- `salesforce-update-case`: Updates case fields.
- `salesforce-get-cases`: Returns all cases.
- `salesforce-close-case`: Close a case
- `salesforce-push-comment-threads`: Add the comment to the Chatter thread. Use this command only after salesforce-push-comment.
- `salesforce-delete-case`: Deletes a case.
- `salesforce-get-casecomment`: Returns a comment through the case number.
- `salesforce-post-casecomment`: The post comment through the case number.


## SalesforceAskUser

**Type:** script  
**Product:** Salesforce  

Asks a user a question via Salesforce Chatter and process the reply directly into the investigation

**Inputs:**

- `persistent`: Indicates whether to use a one-time entitlement or a persistent one.
- `replyEntriesTag`: The tags to add on comment reply entries.
- `retries`: The number of times to try and create an entitlement when there is a failure.
- `task`: The task that should be closed with the reply. If none, then no playbook tasks will be closed.
- `option1`: The first option for a user reply. Options cannot contain whitespaces.
- `option2`: The second option for the user reply. Options cannot contain whitespaces.
- `oid`: The object ID of the subject.
- `additionalOptions`: A comma delimited list of additional options (in cases where more than 2 options are needed). Options cannot contain whitespaces.


## SanePdfReports

**Type:** script  
**Product:** Base  

Internal script used for generating PDF reports

**Inputs:**

- `sane_pdf_report_base64`: sane report json file contents base64
- `orientation`: orientation of the report
- `paperSize`: the paper size of the report
- `resourceTimeout`: timeout for the report generation execution time
- `reportType`: type of report generated
- `customerLogo`: customer's logo
- `platformLogo`: demito's logo
- `disableHeaders`: flag to use headers in the report or not


## SAP - IAM

**Type:** integration  
**Product:** SAP-IAM  

Integrate with SAP's services to execute get and disable operations for employee lifecycle processes

**Commands:**

- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Disable an active user.


## SAP BTP (Business Technology Platform)

**Type:** integration  
**Product:** SAP BTP (Business Technology Platform)  
**Commands:**

- `sap-btp-get-events`: Retrieve audit log events from SAP BTP manually. This command is used for developing/debugging and is to be used with caution, as it can create events, leading 


## Schedule Task and Poll

**Type:** playbook  
**Product:** Schedule Task and Poll  

This playbook will schedule a specified command and monitor for completion by looking for output in context. Make the playbook context shared globally if you have a command that returns to Context automatically, and you have a specific key to monitor. The key monitored must be a single field value and not an array

**Inputs:**

- `Command`: Command to Schedule
- `Cron`: In the format* * * * *Min Hour Day(Month) Month Day(Week)i.e.1 9 * * *9:01 AM- (server time) run !GetTime to see server time
- `Number of Times to Run`: How many times to run before stopping (based on cron as well)
- `OutputContextValue`: Provide the Key of the value that will be output from the command to poll for completion. If specifying a context value of a command that al
- `FrequencyToPoll`: Frequency to run polling command to check context (in minutes)
- `RegExVal`: The regex to check the field for. By default the regex contains .+, which matches anything other than None.


## ScheduleCommand

**Type:** script  
**Product:** Common Scripts  

Schedules a command to run inside the War Room at a future time. Can be once or reoccurring

**Inputs:**

- `command`: The command to schedule.
- `cron`: The scheduled time to run. Uses UTC (Coordinated Universal Time).
- `endDate`: When should we end the schedule. Will be only relevant if times is not provided. Optional. Format is 'Mon, 02 Jan 2006 15:04:05 MST'
- `times`: The number of times to run. Optional.
- `scheduledEntryGuid`: The GUID of the scheduled entry that runs the polling command.


## SCPPullFiles

**Type:** script  
**Product:** Common Scripts  

Pulls a specific file (given by path) from each using SCP from a list of devices

**Inputs:**

- `systems2files`: The JSON object mapping remote access instances to filepaths.


## script-JiraChangeTransition

**Type:** script  
**Product:** Atlassian Jira  

This script applies the transition supplied by the user from the Jira Transitions incident field. It gets the new Jira status after applying the transition and updates the the platform


## script-JiraListTransition

**Type:** script  
**Product:** Atlassian Jira  

This script lists all possible transitions for a given Jira issue


## Search all mailboxes - Gmail with polling

**Type:** playbook  
**Product:** Gmail  

This playbook searches Gmail records for all Google users. It is intended for large companies with over 2500 Google users

**Inputs:**

- `after`: Search for messages sent after a specific date. For example, 2018/05/06
- `before`: Search for messages sent before a specific date. For example, 2018/05/09
- `fields`: Enables partial responses to be retrieved in a comma-separated list. For more information, see https://developers.google.com/gdata/docs/2.0/
- `filename`: Attachments with a certain name or file type. For example, "pdf" or "report.pdf"
- `from`: Specifies the sender. For example, "john"
- `to`: Specifies the receiver. For example, "john"
- `has-attachments`: Whether to search for messages sent with attachments.
- `in`: Messages in any folder, including Spam and Trash. For example, shopping


## Search in mailboxes Gmail (Loop) with polling

**Type:** playbook  
**Product:** Gmail  

This playbook should only run as a sub-playbook for the Search-all-mailboxes - Gmail playbook, it should not run alone

**Inputs:**

- `after`: Search for messages sent after a specific date. For example, 2018/05/06
- `before`: Search for messages sent before a specific date. For example, 2018/05/09
- `fields`: Enables partial responses to be retrieved in a comma-separated list. For more information, see https://developers.google.com/gdata/docs/2.0/
- `filename`: Attachments with a certain name or file type. For example, "pdf" or "report.pdf"
- `from`: Specifies the sender. For example, "john"
- `to`: Specifies the receiver. For example, "john"
- `has-attachments`: Whether to search for messages sent with attachments.
- `in`: Messages in any folder, including Spam and Trash. For example, shopping


## SecneurX Analysis

**Type:** integration  
**Product:** SecneurX Analysis  

Use SecneurX Analysis pack to provide threat analysts and incident response teams with the advanced malware isolation and inspection environment needed to safely execute advanced malware samples, and understand their behavior. You can use the pack's playbooks to detonate both files and URLs. SecneurX Analysis performs both static and dynamic analysis of advanced threats, including zero day and targeted attacks. This integration was integrated and tested with version 1.0.0 of SecneurX Analysis

**Commands:**

- `snx-analysis-get-verdict`: Get verdict summary report of the analyzed sample
- `snx-analysis-get-completed`: Get the list of submitted samples whose status is marked as "Completed"
- `snx-analysis-get-pending`: Get the list of submitted samples that are still in pending state
- `snx-analysis-get-status`: Get the status of all the submitted samples
- `snx-analysis-submit-file`: Submit a file for Analysis
- `snx-analysis-submit-url`: Submit the URL for Analysis
- `snx-analysis-get-report`: Get the detailed report of the analyzed sample.
- `snx-analysis-get-quota`: Get the API Key quota usage details.


## SecurityScorecard

**Type:** integration  
**Product:** SecurityScorecard  

Provides commands to access SecurityScorecard's API. This integration was integrated and tested with the latest version of SecurityScorecard's API as of August 2024

**Commands:**

- `securityscorecard-portfolios-list`: List all Portfolios.
- `securityscorecard-portfolio-list-companies`: Lists all companies in Portfolio.
- `securityscorecard-company-score-get`: Retrieve company overall score.
- `securityscorecard-company-factor-score-get`: Retrieve company factor score.
- `securityscorecard-company-history-score-get`: Retrieve company historical scores.
- `securityscorecard-company-history-factor-score-get`: Retrieve company historical factor scores.
- `securityscorecard-alert-grade-change-create`: Create alert based on grade.
- `securityscorecard-alert-score-threshold-create`: Create alert based threshold met.
- `securityscorecard-alert-delete`: Delete an alert.
- `securityscorecard-alerts-list`: List alerts triggered in the last week.
- `securityscorecard-company-services-get`: Retrieve the service providers of a domain.
- `securityscorecard-company-events-get`: Retrieve a company's historical events.
- `securityscorecard-company-findings-get`: Retrieve an issue_type's historical findings in a scorecard.
- `securityscorecard-issue-metadata`: Retrieve metadata for an issue type, including description and recommendation.
- `securityscorecard-alert-rules-list`: List alert subscriptions for the user.


## SecurityTrails

**Type:** integration  
**Product:** SecurityTrails  

This integration provides API access to the SecurityTrails platform. This integration was integrated and tested with V1 of SecurityTrails

**Commands:**

- `securitytrails-get-subdomains`: Returns child and sibling subdomains for a given hostname.
- `securitytrails-get-tags`: Returns tags for a given hostname
- `securitytrails-get-company-associated-ips`: Returns associated IPs for a company domain. The data is based on whois data with the names matched to the domains.
- `securitytrails-get-dns-history`: Lists out specific historical information about the given hostname parameter. In addition of fetching the historical data for a particular type, the count stati
- `securitytrails-get-ip-neighbors`: Returns the neighbors in any given IP level range and essentially allows you to explore closeby IP addresses. It will divide the range into 16 groups. Example: 
- `securitytrails-statistics-domain`: Domain statistics
- `securitytrails-search-ip`: Search for IP addresses. A maximum of 10000 results can be retrieved.
- `securitytrails-get-ip-whois`: Returns IPs information based on whois information.
- `domain`: Provides data enrichment for domains.
- `securitytrails-sql-get-next`: Retrieves the next page of results returned from a SQL query where the results exceeded the last page.


## Securonix

**Type:** integration  
**Product:** Securonix  
**Commands:**

- `securonix-list-workflows`: Gets a list of all available workflows.
- `securonix-get-default-assignee-for-workflow`: Gets the default assignee for the specified workflow.
- `securonix-list-possible-threat-actions`: Gets a list available threat actions.
- `securonix-list-policies`: Gets a list of all policies.
- `securonix-list-resource-groups`: Gets a list of resource groups.
- `securonix-list-users`: Gets a list of users.
- `securonix-list-activity-data`: Gets a list of activity data for the specified resource group.
- `securonix-list-violation-data`: Gets a list activity data for an account name.
- `securonix-list-incidents`: Gets a list of incidents.
- `securonix-get-incident`: Gets details of the specified incident.
- `securonix-get-incident-status`: Gets the status of the specified incident.
- `securonix-get-incident-workflow`: Gets the workflow of the specified incident.
- `securonix-get-incident-available-actions`: Gets a list of available actions for the specified incident.
- `securonix-perform-action-on-incident`: Performs an action on the specified incident.
- `securonix-add-comment-to-incident`: Adds a comment to the specified incident.


## SecuronixGetViolations

**Type:** script  
**Product:** Securonix  

Gets a list of violations related to a specific threat from the context data and displays it in the layout


## Sekoia XDR

**Type:** integration  
**Product:** SekoiaXDR  

Fetch alerts and events from SEKOIA.IO XDR. To use this integration, please create an API Key with the appropriate permissions. This integration was integrated and tested with version 1.0 of Sekoia XDR

**Commands:**

- `sekoia-xdr-list-alerts`: Command to retrieve a list of Alerts from Sekoia XDR.
- `sekoia-xdr-get-alert`: Command to retrieve a specific alert by uuid or short_id from Sekoia XDR.
- `sekoia-xdr-events-execute-query`: Command to create an event search job on Sekoia XDR, after this execute "sekoia-xdr-status-events-query" to see the status of the query job and "sekoia-xdr-resu
- `sekoia-xdr-events-status-query`: Command to query the status of the search job on Sekoia XDR.
- `sekoia-xdr-events-results-query`: Command to retrieve the events from the search job "sekoia-xdr-execute-events-query" previously done on Sekoia XDR.
- `sekoia-xdr-search-events`: Command to search and retrieve the events from an alert. This is a combination of 3 commands: sekoia-xdr-events-execute-query, sekoia-xdr-events-status-query an
- `sekoia-xdr-update-status-alert`: Command to update the status of a specific Alert by uuid or short_id.
- `sekoia-xdr-post-comment-alert`: Command to post comments to alerts in Sekoia XDR.
- `sekoia-xdr-get-comments`: Command to get all the comments from an alert in Sekoia XDR.
- `sekoia-xdr-get-workflow-alert`: Command to get the possible transitions of status on the alert.
- `sekoia-xdr-get-cases-alert`: Command to retrieve the cases related to an Alert from Sekoia XDR. If a case_id is given, returns the information about it, and if not it will give all cases in
- `sekoia-xdr-get-asset`: Get an asset by its UUID from Sekoia XDR.
- `get-remote-data`: This command gets new information about the incidents in the remote system and updates existing incidents in the platform.
- `get-modified-remote-data`: available from the platform.1.0. This command queries for incidents that were modified since the last update.
- `get-mapping-fields`: This command pulls the remote schema for the different incident types, and their associated incident fields, from the remote system.


## SekoiaXDRAddComment

**Type:** script  
**Product:** SekoiaXDR  

Script to add a comment to an alert in Sekoia, including the name of the person who made the comment

**Inputs:**

- `short_id`: The short ID of the alert.
- `comment`: The comment you want to send to an alert.


## SekoiaXDRChangeStatus

**Type:** script  
**Product:** SekoiaXDR  

This script changes the status of the Sekoia alert

**Inputs:**

- `short_id`: The short ID of the alert.
- `status`: Status to change on the Sekoia alert.
- `comment`: The comment to add to the alert on the status change.


## SekoiaXDRPrintAssets

**Type:** script  
**Product:** SekoiaXDR  

Print all assets by incident


## SekoiaXDRPrintCase

**Type:** script  
**Product:** SekoiaXDR  

Prints case details from the Sekoia alert


## SekoiaXDRPrintComments

**Type:** script  
**Product:** SekoiaXDR  

Prints the comments fetched from the Sekoia alert in a table format


## SendGrid

**Type:** integration  
**Product:** SendGrid  

SendGrid provides a cloud-based service that assists businesses with email delivery. It allows companies to track email opens, unsubscribes, bounces, and spam reports. Our SendGrid pack utilize these SendGrid use cases to help you send and manage your emails

**Commands:**

- `sg-send-email`: Send an email.
- `sg-get-global-email-stats`: Retrieves all of your global email statistics between a given date range.
- `sg-get-category-stats`: Retrieves all of your email statistics for each of your categories.
- `sg-get-all-categories-stats`: Retrieves the total sum of each email statistic for every category over the given date range. By default it returns only 5 categories. Use limit= argument to de
- `sg-list-categories`: Retrieves a list of all of your categories.
- `sg-create-batch-id`: Generates a new batch ID.
- `sg-scheduled-status-change`: Cancel or pause a scheduled send associated with a batch ID.
- `sg-retrieve-all-scheduled-sends`: Retrieves all cancelled and paused scheduled send information.
- `sg-retrieve-scheduled-send`: Retrieves the cancel/paused scheduled send information for a specific batch id.
- `sg-update-scheduled-send`: Update the status of a scheduled send for the given batch id.
- `sg-delete-scheduled-send`: Delete the cancellation/pause of a scheduled send.
- `sg-get-email-activity-list`: Retrieves the email activity list associated with the messages matching your query. If no query provided, it returns a list of most recent emails you've sent. N
- `sg-get-all-lists`: Retrieves all of your recipient lists. If you don't have any lists, an empty array will be returned.
- `sg-get-list-by-id`: Retrieves a single recipient list.
- `sg-create-list`: Creates a new contacts list


## Sepio

**Type:** integration  
**Product:** Sepio  
**Commands:**

- `sepio-query-agents`: Get Agents
- `sepio-query-peripherals`: Get Peripherals
- `sepio-query-switches`: Get Switches
- `sepio-query-switch-ports`: Get Switch Ports
- `sepio-query-system-events`: Get Events
- `sepio-set-agent-mode`: Set Agent Mode
- `sepio-set-peripherals-mode`: Set Agent Peripherals Mode


## Serenety

**Type:** integration  
**Product:** XMCO  

XMCO Serenety

**Commands:**

- `fetch-incidents`: Fetch the Serenety lerts from XMCO LePortail


## Server Message Block (SMB) v2

**Type:** integration  
**Product:** Server Message Block (SMB)  

Files and Directories management with an SMB server. Supports SMB2 and SMB3 protocols

**Commands:**

- `smb-download`: Downloads a file from the server.
- `smb-upload`: Uploads a file to the server.
- `smb-directory-list`: Returns a list containing the names of the entries in the directory given by path.
- `smb-file-remove`: Removes a file from the server.
- `smb-directory-create`: Creates a new directory under the given path.
- `smb-directory-remove`: Removes a directory from the given path.


## ServerLogs

**Type:** script  
**Product:** Common Scripts  

Uses the ssh integration to grab the host server logs This script is supported only on the platform.X)


## ServerLogs_docker

**Type:** script  
**Product:** Common Scripts  

Uses the ssh integration to grab the host server logs This script is supported only on the platform.X)


## Service Desk Plus

**Type:** integration  
**Product:** Manage Engine Service Desk Plus  

IT Service Management

**Commands:**

- `service-desk-plus-requests-list`: View the details of requests. If no parameters are given the details of all requests will be shown.
- `service-desk-plus-request-delete`: Deletes the request with the specified ID. To delete multiple IDs, pass a comma-separated list (string) of the IDs of the requests.
- `service-desk-plus-request-create`: Create new requests
- `service-desk-plus-request-update`: Update the request with the given request id.
- `service-desk-plus-request-assign`: Assigns the request with the given request id to a technician/group
- `service-desk-plus-request-pickup`: Allows the technician to pickup the request with the given request id on his name.
- `service-desk-plus-linked-request-list`: Gets a list with all the linked requests under a request
- `service-desk-plus-request-resolution-add`: Adds a resolution to the given request
- `service-desk-plus-request-resolutions-list`: Gets the resolution to the given request
- `service-desk-plus-generate-refresh-token`: This function generates the refresh token that should be used in the instance configurations
- `service-desk-plus-link-request-modify`: Link or Unlink multiple commands


## Service Desk Plus - Generic Polling

**Type:** playbook  
**Product:** Manage Engine Service Desk Plus  

This playbook uses generic polling to wait until a request is closed

**Inputs:**

- `RequestId`: The id of the Service Desk Plus request
- `Timeout`: Amount of time to poll before declaring a timeout and resuming the playbook (minutes).
- `Interval`: Frequency that the polling command will run (minutes).


## ServiceNow Change Management

**Type:** playbook  
**Product:** Change Management  

If you are using a PAN-OS/Panorama firewall and ServiceNow as a ticketing system this playbook is a perfect match for your change management for firewall process. This playbook is triggered by a fetch from ServiceNow and helps you manage and automate your change management process

**Inputs:**

- `TicketSummary`: Provide a summary for your firewall request.
- `SecurityTeamEmail`: The email of the security team that approves the firewall requests.
- `log_type`: Log type to query. Can be: traffic, threat, wildfire, url or data-filtering.
- `query`: The query string by which to match criteria for the logs. This is similar to the query provided in the web interface under the Monitor tab w
- `addr-src`: Source address.
- `addr-dst`: Destination address.
- `port-dst`: Destination port.
- `TestConfigurations`: By providing YES to this input the requested firewall rule will be tested in your test environment.


## ServiceNow CMDB

**Type:** integration  
**Product:** ServiceNow  

ServiceNow CMDB is a service‑centric foundation that proactively analyzes service‑impacting changes, identifies issues, and eliminates outages

**Commands:**

- `servicenow-cmdb-records-list`: Query records for a CMDB class.
- `servicenow-cmdb-record-get-by-id`: Query attributes and relationship information for a specific record.
- `servicenow-cmdb-record-create`: Create a record with associated relations and attributes.
- `servicenow-cmdb-record-update`: Update a record with the given attributes.
- `servicenow-cmdb-record-add-relations`: Add a new relation to an existing record.
- `servicenow-cmdb-record-delete-relations`: Delete a relation of an existing record.
- `servicenow-cmdb-oauth-login`: This function should be used once before running any command when using OAuth authorization.
- `servicenow-cmdb-oauth-test`: Test the instance configuration when using OAuth authorization.


## ServiceNow CMDB Search

**Type:** playbook  
**Product:** ServiceNow  

Subplaybook for finding CI records in ServiceNow CMDB

**Inputs:**

- `SearchCIClass`: The CMDB CI class to perform the search on (Defaults to cmdb_ci).
- `SearchQueryField`: The CI field used to perform the query (Defaults to ip_address).
- `SearchQueryValue`: The value used to perform the query.
- `BypassAddRecord`: Value to determine if the "add asset to CMDB" branch should be skipped in order to prevent direction to manual task. By default this is set 


## ServiceNow IAM

**Type:** integration  
**Product:** ServiceNow  

Integrate with ServiceNow's services to perform Identity Lifecycle Management operations. This integration was integrated and tested with London version of ServiceNow. For more information, please refer to the Identity Lifecycle Management article

**Commands:**

- `iam-create-user`: Creates a user.
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Disable an active user.


## ServiceNow MCP

**Type:** integration  
**Product:** ServiceNow MCP  

Use this integration to connect securely with a ServiceNow Model Context Protocol (MCP) server and access its tools in real time. This integration was integrated and tested with the latest version of ServiceNow MCP

**Commands:**

- `servicenow-mcp-auth-test`: Test the authentication configuration with the MCP server.
- `servicenow-mcp-generate-login-url`: Generate an authentication login URL.


## ServiceNow v2

**Type:** integration  
**Product:** ServiceNow  

IT service management. Cortex interfaces with ServiceNow to help streamline security-related service management and IT operations. For example, you can use the ServiceNow integration in order to: Please refer to ServiceNow documentation for additional information. We especially recommend the Operators available for filters and queries page. This integration was integrated and tested with the Xanadu version of ServiceNow

**Commands:**

- `servicenow-login`: This function should be used once before running any command when using OAuth authentication.
- `servicenow-test`: Test the instance configuration when using OAuth authorization.
- `servicenow-get-ticket`: Retrieves ticket information by ticket ID.
- `servicenow-create-ticket`: Creates new ServiceNow ticket.
- `servicenow-update-ticket`: Updates the specified ticket.
- `servicenow-delete-ticket`: Deletes a ticket from ServiceNow.
- `servicenow-query-tickets`: Retrieves ticket information according to the supplied query.
- `servicenow-add-link`: Adds a link to the specified ticket.
- `servicenow-add-comment`: Adds a comment to the specified ticket, by ticket ID.
- `servicenow-upload-file`: Uploads a file to the specified ticket.
- `servicenow-delete-file`: Delete an attachment from a ticket.
- `servicenow-get-record`: Retrieves record information, by record ID.
- `servicenow-query-table`: Queries the specified table in ServiceNow.
- `servicenow-create-record`: Creates a new record in the specified ServiceNow table.
- `servicenow-update-record`: Updates a record in the specified ServiceNow table.


## ServiceNowApiModule

**Type:** script  

The ServiceNow API handles the OAuth2 authentication process and API requests. When developing a ServiceNow integration, follow these steps: To use the common ServiceNow API logic, attach the from ServiceNowApiModule import * # noqa: E402 line of code after the main() definition, before it is called to import it as shown in the example below. After you import the module, the ServiceNowClient will be available for use. For examples, see the ServiceNow_CMDB integration


## ServiceNowCreateIncident

**Type:** script  
**Product:** ServiceNow  

Wraps the generic create-record command in ServiceNow. Fields can be added that create the record with a script argument or in the code and work with the records

**Inputs:**

- `severity`: The incident severity.
- `assignee`: The incident assignee name. For example, "John Smith".
- `description`: The incident description.
- `assigned_group`: The incident assigned group name. For example, "Incident Management Group".


## ServiceNowIncidentStatus

**Type:** script  
**Product:** ServiceNow  

populates the value of the ServiceNow Ticket State field and display it in a layout widget


## ServiceNowQueryIncident

**Type:** script  
**Product:** ServiceNow  

Wraps the generic query-table command in ServiceNow. Fields can be added to use as inputs and outputs from the record as script arguments or in the code and work with the records

**Inputs:**

- `id`: The system ID of the incident.
- `number`: Th number of the incident.
- `assignee`: The assignee name of the incident. For example, "John Smith".


## ServiceNowTroubleshoot

**Type:** script  
**Product:** ServiceNow  

Troubleshoot ServiceNow v2 integration by displaying health information


## ServiceNowUpdateIncident

**Type:** script  
**Product:** ServiceNow  

Wraps the generic update-record command in ServiceNow. Fields can be added that update the record with as script arguments or in the code and work with the records easily

**Inputs:**

- `severity`: The severity of the incident.
- `assignee`: The assignee name of the incident. For example, "John Smith".
- `description`: The description of the incident.
- `assigned_group`: The assigned group name of the incident. For example, "Incident Management Group".
- `id`: The incident ID to update.
- `number`: The incident number to update.
- `query`: The query to use.


## Set RaDark Grid For Compromised Accounts

**Type:** playbook  
**Product:** KELA RaDark  

Set grid for RaDark - Compromised Accounts incidents


## Set RaDark Grid For Credit Cards

**Type:** playbook  
**Product:** KELA RaDark  

Set grid for RaDark - Credit Cards incidents


## Set RaDark Grid For Hacking Discussions

**Type:** playbook  
**Product:** KELA RaDark  

Set grid for RaDark - Hacking Discussions incidents


## Set RaDark Grid For Leaked Credentials

**Type:** playbook  
**Product:** KELA RaDark  

Set grid for RaDark - Leaked Credentials incidents


## Set RaDark Grid For Network Vulnerabilities

**Type:** playbook  
**Product:** KELA RaDark  

Set grid for RaDark - Network Vulnerabilities incidents


## Set RDP Bitmap Cache Overall Score

**Type:** playbook  
**Product:** RDPCacheHunting  

This playbook sets the RDP bitmap cache overall score


## ShiftLeft CORE

**Type:** integration  
**Product:** ShiftLeft CORE  

Integrate ShiftLeft CORE code analysis platform with the platform. This integration was integrated and tested with v4 api of ShiftLeft CORE

**Commands:**

- `shiftleft-list-apps`: Return list of apps.
- `shiftleft-list-app-findings`: Return list of app findings.
- `shiftleft-list-app-secrets`: Return list of app secrets.


## Shodan v2

**Type:** integration  
**Product:** Shodan  

Shodan is a search engine for Internet-connected devices. Unlike traditional search engines that index websites, Shodan indexes information about the devices connected to the internet, such as servers, routers, webcams, and other IoT devices

**Commands:**

- `search`: Searches Shodan using facets to get summary information on properties.
- `ip`: Returns all services that have been found on the IP address of the searched host.
- `shodan-search-count`: Returns the total number of results that match only the specified query or facet settings. This command does not return host results. This command does not cons
- `shodan-scan-ip`: Requests Shodan to crawl a network.
- `shodan-scan-internet`: Requests for Shodan to perform a scan on the specified port and protocol.


## SiemApiModule

**Type:** script  

## sigma-button-convert

**Type:** script  
**Product:** Sigma  

This script is needed for the button in the Sigma indicator layout

**Inputs:**

- `SIEM`: 


## SigmaConverttoQuery

**Type:** script  
**Product:** Sigma  

Allows converting a Sigma Rule indicator into a SIEM query

**Inputs:**

- `indicator`: The Sigma Rule indicator to convert to a query
- `SIEM`: 


## SIGNL4 (Beta)

**Type:** integration  
**Product:** SIGNL4  

SIGNL4 offers critical alerting, incident response and service dispatching for operating critical infrastructure. It alerts you persistently via app push, SMS text, voice calls, and email including tracking, escalation, on-call duty scheduling and collaboration

**Commands:**

- `signl4_alert`: Sends a mobile alert to a SIGNL4 team.
- `signl4_close_alert`: Close a SIGNL4 alert.


## Signum

**Type:** integration  
**Product:** Signum  

Signum password expiry notification

**Commands:**

- `signum-list-domain-users`: List domain users by domain ID.


## SilentPush

**Type:** integration  
**Product:** Silent Push  

The Silent Push Platform uses first-party data and a proprietary scanning engine to enrich global DNS data with risk and reputation scoring, giving security teams the ability to join the dots across the entire IPv4 and IPv6 range, and identify adversary infrastructure before an attack is launched. The content pack integrates with the Silent Push system to gain insights into domain/IP information, reputations, enrichment, and infratag-related details. It also provides functionality to live-scan URLs and take screenshots of them. Additionally, it allows fetching future attack feeds from the Silent Push system. This integration was integrated and tested with v1 of SilentPush API

**Commands:**

- `silentpush-add-feed`: Add the new feed.
- `silentpush-add-feed-tags`: Add indicators to the feed.
- `silentpush-add-indicators`: Add indicators to the feed.
- `silentpush-add-indicator-tags`: Updates tags to the indicators.
- `silentpush-bulk-enrich`: Enriches IPs or Domains in a bulk.
- `silentpush-density-lookup`: Queries granular DNS/IP parameters (e.g., NS servers, MX servers, IPaddresses, ASNs) for density information.
- `silentpush-forward-padns-lookup`: Performs a forward PADNS lookup using various filtering parameters.
- `silentpush-get-asns-for-domain`: Retrieves Autonomous System Numbers (ASNs) associated with a domain.
- `silentpush-get-data-exports`: Runs the threat check on the specified export type.
- `silentpush-get-domain-certificates`: Get certificate data collected from domain scanning.
- `silentpush-get-enrichment-data`: 
- `silentpush-get-enrichment-data`: Retrieves comprehensive enrichment information for a given resource (domain, IPv4, or IPv6).
- `silentpush-get-nameserver-reputation`: Retrieves historical reputation data for a specified nameserver, including reputation scores and optional detailed calculation information.
- `silentpush-get-subnet-reputation`: Retrieves the reputation history for a specific subnet.
- `silentpush-ip-diversity-lookup`: Get IP diversity (number of IP addresses pointed to over time) for the query to qtype.


## Silverfort

**Type:** integration  
**Product:** Silverfort  

Silverfort protects organizations from data breaches by delivering strong authentication across entire corporate networks and cloud environments, without requiring any modifications to endpoints or servers. Using patent-pending technology, Silverfort's agentless approach enables multi-factor authentication and AI-driven adaptive authentication even for systems that don’t support it today, including proprietary systems, critical infrastructure, shared folders, IoT devices, and more. Use Silverfort integration to get & update Silverfort risk severity. This integration was integrated and tested with Silverfort version 5.2

**Commands:**

- `silverfort-get-user-risk`: User risk commands - get the user entity risk.
- `silverfort-get-resource-risk`: Gets the resource entity risk information.
- `silverfort-update-user-risk`: Updates the user entity risk.
- `silverfort-update-resource-risk`: Update the resource entity risk.


## Skyhigh Secure Web Gateway (On Prem)

**Type:** integration  
**Product:** McAfee Web Gateway  

Manages the block and allow lists within Skyhigh Secure Web Gateway. This integration was integrated and tested with version 11.2.9 of Skyhigh Secure Web Gateway (On Prem)

**Commands:**

- `swg-get-available-lists`: Get all available lists.
- `swg-get-list`: Retrieve a specific list.
- `swg-get-list-entry`: Retrieve a specific entry from a list.
- `swg-insert-entry`: Insert a new entry to a list.
- `swg-delete-entry`: Insert a new entry to a list.
- `swg-modify-list`: Overwrites the complete XML configuration of a list.
- `swg-create-list`: Create a new list.
- `swg-delete-list`: Delete a list.


## Skyhigh Security

**Type:** integration  
**Product:** Skyhigh Security SSE  

Skyhigh Security is a cloud-based, multi-tenant service that enables Cloud Discovery and Risk Monitoring, Cloud Usage Analytics, Cloud Access and Control. This integration was integrated and tested with version 1 of Skyhigh Security. Do to API limitations, keep in mind that over time the integration can start to work more slowly. The solution is to restart the last-run

**Commands:**

- `skyhigh-security-incident-query`: Retrieves a list of incidents in ascending time modified order.
- `skyhigh-security-incident-status-update`: Update status of single/multiple incidents.
- `skyhigh-security-anomaly-activity-list`: Fetches activities for a given anomaly ID.
- `skyhigh-security-policy-dictionary-list`: List existing policy dictionaries.
- `skyhigh-security-policy-dictionary-update`: Adds new content to an existing policy dictionary.


## Slack IAM

**Type:** integration  
**Product:** Slack  

Note: This integration should be used as part of our Identity Lifecycle Management premium pack. For further details, visit our IAM pack documentation. Integrate with Slack's services to execute CRUD operations for employee lifecycle processes. For more information, please refer to the Identity Lifecycle Management article

**Commands:**

- `iam-create-user`: Creates a user.
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Disable an active user.
- `iam-create-group`: Creates an empty group
- `iam-get-group`: Retrieves the group information including members
- `iam-delete-group`: Permanently removes a group.
- `iam-update-group`: Updates an existing group resource. This command allows individual (or groups of) users to be added or removed from the group with a single operation. A max of 


## Slack v3

**Type:** integration  
**Product:** Slack  

Send messages and notifications to your Slack team. This integration was integrated and tested with Slack

**Commands:**

- `mirror-investigation`: Mirrors the investigation between Slack and the the platform.
- `send-notification`: Sends a message to a user, group, or channel.
- `close-channel`: Archives a Slack channel.
- `slack-send-file`: Sends a file to a user, channel, or group. If not specified, the file is sent to the mirrored investigation channel (if the channel exists).
- `slack-set-channel-topic`: Sets the topic for a channel.
- `slack-create-channel`: Creates a channel in Slack.
- `slack-invite-to-channel`: Invites users to join a channel.
- `slack-kick-from-channel`: Removes users from the specified channel.
- `slack-rename-channel`: Renames a channel in Slack.
- `slack-get-user-details`: Get details about a specified user.
- `slack-edit-message`: Edit an existing Slack message.
- `slack-pin-message`: Pins a selected message to the given channel.
- `slack-get-integration-context`: Returns the integration context as a file. Use this command for debug purposes only.
- `slack-user-session-reset`: Reset user session token in Slack.
- `slack-list-channels`: List all of the channels in the organization workspace. This command required scopes depend on the type of channel-like object you're working with. To use the c


## SMIME Messaging

**Type:** integration  
**Product:** SMIME Messaging  

Use the S/MIME (Secure Multipurpose Internet Mail Extensions) integration to send and receive secure MIME data. This integration was integrated and tested with version 0.40.1 of M2Crypto

**Commands:**

- `smime-verify-sign`: Verifies the signature.
- `smime-decrypt-email-body`: Decrypts the message body.
- `smime-sign-and-encrypt`: Encrypts and signs an email message with S/MIME protocol by using a public RSA certificate.


## Smokescreen IllusionBLACK

**Type:** integration  
**Product:** Smokescreen IllusionBLACK  

Smokescreen IllusionBLACK is a deception-based threat defense platform designed to accurately and efficiently detect targeted threats including reconnaissance, lateral movement, malware-less attacks, social engineering, Man-in-the-Middle attacks, and ransomware in real-time. This integration was integrated and tested with version v3.10.7.4 of Smokescreen IllusionBLACK

**Commands:**

- `illusionblack-get-ad-decoys`: Gets a list of Active Directory decoys.
- `illusionblack-get-network-decoys`: Gets a list of Network decoys.
- `illusionblack-get-ti-decoys`: Gets a list of Threat Intel decoys.
- `illusionblack-is-host-decoy`: Checks if a host or IP address is a network decoy.
- `illusionblack-is-user-decoy`: Checks if an Active Directory user is a decoy.
- `illusionblack-is-subdomain-decoy`: Checks if a subdomain is a Threat Intel decoy.
- `illusionblack-get-events`: Gets events from IllusionBLACK.
- `illusionblack-get-event-by-id`: Gets a single event by the event ID.


## SnmpDetection

**Type:** script  
**Product:** Cortex Attack Surface Management  

Checks to see if SNMP is enabled on the IP address provided

**Inputs:**

- `ip_address`: IP address.
- `time_out`: Request timeout value, in seconds. Default value is 3 seconds.


## SOC Framework Pack Manager

**Type:** integration  
**Product:** SOC Framework  

SOC Framework Pack Manager — internal HTTP layer used by the SOCFWPackManager script to install SOC Framework content packs as system content. End users do not invoke this integration directly

**Commands:**

- `socfw-install-pack`: Downloads a SOC Framework pack ZIP from the supplied URL and installs it on the tenant. After the upload the command reads the installed pack version back from 
- `socfw-catalog-url-get`: Returns the SOC Framework pack catalog URL configured on this instance. Called by the SOCFWPackManager script so the catalog location is set once on the instanc


## SOCFWPackManager

**Type:** script  
**Product:** SOC Framework  

The SOC Framework bootloader for Cortex XSIAM. Lists the SOC Framework pack catalog with the installed version and update status of each pack, installs and configures packs from platform_config.json, re-runs configuration only, and diagnoses the platform endpoints the install path depends on. Also includes sync-tags, a backward-compatible action for older SOC Framework deployments still using the value_tags lookup; modern versions use the SOCActionTimeMap_V3 list and do not require it

**Commands:**

- `socfw-install-pack`: Downloads a SOC Framework pack ZIP from the supplied URL and installs it on the tenant. After the upload the command reads the installed pack version back from 
- `socfw-catalog-url-get`: Returns the SOC Framework pack catalog URL configured on this instance. Called by the SOCFWPackManager script so the catalog location is set once on the instanc

**Inputs:**

- `action`: The action to run. The diagnose action probes every platform endpoint the marketplace install path depends on and reports which one fails; r
- `probe_pack`: The pack ID used to probe the marketplace metadata and dependency endpoints, for the diagnose action only. Whois is a stock Marketplace pack
- `pack_id`: The pack ID from pack_catalog.json (for example, soc-optimization-unified). Required for action=apply.
- `catalog_url`: Override the catalog URL without modifying the integration instance parameters.
- `using`: Integration instance name to route core-api commands through. Defaults to the active instance.
- `include_hidden`: Allow installing packs where visible=false in the catalog.
- `dry_run`: Show what would happen without installing or configuring.
- `install_marketplace`: Whether to install marketplace_packs from platform_config.json.


## SOCRadar Incident

**Type:** playbook  
**Product:** SOCRadar  

Performs indicator extraction and enrichment from the incident content, calculates the severity level, assigns the incident to a particular analyst, notifies SOCRadar platform for the incident response (to mark it as false positive or resolved) and generates investigation summary report just before closing the investigation in the end. This playbook is executed for the SOCRadar Generic incident type

**Inputs:**

- `AutoEnrich`: Auto Enrich input to be used for extracting indicators out of the incident content automatically at the beginning of the playbook. (Options:


## SOCRadar Incidents

**Type:** integration  
**Product:** SOCRadar  

Fetches SOCRadar incidents with desired parameters so that relevant actions over the incidents can be taken by using the platform. This integration was integrated and tested with v21.11 of SOCRadar

**Commands:**

- `socradar-mark-incident-fp`: Marks incident as false positive in SOCRadar platform.
- `socradar-mark-incident-resolved`: Marks incident as resolved in SOCRadar platform.


## SOCRadar Incidents Multi-Tenant

**Type:** integration  
**Product:** SOCRadar  

Fetch and manage security incidents from multiple companies using SOCRadar's Multi-Tenant Incident API. Designed for MSPs, MSSPs, and organizations managing multiple subsidiaries

**Commands:**

- `socradar-change-alarm-status`: Change the status of one or more alarms.
- `socradar-mark-false-positive`: Mark an alarm as false positive.
- `socradar-mark-resolved`: Mark an alarm as resolved.
- `socradar-add-comment`: Add a comment to an alarm.
- `socradar-add-assignee`: Add the assignee(s) of an alarm.
- `socradar-add-tag`: Add or remove a tag from an alarm.
- `socradar-test-fetch`: Test incident fetching to verify alarms are available and date parsing works correctly.


## SOCRadar Incidents v4

**Type:** integration  
**Product:** SOCRadar  

Fetch and manage security incidents from SOCRadar's Incident API v4 with advanced filtering, multi-status selection, and comprehensive incident enrichment


## SOCRadar IoC Enrichment

**Type:** integration  
**Product:** SOCRadar  

## SOCRadar Rapid Reputation

**Type:** integration  
**Product:** SOCRadar  

Enrich indicators (IP, Domain, URL, Hash) by obtaining reputation information via SOCRadar's Rapid Reputation API. This integration was integrated and tested with the latest version of SOCRadar Rapid Reputation API

**Commands:**

- `socradar-bulk-check`: 🎯 NEW FEATURE - Bulk check reputation for mixed list of indicators with automatic entity type detection.


## SOCRadar Takedown

**Type:** integration  
**Product:** SOCRadarTakedown  

Submit and monitor takedown requests for phishing domains, impersonating accounts, and other digital risks

**Commands:**

- `socradar-submit-phishing-domain`: Submits a takedown request for a phishing domain or URL
- `socradar-submit-social-media-impersonation`: Submits a takedown request for an impersonating social media account
- `socradar-submit-source-code-leak`: Submits a takedown request for leaked source code
- `socradar-submit-rogue-app`: Submits a takedown request for a rogue mobile app


## SOCRadar ThreatFusion

**Type:** integration  
**Product:** SOCRadar  

Enrich indicators by obtaining enhanced information and reputation via ThreatFusion of SOCRadar. This integration was integrated and tested with v21.11 of SOCRadar

**Commands:**

- `ip`: Scores provided IP entities' reputation in SOCRadar ThreatFusion.
- `domain`: Scores provided domain entities' reputation in SOCRadar ThreatFusion.
- `file`: Scores provided hash entities' reputation in SOCRadar ThreatFusion.
- `socradar-score-ip`: Scores provided IP entity's reputation in SOCRadar ThreatFusion.
- `socradar-score-domain`: Scores provided domain entity's reputation in SOCRadar ThreatFusion.
- `socradar-score-hash`: Scores provided hash entity's reputation in SOCRadar ThreatFusion.


## SolarWinds

**Type:** integration  
**Product:** SolarWinds  

The SolarWinds integration interacts with the SWIS API to allow users to fetch alerts and events. It also provides commands to retrieve lists of alerts and events. This integration was integrated and tested with version 3.0.0 of SolarWinds Information Service (SWIS API)

**Commands:**

- `swis-event-list`: Retrieves a list of events on the filter values provided in the command arguments.
- `swis-alert-list`: Retrieves a list of alerts based on the filter values provided in the command arguments.
- `swis-query`: Executes a query request. Click here to navigate to the guidelines to generate a query. SolarWinds Information Service schema can be found here.


## Sophos Central

**Type:** integration  
**Product:** Sophos Central  

The unified console for managing Sophos products

**Commands:**

- `sophos-central-alert-list`: List alerts.
- `sophos-central-alert-get`: Get a single alert by ID.
- `sophos-central-alert-action`: Take an action against alerts.
- `sophos-central-alert-search`: Get alerts matching request.
- `sophos-central-endpoint-list`: List all endpoints for a tenant.
- `sophos-central-endpoint-scan`: Scan endpoints of a tenant.
- `sophos-central-endpoint-tamper-get`: Get tamper protection information for one or more endpoints. Potentially harmful because of the password.
- `sophos-central-endpoint-tamper-update`: Update tamper protection information for one or more endpoints. Potentially Harmful because of the password.
- `sophos-central-allowed-item-list`: List all allowed items.
- `sophos-central-allowed-item-get`: Get a single allowed item by ID.
- `sophos-central-allowed-item-add`: Add a new allowed item.
- `sophos-central-allowed-item-update`: Update an existing allowed item.
- `sophos-central-allowed-item-delete`: Delete an existing allowed item.
- `sophos-central-blocked-item-list`: Get all blocked items.
- `sophos-central-blocked-item-get`: Get a single blocked item by ID.


## Spamcop

**Type:** integration  
**Product:** Spamcop  

SpamCop is an email spam reporting service. The integration allows checking the reputation of an IP address. This integration was integrated and tested with Spamcop

**Commands:**

- `ip`: Get IP details from Spamcop service


## SpecterOps BloodHound Enterprise

**Type:** integration  
**Product:** SpecterOps BloodHound Enterprise  

This integration enables automated retrieval of attack path findings from BloodHound into the platform, streamlining incident creation and investigation. This integration was integrated and tested with version 1.0.0 of SpecterOps BloodHound Enterprise

**Commands:**

- `bloodhound-object-id-get`: Fetches the object ID using the object name.
- `bloodhound-asset-info-get`: Fetches asset information using the object ID.
- `bloodhound-path-exist`: Checks if a path exists between the two nodes.


## SpecterOpsBloodHoundEnterprise

**Type:** playbook  
**Product:** SpecterOps BloodHound Enterprise  

Automated playbook that enriches BloodHound Enterprise attack path incidents with object information and validates attack path existence between security principals

**Commands:**

- `bloodhound-object-id-get`: Fetches the object ID using the object name.
- `bloodhound-asset-info-get`: Fetches asset information using the object ID.
- `bloodhound-path-exist`: Checks if a path exists between the two nodes.


## SSDeepReputation

**Type:** script  
**Product:** Common Scripts  

Calculates the SSdeep reputation based on similar files (by ssdeep similarity) on the system

**Inputs:**

- `input`: The SSdeep value.
- `timeFrameDays`: Checks similar values in this time frame (in days).
- `threshold`: Considerers similar SSdeep above this threshold.


## SSDeepSimilarity

**Type:** script  
**Product:** Common Scripts  

This script finds similar files that can be related to each other by fuzzy hash (SSDeep)

**Inputs:**

- `ssdeep_hash`: The SSDeep hash to check for similarity against.
- `ssdeep_hashes_to_compare`: A list of SSDeep hashes to check for similarity to the ssdeep_hash input.
- `output_key`: The context key to which the list of SSDeep hashes will be outputted.In case used, the default outputs will not contain the results.In order


## SSIMScoreWidget

**Type:** script  
**Product:** Suspicious Domain Hunting  

This dynamic automation parses the CVSS score of a CVE and presents it in the layout in color according to its score


## SSL Labs

**Type:** integration  
**Product:** SSL Labs  

Analyze a host or a URL

**Commands:**

- `ssl-labs-register-email`: Register for Scan API initiation and result fetching
- `ssl-labs-info`: Check the availability of the SSL Labs servers, retrieve the engine and criteria version, and initialize the maximum number of concurrent assessments.
- `ssl-labs-analyze`: Invoke assessments.


## SSL_Certificate_Verification

**Type:** playbook  
**Product:** SSL Certificates  

Demo playbook to take a list of addresses from a specified platform list, process the status of the SSL certificate for each address, and generate war room and email outputs for the status of each certificate


## SSLVerifierV2

**Type:** script  
**Product:** SSL Certificates  

Use this automation to check for validity of your SSL certificate and get the time until expiration

**Inputs:**

- `URL`: URL to check
- `Port`: Port to check


## SSLVerifierV2_ParseOutput

**Type:** script  
**Product:** SSL Certificates  

Parses the output from the !SSLVerifierV2 automation into a markdown table and separate context key . This automation uses the SSLVerifierV2 key by default, but a custom context key can be specified in the event extend-context is used with the SSLVerifierV2 automation. Option to specify whether to output certificates with an expiring, warning, or good status (or all at once). Option to specify whether or not to output the generated tables to the war room

**Inputs:**

- `SSLVerifierKey`: The key from context containing the SSLVerifier Data (Defaults to SSLVerifier)
- `StatusType`: The status of certificate to extract (good (&gt; 180 days), warning (&lt;=180 days and &gt; 90 days), expiring (&lt;= 90 days))
- `OutputToWarRoom`: Output the resulting tables to the war room? Default: true


## STA-FetchListContent

**Type:** script  
**Product:** Thales SafeNet Trusted Access  

This script will get the Unusual Activity Group from "sta_unusual_activity_group" List

**Inputs:**

- `list_name`: Name of the list containing the Unusual Activity Group.


## STA-PostProcessing

**Type:** script  
**Product:** Thales SafeNet Trusted Access  

Post processing script to remove the user from the Unusual Activity Group on Close Form


## Stairwell Inception

**Type:** integration  
**Product:** Stairwell  

Use the Stairwell Inception integration to enrich data in platform using Stairwell's knowledge and perform automated variant discovery. Not a customer and interested in signing up? You can request access here

**Commands:**

- `inception-file-enrichment`: Enrich files using file hash (MD5, SHA1, SHA256) with Stairwell's knowledge.
- `inception-variant-discovery`: Hunt for variants using a SHA256 across all files you have access to, including your environments and Stairwell's malware feeds.


## Stamus

**Type:** integration  
**Product:** Stamus  

[Get Declaration of Compromises from Stamus Security Platform and build Incidents. Then get related artifacts, events and Host Insight information] This integration was integrated and tested with version 39.0.1 of Stamus Security Platform

**Commands:**

- `stamus-check-ioc`: [Get events with IOC key/value filter]
- `stamus-get-host-insight`: [Get Host Insights information]
- `stamus-get-doc-events`: [Get events for a Declaration of Compromise using the Stamus ID]


## Stamus Networks - Get Extra Data

**Type:** playbook  
**Product:** Stamus  

## StartAgenticValidation

**Type:** script  
**Product:** Tenzai  

Ad-hoc entry point for Tenzai exposure validation, invoked from the Start Tenzai Validation button on the Tenzai issue layout (the Validate tab). On the first click it gathers the exposure context (optionally enriching from the ASM service via asm-get-external-service, or parsing the host:port from the exposure name), triggers a Tenzai validation assessment with tenzai-trigger-validation-check, and sets Tenzai Assessment Status to Running. It then drives the whole loop itself: a self-scheduling ScheduledCommand polls tenzai-fetch-validation-check until the assessment reaches a terminal status, then writes the verdict — status, exploit validation, assessment details, reproduction, fix guidance, credit usage, and reference URL — back onto the issue. It does not change the issue severity. Transient fetch failures are retried on the next poll; if the polling window (MAX_POLLS) is exhausted without a verdict the status is set to Error rather than left on Running. A second click while a validation is already Running on the issue is a no-op (no duplicate assessment). When run from the Tenzai Agentic Issue Validation playbook, the playbook passes poll=false: the script then only triggers and marks the issue Running, and the playbook owns the poll + write-back so the loop is not run twice

**Inputs:**

- `service_id`: ASM ExternalService id; used to enrich the target when target is not provided.
- `target`: The exposure target (IP or FQDN). If omitted, derived from the ASM service or parsed from exposure_name.
- `exposure_name`: Human-readable exposure name (typically the issue name).
- `supporting_data`: Free-text context (CVEs, rule, classification).
- `alert_internal_id`: The Cortex issue/alert id for result correlation.
- `application_type / port / protocol / service_classification`: Optional raw fields forwarded to Tenzai.
- `poll`: Whether the script polls to completion and writes the verdict itself. Defaults to true (the button); the playbook passes false.


## Stellar Cyber

**Type:** integration  
**Product:** Stellar Cyber  

Fetches and mirrors in Cases from Stellar Cyber to platform. In addition, provides a command to update Case severity/status/assignee/tags, and a command to query an Alert. This integration was integrated and tested with version >= 4.3.7/5.0.4 of StellarCyber

**Commands:**

- `stellar-get-alert`: Retrieve an alert from Stellar Cyber.
- `stellar-update-case`: Update the severity, status, assignee, or tags of a Case in Stellar Cyber.
- `get-remote-data`: Gets remote data from a remote incident. This method is only used for debugging purposes and will not update the current incident.
- `get-modified-remote-data`: Available from the platform.1.0. This command queries for incidents that were modified since the last update. This method is only used for debugging purposes.


## StixCreator

**Type:** script  
**Product:** Common Scripts  

Gets a list of indicators from the indicators argument, and generates a JSON file in STIX 2.1 format

**Inputs:**

- `indicators`: A JSON object of all indicators and their fields, indicator index mapped to platform common indicator fields. Indicator keys that don't matc
- `doubleBackslash`: Adds a second backslash to all existing backslashes in the value field.


## StopScheduledTask

**Type:** script  
**Product:** Common Scripts  

Stops the scheduled task whose ID is given in the taskID argument

**Inputs:**

- `taskID`: The ID of the schedule to stop.


## StopTimeToAssignOnOwnerChange

**Type:** script  
**Product:** Common Scripts  

Stops the "Time To Assign" timer if the owner of the incident was changed

**Inputs:**

- `old`: The old value of the changed field
- `new`: The new value of the changed field


## StringContainsArray

**Type:** script  
**Product:** Filters And Transformers  

Checks whether a substring or an array of substrings is within a string array (each item will be checked). Single strings are also supported. For example, for substrings ['a','b','c'] in a string 'a' the script will return true

**Inputs:**

- `left`: The string to search in. For example, "string1".
- `right`: The array of substrings to search in the string. For example, ["string1","string2"].


## StringifyArray

**Type:** script  
**Product:** Filters And Transformers  

Return the string encoded with JSON from the whole array

**Inputs:**

- `value`: The array to join if it has single element


## StringLength

**Type:** script  
**Product:** Common Scripts  

Returns the length of the string passed as an argument

**Inputs:**

- `str`: The string to evaluate.


## StringReplace

**Type:** script  
**Product:** Common Scripts  

Replaces regex match/es that are found in the string. This script will return the string after the replacement was performed

**Inputs:**

- `data`: The string to perform the replacement on.
- `regex`: The regex used to find matches that will be replaced with a new value.
- `newValue`: The new value to replace the regex match. Pass '' to remove regex match.
- `replaceAll`: Whether to replace matches. Pass true to replace all matches, false to replace only the first occurrence.
- `caseInsensitive`: Whether to perform a case-insensitive search and replace. Pass true to perform case-insensitive search and replace, false for case-sensitive
- `multiLine`: Pass true to indicate 'data' is a multi-line string, false otherwise.


## Strings

**Type:** script  
**Product:** Common Scripts  

Extracts strings from a file with an optional filter. This is similar to binutils strings command

**Inputs:**

- `entry`: The entry ID of a file entry to retrieve strings from.
- `chars`: The number of consecutive characters needed in order for it to be considered a string. The default is 4.
- `size`: The display first 'size' results. The default is 1024.
- `filter`: The regex to filter the strings. This will be compiled with the ignore case.


## StringSifter

**Type:** script  
**Product:** StringSifter  

This script runs the StringSifter ML tool for malware analysis and ranking of words. You can enter an entryID or string_text as input

**Inputs:**

- `limit`: Limit output to the top limit ranked strings.
- `min_score`: Limit output to strings with score &gt;= min-score.
- `file_name`: The file name. Mandatory when entering the data as string_text.
- `string_text`: The text to analyze with StringSifter.
- `entryID`: The file to process.


## StringSimilarity

**Type:** script  
**Product:** Common Scripts  

This automation calculates the similarity ratio between every string in 2 different arrays and outputs a decimal value between 0.0 and 1.0 (1.0 if the sequences are identical, and 0.0 if they don't have anything in common)

**Inputs:**

- `string_A`: First array of strings to compare.
- `string_B`: Second array of strings to compare.
- `similarity_threshold`: The similarity threshold to show results for, a value between 0 < x >1.


## StringToArray

**Type:** script  
**Product:** Filters And Transformers  

Converts string to array. For example:  will be transformed to ["

**Inputs:**

- `value`: The URL to transform.


## StripAccentMarksFromString

**Type:** script  
**Product:** Community Common Scripts  

Strip accent marks (diacritics) from a given string. For example: "Niño שָׁלוֹם Montréal اَلسَّلَامُ عَلَيْكُمْ‎" Will return: "Nino שלום Montreal السلام عليكم"

**Inputs:**

- `value`: 


## StripChars

**Type:** script  
**Product:** Filters And Transformers  

Strip set of characters from prefix and/or suffix e.g. StripChar value=~!!~www.mydomain.com~!~!~ chars=!~ will return www.mydomain.com

**Inputs:**

- `value`: Text to trim (e.g. "~!!~www.mydomain.com~\!~\!~"\)
- `chars`: Characters to stripped from the text (e.g. "!~")


## SuggestBranchName

**Type:** script  
**Product:** platform CI/CD  

The script gets the pack name as input and suggests an available branch name, for example: pack name is "MyPack" the branch name will be "MyPack". If a branch with the name "MyPack" exists, the script return "MyPack_1"

**Inputs:**

- `pack`: The name of the pack.
- `use_command`: Which command to use. Possible commands: gitlab-branch-list GitHub-get-branch * bitbucket-branch-get


## Superna Zero Trust

**Type:** integration  
**Product:** Superna Zero Trust  
**Commands:**

- `superna-zt-snapshot-critical-paths`: Create a snapshot of Superna critical paths for ransomware rapid recovery.
- `superna-zt-lockout-user`: Lock out a user from NAS storage access.
- `superna-zt-unlock-user`: Unlock a user from NAS storage access.


## Superna Zero Trust Request User Storage Lockout

**Type:** playbook  
**Product:** Superna Zero Trust  

## Superna Zero Trust Request User Storage UnLockout

**Type:** playbook  
**Product:** Superna Zero Trust  

## Superna Zero Trust Snapshot

**Type:** playbook  
**Product:** Superna Zero Trust  
**Inputs:**

- `username`: Username from incident context


## Superna Zero Trust User Lockout

**Type:** playbook  
**Product:** Superna Zero Trust  
**Inputs:**

- `username`: Source username from the incident (incident.sourceusername). This field is populated by Superna Zero Trust webhook integration.


## SX - PC - PingCastle Report

**Type:** playbook  
**Product:** PingCastle  

This playbook runs when a new report is sent from PingCastle. It then parses it to json and renders a table. It also puts a download link to the xml report in the war room

**Inputs:**

- `Indicator Query`: playbookInputQuery


## Symantec Data Loss Prevention v2

**Type:** integration  
**Product:** Symantec Data Loss Prevention  

Symantec Data Loss Prevention enables you to discover, monitor and protect your sensitive corporate information. This integration was integrated and tested with Symantec Data Loss Prevention version 15.7 RESTful API. Check Symantec DLP 15.7 API docs Some changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

**Commands:**

- `symantec-dlp-list-incidents`: Returns a list of incidents.
- `symantec-dlp-get-incident-details`: Returns details of the specified incident.
- `symantec-dlp-update-incident`: Updates the details of a specific incident.
- `symantec-dlp-list-incident-status`: Returns a list of the custom status values defined in the Symantec DLP deployment.
- `symantec-dlp-get-incident-history`: Returns the history of the specified incident.
- `symantec-dlp-list-remediation-status`: Returns a list of the remediation status values defined in the Symantec DLP deployment.
- `symantec-dlp-get-incident-original-message`: Fetches the original message from an incident. Requires SDLP 15.8.
- `symantec-dlp-get-report-filters`: Retrieves the filter criteria for a saved search in the Enforce console by report ID. Requires SDLP 16.0.
- `symantec-dlp-list-users`: Returns details for all SDLP users from the Enforce console. Requires SDLP 16.0.
- `symantec-dlp-get-sender-recipient-pattern`: Returns a sender/recipient pattern. Requires SDLP 16.0.
- `symantec-dlp-list-sender-recipient-patterns`: Returns a list of all sender/recipient patterns from the Enforce console. Requires SDLP 16.0.
- `symantec-dlp-update-sender-pattern`: Updates a sender pattern in the Enforce console. Requires SDLP 16.0.
- `symantec-dlp-update-recipient-pattern`: Updates a recipient pattern in the Enforce console. Requires SDLP 16.0.
- `symantec-dlp-get-message-body`: Returns the message body from the Enforce console by incident ID. Requires SDLP 16.0.


## Symantec Endpoint Security (ICDM)

**Type:** integration  
**Product:** SymantecICDM  

Query the Symantec Endpoint Security Cloud Portal (ICDM). This integration was integrated and tested with version 1 of SymantecICDM

**Commands:**

- `file`: Get file reputation for given SHA256.
- `ip`: Get ip reputation.
- `url`: Get reputation for given url.
- `domain`: Get reputation for given domain.
- `symantec-protection-file`: Get information whether a given file has been blocked by any Symantec technologies.
- `symantec-protection-network`: Get information whether given domain or ip has been blocked by any Symantec technologies.
- `symantec-protection-cve`: Get returns information whether a given CVE has been blocked by any Symantec technologies.


## Synapse

**Type:** integration  
**Product:** Synapse  

Synapse intelligence analysis platform. This integration was integrated and tested with version 2.7.0 of Synapse

**Commands:**

- `ip`: Returns IP information and reputation.
- `url`: Returns URL information and reputation.
- `domain`: Returns Domain information and reputation.
- `file`: Returns File information and reputation.
- `synapse-storm-query`: Execute a Synapse Storm query.
- `synapse-list-users`: Lists current users in Synapse Cortex.
- `synapse-list-roles`: Lists current roles in Synapse Cortex.
- `synapse-create-user`: Create a new Synapse user.
- `synapse-create-role`: Create a new Synapse role.
- `synapse-grant-user-role`: Grants a user access to role based perrmissions.
- `synapse-query-model`: Query the Synapse data model and return details for given type or form (i.e. "inet:ipv4" for an IPv4 IP address).


## Synchronize Incident Closure - Cyberhaven

**Type:** playbook  
**Product:** Cyberhaven  

Closes platform incidents by synchronizing their status with the corresponding Cyberhaven incident


## SysAid

**Type:** integration  
**Product:** SysAid  

SysAid is a robust IT management system designed to meet all of the needs of an IT department. This integration was integrated and tested with version 21.4.44 of SysAid

**Commands:**

- `sysaid-table-list`: Retrieve all lists (tables) related to a specific entity, or a specific list from an entity.
- `sysaid-asset-list`: List all assets or get a specific asset by ID. Cortex recommends filtering the results by the desired fields.
- `sysaid-asset-search`: Get information about a specific asset. Cortex recommends filtering the results by the desired fields.
- `sysaid-filter-list`: List all filters. Cortex recommends filtering the results by the desired fields.
- `sysaid-user-list`: Get list of users in SysAid. Cortex recommends filtering the results by the desired fields.
- `sysaid-user-search`: Get information about a specific asset. Cortex recommends filtering the results by the desired fields.
- `sysaid-service-record-list`: List all service requests. Cortex recommends filtering the results by the desired fields.
- `sysaid-service-record-search`: Search by a query through all service records. Cortex recommends filtering the results by the desired fields.
- `sysaid-service-record-update`: The valid statuses can be retrieved using the "sysaid-table-list" command.
- `sysaid-service-record-close`: Close a service record. Sets the service record status to the default Close status, as defined in the Help Desk settings.
- `sysaid-service-record-template-get`: Gets the template of a service record. Cortex recommends filtering the results by the desired fields.
- `sysaid-service-record-create`: Create a new service record and return the newly created service record. The valid statuses can be retrieved using the "sysaid-table-list" command. Cortex recom
- `sysaid-service-record-delete`: Delete one or more service records.
- `sysaid-service-record-attach-file`: Add an attachment to a service record.
- `sysaid-service-record-get-file`: Download an attachment to a service record.


## Syslog Sender

**Type:** integration  
**Product:** Syslog  
**Commands:**

- `mirror-investigation`: Mirrors the investigation's War Room to syslog.
- `send-notification`: Sends a message to syslog.
- `syslog-send`: Send a message to Syslog


## TaegisXDR v2

**Type:** integration  
**Product:** Secureworks  
**Commands:**

- `!taegis-add-evidence-to-investigation`: 
- `!taegis-archive-investigation`: 
- `!taegis-create-comment`: 
- `!taegis-create-investigation`: 
- `!taegis-create-sharelink`: 
- `!taegis-execute-playbook`: 
- `!taegis-fetch-alerts`: 
- `!taegis-fetch-assets`: 
- `!taegis-fetch-comment`: 
- `!taegis-create-comments`: 
- `!taegis-fetch-endpoint`: 
- `!taegis-fetch-investigation`: 
- `!taegis-fetch-investigation-alerts`: 
- `!taegis-fetch-playbook-execution`: 
- `!taegis-fetch-users`: 


## Tag massive and internal IOCs to avoid EDL listing

**Type:** playbook  
**Product:** Generic Export Indicators Service  

This playbook tags internal assets and massive IOCs (TLD wildcards and CIDRs) to be avoided by the EDL. The playbook does the following according to indicator type: We recommend running the playbook as a job to keep tags up to date on new indicators

**Inputs:**

- `Indicator Query`: This query retrieves the following indicator types - IP, IPv6, CIDR, and IPv6CIDR
- `Internal Assets`: A list of internal assets consisting of CIDRs and domains that belong to the user.
- `Maximum CIDR Prefix`: The maximum prefix to allow, any prefix bigger than the specified is tagged to be ignored by the EDL.


## Tanium - Ask Question

**Type:** playbook  
**Product:** Tanium  

Uses generic polling to gets question result

**Inputs:**

- `question-text`: 
- `parameters`: 


## Tanium - Get Saved Question Result

**Type:** playbook  
**Product:** Tanium  

Uses generic polling to gets saved question result

**Inputs:**

- `saved-question-id`: The unique IDs of the saved questons.


## TaniumFilterComputersByIndexQueryFileDetails

**Type:** script  
**Product:** Tanium  

Gets the requested sensors from all of the machines where the index query file details match the given filter. For example, !TaniumFilterQuestionByIndexQueryFileDetails sensors="Computer Name" filter_type=contains filter_value=platform limit=5 will be translated to the following plain text Tanium question: "Get Computer Name from all machines with any Index Query File Details[,, ,, ,, *, 5] containing "platform""

**Inputs:**

- `directoryPath`: The glob of the directory's name used for searching. For example, "Windows".
- `fileName`: The glob of the file's name used for searching. For example, "*exe".
- `fileSize`: The glob of the file's size used for searching. For example, "10??".
- `fileMD5Hash`: The glob of the file's MD5 hash used for searching. For example, "1c7b*".
- `fileSHA1Hash`: The glob of the file's SHA1 hash used for searching. For example, "1c7b*".
- `fileSHA256Hash`: The gob of the file's SHA256 hash used for searching. For example, "1c7b*".
- `magicNumber`: The glob of a magic number used for searching. For example, "4D54*".
- `limit`: The maximum number of rows to return.


## Tavily

**Type:** integration  
**Product:** Tavily  

Tavily is a web service that provides real-time web search and retrieval capabilities through an API, enabling developers to fetch and extract relevant information from the internet

**Commands:**

- `tavily-extract`: Extract web page content from a specified URL.


## TAXII2 Server

**Type:** integration  
**Product:** TAXII Server  
**Commands:**

- `taxii-server-list-collections`: Returns all the collections.
- `taxii-server-info`: Returns the TAXII server info, default URL, title, etc.


## TAXII2ApiModule

**Type:** script  

To use the common TAXII 2 Server logic (authentication and API requests), run the following command to import the TAXII2ApiModule. Then, the TAXII2ApiModule will be available for usage. For examples, see the TAXII 2 Feed integration


## Team Cymru

**Type:** integration  
**Product:** Team Cymru  

Team Cymru provides various service options dedicated to mapping IP numbers to BGP prefixes and ASNs. Each of the services is based on the same BGP feeds from 50+ BGP peers and is updated at 4-hour intervals. This integration was integrated and tested with version 1.0 of TeamCymru

**Commands:**

- `ip`: Checks the reputation of an IP address.
- `cymru-bulk-whois`: Checks the reputation of a CSV list of IPv4 addresses within a file. Note: Results for queries exceeding 10,000 IPs may take more than a minute given a moderate


## Team Cymru Scout

**Type:** integration  
**Product:** Team Cymru  
**Commands:**

- `scout-api-usage`: Returns all the information on used queries and remaining queries with the query limit.
- `ip`: Return all the detailed information available for the given IP address.
- `scout-indicator-search`: Return the summary information available for the given domain or IP address using Scout query language.
- `scout-ip-list`: Returns the summary information available for the given list of IP addresses.


## Tenzai

**Type:** integration  
**Product:** Tenzai  

Validate Cortex ASM-discovered exposures with Tenzai's agentic penetration testing. Create a scan for an exposure, poll it to completion, and fetch the verdict and evidence back into the Cortex issue

**Commands:**

- `tenzai-create-scan`: Create a Tenzai agentic scan for a Cortex ASM-discovered exposure. Finds or creates a Tenzai application for the target domain, then triggers an EXTERNAL_LEAD s
- `tenzai-get-scan`: Poll the status of a Tenzai scan until it reaches a terminal state (Complete or Error).
- `tenzai-get-scan-result`: Fetch the verdict and evidence of a completed Tenzai scan.


## Tenzai Agentic Issue Validation

**Type:** playbook  
**Product:** Tenzai  

Validates an ASM-discovered exposure with Tenzai's agentic penetration testing. Triggers a Tenzai validation assessment, polls until it completes, fetches the verdict, and records the verdict in the Tenzai issue fields. It does not change the issue severity

**Inputs:**

- `RequireAnalystApproval`: When true (default), the playbook pauses for an analyst to approve before Tenzai starts active testing, because validation runs live penetra
- `PollingInterval`: The interval, in seconds, between Tenzai scan status polls.
- `PollingTimeout`: The maximum time, in seconds, to wait for the Tenzai scan to reach a terminal state before giving up.


## TenzaiExposureSidebar

**Type:** script  
**Product:** Tenzai  

Renders the Validate tab's left-column exposure detail: a Timeline card showing the exposure lead's status history (OPEN / IN_PROGRESS / BLOCKED / MATERIALIZED / INVALIDATED, with timestamps). Reads the persisted Tenzai Timeline grid field on the issue. This script is a dynamic-section widget used by the Tenzai Issue Layout and is not intended to be run directly


## TenzaiValidationSummary

**Type:** script  
**Product:** Tenzai  

Renders the Tenzai validation summary panel for the Validate tab: a TENZAI wordmark + status line, a verdict hero (exploitable / not exploitable), a monospace telemetry grid (verdict, exploit, finding count, credit usage, reference link), a per-severity meter, and a per-finding overview (a color-coded severity chip + the finding title + a one-line summary). Reads the persisted Tenzai result fields on the issue. The overview is a summary — each finding's full detail renders in the Tenzai Findings grid directly below. This script is a dynamic-section widget used by the Tenzai Issue Layout and is not intended to be run directly


## Tessian

**Type:** integration  
**Product:** Tessian  

Tessian is an email security platform that allows organizations to protect their users from inbound phishing threats, outbound data loss (both malicious and accidental) and account takeovers

**Commands:**

- `tessian-list-events`: This command allows you to pull Tessian event data into your platform instance.


## TextFromHTML

**Type:** script  
**Product:** Common Scripts  

Extract regular text from the given HTML

**Inputs:**

- `html`: The HTML to strip tags from.
- `html_tag`: Specify the HTML tag to extract the text from within.
- `allow_body_fallback`: Allow using the input HTML as a fallback for the body, if no body tag is found. This only applies, if html_tag is set to body.
- `replace_line_breaks`: Replace `br` in `html` with linebreaks in the output.
- `trim_result`: Trim the extracted result. When set to true, leading and trailing whitespaces are removed and blocks of more than 3 consecutive whitespaces 
- `output_to_context`: Store the extracted text in context.


## Thales CipherTrust Manager

**Type:** integration  
**Product:** Thales CipherTrust Manager  

Manage secrets and protect sensitive data through Thales CipherTrust security platform. This integration was integrated and tested with version v1 of CipherTrust

**Commands:**

- `ciphertrust-csr-generate`: Creates a Certificate Signing Request (CSR) and its corresponding private key. This API does not store any state on the server as everything is returned in the 
- `ciphertrust-certificate-issue`: Issues a certificate by signing the provided CSR with the CA. This is typically used to issue server, client or intermediate CA certificates. Either duration or
- `ciphertrust-certificate-list`: Returns a list of certificates issued by the specified CA. The results can be filtered, using the command arguments.
- `ciphertrust-certificate-resume`: Certificate can be resumed only if it is revoked with reason certificateHold.
- `ciphertrust-certificate-revoke`: Revoke certificate with a given specific reason.
- `ciphertrust-external-ca-delete`: Deletes an external CA certificate.
- `ciphertrust-external-ca-list`: Returns a list of external CA certificates. The results can be filtered, using the command arguments.
- `ciphertrust-external-ca-update`: Update an external CA.
- `ciphertrust-external-ca-upload`: Uploads an external CA certificate. These certificates can later be trusted by services inside the system for verification of client certificates. The uploaded 
- `ciphertrust-group-create`: Create a new group. The group name is required.
- `ciphertrust-group-delete`: Deletes a group given the group name.
- `ciphertrust-group-list`: Returns a list of group Command arguments can be used to filter the results. Groups can be filtered for user or client membership. Connection filter applies onl
- `ciphertrust-group-update`: Update the properties of a group given the group name.
- `ciphertrust-local-ca-create`: Creates a pending local CA. This operation returns a CSR that either can be self-signed by calling the ciphertrust-local-ca-self-sign command or signed by anoth
- `ciphertrust-local-ca-delete`: Deletes a local CA certificate.


## Thales SafeNet Trusted Access

**Type:** integration  
**Product:** Thales SafeNet Trusted Access  

This integration enables you to process alerts from SafeNet Trusted Access (STA) indicating security risks to end user accounts, and apply security remediation actions on SafeNet Trusted Access through security orchestration playbooks. For information about the configuration steps, visit our Help Documentation

**Commands:**

- `sta-get-user-list`: Get list of users in the tenant.
- `sta-get-user-info`: Get the profile information for a specific user.
- `sta-create-user`: Create a new user in the tenant.
- `sta-update-user-info`: Update the profile for a specific user.
- `sta-delete-user`: Delete a user from the tenant.


## TheHive Project

**Type:** integration  
**Product:** TheHive Project  

Integration with The Hive Project Security Incident Response Platform. This integration was integrated and tested with version 4.1.4 of TheHive Project

**Commands:**

- `thehive-list-cases`: List cases.
- `thehive-get-case`: Get a case
- `thehive-update-case`: Update a case
- `thehive-create-case`: Create a new case
- `thehive-create-task`: Create a new task
- `thehive-remove-case`: Removes a case
- `thehive-merge-cases`: Merges 2 cases
- `thehive-get-case-tasks`: Get the tasks of a case
- `thehive-get-task`: Get a specific task.
- `thehive-update-task`: Updates a task.
- `thehive-update-observable`: Update an observable.
- `get-mapping-fields`: Returns the list of fields.
- `thehive-get-version`: Displays the version of TheHive Project.
- `get-modified-remote-data`: Gets the list of incidents that were modified since the last update time. Note that this method is here for debugging purposes. The get-modified-remote-data com


## ThousandEyes

**Type:** integration  
**Product:** ThousandEyes  

This Integration is used to fetch-incidents via “Active alerts”, get alert details via “Alert details”, and get the “Agent list”. It was integrated and tested with API v6 of ThousandEyes

**Commands:**

- `thousandeyes-get-alerts`: Fetches all the alerts.
- `thousandeyes-get-alert`: Fetches a given alert.
- `thousandeyes-get-agents`: Fetches all agents.
- `thousandeyes-get-agent`: Fetches a given agent.


## ThreeDigitAlphaCountryCodeToCountryName

**Type:** script  
**Product:** CyCognito  

Script for converting country names based on 3 letter Alpha codes

**Inputs:**

- `value`: Three digit country code


## ticksToTime

**Type:** script  
**Product:** Common Scripts  

Converts time in ticks to a readable time. The ticks are used to represent time by some vendors, most commonly by Microsoft

**Inputs:**

- `ticks`: The time as represented by ticks.


## TimeComponents

**Type:** script  
**Product:** Filters And Transformers  

Takes a date or time input and get time components in a specific time zone. Returns a dictionary with the following components

**Inputs:**

- `value`: Input date or time in a format that is supported by the dateparser.parse() function as outlined here- https://dateparser.readthedocs.io/en/l
- `time_zone`: The time zone (e.g. -0400, +09:00) or time string to extract a time zone
- `key`: The name of a key to choose which time component to return


## TimersOnOwnerChange

**Type:** script  
**Product:** CaseManagement-Generic  

Stops the "Time To Assignment" timer once an owner is assigned to the Incident Starts the "Remediation SLA' timer once an owner is assigned to the Incident

**Inputs:**

- `old`: The old value of the changed field
- `new`: The new value of the changed field


## TimeStampCompare

**Type:** script  
**Product:** Common Scripts  

Compares a single timestamp to a list of timestamps

**Inputs:**

- `tested_time`: Timestamp to compare to the list of timestamps.
- `values_to_compare`: Values to compare the tested_time against. The script checks each value and determines whether it's before/after/equal to the tested_time.
- `time_format`: Time format of the times you entered. By default, the script uses automatic parsing. This should be used for cases like DD/MM/YYYY. Automati


## TimeStampToDate

**Type:** script  
**Product:** Filters And Transformers  

Converts UNIX Epoch time stamp to a simplified extended ISO format string. Use tihs script to convert a time stamp to a the platform. For example, "1525006939" will return '2018-04-29T13:02:19.000Z'

**Inputs:**

- `value`: The time stamp to convert.


## TOPdesk

**Type:** integration  
**Product:** TOPdesk  

TOPdesk’s Enterprise Service Management software (ESM) lets your service teams join forces and process requests from a single platform. This integration was integrated and tested with 10.08.008-on-premises-release3-build2 for Linux x86 64-bit of TOPdesk

**Commands:**

- `topdesk-subcategories-list`: Get list of subcategories.
- `topdesk-categories-list`: Get list of categories.
- `topdesk-entry-types-list`: Get list of entry types.
- `topdesk-call-types-list`: Get list of entry types.
- `topdesk-deescalation-reasons-list`: Get list of deescalation reasons.
- `topdesk-escalation-reasons-list`: Get list of escalation reasons.
- `topdesk-archiving-reasons-list`: Get list of archiving reasons.
- `topdesk-persons-list`: Get list of persons.
- `topdesk-operators-list`: Get list of operators.
- `topdesk-branches-list`: Get list of branches.
- `topdesk-incidents-list`: Get list of incidents.
- `topdesk-incident-actions-list`: List all actions for specific incident
- `topdesk-incident-create`: Create an incident in TOPdesk.
- `topdesk-incident-update`: Update an incident in TOPdesk.
- `topdesk-incident-escalate`: Escalate an incident in TOPdesk.


## TopMaliciousRatioIndicators

**Type:** script  
**Product:** Common Scripts  

Finds the top malicious ratio indicators. The malicious ratio is defined by the ratio between the number of "bad" incidents divided by the total number of incidents that the indicators appears in

**Inputs:**

- `maxNumberOfIndicators`: The maximum number of indicators for malicious ratio calculation.
- `minimumNumberOfInvs`: The minimum number of investigations the indicator has to appear in.
- `maximumNumberOfResults`: The maximum number of results to display.


## ToTable

**Type:** script  
**Product:** Common Scripts  

Converts an array in to a table display. Usually, from the context

**Inputs:**

- `data`: The data to display as a table. This expects an array of objects.
- `title`: The title for the table.
- `columns`: The comma-separated list of columns to display. This accepts nested columns using dot notation.


## Traceable

**Type:** integration  
**Product:** Traceable  
**Commands:**

- `list_incident_cache`: List the entries present in the Traceable instance cache.
- `purge_incident_cache`: Delete all entries in the incident cache.


## Trello

**Type:** integration  
**Product:** Trello  

Interact with the Trello task manager This integration was integrated and tested with version 1.0.0 of Trello

**Commands:**

- `trello-list-boards`: List the boards available to the provided API Key
- `trello-list-lists`: List all the lists associated with the trello board.
- `trello-create-card`: Create a new card.
- `trello-delete-card`: Delete a card
- `trello-add-comment`: Add a comment to a Trello card


## TrendAI Vision One™

**Type:** integration  
**Product:** TrendAI Vision One™  

Support and maintenance for this integration are provided by the author. Please use the following contact details: TrendAI Vision One™ is a purpose-built threat defense platform that provides added value and new benefits beyond XDR solutions, allowing you to see more and respond faster. Providing deep and broad extended detection and response (XDR) capabilities that collect and automatically correlate data across multiple security layers—email, endpoints, servers, cloud workloads, and networks—TrendAI Vision One™ prevents the majority of attacks with automated protection

**Commands:**

- `trendmicro-visionone-add-to-block-list`: Adds a file SHA-1, IP address, domain, or URL object to the User-Defined Suspicious Objects List, which blocks the objects on subsequent detections
- `trendmicro-visionone-remove-from-block-list`: Removes a file SHA-1, IP address, domain, or URL from the User-Defined Suspicious Objects List
- `trendmicro-visionone-quarantine-email-message`: Moves a message from a mailbox to the quarantine folder
- `trendmicro-visionone-delete-email-message`: Deletes a message from a mailbox
- `trendmicro-visionone-isolate-endpoint`: Disconnects an endpoint from the network (but allows communication with the managing TrendAI™ product)
- `trendmicro-visionone-restore-endpoint-connection`: Restores network connectivity to an endpoint that applied the "isolate endpoint" action
- `trendmicro-visionone-add-objects-to-exception-list`: Adds domains, file SHA-1 values, IP addresses, or URLs to the Exception List and prevents these objects from being added to the Suspicious Object List
- `trendmicro-visionone-delete-objects-from-exception-list`: Deletes domains, file SHA-1 values, IP addresses, or URLs from the Exception List.
- `trendmicro-visionone-add-objects-to-suspicious-list`: Adds domains, file SHA-1 values, IP addresses, or URLs to the Suspicious Object List.
- `trendmicro-visionone-delete-objects-from-suspicious-list`: Deletes domains, file SHA-1 values, IP addresses, or URLs from the Suspicious Object List
- `trendmicro-visionone-get-endpoint-info`: Retrieves information about a specific endpoint
- `trendmicro-visionone-terminate-process`: Terminates a process that is running on an endpoint
- `trendmicro-visionone-get-file-analysis-status`: Retrieves the status of a sandbox analysis submission
- `trendmicro-visionone-get-file-analysis-report`: Retrieves the analysis report, investigation package, or Suspicious Object List of a submitted file
- `trendmicro-visionone-collect-forensic-file`: Compresses a file on an endpoint in a password-protected archive and then sends the archive to the XDR service platform


## TrendAI Vision One™ v3

**Type:** integration  
**Product:** TrendAI Vision One™  

TrendAI Vision One™ is a purpose-built threat defense platform that provides added value and new benefits beyond XDR solutions, allowing you to see more and respond faster. Providing deep and broad extended detection and response (XDR) capabilities that collect and automatically correlate data across multiple security layers—email, endpoints, servers, cloud workloads, and networks—TrendAI Vision One™ prevents the majority of attacks with automated protection. V3 version of the app includes everything that the previous app had and adds more capabilities. It leverages V3 of TrendAI™ APIs and introduces further ability to manage domain accounts with addition of 4 domain account actions for enabling/disabling user account, forcing sign-out and password resets for compromised accounts. This app is in active development. We previously added 4 actions, one to fetch email activity data with count, one to fetch endpoint activity data with count and an action to restore a quarantined email message. In this release we have added 6 new custom script actions allowing the user to fetch a list of available custom scripts in XDR portal, ability to run a custom script on a specified endpoint, capacity to add, download, update and delete a custom script from XDR portal. This integration was integrated and tested with version 3 API of TrendAI Vision One™

**Commands:**

- `trendmicro-visionone-enable-user-account`: Allows the user to sign in to new application and browser sessions. Supported IAM systems -> Azure AD and Active Directory (on-premises).
- `trendmicro-visionone-disable-user-account`: Signs the user out of all active application and browser sessions, and prevents the user from signing in any new session. Supported IAM systems -> Azure AD and 
- `trendmicro-visionone-force-signout`: Signs the user out of all active application and browser sessions. Supported IAM systems -> Azure AD.
- `trendmicro-visionone-force-password-reset`: Signs the user out of all active application and browser sessions, and forces the user to create a new password during the next sign-in attempt. Supported IAM s
- `trendmicro-visionone-add-to-block-list`: Adds a domain, ip, file_sha1, url, sender_mail_address to the User-Defined Suspicious Objects List, which blocks the objects on subsequent detections.
- `trendmicro-visionone-remove-from-block-list`: Removes a domain, ip, file_sha1, url, sender_mail_address from the User-Defined Suspicious Objects List.
- `trendmicro-visionone-quarantine-email-message`: Moves a message from a mailbox to the quarantine folder.
- `trendmicro-visionone-delete-email-message`: Deletes a message from a mailbox.
- `trendmicro-visionone-restore-email-message`: Restores a quarantined message. Deleted messages cannot be restored.
- `trendmicro-visionone-isolate-endpoint`: Disconnects an endpoint from the network (but allows communication with the managing TrendAI™ product).
- `trendmicro-visionone-restore-endpoint-connection`: Restores network connectivity to an endpoint that applied the "isolate endpoint" action.
- `trendmicro-visionone-add-objects-to-exception-list`: Adds domain, ip, url, file_sha1, file_sha256, sender_mail_address to the Exception List and prevents these objects from being added to the Suspicious Object Lis
- `trendmicro-visionone-delete-objects-from-exception-list`: Deletes domain, ip, url, file_sha1, file_sha256, sender_mail_address from the Exception List.
- `trendmicro-visionone-add-objects-to-suspicious-list`: Adds domain, ip, url, file_sha1, file_sha256, sender_mail_address to the Suspicious Object List.
- `trendmicro-visionone-delete-objects-from-suspicious-list`: Deletes domain, ip, url, file_sha1, file_sha256, sender_mail_address from the Suspicious Object List.


## TrendAI™ Apex One

**Type:** integration  
**Product:** TrendAI™ Apex One  

TrendAI™ Apex One central automation to manage agents and User-Defined Suspicious Objects This integration was integrated and tested with version 2019 hotfix 5449 of TrendAI™ Apex One Central

**Commands:**

- `trendmicro-apex-udso-list`: Retrieve a list of User-Defined Suspicious Objects from the Apex One Central server.
- `trendmicro-apex-udso-add`: Add suspicious file SHA-1, IP address, domain, or URL objects to the User-Defined Suspicious Object list.
- `trendmicro-apex-udso-delete`: Delete suspicious file SHA-1, IP address, domain, or URL objects from the User-Defined Suspicious Object list.
- `trendmicro-apex-isolate`: Isolate an agent from the network
- `trendmicro-apex-restore`: Restore an isolated agent connection to the network.
- `trendmicro-apex-list-logs`: Retrieves a maximum of 1000 logs of detection types from the server. The Pattern Update Status and Engine Update Status log types returns all logs (no maximum) 
- `trendmicro-apex-udso-file-add`: Adds the uploaded file information to the User-Defined Suspicious Objects list. If the file already exists, it will be updated with the new arguments.
- `trendmicro-apex-managed-servers-list`: Retrieves a list of managed product servers reporting to Apex One Central.
- `trendmicro-apex-security-agents-list`: Retrieves a list of Security Agents.
- `trendmicro-apex-endpoint-sensors-list`: Retrieves a list of Security Agents with the Endpoint Sensor feature enabled.
- `trendmicro-apex-historical-investigation-create`: Creates a new historical investigation on all Security Agents with Endpoint Sensor enabled using the specified criteria, search operator, and match condition.
- `trendmicro-apex-investigation-result-list`: Retrieves a list of all investigation results.


## TrendAI™ Deep Security™

**Type:** integration  
**Product:** TrendAI™ Deep Security™  

TrendAI™ Deep Security™ This integration was integrated and tested with version 20.0 of TrendAI™ Deep Security™, and v1 of the API

**Commands:**

- `trendmicro-create-computer`: Create a new computer
- `trendmicro-search-computers`: Search for specific computers by some field name with a certain type. Every field has a specific type. It can be a simple type like a string, a numeric or a boo
- `trendmicro-get-computer`: Get information about a certain computer
- `trendmicro-list-computers`: Get information of all existing computers
- `trendmicro-modify-computer`: Modify properties of a certain computer
- `trendmicro-delete-computer`: Delete a certain computer
- `trendmicro-get-computer-setting`: Get information about a setting of a certain computer
- `trendmicro-modify-computer-setting`: Modify a setting of a certain computer
- `trendmicro-reset-computer-setting`: Reset a setting of certain computer to its default value.
- `trendmicro-list-computer-groups`: Get information about all existing computer groups
- `trendmicro-create-computer-group`: Create a new computer group
- `trendmicro-search-computer-groups`: Search for specific computer groups by some field name with a certain type. Every field has a specific type. It can be a simple type like a string, a numeric or
- `trendmicro-get-computer-group`: Get information of a certain computer group
- `trendmicro-modify-computer-group`: Modify the properties of a certain computer group
- `trendmicro-delete-computer-group`: Delete a certain computer group


## Tripwire

**Type:** integration  
**Product:** Tripwire  

Tripwire is a file integrity management (FIM), FIM monitors files and folders on systems and is triggered when they have changed. This integration was integrated and tested with v1 of Tripwire

**Commands:**

- `tripwire-versions-list`: Returns all Element Versions that meet the search critiera.
- `tripwire-rules-list`: Returns a list of all rules or those that match the provided filter criteria.
- `tripwire-elements-list`: Returns a list of all elements or those that match the provided criteria.
- `tripwire-nodes-list`: Returns a list of all nodes or those that match the provided filter criteria.


## TrustwaveFusion

**Type:** integration  
**Product:** Trustwave Fusion  

The Trustwave Fusion platform connects your organization’s digital footprint to a robust security cloud comprised of the Trustwave data lake, advanced analytics, actionable threat intelligence and a wide range of Trustwave services including Trustwave SpiderLabs , elite team of security specialists. Your team will benefit from deep visibility and the advanced security expertise necessary for protecting assets and eradicating threats as they arise. This integration was integrated and tested with version 1.0.68 of TrustwaveFusion

**Commands:**

- `trustwave-get-ticket`: Get a single ticket
- `trustwave-search-tickets`: Search tickets
- `trustwave-add-ticket-comment`: Add a comment to a ticket
- `trustwave-close-ticket`: Close a ticket
- `trustwave-get-updated-tickets`: Get updated tickets.
- `trustwave-search-findings`: Search for Findings
- `trustwave-get-finding`: Get a Finding
- `trustwave-get-asset`: Get an Asset
- `trustwave-search-assets`: Search for Assets


## Tufin

**Type:** integration  
**Product:** Tufin  
**Commands:**

- `tufin-search-topology`: Search the Tufin Topology Map
- `tufin-search-topology-image`: Search the Tufin Topology Map, returning an image
- `tufin-object-resolve`: Resolve IP address to Network Object
- `tufin-policy-search`: Search the policies of all devices managed by Tufin
- `tufin-get-zone-for-ip`: Match the IP address to the assigned Tufin Zone
- `tufin-submit-change-request`: Submit a change request to SecureChange
- `tufin-search-devices`: Search SecureTrack devices
- `tufin-get-change-info`: Get information on a SecureChange Ticket (Ticket ID retrieved from Tufin UI)
- `tufin-search-applications`: Search SecureApp applications
- `tufin-search-application-connections`: Get SecureApp application connections


## Tufin - Enrich IP Address(es)

**Type:** playbook  
**Product:** Tufin  

Enrich an IP using SecureTrack. Returns information such as the associated zones, network objects and policies for the address, and if the address is network device

**Inputs:**

- `IP`: IP address to enrich (ex: 192.168.1.1)


## Tufin - Enrich Source & Destination IP Information

**Type:** playbook  
**Product:** Tufin  

Enrich source and destination IP information using SecureTrack. Returns information such as the associated zones, network objects and policies for the addresses, if the addresses are network devices, and a topology map from source to destination

**Inputs:**

- `SourceIP`: Source IP address, including subnet mask (ex: 192.168.1.1/32)
- `DestinationIP`: Destination IP address, including subnet mask (ex: 192.168.1.1/32)


## Tufin - Get Application Information from SecureApp

**Type:** playbook  
**Product:** Tufin  

Search SecureApp by application name and retrieve basic application information and all application connections

**Inputs:**

- `ApplicationName`: Name of the application to query


## Tufin - Get Network Device Info by IP Address

**Type:** playbook  
**Product:** Tufin  

Use a device's IP address to gather information about the device, including basic device information, USP zone(s), and policies related to the device

**Inputs:**

- `DeviceIP`: IP address of the network device (ex: 192.168.1.1)


## Twinwave

**Type:** integration  
**Product:** Twinwave  

TwinWave analyzes URLs and files to detect credential phishing and malware threats. Supported the platform.8.0 and later

**Commands:**

- `twinwave-submit-url`: Submit New URL for Scanning.
- `twinwave-submit-file`: Submit File for Scanning.
- `twinwave-resubmit-job`: Resubmit a Job
- `twinwave-get-job-summary`: Get Job Summary
- `twinwave-wait-job`: Wait for a Twinwave job to complete and return its final summary and score. This command uses polling and requires the platform.2.0 or later.
- `twinwave-download-job-pdf`: Download a completed job's PDF report to the War Room.
- `twinwave-get-job-normalized-forensics`: Get a Job's Normalized Forensics
- `twinwave-get-task-normalized-forensics`: Get a Task's Normalized Forensics
- `twinwave-get-task-raw-forensics`: Get a Task's Raw Forensics
- `twinwave-download-submitted-resource`: Download the Submitted Resource.
- `twinwave-get-engines`: List Available Engines
- `twinwave-search-across-jobs-and-resources`: Search Across Jobs and Resources
- `twinwave-get-temp-artifact-url`: Get a Temporary Artifact URL


## Twitter v2

**Type:** integration  
**Product:** Twitter  

Twitter integration provides access to searching recent Tweets (in last 7 days) and user information using the Twitter v2 API. This integration was integrated and tested with version v2 of Twitter API. Some changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

**Commands:**

- `twitter-tweet-search`: This command will search for Tweets from the last 7 days and return all information available.
- `twitter-user-get`: Lookup users by name to display information about them. Search multiple users simultaneously by separating them by commas. Ex: 'name='user1,user2,user3'


## TypeSafe Jev

**Type:** integration  
**Product:** TypeSafe Jev  

Use TypeSafe Jev typed judgments and calibrated probabilities in Cortex XSIAM and platform playbooks

**Commands:**

- `jev-evaluate`: Evaluate a state against one or more typed TypeSafe questions in a single request.
- `jev-noul`: Evaluate one yes/no judgment and return the probability that the answer is yes.
- `jev-choice`: Select one option from a defined set and return the complete probability distribution.
- `jev-score`: Score state against ordered levels and return the weighted score and probability distribution.
- `jev-list-models`: List model aliases available to the configured TypeSafe account.


## UltraMSG

**Type:** integration  
**Product:** UltraMSG  

This is the UltraMSG integration for getting started made by Trustnet

**Commands:**

- `send-whatsapp`: Send WhatsApp Message


## Unblock Indicator - Infoblox NIOS

**Type:** playbook  
**Product:** Infoblox NIOS  

This playbook unblocks the given Indicator by deleting its RP Zone rule from Infoblox NIOS platform

**Inputs:**

- `indicator`: The indicator to unblock.
- `target_rp_zone`: The target Response Policy Zone.


## Uncover Unknown Malware Using SSDeep

**Type:** playbook  
**Product:** Uncover Unknown Malware Using SSDeep  

This playbook leverages the case management and TIM aspects of platform to uncover unknown malware. The playbook does the following: These steps allow the analyst to find new files, incidents and endpoints which could be related to the the original hash that was searched simply based on the similarity of SSDeep hashes

**Inputs:**

- `fileHash`: The file hash to hunt for. Supported hash types are MD5 and SHA256.
- `SimilarityThreshold`: SSDeep hashes with a similarity value equal to or greater than the value specified, will be considered as similar hashes.The SSDeep hashes a
- `SearchFromDate`: When looking for existing hashes in the system, this is the date that it will look for hashes from.The value should be in YYYY-MM-DDTHH:MM:S
- `EnrichExistingIndicators`: Whether indicators found in platform will be enriched using the enrichIndicators command. Note: this may use up quota in your threat intelli


## UnEscapeIPs

**Type:** script  
**Product:** Common Scripts  

Removes escaping chars from IP addresses. For Example, "127[.]0[.]0[.]1 -> 127.0.0.1"

**Inputs:**

- `input`: The IP(s) address(es) to unescape.


## UnEscapeURLs

**Type:** script  
**Product:** Common Scripts  

Extracts URLs redirected by security tools like Proofpoint, and changes " ->  Also, this will un-escape URLs that are escaped for safety with formats such as "hxxps://www[.]platform[.]com"

**Inputs:**

- `input`: The URL(s) to process.


## Unisys Stealth

**Type:** integration  
**Product:** Unisys Stealth  

This integration is intended to aid companies in integrating with the Stealth EcoAPI service. Using the included commands, security teams can trigger dynamically isolation of users or endpoints from the rest of the Stealth network

**Commands:**

- `stealth-isolate-machine`: This is the command which will isolate an endpoint from the Stealth Network
- `stealth-unisolate-machine`: This is the command which will un-isolate an endpoint from Stealth Network
- `stealth-get-stealth-roles`: Retrieve roles from Stealth Network
- `stealth-isolate-user`: This is the command which will isolate an user from the Stealth Network
- `stealth-unisolate-user`: This is the command which will un-isolate an user from Stealth Network
- `stealth-isolate-machine-and-user`: This is the command which will isolate an endpoint and user from the Stealth Network
- `stealth-unisolate-machine-and-user`: This is the command which will un-isolate an endpoint and user from Stealth Network


## UnitTest

**Type:** script  
**Product:** Content Testing  

Provides for automated testing of automations, playbooks, and sub-playbooks

**Inputs:**

- `playbook`: Playbook to Execute.
- `addAfter`: Playbook Task to Add This Task After.
- `testType`: Type of Test to Run.
- `listName`: List to Read Subplaybooks or Automations From.


## UnitTestCase

**Type:** script  
**Product:** Content Testing  
**Inputs:**

- `testName`: Test Case Name
- `listName`: List to Read Test Case From
- `addAfter`: Task in Playbook to Add Test Case After


## UnitTestCasePrep

**Type:** script  
**Product:** Content Testing  
**Inputs:**

- `testName`: Test Case Name
- `listName`: List to Read Test Case From


## UnitTestLoadContextList

**Type:** script  
**Product:** Content Testing  
**Inputs:**

- `list`: List to Load Context From


## UnitTestLoadFieldsList

**Type:** script  
**Product:** Content Testing  
**Inputs:**

- `list`: List to Load Incident Fields From


## UnitTestPlaybookAnalyzer

**Type:** script  
**Product:** Content Testing  

Profiles execution time of tasks in a playbook or sub-playbook (if specified). Provides minimum, maximum, and average task execution times in milliseconds as well as the state of each task: completed, error, notexecuted, started, and waiting

**Inputs:**

- `playbook`: Name of the playbook to analyze.
- `subplaybook`: Sub-playbook for analysis versus the parent playbook.
- `firstday`: First day to find incident occurrences using the playbook. Example: "2023-03-01".
- `lastday`: Last day to find incident occurrences using the playbook: Example: "2023-03-31".
- `maxinc`: Maximum number of incidents to analyze.


## UnitTestResults

**Type:** script  
**Product:** Content Testing  
**Inputs:**

- `cmds`: Arrary Of Commands Executed
- `tasks`: Array of Tasks Names
- `gridfield`: Field Name to Store Data In
- `status`: Result of the Command (true, false)


## UnitTestTopLevel

**Type:** playbook  
**Product:** Content Testing  

## UnPackFile

**Type:** script  
**Product:** Common Scripts  

Unpacks a file using the fileName or entryID to specify a file. Files unpacked will be pushed to the War Room and names will be pushed to the context. Supported types include, 7z (.7z), ACE (.ace), ALZIP (.alz), AR (.a), ARC (.arc), ARJ (.arj), BZIP2 (.bz2), CAB (.cab), compress (.Z), CPIO (.cpio), DEB (.deb), DMS (.dms), GZIP (.gz), LRZIP (.lrz), LZH (.lha, .lzh), LZIP (.lz), LZMA (.lzma), LZOP (.lzo), RPM (.rpm), RAR (.rar), RZIP (.rz), TAR (.tar), XZ (.xz), ZIP (.zip, .jar) and ZOO (.zoo)

**Inputs:**

- `fileName`: The name of the file to unpack.
- `entryID`: The entry ID of the attached packed file in the War Room.
- `lastPackedFileInWarroom`: The packaged file extension in the set to look for the last of its kind in the War Room.


## unshortenMe

**Type:** integration  
**Product:** UnshortenMe  
**Commands:**

- `unshorten-me-unshorten-url`: Unshortens a given URL.


## UnzipFile

**Type:** script  
**Product:** Common Scripts  

Unzip a file using fileName or entryID to specify a file. Unzipped files will be loaded to the War Room and names will be put into the context

**Inputs:**

- `fileName`: The file name.
- `password`: Password to protect the ZIP file.
- `nonsensitive_password`: Password to protect the ZIP file, inserted as a non sensative argument.
- `entryID`: The entry ID of the attached ZIPp file in the War Room.
- `lastZipFileInWarroom`: Enter 'yes' (or any other value) if the ZIP file is last ZIP file in the War Room.
- `zipTool`: Tool to extract zip


## UnzipGZFile

**Type:** script  
**Product:** GZip  

Unzip a gz file and upload to war room

**Inputs:**

- `entryID`: CSV list of entry ids for the gzipped files to unzip.


## Update Incident Status And Fetch Attachments - Securonix

**Type:** playbook  
**Product:** Securonix  

This playbook fetches the attachments for the incident. Also, it updates the state of the Securonix incident based on the configuration provided in integration configuration


## Update Live Briefs - Dataminr Pulse

**Type:** playbook  
**Product:** Dataminr Pulse  

This playbook will update the previously fetched Dataminr Pulse ReGenAI incidents with the latest briefs

**Inputs:**

- `number_of_incidents_to_update`: Provide the number of incidents you want to update with the latest Live Brief.


## Upload Vulnerability Report to Automox

**Type:** playbook  
**Product:** Automox  

This sub-playbook takes the entryId of a vendor-generated vulnerability report CSV and uploads it to Automox for remediation. Information about supported CSV formats can be found in the Automox Support Documentation

**Inputs:**

- `entry_id`: The entryId of a vendor-generated vulnerability report.


## Uptycs

**Type:** integration  
**Product:** Uptycs  
**Commands:**

- `uptycs-get-assets`: return assets enrolled with Uptycs
- `uptycs-run-query`: enter a SQL query to run against your Uptycs database. A list of tables can be found at osquery.io/schema, or by using the query "select * from information_sche
- `uptycs-get-alerts`: return alerts from Uptycs DB
- `uptycs-get-alert-rules`: retrieve a list of alert rules
- `uptycs-get-event-rules`: retrieve a list of event rules
- `uptycs-get-events`: return events from Uptycs DB
- `uptycs-get-process-open-sockets`: find processes which opened a socket
- `uptycs-get-process-information`: get information for a particular process
- `uptycs-get-process-child-processes`: get all the child processes for a given parent process
- `uptycs-get-processes`: find processes which are running or have run on a registered Uptycs asset
- `uptycs-get-process-open-files`: find processes which have opened files
- `uptycs-set-alert-status`: Set the status of an alert to new, assigned, resolved, or closed
- `uptycs-set-asset-tag`: Sets a tag on a particular asset
- `uptycs-get-user-information`: get info for an Uptycs user
- `uptycs-get-threat-indicators`: get Uptycs threat indicators


## Uptycs - Bad IP Incident

**Type:** playbook  
**Product:** Uptycs  

Gets information about processes which open connections to known bad IP addresses

**Inputs:**

- `alert_id`: The unique Uptycs ID for a particular alert.


## Uptycs - Outbound Connection to Threat IOC Incident

**Type:** playbook  
**Product:** Uptycs  

Gets information about connections from IOC incidents

**Inputs:**

- `alert_id`: The unique Uptycs ID for a particular alert.


## url-enrichment

**Type:** script  
**Product:** Aggregated Scripts  

Enriches URL indicators with reputation data from multiple integrations and outputs a consolidated URLEnrichment object. This script exclusively supports indicators of type URL and will automatically create the indicator in TIM if it is not already exists. Note: This script is supported in the platform.0 and later, and in Cortex XSIAM

**Inputs:**

- `url_list`: Accepts a list of URLs to enrich.- From CLI: Provide a comma-separated list. If a URL contains a comma, wrap the URLs in a JSON array. Examp
- `external_enrichment`: Whether to call external integrations for enrichment: - 'true': enrich using enabled external integrations (e.g., VirusTotal (API v3), Alien
- `verbose`: Retrieve a human-readable entry for each command; if false, only the final result is summarized and errors are suppressed.
- `brands`: A list of integration brands to run enrichment against. Example: `"VirusTotal (API v3), AlienVault OTX v2"`. - If provided, only the selecte
- `additional_fields`: When set to true, the output includes an `AdditionalFields` objectfor each of the indicator result. `AdditionalFields` contains all fields r


## URLDecode

**Type:** script  
**Product:** Filters And Transformers  

Converts "https:%2F%2Fexample.com" into "

**Inputs:**

- `value`: The URL to input.


## URLEncode

**Type:** script  
**Product:** Filters And Transformers  

Encodes a URL string by replacing special characters in the string using the %xx escape. For example:  converts to https:%2F%2Fexample.com

**Inputs:**

- `value`: The URL to encode.


## URLhaus

**Type:** integration  
**Product:** URLhaus  

URLhaus leverages abuse.ch and shares malicious URLs that are being used for malware distribution. This integration was integrated and tested with version v1 of URLhaus

**Commands:**

- `url`: Retrieves URL information from URLhaus.
- `domain`: Retrieves domain information from URLhaus.
- `file`: Retrieves file information from URLhaus.
- `urlhaus-download-sample`: Downloads a malware sample from URLhaus.


## URLNumberOfAds

**Type:** script  
**Product:** Common Scripts  

Fetches the numbers of ads in the given URL

**Inputs:**

- `url`: The URL to load and count ads on.
- `easylist`: The optional easylist to get ads from.


## URLReputation

**Type:** script  
**Product:** Common Scripts  

A context script for URL entities

**Inputs:**

- `url`: The URL to look up.


## UrlscanGetHttpTransactions

**Type:** script  
**Product:** URLScan.io  

Gets the HTTP transactions made for a given URL using the URLScan integration. To use this script properly, go to the Advanced section in the task that executes this script, and check the Run without a worker checkbox. The system will use less resources for the polling action

**Inputs:**

- `url`: The URL to search the transaction list for.
- `wait_time_for_polling`: The wait time between two polling actions (in Seconds) of the URLScan results page. A rate-limit error may occure if the time value is set t
- `timeout`: The amount of seconds to wait for the scan ID result.
- `limit`: The limit of the results in the War Room. The maximum limit allowed is 100.


## URLSSLVerification

**Type:** script  
**Product:** Common Scripts  

Verifies the URL's/URL redirect chain for SSL certificate

**Inputs:**

- `url`: Comma separated list of URLs to verify.


## USTA

**Type:** integration  
**Product:** USTA  

USTA is an Cyber Intelligence Platform that responds directly and effectively to today's complex cyber threats

**Commands:**

- `usta-get-malicious-urls`: You can get malicious URLs with this command
- `usta-get-phishing-sites`: You can get phishing sites with this command
- `usta-get-stolen-client-accounts`: You can access stolen customer accounts via Stolen-Client-accounts API.
- `usta-get-ip-address`: If you want to get more detailed information about specific IP Address, you can use this command.
- `usta-search-specific-identity-leaks`: With this command, you can search specific identity number that hashed in leaks


## UtilAnyResults

**Type:** script  
**Product:** Common Scripts  

Utility script to use in playbooks. This will return "yes" if the input is not empty

**Inputs:**

- `data`: The data to check. Can be, a list or a string. Strings containing only commas will be considered empty.


## Varonis Data Security Platform

**Type:** integration  
**Product:** Varonis Data Security Platform  

Streamline alerts and related forensic information from Varonis DSP This integration was integrated and tested with version 1.0 of VaronisDataSecurityPlatform

**Commands:**

- `varonis-get-alerts`: Get alerts from Varonis DA
- `varonis-update-alert-status`: Update alert status
- `varonis-close-alert`: Close the alert
- `varonis-get-alerted-events`: Get events applied to specific alerts


## Varonis SaaS

**Type:** integration  
**Product:** Varonis SaaS  

Streamline alerts and related forensic information from Varonis SaaS

**Commands:**

- `varonis-get-threat-models`: Get Varonis threat models
- `varonis-get-alerts`: Get alerts from Varonis DA
- `varonis-get-alerted-events`: Get events applied to specific alerts
- `varonis-alert-add-note`: Add note to alerts
- `varonis-update-alert-status`: Update alert status
- `varonis-close-alert`: Close the alert
- `get-mapping-fields`: Returns the list of fields to map in outgoing mirroring. This command is only used for debugging purposes.


## varonis-alert-post-processing

**Type:** script  
**Product:** Varonis SaaS  

Varonis alert post processing script to set the alert status in platform to closed when an incident is closed


## Vectra Detect

**Type:** integration  
**Product:** Vectra AI  

This integration allows to create incidents based on Vectra Accounts/Hosts/Detections objects. This integration was integrated and tested with version 7.1 of Vectra Detect

**Commands:**

- `vectra-search-accounts`: Returns a list of Account objects. All search attributes will be cumulative unless you're using the search_query_only one, in that case, only this one will be t
- `vectra-search-hosts`: Returns a list of Host objects. All search attributes will be cumulative unless you're using the search_query_only one, in that case, only this one will be take
- `vectra-search-detections`: Returns a list of Detection objects. All search attributes will be cumulative unless you're using the search_query_only one, in that case, only this one will be
- `vectra-search-assignments`: Return a list of assignments. By default already resolved assignment are not returned.
- `vectra-search-users`: Returns a list of Vectra Users. All search attributes will be cumulative.
- `vectra-search-outcomes`: Returns a list of assignment outcomes.
- `vectra-account-describe`: Returns a single Account details
- `vectra-account-add-tags`: Add tags to an Account
- `vectra-account-del-tags`: Delete tags from an Account
- `vectra-account-tag-list`: Returns a list of tags for a specified account.
- `vectra-account-note-add`: Add a note to the account.
- `vectra-account-note-update`: Update a note in the account.
- `vectra-account-note-remove`: Remove a note from the account.
- `vectra-account-note-list`: List all notes of the specific account.
- `vectra-account-markall-detections-asfixed`: Mark active detections as fixed by providing the ID of the account in the argument.


## Vectra RUX - Network Detection & Response

**Type:** integration  
**Product:** Vectra RUX  

This integration allows the security operations center to create and manage incidents based on Vectra Events Detections. This integration was integrated and tested with Vectra API v3.5

**Commands:**

- `vectra-detections-mark-asclosed`: Mark detections as closed with provided detection IDs in the argument.
- `vectra-user-list`: Returns a list of users.
- `vectra-entity-list`: Returns a list of entities.
- `vectra-entity-describe`: Describes an entity by ID.
- `vectra-entity-detection-list`: Returns a list of detections for a specified entity.
- `vectra-detection-describe`: Returns a list of detections for the specified detection ID(s).
- `vectra-entity-note-add`: Add a note to the entity.
- `vectra-entity-note-update`: Update a note in the entity.
- `vectra-entity-note-remove`: Remove a note from the entity.
- `vectra-entity-tag-add`: Add tags in the entity.
- `vectra-entity-tag-remove`: Remove tags from the entity.
- `vectra-entity-tag-list`: Returns a list of tags for a specified entity.
- `vectra-entity-assignment-add`: Add an assignment for the entity.
- `vectra-entity-assignment-update`: Update an assignment in the entity.
- `vectra-detection-pcap-download`: Download pcap of the detection.


## Vectra XDR

**Type:** integration  
**Product:** Vectra XDR  
**Commands:**

- `vectra-user-list`: Returns a list of users.
- `vectra-entity-list`: Returns a list of entities.
- `vectra-entity-describe`: Describes an entity by ID.
- `vectra-entity-detection-list`: Returns a list of detections for a specified entity.
- `vectra-detection-describe`: Returns a list of detections for the specified detection ID(s).
- `vectra-entity-note-add`: Add a note to the entity.
- `vectra-detection-note-add`: Add a note to the detection.
- `vectra-entity-note-update`: Update a note in the entity.
- `vectra-detection-note-update`: Update a note in the detection.
- `vectra-entity-note-remove`: Remove a note from the entity.
- `vectra-detection-note-remove`: Remove a note from the detection.
- `vectra-detections-mark-fixed`: Mark detection as fixed with provided detection IDs in argument.
- `vectra-detections-unmark-fixed`: Unmark detection as fixed with provided detection IDs in argument.
- `vectra-entity-tag-add`: Add tags in the entity.
- `vectra-entity-tag-remove`: Remove tags from the entity.


## VectraDetectCloseDuplicateIncidents

**Type:** script  
**Product:** Vectra AI  

This script closes duplicate incidents in platform while resolving the assignment for the corresponding Vectra entity

**Inputs:**

- `page_size`: Specify the number of incidents to close during a single execution.
- `note`: The note to add to the closed incidents.
- `close_in_vectra`: If set to true, the script will close the entity's assignment in Vectra platform. This option is supported only when instance of Vectra Dete
- `incident_types`: Specify the incident type(s) to close duplicate incidents. Supports comma-separated values.


## VectraDetectDisplayDetections

**Type:** script  
**Product:** Vectra AI  

This script enables the display of detection details, available in the context, in the form of a markdown table


## VectraRUXGetIncidents

**Type:** script  
**Product:** Vectra RUX  

Get the incidents with the type Vectra RUX Events Detection

**Inputs:**

- `page`: Provide the page number. A single page has a maximum of 50 incidents.
- `incident_type`: The platform incident type to search for inactive detections. Default is 'Vectra RUX Events Detection'.


## VectraRUXLinkEntityDetections

**Type:** script  
**Product:** Vectra RUX  

Link the Detections which have the same entity ID

**Inputs:**

- `incident_entity_id`: Incident Entity ID.
- `incident_detection_id`: Incident Detection ID.


## VectraRUXSyncDetectionNotes

**Type:** script  
**Product:** Vectra RUX  

Sync the Detection Notes from the Vectra platform


## VectraRUXSyncDetectionSummary

**Type:** script  
**Product:** Vectra RUX  

Sync the detection summary from the Vectra platform


## VectraRUXSyncEntityAssignment

**Type:** script  
**Product:** Vectra RUX  

Sync Entity Assignment details from the Vectra platform


## VectraXDRDisplayEntityDetections

**Type:** script  
**Product:** Vectra XDR  

This script enables the display of detection details, available in the context, in the form of a markdown table


## VectraXDRSyncEntityAssignment

**Type:** script  
**Product:** Vectra XDR  

Sync Entity Assignment details from the Vectra platform


## VectraXDRSyncEntityDetections

**Type:** script  
**Product:** Vectra XDR  

Sync Entity detection details from the Vectra platform


## Vega

**Type:** integration  
**Product:** Vega  

Vega integration for fetching alerts and incidents from the Vega platform

**Commands:**

- `vega-get-alert-events`: Fetch aggregated alert events for up to 10 Vega alerts using internal API pagination, then return the requested display page as a markdown table and CustomField
- `vega-get-alert-metadata`: Return Vega alert metadata to the War Room. Pass one incident_id to load the alerts related to that Vega incident. When run from a Vega Incident without inciden
- `vega-set-detections-state`: Set the state for one or more Vega detections.
- `vega-update-detections`: Update severity, status, state, and/or tags for one or more Vega detections using the updateDetections GraphQL mutation.
- `vega-update-alert`: Immediately update Vega alert status, severity, verdict, verdict reasoning, assignees, and/or comment on the Vega platform and sync the open the platform.
- `vega-update-incident`: Immediately update Vega incident user status, verdict, verdict reasoning, severity, assignee emails, and/or comment on the Vega platform and sync the open the p
- `vega-reconcile-incidents`: Compare selected Vega alert and incident UUIDs with the platform. Only selected entities are queried. Paste the lists into a Vega instance that has Fetch alerts
- `get-remote-data`: Gets remote data from a remote Vega alert or incident. Used for debugging incoming mirroring.
- `get-modified-remote-data`: Gets Vega alert and incident IDs modified since the last update time. Used for debugging incoming mirroring.
- `update-remote-system`: Pushes the platform.
- `get-mapping-fields`: Returns the outgoing mirroring fields for Vega Alert and Vega Incident investigations.


## Vercara UltraDNS

**Type:** integration  
**Product:** Vercara UltraDNS  

This integration fetches DNS configuration audit logs from Vercara UltraDNS platform. This integration was integrated and tested with the 3.18.0 Vercara UltraDNS API

**Commands:**

- `vercara-ultradns-get-events`: Gets audit events from Vercara UltraDNS. Manual command to fetch and display events. This command is used for developing/debugging and is to be used with cautio


## VerdictResult

**Type:** script  
**Product:** Common Scripts  

This widget displays the incident verdict or the alert verdict based on the 'incident.verdict' or 'alert.verdict' field


## Versa Director

**Type:** integration  
**Product:** VersaDirector  

Versa Director is a virtualization and service creation platform that simplifies the design, automation, and delivery of SASE services. Versa Director provides the essential management, monitoring and orchestration capabilities needed to deliver all of the networking and security capabilities within Versa SASE. This integration was integrated and tested with version 1.0.0 of VersaDirector

**Commands:**

- `vd-auth-start`: Obtain an access token from the API client. If Client ID and Client Secret were not passed as parameters or arguments, a new Auth Client will be created.
- `vd-auth-test`: Run a connectivity test to verify that the OAuth process worked.
- `vd-predefined-application-list`: List all user predefined application objects.
- `vd-appliance-user-modified-application-list`: List all user modified predefined application objects associated with a specific organization and appliance (device).
- `vd-template-user-modified-application-list`: List all user modified predefined application objects associated with a specific organization and template.
- `vd-appliance-user-defined-application-list`: List all user defined application objects associated with a specific organization and appliance (device).
- `vd-template-user-defined-application-list`: List all user defined application objects associated with a specific organization and template.
- `vd-appliance-address-object-delete`: Delete an address object associated with a specific organization and appliance (device).
- `vd-appliance-address-object-edit`: Edit an address object associated with a specific organization and appliance (device).
- `vd-appliance-address-object-create`: Create an address object associated with a specific organization and appliance (device).
- `vd-appliance-address-object-list`: List all address objects associated with a specific organization and appliance (device).
- `vd-template-address-object-delete`: Delete an address object associated with a specific organization and template.
- `vd-template-address-object-edit`: Create an address object associated with a specific organization and template.
- `vd-template-address-object-create`: Create an address object associated with a specific organization and template.
- `vd-template-address-object-list`: List all address objects associated with a specific organization and template.


## Viper

**Type:** integration  
**Product:** Viper  

Viper is a binary analysis and management framework

**Commands:**

- `viper-download`: Download a sample with file hash
- `viper-search`: Search for sample with file hash


## VMRay

**Type:** integration  
**Product:** VMRay Analyzer  

This integration enables users to design playbooks that involve analyzing a file in VMRay and retrieving the analysis results and associated threat intelligence. The Playbooks accelerate incident response and make security operations more scalable and efficient

**Commands:**

- `vmray-upload-sample`: Submits a sample to VMRay for analysis.
- `vmray-upload-url`: Submits a URL for analysis.
- `vmray-get-analysis-by-sample`: Retrieves all analysis details for a specified sample.
- `vmray-get-job-by-sample`: Retrieves details for all jobs for a specified sample.
- `vmray-get-submission`: Retrieves the results of a submission.
- `vmray-get-sample`: Retrieves a sample using the sample ID.
- `vmray-get-sample-by-hash`: Retrieves sample information by hash.
- `vmray-get-threat-indicators`: Retrieves threat indicators (VTI).
- `vmray-add-tag`: Adds a tag to an analysis and/or a submission.
- `vmray-delete-tag`: Deletes tags from an analysis and/or a submission.
- `vmray-get-iocs`: Retrieves Indicators of Compromise for a specified sample.
- `vmray-get-job-by-id`: Retrieves a job by job ID.
- `vmray-get-summary`: Retrieves the Summary JSON v2 for a specific analysis.
- `vmray-get-screenshots`: Retrieves screenshots taken during a specific dynamic analysis. The screenshots are stored with file names like 'analysis_5_screenshot_2.png'. In this example, 
- `vmray-get-license-usage-verdicts`: Gets the usage of verdicts from VMRay.


## VMware

**Type:** integration  
**Product:** VMware  

VMware vCenter server is a centralized management application that lets you manage virtual machines and ESXi hosts centrally. This integration was integrated and tested with version 7.03 of VMware

**Commands:**

- `vmware-get-vms`: Returns all virtual machines on a system.
- `vmware-poweron`: Powers on a powered-off or suspended virtual machine.
- `vmware-poweroff`: Powers off a powered-on or suspended virtual machine.
- `vmware-hard-reboot`: Reboots a powered-on virtual machine.
- `vmware-suspend`: Suspends a powered-on virtual machine.
- `vmware-soft-reboot`: Issues a command to the guest operating system asking it to perform a reboot.
- `vmware-create-snapshot`: Creates a VM snapshot.
- `vmware-revert-snapshot`: Reverts VM to snapshot.
- `vmware-get-events`: Gets events of a VM.
- `vmware-change-nic-state`: Changes the state of a VM NIC.
- `vmware-list-vms-by-tag`: Lists all virtual storage objects attached to the tag.
- `vmware-create-vm`: Creates a new virtual machine in the current folder and attaches it to the specified resource pool. This operation creates a virtual machine, instead of cloning
- `vmware-clone-vm`: Creates a clone of this virtual machine. If the virtual machine is used as a template, this method corresponds to the deploy command.
- `vmware-relocate-vm`: Relocates a virtual machine to a specified location.
- `vmware-delete-vm`: Destroys this object, deleting its contents and removing it from its parent folder (if any).


## VMware Workspace ONE UEM (AirWatch MDM)

**Type:** integration  
**Product:** VMware Workspace ONE UEM  

VMware Workspace ONE UEM integration allows users to search enrolled corporate or employee-owned devices, provides detailed information about each device such as its serial number, installed OS's, pending OS updates, network details, and much more leveraging Workspace ONE UEM's (formerly AirWatch MDM) API. This integration was integrated and tested with version 21.5.0.4 of VMware Workspace ONE UEM (AirWatch MDM)

**Commands:**

- `vmwuem-devices-search`: Searches device(s) using the query information provided.
- `vmwuem-device-get`: Get basic information about the device.
- `vmwuem-device-os-updates-list`: Retrieves a list of all available OS and software updates for the specified device.


## WALLIX Bastion

**Type:** integration  
**Product:** WALLIX Bastion  

Centralized Control and Monitoring of Privileged Access to Sensitive Assets. This integration was integrated and tested with version 12 of WALLIX Bastion

**Commands:**

- `wab-add-session-target-to-target-group`: Add a target account to a target group
- `wab-add-password-target-to-target-group`: Add a password checkout account to a target group
- `wab-add-restriction-to-target-group`: Add a restriction in a targetgroup category: Target Group Restrictions.
- `wab-add-timeframe-period`: Add a period to a timeframe category: Timeframes.
- `wab-add-global-domain`: Add a global domain category: Domains
- `wab-get-account-references`: Get account references category: Account References
- `wab-get-account-reference`: Get account reference category: Account References
- `wab-change-password-or-ssh-key-of-account`: Change password or SSH key of an account and propagate changes on the target host. If the body is empty, an automatic password change is performed: the password
- `wab-get-all-accounts`: Get all accounts category: Accounts
- `wab-get-one-account`: Get one account category: Accounts
- `wab-delete-account`: Delete an account category: Accounts
- `wab-get-application-account-credentials`: Get the application account credentials category: Application Account Credentials
- `wab-add-credential-to-application-account`: Add a credential to an application account on a local domain category: Application Account Credentials
- `wab-get-application-account-credential`: Get the application account credential category: Application Account Credentials
- `wab-edit-credential-of-application-account`: Edit a credential of an application account on a local domain category: Application Account Credentials


## Web File Repository

**Type:** integration  
**Product:** Web File Repository  

Simple web server with a file uploading console to store small files. Helps make your environment ready for testing purpose for your playbooks or automations to download files from a web server. NOTE: For more information about long-running integrations, see the the platform, the platform

**Commands:**

- `wfr-status`: Get the service status
- `wfr-cleanup`: Remove all the files from the repository
- `wfr-upload-as-file`: Upload a file from data to the repository.
- `wfr-upload-file`: Upload a file to the repository
- `wfr-upload-files`: Upload files to the repository
- `wfr-list-files`: List files in the repository
- `wfr-remove-files`: Remove files from the repository
- `wfr-download-file`: Download a file from the repository
- `wfr-download-as-text`: Retrieve the file data from the repository into the context.
- `wfr-archive-zip`: Download a file to which all the files are archived
- `wfr-reset`: Reset the repository data


## WebScraper

**Type:** script  
**Product:** Web Scraper  

An Automation Script to Web Scrap a URL or HTML Page

**Inputs:**

- `page_url`: Page url to scrap
- `page_html`: HTML page to scrap
- `headers`: Request headers
- `params`: Request parameters
- `navigator_tree`: HTML tags navigation tree, example: "body.table"
- `insecure`: Ignore certificate validation errors


## WhereFieldEquals

**Type:** script  
**Product:** Filters And Transformers  

Returns all items from the list where their given field attribute is equal to the equalTo argument. For example, !WhereFieldEquals with the following arguments: This will return all item names where field type equals IP - ['192.1,0.82', '172.0.0.2']

**Inputs:**

- `value`: The list to apply the transformer to.
- `field`: The attribute in the collection items to check equality against equalTo.
- `equalTo`: The value to filter all items by in the collection.
- `getField`: The field to extract from each item (Optional).
- `stringify`: Whether the argument should be saved as a string (Optional).


## WhisperGate and HermeticWiper & CVE-2021-32648

**Type:** playbook  
**Product:** WhisperGate and HermeticWiper & CVE-2021-32648  

CVE-2021-32648 vulnerability has a CVSS score of 9.1 and was found in octobercms, which is a CMS platform based on the Laravel PHP Framework. In affected versions of the october/system package an attacker can request an account password reset and then gain access to the account using a specially crafted request. The issue has been patched in Build 472 and v1.1.5. The playbook includes the following tasks: Mitigations: More information: UNIT42 Blog - Ongoing Russia and Ukraine Cyber Conflict Russia-Ukraine Cyberattacks: How to Protect Against Related Cyberthreats Including DDoS, HermeticWiper, Gamaredon and Website Defacement Microsoft Blog CVE-2021-32648 NVD Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `PlaybookDescription`: The playbook description for Rapid Breach Response layout.
- `BlockIndicatorsAutomatically`: Whether to block the indicators automatically or not.
- `CollectedIndicatorsSeverity`: The verdict of the collected indicators. Default is "Malicious". Other options can be "Suspicious" and "Unknown".
- `RelatedCVE`: The WhisperGate malware related CVE.
- `RunXQLHuntingQueries`: Whether to perform XQL hunting queries. Default is "False".
- `UserVerification`: Possible values: True/False.\nWhether to provide user verification for blocking IPs. \n\nFalse - No prompt will be displayed to the user.\nT
- `AutoBlockIndicators`: Should the given indicators be automatically blocked, or should the user be given the option to choose?If set to True - no prompt will appea


## Whois

**Type:** integration  
**Product:** Whois  

Provides data enrichment for domains. This integration was integrated and tested with version 1.0 of Whois

**Commands:**

- `whois`: Provides data enrichment for domains. This pack relies on free services for WHOIS information. As with many free services, the availability is not guaranteed. F
- `domain`: Provides data enrichment for domains.
- `ip`: Provides data enrichment for ips.


## WidgetNoOp

**Type:** script  
**Product:** Common Widgets  

A no-op placeholder script used by visual-only widgets (e.g. Page Break, Text Widget) that require a script dataType but do not need to query any data source. Returns a mock result to prevent unnecessary database queries


## WildFire Malware

**Type:** playbook  
**Product:** Core  

This playbook handles WildFire Malware alerts. It performs enrichment on the different alert entities and establishes a verdict. For a possible true positive alert, the playbook performs further investigation for related IOCs and executes a containment plan

**Inputs:**

- `sha256`: The SHA256 hash of the suspected file. Decided by the DT expression wether it's the initiator or the target file SHA256.
- `GraywarePhishingAsMalware`: Whether to treat grayware and phishing alerts as malware.
- `AutoContainment`: Whether to execute the containment plan (except isolation) automatically.The specific containment playbook inputs should also be set to 'Tru
- `HostAutoContainment`: Whether to automatically execute endpoint isolation in case there are investigation findings.
- `BlockIndicators`: Set to True if you want to block the indicators.
- `OriginalFileContainment`: Set to True if you want to quarantine the original malicious file.
- `RelatedFileContainment`: Set to True to quarantine the identified files found in the investigation.
- `FileRemediation`: Choose 'Quarantine' or 'Delete' to avoid file remediation conflicts. For example, choosing 'Quarantine' ignores the 'Delete file' task under


## Wiz

**Type:** integration  
**Product:** Wiz  

Agentless, context-aware and full-stack security and compliance across AWS, Azure, GCP, OCI, Kubernetes, and other supported cloud platforms. This integration was integrated and tested with Wiz

**Commands:**

- `wiz-get-issue`: Get the details for a Wiz Issue ID.
- `wiz-get-issues`: Get the issues on cloud resources.
- `wiz-get-resource`: Get Details of a resource. You should pass exactly one of resource_id, resource_name. When searching by name, results are limited to 500 records.
- `wiz-get-resources`: Get details of multiple resources based on various filters.
- `wiz-issue-in-progress`: Set a Wiz Issue to in progress.
- `wiz-reopen-issue`: Re-open an Issue.
- `wiz-reject-issue`: Reject a Wiz Issue. Not supported for THREAT_DETECTION issues.
- `wiz-resolve-issue`: Resolve a Wiz Issue.
- `wiz-set-issue-note`: Set (append) a note to an Issue.
- `wiz-clear-issue-note`: Clears a note from an Issue.
- `wiz-get-issue-evidence`: Get the evidence from an Issue.
- `wiz-rescan-machine-disk`: Deprecated
- `wiz-set-issue-due-date`: Set a due date for an Issue.
- `wiz-clear-issue-due-date`: Clear a due date for an Issue.
- `wiz-get-project-team`: Get the Project Owners and Security Champions details.


## WizDefend

**Type:** integration  
**Product:** Wiz  

Agentless cloud security platform for detecting and addressing cloud issues, detections, and threats

**Commands:**

- `wiz-defend-get-detections`: Retrieve Wiz security detections based on specified filters.
- `wiz-defend-get-detection`: Retrieve detailed information about a specific Wiz detection by ID.
- `wiz-defend-get-threat`: Retrieve detailed information about a specific Wiz threat by issue ID.
- `wiz-defend-get-threats`: Retrieve Wiz threats based on specified filters.
- `wiz-defend-reopen-threat`: Reopen a Wiz Threat.
- `wiz-defend-resolve-threat`: Resolve a Wiz Threat.
- `wiz-defend-set-threat-in-progress`: Set a Wiz Threat to in progress.
- `wiz-defend-set-threat-comment`: Set a comment on a Wiz Threat.
- `wiz-defend-clear-threat-comments`: Clear all the comments from a Wiz Threat.


## Wolken ITSM

**Type:** integration  
**Product:** Wolken ITSM  

Use The Wolken IT Service Management (ITSM) solution to modernize the way you manage and deliver services to your users. This integration was integrated and tested with version 1.0.0 of Wolken ITSM

**Commands:**

- `wolken-add-internal-notes`: Used to add Internal Notes in the specified incident
- `wolken-get-access-token`: Use to get access token and save it in integration context . Refresh Token saved in integration context will be used to create new access token after expiration
- `wolken-post-api-v1-incidents-add-attachments`: Add Attachment to the specified Incident Id using entry Id
- `wolken-post-api-v1-incidents-by-incident-id`: Update an existing incident
- `wolken-put-api-v1-incidents-cancel`: Cancel an Incident


## Wordpress

**Type:** integration  
**Product:** Wordpress  

The WordPress REST API provides an interface for applications to interact with your WordPress site by sending and receiving data as JSON (JavaScript Object Notation) objects. It is the foundation of the WordPress Block Editor, and can likewise enable your theme, plugin or custom application to present new, powerful interfaces for managing and publishing your site content. This integration was integrated and tested with version 5.6 of Wordpress

**Commands:**

- `wordpress-url-request`: Get information from a custom URL
- `wordpress-list-posts`: Lists all posts
- `wordpress-get-post`: Retrieve a specific post record.
- `wordpress-create-post`: Create a post
- `wordpress-update-post`: Update a post
- `wordpress-delete-post`: Delete a post
- `wordpress-list-categories`: List categories
- `wordpress-create-category`: Create a category
- `wordpress-get-category`: Retrieve a category
- `wordpress-update-category`: Update a category
- `wordpress-delete-category`: Delete a category
- `wordpress-list-tags`: Lists all tags
- `wordpress-create-tag`: Create a tag
- `wordpress-get-tag`: Retrieves a tag
- `wordpress-update-tag`: Update a tag


## Workday

**Type:** integration  
**Product:** Workday  

Workday offers enterprise-level software solutions for financial management, human resources, and planning. This integration was integrated and tested with version 47.0 of Workday

**Commands:**

- `workday-list-workers`: List workers command - Returns information for specified workers.


## Workday IAM

**Type:** integration  
**Product:** Workday  

Use the Workday IAM Integration as part of the IAM premium pack. For more information, please refer to the Identity Lifecycle Management article

**Commands:**

- `workday-iam-get-full-report`: Gets the report entries from Workday.


## Workday IAM Event Generator (Beta)

**Type:** integration  
**Product:** Workday  

Generates mock reports and events for Workday IAM. Use these for testing and development

**Commands:**

- `workday-generate-hire-event`: Generate workday new hire event.
- `workday-generate-update-event`: Generate workday update event.
- `workday-generate-rehire-event`: Generate workday rehire event.
- `workday-generate-terminate-event`: Generate workday terminate event.
- `initialize-context`: Reset the integration context to fetch the first run reports.


## XM Cyber

**Type:** integration  
**Product:** XM Cyber  

The XM Cyber integration creates unique incidents with valuable data collected daily, and enriches your existing incidents with attack simulation context. This enables you to prioritize your responses based on XM Cyber’s insights. This integration was integrated and tested with version 1.43.0.355 of XMCyber

**Commands:**

- `xmcyber-affected-critical-assets-list`: List critical assets at risk from an entity and the complexity of the attack
- `xmcyber-affected-entities-list`: List all entities at risk from an entity and the complexity of the attack
- `xmcyber-version-supported`: Check if current XM version supports Cortex platform integration
- `xmcyber-version-get`: Get current xm version
- `xmcyber-enrich-from-ip`: Return data on Entity by IP from XM Cyber
- `xmcyber-enrich-from-entityId`: Return data on Entity by entityId from XM Cyber
- `xmcyber-enrich-from-hostname`: Return data on Entity by hostname from XM Cyber
- `xmcyber-enrich-from-fields`: Return data on an XM entity


## XM Cyber CEM

**Type:** integration  
**Product:** XM Cyber  

The XM Cyber integration connects XM Cyber's Continuous Exposure Management (CEM) platform with platform, enhancing your Security Information and Event Management (SIEM) and Security Orchestration, Automation, and Response processes with attack graph context and prioritization, while also feeding relevant entities back to CEM to be defined as breach points in CEM scenarios

**Commands:**

- `xmcyber-enrich-incident`: Enriches Hostname and User entities on the SOAR platform by using information available in the XM Cyber platform.
- `xmcyber-push-breach-point`: Adds a breach point label to the specified entities based on defined criteria and pushes the label as an Imported Attribute to XM Cyber CEM's platform.
- `xmcyber-remove-breach-point`: Removes a breach point label from the specified entities in XM Cyber CEM's platform.
- `xmcyber-calculate-risk-score`: Calculates the overall risk score for entities based on their Compromise Risk Score and Choke Point Score from XM Cyber enrichment data.


## xMatters

**Type:** integration  
**Product:** xMatters  

This is an integration for using xMatters. This integration was integrated and tested with version 1 of xMatters

**Commands:**

- `xm-trigger-workflow`: sends the event to xMatters
- `xm-get-events`: Get events from xMatters.
- `xm-get-event`: Get a single event from xMatters.


## xMatters - Example Conditional Actions

**Type:** playbook  
**Product:** xMatters  

Trigger the xMatters - Trigger and Wait playbook to fire an event to xMatters targeting the recipients, then branch based on the chosen response

**Inputs:**

- `recipients`: A comma separated list of Groups or Users to target for a notification
- `subject`: A brief summary of the reason to notify
- `body`: Detailed description of the reason to notify
- `incident_id`: The related incident_id


## Xpanse - Alert Handler

**Type:** playbook  
**Product:** Cortex Xpanse  

Default alert handling for Cortex Xpanse alerts

**Inputs:**

- `WriteToXpanse`: Whether to write data back to Cortex Expanse.


## Xpanse - NMap - Detect Service

**Type:** playbook  
**Product:** Cortex Xpanse  

Playbook that looks at what ASM sub-type the alert is and directs it to different pre/post mitigation scans (such as NMAP, SNMP)

**Inputs:**

- `RemoteIP`: Remote IP address in the alert.
- `RemotePort`: Remote port number in the alert.
- `ScanNumber`: Scan number in case there are multiple IDs in the parent playbook.


## XQLDSHelper

**Type:** script  
**Product:** XQLDSHelper  

Run an XQL query and creates an entry for the General Purpose Dynamic Section to display a graph or table widget based on the results. The query is executed by the xdr-xql-generic-query and the xdr-xql-get-query-results command

**Inputs:**

- `templates_type`: The type of the templates data.
- `template_name`: The name of a template to choose it from 'templates'.
- `templates`: A list of templates to choose from for building an entry.
- `base_time`: The base time for the relative time provided to earliest_time or latest_time (The default is the first available value from the following: i
- `round_time`: The value (in seconds) used to round down the base time (Default = 0). If two parameters are provided in a list, they will be applied to the
- `earliest_time`: The earliest time at which the time range of the query starts (Default = 24 hours ago).
- `latest_time`: The latest time at which the time range of the query ends (Default = now).
- `variable_substitution`: The pair of default opening and closing markers that enclose a variable name (Default = ${,}).


## YaraScan

**Type:** script  
**Product:** Yara  

Performs a Yara scan on the specified files

**Inputs:**

- `yaraRule`: The Yara rule to use for the file scan.
- `entryIDs`: A comma-separated list of file entry IDs to scan.


## Zabbix

**Type:** integration  
**Product:** Zabbix  

Allow integration with Zabbix api

**Commands:**

- `zabbix-execute-command`: Execute command on Zabbix API
- `zabbix-execute-command`: 
- `zabbix-hostgroup-get`: Get host groups
- `zabbix-hostgroup-get`: 
- `zabbix-host-get`: Get hosts
- `zabbix-host-get`: 
- `zabbix-trigger-get`: Get triggers
- `zabbix-trigger-get`: 
- `zabbix-event-get`: Get events
- `zabbix-event-get`: 


## Zafran API

**Type:** integration  
**Product:** Zafran  

In today’s complex security landscape, resource-constrained teams struggle to efficiently mitigate exposure risks across large infrastructures. The Zafran Integration with Palo platform helps you implement Automated, High Impact Mitigations at scale. With this integration, teams can prioritize mitigation actions, trigger playbooks with a single click, and streamline their response efforts, all from within the Palo platform environment

**Commands:**

- `zafran-mitigation-performed`: Update on mitigations performed
- `zafran-mitigations-export`: Export recommended mitigations
- `zafran-mitigations-performed`: Update on mitigations performed


## ZeroFox

**Type:** integration  
**Product:** ZeroFox  

Cloud-based SaaS to detect risks found on social media and digital channels. This integration was integrated and tested with versions 1.0 and 2.0 of ZeroFox

**Commands:**

- `zerofox-get-alert`: Fetches an alert by ID.
- `zerofox-alert-user-assignment`: Assigns an alert to a user.
- `zerofox-close-alert`: Closes an alert.
- `zerofox-alert-request-takedown`: Requests a takedown of a specified alert.
- `zerofox-modify-alert-tags`: Adds tags to and or removes tags from a specified alert.
- `zerofox-list-alerts`: Returns alerts that match user-defined or default filters and parameters. By default, no filters are applied and the results are sorted by timestamp.
- `zerofox-create-entity`: Creates a new entity associated with the company of the authorized user.
- `zerofox-alert-cancel-takedown`: Cancels a takedown of a specified alert.
- `zerofox-open-alert`: Opens an alert.
- `zerofox-list-entities`: Lists all entities associated with the company of the authorized user.
- `zerofox-get-entity-types`: Shows a table of all entity type names and IDs in the War Room.
- `zerofox-get-policy-types`: Shows a table of all policy type names and IDs in the War Room.
- `zerofox-modify-alert-notes`: Modify the notes of a specified alert.
- `zerofox-submit-threat`: Submits potential threats into the ZF alert registry for disruption.
- `zerofox-send-alert-attachment`: Sends an attachment to a specified alert.


## ZeroFox Key Incidents

**Type:** integration  
**Product:** ZeroFox  

Cloud-based SaaS to detect risks found on social media and digital channels. This integration was integrated and tested with version 1.4.0 of ZeroFoxKey

**Commands:**

- `zerofox-get-key-incident-attachment`: Fetches a Key Incident Attachment by ID and uploads it to the current investigation War Room.


## Zerohack XDR

**Type:** integration  
**Product:** Zerohack XDR  

The companion integration for Zerohack XDR. Current versions allow the user to collect data from the XDR and later versions will support data exfiltration to XDR. This integration was integrated and tested with version 1.0 of Zerohack XDR

**Commands:**

- `zerohack-get-latest-incident`: Fetch a single incident of your choice of severity level to study the incidents structure before you start continously fecthing incidents.


## ZeroTrustAnalyticsPlatform

**Type:** integration  
**Product:** Zero Trust Analytics Platform  

Zero Trust Analytics Platform (ZTAP) is the underlying investigation platform and user interface for Critical Start's MDR service. This integration was integrated and tested with version 2021-06-25 of ZeroTrustAnalyticsPlatform

**Commands:**

- `get-mapping-fields`: Get mapping fields from remote incident.
- `get-remote-data`: Get remote data from a remote incident. This command should only be called manually for debugging purposes.
- `ztap-get-alert-entries`: Get the entries data from a remote incident.


## Zimperium

**Type:** integration  
**Product:** Zimperium  

Zimperium is a mobile security platform that generates alerts based on anomalous or unauthorized activities detected on a user's mobile device. This integration was integrated and tested with version 4.24 of Zimperium

**Commands:**

- `zimperium-events-search`: Search events.
- `zimperium-users-search`: Search users.
- `zimperium-user-get-by-id`: Retrieves details for a single user by object ID.
- `zimperium-devices-search`: Search devices.
- `zimperium-device-get-by-id`: Retrieves details for a single device.
- `zimperium-devices-get-last-updated`: Retrieves devices from Greater than Last Updated.
- `zimperium-app-classification-get`: Retrieves application classification.
- `zimperium-report-get`: Gets a report.
- `file`: Checks the reputation of an app in Zimperium.


## Zimperium v2

**Type:** integration  
**Product:** Zimperium  

Fetch and investigate mobile security alerts, generated based on anomalous or unauthorized activities detected on a user's mobile device. This integration was integrated and tested with version v.5.24.0 of Zimperium v2. Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `zimperium-users-search`: Search users. Only a user created as a "Team admin" is authorized to perform this request. Also, it will only get information about the teams that this user is 
- `zimperium-devices-search`: Search devices.
- `zimperium-report-get`: Gets a report.
- `zimperium-threat-search`: 
- `zimperium-app-version-list`: List the app versions.
- `zimperium-get-devices-by-cve`: Gets a devices associated with a specific CVE.
- `zimperium-devices-os-version`: Gets devices associated with a specific operating system version.
- `zimperium-get-cves-by-device`: Gets the CVEs associated with a specific device.
- `zimperium-vulnerability-get`: Gets the vulnerabilities.
- `zimperium-policy-group-list`: Get policy groups.
- `zimperium-policy-privacy-get`: Get a privacy policy by its identifier.
- `zimperium-policy-threat-get`: Get a threat policy by its identifier.
- `zimperium-policy-phishing-get`: Get a phishing policy by its identifier.
- `zimperium-policy-app-settings-get`: List the app versions.
- `zimperium-policy-device-inactivity-list`: Get the policy device inactivity list.


## ZipFile

**Type:** script  
**Product:** Common Scripts  

Zip a file and upload to war room Supported the platform.0.0 and later

**Inputs:**

- `entryID`: CSV list of entry ids for the files to zip.
- `zipName`: Name of the output file, for example: zipName="test" would result in output file "test.zip"
- `password`: Used to create a password protected zip file. Example: password="abcd"


## ZipStrings

**Type:** script  
**Product:** Common Scripts  

Joining values by index from 2 list according to a given format

**Inputs:**

- `list1`: The first list. List must be at same size as list2.
- `format`: A format to join strings by, for example- {1}-{2} will take values in the same index of both list, where the {1} will be replaced with the v
- `list2`: The second list. List must be at same size as list1.


## Zoom

**Type:** integration  
**Product:** Zoom  

Use the Zoom integration manage your Zoom users and meetings This integration was integrated and tested with version 2.0.0 of Zoom

**Commands:**

- `zoom-create-user`: Create a new user in zoom account
- `zoom-create-meeting`: Create a new zoom meeting (scheduled ,instant, or recurring)
- `zoom-fetch-recording`: Get meeting record and save as file in the warroom
- `zoom-list-users`: List the existing users
- `zoom-delete-user`: Delete a user from Zoom
- `zoom-meeting-get`: Get the information of an existing zoom meeting
- `zoom-meeting-list`: Show all the meetings of a given user. Note: only scheduled and unexpired meetings will appear.
- `zoom-list-user-channels`: List the existing channels
- `zoom-create-channel`: Creates a channel for a user
- `zoom-delete-channel`: Deletes a specific Zoom channel
- `zoom-update-channel`: Update an existing channel in a Zoom account.
- `zoom-invite-to-channel`: Invites members that are in a user's contact list to a channel. A channel can have one or multiple members. The maximum number of members that can be added at o
- `zoom-remove-from-channel`: Removes a member from a chat channel. A channel can have one or more members.
- `zoom-send-file`: Sends a file on Zoom to either an individual user in your contact list or a channel of which you are a member.
- `zoom-send-message`: Sends chat messages on Zoom to either an individual user who is in your contact list or to a channel of which you are a member.


## Zoom Mail

**Type:** integration  
**Product:** Zoom Mail  

Enables interaction with the Zoom Mail API

**Commands:**

- `zoom-mail-email-move-trash`: Move a message to the trash.
- `zoom-mail-email-list`: Lists the messages in the user's mailbox.
- `zoom-mail-thread-list`: Get an email thread.
- `zoom-mail-email-attachment-get`: Get an email attachment.
- `zoom-mail-send-email`: Sends an email message with support for plain text, HTML, and attachments.
- `zoom-mail-mailbox-profile-get`: Retrieves the mailbox profile.
- `zoom-mail-user-list`: Lists the available users.


## Zoom_IAM

**Type:** integration  
**Product:** Zoom  

An Identity and Access Management integration template. This integration was integrated and tested with version 2.0.0 of Zoom_IAM

**Commands:**

- `iam-disable-user`: Disable an active user.
- `iam-enable-user`: Enable a deactivated user.
- `iam-get-user`: Retrieves a single user resource.
- `get-mapping-fields`: Retrieves a User Profile schema, which holds all of the user fields within the application. Used for outgoing-mapping through the Get Schema option.


## ZoomApiModule

**Type:** script  

To use the common Zoom Server logic (authentication and API requests), run the following command to import the ZoomApiModule. Then, the ZoomApiModule will be available for usage. For examples, see the Zoom integration


## ZoomAsk

**Type:** script  
**Product:** Zoom  

Sends a message (question) to either a user (in a direct message) or to a channel. The message includes predefined reply options. The response can also close a task (might be conditional) in a playbook

**Inputs:**

- `user`: The Zoom user to whom to send the message. Can be either an email address or a Zoom user_id.
- `channel_id`: The Zoom channel_id to which to send the message.
- `message`: The message to send to the user or channel.
- `option1`: The first reply option. The default is "Yes" with a blue button. To change the color of the button, add the pound sign (#) followed by the n
- `option2`: The second reply option. The default is "No" with a red button. To change the button color, add the pound sign (#) followed by the name of t
- `task`: The task to close with the reply. If empty, then no playbook tasks will be closed.
- `persistent`: Indicates whether to use one-time entitlement or persistent entitlement.
- `responseType`: How the user should respond to the question.


## ZTAP Alert

**Type:** playbook  
**Product:** Zero Trust Analytics Platform  

This playbok is triggered by fetching escalated ZTAP Alerts. The playbook fetches newly escalated alerts. Then, the playbook performs enrichment on the incident's indicators. Lastly, it adds comments/logs as Evidence

**Inputs:**

- `Enrich`: Determines whether to enrich all indicators in the incident.
- `OnCall`: Set to true to assign only user that is currently on shift. Requires the platform.5 or later.


## ZTAPBuildTimeline

**Type:** script  
**Product:** Zero Trust Analytics Platform  

Adds unmarked log/comment notes as evidence in the timeline


## ZTAPExtractFields

**Type:** script  
**Product:** Zero Trust Analytics Platform  

Extracts ZTAP fields into a format parsable to grab as indicators

**Inputs:**

- `value`: The input trigger events from the ZTAP api


## ZTAPParseFields

**Type:** script  
**Product:** Zero Trust Analytics Platform  

Parses ZTAP event fields to display as key/value pairs in a dynamic table

**Inputs:**

- `max_fields`: Maximum number of fields to display
- `max_value_length`: Maximum number of characters to display per field
- `full`: Do not truncate output


## ZTAPParseLinks

**Type:** script  
**Product:** Zero Trust Analytics Platform  

Parses ZTAP external links to display in a dynamic table


## ZTAPViewTimeline

**Type:** script  
**Product:** Zero Trust Analytics Platform  

View notes only relating to ZTAP

## Cognyte Luminar V3 Feed

**Type:** integration  
**Product:** Cognyte

This Integration is part of the Luminar IOCs & leaked credentials Pack.#Supported versionsAvailable on Cortex XSOAR (versions 6.9.0 and later) and Cortex XSIAM.Cognyte is a global leader in security analytics software that empowers governments and enterprises with Actionable Intelligence for a safer world. Luminar is Cognyte's asset-based cybersecurity intelligence platform that enables organizations to build and maintain a proactive threat intelligence operation.This integration fetches intelligence-based IOCs and customer-related leaked records identified by Luminar, using the Luminar TAXII

**Commands:**

- `luminar-v3-get-indicators`: Gets Luminar indicators from the IOCs collection
- `luminar-v3-get-leaked-records`: Gets Luminar leaked records (leaked credentials) from the Leaked Records collection


## KELA BrandControl

**Type:** integration  
**Product:** KELA

This Integration is part of the KELA BrandControl Pack.#Supported versionsAvailable on Cortex XSOAR (versions 6.10.0 and later) and Cortex XSIAM.KELA Brand Control#Brand Control detects brand impersonation across the open web, social media and app ecosystems: phishing websites, look-alike domains, fake social media profiles, fake shops and more.This integration fetches brand impersonation incidents from KELA Brand Control into Cortex. This integration was integrated and tested with version 1.0 of the KELA Brand Control API.Configure KELA BrandControl in Cortex#Navigate to Settings > Integratio

**Commands:**

- `kela-brandcontrol-incident-list`: Retrieves the Brand Control incidents of a workspace, with filtering, sorting and pagination


## KELA Identity Guard

**Type:** integration  
**Product:** KELA

This Integration is part of the KELA Identity Guard Pack.#Supported versionsAvailable on Cortex XSOAR (versions 6.10.0 and later) and Cortex XSIAM.KELA Identity Guard#Search KELA Identity Guard incidents: compromised credentials detected on infostealer-infected machines (bots), leaked credential lists, data breaches and cybercrime chatter; bot-market alerts (bots/webmails offered for sale); and compromised session-cookie incidents. Includes fetch-incidents to automatically mirror all three sources into Cortex, each independently toggleable.This integration was integrated and tested with the Id

**Commands:**

- `kela-identityguard-search-incidents`: Search Identity Guard incidents for a workspace, with rich filtering, sorting and pagination
- `kela-identityguard-search-bot-markets`: Search Identity Guard bot-market alerts (bots/webmails offered for sale) for a workspace
- `kela-identityguard-search-cookie-incidents`: Search Identity Guard compromised session-cookie incidents for a workspace

