# Integration and Automation Catalog - Soc Operations

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## 1Password

**Type:** integration  
**Product:** OnePassword  

Fetch events about actions performed by 1Password users within a specific account, access and modifications to items in shared vaults, and user sign-in attempts. This integration was integrated and tested with V2 endpoints of the 1Password Events API

**Commands:**

- `None`: 
- `None`: 


## 1Touch.io's Inventa Connector

**Type:** integration  
**Product:** Inventa  

Use the Inventa integration to generate DSAR reports within Inventa instance and retrieve DSAR data for the platform This integration was integrated and tested with version 2.8.0 of Inventa

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


## Absolute

**Type:** integration  
**Product:** Absolute  

Absolute is an adaptive endpoint security solution that delivers device security, data security, and asset management of endpoints. This integration was integrated and tested with the API version 1.7 of Absolute. Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Akamai Prolexic

**Type:** integration  
**Product:** Akamai Prolexic  

Collects DDoS detection critical events and general events from Akamai Prolexic Analytics for Cortex XSIAM. This integration was integrated and tested with version v2 of the Akamai Prolexic Analytics API

**Commands:**

- `None`: 
- `None`: 


## Akamai WAF

**Type:** integration  
**Product:** Akamai WAF  

Use the Akamai WAF integration to manage common sets of lists used by various Akamai security products and features. This is the modified version where a new command "akamai-update-network-list-elements" was added by the SA

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

- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Amazon DynamoDB

**Type:** integration  
**Product:** Amazon DynamoDB  

Amazon DynamoDB Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database, so that you don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling. With DynamoDB, you can create database tables that can store and retrieve any amount of data, and serve any level of request traffic. You can scale up or scale down your tables' throughput capacity without downtime or performance degradation, and use the AWS Management Console to monitor resource utilization and performance metrics. DynamoDB automatically spreads the data and traffic for your tables over a sufficient number of servers to handle your throughput and storage requirements, while maintaining consistent and fast performance. All of your data is stored on solid state disks (SSDs) and automatically replicated across multiple Availability Zones in an AWS region, providing built-in high availability and data durability. For more information regarding the AWS DynamoDB service, please visit the official documentation found here

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


## Amazon Security Lake

**Type:** integration  
**Product:** Amazon - Security Lake  

Amazon Security Lake is a fully managed security data lake service. This integration was integrated and tested with version 1.34.20 of AWS Security Lake SDK (boto3)

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


## AMP

**Type:** integration  
**Product:** Cisco AMP  

Uses CISCO AMP Endpoint This integration was integrated and tested with API version v1 of AMP

**Commands:**

- `None`: 


## Analyst1

**Type:** integration  
**Product:** Analyst1  
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


## Anomali Match

**Type:** integration  
**Product:** Anomali Enterprise  

Use Anomali Match to search indicators and enrich domains

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


## Anomali Security Analytics Alerts

**Type:** integration  
**Product:** Anomali Security Analytics  

The Anomali Security Analytics pack allows users to manage security alerts by interacting directly with the Anomali Security Analytics platform. It supports creating search jobs, monitoring their status, retrieving results, and updating alert statuses or comments, streamlining integration with Palo Alto platform. This integration was integrated and tested with version 1.0 of AnomaliSecurityAnalyticsAlerts

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Ansible ACME

**Type:** integration  
**Product:** Ansible Linux  

Automatic Certificate Management Environment on Linux hosts management using Ansible modules. This integration lets you manage certificate generation on Linux hosts with a CA supporting the ACME protocol, such as Let’s Encrypt. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the hosts by utilising SSH combined with Python. To use this integration, configure an instance of this integration. This will associate a credential to be used to access hosts when commands are run. The commands from this integration will take the Linux host address(es) as an input, and use the saved credential associated to the instance to execute. Create separate instances if multiple credentials are required. This integration was tested with Let's Encrypt and supports the ACME http-01, dns-01 and tls-alpn-01 challenges

**Commands:**

- `None`: 
- `None`: 


## Ansible Automation Platform

**Type:** integration  
**Product:** Ansible Automation Platform  

Scale IT automation, manage complex deployments, and speed productivity. This integration was integrated and tested with version v3.8.0 of Ansible Automation Platform and with API version v2

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


## Ansible Cisco IOS

**Type:** integration  
**Product:** Ansible Cisco IOS  

This integration enables the management of Cisco IOS Switches and Routers directly from platform using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the hosts by utilising SSH. To use this integration, configure an instance of this integration. This will associate a credential to be used to access hosts when commands are run. The commands from this integration will take the IOS host address(es) as an input, and use the saved credential associated to the instance to execute. Create separate instances if multiple credentials are required

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


## Ansible Cisco NXOS

**Type:** integration  
**Product:** Ansible Cisco NXOS  

This integration enables the management of Cisco NXOS Switches and Routers directly from platform using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the hosts by utilising SSH. To use this integration, configure an instance of this integration. This will associate a credential to be used to access hosts when commands are run. The commands from this integration will take the NXOS host address(es) as an input, and use the saved credential associated to the instance to execute. Create separate instances if multiple credentials are required

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


## Ansible DNS

**Type:** integration  
**Product:** Ansible Linux  

This integration enables the management of DNS Records directly from platform using Dynamic DNS Updates from the NSUpdate Ansible Module. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the DNS server. The DNS master server being managed must be configured to accept Dynamic DNS updates using Transaction signatures as described in RFC2845

**Commands:**

- `None`: 


## Ansible Microsoft Windows

**Type:** integration  
**Product:** Ansible Microsoft Windows  

This integration enables the management of Microsoft Windows hosts directly from platform using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the Windows hosts by utilising the Windows Remote Management (WinRM) API interface present in Windows 2008 and above combined with PowerShell. To use this integration, configure an instance of this integration. This will associate a credential to be used to access hosts when commands are run. The commands from this integration will take the Windows host address(es) as an input, and use the saved credential associated to the instance to execute. Create separate instances if multiple credentials are required. This integration uses NTLM for authentication. This ensures that actual credentials are never sent over the network, instead relying on hashing methods. By default, the initial authentication phase is performed unencrypted over HTTP, after which all communication is encrypted using a symmetric 256-bit key. If it is desired to use HTTPS from the onset, additional configuration on the Windows host is required. After WinRM is configured for HTTPS, update the port setting on the integration. Any port other than the default 5985 will use HTTPS communication

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Ansible OpenSSL

**Type:** integration  
**Product:** Ansible Linux  

This integration enables the management of certificates on Linux hosts directly from platform using Ansible. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the hosts by utilising SSH combined with Python. To use this integration, configure an instance of this integration. This will associate a credential to be used to access hosts when commands are run. The commands from this integration will take the Linux host address(es) as an input, and use the saved credential associated to the instance to execute. Create separate instances if multiple credentials are required

**Commands:**

- `None`: 
- `None`: 


## Ansible VMware

**Type:** integration  
**Product:** Ansible VMware  

This integration enables the management of VMware vCenter and ESXi hosts directly from platform using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the hosts by utilising VMware APIs

**Commands:**

- `None`: 


## Anthropic Claude

**Type:** integration  
**Product:** Anthropic Claude  

Designed to assist security professionals with security investigations, threat hunting, and anomaly detection, leveraging Anthropic Claude's natural language conversational capabilities

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


## Anthropic Claude (Standard Connector)

**Type:** integration  
**Product:** Anthropic Claude (Standard Connector)  

This integration is configured automatically as part of the Anthropic Claude Standard Connector. Do not configure this integration directly — set it up from the connector page instead

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## AnthropicClaudeApiModule

**Type:** script  

Common Anthropic Claude Compliance API code shared by: The module carries only what the two irreversible compliance delete commands (claude-chat-file-delete and claude-project-document-delete) need. The LLM client, the compliance list/get commands, and the event collector stay inline in the parent pack because they are not shared


## ANY.RUN Cloud Sandbox

**Type:** integration  
**Product:** ANY.RUN  

ANY.RUN is a cloud-based sandbox with interactive access

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


## ANY.RUN TI Lookup

**Type:** integration  
**Product:** ANY.RUN  

TI Lookup is a searchable database of IOCs, IOAs, IOBs, and events for threat hunting and a service for browsing malicious files by their content

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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


## appNovi

**Type:** integration  
**Product:** AppNovi  

Search across meshed network, security, and business data in appNovi to make efficient informed security decisions for risk management and incident response. Gain immediate intelligence on assets, visualize risk and threats across your network, and undertake interactive investigations across the network to reduce MTTR for incident response. This integration was integrated and tested with appNovi v2.0

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 


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


## ArcusTeam

**Type:** integration  
**Product:** ArcusTeam  

The ArcusTeam API allows the user to inspect connected devices' attack surface. By feeding device identifiers and the software it runs: DeviceTotal will return a map of the device’s attack surface. DeviceTotal was built from the ground up in order to provide complete visibility into connected devices and mitigate 3rd party risk. DeviceTotal can continuously identify & predict such that the connected device security posture is being assessed, prioritized and mitigated effectively. This integration was integrated and tested with version 6.11.0 of ArcusTeam

**Commands:**

- `None`: 


## Arduino

**Type:** integration  
**Product:** Arduino  

Connects to and controls an Arduino pin system using the network

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## Arkime

**Type:** integration  
**Product:** Arkime  

Arkime (formerly Moloch) is a large scale, open source, indexed packet capture and search tool. This integration was integrated and tested with version 3.4.1 (API v3) of Arkime. For older versions, see the Moloch pack (deprecated)

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


## Armis

**Type:** integration  
**Product:** Armis  

Use the Armis integration to search alerts and devices, tag and untag devices, and set alert statuses. This integration was integrated and tested with the latest version of Armis

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## Armorblox

**Type:** integration  
**Product:** Armorblox  

Armorblox is an API-based platform that stops targeted email attacks, protects sensitive data, and automates incident response. This integration was integrated and tested with version 4.3.0 of Armorblox

**Commands:**

- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 


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

- `None`: 


## Atlassian Confluence Server

**Type:** integration  
**Product:** Atlassian Confluence Server  

Atlassian Confluence Server API. This integration was integrated and tested with version 6.1 of Atlassian Confluence Server

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Atlassian IAM

**Type:** integration  
**Product:** Atlassian IAM  

Note: This integration should be used as part of our IAM premium pack. For further details, visit our IAM pack documentation. For more information, please refer to the Identity Lifecycle Management article. Integrate with Atlassian's services to execute generic ILM management operations such as create, update, delete, etc, for employee lifecycle processes

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Atlassian Jira Service Management

**Type:** integration  
**Product:** Atlassian Jira Service Management  

Use this integration to manage Jira objects and attach files to Jira objects from the platform. This integration was integrated and tested with version 5.4.15 of AtlassianJiraServiceManagement

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


## Atlassian Jira v3

**Type:** integration  
**Product:** Atlassian Jira  

Use the Jira integration to manage issues and create the platform. From the platform.0 and above, the integration also mirrors issues to existing issue incidents in the platform. The integration now supports both OnPrem, and Cloud instances. This integration was integrated and tested with: Jira Cloud Platform V3 (for Cloud), Jira Software Cloud (for Cloud), Jira Server Platform 9.6.0 (for OnPrem), Jira Software Server 9.6.0 (for OnPrem). Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

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


## AtlassianApiModule

**Type:** script  

This API module provides shared OAuth 2.0 authentication functionality for Atlassian products (Jira, Confluence), supporting both Cloud and On-Prem/Data Center instances


## AttackIQ Platform

**Type:** integration  
**Product:** AttackIQ Platform  

Use the AttackIQ integration to simulate a platform that provides validations for security controls, responses, and remediation exercises. This integration was integrated and tested with AttackIQ FireDrill v2.15.96

**Commands:**

- `None`: 


## Augur Security

**Type:** integration  
**Product:** Augur Security  

Leverage Augur's preemptive threat intelligence for actionable data against persistent threat actors. Augur Security return a list which could include IP addresses, domains, URLs, and hash indicators which are updated daily

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Automox

**Type:** integration  
**Product:** Automox  

Use the Automox integration to create device groups, update devices, run policies, and remediate vulnerabilities of devices through the Automox platform. This integration was integrated and tested as of 2022-03-21 with the Automox API

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


## Axonius

**Type:** integration  
**Product:** Axonius  

This integration is for fetching information about assets in Axonius. This integration was integrated and tested with version 3.9 of Axonius

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


## Barracuda Reputation Block List (BRBL)

**Type:** integration  
**Product:** Barracuda  

This integration enables reputation checks against IPs from Barracuda Reputation Block List (BRBL) This integration was integrated and tested with Barracuda Reputation Block List (BRBL)

**Commands:**

- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 


## BeyondTrust Privilege Management Cloud

**Type:** integration  
**Product:** BeyondTrust  
**Commands:**

- `None`: 


## BeyondTrust Retrieve Credentials

**Type:** playbook  
**Product:** BeyondTrust Password Safe  

Playbook for retrieving credentials for BeyondTrust Password Safe


## Binalyze AIR

**Type:** integration  
**Product:** Binalyze AIR  
**Commands:**

- `None`: 
- `None`: 


## Binalyze AIR Extended

**Type:** integration  
**Product:** Binalyze AIR Extended  

Manage Binalyze AIR forensic acquisition, endpoint isolation, triage, cases, tasks, assets, repositories, and evidence artifacts from the platform. This integration was integrated and tested with Binalyze AIR Extended

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


## BinarySearchPy

**Type:** script  
**Product:** Common Scripts  

Searches for a binary on an endpoint using Carbon Black


## Bitbucket

