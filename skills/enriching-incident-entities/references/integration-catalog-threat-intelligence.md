# Integration and Automation Catalog - Threat Intelligence

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## ACTI Block High Severity Indicators

**Type:** playbook  
**Product:** Accenture CTI v2  
**Inputs:**

- `IP`: Considers IP(s) which have severity 5 or more
- `URL`: Considers URL(s) which have severity 5 or more
- `Domain`: Considers Domain(s) which have severity 5 or more


## ACTI Create Report-Indicator Associations

**Type:** playbook  
**Product:** Accenture CTI v2  
**Inputs:**

- `IP`: The extracted IP address.
- `IA`: The Intelligence Alert associated with the indicator.
- `IR`: The Intelligence Report associated with the indicator.
- `URL`: The extracted URL.
- `Domain`: The extracted Domain.
- `MFam`: The Malware Family associated with the indicator.
- `TA`: The Threat Actor associated with the indicator.
- `TG`: The Threat Group associated with the indicator.


## ACTI Indicator Query

**Type:** integration  
**Product:** Accenture CTI v2  

ACTI provides intelligence regarding security threats and vulnerabilities. This integration was integrated and tested with version 2.93.0 of ACTI

**Commands:**

- `ip`: Checks the reputation of the given IP address.
- `domain`: Checks the reputation of the given domain.
- `url`: Checks the reputation of the given URL.
- `acti-get-ioc-by-uuid`: Checks reputation of a specific indicator(URL/IP/Domain) uuid.
- `acti-get-fundamentals-by-uuid`: Checks reputation of a specific Malware Family/ Threat Campaign/ Threat Group/ Threat Actor.
- `acti-getThreatIntelReport`: Fetches Intelligence Alerts & Intelligence Reports.


## ACTI Vulnerability Query

**Type:** integration  
**Product:** Accenture CTI v2  

Accenture CTI provides intelligence regarding security threats and vulnerabilities. This integration was integrated and tested with version v2.93.0 of ACTI

**Commands:**

- `acti-vuln`: Checks the reputation of the given common vulnerabilities and exposures ID.


## Active Directory - Get User Manager Details

**Type:** playbook  
**Product:** Active Directory Query  

Takes an email address or a username of a user account in Active Directory, and returns the email address of the user's manager

**Inputs:**

- `Username`: Search for user by the sAMAccountName attribute in Active Directory.
- `UserEmail`: Search for user by the email attribute in Active Directory.


## Active Directory Query v2

**Type:** integration  
**Product:** Active Directory Query  

The Active Directory Query integration enables you to access and manage Active Directory objects (users, contacts, and computers). This integration was integrated and tested with version 1.5.0 of Active Directory Query v2 Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `ad-expire-password`: Expires the password of an Active Directory user.
- `ad-modify-password-never-expire`: Modifies the AD account attribute "Password Never Expire".
- `ad-create-user`: Creates an Active Directory user. This command requires a secure connection (SSL,TLS).
- `ad-search`: Runs Active Directory queries.
- `ad-add-to-group`: Adds an Active Directory user or computer to a group.
- `ad-remove-from-group`: Removes an Active Directory user or computer from a group.
- `ad-update-user`: Updates attributes of an existing Active Directory user.
- `ad-delete-user`: Deletes an Active Directory user.
- `ad-create-contact`: Creates an Active Directory contact.
- `ad-update-contact`: Updates attributes of an existing Active Directory contact.
- `ad-disable-account`: Disables an Active Directory user account.
- `ad-enable-account`: Enables a previously disabled Active Directory account.
- `ad-unlock-account`: Unlocks a previously locked Active Directory user account.
- `ad-set-new-password`: Sets a new password for an Active Directory user. This command requires a secure connection (SSL,TLS).
- `ad-modify-computer-ou`: Modifies the computer organizational unit within a domain.


## ActiveMQ

**Type:** integration  
**Product:** ActiveMQ  
**Commands:**

- `activemq-send`: Sends a message to the specified destination.
- `activemq-subscribe`: Subscribes to and reads messages from a topic or queue. Must provide either queue-name or topic-name. You can't provide both.


## ADGetUser

**Type:** script  
**Product:** Active Directory Query  

Retrieves detailed information about a user account. The user can be specified by "name", "email" or as an "Active Directory Distinguished Name" (DN). If no filter is provided, the result will show all users

**Inputs:**

- `dn`: The Active Directory Distinguished Name for the desired user.
- `name`: The name of the desired user.
- `attributes`: Include these AD attributes of the resulting objects in addition to the default ones.
- `customFieldType`: Search for a user by this custom field type.
- `customFieldData`: Search for a user by this custom field data (relevant only if customFieldType is provided).
- `headers`: The columns headers to show the order by.
- `nestedSearch`: Select "true" to allow nested groups search as well.
- `username`: The samAccountName of the desire user.


## Alibaba ActionTrail - multiple unauthorized action attempts detected by a user

**Type:** playbook  
**Product:** Alibaba Action Trail  

This playbook investigates an “Alibaba ActionTrail - multiple unauthorized action attempts detected by a user” alert by gathering user and IP information and performing remediation based on the information gathered and received from the user. Used Sub-playbooks: To link this playbook to the relevant alerts automatically, we recommend using the following filters when configuring the playbook triggers: Alert Source = Correlation Alert Name = Alibaba ActionTrail - multiple unauthorized action attempts detected by a user

**Inputs:**

- `InternalRange`: List of internal IP ranges


## Anomali ThreatStream v3

**Type:** integration  
**Product:** Anomali ThreatStream  

Use Anomali ThreatStream to query and submit threats. Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `ip`: Checks the reputation of the given IP address.
- `domain`: Checks the reputation of the given domain name.
- `file`: Checks the reputation of the given hash of the file.
- `threatstream-email-reputation`: Checks the reputation of the given email address.
- `threatstream-get-passive-dns`: Returns enrichment data for Domain or IP for available observables.
- `threatstream-import-indicator-with-approval`: Imports indicators (observables) into ThreatStream. The imported data must be approved using the ThreatStream UI. The data can be imported using one of three me
- `threatstream-import-indicator-without-approval`: Imports indicators (observables) into ThreatStream. Approval is not required for the imported data. You must have the Approve Intel user permission to import wi
- `threatstream-get-model-list`: Returns a list of threat models.
- `threatstream-get-model-description`: Returns an HTML file with a description of the threat model.
- `threatstream-get-indicators-by-model`: Returns a list of indicators associated with the specified model and ID of the model.
- `threatstream-submit-to-sandbox`: Submits a file or URL to the ThreatStream-hosted sandbox for detonation.
- `threatstream-get-analysis-status`: Returns the current status of the report submitted to the sandbox. The report ID is returned from the threatstream-submit-to-sandbox command.
- `threatstream-analysis-report`: Returns the report of a file or URL submitted to the sandbox.
- `threatstream-get-indicators`: Return filtered indicators from ThreatStream. If a query is defined, it overrides all other arguments that were passed to the command.
- `threatstream-add-tag-to-model`: Adds tags to intelligence to filter for related entities.


## ARIA Packet Intelligence

**Type:** integration  
**Product:** ARIAPacketIntelligence  

The ARIA Cybesecurity Solutions Software-Defined Security (SDS) platform integrates with the platform. The combination of ARIA hardware, in the form of a Secure Intelligent Adapter (SIA), and software, specifically Packet Intelligence and SDS orchestrator (SDSo), provides the elements required to react instantly when an incident is detected. When integrated with the ARIA solution, you can create playbooks that instruct one or more SIAs to add, modify, or delete rules automatically. These rule changes, which take effect immediately, can block conversations, redirect packets to a recorder or VLAN, or perform a variety of other actions. This integration was integrated and tested with version 1.0.9 of ARIA Packet Intelligence

**Commands:**

- `aria-block-conversation`: Creates a rule that drops all packets that match the specified 5-tuple values.
- `aria-block-conversation`: 
- `aria-unblock-conversation`: Deletes a named rule from the 5-tuple logic block. This allows the previously blocked conversation to resume.
- `aria-unblock-conversation`: 
- `aria-record-conversation`: Creates a rule that redirects a conversation that matches 5-tuple values to the Packet Recorder. Packets are tagged with the VID specified in the instance.
- `aria-record-conversation`: 
- `aria-stop-recording-conversation`: Removes the named rule from the 5-tuple block. This stops redirecting traffic to the Packet Recorder.
- `aria-stop-recording-conversation`: 
- `aria-alert-conversation`: Adds a rule that generates an alert when a conversation that matches the specified 5-tuple values is detected.
- `aria-alert-conversation`: 
- `aria-mute-alert-conversation`: Removes a named rule from the 5-tuple logic block, disabling the alerts.
- `aria-mute-alert-conversation`: 
- `aria-block-dest-port`: Creates a rule that blocks packets destined for one or more specified ports.
- `aria-block-dest-port`: 
- `aria-unblock-dest-port`: Removes a named rule from the destination port logic block. This allows the previously blocked traffic to resume.


## ATD - Detonate File

**Type:** playbook  
**Product:** McAfee Advanced Threat Defense  

Detonates a File using the McAfee Advanced Threat Defense sandbox. Advanced Threat Defense supports the following File Types: 32-bit Portable Executables (PE)files; 64-bit PE+files exe, sys, dll, com, scr, cpl, ocx, cgi. Microsoft Office Suite documents: doc, dotm, docx, dotx, xls, ppam, xlsx, pps, xlsb, ppsx, xlsm, ppsm, ppt, ppt, pptx, pptm, rtf, shs, xltm, sldm, xltx, sldx, xlam, thmx, docm, xar. Just Systems Ichitaro documents: jtd, jtdc. Adobe pdf, swf. Compressed files: gz, 7z, tgz, msi, zip, lzh, cab, lzma, rar. Android application package: apk, Java, JAR, CLASS, Java Script, Java bin files. Image files: jpeg, png, gif. Other file types: cmd, ace, bat, arj, vbs, chm, xml, lnk, url, mof, htm, ocx, html, potm, eml, potx, msg, ps1, vb, reg, vba, wsc, vbe, wsf, vbs, wsh

**Inputs:**

- `File`: The file to detonate. The file is taken from the context.
- `Interval`: How often the polling command should run (in minutes).
- `Timeout`: How much time to wait before a timeout occurs (in minutes).


## ATDDetonate

**Type:** script  
**Product:** McAfee Advanced Threat Defense  

Detonates a file or URL through McAfee ATD

**Inputs:**

- `vmProfileList`: The analyzer of a profile's ID. The profile ID number can be found in the UI Policy/Analyzer Profile page, Or using the command atd-list-ana
- `submitType`: This parameter accepts four values. Can be, "0", "1", "2" and "3". "0" - a regular file upload. "1" - a URL submission. The URL link is proc
- `url`: Any valid web URL.
- `messageId`: The maximum number character string which is 128.
- `srcIp`: The IPv4 address of the source system or gateway from where the file is downloaded.
- `dstIp`: The IPv4 address of the target endpoint.
- `skipTaskId`: The value "0" indicates corresponding taskID in API response. The value "1" indicates -1 as a taskID in API response.
- `analyzeAgain`: The value "0" indicates to skip sample analysis if it was analyzed previously . The value "2" indicates to not skip sample analysis if it wa


## Block Indicator - Infoblox Cloud

**Type:** playbook  
**Product:** Infoblox Threat Defense with DDI  

This playbook blocks the given IP or domain by adding it to the given block type custom list of the Infoblox Cloud platform. If prompted it also removes the provided indicators from given allow list

**Inputs:**

- `ip_addresses`: The IP addresses to block.
- `domains`: The domains to block.
- `custom_list_name`: Specify the name of the custom list to add the given IP addresses or domains to. Default is "Default Block".
- `custom_list_type`: Specify the type of the custom list to add the given IP addresses or domains to. Possible values are: default_block, custom_list, threat_ins


## Blueliv ThreatCompass

**Type:** integration  
**Product:** Blueliv ThreatCompass  

Blueliv ThreatCompass systematically looks for information about companies,products, people, brands, logos, assets, technology and other information, depending on your needs. Blueliv ThreatCompass allows you to monitor and track all this information to keep your data, your organization and its employees safe

**Commands:**

- `blueliv-resource-all`: Recovers all resources from the module.
- `blueliv-resource-search`: Search for a specific resource.
- `blueliv-resource-set-read-status`: Mark the result as read or not.
- `blueliv-resource-assign-rating`: Assign tating to a given result.
- `blueliv-resource-fav`: Changes the favourite status of a resource.
- `blueliv-resource-set-tlp`: Sets a new TLP status to a given resource.


## Blueliv ThreatContext

**Type:** integration  
**Product:** Blueliv ThreatContext  

The Threat Context module provides SOC, Incident Response and Threat Intelligence teams with continuously updated and intuitive information around threat actors, campaigns, malware indicators, attack patterns, tools, signatures and CVEs

**Commands:**

- `blueliv-authenticate`: Authenticate and get the API token
- `blueliv-tc-malware`: Gets information about malware by ID
- `blueliv-tc-indicator-ip`: Gets information about an IP
- `blueliv-tc-cve`: Gets information about CVE
- `blueliv-tc-indicator-fqdn`: Gets information about FQDN
- `blueliv-tc-indicator-cs`: Gets information about a Crime Server
- `blueliv-tc-threat-actor`: Gets information about a Threat Actor
- `blueliv-tc-campaign`: Gets information about a Campaign
- `blueliv-tc-attack-pattern`: Gets information about a Attack Pattern
- `blueliv-tc-tool`: Gets information about a Tool
- `blueliv-tc-signature`: Gets information about a Signature


## Brandefense Digital Risk Protection Services

**Type:** integration  
**Product:** Brandefense Digital Risk Protection Services  

Brandefense is a SaaS platform offering Digital Risk Protection Services (DRPS), External Attack Surface Management (EASM), and Actionable Threat Intelligence. This integration connects the platform, brand monitoring, and phishing response operations

**Commands:**

- `ip`: Investigate an IP address against Brandefense threat intelligence.
- `domain`: Investigate a domain against Brandefense threat intelligence.
- `url`: Investigate a URL against Brandefense threat intelligence.
- `file`: Investigate a file hash against Brandefense threat intelligence.
- `brandefense_get_incidents`: Get Brandefense incidents with optional filtering by status, module, category, and time period.
- `brandefense_get_incident_detail`: Get detailed information for a specific Brandefense incident.
- `brandefense_change_incident_status`: Change the status of a Brandefense incident.
- `brandefense_incident_indicators`: Get indicators associated with a Brandefense incident.
- `brandefense_get_incident_relatives`: Get related incidents for a specific Brandefense incident.
- `threat_search`: Perform a CTI threat search and poll for results using ScheduledCommand.
- `brandefense_get_intelligences`: Get Brandefense intelligence reports with optional filtering.
- `brandefense_get_intelligence_detail`: Get detailed information for a specific intelligence report.
- `brandefense_intelligence_indicators`: Get indicators associated with a Brandefense intelligence report.
- `brandefense_get_intelligence_rules`: Get rules associated with a Brandefense intelligence report.
- `brandefense_get_assets`: Get list of monitored assets from Brandefense.


## Check Point Threat Emulation (SandBlast)

**Type:** integration  
**Product:** Check Point Threat Emulation (SandBlast)  

Threat Emulation performs remote analysis by uploading files to a virtual SandBox. Uploaded files are monitored in multiple OS and microsoft office application versions. Malicious files are saved in the ThreatCloud. Safe files are available for download after inspection. Upload files using polling, the service supports Microsoft Office files, as well as PDF, SWF, archives and executables. Active content will be cleaned from any documents that you upload (Microsoft Office and PDF files only). Query on existing IOCs, file status, analysis, reports. Download files from the database. Supports both appliance and cloud. Supported Threat Emulation versions are any R80x. This integration was integrated and tested with version v1 of CheckPointSandBlast

**Commands:**

- `file`: Runs reputation on files.
- `sandblast-query`: Use the Query API to have a client application look for either the analysis report of a specific file on the Check Point Threat Prevention service databases or 
- `sandblast-upload`: Use the Upload API to have a client application request that Check Point Threat Prevention modules scan and analyze a file. When you upload a file to the servic
- `sandblast-download`: Use the Download API to download a scanned file from the ThreatCloud according to the file ID.
- `sandblast-quota`: Use the Quote API to have a client application get the current license and quota status of the API Key that you use in the authorization of the other APIs. For 


## Cofense Intelligence v2

**Type:** integration  
**Product:** Cofense Intelligence v2  

Use the Cofense Intelligence integration to check the reputation of domains, URLs, IP addresses, file hashes, and email addresses. This integration was integrated and tested with version 2 of Cofense Intelligence Some changes have been made that might affect your existing content. For more information, see Breaking Changes. Search for threats associated with an indicator. The verdict (Unknown, Benign, Suspicious, Malicious) of each threat is determined by the impact (None, Minor, Moderate, Major) of its associated web locations as detected in cofense, along with a threshold value that is being set by the user (when configuring the instance): for each Threat, if the searched indicator is found in the report - we will use its impact as the verdict, else will use the maximal impact in the report. Example: Threshold = Major (Default value)

**Commands:**

- `ip`: Checks the reputation of an IP address.
- `cofense-search`: Retrieves a specific threat or a list of threats based on the filter values provided in the command arguments.
- `file`: Checks the reputation of a file hash.
- `email`: Checks the reputation of an email address.
- `url`: Checks the reputation of a URL.
- `domain`: Checks the reputation of the domain.
- `cofense-threat-report-get`: Downloads threat report provided by cofense intelligence of an indicator for the given unique report id.


## Compare Process Execution Arguments To LOLBAS Patterns

**Type:** playbook  
**Product:** LOLBAS Feed  

This playbook takes a process name and determines its presence in the LOLBAS repository. It then proceeds to compare the incident command line against known patterns of malicious commands listed in TIM by using LOLBAS feed integration. The playbook outputs results when the similarity between the analyzed command line and the malicious patterns is greater than or equal to the preconfigured StringSimilarity threshold. The playbook offers the flexibility to adjust this threshold through the use of the dedicated playbook input, 'StringSimilarityThreshold'

**Inputs:**

