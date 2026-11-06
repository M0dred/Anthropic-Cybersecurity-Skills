# Integration and Automation Catalog - Ot Ics Security

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## Add Unknown Indicators To Inventory - RiskIQ Digital Footprint

**Type:** playbook  
**Product:** RiskIQ Digital Footprint  

Adds the unknown indicators or updates/removes the indicators identified as a known asset in the RiskIQ Digital Footprint inventory according to the user inputs for each asset. To select the indicators you want to add, go to playbook inputs, choose "from indicators" and set your query. For example reputation:None etc. The purpose of the playbook is to check if the indicators with the unknown reputation are known assets. The default playbook query is "reputation:None". In case indicators with different reputations are to be added to the inventory, the query must be edited accordingly. This playbook cannot be run in quiet mode. This playbook needs to be used with caution as it might use up the integration’s API license when running for large amounts of indicators. Supported integration

**Inputs:**

- `Indicator Query`: Indicators matching the indicator query will be used as playbook input
- `support_contact`: The contact email address of the support team from which manual inputs should be fetched.


## AlienVault OTX v2

**Type:** integration  
**Product:** AlienVault OTX  

Query Indicators of Compromise in AlienVault OTX

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Auto Add Assets - RiskIQ Digital Footprint

**Type:** playbook  
**Product:** RiskIQ Digital Footprint  

This playbook automatically adds the provided asset(s) to the RiskIQ Digital Footprint inventory according to the values provided. Use this playbook as a sub playbook and loop over each asset in the asset list in order to add multiple assets. Supported integration

**Inputs:**

- `assets_to_add`: The list of asset(s) to be added. The list should have some specific keys used in this playbook and this playbook should be used as a sub pl
- `server_url`: The platform server URL to attach with the added asset.


## Auto Update Or Remove Assets - RiskIQ Digital Footprint

**Type:** playbook  
**Product:** RiskIQ Digital Footprint  

This playbook automatically updates or removes the provided asset(s) from the RiskIQ Digital Footprint inventory according to the values provided. Use this playbook as a sub playbook and loop over each asset in the asset list in order to update or remove multiple assets. Supported integration

**Inputs:**