**Type:** integration  
**Product:** Bitbucket  

Bitbucket Cloud is a Git-based code and CI/CD tool optimized for teams using Jira. This integration was integrated and tested with version 7.21.0 of Bitbucket

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


## Bitsight for Security Performance Management

**Type:** integration  
**Product:** Bitsight  

Use the "Bitsight for Security Performance Management" Integration to get company guid, details, and findings. This integration also allows to fetch the findings by using the fetch incidents capability. This integration was integrated and tested with version 01 of Bitsight for Security Performance Management

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Bitwarden Password Manager

**Type:** integration  
**Product:** Bitwarden Password Manager  

This integration collects event logs from Bitwarden Password Manager to Cortex XSIAM. This integration was integrated and tested with version 2024.6.2 of Bitwarden Password Manager

**Commands:**

- `None`: 


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


## BMC Helix Remedyforce

**Type:** integration  
**Product:** Bmc Helix Remedyforce  

BMC Helix Remedyforce integration allows customers to create/update service requests and incidents. It also allows to update status, resolve service requests and incidents with customer notes. This integration exposes standard ticketing capabilities that can be utilized as part of automation & orchestration. This integration was integrated and tested with version 202002.79 of BMC Helix Remedyforce

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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


## BreachConfirmationHTML

**Type:** script  
**Product:** Common Scripts  

This Compliance content pack contains essential incidents fields that are used in the compliance-related packs. The script in this pack is used for a dynamic field in the HIPAA Breach Notification Incident layout and the US Breach Notification layout to indicate if a breach was confirmed. For more information, visit our the platform


## BreachRx

**Type:** integration  
**Product:** BreachRx  

Automate your privacy Incident Response workflow through the BreachRx platform. This integration was integrated and tested with version 1.20 of BreachRx

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Cape Sandbox

**Type:** integration  
**Product:** Cape Sandbox  
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

- `None`: 


## Censys Platform

**Type:** integration  
**Product:** Censys  

Built on the industry’s most comprehensive Internet Map, the Censys Platform delivers unmatched visibility into global internet assets, adversary infrastructure, and evolving threats. This integration was integrated and tested with version 2.0 of Censys

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


## Centrify Vault

**Type:** integration  
**Product:** Centrify Vault  

Leverage the Centrify Vault integration to create and manage Secrets

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Check Point EM Takedowns

**Type:** integration  
**Product:** Cyberint  

Use the Cyberint Takedowns integration to manage takedowns requests

**Commands:**

- `None`: 
- `None`: 


## Check Point Harmony Endpoint

**Type:** integration  
**Product:** Check Point Harmony Endpoint  

Checkpoint Harmony Endpoint provides a complete endpoint security solution built to protect organizations and the remote workforce from today's complex threat landscape. This integration was integrated and tested with version 1 of CheckPointHarmonyEndpoint

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


## Check Point Network Detection and Response (Infinity NDR)

**Type:** integration  
**Product:** Check Point Infinity NDR  

Collect network security events from Check Point Infinity NDR for your secured SaaS periodically This integration was integrated and tested with version 1.1.0 of CheckPointNDR

**Commands:**

- `None`: 


## Check Point XDR

**Type:** integration  
**Product:** Check Point XDR  

The Check Point XDR (Extended Detection and Response) integration allows you to connect to Check Point's CloudInfra platform to fetch and manage incidents. This integration enables you to retrieve incidents from Check Point XDR, convert them into the platform, and manage them effectively within your security operations workflows

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## Cherwell

**Type:** integration  
**Product:** Cherwell  

Cloud-based IT service management solution This integration was integrated and tested with version 10.1.1 of Cherwell

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

- `None`: 


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


## CIRCL CVE Search

**Type:** integration  
**Product:** CIRCL  

Searches for CVE information using circl.lu

**Commands:**

- `None`: 


## CircleCI

**Type:** integration  
**Product:** CircleCI  

Gets the details of the CircleCI workflows; including the details of the last runs and the jobs, and retrieves the artifacts of the jobs. This integration was integrated and tested with version v2 of CircleCI

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


## CIRCLEHashlookup

**Type:** integration  
**Product:** CIRCL hashlookup (hashlookup.circl.lu)  

CIRCL hash lookup is a public API to lookup hash values against known database of files. NSRL RDS database is included and many others are also included. The API is accessible via HTTP ReST API and the API is also described as an OpenAPI. The service is free and served as a best-effort basis. This integration was integrated and tested with online version of CIRCLEHashlookup

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## Cisco AMP v2

**Type:** integration  
**Product:** Cisco AMP  

Cisco Advanced Malware Protection software is designed to prevent, detect, and help remove threats in an efficient manner from computer systems. Threats can take the form of software viruses and other malware such as ransomware, worms, Trojans, spyware, adware, and fileless malware. This integration was integrated and tested with version 1 of CiscoAMP

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


## Cisco AppDynamics

**Type:** integration  
**Product:** Cisco AppDynamics  

AppDynamics enables you to automate incident management, gain real-time performance metrics, and optimize applications to meet business needs

**Commands:**

- `None`: 


## Cisco ASA

**Type:** integration  
**Product:** Cisco ASA  

Use the Cisco Adaptive Security Appliance Software integration to manage interfaces, rules, and network objects. This integration was integrated and tested with version 9.16(3)23 of Cisco ASA

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


## Cisco ESA

**Type:** integration  
**Product:** Cisco Email Security Appliance (IronPort)  

The Cisco Email Security Appliance is an email security gateway product. It is designed to detect and block a wide variety of email-born threats, such as malware, spam and phishing attempts. This integration was integrated and tested with version 16.0 of Cisco Email Security Appliance

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


## Cisco ETD Connector

**Type:** integration  
**Product:** ETD platform Connector  

Fetches Cisco Email Threat Defense (ETD) message events and creates incidents. This integration was integrated and tested with of ETDConnector

**Commands:**

- `None`: 


## Cisco Firepower

**Type:** integration  
**Product:** Cisco Firepower  
**Commands:**

- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Cisco Secure Malware Analytics (Threat Grid) v2

**Type:** integration  
**Product:** Cisco Secure Malware Analytics  

Query and upload samples to Cisco threat grid. This integration was integrated and tested with version 2 of Cisco Secure Malware Analytics (Threat Grid)

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


## Cisco Security Management Appliance

**Type:** integration  
**Product:** CiscoSMA  

The Security Management Appliance (SMA) is used to centralize services from Email Security Appliances (ESAs) and Web Security Appliances (WSAs). This integration was integrated and tested with version 12.0 of Cisco Security Management Appliance

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


## Cisco ThousandEyes

**Type:** integration  
**Product:** Cisco ThousandEyes  

This is the Cisco ThousandEyes event collector integration for Cortex XSIAM. This integration enables you to fetch events such as alerts and audit logs from Cisco ThousandEyes and process them within Cortex XSIAM. This integration was developed and tested with version 1.0.0 of Cisco ThousandEyes

**Commands:**

- `None`: 


## Cisco Umbrella Enforcement

**Type:** integration  
**Product:** Cisco Umbrella Enforcement  

Add and remove domains in Cisco OpenDNS. This integration was integrated and tested with version 1.0 of Cisco Umbrella Enforcement. Supported the platform.0.0 and later

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Cisco Umbrella Investigate

**Type:** integration  
**Product:** Cisco Umbrella Investigate  

Cisco Umbrella Investigate enable you to research domains, IPs, and URLs observed by the Umbrella resolvers. This integration was integrated and tested with version 2.0.0 of Cisco Umbrella Investigate

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


## Cisco Umbrella Reporting

**Type:** integration  
**Product:** Cisco Umbrella Reporting  
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


## Cisco Webex Teams

**Type:** integration  
**Product:** Cisco Webex Teams  

Send messages, create rooms and more, via the Cisco Spark API. This integration was integrated and tested with version 6.2.0 of Cisco Spark

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


## Cisco WSA v2

**Type:** integration  
**Product:** Cisco WSA  

Cisco Secure Web Appliance protects your organization by automatically blocking risky sites and testing unknown sites before allowing users to click on them. This integration was integrated and tested with version 14.0.3-014 of Cisco WSA V2 Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

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


## Citrix Cloud

**Type:** integration  
**Product:** Citrix  
**Commands:**

- `None`: 


## Citrix DaaS

**Type:** integration  
**Product:** Citrix  

Citrix DaaS simplifies the delivery and management of Citrix technologies

**Commands:**

- `None`: 


## Clarizen IAM

**Type:** integration  
**Product:** Clarizen IAM  

Integrate with Clarizen's Identity Access Management service to execute CRUD operations in the employee lifecycle processes. For more information, refer to the Identity Lifecycle Management article

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 


## Code42

**Type:** integration  
**Product:** Code42  

Use the Code42 integration to identify potential data exfiltration from insider threats while speeding investigation and response by providing fast access to file events and metadata across physical and cloud environments

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


## Cofense Triage v3

**Type:** integration  
**Product:** Cofense Triage  

The Cofense Triage v3 integration uses the Cofense Triage v2 API (previous integrations were limited to Triage v1 API) that allows users to ingest phishing reports as incident alerts and execute commands. Security teams can ingest data from Triage such as email reporters, email reports and clusters, threat indicators, and rule matching to name a few. In addition, ingest and create threat indicators, categorize reports, and obtain second stage threat indicators from malicious emails. This integration was integrated and tested with version 1.22.0 of Cofense Triage. Some changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

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


## Cofense Vision

**Type:** integration  
**Product:** Cofense Vision  

The Cofense Vision integration provides commands to initiate advanced search jobs to hunt suspicious emails matching IOCs. It also contains commands to quarantine emails, download messages and their attachments, and aids to manage IOCs in the local repository to keep up with upcoming emerging threats. This integration was integrated and tested with version 4 of Cofense Vision and version 1 of Cofense IOC Repository

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## CohesityHelios

**Type:** integration  
**Product:** Cohesity Helios  

Integrate with Cohesity Helios services to fetch alerts and take remedial action. This integration was integrated and tested with version 08.01 of CohesityHelios

**Commands:**

- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 


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

- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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


## CounterCraft Deception Director

**Type:** integration  
**Product:** CounterCraft Deception Director  
**Commands:**

- `None`: 


## CounterTack

**Type:** integration  
**Product:** CounterTack  

CounterTack empowers endpoint security teams to assure endpoint protection for Identifying Cyber Threats. Integrating a predictive endpoint protection platform

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


## Covalence For Security Providers

**Type:** integration  
**Product:** Covalence For Security Providers  

Triggers by any alert from endpoint, cloud, and network security monitoring, with mitigation steps where applicable. Query Covalence for more detail. This integration was integrated and tested with version 3.0 of Covalence For Security Providers

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


## Covalence Managed Security

**Type:** integration  
**Product:** Covalence Managed Security  

Triggers by triaged alerts from endpoint, cloud, and network security monitoring. Contains event details and easy-to-follow mitigation steps. This integration was integrated and tested with version 1.1.10 of Covalence Managed Security

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

- `None`: 
- `None`: 


## Cribl Search

**Type:** integration  
**Product:** Cribl  

Cribl Search is a search solution that allows you to query, retrieve, and manage search jobs, datasets, and saved searches across your Cribl Cloud deployment. This integration was integrated and tested with version 4.17.0 of Cribl API

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


## CrowdSec

**Type:** integration  
**Product:** CrowdSec  

Identify Malicious IP addresses with the CrowdSec CTI API

**Commands:**

- `None`: 


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

- `None`: 
- `None`: 


## Cryptosim

**Type:** integration  
**Product:** Cryptosim  

CRYPTOSIM meets the SIEM needs of corporations by its unique correlation engine works in memory, capable of hierarchical correlation, supports different correlation techniques, query structure that allows all kinds of data analytics, detects AI based algorithms behavioral anomalies and threat patterns that are not in rule sets. From the personal devices we use to the most critical governmental substructures, the awareness of the importance of cyber threats in every segment of the digitalized world and the fact that cyber security must be in all areas of our lives becomes more and more obvious. The massive attacks on the global scale have clearly demonstrated the importance of taking measures against cyber threats and increasing investments on this area. CRYPTTECH continues to work towards the goal with the mission of developing new, innovative and indigenous technology and products in the increasingly complex cyber security world. CRYPTTECH provides its unique in-memory correlation capability for its SIEM product with its strong correlation system. CRYPTOSIM collects all logs, detects behavioral differences & anomalies and automatically associates them. More over it can catch APT (Advanced Persistent Threats). CRYPTTECH achieves high performance values for the SIEM product with its NoSQL structure developed by itself. CRYPTOSIM has become one of the most strategic products for perception of threats with its unique correlation features working with rules and machine learning m

**Commands:**

- `None`: 


## CSCDomainManager

**Type:** integration  
**Product:** CSCDomainSecurity  

CSCDomainManager uses rules-based technology, customizable reporting, granular user management, and more—and is the world's first multilingual domain management tool, available in English, French, and German. This integration was integrated and tested with version 2.0.0 of CSCDomainManager

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


## CSCFraudProtection

**Type:** integration  
**Product:** CSCDomainSecurity  

This is an anti fraud external api for organizations. This integration was integrated and tested with version v3 of the CSC Fraud Protection API

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


## CSCTakedowns

**Type:** integration  
**Product:** CSCDomainSecurity  

This is a CSCTakedowns api for organizations. This integration was integrated and tested with version v3 of the CSC Fraud Protection (Takedowns) API

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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


## CTM360 HackerView

**Type:** integration  
**Product:** CTM360  