- `ProcessName`: The process names.
- `Commandline`: The command lines.
- `StringSimilarityThreashold`: StringSimilarity automation threshold. The automation will output only the results with a similarity score equal to or greater than the give


## Courses of Action - Collection

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook handles MITRE ATT&CK Techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: MITRE ATT&CK Description: The adversary is attempting to gather data of interest to accomplish their goal. Collection consists of techniques adversaries may use to gather information and the sources information is collected from that are relevant to following through on the adversary’s objectives. Frequently, the next goal after collecting data is to steal (exfiltrate) the data. Common target sources include various drive types, browsers, audio, video, and email. Common collection methods include capturing screenshots and keyboard input. Possible playbook triggers

**Inputs:**

- `technique`: Mitre ATT&amp;CK ID of a technique.


## Courses of Action - Command and Control

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook handles MITRE ATT&CK Techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. It utilizes each of the sub-playbooks for specific techniques that belong to this phase (tactic) according to the MITRE ATT&CK kill chain. The sub-playbook called depends on the technique input. ***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Tactic: MITRE ATT&CK Description: The adversary is trying to communicate with compromised systems to control them. Command and Control consists of techniques that adversaries may use to communicate with systems under their control within a victim network. Adversaries commonly attempt to mimic normal, expected traffic to avoid detection. There are many ways an adversary can establish command and control with various levels of stealth depending on the victim’s network structure and defenses. Possible playbook triggers

**Inputs:**

- `technique`: Mitre ATT&amp;CK ID of a technique.
- `template`: Template name to enforce WildFire best practices profile.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## Courses of Action - Credential Access

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook handles MITRE ATT&CK Techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. It utilizes each of the sub-playbooks for specific techniques that belong to this phase (tactic) according to the MITRE ATT&CK kill chain. The sub-playbook called depends on the technique input. ***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Tactic: MITRE ATT&CK Description: The adversary is trying to steal account names and passwords. Credential Access consists of techniques for stealing credentials like account names and passwords. Techniques used to get credentials include keylogging or credential dumping. Using legitimate credentials can give adversaries access to systems, make them harder to detect, and provide the opportunity to create more accounts to help achieve their goals. Possible playbook triggers

**Inputs:**

- `technique`: Mitre ATT&amp;CK ID of a technique.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## Courses of Action - Defense Evasion

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook handles MITRE ATT&CK Techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. It utilizes each of the sub-playbooks for specific techniques that belong to this phase (tactic) according to the MITRE ATT&CK kill chain. The sub-playbook called depends on the technique input. ***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Tactic: MITRE ATT&CK Description: The adversary is trying to avoid being detected. Defense Evasion consists of techniques that adversaries use to avoid detection throughout their compromise. Techniques used for defense evasion include uninstalling/disabling security software or obfuscating/encrypting data and scripts. Adversaries also leverage and abuse trusted processes to hide and masquerade their malware. Other tactics’ techniques are cross-listed here when those techniques include the added benefit of subverting defenses. Possible playbook triggers

**Inputs:**

- `technique`: Mitre ATT&amp;CK ID of a technique.
- `template`: Template name to enforce WildFire best practices profile.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## Courses of Action - Discovery

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook handles MITRE ATT&CK Techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. It utilizes each of the sub-playbooks for specific techniques that belong to this phase (tactic) according to the MITRE ATT&CK kill chain. The sub-playbook called depends on the technique input. ***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Tactic: MITRE ATT&CK Description: The adversary is trying to figure out your environment. Discovery consists of techniques an adversary may use to gain knowledge about the system and internal network. These techniques help adversaries observe the environment and orient themselves before deciding how to act. They also allow adversaries to explore what they can control and what’s around their entry point in order to discover how it could benefit their current objective. Native operating system tools are often used toward this post-compromise information-gathering objective. Possible playbook triggers

**Inputs:**

- `technique`: Mitre ATT&CK ID of a technique.


## Courses of Action - Execution

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook handles MITRE ATT&CK Techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. It utilizes each of the sub-playbooks for specific techniques that belong to this phase (tactic) according to the MITRE ATT&CK kill chain. The sub-playbook called depends on the technique input. ***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Tactic: MITRE ATT&CK Description: The adversary is trying to run malicious code. Execution consists of techniques that result in adversary-controlled code running on a local or remote system. Techniques that run malicious code are often paired with techniques from all other tactics to achieve broader goals, like exploring a network or stealing data. For example, an adversary might use a remote access tool to run a PowerShell script that does Remote System Discovery. Possible playbook triggers

**Inputs:**

- `technique`: Mitre ATT&amp;CK ID of a technique.
- `template`: Template name to enforce WildFire best practices profile.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## Courses of Action - Exfiltration

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook handles MITRE ATT&CK Techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. It utilizes each of the sub-playbooks for specific techniques that belong to this phase (tactic) according to the MITRE ATT&CK kill chain. The sub-playbook called depends on the technique input. ***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Tactic: MITRE ATT&CK Description: The adversary is trying to steal data. Exfiltration consists of techniques that adversaries may use to steal data from your network. Once they’ve collected data, adversaries often package it to avoid detection while removing it. This can include compression and encryption. Techniques for getting data out of a target network typically include transferring it over their command and control channel or an alternate channel and may also include putting size limits on the transmission. Possible playbook triggers

**Inputs:**

- `technique`: Mitre ATT&amp;CK ID of a technique.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## Courses of Action - Impact

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook handles MITRE ATT&CK Techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. It utilizes each of the sub-playbooks for specific techniques that belong to this phase (tactic) according to the MITRE ATT&CK kill chain. The sub-playbook called depends on the technique input. ***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Tactic: MITRE ATT&CK Description: The adversary is trying to manipulate, interrupt, or destroy your systems and data. Impact consists of techniques that adversaries use to disrupt availability or compromise integrity by manipulating business and operational processes. Techniques used for impact can include destroying or tampering with data. In some cases, business processes can look fine, but may have been altered to benefit the adversaries’ goals. These techniques might be used by adversaries to follow through on their end goal or to provide cover for a confidentiality breach. Possible playbook triggers

**Inputs:**

- `technique`: Mitre ATT&amp;CK ID of a technique.


## Courses of Action - Initial Access

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook handles MITRE ATT&CK Techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. It utilizes each of the sub-playbooks for specific techniques that belong to this phase (tactic) according to the MITRE ATT&CK kill chain. The sub-playbook called depends on the technique input. ***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Tactic: MITRE ATT&CK Description: The adversary is trying to get into your network. Initial Access consists of techniques that use various entry vectors to gain their initial foothold within a network. Techniques used to gain a foothold include targeted spearphishing and exploiting weaknesses on public-facing web servers. Footholds gained through initial access may allow for continued access, like valid accounts and use of external remote services, or may be limited-use due to changing passwords. Possible playbook triggers

**Inputs:**

- `technique`: Mitre ATT&amp;CK ID of a technique
- `template`: Template name to enforce WildFire best practices profile.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## Courses of Action - Lateral Movement

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook handles MITRE ATT&CK Techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. It utilizes each of the sub-playbooks for specific techniques that belong to this phase (tactic) according to the MITRE ATT&CK kill chain. The sub-playbook called depends on the technique input. ***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Tactic: MITRE ATT&CK Description: The adversary is trying to move through your environment. Lateral Movement consists of techniques that adversaries use to enter and control remote systems on a network. Following through on their primary objective often requires exploring the network to find their target and subsequently gaining access to it. Reaching their objective often involves pivoting through multiple systems and accounts to gain. Adversaries might install their own remote access tools to accomplish Lateral Movement or use legitimate credentials with native network and operating system tools, which may be stealthier. Possible playbook triggers

**Inputs:**

- `technique`: Mitre ATT&amp;CK ID of a technique.


## Courses of Action - Persistence

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook handles MITRE ATT&CK Techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. It utilizes each of the sub-playbooks for specific techniques that belong to this phase (tactic) according to the MITRE ATT&CK kill chain. The sub-playbook called depends on the technique input. ***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Tactic: MITRE ATT&CK Description: The adversary is trying to maintain their foothold. Persistence consists of techniques that adversaries use to keep access to systems across restarts, changed credentials, and other interruptions that could cut off their access. Techniques used for persistence include any access, action, or configuration changes that let them maintain their foothold on systems, such as replacing or hijacking legitimate code or adding startup code. Possible playbook triggers

**Inputs:**

- `technique`: Mitre ATT&amp;CK ID of a technique.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## Courses of Action - Privilege Escalation

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook handles MITRE ATT&CK Techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. It utilizes each of the sub-playbooks for specific techniques that belong to this phase (tactic) according to the MITRE ATT&CK kill chain. The sub-playbook called depends on the technique input. ***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Tactic: MITRE ATT&CK Description: The adversary is trying to gain higher-level permissions. Privilege Escalation consists of techniques that adversaries use to gain higher-level permissions on a system or network. Adversaries can often enter and explore a network with unprivileged access but require elevated permissions to follow through on their objectives. Common approaches are to take advantage of system weaknesses, misconfigurations, and vulnerabilities. Examples of elevated access include: • SYSTEM/root level• local administrator• user account with admin-like access • user accounts with access to specific system or perform specific functionThese techniques often overlap with Persistence techniques, as OS features that let an adversary persist can execute in an elevated context. Possible playbook triggers

**Inputs:**

- `technique`: Mitre ATT&amp;CK ID of a technique.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## CTIX - Delete Flagged Indicators

**Type:** playbook  
**Product:** Cyware Intel Exchange  

