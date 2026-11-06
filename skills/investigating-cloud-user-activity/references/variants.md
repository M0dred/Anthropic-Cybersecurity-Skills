# Vendor Variants - Investigating Cloud User Activity

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## AWS - User Investigation

**Product:** AWS Enrichment and Remediation

This playbook performs an investigation on a specific user in AWS environments, using queries and logs from AWS CloudTrail to locate the following activities performed by the user

**Inputs:**

- `Username`: The username to investigate. Please enter the user's email.
- `AwsTimeSearchFrom`: The Search Time for the `GetTime` task used by the AWS Cloud Trail search query. This value represents the number of days to include in the search.Default value: 1. (1 Day)

**Outputs:**

- `AwsMFAConfigCount`
- `AwsUserRoleChangesCount`
- `AwsSuspiciousActivitiesCount`
- `AwsScriptBasedUserAgentCount`
- `AwsAccessKeyActivitiesCount`
- `AwsSecurityChangesCount`
- `AwsAdminActivitiesCount`
- `AwsApiAccessDeniedCount`
- `AwsFailedLogonCount`

**Dependencies:**

- Scripts: Set, LoadJSON, GetTime


## AWS IAM - User enrichment

**Product:** AWS - IAM

Enrich AWS IAM user information from AWS Identity and Access Management

**Inputs:**

- `username`: Name of the AWS IAM user to enrich.

**Dependencies:**

- Integrations: AWS - IAM
- Commands: aws-iam-get-user, aws-iam-list-access-keys-for-user


## Azure - User Investigation

**Product:** Azure Enrichment and Remediation

This playbook performs an investigation on a specific user in Azure environments, using queries and logs from Azure Log Analytics to locate the following activities performed by the user

**Inputs:**

- `Username`: The username to investigate.
- `AzureSearchTime`: The Search Time for the Azure Log Analytics search query. Default value: ago(1d)
- `failedLogonThreshold`: The threshold number of failed logons by the user. Required to determine how many failed logon events count as suspicious events.
- `MfaAttemptThreshold`: The threshold number of MFA failed logons by the user. Required to determine how many MFA failed logon events count as suspicious events.

**Outputs:**

- `AzureScriptBasedUserAgentEvents`
- `CountAzureEvents.AzureScriptBasedUserAgentCount`
- `AzureAdminActivitiesEvents`
- `CountAzureEvents.AzureAdminActivitiesCount`
- `AzureSecurityRulesChangeEvents`
- `CountAzureEvents.AzureSecurityRulesChangeCount`
- `AzureUnsuccessSecurityRulesChangeEvents`
- `CountAzureEvents.AzureUnsuccessSecurityRulesChangeCount`
- `AzureFailLoginCount`
- `AzureFailLoginMFACount`

**Dependencies:**

- Scripts: SetAndHandleEmpty, SetMultipleValues


## GCP - User Investigation

**Product:** GCP Enrichment and Remediation

This playbook performs an investigation on a specific user in GCP environments, using queries and logs from G Suite Auditor, and GCP Logging to locate the following activities performed by the user

**Inputs:**

- `Username`: The username to investigate.
- `GcpProjectName`: The GCP project name. This is a mandatory field for GCP queries.
- `GcpTimeSearchFrom`: The Search Time for the `GetTime` task used by the GCP Logging search query. This value represents the number of days to include in the search.Default value: 1. (1 Day)

**Outputs:**

- `GcpAnomalousNetworkTraffic`
- `GcpSuspiciousApiUsage`
- `GcpFailLogonCount`
- `GsuiteFailLogonCount`
- `GsuiteUnusualLoginAllowedCount`
- `GsuiteUnusualLoginBlockedCount`
- `GsuiteSuspiciousLoginCount`
- `GsuiteUserPasswordLeaked`

**Dependencies:**

- Scripts: GetTime, Set
- Commands: gsuite-activity-search, gcp-logging-log-entries-list


## Okta - User Investigation

**Product:** Okta

This playbook performs an investigation on a specific user, using queries and logs from Okta

**Inputs:**

- `UserEmail`: The user email to search Okta logs.
- `LoginCountry`: The Country code from which the user logged in.Country Code Alpha 2 (Example: US)
- `ASN`: The ASN from which the user logged in.

**Outputs:**

- `PermanentCountry`
- `UserDevices`
- `NumOfOktaSuspiciousActivities`
- `SuspiciousUserActivities`
- `NumOfOktaSuspiciousUserAgent`
- `SuspiciousUserAgent`
- `UserApplication`
- `NumOfOktaFailedLogon`
- `NumOfFailedLogonASN`
- `LogonCountries`

**Dependencies:**

- Integrations: Okta v2
- Scripts: CountArraySize, Set, GetTime
- Commands: okta-get-logs


## User Investigation - Generic

**Product:** Common Playbooks

This playbook performs an investigation on a specific user, using queries and logs from SIEM, Identity management systems, XDR, and firewalls. Supported Integrations: -Okta -Splunk -QRadar -Azure Log Analytics -PAN-OS -XDR / Core By Palo Alto Networks

**Inputs:**

- `SplunkIndex`: Splunk's index name in which to search. Default is "*" - All.
- `SplunkEarliestTime`: The earliest time for the Splunk search query.
- `SplunkLatestTime`: The latest time for the Splunk search query.
- `UserEmail`: The user email to search Okta logs.
- `Username`: User name.
- `LoginCountry`: The Country from which the user logged in.
- `SIEMFailedLogonSearch`: Whether to search for failed logon logs from Siem? Can be False or True.
- `ThreatLogSearch`: Whether to search for threat logs from PAN-OS? Can be False or True.
- `XDRAlertSearch`: Whether to search for Related alerts from XDR? Can be False or True.
- `OktaSearch`: Whether to search for logs from Okta? Can be False or True.

**Outputs:**

- `NumOfSiemFailedLogon`
- `NumOfThreatLogs`
- `PaloAltoNetworksXDR.Alert`
- `ArraySize`
- `PermanentCountry`
- `UserDevices`
- `NumOfOktaSuspiciousActivities`
- `SuspiciousUserActivities`
- `NumOfOktaSuspiciousUserAgent`
- `SuspiciousUserAgent`

**Dependencies:**

- Sub-playbooks: Get entity alerts by MITRE tactics, Okta - User Investigation, SIEM - Search for Failed logins, Cortex XDR - Get entity alerts by MITRE tactics
- Scripts: Set, CountArraySize, SetAndHandleEmpty, MathUtil
- Commands: pan-os-query-logs, pan-os-get-logs

