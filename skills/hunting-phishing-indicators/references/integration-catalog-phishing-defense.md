# Integration and Automation Catalog - Phishing Defense

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## Agari Phishing Defense

**Type:** integration  
**Product:** Agari Phishing Defense  

Agari Phishing Defense stops phishing, BEC, and other identity deception attacks that trick employees into harming your business. This integration was integrated and tested with a standard version of Agari Phishing Defense

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Check Point - Phishing Takedown

**Type:** playbook  
**Product:** Cyberint  

Automates or semi-automates the takedown of high-confidence phishing websites detected by Cyberint. The playbook evaluates the confidence and severity of a Cyberint phishing-website alert, submits a takedown request via the Cyberint Takedown API (automatically or after analyst approval), polls the takedown request until it reaches a terminal status, and annotates the incident and notifies the SOC of the outcome. Requires the Cyberint Takedown integration to be configured

**Inputs:**

- `URL`: The phishing website URL to submit for takedown. Defaults to the URL from the Cyberint alert data.
- `CustomerID`: The Cyberint customer ID, as configured in the Cyberint integration. Used to submit and track the takedown request.
- `Reason`: The takedown reason. One of: phishing, brand_abuse, impersonating_application, unofficial_application_distribution, malicious_content, socia
- `AlertID`: The Cyberint alert ID associated with the phishing website. Used to correlate the takedown request with the alert.
- `Brand`: The brand the phishing website is impersonating. Required by the takedown API to determine the original (legitimate) URL when the customer p
- `OriginalURL`: The URL of the original, legitimate content being impersonated. Required by the takedown API to determine the original URL when the customer
- `Confidence`: The confidence score (0-100) of the phishing website alert. Defaults to the Cyberint alert confidence field.
- `ConfidenceThreshold`: The minimum confidence score (0-100) required to initiate a takedown. Default is 80.


## Check Point Harmony Email and Collaboration (HEC)

**Type:** integration  
**Product:** Check Point Harmony Email and Collaboration (HEC)  

The Best Way to Protect Enterprise Email & Collaboration from phishing, malware, account takeover, data loss, etc. This integration was integrated and tested with version 1.1.14 of CheckPointHEC

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## CheckPhish

**Type:** integration  
**Product:** CheckPhish  

Check any URL to detect supsicious behavior

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## CheckPointHEC Get email for incident

**Type:** playbook  
**Product:** Check Point Harmony Email and Collaboration (HEC)  

Get email entity for a specific incident

**Inputs:**

- `entity`: Get email entity id from incident


## Cisco Email Threat Defense Connector

**Type:** integration  
**Product:** Cisco ETD Connector  

The Cisco ETD Connector ingests Cisco Secure Email Threat Defense (ETD) message, audit, and blocked connection logs into Cortex XSIAM for security analytics, monitoring, and threat investigation. This integration uses the Cisco Secure Email Threat Defense Log Export API

**Commands:**

- `None`: 


## Cloaked Ursa Diplomatic Phishing Campaign

**Type:** playbook  
**Product:** Cloaked Ursa Diplomatic Phishing Campaign  
**Inputs:**

- `PlaybookDescription`: The playbook description to be used in the Rapid Breach Response - Set Incident Info sub-playbook.
- `autoBlockIndicators`: Wether to block the indicators automatically.
- `QRadarTimeRange`: The time range for the QRadar queries.
- `SplunkEarliestTime`: The time range for the Splunk queries.
- `ElasticEarliestTime`: The time range for the Elastic queries.
- `LogAnalyticsTimespan`: The time range for the Azure Log Analytics queries.
- `XQLTimeRange`: The time range for the XQL queries.
- `ElasticIndex`: The elastic index to search in.


## ContextGetEmails

**Type:** script  
**Product:** Common Scripts  

Gets all email addresses in context, excluding ones given

**Inputs:**

- `excludedEmails`: The email addresses to exclude (comma-seperated).


## Darkmon - Email Deep Dive

**Type:** playbook  
**Product:** Darkmon  