Deletes indicators ingested from Cyware Intel Exchange (CTIX v3) that are flagged as deprecated, revoked, false positive, reviewed, or whitelisted, by running the CTIXDeleteFlaggedIndicators script. All delete flags default to false, so the playbook does nothing until at least one flag input is enabled. It is intended to run on a schedule via the bundled CTIX - Delete Flagged Indicators job — jobs cannot pass per-run inputs, so enable the desired flags once by editing the playbook input defaults (or the job's playbook input overrides). Note: an indicator flagged in CTIX is only picked up after the CTIX v3 feed re-fetches it, which updates the indicator's flag fields in the Threat Intel Module; the next run then finds and deletes it

**Inputs:**

- `delete_deprecated`: Whether to delete indicators marked as deprecated in Cyware Intel Exchange (CTIX).
- `delete_revoked`: Whether to delete indicators revoked by their source in Cyware Intel Exchange (CTIX).
- `delete_false_positive`: Whether to delete indicators marked as false positive in Cyware Intel Exchange (CTIX).
- `delete_whitelisted`: Whether to delete indicators allow-listed in Cyware Intel Exchange (CTIX).
- `delete_reviewed`: Whether to delete indicators that have been reviewed in Cyware Intel Exchange (CTIX).
- `exclude`: Whether to also add the deleted indicators to the Exclusion List. When false (default), indicators are purely deleted and can be re-created 
- `reason`: Reason recorded for the deletion (and exclusion, if enabled).


## CTIXDeleteFlaggedIndicators

**Type:** script  
**Product:** Cyware Intel Exchange  

Deletes indicators ingested from Cyware Intel Exchange (CTIX v3) that are flagged as deprecated, revoked, false positive, reviewed, or whitelisted. The script builds a Threat Intel query scoped to indicators from the CTIX v3 integration (sourceBrands:"CTIX v3") with any of the enabled flag fields set, and runs the built-in deleteIndicators command on the matches. All delete flags are disabled by default — the script does nothing until at least one flag is explicitly enabled, so it can never issue an unscoped delete. It is intended to be run on a schedule via the bundled CTIX - Delete Flagged Indicators job (which triggers the playbook of the same name), but can also be run manually from the War Room or Playground. Note: this script only deletes indicators whose flag fields are already up to date in the Threat Intel Module — run the CTIX feed fetch first so it can update those fields, then run this script (or the bundled job/playbook) to pick up the changes

**Inputs:**

- `delete_deprecated`: Whether to delete indicators marked as deprecated in Cyware Intel Exchange (CTIX). Default is false.
- `delete_revoked`: Whether to delete indicators revoked by their source in Cyware Intel Exchange (CTIX). Default is false.
- `delete_false_positive`: Whether to delete indicators marked as false positive in Cyware Intel Exchange (CTIX). Default is false.
- `delete_whitelisted`: Whether to delete indicators allow-listed in Cyware Intel Exchange (CTIX). Default is false.
- `delete_reviewed`: Whether to delete indicators that have been reviewed in Cyware Intel Exchange (CTIX). Default is false.
- `exclude`: Whether to also add the deleted indicators to the Exclusion List. When false (default), indicators are purely deleted and can be re-created 
- `reason`: The reason recorded for the deletion (and exclusion, if enabled).


## CVE-2023-34362 - MOVEit Transfer SQL Injection

**Type:** playbook  
**Product:** CVE-2023-34362 - MOVEit Transfer SQL Injection  

A critical vulnerability has been identified in MOVEit Transfer, a managed file transfer solution. The vulnerability affects versions prior to the latest release and involves improper input validation. Exploiting this vulnerability can lead to remote execution of arbitrary code, potentially resulting in unauthorized access and compromise of sensitive data. To mitigate the risk associated with this vulnerability, it is crucial for users to update to the latest version of MOVEit Transfer that includes necessary security patches. This playbook should be triggered manually or can be configured as a job. Please create a new incident and choose the CVE-2023-34362 - MOVEit SQL Injection playbook and Rapid Breach Response incident type. The playbook includes the following tasks: IoCs Collection Hunting: The hunting queries are searching for the following activities: Mitigations: References: CVE-2023-34362: MOVEit Transfer SQL Injection Vulnerability Threat Brief MOVEit Transfer Critical Vulnerability (May 2023) Note: This is a beta playbook, which lets you implement and test pre-release software. Since the playbook is beta, it might contain bugs. Updates to the pack during the beta phase might include non-backward compatible features. We appreciate your feedback on the quality and usability of the pack to help us identify issues, fix them, and continually improve

**Inputs:**

- `PlaybookDescription`: The playbook description to be used in the Rapid Breach Response - Set Incident Info sub-playbook.
- `autoBlockIndicators`: Wether to block the indicators automatically.
- `QRadarTimeRange`: The time range for the QRadar queries.
- `SplunkEarliestTime`: The time range for the Splunk queries.
- `ElasticEarliestTime`: The time range for the Elastic queries.
- `LogAnalyticsTimespan`: The time range for the Azure Log Analytics queries.
- `XQLTimeRange`: The time range for the XQL queries.
- `ElasticIndex`: The elastic index to search in.


## Cybersixgill Actionable Alerts

**Type:** integration  
**Product:** Cybersixgill Actionable Alerts  

Cybersixgill automatically collects intelligence in real-time on all items that appear in the underground sources which we monitor. By using various rules and machine learning models, Cybersixgill automatically correlates these intelligence items with pre defined organization assets, and automatically alerts users in real time of any relevant intelligence items. The integration will focus on retrieving Cybersixgill's Actionable Alerts as incidents

**Commands:**

- `cybersixgill-update-alert-status`: updates the existing actionable alert status


## CybersixgillActionableAlertStatusUpdate

**Type:** script  
**Product:** Cybersixgill Actionable Alerts  

Updates the Actionable alert status


## Cypho Threat Intelligence

**Type:** integration  
**Product:** Cypho Threat Intelligence  

This integration enables your organization to efficiently collect, analyze, and respond to actionable cyber alerts generated within the Cypho platform enhancing visibility, automation, and overall security posture

**Commands:**

- `cypho-get-incident`: Retrieves the full details of a specific security incident from Cypho using its unique ticket_id. This command returns the raw response from the Cypho API, incl
- `cypho-assign-incident`: Assign a Cypho issue to an analyst by constructing their email from the given username and domain. The incident is assigned and updated with this user’s email.
- `cypho-add-comment`: This command sends a comment as the status_reason parameter and attributes it to a user constructed from the provided username and domain. It is used to log inv
- `cypho-update-severity`: Updates the severity level of a specific Cypho issue using its unique ticket ID. This command is used to escalate or de-escalate the risk level ("Low", "Moderat
- `cypho-download-attachment`: Downloads one or more attachments from a Cypho incident using the incident's unique "ticket_id". The command retrieves the attachment URLs from the issue and re
- `cypho-approve-dismiss-issue`: Approves or dismisses a Cypho issue based on the provided ticket ID, user email, and approval decision.


## CyphoAddCommentButton

**Type:** script  
**Product:** Cypho Threat Intelligence  

This automation allows analysts to add a comment to a Cypho issue directly from the platform. The script is designed to be used as a button automation on Cypho-related incidents. When executed, it synchronizes the analyst’s comment from platform to the corresponding issue in Cypho, ensuring that investigation notes, explanations, and analyst feedback remain consistent across both platforms. The automation validates that the incident is properly assigned to an owner before executing the action. This ensures accountability, accurate analyst activity tracking, and alignment with Cypho’s incident management workflow


## CyphoApproveIssue

**Type:** script  
**Product:** Cypho Threat Intelligence  

This automation allows analysts to approve a Cypho issue directly from the platform. The script synchronizes the approval action with Cypho, ensuring that the issue status in Cypho accurately reflects the decision made by the analyst in platform. This eliminates the need for manual approval actions in external systems and maintains consistency across platforms. The automation enforces ownership validation before execution, ensuring that the incident is assigned to an analyst. This guarantees proper accountability, accurate activity tracking, and reliable SOC metrics such as MTTR and analyst attribution


## CyphoAssignToMeButton

**Type:** script  
**Product:** Cypho Threat Intelligence  

This automation allows an analyst to assign a Cypho-related incident to themselves directly from the platform. The script synchronizes the assignment action with Cypho, ensuring that the issue owner is updated consistently across both platforms. This guarantees accurate ownership tracking, accountability, and proper analyst attribution throughout the incident lifecycle. The automation is designed to simplify incident ownership management by eliminating manual assignment steps in Cypho. Once executed, the incident is immediately assigned to the current analyst in platform and reflected accordingly in Cypho


## CyphoDismissIssue

**Type:** script  
**Product:** Cypho Threat Intelligence  

This automation allows analysts to dismiss a Cypho issue directly from the platform. The script synchronizes the dismissal action from platform to Cypho, ensuring that the issue status remains consistent across both platforms. This eliminates the need for analysts to manually update issue status in Cypho and helps maintain a clean and accurate incident lifecycle. The automation enforces incident ownership validation before execution. This guarantees that only an assigned analyst can dismiss an issue, preserving accountability, accurate audit trails, and reliable SOC performance metrics such as MTTR and analyst attribution


## CyphoDownloadAttachments

**Type:** script  
**Product:** Cypho Threat Intelligence  

This automation enables analysts to download all attachments associated with a Cypho issue directly from the platform. The script retrieves attachment metadata from Cypho, securely downloads each available file, and attaches them to the platform incident. This eliminates the need for analysts to manually access Cypho to retrieve evidence, artifacts, or supporting documentation. The automation is designed to streamline investigations by ensuring that all relevant files are readily available within the incident context in platform, improving analysis speed and operational efficiency


## CyphoServerityChange

**Type:** script  
**Product:** Cypho Threat Intelligence  

This automation is triggered when the severity field of a Cypho-related incident is updated in the platform. The script synchronizes the updated severity value with the corresponding issue in Cypho, ensuring that both platforms remain consistent. This allows analysts to manage incident severity directly from platform without performing manual updates in Cypho. The automation is designed to work as a field-change-triggered script and is typically attached to the Cypho Severity incident field. It validates that the incident is properly assigned before executing the update, ensuring accountability and accurate analyst activity tracking


## CyrenCountryLookup

**Type:** script  
**Product:** Cyren Threat InDepth Threat Intelligence  

This script will translate a country code provided by Cyren Threat InDepth to the full country name, based on ISO 3166-1 as defined in pycountry

**Inputs:**

- `value`: the country code provided by Cyren Threat InDepth


## CyrenThreatInDepthRandomHunt

**Type:** script  
**Product:** Cyren Threat InDepth Threat Intelligence  

This script will take a random Cyren Threat InDepth feed indicator and its relationships and create a threat hunting incident for you. The main query parameters for the resulting, internal indicator query are

**Inputs:**

- `indicator_type`: Optional: One of ip_reputation, malware_files, malware_urls, phishing_urls, will determine the Cyren Threat InDepth feed the indicator is ta
- `incident_type`: Optional: If not provided, an incident of type "Hunt" is created


## CyrenThreatInDepthRelatedWidget

**Type:** script  
**Product:** Cyren Threat InDepth Threat Intelligence  

Widget script to view a full set of information about the relationship information the Cyren Threat InDepth feeds offer. For instance, you can see and navigate to a malicious SHA256 that was hosted by a malicious URL. The script can be used similar to the Feed Related Indicators. This script uses the script CyrenThreatInDepthRenderRelated using the following (default) columns


## CyrenThreatInDepthRelatedWidgetQuick

**Type:** script  
**Product:** Cyren Threat InDepth Threat Intelligence  

Widget script to view limited information about the relationship information the Cyren Threat InDepth feeds offer. For instance, you can see and navigate to a SHA256 that was hosted by a malicious URL. The script can be used similar to the Feed Related Indicators. This script uses the script CyrenThreatInDepthRenderRelated using the following columns


## CyrenThreatInDepthRenderRelated

**Type:** script  
**Product:** Cyren Threat InDepth Threat Intelligence  

Widget script to view information about the relationship information the Cyren Threat InDepth feeds offer. For instance, you can see and navigate to a malicious SHA256 that was hosted by a malicious URL. The script provides base functionality for other scripts that are supposed to be used similar to the Feed Related Indicators

**Inputs:**

- `indicator`: JSON representation of the indicator holding the relationship data.
- `columns`: Optional Comma-separated column list (for instance Value,Indicator Type). If not provided, the full list of supported columns is assumed.


## Cyware Intel Exchange

**Type:** integration  
**Product:** Cyware Intel Exchange  

The Cyware Intel Exchange integration allows users to fetch threat intelligence incidents and indicators, enrich IP, domain, URL, and file data, manage tags and notes, perform vulnerability lookups, and run generic API requests. The integration was tested with Cyware Intel Exchange version 3.x

**Commands:**

- `ctix-create-tag`: Create a new tag in the Cyware Intel Exchange platform
- `ctix-get-tags`: Get a paginated list of tags.
- `ctix-disable-or-enable-tags`: Enable or disable tags in the Cyware Intel Exchange platform.
- `ctix-allowed-iocs`: Add a list of same type IOCs to the allowed list.
- `ctix-get-allowed-iocs`: Get a paginated list of allowed IOCs.
- `ctix-remove-allowed-ioc`: Removes an allowed IOC using the specified ID.
- `ctix-get-threat-data`: Command for querying and listing threat data.
- `ctix-get-saved-searches`: List saved searches with pagination.
- `ctix-get-server-collections`: List source collections with pagination.
- `ctix-get-actions`: List enrichment tools.
- `ctix-add-indicator-as-false-positive`: Marks indicators as false positive in bulk.
- `ctix-ioc-manual-review`: Add IOCs to manual review in bulk.
- `ctix-deprecate-ioc`: Deprecates IOCs in bulk
- `ctix-add-analyst-tlp`: Add analyst TLP
- `ctix-add-analyst-score`: Add analyst score for threat data.


## Darkfeed IOC detonation and proactive blocking

**Type:** playbook  
**Product:** Sixgill Darkfeed - Annual Subscription  
**Inputs:**

- `File`: File hash (MD5, SHA-1, SHA-256) from Darkfeed
- `Indicator Query`: Indicators matching the indicator query will be used as playbook input
- `URL`: URL from Darkfeed_010 - Malware available for download from the deep and dark web
- `Manual download`: Set "true" if analyst can manually download malware from deep and dark web filesharing site.
- `VTdownload`: Set "true" if you would like to automatically download file from Virustotal API.
- `AutomatedIndicatorBlocking`: Set "true" if you would like to automatically block discovered malicious indicators.


## Detonate File - FireEye Detection on Demand

**Type:** playbook  
**Product:** FireEye Detection on Demand  

Detonate one or more files using the FireEye Detection on Demand integration. This playbook returns relevant reports to the War Room and file reputations to the context data

**Inputs:**

- `File`: File object of the file to detonate
- `Interval`: Polling frequency - how often the polling command should run (minutes)
- `Timeout`: How much time to wait before a timeout occurs (minutes)


## Detonate File - ThreatStream

**Type:** playbook  
**Product:** Anomali ThreatStream  

Detonates one or more files using the Anomali ThreatStream v2 integration. This playbook returns relevant reports to the War Room, and file reputations to the context data

**Inputs:**

- `File`: The file object of the file to detonate.
- `VM`: The VM to use (string).
- `SubmissionClassification`: The classification of the sandbox submission.
- `PremiumSandbox`: Specifies if the premium sandbox should be used for detonation.
- `Tags`: A CSV list of tags applied to this sample.
- `Interval`: The polling frequency. How often the polling command should run (in minutes).
- `Timeout`: The amount of time to wait before a timeout occurs (in minutes).


## Detonate Remote File from URL - McAfee ATD

**Type:** playbook  
**Product:** McAfee Advanced Threat Defense  

Detonates a File from a URL using the McAfee Advanced Threat Defense sandbox integration

**Inputs:**

- `URL`: URL to detonate.
- `Interval`: Polling frequency - how often the polling command should run (minutes)
- `Timeout`: How much time to wait before a timeout occurs (minutes)


## Detonate URL - McAfee ATD

**Type:** playbook  
**Product:** McAfee Advanced Threat Defense  

Detonates a URL using the McAfee Advanced Threat Defense Sandbox integration

**Inputs:**

- `URL`: The URL to detonate.
- `Interval`: The polling frequency. How often the polling command should run (in minutes).
- `Timeout`: How much time to wait before a timeout occurs (in minutes).


## Detonate URL - ThreatStream

**Type:** playbook  
**Product:** Anomali ThreatStream  

Detonates one or more URLs using the Anomali ThreatStream sandbox integration. Returns relevant reports to the War Room and URL reputations to the context data

**Inputs:**

- `URL`: URL to detonate.
- `Interval`: How often to execute polling (in minutes).
- `Timeout`: The duration after which to stop polling and to resume the playbook (in minutes).
- `VM`: The VM to use (string)
- `SubmissionClassification`: Classification of the sandbox submission.
- `PremiumSandbox`: Specifies if the premium sandbox should be used for detonation.
- `Tags`: A CSV list of tags applied to this sample.


## Digital Shadows

**Type:** integration  
**Product:** ReliaQuest Digital Risk Protection  

Digital Shadows monitors and manages an organization's digital risk across the widest range of data sources within the open, deep, and dark web

**Commands:**

- `ds-get-breach-reviews`: Retrieve all review updates for a given data breach record
- `ds-snapshot-breach-status`: Snapshot the review status of a data breach record
- `ds-find-breach-records`: Find data breach records
- `ds-get-breach-summary`: Summary of all data breaches for the current client
- `ds-find-breach-usernames`: Find unique usernames found across all data breaches
- `ds-get-breach`: Retrieve a data breach by its id
- `ds-get-breach-records`: Find data breach records
- `ds-find-data-breaches`: Find data breaches
- `ds-get-incident`: Retrieve an incident by its id
- `ds-get-incident-reviews`: Retrieve all review updates for a given incident
- `ds-snapshot-incident-review`: Snapshot the review status of an incident
- `ds-find-incidents-filtered`: Find incidents with filtering options
- `ds-get-incidents-summary`: Aggregated summary of incident information used to generate reports/statistics
- `ds-get-apt-report`: Retrieve details of the specified APT report
- `ds-get-intelligence-incident`: Retrieve an intelligence incident by its id


## Digital Shadows - Domain Alert Intelligence (Automated)

**Type:** playbook  
**Product:** ReliaQuest Digital Risk Protection  

Provides intelligence and reputation outputs based on the most recent Impersonating Domain, Subdomain or Phishing URL reported by Digital Shadows SearchLight

**Inputs:**

- `Phishing Attempt Incident ID`: The ID of a Phishing Attempt incident raised by Digital Shadows SearchLight


## Domain Enrichment - Infoblox Cloud

**Type:** playbook  
**Product:** Infoblox Threat Defense with DDI  

This playbook enriches domains or hosts with the dossier, TIDE and asset data using Infoblox Threat Defense with DDI integration

**Inputs:**

- `domains`: The optional comma-separated list of domains or hosts to enrich.


## Domain Enrichment - RST Threat Feed

**Type:** playbook  
**Product:** RST Threat Feed  

Enrich domains using RST Threat Feed integration

**Inputs:**

- `Domain`: The domain name to enrich.
- `threshold`: Defines the minimum score to set indicators as malicious


## DsSearchQueryArray

**Type:** script  
**Product:** ReliaQuest Digital Risk Protection  

Combines an array of queries to as few as possible whilst staying under the maximum term count

**Inputs:**

- `field`: Input field to extract data from for e.g. IP.Address


## EclecticIQ Intelligence Center v3

**Type:** integration  
**Product:** EclecticIQ Platform  

Threat Intelligence Platform that connects and interprets intelligence data from open sources, commercial suppliers and industry partnerships . This integration was integrated and tested with version 2.14 and 3.0 of EclecticIQ Intelligence Center v3. Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `ip`: Get reputation of IP address observable.
- `url`: Gets the reputation of a URL observable.
- `file`: Gets the reputation of a file hash observable.
- `eclecticiq-get-entity`: Query EIC for entity.
- `email`: Gets the reputation of an email address observable.
- `domain`: Gets the reputation of a domain observable.
- `eclecticiq-create-sighting`: Create a sighting entity on EIC. Must contain at least one observable.
- `eclecticiq-create-indicator`: Create an indicator entity on EIC. Must contain at least one observable.
- `eclecticiq-get-entity-by-id`: Query EclecticIQ Intelligence Center for entity by its ID.
- `eclecticiq-request-get`: Make HTTP GET request to EclecticIQ Intelligence Center.
- `eclecticiq-request-post`: Make HTTP POST request to EclecticIQ Intelligence Center.
- `eclecticiq-request-put`: Make HTTP PUT request to EclecticIQ Intelligence Center.
- `eclecticiq-request-patch`: Make HTTP PATCH request to EclecticIQ Intelligence Center.
- `eclecticiq-request-delete`: Make HTTP DELETE request to EclecticIQ Intelligence Center.
- `eclecticiq-get-indicators`: Get last block of Indicators from configured to fetch Outgoing feed.


## Email Collection by Enriched Domain - Google Threat Intelligence

**Type:** playbook  
**Product:** GoogleThreatIntelligence  

This playbook accepts a domain as input, filters the email list to identify addresses containing the specified domain, and outputs the extracted email addresses for further processing

**Inputs:**

- `domain`: Provide the enriched domain using the domain reputation command.


## EntryWidgetCoAHandled

**Type:** script  
**Product:** MITRE ATT&CK - Courses of Action  

Entry widget that shows the number of techniques that were already handled by the CoA playbooks


## EntryWidgetCoATechniquesList

**Type:** script  
**Product:** MITRE ATT&CK - Courses of Action  

Entry widget that shows the number of techniques that were not yet handled by the CoA playbooks


## Extract and Create Relationships

**Type:** playbook  
**Product:** RSS Feed  

Extract and enrich indicators from report raw content

**Inputs:**

- `raw_content`: The raw content of an article
- `indicator_value`: Report indicator value


## FeedCyCognitoGetAssetEndpoint

**Type:** script  
**Product:** CyCognito Feed  

Generates a deep link to the CyCognito platform using the indicator context


## FeedDomainTools

**Type:** integration  
**Product:** DomainTools Feed  

Real-Time Threat Intelligence Feeds provide data on the different stages of the domain lifecycle: from first-observed in the wild, to newly re-activated after a period of quiet. Newly Active Domains surfaces apex-level domains seen for the first time or after ten or more days of inactivity. Newly Observed Domains surfaces domains that we observe for the first time

**Commands:**

- `domaintools-get-indicators`: Gets indicators from the feed.


## Fighting Ursa Luring Targets With Car For Sale

**Type:** playbook  
**Product:** Unit42 Threat Brief - Fighting Ursa  

A Russian threat actor we track as Fighting Ursa advertised a car for sale as a lure to distribute HeadLace backdoor malware. The campaign likely targeted diplomats and began as early as March 2024. Fighting Ursa (aka APT28, Fancy Bear and Sofacy) has been associated with Russian military intelligence and classified as an advanced persistent threat (APT). Diplomatic-car-for-sale phishing lure themes have been used by Russian threat actors for years. These lures tend to resonate with diplomats and get targets to click on the malicious content. Unit 42 has previously observed other threat groups using this tactic. For example, in 2023, a different Russian threat group, Cloaked Ursa, repurposed an advertisement for a BMW for sale to target diplomatic missions within Ukraine. This campaign is not directly connected to the Fighting Ursa campaign described here. However, the similarity in tactics points to known behaviors of Fighting Ursa. The Fighting Ursa group is known for repurposing successful tactics – even continuously exploiting known vulnerabilities for 20 months after their cover was already blown. The details of the March 2024 campaign, which we attribute to Fighting Ursa with a medium to high level of confidence, indicate the group targeted diplomats and relied on public and free services to host various stages of the attack. This article examines the infection chain from the attack. Palo Alto Networks customers are better protected from the threats discussed in this ar

**Inputs:**

- `PlaybookDescription`: The playbook description to be used in the Rapid Breach Response - Set Incident Info sub-playbook.
- `autoBlockIndicators`: Whether to block the indicators automatically.


## File Enrichment - RST Threat Feed

**Type:** playbook  
**Product:** RST Threat Feed  

Enrich File hashes using RST Threat Feed integrations

**Inputs:**

- `File`: The Files to enrich.
- `threshold`: Defines the minimum score to set indicators as malicious


## FireEye Detection on Demand

**Type:** integration  
**Product:** FireEye Detection on Demand  

FireEye Detection On Demand is a threat detection service delivered as an API for integration into the SOC workflow, SIEM analytics, data repositories, or web applications, etc. It delivers flexible file and content analysis to identify malicious behavior wherever the enterprise needs it. This integration was integrated and tested with version 1.4.1 of FireEye Detection on Demand

**Commands:**

- `fireeye-dod-get-hashes`: Queries FireEye Detection on Demand reports for the provided md5 hashes
- `fireeye-dod-submit-file`: Submits file to FireEye Detection on Demand for analysis
- `fireeye-dod-submit-urls`: Submits URLs to FireEye Detection on Demand for analysis
- `fireeye-dod-get-reports`: Retrieves one or more reports of file scans
- `fireeye-dod-get-report-url`: Generates a pre-signed URL for a report


## Get Email From Email Gateway - Proofpoint Protection Server

**Type:** playbook  
**Product:** Proofpoint Protection Server  

This playbook retrieves a specified EML/MSG file directly from the Proofpoint Protection Server

**Inputs:**

- `MessageID`: The Proofpoint message GUID.


## GIBDRPCreateViolationIndicator

**Type:** script  
**Product:** Group-IB Digital Risk Protection  

Creates the indicator of a Group-IB DRP violation from its incident. The Group-IB Digital Risk Protection - Violation Incident Postprocessing playbook runs it on a new incident whose GIB DRP Indicator Wanted field is set, which the fetch sets for the violation types selected in Create indicators from Violations on the instance. The script creates the indicator with createNewIndicator and links it to the incident (relatedIncidents). It sets Group-IB Digital Risk Protection as its source, the violation's first detection and current status date as first and last seen, the violation title as description, and the violation type and brand as tags. The verdict follows the violation type: Counterfeit, Scam, Malware and Phishing are Malicious; Partner policy compliance, Piracy and Trademark are Suspicious; No violation is Benign. An unknown type is Suspicious. Only an http or https URL, a domain or an IPv4 address becomes an indicator. DRP writes many URIs without a scheme: //bad.example/login is read as an https URL and bad.example as a domain. A URI with any other scheme (mail://, tg://), a marketplace seller id or a messenger handle creates no indicator; the automation says so and ends without error. When the violation is over (resolved, handed to legal, found false or rejected), the GIBDRPIncidentUpdate pre-processing rule and the GIBDRPResolveViolation automation expire the indicator if GIB DRP Expire Indicator On Close is set on the incident, which the fetch sets from the instan

**Inputs:**

- `value`: The violation URI to create the indicator from. Defaults to the incident's GIB DRP Violation URI field.


## GIBDRPIncidentUpdate

**Type:** script  
**Product:** Group-IB Digital Risk Protection  

Updates the existing incident of a Group-IB DRP violation in place instead of creating a duplicate, and closes it once the work on the violation is over. Run as the action of the GIB DRP Rule All Types pre-processing rule, it takes the incoming Group-IB DRP violation and, for every incident that already carries the same GIB DRP ID: The fetch passes every change of a violation it created an incident for through to this rule, whatever the instance's status and approval filters say, so the close arrives here as an ordinary update. The incoming incident is then dropped, so an updated violation never becomes a second incident. It is kept only when no existing incident matched, or when every update failed, so a new violation state is never silently lost. The search deliberately covers closed incidents too, and never writes status or severity back. A violation whose incident was already closed is updated in place instead of coming back as a new incident, and a closed incident is not reopened by the update. The severity set by the instance that created the incident - or raised by an analyst since - survives an update that arrives through another instance. The rule that runs this script must carry the script's scriptID, not only its scriptName. the platform; with the name alone the rule matches the incoming incident and then lets it through untouched, so every re-fetch of a violation becomes a new incident. The search sees an incide


## GIBDRPResolveViolation

**Type:** script  
**Product:** Group-IB Digital Risk Protection  

Approves or rejects a Group-IB DRP violation. This sits behind the Approve Violation and Reject Violation buttons on the GIB DRP Violation layout, and behind the approve/reject tasks of the Group-IB Digital Risk Protection - Violation Incident Postprocessing playbook. The decision goes to the instance that fetched the incident. Without using, the platform, and with several instances (one per brand, section or severity) the instances that do not own the violation answer with an error and the button fails. The using argument wins; then the incident's sourceInstance, when that instance is still active; then the only active instance. Approving does not close the incident by default. It settles the customer's half of the case; the take-down continues in Group-IB DRP afterwards, and the incident is closed later by the GIBDRPIncidentUpdate pre-processing rule, once DRP reports the violation as resolved (taken down; solved on older API versions) or legal (handed to legal). With Close the incident when a violation is approved enabled on the instance, gibdrp-change-violation-status answers with closeIncident: true and the automation closes the incident as Resolved at once. Rejecting always closes the incident as False Positive: DRP does nothing more with a rejected violation, so nothing later would close the incident. When GIB DRP Expire Indicator On Close is set on the incident (from the instance's Expire

**Inputs:**

- `status`: Whether to approve or reject the violation. Possible values are: approve, reject.
- `id`: The Group-IB DRP violation ID. Defaults to the incident's GIB DRP ID field.
- `using`: The name of the Group-IB Digital Risk Protection integration instance to use. Defaults to the instance that fetched the incident, or to the 


## GIBIncidentUpdate

**Type:** script  
**Product:** Group-IB Threat Intelligence  

This script prevents duplication of existing incidents


## GIBIncidentUpdateAllTypes

**Type:** script  
**Product:** Group-IB Threat Intelligence  

This script prevents duplication of existing incidents


## GIBIncidentUpdateIncludingClosed

**Type:** script  
**Product:** Group-IB Threat Intelligence  

This script prevents duplication of existing incidents


## Gigamon ThreatINSIGHT

**Type:** integration  
**Product:** Gigamon ThreatINSIGHT  
**Commands:**

- `insight-get-sensors`: Get a list of all sensors.
- `insight-get-devices`: Get a list of all devices.
- `insight-get-tasks`: Get a list of all the PCAP tasks.
- `insight-create-task`: Create a new PCAP task.
- `insight-get-telemetry-events`: Get event telemetry data grouped by time.
- `insight-get-telemetry-packetstats`: Get packetstats telemetry data grouped by time.
- `insight-get-telemetry-network`: Get network telemetry data grouped by time
- `insight-get-entity-summary`: Get summary information about an IP or domain.
- `insight-get-entity-pdns`: Get passive DNS information about an IP or domain.
- `insight-get-entity-dhcp`: Get DHCP information about an IP address.
- `insight-get-entity-file`: Get information about a file.
- `insight-get-detections`: Get a list of detections.
- `insight-get-detection-rules`: Get a list of detection rules.
- `insight-resolve-detection`: Resolve a specific detection.
- `insight-get-detection-rule-events`: Get a list of the events that matched on a specific rule.


## Google Threat Intelligence

**Type:** integration  
**Product:** GoogleThreatIntelligence  

This integration analyzes suspicious hashes, URLs, domains, and IP addresses

**Commands:**

- `ip`: Checks the reputation of an IP address.
- `url`: Checks the reputation of a URL.
- `domain\`: Checks the reputation of a domain.
- `cve`: Retrieves CVE information from Google Threat Intelligence.
- `url-scan`: Scans a specified URL. Use the gti-analysis-get command to get the scan results.
- `gti-comments-add`: Adds comments to files and URLs.
- `gti-file-scan-upload-url`: Premium API. Get a special URL for files larger than 32 MB.
- `gti-comments-delete`: Delete a comment.
- `gti-comments-get`: Retrieves comments for a given resource.
- `gti-comments-get-by-id`: Retrieves a comment by comment ID.
- `gti-search`: Search for an indicator in GoogleThreatIntelligence.
- `gti-file-sandbox-report`: Retrieves a behavioral relationship of the given file hash.
- `gti-passive-dns-data`: Returns passive DNS records by indicator.
- `gti-analysis-get`: Retrieves resolutions of the given IP.
- `gti-file-sigma-analysis`: Retrieves result of the last Sigma analysis.


## Google Threat Intelligence - ASM Issues

**Type:** integration  
**Product:** GoogleThreatIntelligence  

This integration allows the creation of incidents based on ASM Issues from Google Threat Intelligence

**Commands:**

- `gti-asm-issue-list`: Search the ASM Issues with provided filter arguments.
- `gti-asm-issue-get`: Get a particular ASM Issue by ID.
- `gti-asm-issue-status-update`: Update the status of an ASM Issue.


## Google Threat Intelligence - DTM Alerts

**Type:** integration  
**Product:** GoogleThreatIntelligence  

This integration allows the creation of incidents based on DTM Alerts from Google Threat Intelligence

**Commands:**

- `gti-dtm-alert-list`: Search the DTM Alerts with provided filter arguments.
- `gti-dtm-alert-get`: Get a particular DTM Alert by ID.
- `gti-dtm-alert-status-update`: Update the status of DTM alert.


## Google Threat Intelligence - Relevance System Alerts

**Type:** integration  
**Product:** GoogleThreatIntelligence  

This integration allows the creation of incidents based on RS Alerts from Google Threat Intelligence

**Commands:**

- `gti-rs-alert-list`: List the RS Alerts with provided filter arguments.
- `gti-rs-alert-get`: Get a particular RS Alert by ID.
- `gti-rs-alert-status-update`: Update the status of an RS Alert.


## Group-IB Digital Risk Protection

**Type:** integration  
**Product:** Group-IB Digital Risk Protection  

Pack helps to integrate Group-IB Digital Risk Protection and get violations incidents directly into the platform. This integration was integrated and tested with version 1.0 of Group-IB Digital Risk Protection

**Commands:**

- `gibdrp-get-brands`: Receive all configured brands.
- `gibdrp-get-subscriptions`: Receive all configured subscriptions.
- `gibdrp-get-violation-by-id`: Getting a single violation by its ID.
- `gibdrp-change-violation-status`: Approves or rejects a single violation pending customer review (approveState under_review). Reports whether the instance wants the incident closed after an appr
- `gibdrp-create-violation`: Creates one or more violations in the Group-IB DRP portal. Fails with an error entry if the DRP API rejects every submitted item; a partial success reports both


## Group-IB Threat Intelligence

**Type:** integration  
**Product:** Group-IB Threat Intelligence  

Pack helps to integrate Group-IB Threat Intelligence and get incidents directly into the platform. The integration supports multiple collections including compromised accounts, bank cards, breaches, malware, attacks, OSI leaks, vulnerabilities, and threat intelligence. See the Data Collections Overview section below for the complete list with descriptions and recommended date ranges

**Commands:**

- `gibti-get-compromised-account-info`: Command performs Group-IB event lookup in compromised/account collection with provided ID.
- `gibti-get-compromised-breached-info`: Command performs Group-IB event lookup in compromised/breached collection with provided ID.
- `gibti-get-compromised-mule-info`: Command performs Group-IB event lookup in compromised/mule collection with provided ID.
- `gibti-get-compromised-spd-info`: Command performs Group-IB event lookup in compromised/spd (suspicious payment details) collection with provided ID. Returns payment-related observables (e.g. cr
- `gibti-get-osi-git-leak-info`: Command performs Group-IB event lookup in osi/git_leak collection with provided ID.
- `gibti-get-osi-public-leak-info`: Command performs Group-IB event lookup in osi/public_leak collection with provided ID.
- `gibti-get-osi-vulnerability-info`: Command performs Group-IB event lookup in osi/vulnerability collection with provided ID.
- `gibti-get-attacks-ddos-info`: Command performs Group-IB event lookup in attacks/ddos collection with provided ID.
- `gibti-get-attacks-deface-info`: Command performs Group-IB event lookup in attacks/deface collection with provided ID.
- `gibti-get-phishing-kit-info`: Command performs Group-IB event lookup in attacks/phishing_kit collection with provided ID.
- `gibti-get-threat-info`: Command performs Group-IB event lookup in hi/threat (or in apt/threat if the APT flag is true) collection with provided ID.
- `gibti-get-threat-actor-info`: Command performs Group-IB event lookup in hi/threat_actor (or in apt/threat_actor if the APT flag is true) collection with provided ID.
- `gibti-get-suspicious-ip-tor-node-info`: Command performs Group-IB event lookup in suspicious_ip/tor_node collection with provided ID.
- `gibti-get-suspicious-ip-open-proxy-info`: Command performs Group-IB event lookup in suspicious_ip/open_proxy collection with provided ID.
- `gibti-get-suspicious-ip-socks-proxy-info`: Command performs Group-IB event lookup in suspicious_ip/socks_proxy collection with provided ID.


## Handle TD events

**Type:** playbook  
**Product:** NTT Cyber Threat Sensor  

Playbook to enrich TD events


## Haseen - Delta Feed - Generic

**Type:** playbook  
**Product:** HaseenThreatIntel  

## iManage Threat Manager

**Type:** integration  
**Product:** iManage Threat Manager  

This integration fetches alerts from iManage Threat Manager, an AI-driven security solution that uses machine learning to detect unusual user behavior, prevent data loss, and ensure compliance. This is the default integration for this content pack when configured by the Data Onboarder in Cortex

**Commands:**

- `imanage-threat-manager-get-events`: Fetches events from iManage Threat Manager. This manual command is used for developing or debugging and should be used with caution, as it can create events, le


## Indicator Enrichment - Infoblox Cloud

**Type:** playbook  
**Product:** Infoblox Threat Defense with DDI  

This playbook enriches IP addresses, MAC addresses, domains and URLs with the dossier, DHCP lease, TIDE and asset data using Infoblox Threat Defense with DDI integration

**Inputs:**

- `ip_addresses`: The optional comma-separated list of IP addresses to enrich.
- `domains`: The optional comma-separated list of domains or hosts to enrich.
- `urls`: The optional comma-separated list of URLs to enrich.
- `mac_addresses`: The optional comma-separated list of MAC addresses to enrich.


## Indicator Enrichment - Qintel

**Type:** playbook  
**Product:** Qintel  

Enriches indicators from Qintel products

**Inputs:**

- `IP`: IPs to be enriched
- `Domain`: Domains to be enriched
- `CVE`: CVEs to be enriched
- `Email`: Email to be enriched


## Infoblox Threat Defense with DDI

**Type:** integration  
**Product:** Infoblox Threat Defense with DDI  

Infoblox Threat Defense with DDI integration leverages DNS as the first line of defense to detect and block cyber threats, while also using threat intelligence to manage IQ for TD Insight incident response and enrich indicators. This integration was integrated and tested with version 1.0.0 of Infoblox Threat Defense with DDI

**Commands:**

- `bloxone-td-dossier-lookup-get`: The Dossier Lookup API returns detailed information on the specified indicator from the requested sources.
- `bloxone-td-dossier-source-list`: Get available Dossier sources.
- `bloxone-td-lookalike-domain-list`: Get lookalike domain lists.
- `infobloxcloud-block-ip`: The given IP addresses will be added to the provided block list.
- `infobloxcloud-unblock-ip`: The given IP addresses will be added to the provided allow list.
- `infobloxcloud-block-domain`: The given domains will be added to the provided block list.
- `infobloxcloud-unblock-domain`: The given domains will be added to the provided allow list.
- `infobloxcloud-customlist-indicator-remove`: The given indicators will be removed from the provided custom list.
- `ip`: Gets the comprehensive IP reputation and threat intelligence from Infoblox Threat Defense, including threat indicators, IPAM address information, and standard I


## Intel471 Credentials

**Type:** integration  
**Product:** Intel471 Feed  

Fetches leaked credentials from the Intel471 Credentials API (/credentials/stream). The primary command is fetch-indicators: each credential is converted into one Cortex indicator (Email if the login contains @, otherwise Account). While iterating the indicator-creation loop, the integration also creates an associated Cortex incident for the same credential and links it back via the indicator's relatedIncidents field

**Commands:**

- `intel471-credentials-get-indicators`: Gets a preview of indicators that the feed would pull on the next run (no state is persisted).


## IP Enrichment - External - RST Threat Feed

**Type:** playbook  
**Product:** RST Threat Feed  

Enrich IP addresses using one or more integrations

**Inputs:**

- `IP`: The IP address to enrich.
- `InternalRange`: A CSV list of IP address ranges (in CIDR notation). Use this list to check if an IP address is found within a set of IP address ranges. For 
- `ResolveIP`: Whether to convert the IP address to a hostname using a DNS query (True/False).
- `threshold`: Defines the minimum score to set indicators as malicious


## IP Enrichment - Infoblox Cloud

**Type:** playbook  
**Product:** Infoblox Threat Defense with DDI  

This playbook enriches IP addresses with the dossier, TIDE and asset data using Infoblox Threat Defense with DDI integration

**Inputs:**

- `ip_addresses`: The optional comma-separated list of IP addresses to enrich.


## IPQualityScore

**Type:** integration  
**Product:** IPQualityScore (IPQS) Threat Risk Scoring  
**Commands:**

- `ipqs-ip-reputation`: Runs reputation on IPs.
- `ip`: Deprecated. Use ipqs-ip-reputation instead.
- `ipqs-email-reputation`: Runs reputation on email addresses.
- `email`: Deprecated. Use ipqs-email-reputation instead.
- `ipqs-url-reputation`: Runs reputation on URLs.
- `url`: Deprecated. Use ipqs-url-reputation instead.
- `ipqs-phone-reputation`: Runs validation and reputation on phone numbers.
- `ipqs-username-leaked`: Checks if a username has been exposed in known data breaches.
- `ipqs-password-leaked`: Checks if a password has been exposed in known data breaches.
- `ipqs-email-leaked`: Checks if an email address has been exposed in known data breaches.
- `ipqs-file-scan`: Uploads a file and scans it using the IPQualityScore Malware File Scanner API. First attempts a cached lookup by file hash; if not cached, the file is submitted
- `ipqs-url-file-scan`: Submits a URL to the IPQualityScore Malware File Scanner API. First attempts a cached lookup; if not cached, the URL is submitted for scanning. Polls for result


## Malwarebytes

**Type:** integration  
**Product:** ThreatDown  
**Commands:**

- `malwarebytes-scan-and-remediate`: Initiate Scan and Remediate action on an endpoint based on IP or Hostname.
- `malwarebytes-scan-and-report`: Initiate Scan and report action on an endpoint based on IP or Hostname.
- `malwarebytes-isolate-endpoint`: Initiate Isolation action on an endpoint based on IP or Hostname. This action isolate an endpoint by Process, Network and Desktop.
- `malwarebytes-isolate-process`: Initiate Process Isolation action on an endpoint based on IP or Hostname.
- `malwarebytes-isolate-desktop`: Initiate Desktop Isolation action on an endpoint based on IP or Hostname.
- `malwarebytes-isolate-network`: Initiate Network Isolation action on an endpoint based on IP or Hostname.
- `malwarebytes-deisolate-endpoint`: Initiate Deisolation action on an endpoint based on IP or Hostname. This action deisolate an endpoint by Process, Network and Desktop.
- `malwarebytes-list-endpoints`: List all/online/offline endpoints available in the Malwarebytes Cloud.
- `malwarebytes-list-endpoint-info`: Lists more granular information about an endpoint.
- `malwarebytes-get-scan-detections`: Lists detections from an endpoint for the scans initiated from the platform.
- `malwarebytes-get-job-status`: Lists scan/isolation/deisolation status of the endpoint for the scan/isolation/deisolation initated from the platform.
- `malwarebytes-open-sa-incident`: Open Suspicious Activity for investigation in Malwarebytes Cloud. Use malwarebytes-get-sa-activities command to get machine and detection ID.
- `malwarebytes-remediate-sa-incident`: Remediate Suspicious Activity from Malwarebytes Cloud. Use malwarebytes-get-sa-activities command to get machine and detection ID.
- `malwarebytes-close-sa-incident`: Close Suspicious Activity Incident in Malwarebytes Cloud. Use malwarebytes-get-sa-activities command to get machine and detection ID.
- `malwarebytes-get-sa-activities`: Lists all suspicious activities from hostname value and list all the hostnames from path of file.


## Mandiant Advantage Threat Intelligence

**Type:** integration  
**Product:** Mandiant Advantage Threat Intelligence  

Enrich Indicators of Compromise, and fetch information about Actors, Malware Families, and Campaigns from Mandiant Advantage. This integration was integrated and tested with version 4 of the Mandiant Advantage Threat Intelligence API

**Commands:**

- `mati-get-indicator`: Get information about a single Indicator of Compromise from Mandiant
- `mati-get-actor`: Get information about a Threat Actor from Mandiant
- `mati-get-malware`: Get information about a Malware Family from Mandiant
- `file`: Retrieve information about a File Hash from Mandiant
- `ip`: Retrieve information about an IP Address from Mandiant
- `url`: Retrieve information about a URL from Mandiant
- `domain`: Retrieve information about an FQDN from Mandiant
- `cve`: Retrieve information about a Vulnerability (by CVE) from Mandiant
- `mati-get-campaign`: Retrieve information about a Campaign from Mandiant


## Mandiant Enrich

**Type:** integration  
**Product:** Mandiant Advantage Threat Intelligence  

Enrich Indicators of Compromise using the platform, and create indicators for Threat Actors, Malware Families, and Campaigns from Mandiant Advantage

**Commands:**

- `file`: Get information about a file hash from Mandiant.
- `ip`: Get information about an IP address from Mandiant.
- `url`: Get information about a URL from Mandiant.
- `domain`: Get information about a domain from Mandiant.
- `cve`: Get information about a CVE from Mandiant.
- `mati-get-actor`: Get information about a Threat Actor from Mandiant.
- `mati-get-malware`: Get information about a Malware Family from Mandiant.
- `mati-get-campaign`: Retrieve information about a Campaign from Mandiant.


## MAR - Endpoint data collection

**Type:** playbook  
**Product:** McAfee Active Response  

Use McAfee Active Response to collect data from an endpoint for IR purposes (requires ePO as well). Input

**Inputs:**

- `Hostname`: Hostname to run on.


## McAfee Threat Intelligence Exchange v2

**Type:** integration  
**Product:** McAfee Threat Intelligence Exchange  

Use the McAfee Threat Intelligence Exchange (TIE) integration to get file reputations and the systems that reference the files. Connect to McAfee TIE using the McAfee DXL client. This integration was integrated and tested with version 2.0 of McAfee Threat Intelligence Exchange V2 Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `file`: Retrieves the reputations for the specified hashes. Can be "MD5", "SHA1", or "SHA256".
- `tie-set-file-reputation`: Sets the “Enterprise” reputation (trust level, filename, and comment) of the specified hashes. Hashes that represent the same file can have a different "Enterpr
- `tie-file-references`: Retrieves the set of systems which have referenced (typically executed) the specified hashes.


## MITRE ATT&CK - Courses of Action

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This is the parent playbook, which contains all phases and remediates MITRE ATT&CK techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. The playbook utilizes several other MITRE ATT&CK remediation playbooks. The playbook follows the MITRE ATT&CK kill chain phases and takes action to protect the organization from the inputted techniques, displaying and implementing security policy recommendations for Palo Alto Networks products. ***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Possible playbook triggers

**Inputs:**

- `TechniquesList`: MITRE ATT&amp;CK ID of a technique, or comma-separated list of techniques IDs.
- `template`: Template name to enforce WildFire best practices profile.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## MITRE ATT&CK - Courses of Action Trigger Job

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This is a wrapper playbook for the "MITRE ATT&CK - Courses of Action" use-case. Possible playbook triggers: Once triggered, the playbook will create a new incident from type "MITRE ATT&CK CoA". The incident will trigger the playbook "MITRE ATT&CK - Courses of Action", which contains all phases and remediates MITRE ATT&CK techniques using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified techniques, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs)

**Inputs:**

- `techniqueByIncident`: MITRE ATT&amp;CK ID of a technique, or comma-separated list of techniques IDs.
- `Indicator Query`: Define a query that will retrieve indicators that contain MITRE ATT&amp;CK techniques under the "Feed Related Indicators" field.(Possible qu
- `template`: Template name to enforce WildFire best practices profile.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.
- `query_type`: The type of the indicator query this playbook is running. Possible values can be:Direct - The playbook query returns a list of "STIX ATT&amp


## MITRE ATT&CK CoA - T1003 - OS Credential Dumping

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the OS Credential Dumping technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may attempt to dump credentials to obtain account login and credential material, normally in the form of a hash or a clear text password, from the operating system and software. Credentials can then be used to perform Lateral Movement and to access restricted information. Possible playbook uses


## MITRE ATT&CK CoA - T1005 - Data from Local System

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Data from Local System technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may search local system sources, such as file systems or local databases, to find files of interest and sensitive data prior to Exfiltration. Adversaries may do this using a Command and Scripting Interpreter, such as cmd, which has functionality to interact with the file system to gather information. Some adversaries may also use Automated Collection on the local system. Possible playbook uses


## MITRE ATT&CK CoA - T1021.001 - Remote Desktop Protocol

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Remote Desktop Protocol technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may use Valid Accounts to log into a computer using the Remote Desktop Protocol (RDP). The adversary may then perform actions as the logged-on user. Remote desktop is a common feature in operating systems. It allows a user to log into an interactive session with a system desktop graphical user interface on a remote system. Microsoft refers to its implementation of the Remote Desktop Protocol (RDP) as Remote Desktop Services (RDS). Adversaries may connect to a remote system over RDP/RDS to expand access if the service is enabled and allows access to accounts with known credentials. Adversaries will likely use Credential Access techniques to acquire credentials to use with RDP. Adversaries may also use RDP in conjunction with the Accessibility Features technique for Persistence. Possible playbook uses


## MITRE ATT&CK CoA - T1027 - Obfuscated Files or Information

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Obfuscated Files or Information technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may attempt to make an executable or file difficult to discover or analyze by encrypting, encoding, or otherwise obfuscating its contents on the system or in transit. This is common behavior that can be used across different platforms and the network to evade defenses. Possible playbook uses

**Inputs:**

- `template`: Template name to enforce WildFire best practices profile.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the results.


## MITRE ATT&CK CoA - T1041 - Exfiltration Over C2 Channel

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Exfiltration Over C2 Channel technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may steal data by exfiltrating it over an existing command and control channel. Stolen data is encoded into the normal communications channel using the same protocol as command and control communications. Possible playbook uses

**Inputs:**

- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## MITRE ATT&CK CoA - T1048 - Exfiltration Over Alternative Protocol

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Exfiltration Over Alternative Protocol technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may steal data by exfiltrating it over a different protocol than that of the existing command and control channel. The data may also be sent to an alternate network location from the main command and control server. Alternate protocols include FTP, SMTP, HTTP/S, DNS, SMB, or any other network protocol not being used as the main command and control channel. Different protocol channels could also include Web services such as cloud storage. Adversaries may also opt to encrypt and/or obfuscate these alternate channels. Exfiltration Over Alternative Protocol can be done using various common operating system utilities such as Net/SMB or FTP. Possible playbook uses

**Inputs:**

- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## MITRE ATT&CK CoA - T1057 - Process Discovery

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Process Discovery technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may attempt to get information about running processes on a system. Information obtained could be used to gain an understanding of common software/applications running on systems within the network. Adversaries may use the information from Process Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. Possible playbook uses


## MITRE ATT&CK CoA - T1059 - Command and Scripting Interpreter

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Command and Scripting Interpreter technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may abuse command and script interpreters to execute commands, scripts, or binaries. These interfaces and languages provide ways of interacting with computer systems and are a common feature across many different platforms. Most systems come with some built-in command-line interface and scripting capabilities, for example, macOS and Linux distributions include some flavor of Unix Shell while Windows installations include the Windows Command Shell and PowerShell. There are also cross-platform interpreters such as Python, as well as those commonly associated with client applications such as JavaScript/JScript and Visual Basic. Adversaries may abuse these technologies in various ways as a means of executing arbitrary commands. Commands and scripts can be embedded in Initial Access payloads delivered to victims as lure documents or as secondary payloads downloaded from an existing C2. Adversaries may also execute commands through interactive terminals/shells. Possible playbook uses


## MITRE ATT&CK CoA - T1059.001 - PowerShell

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Command and Scripting Interpreter technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may abuse PowerShell commands and scripts for execution. PowerShell is a powerful interactive command-line interface and scripting environment included in the Windows operating system. [1] Adversaries can use PowerShell to perform a number of actions, including discovery of information and execution of code. Examples include the Start-Process cmdlet which can be used to run an executable and the Invoke-Command cmdlet which runs a command locally or on a remote computer (though administrator permissions are required to use PowerShell to connect to remote systems). PowerShell may also be used to download and run executables from the Internet, which can be executed from disk or in memory without touching disk. Possible playbook uses


## MITRE ATT&CK CoA - T1068 - Exploitation for Privilege Escalation

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Exploitation for Privilege Escalation technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may exploit software vulnerabilities in an attempt to collect elevate privileges. Exploitation of a software vulnerability occurs when an adversary takes advantage of a programming error in a program, service, or within the operating system software or kernel itself to execute adversary-controlled code. Security constructs such as permission levels will often hinder access to information and use of certain techniques, so adversaries will likely need to perform privilege escalation to include use of software exploitation to circumvent those restrictions. When initially gaining access to a system, an adversary may be operating within a lower privileged process which will prevent them from accessing certain resources on the system. Vulnerabilities may exist, usually in operating system components and software commonly running at higher permissions, that can be exploited to gain higher levels of access on the system. This could enable someone to move from unprivileged or user level permissions to SYSTEM or root permi


## MITRE ATT&CK CoA - T1071 - Application Layer Protocol

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Application Layer Protocol technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may communicate using application layer protocols to avoid detection/network filtering by blending in with existing traffic. Commands to the remote system, and often the results of those commands, will be embedded within the protocol traffic between the client and server. Adversaries may utilize many different protocols, including those used for web browsing, transferring files, electronic mail, or DNS. For connections that occur internally within an enclave (such as those between a proxy or pivot node and other nodes), commonly used protocols are SMB, SSH, or RDP. Possible playbook uses

**Inputs:**

- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## MITRE ATT&CK CoA - T1078 - Valid Accounts

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Valid Accounts technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may obtain and abuse credentials of existing accounts as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Compromised credentials may be used to bypass access controls placed on various resources on systems within the network and may even be used for persistent access to remote systems and externally available services, such as VPNs, Outlook Web Access and remote desktop. Compromised credentials may also grant an adversary increased privilege to specific systems or access to restricted areas of the network. Adversaries may choose not to use malware or tools in conjunction with the legitimate access those credentials provide to make it harder to detect their presence. The overlap of permissions for local, domain, and cloud accounts across a network of systems is of concern because the adversary may be able to pivot across accounts and systems to reach a high level of access (i.e., domain or enterprise administrator) to bypass access controls set within the enterprise. Possible playbook uses

**Inputs:**

- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the results.


## MITRE ATT&CK CoA - T1082 - System Information Discovery

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the System Information Discovery technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: An adversary may attempt to get detailed information about the operating system and hardware, including version, patches, hotfixes, service packs, and architecture. Adversaries may use the information from System Information Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. Tools such as Systeminfo can be used to gather detailed system information. A breakdown of system data can also be gathered through the macOS systemsetup command, but it requires administrative privileges. Infrastructure as a Service (IaaS) cloud providers such as AWS, GCP, and Azure allow access to instance and virtual machine information via APIs. Successful authenticated API calls can return data such as the operating system platform and status of a particular instance or the model view of a virtual machine. Possible playbook uses


## MITRE ATT&CK CoA - T1083 - File and Directory Discovery

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the File and Directory Discovery technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may enumerate files and directories or may search in specific locations of a host or network share for certain information within a file system. Adversaries may use the information from File and Directory Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. Many command shell utilities can be used to obtain this information. Examples include dir, tree, ls, find, and locate. Custom tools may also be used to gather file and directory information and interact with the Native API. Possible playbook uses


## MITRE ATT&CK CoA - T1105 - Ingress tool transfer

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Ingress tool transfer technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may transfer tools or other files from an external system into a compromised environment. Files may be copied from an external adversary controlled system through the command and control channel to bring tools into the victim network or through alternate protocols with another tool such as FTP. Files can also be copied over on Mac and Linux with native tools like scp, rsync, and sftp. Possible playbook uses

**Inputs:**

- `template`: Template name to enforce WildFire best practices profile.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## MITRE ATT&CK CoA - T1110 - Brute Force

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Brute Force technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may use brute force techniques to gain access to accounts when passwords are unknown or when password hashes are obtained. Without knowledge of the password for an account or set of accounts, an adversary may systematically guess the password using a repetitive or iterative mechanism. Brute forcing passwords can take place via interaction with a service that will check the validity of those credentials or offline against previously acquired credential data, such as password hashes. Possible playbook uses

**Inputs:**

- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the results.


## MITRE ATT&CK CoA - T1133 - External Remote Services

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the External Remote Services technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may use brute force techniques to gain access to accounts when passwords are unknown or when password hashes are obtained. Without knowledge of the password for an account or set of accounts, an adversary may systematically guess the password using a repetitive or iterative mechanism. Brute forcing passwords can take place via interaction with a service that will check the validity of those credentials or offline against previously acquired credential data, such as password hashes. Possible playbook uses

**Inputs:**

- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the results.


## MITRE ATT&CK CoA - T1135 - Network Share Discovery

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Network Share Discovery technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. File sharing over a Windows network occurs over the SMB protocol. [1][2] Net can be used to query a remote system for available shared drives using the net view \remotesystem command. It can also be used to query shared drives on the local system using net share. Possible playbook uses


## MITRE ATT&CK CoA - T1189 - Drive-by Compromise

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Drive-by Compromise technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may gain access to a system through a user visiting a website over the normal course of browsing. With this technique, the user's web browser is typically targeted for exploitation, but adversaries may also use compromised websites for non-exploitation behavior such as acquiring Application Access Token. Possible playbook uses

**Inputs:**

- `template`: Template name to enforce WildFire best practices profile.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## MITRE ATT&CK CoA - T1199 - Trusted Relationship

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Trusted Relationship technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may breach or otherwise leverage organizations who have access to intended victims. Access through trusted third party relationship exploits an existing connection that may not be protected or receives less scrutiny than standard mechanisms of gaining access to a network. Organizations often grant elevated access to second or third-party external providers in order to allow them to manage internal systems as well as cloud-based environments. Some examples of these relationships include IT services contractors, managed security providers, infrastructure contractors (e.g. HVAC, elevators, physical security). The third-party provider's access may be intended to be limited to the infrastructure being maintained, but may exist on the same network as the rest of the enterprise. As such, Valid Accounts used by the other party for access to internal network systems may be compromised and used. Possible playbook uses


## MITRE ATT&CK CoA - T1204 - User Execution

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the User Execution technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: An adversary may rely upon specific actions by a user in order to gain execution. Users may be subjected to social engineering to get them to execute malicious code by, for example, opening a malicious document file or link. These user actions will typically be observed as follow-on behavior from forms of Phishing. While User Execution frequently occurs shortly after Initial Access it may occur at other phases of an intrusion, such as when an adversary places a file in a shared directory or on a user's desktop hoping that a user will click on it. This activity may also be seen shortly after Internal Spearphishing. Possible playbook uses

**Inputs:**

- `template`: Template name to enforce WildFire best practices profile.
- `template_stack`: The template stack to use when running the command.
- `vsys`: The name of the virtual system to be configured. Will use the configured VSYS parameter if exists. If given a value, will override the VSYS 
- `device-group`: The device group to work on. Exists only in panorama!
- `tag`: Tag for which to filter the results.
- `pre-post-rulebase`: Determines whether the rule is a pre-rulebase or post-rulebase rule, according to the rule structure. Exists only in panorama!


## MITRE ATT&CK CoA - T1486 - Data Encrypted for Impact

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Data Encrypted for Impact technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may encrypt data on target systems or on large numbers of systems in a network to interrupt availability to system and network resources. They can attempt to render stored data inaccessible by encrypting files or data on local and remote drives and withholding access to a decryption key. This may be done in order to extract monetary compensation from a victim in exchange for decryption or a decryption key (ransomware) or to render data permanently inaccessible in cases where the key is not saved or transmitted.[1][2][3][4] In the case of ransomware, it is typical that common user files like Office documents, PDFs, images, videos, audio, text, and source code files will be encrypted. In some cases, adversaries may encrypt critical system files, disk partitions, and the MBR. To maximize impact on the target organization, malware designed for encrypting data may have worm-like features to propagate across a network by leveraging other attack techniques like Valid Accounts, OS Credential Dumping, and SMB/Windows Admin Shares. Po


## MITRE ATT&CK CoA - T1518 - Software Discovery

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Software Discovery technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may attempt to get a listing of software and software versions that are installed on a system or in a cloud environment. Adversaries may use the information from Software Discovery during automated discovery to shape follow-on behaviors, including whether or not the adversary fully infects the target and/or attempts specific actions. Adversaries may attempt to enumerate software for a variety of reasons, such as figuring out what security measures are present or if the compromised system has a version of software that is vulnerable to Exploitation for Privilege Escalation. Possible playbook uses


## MITRE ATT&CK CoA - T1543.003 - Windows Service

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Windows Service technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may create or modify Windows services to repeatedly execute malicious payloads as part of persistence. When Windows boots up, it starts programs or applications called services that perform background system functions.[1] Windows service configuration information, including the file path to the service's executable or recovery programs/commands, is stored in the Windows Registry. Service configurations can be modified using utilities such as sc.exe and Reg. Adversaries may install a new service or modify an existing service by using system utilities to interact with services, by directly modifying the Registry, or by using custom tools to interact with the Windows API. Adversaries may configure services to execute at startup in order to persist on a system. Possible playbook uses


## MITRE ATT&CK CoA - T1547 - Boot or Logon Autostart Execution

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Boot or Logon Autostart Execution technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may configure system settings to automatically execute a program during system boot or logon to maintain persistence or gain higher-level privileges on compromised systems. Operating systems may have mechanisms for automatically running a program on system boot or account logon.[1][2][3][4][5] These mechanisms may include automatically executing programs that are placed in specially designated directories or are referenced by repositories that store configuration information, such as the Windows Registry. An adversary may achieve the same goal by modifying or extending features of the kernel. Since some boot or logon autostart programs run with higher privileges, an adversary may leverage these to elevate privileges. Possible playbook uses


## MITRE ATT&CK CoA - T1547.001 - Registry Run Keys Startup Folder

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Registry Run Keys / Startup Folder technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may achieve persistence by adding a program to a startup folder or referencing it with a Registry run key. Adding an entry to the "run keys" in the Registry or startup folder will cause the program referenced to be executed when a user logs in. [1] These programs will be executed under the context of the user and will have the account's associated permissions level. Placing a program within a startup folder will also cause that program to execute when a user logs in. There is a startup folder location for individual user accounts as well as a system-wide startup folder that will be checked regardless of which user account logs in. The startup folder path for the current user is C:\Users[Username]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup. The startup folder path for all users is C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp. Possible playbook uses


## MITRE ATT&CK CoA - T1560.001 - Archive via Utility

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Data Encrypted technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: An adversary may compress or encrypt data that is collected prior to exfiltration using 3rd party utilities. Many utilities exist that can archive data, including 7-Zip[1], WinRAR[2], and WinZip[3]. Most utilities include functionality to encrypt and/or compress data. Some 3rd party utilities may be preinstalled, such as tar on Linux and macOS or zip on Windows systems. Possible playbook uses


## MITRE ATT&CK CoA - T1562.001 - Disable or Modify Tools

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Disable or Modify Tools technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may disable security tools to avoid possible detection of their tools and activities. This can take the form of killing security software or event logging processes, deleting Registry keys so that tools do not start at run time, or other methods to interfere with security tools scanning or reporting information. Possible playbook uses


## MITRE ATT&CK CoA - T1564.004 - NTFS File Attributes

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the NTFS File Attributes technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may use NTFS file attributes to hide their malicious data in order to evade detection. Every New Technology File System (NTFS) formatted partition contains a Master File Table (MFT) that maintains a record for every file/directory on the partition. [1] Within MFT entries are file attributes, [2] such as Extended Attributes (EA) and Data [known as Alternate Data Streams (ADSs) when more than one Data attribute is present], that can be used to store arbitrary data (and even complete files). Adversaries may store malicious data or binaries in file attribute metadata instead of directly in files. This may be done to evade some defenses, such as static indicator scanning tools and anti-virus. Possible playbook uses

**Inputs:**

- `template`: Template name to enforce WildFire best practices profile.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## MITRE ATT&CK CoA - T1566 - Phishing

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Phishing technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may send phishing messages to gain access to victim systems. All forms of phishing are electronically delivered social engineering. Phishing can be targeted, known as spearphishing. In spearphishing, a specific individual, company, or industry will be targeted by the adversary. More generally, adversaries can conduct non-targeted phishing, such as in mass malware spam campaigns. Adversaries may send victims emails containing malicious attachments or links, typically to execute malicious code on victim systems or to gather credentials for use of Valid Accounts. Phishing may also be conducted via third-party services, like social media platforms. Possible playbook uses

**Inputs:**

- `template`: Template name to enforce WildFire best practices profile.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the results.


## MITRE ATT&CK CoA - T1566.001 - Spear-Phishing Attachment

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Spear-Phishing Attachment technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may send spearphishing emails with a malicious attachment in an attempt to gain access to victim systems. Spearphishing attachment is a specific variant of spearphishing. Spearphishing attachment is different from other forms of spearphishing in that it employs the use of malware attached to an email. All forms of spearphishing are electronically delivered social engineering targeted at a specific individual, company, or industry. In this scenario, adversaries attach a file to the spearphishing email and usually rely upon User Execution to gain execution. Possible playbook uses

**Inputs:**

- `template`: Template name to enforce WildFire best practices profile.
- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the results.


## MITRE ATT&CK CoA - T1569.002 - Service Execution

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook Remediates the Service Execution technique using intelligence-driven Courses of Action (COA) defined by Palo Alto Networks Unit 42 team. ***Disclaimer: This playbook does not simulate an attack using the specified technique, but follows the steps to remediation as defined by Palo Alto Networks Unit 42 team’s Actionable Threat Objects and Mitigations (ATOMs). Techniques Handled: Kill Chain phases: MITRE ATT&CK Description: Adversaries may abuse the Windows service control manager to execute malicious commands or payloads. The Windows service control manager (services.exe) is an interface to manage and manipulate services.[1] The service control manager is accessible to users via GUI components as well as system utilities such as sc.exe and Net. PsExec can also be used to execute commands or payloads via a temporary Windows service created through the service control manager API.[2] Adversaries may leverage these mechanisms to execute malicious content. This can be done by either executing a new or modified service. This technique is the execution used in conjunction with Windows Service during service persistence or privilege escalation. Possible playbook uses


## NTT Cyber Threat Sensor

**Type:** integration  
**Product:** NTT Cyber Threat Sensor  

Retrieve alerts and recommendations from NTT CTS This integration was integrated and tested with version 1.0 of NTT Cyber Threat Sensor

**Commands:**

- `ntt-cyber-threat-sensor-poll-blobs`: Check if blobs is available
- `ntt-cyber-threat-sensor-fetch-blobs`: Collecting blobs, most commonly pcap from an incident


## OpenCTI

**Type:** integration  
**Product:** OpenCTI  

Manages indicators from OpenCTI. This integration was tested with version 5.12.17 of OpenCTI

**Commands:**

- `opencti-get-indicators`: Get indicators in OpenCTI.
- `opencti-indicator-delete`: Delete indicator.
- `opencti-indicator-field-update`: Update the indicator field. The fields that can be updated are: score, description.
- `opencti-indicator-create`: Create new indicator.
- `opencti-indicator-field-add`: Add a field to the indicator. Fields that can be added are marking definition and label.
- `opencti-indicator-field-remove`: Remove indicator field value. Fields which values can be removed are marking definition and label.
- `opencti-indicator-create`: Create a new indicator in OpenCTI.
- `opencti-label-list`: Get list of all labels.
- `opencti-label-create`: Create a new label.
- `opencti-external-reference-create`: Create external reference.
- `opencti-marking-definition-list`: Get a list of all marking definitions.
- `opencti-relationship-create`: Create new relationship.
- `opencti-incident-delete`: Delete incident.
- `opencti-incident-create`: Create new incident.
- `opencti-observable-field-add`: Add a field to the observable. Fields that can be added are marking definition and label.


## OpenCTI Create Indicator

**Type:** playbook  
**Product:** OpenCTI  

Create indicator at OpenCTI

**Inputs:**

- `label_name`: Label name to add to new indicator.
- `type`: The indicator type to create. Possible values: "Account", "Domain", "Email", "File-md5", "File-sha1", "File-sha256", "Host", "IP", "IPV6", "
- `marking_definition_id`: Marking definition id to add to new indicator. Use opencti-marking-definition-list to get marking id.
- `created_by_id`: Creator of the new indicator. Use opencti-organization-list to find all organizations id at opencti, or use opencti-organization-create to c
- `external_reference_source_name`: External References Source Name. In order to use external references, external_reference_url and external_reference_source_name are mandator
- `external_reference_url`: External References URL. In order to use external references, external_reference_url and external_reference_source_name are mandatory.
- `description`: New indicator description.
- `score`: New indicator score. Valid value: number between 0 to 100.


## Palo Alto Networks Threat Vault v2

**Type:** integration  
**Product:** Threat Vault by Palo Alto Networks  

Use the Palo Alto Networks Threat Vault to research the latest threats (vulnerabilities/exploits, viruses, and spyware) that Palo Alto Networks next-generation firewalls can detect and prevent. This integration was integrated and tested with Palo Alto Networks Threat Vault v2. Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `file`: Checks the reputation of an antivirus in Threat Vault.
- `cve`: Checks the reputation of CVE in Threat Vault.
- `threatvault-threat-signature-get`: Gets the antivirus or anti-spyware or files signature.
- `threatvault-release-note-get`: Retrieves the release notes information by version.
- `threatvault-threat-batch-search`: Retrieves the threats signature metadata by ID, name, or sample hash (sha256 or md5) in batch mode. Batch limit is 100 entries.
- `threatvault-threat-search`: Retrieves threat metadata. The nature of the query is determined by the query parameter you provide.


## PAN-OS - Apply Security Profile to Policy Rule

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook is used to apply a PAN-OS security profile to a policy rule. The playbook performs the following tasks

**Inputs:**

- `device-group`: The device group to work on. Exists only in panorama!
- `profile_type`: Security profile type. Can be 'data-filtering', 'file-blocking', 'spyware', 'url-filtering', 'virus, 'vulnerability', or wildfire-analysis.'
- `profile_name`: The profile name to apply to the rule.
- `pre-post-rulebase`: Determines whether the rule is a pre-rulebase or post-rulebase rule, according to the rule structure. Exists only in panorama!
- `tag`: Tag for which to filter the rules.


## PAN-OS - Block all unknown and unauthorized applications

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook is used to find and remove all rules that allow unauthorized applications communication as any. The playbook performs the following tasks

**Inputs:**

- `pre_post`: Rules location. Can be 'pre-rulebase' or 'post-rulebase'. Mandatory for Panorama instances.
- `device-group`: The device group for which to return addresses (Panorama instances).
- `tag`: Tag for which to filter the rules.


## PAN-OS - Enforce Anti-Spyware Best Practices Profile

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook enforces the Anti-Spyware Best Practices Profile as defined by Palo Alto Networks BPA. The playbook performs the following tasks

**Inputs:**

- `device-group`: The device group to work on. Exists only in panorama!
- `tag`: Tag for which to filter the results.
- `pre-post-rulebase`: Determines whether the rule is a pre-rulebase or post-rulebase rule, according to the rule structure. Exists only in panorama!


## PAN-OS - Enforce Anti-Virus Best Practices Profile

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook enforces the Anti-Virus Best Practices Profile as defined by Palo Alto Networks BPA. The playbook performs the following tasks

**Inputs:**

- `device-group`: The device group to work on. Exists only in panorama!
- `tag`: Tag for which to filter the results.
- `pre-post-rulebase`: Determines whether the rule is a pre-rulebase or post-rulebase rule, according to the rule structure. Exists only in panorama!


## PAN-OS - Enforce File Blocking Best Practices Profile

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook enforces the File Blocking Best Practices Profile as defined by Palo Alto Networks BPA. The playbook performs the following tasks

**Inputs:**

- `device-group`: The device group to work on. Exists only in panorama!
- `tag`: Tag for which to filter the results.
- `pre-post-rulebase`: Determines whether the rule is a pre-rulebase or post-rulebase rule, according to the rule structure. Exists only in panorama!


## PAN-OS - Enforce URL Filtering Best Practices Profile

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook enforces the URL Filtering Best Practices Profile as defined by Palo Alto Networks BPA. The playbook performs the following tasks

**Inputs:**

- `device-group`: The device group to work on. Exists only in panorama!
- `tag`: Tag for which to filter the results.
- `pre-post-rulebase`: Determines whether the rule is a pre-rulebase or post-rulebase rule, according to the rule structure. Exists only in panorama!


## PAN-OS - Enforce Vulnerability Protection Best Practices Profile

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook enforces the Vulnerability Protection Best Practices Profile as defined by Palo Alto Networks BPA. The playbook performs the following tasks

**Inputs:**

- `device-group`: The device group to work on. Exists only in panorama!
- `tag`: Tag for which to filter the results.
- `pre-post-rulebase`: Determines whether the rule is a pre-rulebase or post-rulebase rule, according to the rule structure. Exists only in panorama!


## PAN-OS - Enforce WildFire Best Practices Profile

**Type:** playbook  
**Product:** MITRE ATT&CK - Courses of Action  

This playbook enforces the WildFire Best Practices Profile as defined by Palo Alto Networks BPA. The playbook performs the following tasks

**Inputs:**

- `template`: Template name to enforce WildFire best practices profile.
- `device-group`: The device group to work on. Exists only in panorama!
- `tag`: Tag for which to filter the results.
- `pre-post-rulebase`: Determines whether the rule is a pre-rulebase or post-rulebase rule, according to the rule structure. Exists only in panorama!


## PANW Threat Vault - Signature Search

**Type:** playbook  
**Product:** Threat Vault by Palo Alto Networks  

Initiates a Signature Search in Palo Alto Networks threat Vault

**Inputs:**

- `signature_name`: Signature name to search.
- `domain_name`: Domain name to search.
- `vendor`: Vendor name to search.
- `cve`: CVE name to search.
- `from`: From which signature to return results(used for paging). Default is 0.
- `to`: To which signature to return results. Default is from plus 10.
- `search_type`: Search type. ips for antispyware, dns for DNS and panav for antivirus.


## Process QWatch Alert - Qintel

**Type:** playbook  
**Product:** Qintel  

Extracts exposure records from a QWatch alert


## Proofpoint Protection Server v2

**Type:** integration  
**Product:** Proofpoint Protection Server  

Proofpoint email security appliance. This integration was integrated and tested with the following versions of Proofpoint Protection Server

**Commands:**

- `proofpoint-pps-smart-search`: Trace and analyze information about messages after they have been filtered by the Proofpoint Protection Server.
- `proofpoint-pps-quarantine-messages-list`: Search for quarantined messages.
- `proofpoint-pps-quarantine-message-release`: Releases the message to the email infrastructure without further scanning. The message remains in the folder and is moved to the deleted_folder if specified.
- `proofpoint-pps-quarantine-message-resubmit`: Resubmits the message to the filtering modules. The message is removed from the folder and is moved to any folder.
- `proofpoint-pps-quarantine-message-forward`: Forwards the message to another recipient. The message remains in the folder and will be moved to the deleted_folder if specified.
- `proofpoint-pps-quarantine-message-move`: Moves the message to the specified target folder.
- `proofpoint-pps-quarantine-message-delete`: Deletes the message from the quarantine folder. The message is removed from its folder and is moved to the deleted_folder if specified.
- `proofpoint-pps-quarantine-message-download`: Downloads an email message's raw data.
- `proofpoint-pps-get-user`: Gets the end user resource with the specified email address or UID.
- `proofpoint-pps-create-user`: Creates a new end user resource with the specified email address.
- `proofpoint-pps-modify-user`: Modifies a user profile.
- `proofpoint-pps-delete-user`: Delete a user profile.


## Proofpoint Threat Protection

**Type:** integration  
**Product:** Proofpoint Threat Protection  

Threat Protection APIs are REST APIs that allow Proofpoint On Demand customers to retrieve, add, update or delete certain PoD configurations

**Commands:**

- `proofpoint-tp-blocklist-get`: Get all entries in the Organizational Block List.
- `proofpoint-tp-blocklist-add-or-delete-entry`: Add/Delete entry from the Organizational Block List.
- `proofpoint-tp-safelist-get`: Get all entries in the Organizational Safe List.
- `proofpoint-tp-safelist-add-or-delete-entry`: Add To/Delete From the Organizational Safe List.
- `proofpoint-tp-blocklist-list`: Get entries from the Organizational Block List.
- `proofpoint-tp-blocklist-add-entry`: Add an entry to the Organizational Block List.
- `proofpoint-tp-blocklist-delete-entry`: Delete an entry from the Organizational Block List.
- `proofpoint-tp-safelist-list`: Get entries from the Organizational Safe List.
- `proofpoint-tp-safelist-add-entry`: Add an entry to the Organizational Safe List.
- `proofpoint-tp-safelist-delete-entry`: Delete an entry from the Organizational Safe List.


## Proofpoint Threat Response

**Type:** integration  
**Product:** Proofpoint Threat Response  

Use the Proofpoint Threat Response integration to orchestrate and automate incident response

**Commands:**

- `proofpoint-tr-get-list`: Gets items for the specified list.
- `proofpoint-tr-add-to-list`: Adds a member to the specified list.
- `proofpoint-tr-block-ip`: Adds the supplied IP addresses to the specified IP block list.
- `proofpoint-tr-block-domain`: Adds the supplied domains to the specified block list.
- `proofpoint-tr-search-indicator`: Returns indicators from the specified list, according to the defined filter.
- `proofpoint-tr-delete-indicator`: Deletes an indicator from the specified list.
- `proofpoint-tr-block-url`: Adds the supplied URLs to the specified URL block list.
- `proofpoint-tr-block-hash`: Adds the supplied file hashes to the specified file hash block list.
- `proofpoint-tr-list-incidents`: Retrieves all incident metadata from Threat Response by specifying filter criteria such as the state of the incident or time of closure.
- `proofpoint-tr-get-incident`: Retrieves incident metadata from Threat Response.
- `proofpoint-tr-update-incident-comment`: Adds comments to an existing Threat Response incident, by incident ID.
- `proofpoint-tr-add-user-to-incident`: Assigns a user to an incident as a target or attacker.
- `proofpoint-tr-ingest-alert`: Ingest an alert into Threat Response.
- `proofpoint-tr-close-incident`: Close an incident
- `proofpoint-tr-verify-quarantine`: Verify if an email has been quarantined.


## PublishThreatIntelReport

**Type:** script  
**Product:** Threat Intel Reports (BETA)  

Sets a Threat Intel Report as published

**Inputs:**

- `object`: The Threat Intel Report object to publish.


## Qintel PMI

**Type:** integration  
**Product:** Qintel  

Qintel’s Patch Management Intelligence (PMI) product simplifies the vulnerability management process by providing vital context around reported Common Vulnerabilities and Exposures. With this integration, users can query PMI to surface CVEs that are known by Qintel to be leveraged by eCrime and Nation State adversaries. This integration was integrated and tested with version 0.16.0 of PMI

**Commands:**

- `cve`: Queries Qintel for CVE intelligence


## Qintel QSentry

**Type:** integration  
**Product:** Qintel  

QSentry queries help measure the likelihood that a user is masking their identity using publicly or privately available proxy or VPN services. The returns also flag any known fraud associations. QSentry aggregates data from Qintel’s proprietary Deep and DarkWeb research, as well as from commercially available anonymization services. This integration was integrated and tested with version 4.0 of Qintel QSentry

**Commands:**

- `ip`: Queries Qintel for IP reputation data


## Qintel QWatch

**Type:** integration  
**Product:** Qintel  

Qintel's QWatch system contains credentials obtained from dump sites, hacker collaboratives, and command and control infrastructures of eCrime- and APT-related malware. With this integration, users can fetch exposure alerts as incidents and discover exposed credentials associated with their organization. This integration was integrated and tested with version 1.1.6 of QWatch

**Commands:**

- `qintel-qwatch-exposures`: Search QWatch for exposed credentials


## Rapid7 - Threat Command (IntSights)

**Type:** integration  
**Product:** Rapid7 - Threat Command (IntSights)  

Rapid7 Insight - Threat Command allows managing alerts, CVEs, IOCs, and assets by accounts and MSSP accounts. This integration was integrated and tested with version 3.1.4 of rapid7_threat_command

**Commands:**

- `threat-command-cyber-term-list`: List cyber terms by filter.
- `threat-command-cyber-term-cve-list`: List cyber term CVEs by cyber term ID.
- `threat-command-cyber-term-ioc-list`: List cyber term IOCs by cyber term ID.
- `threat-command-source-list`: Gets lists of IOC document sources.
- `threat-command-source-document-create`: Adds a new IOC source document. At least one IOC is required.
- `threat-command-source-document-delete`: Deletes an existing IOC source document.
- `threat-command-source-document-ioc-create`: Create new IOCs to existing IOC source documents. At least one IOC is required.
- `threat-command-ioc-search`: Gets IOC details by value or IOC's full enrichment data. While using the enrichment flag, the command is scheduled and allows us to get full enrichment data. No
- `threat-command-ioc-tags-add`: Adds user tags to IOCs. This enables you to classify IOCs and later search for all IOCs with a specific tag. There is no indication of success or failure for th
- `threat-command-account-whitelist-update`: You can add an IOC to your user whitelist (even if it is already on the system whitelist). If you change your mind, you can then revert that decision to rely ag
- `threat-command-account-whitelist-remove`: Reverts IOC values to the system-default whitelist status. The ETP Suite automatically whitelists certain IOCs, such as company assets. You can override this de
- `threat-command-ioc-blocklist-add`: Adds an IOC to an internal Remediation Blocklist. By sending the blocklist to security devices, you can block the IOCs. At least one IOC is required.
- `threat-command-ioc-blocklist-remove`: Removes IOC values from the Remediation blocklist. There is no indication of success or failure for this command. The user has to choose a correct and existing 
- `threat-command-ioc-severity-update`: Changes the severity of existing IOCs for the requester account (overrides the system severity). At least one IOC is required.
- `threat-command-ioc-comment-add`: Adds comments to IOCs. At least one IOC is required.


## Recorded Future - Lists

**Type:** integration  
**Product:** Recorded Future Intelligence  

Search and manage watchlists in Recorded Future This integration was integrated and tested with version 1.1.1 of RecordedFutureLists

**Commands:**

- `recordedfuture-lists-search`: Search for lists in Recorded Future
- `recordedfuture-lists-add-entities`: Add entities to a list, separate entities by commas. "NOTE:" if entity type is specified, only one entity type can be added with each action. When adding IDs us
- `recordedfuture-lists-remove-entities`: Remove entities from a list. Separate entities with commas. "NOTE:" If entity type is specified, only one entity type can be added with each action. When adding
- `recordedfuture-lists-entities`: Get the entities that are currently in the given lists.


## Recorded Future - Playbook Alerts

**Type:** integration  
**Product:** Recorded Future Intelligence  

Fetch & triage Recorded Future Playbook Alerts

**Commands:**

- `recordedfuture-playbook-alerts-search`: Search playbook alerts based on filters.
- `recordedfuture-playbook-alerts-details`: Get Playbook alert details by ID.
- `recordedfuture-playbook-alerts-update`: Update the status of one or multiple Playbook alerts


## Recorded Future - Threat Actor Search

**Type:** playbook  
**Product:** Recorded Future Intelligence  

Template playbook to initiate an Automated Threat Hunt based on the Threat Map in Recorded Future. The Playbook fetches links related to the Threat Actors part of the Threat Map from Recorded Future and launches a hunt in the SIEM for any detections within the environment

**Inputs:**

- `threat_actor`: The threat actor to enrich & hunt indicators for.


## Recorded Future Alerts

**Type:** integration  
**Product:** Recorded Future  

Fetch and triage Recorded Future Classic Alerts and Recorded Future Playbook Alerts directly from the platform. The integration allows you to: Guide: migrating from Recorded Future Intelligence pack

**Commands:**

- `rf-alerts`: List Classic or Playbook alerts.
- `rf-alert-lookup`: Look up a single Recorded Future alert by ID.
- `rf-alert-update`: Update an alert in the Recorded Future platform.
- `rf-alert-rules`: Search for alert rule IDs.
- `rf-alert-images`: Fetch alert images and attach to incident in context Files.


## Recorded Future Attack Surface Intelligence

**Type:** integration  
**Product:** Recorded Future Attack Surface Intelligence  
**Commands:**

- `asi-project-issues-fetch`: Fetches all the current or added issues.


## Recorded Future CVE Intelligence

**Type:** playbook  
**Product:** Recorded Future Intelligence  

CVE Enrichment using Recorded Future Intelligence

**Inputs:**

- `CVE`: The CVE ID to enrich.


## Recorded Future CVE Reputation

**Type:** playbook  
**Product:** Recorded Future Intelligence  

CVE reputation with Recorded Future SOAR Enrichment

**Inputs:**

- `CVE`: The CVE ID to get reputation of.


## Recorded Future Detailed Alert example

**Type:** playbook  
**Product:** Recorded Future Intelligence  

Detailed alert example for Recorded Future. This playbook is intended as guidance for how the command recordedfuture-single-alert can be used in playbooks. The single alert takes an alert id which can be retrieved from recordedfuture-alerts. If a specific alert rule is desired you can first fetch alert rules and input the alert rule id into reccordedfuture-alerts

**Inputs:**

- `freetext`: Freetext to search for specific alert


## Recorded Future Domain Abuse

**Type:** playbook  
**Product:** Recorded Future Intelligence  

This playbook was developed as a template to handle the ingestion of Recorded Future Domain Abuse playbook alerts


## Recorded Future Domain Intelligence

**Type:** playbook  
**Product:** Recorded Future Intelligence  

Domain Enrichment using Recorded Future Intelligence

**Inputs:**

- `Domain`: The domain name to enrich.


## Recorded Future Domain Reputation

**Type:** playbook  
**Product:** Recorded Future Intelligence  

Domain reputation using Recorded Future SOAR Enrichment

**Inputs:**

- `Domain`: The domain name to get reputation of.


## Recorded Future External Usecase

**Type:** playbook  
**Product:** Recorded Future Identity  

External use case for Identity search and lookup using Recorded Future Identity

**Inputs:**

- `latest-downloaded`: Time frame for the leaked identities
- `domain-type`: Type of the domain(Email, Authorization, All)
- `identities`: String of identities separated by comma
- `first-downloaded`: Time frame for the leaked identities


## Recorded Future File Intelligence

**Type:** playbook  
**Product:** Recorded Future Intelligence  

File Enrichment using Recorded Future Intelligence

**Inputs:**

- `MD5`: File MD5 hash to enrich.
- `SHA256`: File SHA-256 hash to enrich.
- `SHA1`: File SHA-1 hash to enrich.


## Recorded Future File Reputation

**Type:** playbook  
**Product:** Recorded Future Intelligence  

File reputation using Recorded Future SOAR Enrichment

**Inputs:**

- `MD5`: File MD5 hash to get reputation of.
- `SHA256`: File SHA-256 hash to get reputation of.
- `SHA1`: File SHA-1 hash to get reputation of.


## Recorded Future Identity

**Type:** integration  
**Product:** Recorded Future Identity  
**Commands:**

- `recordedfuture-identity-search`: Search for identities in the Recorded Future dataset.
- `recordedfuture-identity-lookup`: Get detailed information regarding identities.


## Recorded Future Identity - Create Incident (sub)

**Type:** playbook  
**Product:** Recorded Future Identity  
**Inputs:**

- `ExposedIdentity`: 
- `Domain`: 


## Recorded Future Identity - Identity Found (incident)

**Type:** playbook  
**Product:** Recorded Future Identity  

Identity playbook for Incident when the Identity has been found in Recorded Future Identity Dataset

**Inputs:**

- `ExposedIdentity`: 


## Recorded Future Identity - Lookup Identities (parent)

**Type:** playbook  
**Product:** Recorded Future Identity  

## Recorded Future IOC Reputation

**Type:** playbook  
**Product:** Recorded Future Intelligence  

Entity Reputation using sub-playbooks

**Inputs:**

- `IP`: The IP addresses to enrich
- `MD5`: File MD5 to enrich
- `SHA256`: File SHA256 to enrich
- `SHA1`: File SHA1 to enrich
- `URL`: URL to enrich
- `Domain`: The domain name to enrich


## Recorded Future IP Intelligence

**Type:** playbook  
**Product:** Recorded Future Intelligence  

IP Address Enrichment using Recorded Future Intelligence

**Inputs:**

- `IP`: The IP address to enrich.


## Recorded Future IP Reputation

**Type:** playbook  
**Product:** Recorded Future Intelligence  

IP address reputation using Recorded Future SOAR Enrichment

**Inputs:**

- `IP`: The IP address to get reputation of.


## Recorded Future Leaked Credential Alert Handling

**Type:** playbook  
**Product:** Recorded Future Intelligence  

Template playbook showing suggested steps to triage leaked credential alerts. Classifier/Mapper are available to ingest Recorded Future Leaked Credential Alerts

**Inputs:**

- `account`: 


## Recorded Future List Management

**Type:** playbook  
**Product:** Recorded Future Intelligence  

Manage, view, and edit your lists in Recorded Future


## Recorded Future Playbook Alert Details

**Type:** playbook  
**Product:** Recorded Future Intelligence  

A default playbook to fetch details of Playbook alert that does not yet have mapping made by Recorded Future


## Recorded Future Sandbox

**Type:** playbook  
**Product:** Recorded Future Intelligence  

Template playbook utilizing Hatching.io to sandbox a given file and generate an analysis report. Indicators from the given report are then extracted and enriched with Recorded Future data

**Inputs:**

- `File`: 


## Recorded Future Threat Assessment

**Type:** playbook  
**Product:** Recorded Future Intelligence  

Threat Assessment using the Recorded Future SOAR Triage API and the context Phishing

**Inputs:**

- `CVE`: CVE ID to check if it is related to the C2 context.
- `IP`: IP Address to check if it is related to the C2 context.
- `URL`: URL to check if it is related to the C2 context.
- `MD5`: MD5 to check if it is related to the C2 context.
- `SHA1`: SHA-1 to check if it is related to the C2 context.
- `SHA256`: SHA-256 to check if it is related to the C2 context.
- `Domain`: Domain to check if it is related to the C2 context.
- `threat-assessment-context`: Context to use for assessment. This is used by Recorded Future to calculate the relevant score and verdict. Valid values are "c2", "malware"


## Recorded Future Typosquat Alert Handling

**Type:** playbook  
**Product:** Recorded Future Intelligence  

Template playbook showing suggested steps to triage typo squat alerts. Classifier/Mapper are available to ingest Recorded Future Typo squat Alerts

**Inputs:**

- `domain`: 


## Recorded Future URL Intelligence

**Type:** playbook  
**Product:** Recorded Future Intelligence  

URL Enrichment using Recorded Future Intelligence

**Inputs:**

- `URL`: The URL to enrich.


## Recorded Future URL Reputation

**Type:** playbook  
**Product:** Recorded Future Intelligence  

URL reputation using Recorded Future SOAR Enrichment

**Inputs:**

- `URL`: URL to get reputation of.


## Recorded Future v2

**Type:** integration  
**Product:** Recorded Future Intelligence  

Unique threat intel technology that automatically serves up relevant insights in real time. This integration was integrated and tested with version 2.4.3 of Recorded Future v2 Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `domain`: Gets a quick indicator of the risk associated with a domain.
- `ip`: Gets a quick indicator of the risk associated with an IP address.
- `file`: Gets a quick indicator of the risk associated with a file.
- `cve`: Gets a quick indicator of the risk associated with a CVE.
- `url`: Gets a quick indicator of the risk associated with a URL.
- `recordedfuture-threat-assessment`: Get an indicator of the risk based on context.
- `recordedfuture-intelligence`: Get threat intelligence for an IP, Domain, CVE, URL, File or Malware.
- `recordedfuture-links`: Get Insikt Group Research Links for an IP, Domain, CVE, URL, File, or Malware.
- `recordedfuture-single-alert`: Get detailed information from vulnerability, typosquat and credential alerts.
- `recordedfuture-alerts`: Gets details on alerts configured and generated by Recorded Future by alert rule ID and/or time range.
- `recordedfuture-alert-rules`: Search for alert rule IDs.
- `recordedfuture-alert-set-status`: Set alert into predefined status.
- `recordedfuture-alert-set-note`: Set a note for the alert in Recorded Future.
- `recordedfuture-malware-search`: Search for a malware by specified filters.


## Recorded Future Vulnerability

**Type:** playbook  
**Product:** Recorded Future Intelligence  

This playbook was developed as a template to handle the ingestion of Recorded Future Cyber Vulnerability playbook alerts


## Recorded Future Vulnerability Alert Handling

**Type:** playbook  
**Product:** Recorded Future Intelligence  

Template playbook showing suggested steps to triage new critical vulnerability alerts. Playbook include New and Critical CVEs. Classifier/Mapper are available to ingest Recorded Future New, Critical or Pre NVD Vulnerability Alerts

**Inputs:**

- `cve`: 


## Recorded Future Workforce Usecase

**Type:** playbook  
**Product:** Recorded Future Identity  

Workforce use case for Identity search and lookup using Recorded Future Identity

**Inputs:**

- `latest-downloaded`: Time frame for the leaked identities
- `domain-type`: Type of the domain(Email, Authorization, All)
- `identities`: String of identities separated by comma
- `first-downloaded`: Time frame for the leaked identities


## ReliaQuest GreyMatter DRP Incidents

**Type:** integration  
**Product:** ReliaQuest Digital Risk Protection  

ReliaQuest GreyMatter DR monitors and manages an organization's digital risk across the widest range of data sources within the open, deep, and dark web. This integration was integrated and tested with version v1 of ReliaQuest GreyMatter DRP Incidents

**Commands:**

- `ds-search`: Perform a general search against incidents, threats closed sources, etc.


## ReliaquestTakedown

**Type:** integration  
**Product:** ReliaQuest Digital Risk Protection  

This is Reliaquest DRP Takedown integration. It enables platform user to create and manage takedowns. This integration was integrated and tested with version 6.9.0 of ReliaquestTakedown

**Commands:**

- `rq-takedown-create`: Create takedown command takes brand id, type, target and portal shortcode (optional) and returns the created takedown in response.
- `rq-takedown-list-brand`: Returns list of allowed brand details for takedown.
- `rq-takedown-create-comment`: Create comment for a takedown.
- `rq-takedown-upload-attachment`: Uploads attachment for takedown.
- `rq-takedown-download-attachment`: Downloads attachment for takedown.


## Retrieve Alert Attachments - Rapid7 ThreatCommand

**Type:** playbook  
**Product:** Rapid7 - Threat Command (IntSights)  

This playbook is used by default for the Rapid7 ThreatCommand alerts being ingested as platform incidents. This playbook retrieves attachments (CSV file and images) using the Alert ID incident field

**Inputs:**

- `alert_id`: Alert ID of the Rapid7 Threat Command incident.
- `fetch_attachments`: Boolean value indicating to include image files of alerts. If set to "true", then it fetches image files; otherwise, it does not.
- `fetch_csv`: Boolean value indicating to include CSV file of alerts. If set to "true", then it fetches CSV file; otherwise, it does not.


## RSS Create Indicators From Report

**Type:** playbook  
**Product:** RSS Feed  

The RSS Feed integration provides information for the RSS Create Indicators From Report playbook. The playbook: the platform. Note that if you selected the Triggered by delta in feed option when configuring the Job, the “Run only on new and modified indicators” playbook option is automatically selected

**Inputs:**

- `Indicator Query`: Filter all Report indicators which haven't been processed. Make sure to add "-tags:in_process " to the query to filter out the reports that 
- `tag`: The tag that will be added to each processed report.


## Sanitize File - CDR - ThreatZone

**Type:** playbook  
**Product:** ThreatZone  

Sanitize one file using the ThreatZone CDR integration. Returns relevant reports to the War Room and file reputations to the context data. CDR Scan Extensions: doc, docm, docx, dotm, ppt, pptm, pptx, xls, xlsm, pdf, odc, odt, ott, odp, otp, ods, ots, rtf, tiff, jpeg, png, gif, bmp, webp, jpx, svg, zip, xml, ics, html, lnk, xlsx

**Inputs:**

- `File`: File object of the file to analyze. The File is taken from the context.
- `Interval`: Frequency (in minutes) between polling attempts.
- `Timeout`: Maximum polling duration (in minutes) before the playbook resumes.


## Sanitize File - CDR - ThreatZone v2

**Type:** playbook  
**Product:** ThreatZone  

Sanitize one file using the ThreatZone CDR integration. Returns relevant reports to the War Room and file reputations to the context data. CDR Scan Extensions: doc, docm, docx, dotm, ppt, pptm, pptx, xls, xlsm, pdf, odc, odt, ott, odp, otp, ods, ots, rtf, tiff, jpeg, png, gif, bmp, webp, jpx, svg, zip, xml, ics, html, lnk, xlsx

**Inputs:**

- `File`: File object of the file to analyze. The File is taken from the context.
- `Interval`: Frequency (in minutes) between polling attempts.
- `Timeout`: Maximum polling duration (in minutes) before the playbook resumes.


## Search LOLBAS Tools By Name

**Type:** playbook  
**Product:** LOLBAS Feed  

This playbook searches for LOLBAS tools by their name, and returns the tool command from LOLBAS

**Inputs:**

- `Tool`: 


## SecneurX Threat Feeds

**Type:** integration  
**Product:** Secneurx Threat Feeds  

SecneurX provides real-time threat intelligence that protects companies against the latest cyber threats, including APTs, phishing, malware, ransomware, data exfiltration, and brand infringement. Security teams rely on our dependable and rich data to expand their threat landscape visibility, resulting in improved detection rates and response times. This integration was integrated and tested with version 1.0.0 of SecneurX Threat Feeds

**Commands:**

- `snxfeeds-get-indicators`: Retrieves a limited number of the indicators.


## SEKOIAIntelligenceCenter

**Type:** integration  
**Product:** SEKOIAIntelligenceCenter  

Fetch Indicator and Observables from SEKOIA.IO Intelligence Center. To use this integration, please create an API Key with the right permissions. This integration was integrated and tested with version 2.20220712 of SEKOIA.IO Intelligence Center

**Commands:**

- `GetObservable`: Query SEKOIA.IO Intelligence Center for information about this observable.
- `GetIndicator`: Query SEKOIA.IO Intelligence Center for information about this indicator. No information is returned if the value is not a known by SEKOIA.IO as an indicator (I
- `ip`: Query SEKOIA.IO Intelligence Center for information about this indicator. No information is returned if the value is not a known by SEKOIA.IO as an indicator (I
- `url`: Query SEKOIA.IO Intelligence Center for information about this indicator. No information is returned if the value is not a known by SEKOIA.IO as an indicator (I
- `domain`: Query SEKOIA.IO Intelligence Center for information about this indicator. No information is returned if the value is not a known by SEKOIA.IO as an indicator (I
- `file`: Query SEKOIA.IO Intelligence Center for information about this indicator. No information is returned if the value is not a known by SEKOIA.IO as an indicator (I
- `email`: Query SEKOIA.IO Intelligence Center for information about this indicator. No information is returned if the value is not a known by SEKOIA.IO as an indicator (I
- `GetIndicatorContext`: Query SEKOIA.IO Intelligence Center for context around this indicator


## SEPCheckOutdatedEndpoints

**Type:** script  
**Product:** Symantec Endpoint Protection  

Checks if any endpoints are using an AV definition that is not the latest version

**Inputs:**

- `requiredavdefversion`: The AV definitions version to check against.


## Sixgill DarkFeed Enrichment

**Type:** integration  
**Product:** Sixgill Darkfeed - Annual Subscription  

Leverage the power of Sixgill to supercharge the platform. Enrich IOCs such as domains, URLs, hashes, and IP addresses straight from platform platform. This integration was integrated and tested with sixgill-clients

**Commands:**

- `ip`: Returns information and a reputation for each IP in the input list.
- `url`: Returns information and a reputation for each URL in the input list.
- `sixgill-get-actor`: Returns information and a reputation for each actor in the input list.


## Sixgill DarkFeed Threat Intelligence

**Type:** integration  
**Product:** Sixgill Darkfeed - Annual Subscription  

Sixgill's premium underground intelligence collection capabilities, real-time collection and advanced warnings of IOCs help you keep your edge against unknown threats. This integration was integrated and tested with Sixgill clients

**Commands:**

- `sixgill-get-indicators`: Fetching Sixgill DarkFeed indicators


## SixgillSearchIndicators

**Type:** script  
**Product:** Sixgill Darkfeed - Annual Subscription  

Search indicator based on query


## Symantec Endpoint Detection and Response (EDR) - On Prem

**Type:** integration  
**Product:** Symantec Endpoint Detection and Response  

Symantec EDR (On Prem) endpoints help to detect threats in your network by filter endpoints data to find Indicators of Compromise (IoCs) and take actions to remediate the threat(s). EDR on-premise capabilities allow incident responders to quickly search, identify, and contain all impacted endpoints while investigating threats using a choice of on-premises. This integration was integrated and tested with version 4.6 of SymantecEDR

**Commands:**

- `symantec-edr-endpoint-isolate`: Isolates or quarantines endpoints by cutting connections that the endpoint(s) has to internal networks and external networks, based on the endpoint device IDs.
- `symantec-edr-domain-file-association-list`: List of domain and file association.
- `symantec-edr-endpoint-domain-association-list`: List of endpoint and domain association.
- `symantec-edr-endpoint-file-association-list`: List of domain and file association.
- `symantec-edr-domain-instance-list`: Get domain instances.
- `symantec-edr-endpoint-instance-list`: Get endpoint instances.
- `symantec-edr-file-instance-list`: Get File Instances
- `symantec-edr-system-activity-list`: Get system activities or logs.
- `symantec-edr-audit-event-list`: Get Audit Events
- `symantec-edr-event-list`: Get events or system alerts from EDR on-premise.
- `symantec-edr-incident-event-list`: Get events for incidents.
- `symantec-edr-incident-list`: Get incidents from Symantec EDR on-premise API.
- `symantec-edr-incident-comment-get`: Get incident comments based on incident UUID.
- `symantec-edr-deny-list-policy-get`: Get deny list policies.
- `symantec-edr-allow-list-policy-get`: Get allow list policies.


## Symantec Endpoint Protection v2

**Type:** integration  
**Product:** Symantec Endpoint Protection  

Query the Symantec Endpoint Protection Manager using the official REST API

**Commands:**

- `sep-endpoints-info`: Returns information about endpoints.
- `sep-groups-info`: Returns information about groups.
- `sep-system-info`: Returns information about the system, such as version or AV definition.
- `sep-command-status`: Retrieves the status of a command.
- `sep-client-content`: Retrieves the content of the client.
- `sep-list-policies`: Retrieves a list of existing policies.
- `sep-assign-policy`: Assigns an existing policy to a specified location.
- `sep-list-locations`: Retrieves a list of location IDs for a specified group.
- `sep-endpoint-quarantine`: Quarantines an endpoint according to its policy.
- `sep-scan-endpoint`: Scans an endpoint.
- `sep-update-endpoint-content`: Updates the content of a specified client.
- `sep-move-client-to-group`: Moves a client to a group.
- `sep-identify-old-clients`: Get endpoints for a running version that is different than the target version or the desired version (if specified).


## Sysdig Response Actions

**Type:** integration  
**Product:** Sysdig Response Actions  

This is an integration that will use Sysdig agent to respond to malicious activity by triggering different actions at the host or container level like killing a container, quarantine a file or perform a system capture This integration was integrated and tested with Host shield 13.9.1 of the Sysdig Agent and ResponseActions version 0.1.0

**Commands:**

- `execute-response-action`: Executes response actions through the Sysdig API. Each action type requires a specific set of parameters.
- `create-system-capture`: Triggers a system capture, recording all system calls at the host level.
- `get-capture-file`: Gets a system capture based on the capture ID.
- `get-action-execution`: Gets the status and information of a triggered action execution.
- `sysdig-agent-info-get`: Resolves a host MAC address to its Sysdig agent details (agent ID, customer ID, hostname). The result is cached per MAC address.
- `sysdig-customer-info-get`: Gets the Sysdig customer ID and name. The result is cached per integration instance.


## Sysdig Trigger System Capture

**Type:** playbook  
**Product:** Sysdig Response Actions  

Enriches Sysdig runtime event incidents with agent information via API and optionally triggers a system capture on the affected host


## Tanium Threat Response

**Type:** integration  
**Product:** Tanium Threat Response  

Tanium Threat Response - This Integration works with Tanium Threat Response version below 3.0.159. In order to use Tanium Threat Response version 3.0.159 and above, use Tanium Threat Response V2 Integration

**Commands:**

- `tanium-tr-get-intel-doc-by-id`: Returns an intel document object based on ID.
- `tanium-tr-list-intel-docs`: Returns a list of all intel documents.
- `tanium-tr-list-alerts`: Returns a list of all alerts.
- `tanium-tr-get-alert-by-id`: Returns an alert object based on alert ID.
- `tanium-tr-alert-update-state`: Updates the state of a single alert.
- `tanium-tr-list-snapshots-by-connection`: Returns all snapshots of a single connection.
- `tanium-tr-create-snapshot`: Captures a new snapshot by connection name.
- `tanium-tr-delete-snapshot`: Deletes a snapshot by connection name and snapshot ID.
- `tanium-tr-list-local-snapshots-by-connection`: Returns all local snapshots of a single connection.
- `tanium-tr-delete-local-snapshot`: Deletes a local snapshot by directory name and file name.
- `tanium-tr-list-connections`: Returns all connections.
- `tanium-tr-get-connection-by-name`: Returns a connection object based on connection name.
- `tanium-tr-create-connection`: Creates a local or remote connection.
- `tanium-tr-delete-connection`: Deletes a connection by connection name.
- `tanium-tr-list-labels`: Returns all available labels in the system.


## Tanium Threat Response v2

**Type:** integration  
**Product:** Tanium Threat Response  

Use the Tanium Threat Response integration to manage endpoints processes, evidence, alerts, files, snapshots, and connections. This Integration works with Tanium Threat Response version 3.0.159 and above. This integration was integrated and tested with versions 3.5.284 and 4.x of Tanium Threat Response v2

**Commands:**

- `tanium-tr-get-intel-doc-by-id`: Returns an intel document object based on ID.
- `tanium-tr-list-intel-docs`: Returns a list of all intel documents.
- `tanium-tr-list-alerts`: Returns a list of all alerts.
- `tanium-tr-get-alert-by-id`: Returns an alert object based on alert ID.
- `tanium-tr-alert-update-state`: Updates the state of the specified alerts.
- `tanium-tr-create-snapshot`: Captures a new snapshot by connection id.
- `tanium-tr-delete-snapshot`: Deletes a snapshot by connection name and snapshot ID.
- `tanium-tr-list-snapshots`: Returns all local snapshots of a single connection.
- `tanium-tr-delete-local-snapshot`: Deletes a local snapshot by connection id.
- `tanium-tr-list-connections`: Returns all connections.
- `tanium-tr-create-connection`: Creates a local or remote connection.
- `tanium-tr-delete-connection`: Deletes a connection by connection id.
- `tanium-tr-close-connection`: Closes a connection by connection id.
- `tanium-tr-list-labels`: Returns all available labels in the system.
- `tanium-tr-get-label-by-id`: Returns a label object based on label ID.


## ThreatConnect v3

**Type:** integration  
**Product:** ThreatConnect  

ThreatConnect's integration is a intelligence-driven security operations solution with intelligence, automation, analytics, and workflows. This integration was integrated and tested with version 3 of ThreatConnect v3 REST API

**Commands:**

- `ip`: Searches for an indicator of type IP address.
- `url`: Searches for an indicator of type URL.
- `file`: Searches for an indicator of type file.
- `tc-owners`: Retrieves all owners for the current account.
- `tc-indicators`: Retrieves a list of all indicators.
- `tc-get-tags`: Returns a list of all ThreatConnect tags.
- `tc-tag-indicator`: Adds a tag to an existing indicator.
- `tc-get-indicator`: Retrieves information about an indicator.
- `tc-get-indicators-by-tag`: Fetches all indicators that have a tag.
- `tc-add-indicator`: Adds a new indicator to ThreatConnect.
- `tc-create-incident`: Creates a new incident group.
- `tc-incident-associate-indicator`: Associates an indicator with an existing incident. The indicator must exist before running this command. To add an indicator, run the tc-add-indicator command.
- `domain`: Searches for an indicator of type domain.
- `tc-get-incident-associate-indicators`: Returns indicators that are related to a specific incident.
- `tc-update-indicator`: Updates the indicator in ThreatConnect.


## ThreatExchange v2

**Type:** integration  
**Product:** ThreatExchange  

Receive threat intelligence about applications, IP addresses, URLs, and hashes. A service by Facebook This integration was integrated and tested with API version v3.2 of ThreatExchange

**Commands:**

- `file`: Checks the file reputation of the given hash.
- `ip`: Checks the reputation of the given IP address.
- `url`: Checks URL Reputation
- `domain`: Checks domain reputation.
- `threatexchange-query`: Searches for subjective opinions on indicators of compromise stored in ThreatExchange.
- `threatexchange-members`: Returns a list of current members of the ThreatExchange, alphabetized by application name. Each application may also include an optional contact email address. 
- `threatexchange-tags-search`: Enables searching for tags in ThreatExchange. With this call you can search for ThreatTag objects by text.
- `threatexchange-tagged-objects-list`: Gets a list of tagged objects for a specific ThreatTag.
- `threatexchange-object-get-by-id`: Gets ThreatExchange object by ID.


## ThreatIntelManagementGetIncidentsPerFeed

**Type:** script  
**Product:** Threat Intelligence Management  

Total number of incidents per OOTB feed. This automation runs using the default Limited User role, unless you explicitly change the permissions. For more information, see the section about permissions here: For the platform, see the  for the platform, see the  for the platform, see the


## ThreatMiner

**Type:** integration  
**Product:** ThreatMiner  

Data Mining for Threat Intelligence

**Commands:**

- `domain`: Retrieves data from ThreatMiner about a specified domain.
- `ip`: Retrieves data from ThreatMiner about a specified IP address.
- `file`: Retrieves data from ThreatMiner about a specified file.


## ThreatstreamBuildIocImportJson

**Type:** script  
**Product:** Anomali ThreatStream  

Builds A JSON array based on the values provided by the user for the 'threatstream-import-indicator-without-approval' command

**Inputs:**

- `email_values`: A comma-separated list of emails.
- `md5_values`: A comma-separated list of MD5 hashes.
- `ip_values`: A comma-separated list of IPs.
- `url_values`: A comma-separated list of URLs.
- `domain_values`: A comma-separated list of domains.
- `email_indicator_type`: The indicator type (Itype) of the emails provided. By default the type will be “Malware Email” (mal_email).
- `md5_indicator_type`: The indicator type (Itype) of the hashes provided. By default the type will be “Malware MD5” (mal_md5).
- `ip_indicator_type`: The indicator type (Itype) of the ip provided. By default the type will be “Malware IP” (mal_ip).


## ThreatZone

**Type:** integration  
**Product:** ThreatZone  

ThreatZone malware analysis sandboxing. This integration was integrated and tested with ThreatZone

**Commands:**

- `tz-sandbox-upload-sample`: Submits a sample to ThreatZone for sandbox analysis.
- `tz-static-upload-sample`: Submits a sample to ThreatZone for static analysis.
- `tz-cdr-upload-sample`: Submits a sample to ThreatZone for CDR.
- `tz-url-analysis`: Submits a URL to ThreatZone for analysis.
- `tz-get-result`: Retrieve the analysis result from ThreatZone.
- `tz-get-indicator-result`: Retrieves dynamic behaviour indicators for a submission from ThreatZone.
- `tz-get-ioc-result`: Retrieves Indicators of Compromise for a submission from ThreatZone.
- `tz-get-yara-result`: Retrieves YARA rules matched during analysis. Use tz-download-yara-rule for the generated rule file.
- `tz-get-artifact-result`: Retrieves analysis artifacts for a submission from ThreatZone.
- `tz-get-config-result`: Retrieves configuration extractor results for a submission from ThreatZone.
- `tz-get-sanitized`: Downloads a sanitized file from the ThreatZone API and uploads it to the War Room.
- `tz-download-html-report`: Downloads the HTML report for a submission and uploads it to the War Room.
- `tz-get-metafields`: Retrieves available ThreatZone metafields, optionally filtered by scan type.
- `tz-get-environments`: Retrieves available ThreatZone sandbox environments.
- `tz-list-network-configs`: Lists network configurations available to the current ThreatZone workspace.


## Unblock Indicator - Infoblox Cloud

**Type:** playbook  
**Product:** Infoblox Threat Defense with DDI  

This playbook unblocks the given IP or domain by adding it to the given allow type custom list of the Infoblox Cloud platform

**Inputs:**

- `ip_addresses`: The IP addresses to unblock.
- `domains`: The domains to unblock.
- `custom_list_name`: Specify the name of the custom list to add the given IP addresses or domains to. Default is "Default Allow".
- `custom_list_type`: Specify the type of the custom list to add the given IP addresses or domains to. Possible values are: default_allow, custom_list, threat_ins


## Unit 42 Intelligence

**Type:** integration  
**Product:** Unit 42 Threat Intelligence by Palo Alto Networks  

Enrich indicators with Unit 42 threat intelligence context including verdicts, threat object associations, and relationships

**Commands:**

- `ip`: Enrich an IP address with Unit 42 threat intelligence context.
- `domain`: Enrich a domain with Unit 42 threat intelligence context.
- `url`: Enrich a URL with Unit 42 threat intelligence context.
- `file`: Enrich a file hash with Unit 42 threat intelligence context.


## UnpublishThreatIntelReport

**Type:** script  
**Product:** Threat Intel Reports (BETA)  

Sets a Threat Intel Report as unpublished

**Inputs:**

- `object`: The Threat Intel Report object to unpublish.


## URL Enrichment - Infoblox Cloud

**Type:** playbook  
**Product:** Infoblox Threat Defense with DDI  

This playbook enriches URL with the dossier and TIDE data using Infoblox Threat Defense with DDI integration

**Inputs:**

- `urls`: The optional comma-separated list of URLs to enrich.


## URL Enrichment - RST Threat Feed

**Type:** playbook  
**Product:** RST Threat Feed  

Enrich URLs using one or more integrations. URL enrichment includes

**Inputs:**

- `URL`: URLs to enrich.
- `Rasterize`: Should the system take safe screenshots of input URLs?
- `VerifyURL`: Should the system perform SSL certificate verification on the URLs?
- `threshold`: Defines the minimum score to set indicators as malicious


## USTA Account Takeover Prevention Employee Credential Incident

**Type:** playbook  
**Product:** USTAv4 Cyber Threat Intelligence Platform  

This playbook automates the detection and response process when compromised employee credentials are identified via USTA platform

**Inputs:**

- `Minimum Password Length`: Minimum length of password


## USTAv4 Account Takeover Prevention

**Type:** integration  
**Product:** USTAv4 Cyber Threat Intelligence Platform  

USTAv4 Account Takeover Prevention is designed to collect compromised credentials sourced from stealer malware attacks, helping organizations identify potential account takeovers and enhance their security posture. Provided by PRODAFT. This integration was integrated and tested with version 4.1.0 of USTAv4 Account Takeover Prevention

**Commands:**

- `usta-atp-search-username`: Search for compromised credentials by username


## USTAv4 Stolen Credit Cards

**Type:** integration  
**Product:** USTAv4 Cyber Threat Intelligence Platform  

This integration offers organizations the ability to track stolen credit card data across the web, providing comprehensive insight into compromised card information sourced from underground markets, dark web forums, and other malicious platforms

**Commands:**

- `usta-scc-search`: Search for stolen credit card number


## XDR Best Practice Assessment

**Type:** playbook  
**Product:** XDR Best Practice Assessment  

This playbook covers an XDR Best Practice Assessment for existing XDR deployments. It provides surveys for each domain of the assessment. The assessment covers the following domains: Configurations, Agent Management, Policy and Profiles, Profile Extensions, Incident Management, and Incident Response

**Inputs:**

- `SurveyOwner`: Input the email address of the individual who will be filling out the survey. Default is the owner of the incident in platform.