External Attack Surface Management platform, which combines automated asset discovery, issue identification / management, remediation guidelines, security ratings and third party risk management. Use Module To Use to select which HackerView data source this instance fetches: This integration was integrated and tested with version 1.0.0 of CTM360_HackerView

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 


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


## CybelAngel EASM

**Type:** integration  
**Product:** CybelAngel  

This integration enables the platform, allowing security teams to monitor and respond to digital risk exposure incidents

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 


## Cyberhaven

**Type:** integration  
**Product:** Cyberhaven  

Fetches DLP incidents from the Cyberhaven data security platform and enables investigation of events and data lineage. This integration was integrated and tested with version 2 of Cyberhaven API

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Cyberpion Domain State

**Type:** playbook  
**Product:** Cyberpion  

Allows analyst to get basic information about the domain


## Cyberwatch

**Type:** integration  
**Product:** Cyberwatch  

Find, prioritize, and fix vulnerabilities on your IT & OT assets. This integration was integrated and tested with version 13.11 of Cyberwatch

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


## Cyble Vision Alert V2

**Type:** playbook  
**Product:** CybleEventsV2  

This is a playbook which will handle the alerts coming from the Cyble Events service


## CybleEvents v2

**Type:** integration  
**Product:** CybleEventsV2  

Cyble Events for Vision Users. Must have Vision API access to use the threat intelligence. This integration was integrated and tested with version 2.0 of cybleeventsv2

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## CyCognito

**Type:** integration  
**Product:** CyCognito  

The CyCognito integration fetches issues discovered by the CyCognito platform, thereby providing users with a view of their organization's internet-exposed attack surface. These issues include identification, prioritization, and recommendations for remediation of the risks faced by the organization. The integration contains commands to query assets and issues detected by the CyCognito platform, and includes a rich dashboard and layout with issue management capability. This integration was integrated and tested with CyCognito V1 API

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


## CyCognitoGetEndpoints

**Type:** script  
**Product:** CyCognito  

Generates a deep link to the CyCognito platform using the incident context


## Cymptom

**Type:** integration  
**Product:** Cymptom  

Cymptom is a Breach and Attack Simulation solution that revolutionizes the existing approach by transforming attack simulation into a data analysis question. Cymptom agentless scanning brings real-time always-on visibility into the entire security posture. This integration was integrated and tested with version 0.3.4 of Cymptom

**Commands:**

- `None`: 
- `None`: 


## Cymulate

**Type:** integration  
**Product:** Cymulate  
**Commands:**

- `None`: 


## Cymulate IOC Findings Mitigation

**Type:** playbook  
**Product:** Cymulate  

Cymulate IOC Findings Mitigation is a playbook that takes IOC (Indicator of Compromise) findings from the Cymulate Exposure Management platform and automates or guides mitigation actions to update controls and reduce security gaps quickly. It helps turn validated threat indicators into practical response steps within the platform


## Cyren Inbox Security

**Type:** integration  
**Product:** Cyren Inbox Security  

Cyren Inbox Security is an innovative solution that safeguards Office 365 mailboxes in your organization against evasive phishing, business email compromise (BEC), and fraud. This integration imports incidents from Cyren Inbox Security into platform, and includes a playbook for incident resolution. This integration was integrated and tested with version 1.0 of Cyren Inbox Security

**Commands:**

- `None`: 
- `None`: 
- `None`: 


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


## Darktrace AI Analyst

**Type:** integration  
**Product:** Darktrace  

Darktrace is a Cyber AI platform for threat detection and response across cloud, email, industrial, and the network. This integration was integrated and tested with version 6.0.0 of Darktrace

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Darktrace ASM

**Type:** integration  
**Product:** DarktraceASM  

Darktrace is a Cyber AI platform for threat detection and response across cloud, email, industrial, and the network. This integration was integrated and tested with version 6.0.0 of Darktrace

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


## DataBee

**Type:** integration  
**Product:** DataBee  

DataBee, from Comcast Technology Solutions, is a cloud-native security and compliance data fabric that ingests data from multiple disparate feeds and then aggregates, compresses, standardizes, enriches, correlates, and normalizes the data before transferring a full time-series dataset to your data lake of choice. This integration was integrated and tested with version 1.0 of DataBee

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Databricks

**Type:** integration  
**Product:** Databricks  

Comprehensive integration with Databricks workspace APIs for managing clusters, jobs, SQL, pipelines, Unity Catalog, MLflow, IAM, and more. This integration was integrated and tested with the Databricks REST API

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


## Dataminr Pulse

**Type:** integration  
**Product:** Dataminr Pulse  
**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Dataminr Pulse - ReGenAI

**Type:** integration  
**Product:** Dataminr Pulse  
**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 


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

- `None`: 
- `None`: 


## DeCYFIR - v1

**Type:** playbook  
**Product:** DeCYFIR  

DeCYFIR API's provides External Threat Landscape Management insights


## Deep Instinct

**Type:** integration  
**Product:** DeepInstinct  
**Commands:**

- `None`: 


## DeepInstinct v3

**Type:** integration  
**Product:** DeepInstinct  

Deep Instinct is a prevention-first approach to stopping ransomware and other malware using the world's first purpose-built, deep learning cybersecurity framework. This integration was integrated and tested with version 3.3.x of DeepInstinct v3

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


## DeepL

**Type:** integration  
**Product:** DeepL  