Analyst-driven full Darkmon profile for a single email address. Runs board-protection check, all three boardemails categories, and global search. Outputs a unified summary into the incident War Room

**Inputs:**

- `Email`: Email address to investigate.


## Darkmon - Enrich Email

**Type:** playbook  
**Product:** Darkmon  

Sub-playbook that calls the Darkmon !email command and returns DBotScore + Common.Account.Email for the input Email indicator. Designed to be invoked from a parent playbook; does not auto-run on indicator creation

**Inputs:**

- `Email`: The Email indicator value to enrich. Defaults to ${Email.Address}.


## Darkmon - VIP Email Monitor

**Type:** playbook  
**Product:** Darkmon  

Hourly poll of board-protected emails. For each protected email, checks accounts/combo-lists/public-breaches and opens a 'Darkmon VIP Email Leak' incident per new entry


## Darktrace Email Basic Email Handler

**Type:** playbook  
**Product:** Darktrace  

Runs a common Email workflow for fetch Darktrace Email incidents

**Inputs:**

- `Incident ID`: 


## Darktrace Email Update Incident Fields

**Type:** playbook  
**Product:** Darktrace  

Update all incident fields that may change over time

**Inputs:**

- `Incident ID`: 


## DarktraceEmail

**Type:** integration  
**Product:** Darktrace  

This pack includes configurations to combine the world-class threat detection of Darktrace with the synchrony and automation abilities of platform, allowing security teams to investigate critical incidents along with accompanying summaries and timelines. This integration was integrated and tested with version 6.2 of DarktraceEmail

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## DBot Create Phishing Classifier V2

**Type:** playbook  
**Product:** Machine Learning  

Creates a phishing classifier using machine learning technique, based on the email content

**Inputs:**

- `modelName`: The model name to store in the system.
- `emailTextKey`: The CSV list of incident fields names with the email body or html body. You can also use "
- `emailSubjectKey`: The CSV list of incident fields names with the email subject. You can also use "
- `emailTagKey`: The field name with the email tag. Supports a CSV list, the first non-empty value will be taken.
- `phishingLabels`: The CSV list of email tags values and mapping. The script considers only the tags specified in this field. You can map label to another valu
- `incidentsQuery`: The incidents query to fetch the training data for the model.
- `maxIncidentsToFetchOnTraining`: The maximum number of incidents to fetch.
- `hashSeed`: If non-empty, hash every word with this seed.


## DBot Create Phishing Classifier V2 Job

**Type:** playbook  
**Product:** Machine Learning  

Trains the phishing machine learning model. This playbook should be used as job, to run repeatedly, for example every week


## DBotBuildPhishingClassifier

**Type:** script  
**Product:** Base  

Create a phishing classifier using machine learning technique, based on email content

**Inputs:**