- `assets_to_update`: The list of the assets to be updated or removed. The list should have some specific keys used in this playbook. Example of the list: [{"Asse


## CertificatesTroubleshoot

**Type:** script  
**Product:** Troubleshoot  

This automation exports all custom certificate-related information from the Python Docker container and decode it using RFC. In addition, it will get the certificate located in the specified endpoint

**Inputs:**

- `endpoint`: The endpoint identifier IP address or URL:Port. If the port is not included, 443 will be used by default.
- `port`: The endpoint port. Default is 443.
- `mode`: Operation mode. Determines how the endpoint is inspected. Either using python built-in SSL or openssl client.


## Check Indicators For Unknown Assets - RiskIQ Digital Footprint

**Type:** playbook  
**Product:** RiskIQ Digital Footprint  

This playbook receives indicators from its parent playbook and checks if the indicator is an unknown or a known asset in the RiskIQ Digital Footprint inventory and gives out a list of the unknown as well as known assets. This playbook cannot be run in quiet mode. This playbook needs to be used with caution as it might use up the integration’s API license when running for large amounts of indicators. Supported integration

**Inputs:**

- `asset_name`: Name of the asset.
- `asset_type`: Type of the asset. Possible values: Domain, Host, IP Address, IP Block, ASN, Page, SSL Cert, Contact.


## Check IP Address For Whitelisting - RiskIQ Digital Footprint

**Type:** playbook  
**Product:** RiskIQ Digital Footprint  

Checks if the provided IP Address should be added to allow list and excluded or not. Use this playbook as a sub-playbook to loop over multiple IP Addresses to check if they should be added to allow list and excluded

**Inputs:**

- `IP`: IP Address for checking if it should be add to allow list. Use this playbook as a sub-playbook to loop over multiple IP Addresses to check i
- `InternalRange`: A list of IP ranges to check the IP in. The list should be provided in CIDR notation, separated by commas. An example of a list of ranges wo


## Claroty

**Type:** integration  
**Product:** Claroty  

Use the Claroty CTD integration to manage assets and alerts. This integration was integrated and tested with version 4.0.1 of Claroty

**Commands:**

- `None`: 


## Claroty Incident

**Type:** playbook  
**Product:** Claroty  

## Claroty Manage Asset CVEs

**Type:** playbook  
**Product:** Claroty  

## CollectPacksData

**Type:** script  
**Product:** platform Content Update Notifications  

## Content Update Manager

**Type:** playbook  
**Product:** platform Content Update Notifications  

This playbook is part of the Content Management pack

**Inputs:**

- `notificationemail`: Provides semi-colon delimited e-mail addresses for the new content notifications. Note: You must have an installed and configured integratio
- `slackuser`: Provides a Slack username for the new content notifications. Note: You must have an installed and configured Slack integration.
- `slackchannel`: Provides a Slack channel for the new content notifications. Note: You must have an installed and configured Slack integration. Also, make su
- `packs`: A CSV of packs to monitor.
- `auto_update`: Establishes whether to automatically update the content packs if there are available updates or wait for an analyst's approval or the manual


## Cortex XDR - CVE-2025-59287 - Microsoft WSUS Remote Code Execution

**Type:** playbook  
**Product:** CVE-2025-59287 - Microsoft WSUS Remote Code Execution  

CVE-2025-59287 - Microsoft WSUS Remote Code Execution


## CVE-2022-41040 & CVE-2022-41082 - ProxyNotShell

**Type:** playbook  
**Product:** CVE-2022-41040 & CVE-2022-41082 - ProxyNotShell  

UPDATE A new method for bypassing ProxyNotShell mitigations was found after being seen exploited in the wild by the Play ransomware gang. While the original exploit took advantage of the Autodiscover endpoint, the new exploit is using the OWA endpoint leading to SSRF. The OWASSRF exploit method involves two different vulnerabilities tracked by CVE-2022-41080 and CVE-2022-41082 that allow remote code execution (RCE) via Outlook Web Access (OWA). This playbook introduces several updates in response to the new discovery: Microsoft is investigating two reported zero-day vulnerabilities affecting Microsoft Exchange Server 2013, Exchange Server 2016, and Exchange Server 2019. The first one, identified as CVE-2022-41040, is a Server-Side Request Forgery (SSRF) vulnerability, and the second one, identified as CVE-2022-41082, allows Remote Code Execution (RCE) when PowerShell is accessible to the attacker. Currently, Microsoft is aware of limited targeted attacks using these two vulnerabilities. In these attacks, CVE-2022-41040 can enable an authenticated attacker to remotely trigger CVE-2022-41082. It should be noted that authenticated access to the vulnerable Exchange Server is necessary to successfully exploit either vulnerability. This playbook includes the following tasks: More information: Threat Brief: OWASSRF Vulnerability Exploitation Threat Brief: CVE-2022-41040 and CVE-2022-41082: Microsoft Exchange Server (ProxyNotShell) References: OWASSRF: CrowdStrike Identifies New Expl

**Inputs:**

- `CVEs`: The vulnerabilities CVE indicators.
- `SplunkIndex`: Splunk's index name in which to search. The default is "*" - All.
- `SplunkEarliestTime`: Splunk's earliest time to search.
- `SplunkLatestTime`: Splunk's latest time to search.
- `ElasticIndex`: Elastic's index name in which to search. The default is "winlogbeat-*" - All.
- `QRadarTimeRange`: QRadar's query time range.
- `RunXQLHuntingQueries`: Whether to execute the XQL queries.
- `XQLHuntingQueriesType`: Whether to execute the ProxyNotShell or OWASSRF XQL queries or both.* Use 'ProxyNotShell' as an input to execute ProxyNotShell queries* Use 


## CyberTotal

**Type:** integration  
**Product:** CyberTotal  

CyberTotal is a cloud-based threat intelligence service developed by CyCraft. This integration was integrated and tested with version 1.6.4 of CyberTotal

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## CyberTotal Whois - CyCraft

**Type:** playbook  
**Product:** CyberTotal  

This playbook is used to automatically retrieve Whois information regarding IPs, URLs and domains. Playbook input: IPs, URLs, domains. Playbook output: Whois lookup information

**Inputs:**

- `Domain`: The input domain will be searched automatically on CyberTotal to retrieve whois information.
- `IP`: The input ip will be searched automatically on CyberTotal to retrieve whois information.
- `URL`: The input url will be searched automatically on CyberTotal to retrieve whois information.


## Detonate File - VirusTotal (API v3)

**Type:** playbook  
**Product:** VirusTotal  

Detonate a file through VirusTotal (API v3)

**Inputs:**

- `File`: Entry ID of the file to detonate


## Detonate URL - VirusTotal (API v3)

**Type:** playbook  
**Product:** VirusTotal  

Detonate URL through VirusTotal (API v3) integration

**Inputs:**

- `URL`: Entry ID of the file to detonate


## Enrich Incident With Asset Details - RiskIQ Digital Footprint

**Type:** playbook  
**Product:** RiskIQ Digital Footprint  

Enriches the incident with asset details and the asset with the incident URL on the RiskIQ Digital Footprint platform. This playbook also sends an email containing the owner's information to the primary or secondary contact of the asset and provides the user with an opportunity to update or remove the asset. Supported integration

**Inputs:**

- `asset_type`: Type of the asset. Possible values: Domain, Host, IP Address, IP Block, ASN, Page, SSL Cert, Contact. This input supports a single value onl
- `asset_name`: Name of the asset.
- `skip_manual_tasks`: Skip the manual tasks and do not prompt for user input. Possible values: "Yes" and "No". The default value is "No".
- `support_email_address`: The contact email address of the support team from which manual inputs should be fetched.


## File Enrichment - Virus Total (API v3)

**Type:** playbook  
**Product:** VirusTotal  

Get file information using the Virus Total API integration

**Inputs:**

- `FileHash`: File Hash to enrich


## HYAS Protect

**Type:** integration  
**Product:** HYAS Protect  

HYAS Protect is a generational leap forward utilizing authoritative knowledge of attacker infrastructure including unrivaled domain-based intelligence to proactively protect enterprises from cyberattacks. HYAS Protect is deployed as a cloud-based DNS security solution or through API integration with existing solutions. HYAS Protect combines infrastructure expertise and multi-variant communication pattern analysis to deliver reputational verdicts for any domain and infrastructure, allowing enterprises to preempt attacks while proactively assessing risk in real-time. HYAS Protect can enforce security, block command and control (C2) communication used by malware, ransomware, and botnets, block phishing attacks, and deliver a high-fidelity threat signal that enhances an enterprise’s existing security and IT governance stack. Use the HYAS Protect integration to get the verdict information for FQDN, IP Address and NameServer. This integration was integrated and tested with version 1.0.0 of HYAS Protect

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Integration Troubleshooting

**Type:** playbook  
**Product:** Troubleshoot  

Troubleshoot a problem with either an integration's configuration or with running a command

**Inputs:**

- `instancename`: The name of the instance to check.
- `troubleshoottype`: The troubleshoot type.
- `commandline`: The full command to run, for example, "!vt-comments-get resource=www.example.com"
- `insecure`: Whether to run with changing the insecure flag.


## IP Whitelist And Exclusion - RiskIQ Digital Footprint

**Type:** playbook  
**Product:** RiskIQ Digital Footprint  

Adds the IP Address(es) to allow list after checking if it should be added to allow list according to the user inputs provided. This playbook also adds these IP Address indicators to the exclusion list and tags it with the "RiskIQ Whitelisted IP Address" tag

**Inputs:**

- `ip_address`: The list of IP Address(es) to be added to allow list and excluded.
- `InternalRange`: A list of IP ranges to check if the IP Address is in that range to add to allow list. The list should be provided in CIDR notation, separate
- `auto_whitelist_ip_address`: Automatically add to allow list the IP Address(es). You can set this as 'Yes' or 'No' manually here or you can set it into a custom incident
- `auto_exclude_whitelisted_ip_address`: Automatically add the IP Address(es) on allow list to the exclusion list. You can set this as 'Yes' or 'No' manually here or you can set it 
- `support_contact`: The contact email address of the support team from which manual inputs should be fetched.
- `aws_security_group_name`: Name of the AWS Security Group to update the allow listed IPs.
- `gcp_firewall_name`: Name of the GCP Firewall where the playbook should set the allow listed IPs.
- `okta_zone_id`: ID of the Okta Zone to update the allow listed IPs. Use !okta-list-zones to obtain the available zones.


## LINENotify

**Type:** integration  
**Product:** LINENotify  

The LINE API Integration is used for sending a message to LINE Group. This integration was integrated and tested with LINE version 7.0.3 of LINENotify

**Commands:**

- `None`: 


## OTRS

**Type:** integration  
**Product:** OTRS Service Management platform  

Service management suite that comprises ticketing, workflow automation, and notification. This integration was integrated and tested with OTRS versions 5, 6, and 7

**Commands:**

- `None`: 


## PassiveTotal v2

**Type:** integration  
**Product:** PassiveTotal  

Analyze and understand threat infrastructure from a variety of sources-passive DNS, active DNS, WHOIS, SSL certificates and more-without devoting resources to time-intensive manual threat research and analysis. This integration was integrated and tested with enterprise version of PassiveTotal v2

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## PowerShell Remoting (Beta)

**Type:** integration  
**Product:** Powershell Remoting  

PowerShell Remoting is a comprehensive built-in remoting subsystem that is a part of Microsoft's native Windows management framework (WMF) and Windows remote management (WinRM). This feature allows you to handle most remoting tasks in any configuration you might encounter by creating a remote PowerShell session to Windows hosts and executing commands in the created session. The integration includes out-of-the-box commands which supports agentless forensics for remote hosts. For more information about setting up PowerShell Remoting, see the PowerShell Remoting - Configuration guide

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## PTEnrich

**Type:** script  
**Product:** PassiveTotal  

Enriches the given IP address or domain with metadata, malware, or osint

**Inputs:**

- `query`: The IP address or domain to enrich.


## RemoteAccess v2

**Type:** integration  
**Product:** Remote Access  

This integration transfers files between the platform. Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes. Note: This integration was integrated and tested on a remote machine with Centos-7 operating system. It does not work with Windows operation system

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Reset User Password via Chatbot

**Type:** playbook  
**Product:** Password Reset via Chatbot  

This playbook resets the password of an Active Directory or Okta user. The process is as follows: This playbook is intended for use with Slack or Teams. In order to use it, please make sure that you have a classifier and mapper in place. The classifier should create a Password Reset via Chatbot incident, while the mapper should map the email of the user to the Reporter Email Address field. This playbook assumes that the user requesting the password reset has the same email in Slack / Teams, and in Active Directory / Okta

**Inputs:**

- `PasswordMaxDigits`: The maximum number of digits in the generated password. If no value is specified, a value of 10 will be used.
- `PasswordMaxLowercase`: Maximum number of lower case characters to include in the password. If no value is specified, a value of 10 will be used.
- `PasswordMaxSymbols`: Maximum number of symbols to include in the password. If no value is specified, a value of 10 will be used.
- `PasswordMaxUppercase`: Maximum number of upper case characters to include in the password. If no value is specified, a value of 10 will be used.
- `PasswordMinDigits`: Minimum number of digits to include in the password. If no value is specified, a value of 0 will be used.
- `PasswordMinLowercase`: Minimum number of lower case characters to include in the password. If no value is specified, a value of 0 will be used.
- `PasswordMinSymbols`: Minimum number of symbols to include in the password. If no value is specified, a value of 0 will be used.
- `PasswordMinUppercase`: Minimum number of upper case characters to include in the password. If no value is specified, a value of 0 will be used.


## RiskIQ Digital Footprint

**Type:** integration  
**Product:** RiskIQ Digital Footprint  

RiskIQ Digital Footprint integration enables your security team to manage assets outside your firewall, by bringing its details, providing you to add or update assets and analyze your digital footprint from the view of the global adversary with the help of various commands that summarise the activities performed on your assets. This integration was integrated and tested with enterprise version of RiskIQDigitalFootprint

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## RiskIQDigitalFootprintAssetDetailsWidgetScript

**Type:** script  
**Product:** RiskIQ Digital Footprint  

Shows the detailed information of an asset identified as a "RiskIQAsset" type of indicator in the layout of the indicator


## RiskIQPassiveTotalComponentsScript

**Type:** script  
**Product:** PassiveTotal  

Enhancement script to enrich PassiveTotal components for Domain and IP type of indicators. It can be set by following these steps

**Inputs:**

- `indicator_value`: Domain or IP indicator value that need to enrich


## RiskIQPassiveTotalComponentsWidgetScript

**Type:** script  
**Product:** PassiveTotal  

Set widgets to custom layout in Domain, IP and RiskIQ Asset type of indicators


## RiskIQPassiveTotalHostPairChildrenScript

**Type:** script  
**Product:** PassiveTotal  

Enhancement script to enrich PassiveTotal host pair of children for Domain and IP type of indicators. It can be set by following these steps

**Inputs:**

- `indicator_value`: Domain or IP indicator value that need to enrich


## RiskIQPassiveTotalHostPairParentsScript

**Type:** script  
**Product:** PassiveTotal  

Enhancement script to enrich PassiveTotal host pair of parents for Domain and IP type of indicators. It can be set by following these steps

**Inputs:**

- `indicator_value`: Domain or IP indicator value that need to enrich


## RiskIQPassiveTotalHostPairsChildrenWidgetScript

**Type:** script  
**Product:** PassiveTotal  

Set widgets to custom layout in Domain, IP and RiskIQ Asset type of indicators


## RiskIQPassiveTotalHostPairsParentsWidgetScript

**Type:** script  
**Product:** PassiveTotal  

Set widgets to custom layout in Domain, IP and RiskIQ Asset type of indicators


## RiskIQPassiveTotalPDNSScript

**Type:** script  
**Product:** PassiveTotal  

Enhancement script to enrich PDNS information for Domain and IP type of indicators. It can be set by following these steps

**Inputs:**

- `indicator_value`: domain or IP indicator value that need to enrich


## RiskIQPassiveTotalPDNSWidgetScript

**Type:** script  
**Product:** PassiveTotal  

Set widgets to custom layout in Domain, IP and RiskIQ Asset type of indicators


## RiskIQPassiveTotalSSLScript

**Type:** script  
**Product:** PassiveTotal  

Enhancement script to enrich SSL information for Email, File SHA-1 and RiskIQSerialNumber type of indicators. It can be set by following these steps

**Inputs:**

- `indicator_value`: Email, File SHA-1 and RiskIQSerialNumber indicator value that need to enrich


## RiskIQPassiveTotalSSLWidgetScript

**Type:** script  
**Product:** PassiveTotal  

Set widgets to custom layout in Email, RiskIQSerialNumber and File SHA-1 type of indicators


## RiskIQPassiveTotalTrackersScript

**Type:** script  
**Product:** PassiveTotal  

Enhancement script to enrich web trackers information for Domain and IP type of indicators. It can be set by following these steps

**Inputs:**

- `indicator_value`: Domain or IP indicator value that need to enrich


## RiskIQPassiveTotalTrackersWidgetScript

**Type:** script  
**Product:** PassiveTotal  

Set widgets to custom layout in Domain, IP and RiskIQ Asset type of indicators


## RiskIQPassiveTotalWhoisScript

**Type:** script  
**Product:** PassiveTotal  

Enhancement script to enrich whois information for Domain and Email type of indicators. It can be set by following these steps

**Inputs:**

- `indicator_value`: domain or email indicator value that need to enrich


## RiskIQPassiveTotalWhoisWidgetScript

**Type:** script  
**Product:** PassiveTotal  

Set widgets to custom layout in Domain, Email and RiskIQ Asset type of indicators


## Screenshot Machine

**Type:** integration  
**Product:** Screenshot Machine  

Uses screenshot machine to get a screenshot

**Commands:**

- `None`: 


## TroubleshootAggregateResults

**Type:** script  
**Product:** Troubleshoot  

Collects all results from previous tasks. (Available from the platform.0.0.)

**Inputs:**

- `succeeded_changed_params`: Parameters that were changed and caused the integration to run successfully.
- `file_names`: All file entry IDs in the incident.
- `configuration`: The raw configuration output.
- `errors`: The errors when testing the instance.
- `execute_command_errors`: Errors from the ExecuteCommand automation.


## TroubleshootCloseAlertsByQuery

**Type:** script  
**Product:** Troubleshoot  

Closes alerts by receiving a list of alert IDs and executing the closure process for each

**Inputs:**

- `alert_ids`: A comma-separated list of alert IDs to close.


## TroubleshootExecuteCommand

**Type:** script  
**Product:** Troubleshoot  

Executes a command in the platform

**Inputs:**

- `command`: The command to run.
- `arguments`: The arguments of the command.
- `instance_name`: The instance name.


## TroubleshootExecutePlaybookByAlertQuery

**Type:** script  
**Product:** Troubleshoot  

Retrieves alerts based on a given query and filter arguments. It provides two operational modes

**Inputs:**

- `query`: A query string to filter alerts. For example, to fetch pending alerts, use "runStatus:\"Pending\"".
- `playbook_id`: The ID of the playbook to apply to the fetched alerts.
- `playbook_name`: The name of the playbook to apply to the fetched alerts.
- `limit`: The maximum number of alerts to retrieve.
- `incidentTypes`: A comma-separated list of alert types to filter the results by.
- `timeField`: The field to filter alerts by date range. Options are "created" or "modified". Default is "created". Use "modified" cautiously due to perfor
- `fromDate`: The start date for filtering alerts. Accepted formats are similar to those on the alerts query page (e.g., "3 days ago" or "2019-01-01T00:00
- `toDate`: The end date for filtering alerts. Accepted formats are similar to those on the alerts query page (e.g., "3 days ago" or "2019-01-01T00:00:0


## TroubleshootGetCommandandArgs

**Type:** script  
**Product:** Troubleshoot  

Gets a command with its arguments, validates the command and the arguments, and then parses it to use in the the platform

**Inputs:**

- `instance_name`: Instance on which to check the command.
- `command_line`: Command line to process.


## TroubleshootGetInstanceParameters

**Type:** script  
**Product:** Troubleshoot  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## TroubleshootInstanceField

**Type:** script  
**Product:** Troubleshoot  

Populates the InstanceName field with active instances


## TroubleshootIsDockerImageExists

**Type:** script  
**Product:** Troubleshoot  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## TroubleshootRestartFailedPlaybooks

**Type:** script  
**Product:** Troubleshoot  

Scans all non-closed alerts for playbook tasks in Error state and restarts them from the specific failed task. The script reopens each errored task and re-executes it, allowing the playbook to continue from where it stopped. Includes throttling support via the group_size and sleep_time arguments: after every group_size task restarts the script pauses for sleep_time seconds to avoid overloading the engine queue when scanning many alerts. This automation runs using the default Limited User role, unless you explicitly change the permissions. For more information, see the section about permissions here

**Inputs:**

- `max_alerts`: Maximum number of non-closed alerts to scan for failed tasks. The maximum allowed value is 200; any larger value will be clamped to 200.
- `days_back`: Only scan non-closed alerts that were modified within this number of days back. Defaults to 3.
- `group_size`: Number of tasks to restart before pausing. Helps avoid overwhelming the system.
- `sleep_time`: Number of seconds to pause between each group of restarted tasks.


## TroubleshootTestInstance

**Type:** script  
**Product:** Troubleshoot  

Multi-tenant environments should be configured with the Cortex Rest API instance when using this automation. Make sure the Use tenant parameter (in the Cortex Rest API integration) is checked to ensure that API calls are made to the current tenant instead of the master tenant


## Update Or Remove Assets - RiskIQ Digital Footprint

**Type:** playbook  
**Product:** RiskIQ Digital Footprint  

Checks if the user wants to update or remove the asset using various user inputs and performs the respective actions. Supported integration

**Inputs:**

- `asset_name`: Name of the asset.
- `asset_type`: Type of the asset. Possible values: Domain, Host, IP Address, IP Block, ASN, Page, SSL Cert, Contact.
- `support_email_address`: The contact email address of the support team from which manual inputs should be fetched.


## VirusTotal (API v3)

**Type:** integration  
**Product:** VirusTotal  

This integration analyzes suspicious hashes, URLs, domains, and IP addresses. The integration was integrated and tested with version v3 API of VirusTotal

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## VirusTotal - Premium (API v3)

**Type:** integration  
**Product:** VirusTotal  

Use the premium API capabilities of VirusTotal to analyze retro hunts, read live hunt notifications, and download files from VirusTotal. The differences between VirusTotal's Public API and Premium API can be found in the VirusTotal v3 API documentation. This integration was integrated and tested with VirusTotal - Premium (API v3)

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Windows Remote Management (Beta)

**Type:** integration  
**Product:** Windows Remote Management  

Uses the Python pywinrm library and commands to execute either a process or using Powershell scripts. This integration was integrated and tested with Windows Remote Management

**Commands:**

- `None`: 
- `None`: 


## xDome

**Type:** integration  
**Product:** Claroty xDome  

Use the xDome integration to manage assets and alerts. This integration was integrated and tested with version 1.0.0 of XDome

**Commands:**

- `None`: 
- `None`: 
- `None`: 