This integration uses DeepL ( to translate text or files This integration was integrated and tested with DeepL

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 


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

- `None`: 


## DelineaSS

**Type:** integration  
**Product:** Delinea Secret Server  

Secret Server and Platform is the fully featured Privileged Account Management (PAM) solution available both on premise and in the cloud. It empowers security and IT ops teams to secure and manage all types of privileged accounts and offers the fastest time to value of any PAM solution. This integration was integrated and tested with version 5.0 of Delinea

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## DFIRe

**Type:** integration  
**Product:** DFIRe  

DFIRe is a self-hosted Digital Forensics and Incident Response (DFIR) case management platform built for security professionals. It provides structured case management, evidence tracking with chain of custody, IOC indicator management, and incident response workflows aligned with the NIST Incident Response framework — all running on your own infrastructure with AES-256 encryption. This integration connects Cortex XSIAM and the platform, enabling automated case creation and updates, bi-directional IOC indicator synchronization, evidence item tracking, file attachment uploads, and timeline enrichment directly from playbooks

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

- `None`: 
- `None`: 


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

- `None`: 


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

- `None`: 
- `None`: 


## DNSOverHttps

**Type:** integration  
**Product:** DNSOverHttps  

Query dns names over https from Cloudflare or Google

**Commands:**

- `None`: 
- `None`: 


## Docker Engine API

**Type:** integration  
**Product:** DevSecOps  

The Engine API is an HTTP API served by Docker Engine. It is the API the Docker client uses to communicate with the Engine, so everything the Docker client can do can be done with the API. This integration was integrated and tested with version 20.10.17 (API Version 1.41) of Docker Engine API

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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


## DomainTools Iris Detect

**Type:** integration  
**Product:** DomainTools Iris Detect  

Iris Detect is an Internet infrastructure detection, monitoring, and enforcement tool built on the industry’s fastest and broadest domain discovery engine and the largest databases of domain data. Capturing key data on new domains and risk-scoring them within minutes of discovery, Detect is a game-changer for brand managers, digital risk and fraud prevention teams, and network defenders. Rapid Discovery of Infringing Domains Continuous Monitoring of Evolving Infrastructure Enforcement Actions for Dangerous Domains Iris Detect employs the most sophisticated and extensive new-domain discovery capabilities, across all TLDs globally. Domains are enriched with preliminary Whois, DNS, and Risk Score data. The Iris Detect for the platform, incidents containing mapped indicators of newly-discovered domains matching the monitored keywords. Through ad-hoc War-Room commands or on the incidents directly, domains of interest may be added to Iris Detect’s Watchlist, which triggers automatic daily updates, looking for hosting infrastructure or webpage changes. These changes can be consumed as their own incidents or sent to a separate workflow, giving you the ability to track evolving threat campaigns, classify, and identify which domains are most likely to do harm. Merely knowing about malicious infrastructure is not enough. Iris Detect offers impactful enforcement options: Block flagged domains from incidents directly or using ad-hoc

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

- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 


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


## DuoAuth

**Type:** integration  
**Product:** DuoAuth  

The Duo Auth API lets developers integrate with Duo Security's platform at a low level

**Commands:**

- `None`: 


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

- `None`: 
- `None`: 
- `None`: 


## Endace

**Type:** integration  
**Product:** Endace  

The EndaceProbe Analytics Platform provides 100% accurate, continuous packet capture on network links up to 100Gbps, with unparalleled depth of storage and retrieval performance. Coupled with the Endace InvestigationManager, this provides a central search and data-mining capability across a fabric of EndaceProbes deployed in a network. This integration uses Endace APIs to search, archive and download PCAP file from either a single EndaceProbe or many via the InvestigationManager and enables integration of full historical packet capture into security automation workflows. This integration was integrated and tested with version 6.5.7 & 7.0.0 of Endace

**Commands:**

- `None`: 


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


## Entra ID Users

**Type:** integration  
**Product:** Microsoft Graph User  

The Entra ID Users integration (formerly Azure Active Directory Users) is a Unified gateway to security insights - all from a unified Microsoft Graph User API

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


## Envoy IAM

**Type:** integration  
**Product:** Envoy  

Integrate with Envoy Identity Access Management services to execute CRUD operations to employee lifecycle processes. This integration was integrated and tested with version v2 of Envoy SCIM API

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


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


## EWS v2

**Type:** integration  
**Product:** Microsoft Exchange On-Premise  

Exchange Web Services (EWS) provides the functionality to enable client applications to communicate with the Exchange server. EWS provides access to much of the same data that is made available through Microsoft Office Outlook. The EWS v2 integration implants EWS leading services. The integration allows getting information on emails and activities in a target mailbox, and some active operations on the mailbox such as deleting emails and attachments or moving emails from folder to folder. Note: Starting from pack version 2.0.0 the EWS v2 integration requires the Exchange server to support TLS v1.2 and up in order to connect. Multi-Factor Authentication (MFA) EWS v2 does not support Multi-Factor Authentication (MFA). If using MFA, use EWS O365 (see  or if you have Graph Outlook use O365 Outlook Mail (Using Graph API) (see  or O365 Outlook Mail Single User (Using Graph API) (see

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


## EWSApiModule

**Type:** script  

The EWS API Module handles generic logic for interacting with an EWS Server. It provides a client class for interacting with the EWS API as well as common methods for performing various EWS related operations such as getting or sending items, retrieving attachments, creating/updating/deleting folders, and more. To use the EWS API module, you'll need to follow these steps: For examples, see the EWSO365 and EWSv2 integrations


## Exabeam Advanced Analytics

**Type:** integration  
**Product:** Exabeam Advanced Analytics  

The Exabeam Security Management Platform provides end-to-end detection, User Event Behavioral Analytics and SOAR. This integration was integrated and tested with version 53.5 of Exabeam. There are 2 authentication methods: For additional information, refer to Exabeam Administration Guide

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


## Exabeam Data Lake

**Type:** integration  
**Product:** ExabeamDataLake  

Exabeam Data Lake provides a searchable log management system. Data Lake is used for log collection, storage, processing, and presentation. This integration was integrated and tested with version LMS-i40.3 of Exabeam Data Lake

**Commands:**

- `None`: 
- `None`: 


## Exabeam Security Operations Platform

**Type:** integration  
**Product:** Exabeam Security Operations Platform  

Exabeam Security Operations Platform offers a centralized and scalable platform for log management. This integration was integrated and tested with version v1.0 of ExabeamSecOpsPlatform

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 


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


## ExtraHopTrackIncidents

**Type:** script  
**Product:** ExtraHop Reveal(x)  

Links an incident investigation back to the ExtraHop Detection that created it


## F5 LTM

**Type:** integration  
**Product:** F5 LTM  

Manages F5 LTM This integration was integrated and tested with version 16.1.0 of F5LTM

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


## F5 Silverline

**Type:** integration  
**Product:** F5 Silverline  

F5 Silverline Threat Intelligence is a cloud-based service incorporating external IP reputation and reducing threat-based communications. By identifying IP addresses and security categories associated with malicious activity, this managed service integrates dynamic lists of threatening IP addresses with the Silverline cloud-based platform, adding context-based security to policy decisions

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## FailedInstances

**Type:** script  
**Product:** Common Scripts  

Executes a test for all integration instances available and returns a detailed table with information about any failed integration instances. The script runs on all enabled instances, regardless of whether the “Do not use by default in CLI” checkbox is selected


## Farsight DNSDB

**Type:** integration  
**Product:** Farsight DNSDB  

This integration uses Farsight Security’s DNSDB solution to interactively lookup rich, historical DNS information – either as playbook tasks or through API calls in the War Room – to access rdata and rrset records

**Commands:**

- `None`: 
- `None`: 


## Farsight DNSDB v2

**Type:** integration  
**Product:** Farsight DNSDB  

Farsight Security DNSDB® is the world’s largest DNS intelligence database that provides a unique, fact-based, multifaceted view of the configuration of the global Internet infrastructure. DNSDB leverages the richness of Farsight’s Security Information Exchange (SIE) data-sharing platform and is engineered and operated by leading DNS experts. Farsight collects Passive DNS data from its global sensor array. It then filters and verifies the DNS transactions before inserting them into the DNSDB, along with ICANN-sponsored zone file access download data. The end result is the highest-quality and most comprehensive DNS intelligence data service of its kind - with more than 100 billion DNS records since 2010. This integration uses Farsight Security’s DNSDB solution to interactively lookup rich, historical DNS information – either as playbook tasks or through API calls in the War Room – to access rdata and rrset records. It was integrated and tested with version 2 of the DNSDB API

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

- `None`: 


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

- `None`: 


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


## FireEye Endpoint Security (HX) v2

**Type:** integration  
**Product:** FireEye HX  

FireEye Endpoint Security is an integrated solution that detects what others miss and protects endpoint against known and unknown threats. This integration provides access to information about endpoints, acquisitions, alerts, indicators, and containment. Customers can extract critical data and effectively operate security operations automated playbook Some changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

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


## FireEye Helix

**Type:** integration  
**Product:** FireEye Helix  

Use the FireEye Helix integration to integrate security tools and arguments with next-generation SIEM, orchestration and threat intelligence tools such as alert management, search, analysis, investigations and reporting. In order to configure this integration you must have a FireEye customer ID. Your customer ID will placed in the FireEye Helix URL of your FireEye Helix app after /helix/id/. e.g. for the following URL  the customer ID is "helixid". The API key can be found and generated in the API KEYS section. You can navigate to it from your FireEye Helix app home page by clicking on the user icon on the top right, and choosing HELIX Settings. You'll be redirected to the HELIX Settings page, where API KEYS can be found

**Commands:**

- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 


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


## Forescout EyeInspect

**Type:** integration  
**Product:** Forescout EyeInspect  
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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## FortiAuthenticator

**Type:** integration  
**Product:** FortiAuthenticator  

FortiAuthenticator provides centralized authentication services. Seamless secure two-factor/OTP authentication across the organization in conjunction with FortiToken. This integration was integrated and tested with versions 4.0 - 6.3.0 of FortiAuthenticator

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## FortiGate

**Type:** integration  
**Product:** FortiGate  

FortiGate provides flawless convergence that can scale to any location: remote office, branch, campus, data center, and cloud. FortiGate always delivered on the concept of hybrid mesh firewalls with FortiManager for unified management and consistent security across complex hybrid environments. The Fortinet FortiOS operating system provides deep visibility and security across a variety of form factors. This integration was integrated and tested with version 7.2.5 of FortiGate

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## FortiMail

**Type:** integration  
**Product:** Fortimail  

FortiMail is a comprehensive email security solution by Fortinet, offering advanced threat protection, data loss prevention, encryption, and email authentication to safeguard organizations against email-based cyber threats and protect sensitive information. This integration was integrated and tested with version 7.4 of fortimail

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


## FortiManager

**Type:** integration  
**Product:** FortiManager  

FortiManager is a single console central management system that manages Fortinet Devices. This integration was integrated and tested with version 6.2.2 of FortiManager

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

- `None`: 
- `None`: 
- `None`: 


## Fortiweb VM

**Type:** integration  
**Product:** Fortinet Fortiweb  

Fortiweb VM integration allows to manage WAF policies and block cookies, URLs, and host names. This integration was integrated and tested with version 1 & 2 of fortiweb_vm

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


## Freshworks Freshservice

**Type:** integration  
**Product:** Freshworks Freshservice  

Freshservice is a service management solution that allows customers to manage service requests, incidents, change requests tasks, and problem investigation. This integration was integrated and tested with version 2 of FreshworksFreshservice

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


## FTP

**Type:** integration  
**Product:** FTP  

FTP integration to download or upload files to a remote FTP server. Please note that FTP transfer is insecure. Please use it with care

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## G Suite Auditor

**Type:** integration  
**Product:** GsuiteAuditor  

G Suite Auditor is an integration that receives audit logs from G Suite's different applications - admin, drive, calendar, and more

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## G Suite Security Alert Center

**Type:** integration  
**Product:** G Suite Security Alert Center  

G Suite Security Alert Center allows users to fetch different alert types such as Suspicious login, Device compromised, Leaked password, and more. Users can delete or recover a single alert or a batch of alerts and retrieve the alert's metadata. This integration allows users to provide feedback for alerts and fetch existing feedback for a particular alert. This integration was integrated and tested with version v1beta1 dated Oct 15, 2018 of Google Workspace Alert Center. Supported the platform.0.0 and later

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


## Gamma

**Type:** integration  
**Product:** Gamma  

Gamma Enterprise DLP provides 1-click automatic discovery and remediation of data loss instances across enterprise sanctioned SaaS applications (cloud and on-prem) such as: Slack, Github, GSuite (Gmail, GDrive), Atlassian Suite (Jira, Confluence), Microsoft Office 365 (Outlook, Teams, OneDrive), ServiceNow, ZenDesk and many more

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## GatewatcherAlertEngine

**Type:** script  
**Product:** Gatewatcher AionIQ  

Automation script for displaying engine fields on the Alert layout


## GCenter

**Type:** integration  
**Product:** Gatewatcher AionIQ  

This integration allows, via about twenty commands, to interact with the GCenter appliance via its API. This integration was integrated and tested with version v2.5.3.102 of GCenter. To simplify GCenter v2.5.3.102 is called GCenter in the Pack

**Commands:**

- `None`: 


## GCenter 103

**Type:** integration  
**Product:** Gatewatcher AionIQ  

This integration fetch events generated by the GCenter appliance. This integration was integrated and tested with version 2.5.3.103 of GCenter 103

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


## Gem

**Type:** integration  
**Product:** Gem  

Use Gem alerts as a trigger for the platform, to automate response to specific TTPs

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

- `None`: 


## Generic MCP

**Type:** integration  
**Product:** Generic MCP  

Use this integration to connect to an MCP server and automatically discover its available tools

**Commands:**

- `None`: 
- `None`: 


## Generic SQL

**Type:** integration  
**Product:** GenericSQL  

Generic SQL integration for the Databases: MySQL, PostgreSQL, Microsoft SQL Server, Oracle, Teradata and Trino

**Commands:**

- `None`: 


## Genians

**Type:** integration  
**Product:** Genians  

Use the Genian NAC integration to block IP addresses using the assign tag. Genian NAC network sensing technology powered by Device Platform Intelligence (DPI) discovers and presents all detected devices’ business contextual and risk-related information along with their technical information without disturbing existing network infrastructure. The resulting intelligence enhances visibility and allows operators to detect and respond to any non-compliant or compromised devices in real time. With the result of comprehensive network visibility, Genian NAC can ensure compliance from all connected devices by leveraging Virtual In-Line Packet Inspection which operates at Layer 2. This technology has complete control over endpoint device traffic over TCP and UDP by eliminating the need for complex configurations and network changes

**Commands:**

- `None`: 
- `None`: 


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

- `None`: 


## GitHub IAM

**Type:** integration  
**Product:** GitHub  

Note: This integration should be used as part of our IAM premium pack. For further details, visit our IAM pack documentation. GitHub Integration consists of a set of API endpoints that enable you to automate provisioning of GitHub organization membership. This integration was integrated and tested with version v2 of GitHub IT Admin. For more information, please refer to the Identity Lifecycle Management article

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## GLIMPS Detect

**Type:** integration  
**Product:** GLIMPS Detect  

Use the GLIMPS Detect Integration to send files to GLIMPS Malware and get results from it This integration was integrated and tested with version 0.2.0 of gdetect client

**Commands:**

- `None`: 


## GLPI

**Type:** integration  
**Product:** GLPI  

GLPI open source ITSM solution This integration was integrated and tested with version 9.5.5 of GLPI

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


## GLPIIncidentStatus

**Type:** script  
**Product:** GLPI  

populates the value of the GLPI Ticket State field and display it in a layout widget


## Gmail

**Type:** integration  
**Product:** Gmail  

Use the Gmail integration to search and process emails in your organization's Gmail mailboxes. This integration replaces the Gmail functionality in the GoogleApps API and G Suite integration. You need to do the following in Google before configuring your integration instance in the platform. Both the Gmail API and the Admin SDK API are required to use this integration.  To revoke or fetch a user role, you need an Immutable Google Apps ID

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


## Gmail Single User

**Type:** integration  
**Product:** Gmail Single User  

Use the Gmail Single User integration to send emails and fetch emails as incidents to the platform. Note: Use this integration if you only want to fetch and send emails from a single user's mailbox. If you need to access multiple user mailboxes, use the GMail Integration

**Commands:**

- `None`: 


## Google Chat via Webhook

**Type:** integration  
**Product:** Google Chat via Webhook  

Integration for sending notifications to a Google Chat space via Incoming Webhook

**Commands:**

- `None`: 
- `None`: 


## Google Docs

**Type:** integration  
**Product:** Google Docs  

Use the Google Docs integration to create and modify Google Docs documents

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Google Dorking

**Type:** integration  
**Product:** Google Dorking  

Automate the process of google dorking searches in order to detect leaked data

**Commands:**

- `None`: 


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


## Google Drive (Standard Connector)

**Type:** integration  
**Product:** Google Drive (Standard Connector)  

Google Drive allows users to store files on their servers, synchronize files across devices, and share files. This integration helps you to create a new drive, query past activity, and view change logs performed by the users. This integration was integrated and tested with version 1.31.0 of GoogleDrive

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


## Google Gemini

**Type:** integration  
**Product:** Google Gemini  

This integration provides access to Google Gemini's large language models for AI-powered analysis and chat capabilities in the platform. Supports both Google AI Studio (API key) and Google Cloud Vertex AI (service account) authentication

**Commands:**

- `None`: 


## Google Key Management Service

**Type:** integration  
**Product:** Google Key Management Service  

Use the Google Key Management Service API for CryptoKey management and encrypt/decrypt functionality

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


## Google Maps

**Type:** integration  
**Product:** Google Maps  

Use the Google Maps API. This integration was integrated and tested with version 3.43 of the Google Maps API. This integration always uses the latest API version

**Commands:**

- `None`: 
- `None`: 


## Google Safe Browsing v2

**Type:** integration  
**Product:** Google Safe Browsing  

Search Safe Browsing v4

**Commands:**

- `None`: 
- `None`: 


## Google SecOps Cases

**Type:** integration  
**Product:** Google SecOps  

Use the Google SecOps Cases integration to retrieve Cases as Incidents. This integration also provides commands to manage the Cases lifecycle. This integration was integrated and tested with version v1 Alpha of Google SecOps API

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


## Google SecOps v1 Alpha

**Type:** integration  
**Product:** Google SecOps  

Use the Google SecOps integration to retrieve IOC Domain matches as Incidents. This integration also provides reputation and threat enrichment of indicators observed in the enterprise. This integration was integrated and tested with version v1 Alpha of GoogleSecOps. Note: The commands will do up to 3 internal retries with a gap of 15, 30, and 60 seconds (exponentially) between the retries. If you are upgrading from a Google Chronicle Backstory integration, please refer to the Migration Guide for guidance

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


## Google Sheets

**Type:** integration  
**Product:** Google Sheets  

Google Sheets is a spreadsheet program that is part of the free web-based Google applications to create and format spreadsheets. Use this integration to create and modify spreadsheets. This integration was integrated and tested with version 4 of Google Sheets API

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

- `None`: 


## Google Workspace Admin

**Type:** integration  
**Product:** G Suite Admin  

G Suite or Google Workspace Admin is an integration to perform an action on IT infrastructure, create users, update settings, and more administrative tasks. This integration was integrated and tested majorly with G Suite Basic edition

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


## GoogleApps API and G Suite

**Type:** integration  

Use the GoogleApps API and G Suite integration to help administrators migrate to G Suite, create custom usage reports, and manage users, groups, and devices. NOTE: The googleapps-gmail commands are deprecated, to execute Gmail commands, use the Gmail integration

**Commands:**

- `None`: 


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


## GRAIncidentAnomaliesDisplay

**Type:** script  
**Product:** Gurucul Risk Analytics  

Displays and refreshes GRA incident anomaly details


## GraphQL

**Type:** integration  
**Product:** GraphQL  

Generic GraphQL client to interact with any GraphQL server API

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


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


## Graylog

**Type:** integration  
**Product:** Graylog  

Integration with Graylog to search for logs and events This integration was integrated and tested with version 3.3.6 of Graylog

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## GreyNoise

**Type:** integration  
**Product:** GreyNoise  

GreyNoise is a cybersecurity platform that collects and analyzes Internet-wide scan and attack traffic. With this integration, users can contextualize existing alerts, filter false-positives, identify compromised devices, and track emerging threats. This integration was integrated and tested with version 3.0.0 of the GreyNoise SDK. Supported the platform.0.0 and later

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


## GreyNoise Community

**Type:** integration  
**Product:** GreyNoise  

GreyNoise tells security analysts what not to worry about. We do this by curating data on IPs that saturate security tools with noise. This unique perspective helps analysts confidently ignore irrelevant or harmless activity, creating more time to uncover and investigate true threats. The Action allows IP enrichment via the GreyNoise Community API. The GreyNoise Integration should be used by customers with a paid subscription to GreyNoise with the exception of the IP command, which is available with limit results to free users. This integration was integrated and tested with version 3.0.0 of GreyNoise Python SDK. Supported the platform.0.0 and later

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Gurucul-GRA

**Type:** integration  
**Product:** Gurucul Risk Analytics  

Gurucul Risk Analytics (GRA) is a data science backed cloud native platform that predicts, detects and prevents breaches. It ingests and analyzes massive amounts of data from the network, IT systems, cloud platforms, EDR, applications, IoT, HR and much more to give you a comprehensive contextual view of user and entity behaviors. This integration fetches GRA Incidents or Alerts into Cortex and exposes War Room commands for investigation and actions. Workflows can be configured in Cortex based on the commands provided by GRA. Please make sure you look at the integration source code and comments

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 


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


## Halcyon

**Type:** integration  
**Product:** Halcyon  

Halcyon is a device management platform that helps organizations monitor, control, and secure their network of devices. It provides centralized tools for overseeing hardware and software inventory, deploying updates, enforcing security policies, and ensuring compliance across device environments. This integration fetches alerts and events from the Halcyon platform and ingests them into Cortex XSIAM

**Commands:**

- `None`: 


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


## HashiCorp Vault

**Type:** integration  
**Product:** HashiCorp Vault  

Secure, store, and tightly control access to tokens, passwords, certificates, and encryption keys for protecting secrets and other sensitive data using HashiCorp Vault. This integration fetches credentials. For more information, see Managing Credentials. This integration was integrated and tested with version 1.12.2 of HashiCorp Vault

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


## Hatching Triage

**Type:** integration  
**Product:** Hatching Triage  

Submit a high volume of samples to run in a sandbox and view reports This integration was integrated and tested with version 0 of Hatching Triage

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


## Have I Been Pwned? v2

**Type:** integration  
**Product:** Pwned  
**Commands:**

- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Hello World v2

**Type:** integration  
**Product:** HelloWorld  
**Commands:**

- `None`: 


## HelloWorld

**Type:** integration  
**Product:** HelloWorld  

This is the Hello World integration for getting started

**Commands:**

- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## HPE Aruba ClearPass

**Type:** integration  
**Product:** HPE Aruba Clearpass  

Aruba ClearPass Policy Manager provides role and device-based network access control for employees, contractors, and guests across any multi-vendor wired, wireless, and VPN infrastructure. This integration was integrated and tested with version 6.9 of HPE Aruba ClearPass

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

- `None`: 
- `None`: 
- `None`: 


## Humio

**Type:** integration  
**Product:** Humio  

Integration with Humio

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


## IAMApiModule

**Type:** script  

To use the common IAM API logic, run the following command to import the IAMApiModule. Then, the IAMApiModule will be available for usage. For examples, see the Workday IAM or Okta IAM integrations. The IAMApiModule contains the following classes


## IBM MaaS360 Security

**Type:** integration  
**Product:** IBM MaaS360 Security  

This is the IBM MaaS360 Security integration for Cortex XSIAM

**Commands:**

- `None`: 
- `None`: 


## IBM Security Guardium

**Type:** integration  
**Product:** IBM Guardium  

IBM Security Guardium is a comprehensive data security platform that provides visibility and protection for sensitive data across databases, data warehouses, big data platforms, and cloud environments. This integration enables the collection of security events from IBM Guardium Data Security Center

**Commands:**

- `None`: 
- `None`: 


## IBM Security Verify

**Type:** integration  
**Product:** IBM Security Verify  

IBM Security Verify provides a secure and scalable solution for collecting and managing security events from IBM Security Verify, offering advanced threat detection and response capabilities for protecting identities, applications, and data

**Commands:**

- `None`: 


## IBM X-Force Exchange v2

**Type:** integration  
**Product:** IBM X-Force Exchange  

IBM X-Force Exchange lets you receive threat intelligence about applications, IP addresses, URls and hashes

**Commands:**

- `None`: 


## iboss

**Type:** integration  
**Product:** iboss  

Manage block lists, manage allow lists, and perform domain, IP, and/or URL reputation and categorization lookups. This integration was integrated and tested with version 9.8.38.245 of iboss Zero Trust Secure Service Edge

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

- `None`: 
- `None`: 
- `None`: 


## Image OCR

**Type:** integration  
**Product:** Image OCR  

Use the Image OCR integration to extract text from images. The integration utilizes the open-source tesseract OCR engine

**Commands:**

- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Imperva Incapsula

**Type:** integration  
**Product:** Imperva Incapsula  

Uses incapsula to manage sites and IPs

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


## Imperva Skyfence

**Type:** integration  
**Product:** Imperva Skyfence  

The Imperva Skyfence Cloud Gateway is a Cloud Access Security Broker (CASB) that provides visibility and control over sanctioned and unsanctioned cloud apps to enable their safe and productive use. This integration was integrated and tested with version 1.0.8 of Imperva Skyfence

**Commands:**

- `None`: 
- `None`: 


## Imperva WAF

**Type:** integration  
**Product:** Imperva WAF  

Use the Imperva WAF integration to manage IP groups and Web security policies in Imperva WAF. This integration was integrated and tested with version 14.2 of Imperva WAF and based on Imperva On-Premises WAF (SecureSphere) REST API

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

- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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


## Infoblox NIOS

**Type:** integration  
**Product:** Infoblox NIOS  

Infoblox NIOS enables you to receive metadata about IPs in your network and manages the DNS Firewall by configuring RPZs. It defines RPZ rules to block DNS resolution for malicious or unauthorized hostnames, or redirect clients to a walled garden by substituting responses. This integration was integrated and tested with version V2 of Infoblox

**Commands:**

- `None`: 


## Infocyte

**Type:** integration  
**Product:** Infocyte  

Infocyte can pivot off incidents to automate triage, validate events with forensic data and enabling dynamic response actions against any or all host using both agentless or agented endpoint access. This integration was integrated and tested with version 3008.0.1.2800 of Infocyte

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

- `None`: 


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

- `None`: 
- `None`: 


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

- `None`: 


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


## Ironscales

**Type:** integration  
**Product:** Ironscales  

IRONSCALES, a self-learning email security platform integration

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## Ironscales-Classify-Incident

**Type:** playbook  
**Product:** Ironscales  

## IsMalicious

**Type:** integration  
**Product:** IsMalicious  

Enrich IP, domain, URL and file-hash indicators with IsMalicious reputation, evidence and data-trust context. This integration uses the public IsMalicious REST API contract. Local validation uses synthetic provider responses and the real CommonServerPython framework; no production the platform. API checks consume the applicable account quota. Unknown hashes, delisted indicators and absent supported verdicts remain DBotScore 0; risk and confidence are separate fields. See the pack README for evidence interpretation and limits

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Ivanti Heat

**Type:** integration  
**Product:** Ivanti Heat  

Ivanti Heat service manager This integration was integrated and tested with version 2020.1.0.20200313 of Ivanti Heat

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Ja3er

**Type:** integration  
**Product:** Ja3er  

Query the ja3er API for MD5 hashes of JA3 fingerprints

**Commands:**

- `None`: 
- `None`: 


## JAMF v2

**Type:** integration  
**Product:** Jamf  

Enterprise Mobility Management (EMM) for Apple devices (Mac, iPhone, Apple TV, iPad). Can be used to control various configurations via different policies, install and uninstall applications, lock devices, smart groups searches, and more. This integration was integrated and tested with version 10.28.0 of jamf v2 JAMF classic API:  JAMF Pro API:  Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

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


## JARM

**Type:** integration  
**Product:** JARM  

Active TLS fingerprinting using JARM

**Commands:**

- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 


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

- `None`: 


## JWT

**Type:** integration  
**Product:** JWT Token Generator  

JSON Web Token (JWT) is a compact, URL-safe means of representing claims to be transferred between two parties. This Integration can be used to Generate New JWT Tokens, Encode and Decode Existing Ones. This integration was integrated and tested with generic JWT authentication service

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Kafka v3

**Type:** integration  
**Product:** Kafka  

Use the Kafka integration to manage messages and partitions and to fetch Kafka messages to create incidents in the platform. This integration was integrated and tested with version 2.7.1 of Kafka. This integration is fully compatible with the Kafka v2 integration

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Kaspersky Security Center (Beta)

**Type:** integration  
**Product:** Kaspersky Security Center  

The administration console for controlling all Kaspersky Lab security solutions and system administration tools. This integration was integrated and tested with version 12 of Kaspersky Security Center. Note: The integration is in beta because it only covers a subset of the endpoints and API use cases

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


## Keeper Secrets Manager

**Type:** integration  
**Product:** Keeper Secrets Manager  

Manage Secrets and Protect Sensitive Data through Keeper Vault. This integration was integrated and tested with version 16.3.5 of Keeper Secrets Manager

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Keeper Security

**Type:** integration  
**Product:** Keeper Security  

Use this integration to fetch audit logs from Keeper Security Admin Console as XSIAM events. This integration was integrated and tested with version 16.11.8 of Keeper Commander

**Commands:**

- `None`: 
- `None`: 
- `None`: 


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


## KOI

**Type:** integration  
**Product:** KOI  
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


## Koodous

**Type:** integration  
**Product:** Koodous  

Check Android app samples (APK) against Koodous API

**Commands:**

- `None`: 


## Lacework

**Type:** integration  
**Product:** Lacework  

Lacework provides end-to-end cloud security automation for AWS, Azure, and GCP with a comprehensive view of risks across cloud workloads and containers. This integration was integrated and tested with version 2 of the Lacework APIs

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 


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

- `None`: 


## Linux

**Type:** integration  
**Product:** Ansible Linux  

This integration enables the management of Linux hosts directly from platform using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration functions without any agents or additional software installed on the hosts by utilising SSH combined with Python. To use this integration, configure an instance of this integration. This will associate a credential to be used to access hosts when commands are run. The commands from this integration will take the Linux host address(es) as an input, and use the saved credential associated to the instance to execute. Create separate instances if multiple credentials are required

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 


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


## LogRhythmRest v2

**Type:** integration  
**Product:** LogRhythm  

LogRhythm security intelligence. This integration was integrated and tested with version 7.7 of LogRhythm Rest API. Previous versions that have been declared EOL by the vendor, are not supported. Some changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

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

- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Lumu

**Type:** integration  
**Product:** Lumu  

SecOps operations - Reflect and manage the Lumu Incidents either from platform Cortex or viceversa using the mirroring integration flow,  This integration was integrated and tested with version 20230215 of Lumu

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


## Lumu Secops

**Type:** integration  
**Product:** Lumu  

SecOps operations for the new Lumu Defender API. Fetch, investigate, and manage Lumu incidents from the platform. This integration was integrated and tested with new Lumu Defender SecOps API

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

- `None`: 


## Magnet Automate Beta

**Type:** integration  
**Product:** Magnet Forensics  

Magnet Automate is an orchestration and automation platform that accelerates your digital forensics investigations by automating workflows and integrating with various forensic tools. This integration was integrated and tested with version 0.2.0 of Magnet Automate API

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


## Mail Listener v2

**Type:** integration  
**Product:** Mail Listener  
**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## ManageEngine

**Type:** integration  
**Product:** ManageEngine  

ManageEngine Endpoint Central is a Unified Endpoint Management solution that helps in managing thousands of servers, desktops, laptops and mobile devices from a single console. This integration serves as an Event Collector for Cortex XSIAM, enabling fetching AuditLogs from Endpoint Central. Endpoint Central cloud is hosted at multiple data centers, and therefore available on different domains. There are several domains for Endpoint Central Cloud APIs, so you can use the one that is applicable to you. The APIs on this page are intended for organizations hosted on the .com domain. If your organization is on a different domain, replace “.com” with the appropriate domain for the API endpoints before using them. Note: You can also find out which domain you’re accessing by checking the URL while logged in to Endpoint Central

**Commands:**

- `None`: 
- `None`: 


## ManageEngine PAM360

**Type:** integration  
**Product:** ManageEngine_PAM360  

Use ManageEngine PAM360, a privileged access management solution to manage critical enterprise data such as privileged resources and accounts and secure credentials from the platform

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Mandiant Automated Defense (Formerly Respond Software)

**Type:** integration  
**Product:** Mandiant Automated Defense  

Disclaimer: Respond Software was recently acquired by FireEye and has rebranded from the Respond Analyst to the Mandiant Defense Engine. These terms refer to the same product. Most of this integration was written prior to rebranding, and primarily includes references to Respond. This will be updated in the future, at which point this disclaimer will be removed. Mandiant Defense is the cybersecurity investigation automation solution that connects the dots across disparate cybersecurity data to find real incidents fast. The Mandiant Defense engine is built to accelerate investigations for security operations teams in defense agencies, government bodies, universities, large enterprises, and leading managed service providers to get investigation power at machine speed. Mandiant Defense works with the broadest range of vendors, sensors, threat intelligence and data repositories in the industry to improve detection and response while raising security analyst productivity. This pack provides a set of commands which can be executed against an instance of the Respond Analyst. The commands allow users to retrieve information from Respond and modify incidents from within platform. Additionally, this integration supports bi-directional mirroring (for platform v6 and above) of When fetch incidents is enabled, the pack will pull all open incidents from Respond into platform. Each incident in platform will follow the naming convention <Respond Tenant Id>:<Respond Incident Id> It is worth noting that th

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 


## McAfee DXL

**Type:** integration  
**Product:** McAfee DXL  

Use the McAfee DXL integration to connect and optimize security actions across multiple vendor products

**Commands:**

- `None`: 


## McAfee ePO Endpoint Connectivity Diagnostics Playbook v2

**Type:** playbook  
**Product:** McAfee ePO  

Perform a check on ePO endpoints to see if any endpoints are unmanaged or lost connectivity with ePO and take steps to return to a valid state


## McAfee ePO v2

**Type:** integration  
**Product:** McAfee ePO  

McAfee ePolicy Orchestrator This integration was integrated and tested with version 5.3.2 and 5.10 of McAfee ePO

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


## McAfee ESM v2

**Type:** integration  
**Product:** McAfee ESM  

Run queries and receive alarms from Trellix (McAfee) ESM. This integration was tested with version 11.6 of McAfee ESM v2. Versions earlier than 11.6 are not supported, as they reached Trellix end-of-life. Starting with ESM 11.6.11, the login API requires the username and password to be AES-encrypted. Enter the version number of your ESM instance in the Version parameter — the integration applies AES encryption automatically for versions 11.6.11 and later; no manual encryption is required

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


## McAfee NSM v2

**Type:** integration  
**Product:** McAfee NSM  

McAfee Network Security Manager gives you real-time visibility and control over all McAfee intrusion prevention systems deployed across your network. This integration was integrated and tested with version 9.1 of McAfeeNSMv2 Some changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

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

- `None`: 


## Micro Focus Service Manager

**Type:** integration  
**Product:** Micro Focus Service Manager  

Service Manager By Micro Focus (Formerly HPE Software)

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


## MicroFocus SMAX

**Type:** integration  
**Product:** MicroFocus SMAX  

Fetch SMAX incidents, requests and automate different SMAX case management actions This integration was integrated and tested with version 2021.08 of MicroFocus SMAX

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


## Microsoft Endpoint Configuration Manager

**Type:** integration  
**Product:** Microsoft Endpoint Configuration Manager  
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


## Microsoft Endpoint Manager (Intune)

**Type:** integration  
**Product:** Microsoft Graph Device Management  

Microsoft Intune is a Microsoft cloud-based management solution that provides for mobile device and operating system management

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


## Microsoft Graph Mail Single User

**Type:** integration  
**Product:** Microsoft Graph Mail  

Microsoft Graph grants the platform. This integration was integrated and tested with version 1.0 of Microsoft Graph Mail Single User Note: This integration operates against a single user mailbox — the one specified in the Email address to associate for this integration. configuration parameter. Because it uses delegated permissions, it cannot access other users' mailboxes. For multi-mailbox or cross-tenant access, use the Microsoft Graph Mail (multi-tenant) integration

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


## Microsoft Graph Search

**Type:** integration  
**Product:** Microsoft Graph Search  

Use the Microsoft Search API in Microsoft Graph to search content stored in OneDrive or SharePoint: files, folders, lists, list items, or sites

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## Microsoft Graph Security

**Type:** integration  
**Product:** Microsoft Graph Security  
**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Microsoft Graph Teams (Standard Connector)

**Type:** integration  
**Product:** Microsoft Graph Teams (Standard Connector)  

This integration is configured automatically as part of the Microsoft 365 Standard Connector. Do not configure this integration directly — set it up from the connector page instead

**Commands:**

- `None`: 
- `None`: 


## Microsoft Teams

**Type:** integration  
**Product:** Microsoft Teams  

Use the Microsoft Teams integration to send messages, notifications, and create meetings. This integration was tested with version 1.0 of Microsoft Teams. This document includes the following sections to help you understand, set up, and use the integration effectively: Data is exchanged between Microsoft Teams and the platform. A webhook (that you will configure) receives the data from Teams and passes it to the messaging endpoint. The web server on which the integration runs in the platform. You can use an engine for communication between Teams and the the platform. To mirror messages from Teams into the platform, the bot must be explicitly mentioned in the message using the '@' symbol. The web server for the integration runs within a long-running Docker container. the platform, to the host port (to which Teams posts messages). For more information, see long-running integrations documentation and Docker documentation. Note: The information in this video is for the platform. Refer to the Prerequisites section for the latest instructions

**Commands:**

- `None`: 


## Microsoft Teams Management

**Type:** integration  
**Product:** Microsoft Teams  

Manage teams and members in Microsoft Teams

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


## Microsoft Teams via Webhook

**Type:** integration  
**Product:** Microsoft Teams  

Integration for sending notifications to a Microsoft Teams channel via workflow. This integration was integrated and tested with version 6.8 of Microsoft Teams via Webhook

**Commands:**

- `None`: 


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


## MobileIronCLOUD

**Type:** integration  
**Product:** MobileIron-UEM  
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


## MobileIronCORE

**Type:** integration  
**Product:** MobileIron-UEM  

This integration was created and tested with version 11.0.0 of MobileIronCORE

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

- `None`: 
- `None`: 
- `None`: 


## MongoDB

**Type:** integration  
**Product:** MongoDB  
**Commands:**

- `None`: 


## MongoDB Atlas

**Type:** integration  
**Product:** MongoDB Atlas  

MongoDB Atlas is an integration that supports fetching and managing alerts and events within Cortex XSIAM. This integration was integrated and tested with version 2.0 of MongoDB Atlas

**Commands:**

- `None`: 


## MongoDB Key Value Store

**Type:** integration  
**Product:** MongoDB  
**Commands:**

- `None`: 


## MongoDB Log

**Type:** integration  
**Product:** MongoDB  
**Commands:**

- `None`: 


## MS-ISAC

**Type:** integration  
**Product:** MS-ISAC  

This API queries alerts and alert data from the MS-ISAC API to enrich and query alerts from the platform This integration was integrated and tested with version 1.2 (7/1/25) of the MS-ISAC API

**Commands:**

- `None`: 
- `None`: 


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

- `None`: 


## Neosec

**Type:** integration  
**Product:** Neosec  

Neosec is reinventing application security. Its pioneering SaaS platform gives security professionals visibility into behavior across their entire API estate. Built for organizations that expose APIs to partners, suppliers, and users, Neosec discovers all your APIs, analyzes their behavior, and stops threats lurking inside

**Commands:**

- `None`: 


## Netcraft

**Type:** integration  
**Product:** Netcraft  

Netcraft takedown, submission and screenshot management

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


## NetQuest OMX

**Type:** integration  
**Product:** NetQuest OMX  

NetQuest’s products are high-capacity service nodes that help security teams access and analyze network traffic. Powerful packet and flow processing features assist security tools in detecting and mitigating security threats as cost effectively as possible. This integration was integrated and tested with version 3.7.5a of NetQuest OMX

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Netscout Arbor Edge Defense

**Type:** integration  
**Product:** Netscout Arbor Edge Defense - AED  

The Netscout Arbor Edge Defense (AED) integration enables you to block and allow outbound and inbound traffic

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


## Netscout Arbor Sightline (Peakflow)

**Type:** integration  
**Product:** Netscout Arbor Sightline  

DDoS protection and network visibility. This integration was integrated and tested with version 9.3 of Netscout Arbor Sightline

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

- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## nmap

**Type:** integration  
**Product:** Nmap  

Run nmap scans with the given parameters. This integration was integrated and tested with version 7.70 of nmap. The nmap binary is shipped with the integration Docker. You can see the options available for running an nmap scan here:  Some scan options require root access for using raw packet scanning techniques. See here for detailed scanning techniques. If you've configured the server to run Docker images with a non-root internal user and you want to use raw packet scanning (for example via the -sS option for SYN/ACK scan), make sure to exclude the platform/nmap Docker image as documented For the platform. For the platform. For the platform.7 On-prem here

**Commands:**

- `None`: 


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

- `None`: 
- `None`: 


## NodeZero MCP

**Type:** integration  
**Product:** NodeZero MCP  

Use the NodeZero MCP integration to connect to the NodeZero MCP server and automatically discover its available pentesting tools. This integration uses OAuth 2.0 Dynamic Client Registration (DCR). It registers itself as a public OAuth client with the NodeZero OAuth proxy, so no pre-issued Client ID or Client Secret is required. Authentication flows through the NodeZero portal

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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


## O365 File Management (Onedrive/Sharepoint/Teams)

**Type:** integration  
**Product:** Microsoft Graph Files  

Use the O365 File Management (Onedrive/Sharepoint/Teams) integration to enable your app to get authorized access to files in OneDrive, SharePoint, and MS Teams across your entire organization. This integration requires admin consent

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


## O365 File Management (Onedrive/Sharepoint/Teams) (Standard Connector)

**Type:** integration  
**Product:** Microsoft Graph Files (Standard Connector)  

Use the O365 File Management (Onedrive/Sharepoint/Teams) integration to enable your app to get authorized access to files in OneDrive, SharePoint, and MS Teams across your entire organization. This integration requires admin consent

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


## O365 Message Trace

**Type:** integration  
**Product:** Microsoft Exchange Online  

Message Trace enables tenant administrators to track the lifecycle of an email, determine its delivery status (delivered, pending, failed, or quarantined), and understand the actions applied to it. This integration was integrated and tested with the Graph-based Message Trace API (v1.0/admin/exchange/tracing/messageTraces)

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## O365 Outlook Mail (Using Graph API)

**Type:** integration  
**Product:** Microsoft Graph Mail  

Microsoft Graph lets your app get authorized access to a user's Outlook mail data in a personal or organization account. This integration was integrated and tested with version v1 of Microsoft Graph

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


## O365 Teams (Using Graph API)

**Type:** integration  
**Product:** MicrosoftGraphTeams  

Microsoft Graph lets your app get authorized access to a user's Teams app in a personal or organization account. This is a long-running integration. For more information about long-running integrations, see the the platform, the platform

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


## OctoxLabs

**Type:** integration  
**Product:** OctoxLabs  

Octox Labs Cyber Security Asset Management platform This integration was integrated and tested with version 4.5.0 of OctoxLabs

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## OnboardingIntegration

**Type:** integration  
**Product:** OnboardingIntegration  

Creates mock email incidents using one of two randomly selected HTML templates. Textual content is randomly generated and defined to include some text (100 random words) and the following data (at least 5 of each data type): IP addresses, URLs, SHA-1 hashes, SHA-256 hashes, MD5 hashes, email addresses, domain names

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## OpenAI GPT

**Type:** integration  
**Product:** OpenAI  
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


## OpenCVE

**Type:** integration  
**Product:** OpenCVE  

Ingests CVEs from an instance of OpenCVE

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


## OPNSense

**Type:** integration  
**Product:** OPNSense  

Manage OPNsense Firewall. For more information see OPNsense documentation. OPNsense is an open source, easy-to-use and easy-to-build HardenedBSD based firewall and routing platform. This integration was integrated and tested with version 22.1 of OPNSense

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


## OpsGenie v3

**Type:** integration  
**Product:** OpsGenie  

Integration with Atlassian OpsGenie. OpsGenie is a cloud-based service that enables operations teams to manage alerts generated by monitoring tools to ensure the right people are notified, and the problems are addressed in a timely manner. This integration was integrated and tested with OpsGenie. Some changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

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


## Oracle IAM

**Type:** integration  
**Product:** Oracle IAM  

Integrate with Oracle Identity Access Management service to execute CRUD (create, read, update, and delete) operations for employee lifecycle processes

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


## Orca

**Type:** integration  
**Product:** Orca  

Agentless, Workload-Deep, Context-Aware Security and Compliance for AWS, Azure, and GCP. This integration was integrated and tested with Orca

**Commands:**

- `None`: 


## OrionMalware

**Type:** integration  
**Product:** OrionMalware  

This is the Orion Malware integration. Analyzes hash and files with static and dynamic analysis This integration was integrated and tested with version 5.3.0 of OrionMalware

**Commands:**

- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 


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

- `None`: 


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

- `None`: 


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

- `None`: 


## Perplexity AI

**Type:** integration  
**Product:** Perplexity AI  

Perplexity AI is a web search engine that uses a large language model to process queries and synthesize responses based on web search results. With a conversational approach, Perplexity AI allows users to ask follow-up questions and receive answers with citations to its sources from the internet

**Commands:**

- `None`: 


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


## PiHole

**Type:** integration  
**Product:** PiHole  

Pi-hole is a network-level advertisement and Internet tracker blocking application which acts as a DNS sinkhole and optionally a DHCP server, intended for use on a private network. This integration was integrated and tested with version FTL5.2 of PiHole

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


## PiHole v6

**Type:** integration  
**Product:** PiHole  

PiHole v6 integration using the new REST API. PiHole is a network-level advertisement and Internet tracker blocking application which acts as a DNS sinkhole and optionally a DHCP server, intended for use on a private network. This integration was integrated and tested with PiHole v6.0 API

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

- `None`: 
- `None`: 


## Pipl

**Type:** integration  
**Product:** Pipl  

Pipl provides a reputation for email addresses and identity solutions

**Commands:**

- `None`: 
- `None`: 


## Polar Security

**Type:** integration  
**Product:** Polar Security  

Polar Security, an innovator in technology that helps companies discover, continuously monitor and secure cloud and software-as-a-service (SaaS) application data – and addresses the growing shadow data problem

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## PolySwarm

**Type:** integration  
**Product:** PolySwarm  

Real-time threat intelligence from a crowd-sourced network of security experts and antivirus companies

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


## Popular News

**Type:** integration  
**Product:** Popular Cybersecurity News  

How to use this integration ? This integration was integrated and tested with version 1.0.0 of Popular News

**Commands:**

- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## QR Code Reader - goqr.me

**Type:** integration  
**Product:** QR Code Reader  

Read QR Code from image file. This integration was integrated and tested with version 1.0.0 of QR Code Reader - goqr.me

**Commands:**

- `None`: 


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

- `None`: 


## Quest KACE Systems Management Appliance (Beta)

**Type:** integration  
**Product:** Quest Kace  

This is the Quest KACE integration. This integration was integrated and tested with version v10.0.290 of QuestKace

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


## QutteraWebsiteMalwareScanner

**Type:** integration  
**Product:** Quttera Website Malware Scanner  

Quttera Website Malware Scanner This integration was integrated and tested with version v3 of QutteraWebsiteMalwareScanner

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## RaDark

**Type:** integration  
**Product:** KELA RaDark  

This integration enables you to fetch incidents and manage your RaDark monitor from the platform. This integration was integrated and tested with version 2 of RaDark

**Commands:**

- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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
**Commands:**

- `None`: 
- `None`: 


## Reco

**Type:** integration  
**Product:** Reco  

Reco is the leader in SaaS & AI Security — securing AI sprawl across SaaS apps and agents. This integration connects Reco's SaaS & AI Security platform to the platform, enabling real-time threat response, posture management, AI governance, and identity risk workflows. This integration was integrated and tested with Reco External API v1

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 


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

- `None`: 


## ReversingLabs TitaniumScale

**Type:** integration  
**Product:** ReversingLabs TitaniumScale  
**Commands:**

- `None`: 


## RiskSense

**Type:** integration  
**Product:** RiskSense  
**Commands:**

- `None`: 


## Roksit DNS Security (DNSSense)

**Type:** integration  
**Product:** Roksit DNS Security  

This integration provides adding selected domains to the Roksit Secure DNS's Blacklisted Domain List through API . This integration was integrated and tested with version 1.0.0 of Roksit DNS Security (DNSSense)

**Commands:**

- `None`: 


## RSA Archer v2

**Type:** integration  
**Product:** RSA Archer  

The RSA Archer GRC platform provides a common foundation for managing policies, controls, risks, assessments and deficiencies across lines of business

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


## RSA NetWitness Security Analytics

**Type:** integration  
**Product:** RSA NetWitness Security Analytics  

RSA Security Analytics is a distributed and modular system that enables highly flexible deployment architectures that scale with the needs of the organization. Security Analytics allows administrators to collect two types of data from the network infrastructure, packet data and log data. This integraitons should work with RSA Netwitness older than v11. For versions v11 and above use the integration RSA NetWitness v11.1

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


## SafeBreach

**Type:** integration  
**Product:** SafeBreach - Breach and Attack Simulation platform  

For enterprises using SafeBreach and platform, integrating this package streamlines operations by allowing you to operate SafeBreach through platform, making SafeBreach an integral part of the enterprise workflows. This integration includes commands for managing tests, insight indicators, simulators and deployments, users, API keys, integration issues, and more. This integration was integrated and tested with version 2024Q1.4 of Safebreach

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


## Safewalk Reports

**Type:** integration  
**Product:** Altipeak  

Safewalk server integration This integration was integrated and tested with version 3 of SafewalkReports

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


## Salesforce Fusion IAM

**Type:** integration  
**Product:** Salesforce Fusion  

Integrate with Salesforce Fusion Identity Access Management service to execute CRUD (create, read, update, and delete) operations for employee lifecycle processes. For more information, refer to the Identity Lifecycle Management article

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Salesforce IAM

**Type:** integration  
**Product:** Salesforce  

Integrate with Salesforce's services to perform Identity Lifecycle Management operations. For more information, please refer to the Identity Lifecycle Management article

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Salesforce v2

**Type:** integration  
**Product:** SalesforceV2  

CRM Services

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

- `None`: 
- `None`: 


## SAP BTP (Business Technology Platform)

**Type:** integration  
**Product:** SAP BTP (Business Technology Platform)  
**Commands:**

- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## SecurityScorecard

**Type:** integration  
**Product:** SecurityScorecard  

Provides commands to access SecurityScorecard's API. This integration was integrated and tested with the latest version of SecurityScorecard's API as of August 2024

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


## SecurityTrails

**Type:** integration  
**Product:** SecurityTrails  

This integration provides API access to the SecurityTrails platform. This integration was integrated and tested with V1 of SecurityTrails

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


## Securonix

**Type:** integration  
**Product:** Securonix  
**Commands:**

- `None`: 


## SecuronixGetViolations

**Type:** script  
**Product:** Securonix  

Gets a list of violations related to a specific threat from the context data and displays it in the layout


## Sekoia XDR

**Type:** integration  
**Product:** SekoiaXDR  

Fetch alerts and events from SEKOIA.IO XDR. To use this integration, please create an API Key with the appropriate permissions. This integration was integrated and tested with version 1.0 of Sekoia XDR

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


## Sepio

**Type:** integration  
**Product:** Sepio  
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


## Serenety

**Type:** integration  
**Product:** XMCO  

XMCO Serenety

**Commands:**

- `None`: 


## Server Message Block (SMB) v2

**Type:** integration  
**Product:** Server Message Block (SMB)  

Files and Directories management with an SMB server. Supports SMB2 and SMB3 protocols

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## ServiceNow MCP

**Type:** integration  
**Product:** ServiceNow MCP  

Use this integration to connect securely with a ServiceNow Model Context Protocol (MCP) server and access its tools in real time. This integration was integrated and tested with the latest version of ServiceNow MCP

**Commands:**

- `None`: 
- `None`: 


## ServiceNow v2

**Type:** integration  
**Product:** ServiceNow  

IT service management. Cortex interfaces with ServiceNow to help streamline security-related service management and IT operations. For example, you can use the ServiceNow integration in order to: Please refer to ServiceNow documentation for additional information. We especially recommend the Operators available for filters and queries page. This integration was integrated and tested with the Xanadu version of ServiceNow

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

- `None`: 
- `None`: 
- `None`: 


## Shodan v2

**Type:** integration  
**Product:** Shodan  

Shodan is a search engine for Internet-connected devices. Unlike traditional search engines that index websites, Shodan indexes information about the devices connected to the internet, such as servers, routers, webcams, and other IoT devices

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 


## Signum

**Type:** integration  
**Product:** Signum  

Signum password expiry notification

**Commands:**

- `None`: 


## SilentPush

**Type:** integration  
**Product:** Silent Push  

The Silent Push Platform uses first-party data and a proprietary scanning engine to enrich global DNS data with risk and reputation scoring, giving security teams the ability to join the dots across the entire IPv4 and IPv6 range, and identify adversary infrastructure before an attack is launched. The content pack integrates with the Silent Push system to gain insights into domain/IP information, reputations, enrichment, and infratag-related details. It also provides functionality to live-scan URLs and take screenshots of them. Additionally, it allows fetching future attack feeds from the Silent Push system. This integration was integrated and tested with v1 of SilentPush API

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


## SilentPush

**Type:** integration  
**Product:** Silent Push  

The Silent Push Platform uses first-party data and a proprietary scanning engine to enrich global DNS data with risk and reputation scoring, giving security teams the ability to join the dots across the entire IPv4 and IPv6 range, and identify adversary infrastructure before an attack is launched. The content pack integrates with the Silent Push system to gain insights into domain/IP information, reputations, enrichment, and infratag-related details. It also provides functionality to live-scan URLs and take screenshots of them. Additionally, it allows fetching future attack feeds from the Silent Push system. This integration was integrated and tested with version 4.2 of SilentPush

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


## Silverfort

**Type:** integration  
**Product:** Silverfort  

Silverfort protects organizations from data breaches by delivering strong authentication across entire corporate networks and cloud environments, without requiring any modifications to endpoints or servers. Using patent-pending technology, Silverfort's agentless approach enables multi-factor authentication and AI-driven adaptive authentication even for systems that don’t support it today, including proprietary systems, critical infrastructure, shared folders, IoT devices, and more. Use Silverfort integration to get & update Silverfort risk severity. This integration was integrated and tested with Silverfort version 5.2

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Skyhigh Secure Web Gateway (On Prem)

**Type:** integration  
**Product:** McAfee Web Gateway  

Manages the block and allow lists within Skyhigh Secure Web Gateway. This integration was integrated and tested with version 11.2.9 of Skyhigh Secure Web Gateway (On Prem)

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


## Skyhigh Security

**Type:** integration  
**Product:** Skyhigh Security SSE  

Skyhigh Security is a cloud-based, multi-tenant service that enables Cloud Discovery and Risk Monitoring, Cloud Usage Analytics, Cloud Access and Control. This integration was integrated and tested with version 1 of Skyhigh Security. Do to API limitations, keep in mind that over time the integration can start to work more slowly. The solution is to restart the last-run

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Slack IAM

**Type:** integration  
**Product:** Slack  

Note: This integration should be used as part of our Identity Lifecycle Management premium pack. For further details, visit our IAM pack documentation. Integrate with Slack's services to execute CRUD operations for employee lifecycle processes. For more information, please refer to the Identity Lifecycle Management article

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


## Slack v3

**Type:** integration  
**Product:** Slack  

Send messages and notifications to your Slack team. This integration was integrated and tested with Slack

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


## SMIME Messaging

**Type:** integration  
**Product:** SMIME Messaging  

Use the S/MIME (Secure Multipurpose Internet Mail Extensions) integration to send and receive secure MIME data. This integration was integrated and tested with version 0.40.1 of M2Crypto

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Smokescreen IllusionBLACK

**Type:** integration  
**Product:** Smokescreen IllusionBLACK  

Smokescreen IllusionBLACK is a deception-based threat defense platform designed to accurately and efficiently detect targeted threats including reconnaissance, lateral movement, malware-less attacks, social engineering, Man-in-the-Middle attacks, and ransomware in real-time. This integration was integrated and tested with version v3.10.7.4 of Smokescreen IllusionBLACK

**Commands:**

- `None`: 


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

- `None`: 
- `None`: 


## SOCFWPackManager

**Type:** script  
**Product:** SOC Framework  

The SOC Framework bootloader for Cortex XSIAM. Lists the SOC Framework pack catalog with the installed version and update status of each pack, installs and configures packs from platform_config.json, re-runs configuration only, and diagnoses the platform endpoints the install path depends on. Also includes sync-tags, a backward-compatible action for older SOC Framework deployments still using the value_tags lookup; modern versions use the SOCActionTimeMap_V3 list and do not require it

**Commands:**

- `None`: 
- `None`: 

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

- `None`: 
- `None`: 


## SOCRadar Incidents Multi-Tenant

**Type:** integration  
**Product:** SOCRadar  

Fetch and manage security incidents from multiple companies using SOCRadar's Multi-Tenant Incident API. Designed for MSPs, MSSPs, and organizations managing multiple subsidiaries

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## SOCRadar Incidents v4

**Type:** integration  
**Product:** SOCRadar  

Fetch and manage security incidents from SOCRadar's Incident API v4 with advanced filtering, multi-status selection, and comprehensive incident enrichment

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## SOCRadar IoC Enrichment

**Type:** integration  
**Product:** SOCRadar  
**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## SOCRadar Rapid Reputation

**Type:** integration  
**Product:** SOCRadar  

Enrich indicators (IP, Domain, URL, Hash) by obtaining reputation information via SOCRadar's Rapid Reputation API. This integration was integrated and tested with the latest version of SOCRadar Rapid Reputation API

**Commands:**

- `None`: 
- `None`: 


## SOCRadar Takedown

**Type:** integration  
**Product:** SOCRadarTakedown  

Submit and monitor takedown requests for phishing domains, impersonating accounts, and other digital risks

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## SOCRadar ThreatFusion

**Type:** integration  
**Product:** SOCRadar  

Enrich indicators by obtaining enhanced information and reputation via ThreatFusion of SOCRadar. This integration was integrated and tested with v21.11 of SOCRadar

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


## SolarWinds

**Type:** integration  
**Product:** SolarWinds  

The SolarWinds integration interacts with the SWIS API to allow users to fetch alerts and events. It also provides commands to retrieve lists of alerts and events. This integration was integrated and tested with version 3.0.0 of SolarWinds Information Service (SWIS API)

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Sophos Central

**Type:** integration  
**Product:** Sophos Central  

The unified console for managing Sophos products

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


## Spamcop

**Type:** integration  
**Product:** Spamcop  

SpamCop is an email spam reporting service. The integration allows checking the reputation of an IP address. This integration was integrated and tested with Spamcop

**Commands:**

- `None`: 
- `None`: 


## SpecterOps BloodHound Enterprise

**Type:** integration  
**Product:** SpecterOps BloodHound Enterprise  

This integration enables automated retrieval of attack path findings from BloodHound into the platform, streamlining incident creation and investigation. This integration was integrated and tested with version 1.0.0 of SpecterOps BloodHound Enterprise

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## SpecterOpsBloodHoundEnterprise

**Type:** playbook  
**Product:** SpecterOps BloodHound Enterprise  

Automated playbook that enriches BloodHound Enterprise attack path incidents with object information and validates attack path existence between security principals

**Commands:**

- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Stamus

**Type:** integration  
**Product:** Stamus  

[Get Declaration of Compromises from Stamus Security Platform and build Incidents. Then get related artifacts, events and Host Insight information] This integration was integrated and tested with version 39.0.1 of Stamus Security Platform

**Commands:**

- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 


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


## Symantec Endpoint Security (ICDM)

**Type:** integration  
**Product:** SymantecICDM  

Query the Symantec Endpoint Security Cloud Portal (ICDM). This integration was integrated and tested with version 1 of SymantecICDM

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Synapse

**Type:** integration  
**Product:** Synapse  

Synapse intelligence analysis platform. This integration was integrated and tested with version 2.7.0 of Synapse

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


## Synchronize Incident Closure - Cyberhaven

**Type:** playbook  
**Product:** Cyberhaven  

Closes platform incidents by synchronizing their status with the corresponding Cyberhaven incident


## SysAid

**Type:** integration  
**Product:** SysAid  

SysAid is a robust IT management system designed to meet all of the needs of an IT department. This integration was integrated and tested with version 21.4.44 of SysAid

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


## Syslog Sender

**Type:** integration  
**Product:** Syslog  
**Commands:**

- `None`: 


## TaegisXDR v2

**Type:** integration  
**Product:** Secureworks  
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

- `None`: 


## TAXII2 Server

**Type:** integration  
**Product:** TAXII Server  
**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## TAXII2ApiModule

**Type:** script  

To use the common TAXII 2 Server logic (authentication and API requests), run the following command to import the TAXII2ApiModule. Then, the TAXII2ApiModule will be available for usage. For examples, see the TAXII 2 Feed integration


## Team Cymru

**Type:** integration  
**Product:** Team Cymru  

Team Cymru provides various service options dedicated to mapping IP numbers to BGP prefixes and ASNs. Each of the services is based on the same BGP feeds from 50+ BGP peers and is updated at 4-hour intervals. This integration was integrated and tested with version 1.0 of TeamCymru

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## Team Cymru Scout

**Type:** integration  
**Product:** Team Cymru  
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


## Tenzai

**Type:** integration  
**Product:** Tenzai  

Validate Cortex ASM-discovered exposures with Tenzai's agentic penetration testing. Create a scan for an exposure, poll it to completion, and fetch the verdict and evidence back into the Cortex issue

**Commands:**

- `None`: 
- `None`: 
- `None`: 


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

- `None`: 


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


## Thales SafeNet Trusted Access

**Type:** integration  
**Product:** Thales SafeNet Trusted Access  

This integration enables you to process alerts from SafeNet Trusted Access (STA) indicating security risks to end user accounts, and apply security remediation actions on SafeNet Trusted Access through security orchestration playbooks. For information about the configuration steps, visit our Help Documentation

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


## TheHive Project

**Type:** integration  
**Product:** TheHive Project  

Integration with The Hive Project Security Incident Response Platform. This integration was integrated and tested with version 4.1.4 of TheHive Project

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


## ThousandEyes

**Type:** integration  
**Product:** ThousandEyes  

This Integration is used to fetch-incidents via “Active alerts”, get alert details via “Alert details”, and get the “Agent list”. It was integrated and tested with API v6 of ThousandEyes

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 


## Trello

**Type:** integration  
**Product:** Trello  

Interact with the Trello task manager This integration was integrated and tested with version 1.0.0 of Trello

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## TrendAI Vision One™

**Type:** integration  
**Product:** TrendAI Vision One™  

Support and maintenance for this integration are provided by the author. Please use the following contact details: TrendAI Vision One™ is a purpose-built threat defense platform that provides added value and new benefits beyond XDR solutions, allowing you to see more and respond faster. Providing deep and broad extended detection and response (XDR) capabilities that collect and automatically correlate data across multiple security layers—email, endpoints, servers, cloud workloads, and networks—TrendAI Vision One™ prevents the majority of attacks with automated protection

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


## TrendAI Vision One™ v3

**Type:** integration  
**Product:** TrendAI Vision One™  

TrendAI Vision One™ is a purpose-built threat defense platform that provides added value and new benefits beyond XDR solutions, allowing you to see more and respond faster. Providing deep and broad extended detection and response (XDR) capabilities that collect and automatically correlate data across multiple security layers—email, endpoints, servers, cloud workloads, and networks—TrendAI Vision One™ prevents the majority of attacks with automated protection. V3 version of the app includes everything that the previous app had and adds more capabilities. It leverages V3 of TrendAI™ APIs and introduces further ability to manage domain accounts with addition of 4 domain account actions for enabling/disabling user account, forcing sign-out and password resets for compromised accounts. This app is in active development. We previously added 4 actions, one to fetch email activity data with count, one to fetch endpoint activity data with count and an action to restore a quarantined email message. In this release we have added 6 new custom script actions allowing the user to fetch a list of available custom scripts in XDR portal, ability to run a custom script on a specified endpoint, capacity to add, download, update and delete a custom script from XDR portal. This integration was integrated and tested with version 3 API of TrendAI Vision One™

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


## TrendAI™ Apex One

**Type:** integration  
**Product:** TrendAI™ Apex One  

TrendAI™ Apex One central automation to manage agents and User-Defined Suspicious Objects This integration was integrated and tested with version 2019 hotfix 5449 of TrendAI™ Apex One Central

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


## TrendAI™ Deep Security™

**Type:** integration  
**Product:** TrendAI™ Deep Security™  

TrendAI™ Deep Security™ This integration was integrated and tested with version 20.0 of TrendAI™ Deep Security™, and v1 of the API

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


## Tripwire

**Type:** integration  
**Product:** Tripwire  

Tripwire is a file integrity management (FIM), FIM monitors files and folders on systems and is triggered when they have changed. This integration was integrated and tested with v1 of Tripwire

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## TrustwaveFusion

**Type:** integration  
**Product:** Trustwave Fusion  

The Trustwave Fusion platform connects your organization’s digital footprint to a robust security cloud comprised of the Trustwave data lake, advanced analytics, actionable threat intelligence and a wide range of Trustwave services including Trustwave SpiderLabs , elite team of security specialists. Your team will benefit from deep visibility and the advanced security expertise necessary for protecting assets and eradicating threats as they arise. This integration was integrated and tested with version 1.0.68 of TrustwaveFusion

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


## Tufin

**Type:** integration  
**Product:** Tufin  
**Commands:**

- `None`: 


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


## Twitter v2

**Type:** integration  
**Product:** Twitter  

Twitter integration provides access to searching recent Tweets (in last 7 days) and user information using the Twitter v2 API. This integration was integrated and tested with version v2 of Twitter API. Some changes have been made that might affect your existing content. If you are upgrading from a previous of this integration, see Breaking Changes

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## TypeSafe Jev

**Type:** integration  
**Product:** TypeSafe Jev  

Use TypeSafe Jev typed judgments and calibrated probabilities in Cortex XSIAM and platform playbooks

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## UltraMSG

**Type:** integration  
**Product:** UltraMSG  

This is the UltraMSG integration for getting started made by Trustnet

**Commands:**

- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 


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

- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Varonis SaaS

**Type:** integration  
**Product:** Varonis SaaS  

Streamline alerts and related forensic information from Varonis SaaS

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


## varonis-alert-post-processing

**Type:** script  
**Product:** Varonis SaaS  

Varonis alert post processing script to set the alert status in platform to closed when an incident is closed


## Vectra Detect

**Type:** integration  
**Product:** Vectra AI  

This integration allows to create incidents based on Vectra Accounts/Hosts/Detections objects. This integration was integrated and tested with version 7.1 of Vectra Detect

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


## Vectra RUX - Network Detection & Response

**Type:** integration  
**Product:** Vectra RUX  

This integration allows the security operations center to create and manage incidents based on Vectra Events Detections. This integration was integrated and tested with Vectra API v3.5

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


## Vectra XDR

**Type:** integration  
**Product:** Vectra XDR  
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


## Vercara UltraDNS

**Type:** integration  
**Product:** Vercara UltraDNS  

This integration fetches DNS configuration audit logs from Vercara UltraDNS platform. This integration was integrated and tested with the 3.18.0 Vercara UltraDNS API

**Commands:**

- `None`: 


## VerdictResult

**Type:** script  
**Product:** Common Scripts  

This widget displays the incident verdict or the alert verdict based on the 'incident.verdict' or 'alert.verdict' field


## Versa Director

**Type:** integration  
**Product:** VersaDirector  

Versa Director is a virtualization and service creation platform that simplifies the design, automation, and delivery of SASE services. Versa Director provides the essential management, monitoring and orchestration capabilities needed to deliver all of the networking and security capabilities within Versa SASE. This integration was integrated and tested with version 1.0.0 of VersaDirector

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


## Viper

**Type:** integration  
**Product:** Viper  

Viper is a binary analysis and management framework

**Commands:**

- `None`: 
- `None`: 


## VMRay

**Type:** integration  
**Product:** VMRay Analyzer  

This integration enables users to design playbooks that involve analyzing a file in VMRay and retrieving the analysis results and associated threat intelligence. The Playbooks accelerate incident response and make security operations more scalable and efficient

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


## VMware

**Type:** integration  
**Product:** VMware  

VMware vCenter server is a centralized management application that lets you manage virtual machines and ESXi hosts centrally. This integration was integrated and tested with version 7.03 of VMware

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


## VMware Workspace ONE UEM (AirWatch MDM)

**Type:** integration  
**Product:** VMware Workspace ONE UEM  

VMware Workspace ONE UEM integration allows users to search enrolled corporate or employee-owned devices, provides detailed information about each device such as its serial number, installed OS's, pending OS updates, network details, and much more leveraging Workspace ONE UEM's (formerly AirWatch MDM) API. This integration was integrated and tested with version 21.5.0.4 of VMware Workspace ONE UEM (AirWatch MDM)

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## WALLIX Bastion

**Type:** integration  
**Product:** WALLIX Bastion  

Centralized Control and Monitoring of Privileged Access to Sensitive Assets. This integration was integrated and tested with version 12 of WALLIX Bastion

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


## Web File Repository

**Type:** integration  
**Product:** Web File Repository  

Simple web server with a file uploading console to store small files. Helps make your environment ready for testing purpose for your playbooks or automations to download files from a web server. NOTE: For more information about long-running integrations, see the the platform, the platform

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

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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


## WizDefend

**Type:** integration  
**Product:** Wiz  

Agentless cloud security platform for detecting and addressing cloud issues, detections, and threats

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


## Wolken ITSM

**Type:** integration  
**Product:** Wolken ITSM  

Use The Wolken IT Service Management (ITSM) solution to modernize the way you manage and deliver services to your users. This integration was integrated and tested with version 1.0.0 of Wolken ITSM

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Wordpress

**Type:** integration  
**Product:** Wordpress  

The WordPress REST API provides an interface for applications to interact with your WordPress site by sending and receiving data as JSON (JavaScript Object Notation) objects. It is the foundation of the WordPress Block Editor, and can likewise enable your theme, plugin or custom application to present new, powerful interfaces for managing and publishing your site content. This integration was integrated and tested with version 5.6 of Wordpress

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


## Workday

**Type:** integration  
**Product:** Workday  

Workday offers enterprise-level software solutions for financial management, human resources, and planning. This integration was integrated and tested with version 47.0 of Workday

**Commands:**

- `None`: 
- `None`: 


## Workday IAM

**Type:** integration  
**Product:** Workday  

Use the Workday IAM Integration as part of the IAM premium pack. For more information, please refer to the Identity Lifecycle Management article

**Commands:**

- `None`: 
- `None`: 


## Workday IAM Event Generator (Beta)

**Type:** integration  
**Product:** Workday  

Generates mock reports and events for Workday IAM. Use these for testing and development

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## XM Cyber

**Type:** integration  
**Product:** XM Cyber  

The XM Cyber integration creates unique incidents with valuable data collected daily, and enriches your existing incidents with attack simulation context. This enables you to prioritize your responses based on XM Cyber’s insights. This integration was integrated and tested with version 1.43.0.355 of XMCyber

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


## XM Cyber CEM

**Type:** integration  
**Product:** XM Cyber  

The XM Cyber integration connects XM Cyber's Continuous Exposure Management (CEM) platform with platform, enhancing your Security Information and Event Management (SIEM) and Security Orchestration, Automation, and Response processes with attack graph context and prioritization, while also feeding relevant entities back to CEM to be defined as breach points in CEM scenarios

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## xMatters

**Type:** integration  
**Product:** xMatters  

This is an integration for using xMatters. This integration was integrated and tested with version 1 of xMatters

**Commands:**

- `None`: 
- `None`: 
- `None`: 


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

- `None`: 


## Zafran API

**Type:** integration  
**Product:** Zafran  

In today’s complex security landscape, resource-constrained teams struggle to efficiently mitigate exposure risks across large infrastructures. The Zafran Integration with Palo platform helps you implement Automated, High Impact Mitigations at scale. With this integration, teams can prioritize mitigation actions, trigger playbooks with a single click, and streamline their response efforts, all from within the Palo platform environment

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## ZeroFox

**Type:** integration  
**Product:** ZeroFox  

Cloud-based SaaS to detect risks found on social media and digital channels. This integration was integrated and tested with versions 1.0 and 2.0 of ZeroFox

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


## ZeroFox Key Incidents

**Type:** integration  
**Product:** ZeroFox  

Cloud-based SaaS to detect risks found on social media and digital channels. This integration was integrated and tested with version 1.4.0 of ZeroFoxKey

**Commands:**

- `None`: 


## Zerohack XDR

**Type:** integration  
**Product:** Zerohack XDR  

The companion integration for Zerohack XDR. Current versions allow the user to collect data from the XDR and later versions will support data exfiltration to XDR. This integration was integrated and tested with version 1.0 of Zerohack XDR

**Commands:**

- `None`: 


## ZeroTrustAnalyticsPlatform

**Type:** integration  
**Product:** Zero Trust Analytics Platform  

Zero Trust Analytics Platform (ZTAP) is the underlying investigation platform and user interface for Critical Start's MDR service. This integration was integrated and tested with version 2021-06-25 of ZeroTrustAnalyticsPlatform

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## Zimperium

**Type:** integration  
**Product:** Zimperium  

Zimperium is a mobile security platform that generates alerts based on anomalous or unauthorized activities detected on a user's mobile device. This integration was integrated and tested with version 4.24 of Zimperium

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


## Zimperium v2

**Type:** integration  
**Product:** Zimperium  

Fetch and investigate mobile security alerts, generated based on anomalous or unauthorized activities detected on a user's mobile device. This integration was integrated and tested with version v.5.24.0 of Zimperium v2. Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

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


## Zoom Mail

**Type:** integration  
**Product:** Zoom Mail  

Enables interaction with the Zoom Mail API

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Zoom_IAM

**Type:** integration  
**Product:** Zoom  

An Identity and Access Management integration template. This integration was integrated and tested with version 2.0.0 of Zoom_IAM

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


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