- `query`: Additional text by which to query incidents.
- `incidentTypes`: A comma-separated list of incident types by which to filter.
- `fromDate`: The start date by which to filter incidents. Date format will be the same as in the incidents query page (valid strings example: "3 days ago
- `toDate`: The end date by which to filter incidents. Date format will be the same as in the incidents query page (valid strings example: "3 days ago",
- `limit`: The maximum number of incidents to fetch.
- `includeContext`: Whether to query and fetch incident context.
- `timeField`: The incident field (created or modified) to specify for the date range.
- `tagField`: The field name with the label. Supports a comma-separated list, the first non-empty value will be taken.


## DBotPredictPhishingWords

**Type:** script  
**Product:** Base  

Predict text label using a pre-trained machine learning phishing model, and get the most important words used in the classification decision

**Inputs:**

- `modelName`: The model name (or list name) in platform.
- `hashSeed`: Seed for the hash function, at the pre-process stage.
- `emailSubject`: Subject of the email.
- `emailBody`: Body of the email.
- `emailBodyHTML`: HTML body of the email. Only use this field if the emailBody argument is empty.
- `topWordsLimit`: Maximum number of positive/negative words to return for the model decision. Default is 20.
- `wordThreshold`: Threshold to determine word importance (range 0-1). Default is 0.05.
- `modelStoreType`: How the model is stored in platform. Can be "list" or "mlModel". Default is "list".


## DBotPredictURLPhishing

**Type:** script  
**Product:** Phishing URL  

Predict phishing URLs using a pre-trained model

**Inputs:**

- `urls`: Space-separated list of URLs.
- `emailBody`: Body of the email for URL extraction.
- `emailHTML`: HTML of the email for URL extraction.
- `maxNumberOfURL`: Maximum number of extracted URLs on which to run the model.
- `forceModel`: Whether to force the model to run if the URL belongs to the whitelist. If True, the model will run in every case. If False, the model will r
- `resetModel`: Whether to reset the model to the model existing in Docker.
- `defaultRequestProtocol`: The protocol to use when calling the URLs. This argument effects the calls sent by the model only and has no effect on the rasterize or whoi
- `debug`: Whether to enter debug mode.


## DBotUpdateLogoURLPhishing

**Type:** script  
**Product:** Phishing URL  

Add, remove, or modify logos for the URL Phishing model to compare to suspicious websites

**Inputs:**

- `logoImageId`: "Entry ID" of the uploaded logo in the platform.
- `logoName`: Name of the logo. The name is the unique identifier for the logo.
- `associatedDomains`: Comma-separated list of domains that are associated to the logo defined in the logoName argument. It will only be used if the action argumen
- `action`: Action to execute on the model.


## Detect & Manage Phishing Campaigns

**Type:** playbook  
**Product:** Phishing Campaign  

This playbook is used to find, create and manage phishing campaigns. When a number of similar phishing incidents exist in the system, the playbook can be used to do the following

**Inputs:**

- `AutomaticallyLinkIncidents`: Whether to automatically link the incidents that make up the campaign, to the phishing campaign incident. Can be True (default) or False. It
- `incidentTypeFieldName`: The name of the incident field in which the incident type is stored. Default is "type". Change this argument only if you're using a custom f
- `incidentTypes`: A comma-separated list of incident types by which to filter. Specify "None" to search through all incident types By default, the value is "P
- `existingIncidentsLookback`: The date from which to search for similar incidents. Date format is the same as in the incidents query page. For example: "3 days ago", "201
- `query`: Additional text by which to query incidents to find similar Phishing incidents. Uses the same language to query incidents in the UI.
- `limit`: The maximum number of incidents to fetch. Determines how many incidents can be checked for similarity at the time of execution.
- `emailSubject`: The name of the incident field that contains the email subject. By default this is `emailsubject` (because the email subject is stored under
- `emailBody`: The name of the incident field that contains the email body.


## DLP - Get User Feedback via Email

**Type:** playbook  
**Product:** Enterprise DLP by Palo Alto Networks  

Get the user feedback via email on a blocked file, whether it is false or true positive and if an exemption is needed

**Inputs:**

- `UserDisplayName`: The display name of the user.
- `data_profile_name`: The name of the DLP data profile that detected the violation.
- `file_name`: The name of the file that triggered the incident.
- `question_type`: Whether to ask the user about the file content or about an exemption.
- `SendMailInstance`: The name of the instance to be used when executing the "send-mail" command in the playbook. In case it will be empty, all available instance
- `UserEmail`: The user email address.
- `Snippets`: The snippets of the violation.


## EDL Monitor- Email EDL content

**Type:** playbook  
**Product:** EDL Monitor  

You can use the playbook (or a cloned copy) with a job to check the EDL on a schedule


## Email Hippo

**Type:** integration  
**Product:** Email Hippo  

This is the Email Hippo integration used to verify email sources as fake emails that were used as part of phishing attacks. . This integration was integrated and tested with version 2.0.1551 of Email Hippo

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## EmailAskUser

**Type:** script  
**Product:** Common Scripts  

Asks a user a question via email and process the reply directly into the investigation

**Inputs:**

- `email`: The email of the user to ask.
- `subject`: The subject for the email.
- `message`: The message sent to the user you are going to ask.
- `option1`: The first option for a user reply.The default is "yes". Options cannot contain whitespaces.
- `option2`: The second option for the user reply. The default is "no". Options cannot contain whitespaces.
- `additionalOptions`: The comma delimited list of additional options if there are more than 2. Options cannot contain whitespaces.
- `task`: Which task the reply will close. If none, then no playbook tasks will be closed.
- `roles`: Send mail to all users of these roles (a CSV list).


## EmailAskUserResponse

**Type:** script  
**Product:** Common Scripts  

Extract a user's response from EmailAskUser reply. Returns the first textual response line of the provided entry that contains the reply body. Use ${lastCompletedTaskEntries} to analyze the previous playbook task containing the user's reply

**Inputs:**

- `responseEntryId`: The entry ID where EmailAskUser will complete when the user replies.
- `prefix`: Text to remove from the start of the answer. If the response contains a known prefix that should be removed, this argument should be used.
- `suffix`: Text to remove from the end of the answer. If the response contains a known suffix that should be removed, this argument should be used.


## EmailDomainSquattingReputation

**Type:** script  
**Product:** Common Scripts  

Checks if an email address's domain is trying to squat other domain using Levenshtein distance algorithm

**Inputs:**

- `email`: The email address to check.
- `domain`: The domain list to check against for squatting (comma separated).
- `threshold`: The similarity threshold.


## EmailDomainWhitelist

**Type:** script  
**Product:** Filters And Transformers  

Accepts an array of domains as an allow list, and a list of email addresses. The script then filters out any email address whose domain is not in the allow list. The filtered list will be returned as an array

**Inputs:**

- `value`: An array of email addresses to be filtered by domain.
- `domain_list`: An array of domains to allow list.


## emailFieldTriggered

**Type:** script  
**Product:** Common Scripts  

Sends an email to the incident owner when a selected field is triggered


## EmailRep.io

**Type:** integration  
**Product:** EmailRepIO  

EmailRep.io provides the reputation and reports for email addresses. This integration was integrated and tested with version EmailRep Alpha API v0.1 of EmailRep.io

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## EmailReputation

**Type:** script  
**Product:** Common Scripts  

A context script for email entities

**Inputs:**

- `email`: The email address to look up.


## ExtendQueryBasedOnPhishingLabels

**Type:** script  
**Product:** Machine Learning  

A helper script for the DBot Create Phishing Classifier V2 playbook. This script extends the query based on the phishingLabels argument

**Inputs:**

- `query`: Additional text by which to query incidents.
- `tagField`: The field name with the label. Supports a comma-separated list, the first non-empty value will be taken.
- `phishingLabels`: A comma-separated list of email tag values and mapping. The script considers only the tags specified in this field. You can map a label to a


## FireEye Email Security

**Type:** integration  
**Product:** FireEye Email Security (EX)  

FireEye Email Security (EX) series protects against breaches caused by advanced email attacks. This integration was integrated and tested with version 9.0.2.929543 of FireEye Email Security

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Get Email From Email Gateway - FireEye

**Type:** playbook  
**Product:** FireEye Email Security (EX)  

Retrieve a specified eml/msg file directly from FireEye Email Security or Central Management

**Inputs:**

- `MessageID`: The email UUID provided by FireEye.
- `EmailTimestamp`: The Timestamp of the email received.


## Get Email From Email Gateway - Mimecast

**Type:** playbook  
**Product:** Mimecast  

This playbook retrieves a specified EML/MSG file directly from Mimecast

**Inputs:**

- `MessageID`: The message ID provided by Mimecast.


## Get Original Email - EWS v2

**Type:** playbook  
**Product:** Microsoft Exchange On-Premise  

This v2 playbook retrieves the original email in a thread as an EML file (and not an email object as in the previous version) by using the EWS v2 or EWSO365 integration. It also reduces the number of tasks to perform the fetch action. Note: You must have the necessary eDiscovery permissions in the EWS integration to execute a global search

**Inputs:**

- `TargetMailbox`: The target mailbox to retrieve the EML file from.
- `MessageID`: The InReplyTo header in the forwarded email.


## Get Original Email - Gmail v2

**Type:** playbook  
**Product:** Gmail  

This v2 playbook uses the reporter email headers to retrieve the original email. This decreases the amount of the tasks needed to retrieve the original email. Use this playbook to retrieve the original email using Gmail integration, including headers and attachments. You must have the necessary permissions in your Gmail service to execute global search: Google Apps Domain-Wide Delegation of Authority

**Inputs:**

- `MessageID`: The original email message id to retrieve. Holds the value of the "Message-ID" header of the original email and not Gmail's internal ID of t
- `UserID`: The email address of the user for which to fetch the original email.


## Get Original Email - Microsoft Graph Mail

**Type:** playbook  
**Product:** Microsoft Graph Mail  

This playbook retrieves the original email using the Microsoft Graph Mail integration. Note: You must have the necessary permissions in the Microsoft Graph Mail integration as described in the message-get API and the user-list-messages API

**Inputs:**

- `UserID`: The email address of the reporting user.
- `MessageID`: The InReplyTo header in the forwarded email.
- `ThreadTopic`: The ThreadTopic header in the forwarded email.
- `PagesToPull`: The number of pages of emails to return (maximum is 10 emails per page).


## Gophish

**Type:** integration  
**Product:** Gophish  

Gophish is a powerful, open-source phishing framework that makes it easy to test your organization's exposure to phishing. For Free This integration was integrated and tested with version 0.11.0 of gophish

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## HtmlPhishingCheck

**Type:** script  
**Product:** Suspicious Domain Hunting  

## IncapGetDomainApproverEmail

**Type:** script  
**Product:** Imperva Incapsula  

Gets the list of email addresses that can be used when adding an SSL site

**Inputs:**

- `domain`: The domain name of the site. For example, www.example.com, hello.example.com, example.com


## IronscalesEmailFieldTrigger

**Type:** script  
**Product:** Ironscales  

Automatically changes email field when choosing a classification


## IsItPhishing

**Type:** integration  
**Product:** IsItPhishing  

Collaborative web service that provides validation on whether a URL is a phishing page or not by analyzing the content of the webpage

**Commands:**

- `None`: 


## LinkToPhishingCampaign

**Type:** script  
**Product:** Phishing  

Links a Phishing incident to its related Phishing Campaign incident


## Mimecast v2

**Type:** integration  
**Product:** Mimecast  

Use the Mimecast integration to manage email security, continuity, and archiving services

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## MimecastFindEmail

**Type:** script  
**Product:** Mimecast  

Searches all mailboxes to find an email, and returns the list of mailboxes where the email was found. "Yes" will be displayed if the mail was found anywhere or "No" if not

**Inputs:**

- `queryXml`: The query string XML for the search, using Mimecast Unified Search Experience (MUSE). For more on information click here. Using this will ov
- `text`: The search for this text in API messages.
- `dryRun`: Will not execute the query, but will just return the query string that was built.
- `date`: Searches the specific dates only.
- `dateFrom`: Searches emails from a specific date. In format 2015-09-21T23:00:00Z.
- `dateTo`: Searches emails up until a specific date. In format 2015-09-21T23:00:00Z.
- `sentTo`: The filter on the messages to a specific address.
- `sentFrom`: The filter on the messages from a specific address.


## NexposeEmailParser

**Type:** script  
**Product:** Rapid7 InsightVM  

Parses the Nexpose report into a clear table that contains risk scores and vulnerability counts for each server, and creates a new incident for each server

**Inputs:**

- `entryID`: The ID of the entry containing the Nexpose report. If none is provided, the script will iterate and find a relevant entry.
- `minRiskScore`: The Minimal Risk Score an item in the report needs to reach in order to trigger an incident. Leave this field empty to trigger for any risk 
- `minVulnCount`: The Minimal Vulnerability Count an item in the report needs to reach in order to trigger an incident. Leave this field empty to trigger for 
- `defaultNexposeSeverity`: The severity to be set on the triggered incidents.


## NumberOfPhishingAttemptPerUser

**Type:** script  
**Product:** Common Scripts  

Shows a bar chart of the number of incident the 'To' and 'From' email addresses. This automation runs using the default Limited User role, unless you explicitly change the permissions. For more information, see the section about permissions here: For the platform, see the  for the platform, see the  for the platform, see the


## OpenPhish v2

**Type:** integration  
**Product:** OpenPhish  

OpenPhish uses proprietary Artificial Intelligence algorithms to automatically identify zero-day phishing sites and provide comprehensive, actionable, real-time threat intelligence

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## PhishER

**Type:** integration  
**Product:** PhishER  

KnowBe4 PhishER integration allows to pull events from PhishER system and do mutations. This integration was integrated and tested with version 6.0.0 of platform

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## Phishing - Handle Microsoft 365 Defender Results

**Type:** playbook  
**Product:** Phishing  

This playbook is used to handle the results from the "Microsoft 365 Defender - Threat Hunting Generic" playbook inside a phishing incident. It will do the following actions: 1) Set the relevant incident fields based on the results, such as "Clicked URLs", "Malicious URL Viewed" and "Malicious URL Clicked". 2) In case the relevant playbook inputs were configured, it will create new incidents for each email returned in the results. First, it will try to retrieve the original emails' files and then it will create an incident for each retrieved email. 3) Link the newly created incidents to the main originating incident. Note that this playbook should only be used inside a phishing incident and not as a main playbook

**Inputs:**

- `RetrievedEmails`: Emails retrieved by the "Microsoft 365 Defender - Threat Hunting Generic" playbook.
- `CreateNewIncidents`: When "True", the playbook will create new phishing incidents for each email that contains one of the malicious indicators. Default is "False
- `EmailBrand`: In order to retrieve email files in case any emails containing malicious indicators were found, this playbook would run the "Phishing - Get 


## Phishing - Search Related Incidents (Defender 365)

**Type:** playbook  
**Product:** Phishing  

This playbook should only be used as a sub-playbook inside the "Phishing - Handle Microsoft 365 Defender Results" playbook. It searches through existing the platform

**Inputs:**

- `RetrievedEmails`: Emails retrieved by the "Microsoft 365 Defender - Threat Hunting Generic" playbook.


## Phishing Alerts - Check Severity

**Type:** playbook  
**Product:** PhishingAlerts  

This playbook calculates and assigns the incident severity based on the highest returned severity level from the following calculations

**Inputs:**

- `Role`: The default role to assign the incident to.
- `escalationRole`: The higher tier role to assign the incident to.
- `OnCall`: Set to True to assign only to analysts on the current shift.
- `AuthenticityCheck`: Indicates the email authenticity resulting from the EmailAuthenticityCheck script. Possible values are: Pass, Fail, Suspicious, and Undeterm
- `MicrosoftHeadersSeverityCheck`: This value is set by the "Process Microsoft's Anti-Spam Headers" playbook, which calculates the severity after processing the PCL, BCL and P
- `SOCEmailAddress`: The SOC email address to set if the playbook handles an email security alert.
- `EmailTo`: The email recipient.
- `blockedAlertActionValue`: A comma-separated list of optional values the email security device returns for blocked\denied\etc. emails.


## PhishLabs - Populate Indicators

**Type:** playbook  
**Product:** PhishLabs  

Populates indicators from PhishLabs, according to a defined period of time

**Inputs:**

- `Since`: Get indicators within this duration (from now).
- `Limit`: The maximum number of indicators.
- `Remove protocol`: Removes the protocol part from indicators, when the rule can be applied.
- `Remove query`: Removes the query string part from indicators, when the rules can be applied.
- `Indicator type`: The filter of the indicators by indicator type.


## PhishLabs - Whitelist false positives

**Type:** playbook  
**Product:** PhishLabs  

Adds indicators from PhishLabs that were classified as false positives to allow list, according to a defined period of time

**Inputs:**

- `Since`: The allow list indicators within this duration (from now).


## PhishTank v2

**Type:** integration  
**Product:** PhishTank  

PhishTank is a free community site where anyone can submit, verify, track and share phishing data. This integration was integrated and tested with version 1.0.1 of PhishTank

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 


## PhishUp

**Type:** integration  
**Product:** PhishUp  

If you don't have PhishUp Api Key please create an account on PhishUp and get a free Api Key. Also you can visit and test PhishUp Web Demo. If you have any question feel free to concat us: info@phishup.com

**Commands:**

- `None`: 


## Process Email - EWS

**Type:** playbook  
**Product:** Microsoft Exchange On-Premise  

Processes an EWS email

**Inputs:**

- `EmailID`: The EWS Email ID.


## Proofpoint Isolation

**Type:** integration  
**Product:** Proofpoint Isolation  

Proofpoint Isolation is an integration that supports fetching Browser and Email Isolation logs events within Cortex XSIAM. This integration was integrated and tested with version V2 of ProofpointIsolation

**Commands:**

- `None`: 


## Proofpoint TAP v2

**Type:** integration  
**Product:** Proofpoint TAP  

Use the Proofpoint Targeted Attack Protection (TAP) integration to protect against and provide additional visibility into phishing and other malicious email attacks. This integration was integrated and tested with version v2 of Proofpoint TAP v2

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## ProofpointTAPMostAttackedUsers

**Type:** script  
**Product:** Proofpoint TAP  

Exports a list of Proofpoint TAP most attacked users to the the platform


## ProofpointTapTopClickers

**Type:** script  
**Product:** Proofpoint TAP  

Exports a list of Proofpoint TAP top clickers to the the platform


## Retrieve Email Data - Agari Phishing Defense

**Type:** playbook  
**Product:** Agari Phishing Defense  

Retrieve Email Data from one of the Integrations of Gmail, Mail Listener v2, EWS O365, Microsoft Graph Mail

**Inputs:**

- `Message Id`: Message Id of email.
- `User Id`: User Id of user.


## RiskIQPassiveTotalSSLForIssuerEmailWidgetScript

**Type:** script  
**Product:** PassiveTotal  

Set widgets to custom layout in Email and RiskIQAsset type of indicators


## RiskIQPassiveTotalSSLForSubjectEmailWidgetScript

**Type:** script  
**Product:** PassiveTotal  

Set widgets to custom layout in Email and RiskIQAsset type of indicators


## SSLVerifierV2_GenerateEmailBody

**Type:** script  
**Product:** SSL Certificates  

Generates the HTML needed for a formatted email to be sent using the outputs of !SSLVerifierV2, as part of the SSLVerifierV2 content pack


## Symantec Email Security Cloud

**Type:** integration  
**Product:** SymantecEmailSecurity  

Symantec Email Security.cloud is a hosted service that filters email messages and helps protect organizations from malware (including targeted attacks and phishing), spam, and unwanted bulk email. The service offers encryption and data protection options to help control sensitive information sent by email and supports multiple mailbox types from various vendors. This integration was integrated and tested with version 10.6.6 of Symantec Email Security Cloud

**Commands:**

- `None`: 
- `None`: 
- `None`: 


## Trustwave Secure Email Gateway

**Type:** integration  
**Product:** TrustwaveSEG  

Trustwave SEG is a secure messaging solution that protects businesses and users from email-borne threats, including phishing, blended threats, and spam. Trustwave Secure Email Gateway also delivers improved policy enforcement and data leakage prevention. This integration was integrated and tested with version 10 of trustwave secure email gateway

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## VectraXDRGenerateMailBody

**Type:** script  
**Product:** Vectra XDR  

Generate an email body based on the detection assessment for MDR escalation process

**Inputs:**

- `body_content`: Please provide the content needed to generate the email body.

