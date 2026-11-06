# Vendor Variants - Remediating Exposure Issues

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Agari Message Remediation - Agari Phishing Defense

**Product:** Agari Phishing Defense

Investigates Agari policy events by obtaining the original message and attachments from the existing email integrations and remediates in Agari. Supported   versions: 5.0.0 and later

**Inputs:**

- `APD Global Message ID`: Global Message Id obtained from the incident.
- `AuthenticateEmail`: Whether the authenticity of the email should be verified, using Authenticity Score.
- `OnCall`: Set to true to assign only user that is currently on shift. Requires the platform.5 or later.
- `Role`: The default role to assign the incident to.
- `ResolveIP`: Resolve IP addresses to hostnames (DNS).
- `AutoRemeditaion`: Whether Automatic remediate message or not.
- `RemediateAction`: Default action for remediation of message.
- `UserEnrichmentEnable`: Flag for enabling User Enrichment.
- `User Id`: Id of User.
- `APD Internal Message ID`: Internal Message Id obtained from the incident.

**Dependencies:**

- Sub-playbooks: Entity Enrichment - Phishing v2, Extract Indicators From File - Generic v2, Email Address Enrichment - Generic v2.1, Retrieve Email Data - Agari Phishing Defense, Calculate Severity - Generic v2, Process Email - Generic, Remediate Message - Agari Phishing Defense, Detonate File - Generic
- Scripts: AssignAnalystToIncident, Set, CheckEmailAuthenticity
- Commands: closeInvestigation, setIncident


## AWS - EC2 Instance Security Group Remediation

**Product:** Cloud Security Policy Management

This playbook identifies the security groups used on an EC2 interface with a specific public IP. It determines which rules allow access via the given port and protocol, creates a copy of the security groups with those rules removed, and updates the interface to use the modified security groups. The original security groups are left unmodified, and the remediated copy is applied to the exposed EC2 instance

**Inputs:**

- `AssetID`: The asset ID of the VM Instance.
- `PublicIP`: The public IP address to remediate for public exposure.
- `RemotePort`: The TCP/UDP port number to be restricted.
- `RemoteProtocol`: The protocol to be restricted (tcp/udp).
- `RemediationAllowRanges`: A comma-separated list of IPv4 network ranges to be used as source addresses for the `cortex-remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically these are priva
- `IntegrationInstance`: The AWS integration instance to use if multiple instances are configured (optional).

**Outputs:**

- `remediatedFlag`
- `remediation_action`

**Dependencies:**

- Integrations: AWS, Cortex Core - Platform
- Scripts: AWSIdentifySGPublicExposure, AWSRemediateSG, GetTime, Print, Set
- Commands: aws-ec2-network-interface-attribute-modify, core-get-asset-details


## AWS - Security Group Remediation v2

**Product:** AWS Enrichment and Remediation

This playbook takes in some information about an EC2 instance (ID and public_ip) and with provided port and protocol, determines what security groups on the primary interface of an EC2 instance are over-permissive. It uses an automation to determine what interface on an EC2 instance has an over-permissive security group on, determine which security groups have over-permissive rules and to replace them with a copy of the security group that has only the over-permissive portion removed. Over-permissive is defined as sensitive ports (SSH, RDP, etc) being exposed to the internet via IPv4

**Inputs:**

- `InstanceID`: ID of the AWS EC2 instance.
- `Port`: TCP/UDP port to be restricted.
- `Protocol`: Protocol of the port to be restricted.
- `PublicIP`: Public IP address of the EC2 instance.
- `AWSAssumeArn`: Name of an AWS role to assume (should be the same for all organizations).
- `Region`: Region where EC2 instance is present.

**Dependencies:**

- Scripts: AWSRecreateSG


## AWS - Unclaimed S3 Bucket Remediation

**Product:** AWS Enrichment and Remediation

The playbook will create the unclaimed S3 bucket

**Inputs:**

- `S3BucketName`: Unclaimed S3 bucket name.

**Dependencies:**

- Integrations: AWS - S3
- Commands: aws-s3-list-buckets, aws-s3-create-bucket


## AWS Network Exposure - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

This playbook remediates the following AWS Network Exposure detections

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Outputs:**

- `remediatedFlag`

**Dependencies:**

- Sub-playbooks: AWS - EC2 Instance Security Group Remediation, Notify Stakeholders
- Integrations: Cortex Core - Platform
- Scripts: Print
- Commands: core-get-issue-recommendations, setIssueStatus


## AWS Public Access Misconfiguration - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates 9 AWS public access misconfigurations: 1 RDS database, 1 EBS snapshot, and 7 S3 bucket issues: The playbook disables public access by modifying RDS publicly_accessible settings, removing EBS snapshot createVolumePermission, and enabling S3 PublicAccessBlockConfiguration respectively. Optional stakeholder notification is available via the "Notify Stakeholders" sub-playbook by setting enableNotifications input to 'yes' (default: 'no'). When enabled, configure at least one recipient (email, Slack channel, or Teams channel) in the Notify Stakeholders playbook inputs. The playbook automatically updates the issue status to "Resolved - Fixed" upon successful remediation

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: Notify Stakeholders
- Integrations: AWS, Cortex Core - Platform
- Scripts: Print, Set
- Commands: aws-ec2-snapshot-attribute-modify, aws-rds-db-instance-modify, aws-s3-public-access-block-update, core-get-asset-details, setIssueStatus


## Azure - Network Security Group Remediation

**Product:** Azure Enrichment and Remediation

This playbook adds new Azure Network Security Groups (NSG) rules to NSGs attached to a NIC. The new rules will give access only to a private IP address range and block traffic that's exposed to the public internet (using the private IP of the VM as stated in Azure documentation). For example, if RDP is exposed to the public internet, this playbook adds new firewall rules that only allow traffic from private IP addresses and blocks the rest of the RDP traffic. Conditions and limitations

**Inputs:**

- `AzureSecurityGroup`: The Azure Network Security Group that will have new rules created or updated.
- `AzureVMPrivateIP`: The private IP of the Azure Virtual Machine.
- `RemoteProtocol`: The remote protocol that is publicly exposed.
- `RemotePort`: The remote port that is publicly exposed.
- `SubscriptionID`: The Azure subscription ID (optional).
- `ResourceGroup`: The Azure resource group (optional).
- `InstanceName`: Azure Network Security Groups integration instance to use if you have multiple instances configured (optional).
- `RemediationAllowRanges`: Comma-separated list of IPv4 network ranges to be used as source addresses for the `remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically this will be private IP 

**Outputs:**

- `remediatedFlag`
- `remediatedReason`

**Dependencies:**

- Integrations: Azure Network Security Groups
- Scripts: Set, AzureFindAvailableNSGPriorities
- Commands: azure-nsg-security-rule-update, azure-nsg-security-rule-create, azure-nsg-security-rules-list


## Azure - VM Instance Network Security Group Remediation

**Product:** Cloud Security Policy Management

This playbook adds new Azure Network Security Group (NSG) rules to NSGs attached to a NIC. The new rules give access to only a private IP address range and block traffic exposed to the public internet using the private IP of the VM, as explained in the (Azure documentation). For example, if RDP is exposed to the public internet, this playbook adds new firewall rules that only allow traffic from private IP addresses and blocks the rest of the RDP traffic. Conditions and limitations

**Inputs:**

- `AssetID`: The asset ID of the VM Instance.
- `PublicIP`: The public IP address to remediate for public exposure.
- `RemoteProtocol`: The remote protocol that is publicly exposed.
- `RemotePort`: The remote port that is publicly exposed.
- `IntegrationInstance`: The Azure Network Security Groups integration instance to use if you have multiple instances configured (optional).
- `RemediationAllowRanges`: A comma-separated list of IPv4 network ranges to be used as source addresses for the `cortex-remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically these are priva

**Outputs:**

- `remediatedFlag`
- `remediation_action`

**Dependencies:**

- Integrations: Azure, Cortex Core - Platform
- Scripts: AzureIdentifyNSGExposureRule, Print, Set, SetAndHandleEmpty
- Commands: azure-vn-network-interface-get, azure-vn-public-ip-address-get, azure-vn-security-rule-create, azure-vn-security-rule-update, azure-vn-security-rules-list, core-get-asset-details


## Azure Network Exposure - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

This playbook remediates the following Azure Network Exposure detections

**Inputs:**

- `enableNotifications`: Options: yes/no Choose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify 

**Dependencies:**

- Sub-playbooks: Azure - Network Security Group Remediation v2, Notify Stakeholders
- Integrations: Cortex Core - Platform
- Scripts: Print
- Commands: core-get-issue-recommendations, setIssueStatus


## Azure Public Access Misconfiguration - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates 3 Azure public access misconfigurations: The playbook disables public access by setting allowBlobPublicAccess to false, configuring VM disk publicNetworkAccess to Disabled with a DenyAll policy, and updating the storage account default network access action to Deny. Optional stakeholder notification is available via the "Notify Stakeholders" sub-playbook by setting enableNotifications input to 'yes' (default: 'no'). When enabled, configure at least one recipient (email, Slack channel, or Teams channel) in the Notify Stakeholders playbook inputs. The playbook automatically updates the issue status to "Resolved - Fixed" upon successful remediation

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: Notify Stakeholders
- Integrations: Azure, Cortex Core - Platform
- Scripts: Print, Set
- Commands: azure-compute-disk-update, azure-storage-account-update, core-get-asset-details, setIssueStatus


## ChronicleAssets Investigation And Remediation - Chronicle

**Product:** Google SecOps

Performs enrichment and investigation of the ChronicleAsset type of indicators, provides an opportunity to remediate in case any of the ChronicleAsset information i.e., hostname or IP address is found to be malicious or suspicious, and sends out an email containing the list of isolated and potentially blocked entities. To select the indicators you want to add, go to playbook inputs, choose "from indicators" and set your query. For example, type:ChronicleAsset etc. The default playbook query is "type:ChronicleAsset". In case indicators with different query parameters are to be investigated, the query must be edited accordingly. This playbook needs to be used with caution as it might use up the integration’s API license when running large amounts of indicators

**Inputs:**

- `Indicator Query`: Indicators matching the indicator query will be used as playbook inputs.
- `chronicleasset_support_contact`: The support email address for the Chronicle asset.
- `auto_block_entities`: Autoblock the detected suspicious IP address(es). You can manuall set this as 'Yes' or 'No' here or you can set it in a 'Chronicle Auto Block Entities' custom incident field.
- `skip_entity_isolation`: Skip the isolation of entities. You can manually set this as 'Yes' or 'No' here or you can set it in a 'Chronicle Skip Entity Isolation' custom incident field.


## Commvault Suspicious File Activity Remediation

**Product:** Commvault Cloud

Playbook to disable data-aging on commvault client when a threat is detected

**Dependencies:**

- Integrations: CommvaultSecurityIQ
- Scripts: AssignAnalystToIncident
- Commands: closeInvestigation, setIncident, disable-data-aging


## Cortex ASM - Cortex Endpoint Remediation

**Product:** Cortex Attack Surface Management

This playbook is used to isolate a single  Endpoint (XSIAM/XDR) for remediation purposes

**Inputs:**

- `CortexEndpointID`: The ID of the Cortex Endpoint (XDR).

**Dependencies:**

- Integrations: Cortex Core - IR, Cortex XDR - IR
- Scripts: Set
- Commands: xdr-endpoint-isolate, core-isolate-endpoint


## Cortex ASM - On Prem Remediation

**Product:** Cortex Attack Surface Management

This playbook adds new block rule(s) to on-prem firewall vendors in order to block internet access for internet exposures. Conditions

**Inputs:**

- `RuleName`: Firewall rule name to look up in the company configuration setting for block rule.
- `RemoteIP`: IP address of the service.
- `RemoteProtocol`: Protocol of the service.
- `RemotePort`: Port number of the service.
- `DeviceGroup`: Device group of the firewall rule to lookup.
- `SecondaryDeviceGroup`: If the rule, address and service are created in the "Shared" location, we need to know what device-groups we can push to because it isn't possible to push to the "Shared" location.

**Dependencies:**

- Sub-playbooks: PAN-OS - Block Destination Service
- Integrations: Panorama
- Commands: pan-os-list-rules


## Cortex ASM - Remediation Confirmation Scan

**Product:** Cortex Attack Surface Management

This playbook handles ASM Remediation Confirmation Scan by first creating a scan for an existing service ID, if the scan does not already exist. It then polls for results of a successful or failed scan

**Dependencies:**

- Scripts: GridFieldSetup, GetTime
- Commands: asm-get-remediation-confirmation-scan-status, asm-start-remediation_confirmation_scan


## Cortex ASM - Remediation Guidance

**Product:** Cortex Attack Surface Management

This playbook pulls remediation guidance off of a list based on ASM RuleID to be used in service owner notifications (email or ticketing system)

**Inputs:**

- `IssueTypeID`: Attack surface management issue rule ID.

**Outputs:**

- `RemediationGuidance`

**Dependencies:**

- Commands: asm-get-attack-surface-rule, setAlert


## Cortex ASM - Remediation Objectives

**Product:** Cortex Attack Surface Management

Playbook that populates the remediation objectives field that is used to display the remediation actions to the end user

**Dependencies:**

- Scripts: Set, GridFieldSetup


## Cortex ASM - Remediation Path Rules

**Product:** Cortex Attack Surface Management

This playbook returns "RemediationAction" options based on the return from the Remediation Path Rules API, or defaults to data collection task

**Inputs:**

- `ExternallyDetectedProviders`: Providers of external service.
- `BypassDevCheck`: Determine whether to bypass the Dev Check in automated remediation criteria: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-Expander-User-Guide/Automated-Re

**Outputs:**

- `RemediationAction`
- `RPR_Timestamp`

**Dependencies:**

- Integrations: CortexAttackSurfaceManagement
- Scripts: GetTime, GridFieldSetup, Set, RemediationPathRuleEvaluation
- Commands: asm-list-remediation-rule


## Cortex ASM - Remediation

**Product:** Cortex Attack Surface Management

This playbook contains all the cloud provider sub playbooks for remediation

**Inputs:**

- `AWSAssumeRoleName`: If assuming roles for AWS, this is the name of the role to assume (should be the same for all organizations)

**Dependencies:**

- Sub-playbooks: AWS - Package Upgrade, AWS - Security Group Remediation v2, AWS - Unclaimed S3 Bucket Remediation, Azure - Network Security Group Remediation, Cortex ASM - Cortex Endpoint Remediation, Cortex ASM - On Prem Remediation, GCP - Firewall Remediation


## Cortex EM - Remediation

**Product:** Cortex Exposure Management

This playbook handles exposure issue remediation

**Inputs:**

- `AWSAssumeRoleName`: The name of the role to assume for AWS (should be the same for all organizations).

**Dependencies:**

- Sub-playbooks: AWS - Enrichment, AWS - Security Group Remediation v2, Cortex EM - Exposure Issue


## DSPM Multi-Cloud Risk Remediation

**Product:** DSPM

The playbook ensures efficient incident resolution and compliance with security policies by guiding the user through decision points based on incident type, such as empty storage assets or assets open to the world. It concludes by updating the incident status and closing the playbook upon resolution

**Inputs:**

- `defaultSlackUserName`: In the event that the risk asset tag is absent, the risk notice will be sent to this Slack user email address.
- `slackMessageLifetime`: Lifetime for slack notification (in seconds)
- `rerunTime`: Incident re-run time (in hours)

**Dependencies:**

- Sub-playbooks: DSPM Valid User Response, Send slack notificaton to user, Invalid response sending notification to user again, DSPM notify user in case of error
- Scripts: DSPMCreateSimpleSlackMessageBlock, DSPMCheckAndSetErrorEntries, IsIntegrationAvailable, DSPMIncidentList, DSPMExtractRiskDetails, DeleteContext, DSPMCreateRiskSlackBlocks, isError
- Commands: createList, setList, getList, addToList, closeInvestigation, core-api-post


## DSPM Remediation for Empty storage asset

**Product:** DSPM

This playbook is designed to remediate risks associated with empty storage assets across AWS, Azure, and GCP environments. It identifies the cloud provider for the asset and proceeds to delete the storage container or bucket accordingly. Additionally, it sends notifications via Slack to inform stakeholders about the status of the remediation process

**Dependencies:**

- Integrations: AWS - S3, DSPM, Google Cloud Storage
- Scripts: IsIntegrationAvailable, DSPMIncidentList, DSPMCheckAndSetErrorEntries, DeleteContext, DSPMCreateSimpleSlackMessageBlock
- Commands: aws-s3-delete-bucket, dspm-update-risk-finding-status, gcs-delete-bucket, setList


## DSPM Remediation for Sensitive asset open to world

**Product:** DSPM

The DSPM Remediation Playbook for Sensitive Asset Open to World is designed to handle incidents where sensitive assets are exposed to the public, with specific focus on remediating this vulnerability across different cloud providers (AWS). Below is an overview of the key steps and actions included in this playbook

**Dependencies:**

- Integrations: DSPM, Google Cloud Storage, AWS - S3, Azure Storage Container
- Scripts: DSPMIncidentList, DSPMCreateSimpleSlackMessageBlock, DSPMCheckAndSetErrorEntries, DeleteContext, DSPMGetContianers, IsIntegrationAvailable
- Commands: dspm-update-risk-finding-status, setList, aws-s3-put-public-access-block, gcs-block-public-access-bucket, azure-storage-container-block-public-access, dspm-get-asset-files-by-id


## ETD Email Reclassification And Remediation

**Product:** ETD the platform Connector

Allows analysts to review Cisco ETD emails, reclassify message verdicts, and perform remediation actions

**Dependencies:**

- Integrations: ETDConnector
- Scripts: IsIntegrationAvailable, Print
- Commands: cisco-etd-move-message


## GCP - Firewall Remediation

**Product:** GCP Enrichment and Remediation

This playbook adds new firewall rules with access only from private ip address range and blocks traffic that's exposed to public internet. For example, if RDP is exposed to the entire world, this playbook adds new firewall rules that only allows traffic from private ip address and blocks rest of the RDP traffic

**Inputs:**

- `GcpInstance`: The name of the GCP instance that has the public ip.
- `GcpZone`: The zone of the GCP instance that is hosted in.
- `GcpNetwork`: The VPC network of the GCP instance.
- `RemotePort`: The remote port that is publicly exposed to.
- `RemoteProtocol`: The remote protocol that is publicly exposed to.
- `GcpProject`: The name of the GCP project associated with the instance and related objects.
- `instance_name`: Google Cloud Compute integration instance to use if you have multiple instances configured (optional).

**Dependencies:**

- Integrations: Google Cloud Compute
- Scripts: Set
- Commands: gcp-compute-list-firewall, gcp-compute-insert-firewall, gcp-compute-add-network-tag, gcp-compute-get-instance


## GCP - VM Instance Firewall Rule Remediation

**Product:** Cloud Security Policy Management

This playbook adds new VPC firewall rules to restrict access to private IP address ranges and block traffic exposed to the public internet. For example, if RDP is exposed this playbook adds new firewall rules that allow traffic only from private IP addresses and it blocks all other RDP traffic. New allow and block rules created by this playbook target only the exposed asset

**Inputs:**

- `AssetID`: The asset ID of the VM instance.
- `RemotePort`: The remote port that is publicly exposed.
- `RemoteProtocol`: The remote protocol that is publicly exposed.
- `IntegrationInstance`: The GCP integration instance to use if multiple instances are configured (optional).
- `RemediationAllowRanges`: A comma-separated list of IPv4 network ranges to be used as source addresses for the `cortex-remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically these are priva

**Outputs:**

- `remediatedFlag`
- `remediation_action`

**Dependencies:**

- Integrations: Cortex Core - Platform, GCP
- Scripts: Print, Set
- Commands: core-get-asset-details, gcp-compute-firewall-insert, gcp-compute-firewall-list, gcp-compute-instance-get, gcp-compute-network-tag-set


## GCP Network Exposure - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates the following Network Exposure detection

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: GCP - VM Instance Firewall Rule Remediation, Notify Stakeholders
- Integrations: Cortex Core - Platform
- Scripts: Print
- Commands: core-get-issue-recommendations, setIssueStatus


## GCP Public Access Misconfiguration - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates 2 GCP public access misconfigurations: The playbook removes public IAM policy bindings by deleting 'allUsers' and 'allAuthenticatedUsers' entities from the bucket's Access Control List respectively. Optional stakeholder notification is available via the "Notify Stakeholders" sub-playbook by setting enableNotifications input to 'yes' (default: 'no'). When enabled, configure at least one recipient (email, Slack channel, or Teams channel) in the Notify Stakeholders playbook inputs. The playbook automatically updates the issue status to "Resolved - Fixed" upon successful remediation

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: Notify Stakeholders
- Integrations: Cortex Core - Platform, GCP
- Scripts: Print, Set
- Commands: core-get-asset-details, gcp-storage-bucket-policy-delete, setIssueStatus


## Hostname And IP Address Investigation And Remediation - Chronicle

**Product:** Google SecOps

This playbook receives ChronicleAsset type of indicators from its parent playbook "ChronicleAsset Investigation - Chronicle", performs enrichment and investigation for each one of them, provides an opportunity to isolate and block the hostname or IP address associated with the current indicator, and provides a list of isolated and blocked entities

**Inputs:**

- `chronicleasset_value`: The value of the ChronicleAsset indicator.
- `chronicleasset_hostname`: The hostname associated with the ChronicleAsset.
- `chronicleasset_ip`: The IP address associated with the ChronicleAsset.
- `chronicleasset_support_contact`: The support email address for the ChronicleAsset.
- `auto_block_entities`: Autoblock the detected suspicious IP Address(es). You can manually set this as "Yes" or "No" here or you can set it in a 'Chronicle Auto Block Entities' custom incident field.
- `skip_entity_isolation`: Skip the isolation of entities. You can manually set this as "Yes" or "No" here or you can set it in a 'Chronicle Skip Entity Isolation' custom incident field.

**Outputs:**

- `IsolatedEntities`
- `PotentiallyBlockedIPs`

**Dependencies:**

- Sub-playbooks: IP Enrichment - Generic v2, Isolate Endpoint - Generic, Block IP - Generic v2, Isolate Endpoint - Generic V2, Endpoint Enrichment - Generic v2.1
- Integrations: GoogleChronicleBackstory
- Scripts: DeleteContext, Set
- Commands: df-get-asset, setIndicator, ip


## Prisma Cloud Remediation - AWS CloudTrail is not Enabled on the Account

**Product:** Prisma Cloud by Palo Alto Networks

AWS Cloudtrail is a service which provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. To remediate Prisma Cloud Alert "CloudTrail is not enabled on the account", this playbook creates an S3 bucket to host Cloudtrail logs and enable Cloudtrail (includes all region events and global service events)

**Inputs:**

- `AutoEnableCloudTrail`: The following resources will be created:- S3 bucket cloudtrail-<account_id>- Cloudtrail cloudtrail-<account_id>Type 'Yes' to auto-enable CloudTrail.
- `CloudTrailRegion`: S3 bucket and (global) Cloudtrail will be created on this region

**Dependencies:**

- Commands: aws-s3-put-bucket-policy, aws-cloudtrail-start-logging, aws-cloudtrail-create-trail, aws-s3-create-bucket


## Prisma Cloud Remediation - AWS CloudTrail Is Not Integrated With CloudWatch Logs

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud AWS CloudTrail alerts. Prisma Cloud policies remediated

**Dependencies:**

- Integrations: AWS - CloudTrail, AWS - CloudWatchLogs, AWS - IAM
- Scripts: Sleep, isError
- Commands: aws-cloudtrail-describe-trails, aws-cloudtrail-update-trail, aws-iam-attach-policy, aws-iam-create-policy, aws-iam-create-role, aws-iam-get-role, aws-logs-create-log-group, aws-logs-describe-log-groups


## Prisma Cloud Remediation - AWS CloudTrail Trail Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud AWS CloudTrail alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Grab the Prisma Cloud policy Id.

**Dependencies:**

- Integrations: AWS - CloudTrail
- Commands: aws-cloudtrail-update-trail, aws-cloudtrail-describe-trails


## Prisma Cloud Remediation - AWS EC2 Security Group Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

Remediates the Prisma Cloud AWS EC2 alerts generated by the following policies

**Inputs:**

- `policyId`: Returns the Prisma Cloud policy ID.

**Dependencies:**

- Scripts: isError, Sleep
- Commands: aws-ec2-revoke-security-group-ingress-rule, aws-ec2-describe-security-groups


## Prisma Cloud Remediation - AWS IAM Password Policy Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

Remediates the following Prisma Cloud AWS IAM password policy alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Returns the Prisma Cloud policy ID.

**Dependencies:**

- Commands: aws-iam-update-account-password-policy


## Prisma Cloud Remediation - AWS IAM User Policy Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud AWS IAM User alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Scripts: Print
- Commands: aws-iam-list-access-keys-for-user, aws-iam-update-access-key


## Prisma Cloud Remediation - AWS Inactive Users For More Than 30 Days

**Product:** Prisma Cloud by Palo Alto Networks

Remediates Prisma Cloud Alert inactive users for more than 30 days, this playbook deactivates the user by disabling the access keys (marking them as inactive) as well as resetting the user console password. To increase the security of your AWS account, it is recommended to find and remove IAM user credentials (passwords, access keys) that have not been used within a specified period of time

**Inputs:**

- `AutoQuarantine`: Can be, "yes" - access keys will be disabled and password reset, or "no" - an analyst will be prompted for action.

**Dependencies:**

- Integrations: Builtin
- Scripts: Print
- Commands: aws-iam-update-login-profile, closeInvestigation, aws-iam-list-access-keys-for-user, aws-iam-update-access-key


## Prisma Cloud Remediation - AWS Security Groups Allows Internet Traffic To TCP Port

**Product:** Prisma Cloud by Palo Alto Networks

Extracts the TCP public Security Groups rule and provides manual/automatic options to have the rules revoked

**Inputs:**

- `AutoRevokeRule`: Can be, "yes" - public security group rules will be automatically revoked, or "no" - analyst will be prompted whether or not to allow automatic removal of the rules.

**Dependencies:**

- Integrations: Builtin, AWS - EC2
- Scripts: AwsEC2GetPublicSGRules
- Commands: aws-ec2-revoke-security-group-ingress-rule, aws-ec2-describe-security-groups, closeInvestigation


## Prisma Cloud Remediation - Azure AKS Cluster Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure AKS cluster alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Outputs:**

- `incident.labels.resource.name`

**Dependencies:**

- Integrations: Azure Kubernetes Services
- Scripts: IsIntegrationAvailable
- Commands: azure-ks-cluster-addon-update


## Prisma Cloud Remediation - Azure Network Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud Azure Network alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateAzureNetwork`: Execute Azure Network remediation automatically?
- `policyId`: Grab the Prisma Cloud policy ID.
- `portNumber`: Port number.

**Outputs:**

- `incident.resourcename`

**Dependencies:**

- Commands: closeInvestigation, prisma-cloud-alert-dismiss


## Prisma Cloud Remediation - Azure Network Security Group Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure Network security group alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.
- `portNumber`: Port number.

**Outputs:**

- `incident.resourcename`

**Dependencies:**

- Integrations: Azure Network Security Groups
- Scripts: IsIntegrationAvailable, Set
- Commands: azure-nsg-security-rule-delete


## Prisma Cloud Remediation - Azure SQL Database Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure SQL database alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Azure SQL Management
- Scripts: IsIntegrationAvailable
- Commands: azure-sql-db-threat-policy-create-update, azure-sql-db-audit-policy-create-update


## Prisma Cloud Remediation - Azure SQL Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud Azure SQL alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateAzureSQL`: Execute Azure SQL remediation automatically?
- `policyId`: Grab the Prisma Cloud policy ID.

**Dependencies:**

- Commands: prisma-cloud-alert-dismiss, closeInvestigation


## Prisma Cloud Remediation - Azure Storage Blob Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure Storage blob alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Azure Storage
- Scripts: IsIntegrationAvailable
- Commands: azure-storage-account-create-update


## Prisma Cloud Remediation - GCP Compute Engine Instance Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP Compute Engine VM Instance alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Google Cloud Compute
- Commands: gcp-compute-get-instance, gcp-compute-set-instance-metadata


## Prisma Cloud Remediation - GCP Compute Engine Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud GCP Compute Engine alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateComputeEngine`: Execute GCP Compute Engine remediation automatically?
- `policyId`: Grab the Prima Cloud policy ID.

**Dependencies:**

- Commands: closeInvestigation, prisma-cloud-alert-dismiss


## Prisma Cloud Remediation - GCP Kubernetes Engine Cluster Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP Kubernetes Engine Cluster alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: GoogleKubernetesEngine
- Commands: gcloud-clusters-set-muster-auth, gcloud-clusters-describe, gcloud-clusters-set-binary-auth, gcloud-clusters-set-intra-node-visibility, gcloud-clusters-set-legacy-auth, gcloud-clusters-set-master-authorized-network, gcloud-clusters-set-k8s-stackdriver, gcloud-clusters-set-addons


## Prisma Cloud Remediation - GCP Kubernetes Engine Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud GCP Kubernetes Engine alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateKubernetesEngine`: Execute GCP Kubernetes Engine remediation automatically?
- `policyId`: Grab the Prima Cloud policy ID.

**Dependencies:**

- Commands: prisma-cloud-alert-dismiss, closeInvestigation


## Prisma Cloud Remediation - GCP VPC Network Firewall Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP VPC Network Firewall alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Google Cloud Compute
- Commands: gcp-compute-get-firewall, gcp-compute-patch-firewall


## Prisma Cloud Remediation - GCP VPC Network Project Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP VPC Network Project alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Google Cloud Compute
- Scripts: isError
- Commands: gcp-compute-get-network, gcp-compute-delete-network


## Remediate Message - Agari Phishing Defense

**Product:** Agari Phishing Defense

Remediates a given message id. Supported   versions: 5.0.0 and later

**Inputs:**

- `id`: Id of message to remediate.
- `auto_remediation`: Flag for whether to automatically remediate or not.
- `remediate_action`: Action for remediation.

**Dependencies:**

- Commands: apd-remediate-message


## Rubrik IR Violation Remediation - Rubrik Security Cloud

**Product:** Rubrik Security Cloud

This playbook remediates Identity Resilience (IR) violations by retrieving the latest violation details and updating the violation status

**Inputs:**

- `violation_id`: The ID of the IR violation.Note: Users can get the violation ID by executing the "rubrik-identity-resilience-violation-list" command.
- `policy_type`: The policy type of the violation.Note: Users can get the policy type by executing the "rubrik-identity-resilience-violation-list" command.Possible values are: IDENTITY, IDP,IDENTIT

**Dependencies:**

- Scripts: DeleteContext, RubrikPullIRViolationInformation, Set
- Commands: rubrik-identity-resilience-violation-status-update


## SaaS Security - Remediate an Asset

**Product:** SaaS Security by Palo Alto Networks

Take a remediation action over an asset: Use this playbook as a sub-playbook to take a remediation action on an asset. Available remediation actions are 1) Remove public sharing, 2) Quarantine, and 3) Restore. This playbook implements polling by continuously running the saas-security-remediation-status-get command to get the remediation status for a given asset ID, until the operation completes. The remote action should have the following structure

**Inputs:**

- `asset_id`: The ID of the asset to remediate
- `remediation_type`: The remediation action to take.Possible values: Remove public sharing, Quarantine, Restore.
- `remove_inherited_sharing`: Used when remediation type is “remove_public_sharing”, when set to true, all the parent folder sharing url will be removed.

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: SaaS Security
- Commands: saas-security-remediation-status-get, saas-security-asset-remediate

## Agari Message Remediation - Agari Phishing Defense

**Product:** Agari Phishing Defense

Investigates Agari policy events by obtaining the original message and attachments from the existing email integrations and remediates in Agari. Supported   versions: 5.0.0 and later

**Inputs:**

- `APD Global Message ID`: Global Message Id obtained from the incident.
- `AuthenticateEmail`: Whether the authenticity of the email should be verified, using Authenticity Score.
- `OnCall`: Set to true to assign only user that is currently on shift. Requires the platform.5 or later.
- `Role`: The default role to assign the incident to.
- `ResolveIP`: Resolve IP addresses to hostnames (DNS).
- `AutoRemeditaion`: Whether Automatic remediate message or not.
- `RemediateAction`: Default action for remediation of message.
- `UserEnrichmentEnable`: Flag for enabling User Enrichment.
- `User Id`: Id of User.
- `APD Internal Message ID`: Internal Message Id obtained from the incident.

**Dependencies:**

- Sub-playbooks: Entity Enrichment - Phishing v2, Extract Indicators From File - Generic v2, Email Address Enrichment - Generic v2.1, Retrieve Email Data - Agari Phishing Defense, Calculate Severity - Generic v2, Process Email - Generic, Remediate Message - Agari Phishing Defense, Detonate File - Generic
- Scripts: AssignAnalystToIncident, Set, CheckEmailAuthenticity
- Commands: closeInvestigation, setIncident


## AWS - EC2 Instance Security Group Remediation

**Product:** Cloud Security Policy Management

This playbook identifies the security groups used on an EC2 interface with a specific public IP. It determines which rules allow access via the given port and protocol, creates a copy of the security groups with those rules removed, and updates the interface to use the modified security groups. The original security groups are left unmodified, and the remediated copy is applied to the exposed EC2 instance

**Inputs:**

- `AssetID`: The asset ID of the VM Instance.
- `PublicIP`: The public IP address to remediate for public exposure.
- `RemotePort`: The TCP/UDP port number to be restricted.
- `RemoteProtocol`: The protocol to be restricted (tcp/udp).
- `RemediationAllowRanges`: A comma-separated list of IPv4 network ranges to be used as source addresses for the `cortex-remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically these are priva
- `IntegrationInstance`: The AWS integration instance to use if multiple instances are configured (optional).

**Outputs:**

- `remediatedFlag`
- `remediation_action`

**Dependencies:**

- Integrations: AWS, Cortex Core - Platform
- Scripts: AWSIdentifySGPublicExposure, AWSRemediateSG, GetTime, Print, Set
- Commands: aws-ec2-network-interface-attribute-modify, core-get-asset-details


## AWS - Security Group Remediation v2

**Product:** AWS Enrichment and Remediation

This playbook takes in some information about an EC2 instance (ID and public_ip) and with provided port and protocol, determines what security groups on the primary interface of an EC2 instance are over-permissive. It uses an automation to determine what interface on an EC2 instance has an over-permissive security group on, determine which security groups have over-permissive rules and to replace them with a copy of the security group that has only the over-permissive portion removed. Over-permissive is defined as sensitive ports (SSH, RDP, etc) being exposed to the internet via IPv4

**Inputs:**

- `InstanceID`: ID of the AWS EC2 instance.
- `Port`: TCP/UDP port to be restricted.
- `Protocol`: Protocol of the port to be restricted.
- `PublicIP`: Public IP address of the EC2 instance.
- `AWSAssumeArn`: Name of an AWS role to assume (should be the same for all organizations).
- `Region`: Region where EC2 instance is present.

**Dependencies:**

- Scripts: AWSRecreateSG


## AWS - Unclaimed S3 Bucket Remediation

**Product:** AWS Enrichment and Remediation

The playbook will create the unclaimed S3 bucket

**Inputs:**

- `S3BucketName`: Unclaimed S3 bucket name.

**Dependencies:**

- Integrations: AWS - S3
- Commands: aws-s3-list-buckets, aws-s3-create-bucket


## AWS Network Exposure - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

This playbook remediates the following AWS Network Exposure detections

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Outputs:**

- `remediatedFlag`

**Dependencies:**

- Sub-playbooks: AWS - EC2 Instance Security Group Remediation, Notify Stakeholders
- Integrations: Cortex Core - Platform
- Scripts: Print
- Commands: core-get-issue-recommendations, setIssueStatus


## AWS Public Access Misconfiguration - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates 9 AWS public access misconfigurations: 1 RDS database, 1 EBS snapshot, and 7 S3 bucket issues: The playbook disables public access by modifying RDS publicly_accessible settings, removing EBS snapshot createVolumePermission, and enabling S3 PublicAccessBlockConfiguration respectively. Optional stakeholder notification is available via the "Notify Stakeholders" sub-playbook by setting enableNotifications input to 'yes' (default: 'no'). When enabled, configure at least one recipient (email, Slack channel, or Teams channel) in the Notify Stakeholders playbook inputs. The playbook automatically updates the issue status to "Resolved - Fixed" upon successful remediation

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: Notify Stakeholders
- Integrations: AWS, Cortex Core - Platform
- Scripts: Print, Set
- Commands: aws-ec2-snapshot-attribute-modify, aws-rds-db-instance-modify, aws-s3-public-access-block-update, core-get-asset-details, setIssueStatus


## Azure - Network Security Group Remediation

**Product:** Azure Enrichment and Remediation

This playbook adds new Azure Network Security Groups (NSG) rules to NSGs attached to a NIC. The new rules will give access only to a private IP address range and block traffic that's exposed to the public internet (using the private IP of the VM as stated in Azure documentation). For example, if RDP is exposed to the public internet, this playbook adds new firewall rules that only allow traffic from private IP addresses and blocks the rest of the RDP traffic. Conditions and limitations

**Inputs:**

- `AzureSecurityGroup`: The Azure Network Security Group that will have new rules created or updated.
- `AzureVMPrivateIP`: The private IP of the Azure Virtual Machine.
- `RemoteProtocol`: The remote protocol that is publicly exposed.
- `RemotePort`: The remote port that is publicly exposed.
- `SubscriptionID`: The Azure subscription ID (optional).
- `ResourceGroup`: The Azure resource group (optional).
- `InstanceName`: Azure Network Security Groups integration instance to use if you have multiple instances configured (optional).
- `RemediationAllowRanges`: Comma-separated list of IPv4 network ranges to be used as source addresses for the `remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically this will be private IP 

**Outputs:**

- `remediatedFlag`
- `remediatedReason`

**Dependencies:**

- Integrations: Azure Network Security Groups
- Scripts: Set, AzureFindAvailableNSGPriorities
- Commands: azure-nsg-security-rule-update, azure-nsg-security-rule-create, azure-nsg-security-rules-list


## Azure - VM Instance Network Security Group Remediation

**Product:** Cloud Security Policy Management

This playbook adds new Azure Network Security Group (NSG) rules to NSGs attached to a NIC. The new rules give access to only a private IP address range and block traffic exposed to the public internet using the private IP of the VM, as explained in the (Azure documentation). For example, if RDP is exposed to the public internet, this playbook adds new firewall rules that only allow traffic from private IP addresses and blocks the rest of the RDP traffic. Conditions and limitations

**Inputs:**

- `AssetID`: The asset ID of the VM Instance.
- `PublicIP`: The public IP address to remediate for public exposure.
- `RemoteProtocol`: The remote protocol that is publicly exposed.
- `RemotePort`: The remote port that is publicly exposed.
- `IntegrationInstance`: The Azure Network Security Groups integration instance to use if you have multiple instances configured (optional).
- `RemediationAllowRanges`: A comma-separated list of IPv4 network ranges to be used as source addresses for the `cortex-remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically these are priva

**Outputs:**

- `remediatedFlag`
- `remediation_action`

**Dependencies:**

- Integrations: Azure, Cortex Core - Platform
- Scripts: AzureIdentifyNSGExposureRule, Print, Set, SetAndHandleEmpty
- Commands: azure-vn-network-interface-get, azure-vn-public-ip-address-get, azure-vn-security-rule-create, azure-vn-security-rule-update, azure-vn-security-rules-list, core-get-asset-details


## Azure Network Exposure - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

This playbook remediates the following Azure Network Exposure detections

**Inputs:**

- `enableNotifications`: Options: yes/no Choose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify 

**Dependencies:**

- Sub-playbooks: Azure - Network Security Group Remediation v2, Notify Stakeholders
- Integrations: Cortex Core - Platform
- Scripts: Print
- Commands: core-get-issue-recommendations, setIssueStatus


## Azure Public Access Misconfiguration - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates 3 Azure public access misconfigurations: The playbook disables public access by setting allowBlobPublicAccess to false, configuring VM disk publicNetworkAccess to Disabled with a DenyAll policy, and updating the storage account default network access action to Deny. Optional stakeholder notification is available via the "Notify Stakeholders" sub-playbook by setting enableNotifications input to 'yes' (default: 'no'). When enabled, configure at least one recipient (email, Slack channel, or Teams channel) in the Notify Stakeholders playbook inputs. The playbook automatically updates the issue status to "Resolved - Fixed" upon successful remediation

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: Notify Stakeholders
- Integrations: Azure, Cortex Core - Platform
- Scripts: Print, Set
- Commands: azure-compute-disk-update, azure-storage-account-update, core-get-asset-details, setIssueStatus


## ChronicleAssets Investigation And Remediation - Chronicle

**Product:** Google SecOps

Performs enrichment and investigation of the ChronicleAsset type of indicators, provides an opportunity to remediate in case any of the ChronicleAsset information i.e., hostname or IP address is found to be malicious or suspicious, and sends out an email containing the list of isolated and potentially blocked entities. To select the indicators you want to add, go to playbook inputs, choose "from indicators" and set your query. For example, type:ChronicleAsset etc. The default playbook query is "type:ChronicleAsset". In case indicators with different query parameters are to be investigated, the query must be edited accordingly. This playbook needs to be used with caution as it might use up the integration’s API license when running large amounts of indicators

**Inputs:**

- `Indicator Query`: Indicators matching the indicator query will be used as playbook inputs.
- `chronicleasset_support_contact`: The support email address for the Chronicle asset.
- `auto_block_entities`: Autoblock the detected suspicious IP address(es). You can manuall set this as 'Yes' or 'No' here or you can set it in a 'Chronicle Auto Block Entities' custom incident field.
- `skip_entity_isolation`: Skip the isolation of entities. You can manually set this as 'Yes' or 'No' here or you can set it in a 'Chronicle Skip Entity Isolation' custom incident field.


## Commvault Suspicious File Activity Remediation

**Product:** Commvault Cloud

Playbook to disable data-aging on commvault client when a threat is detected

**Dependencies:**

- Integrations: CommvaultSecurityIQ
- Scripts: AssignAnalystToIncident
- Commands: closeInvestigation, setIncident, disable-data-aging


## Cortex ASM - Cortex Endpoint Remediation

**Product:** Cortex Attack Surface Management

This playbook is used to isolate a single  Endpoint (XSIAM/XDR) for remediation purposes

**Inputs:**

- `CortexEndpointID`: The ID of the Cortex Endpoint (XDR).

**Dependencies:**

- Integrations: Cortex Core - IR, Cortex XDR - IR
- Scripts: Set
- Commands: xdr-endpoint-isolate, core-isolate-endpoint


## Cortex ASM - On Prem Remediation

**Product:** Cortex Attack Surface Management

This playbook adds new block rule(s) to on-prem firewall vendors in order to block internet access for internet exposures. Conditions

**Inputs:**

- `RuleName`: Firewall rule name to look up in the company configuration setting for block rule.
- `RemoteIP`: IP address of the service.
- `RemoteProtocol`: Protocol of the service.
- `RemotePort`: Port number of the service.
- `DeviceGroup`: Device group of the firewall rule to lookup.
- `SecondaryDeviceGroup`: If the rule, address and service are created in the "Shared" location, we need to know what device-groups we can push to because it isn't possible to push to the "Shared" location.

**Dependencies:**

- Sub-playbooks: PAN-OS - Block Destination Service
- Integrations: Panorama
- Commands: pan-os-list-rules


## Cortex ASM - Remediation Confirmation Scan

**Product:** Cortex Attack Surface Management

This playbook handles ASM Remediation Confirmation Scan by first creating a scan for an existing service ID, if the scan does not already exist. It then polls for results of a successful or failed scan

**Dependencies:**

- Scripts: GridFieldSetup, GetTime
- Commands: asm-get-remediation-confirmation-scan-status, asm-start-remediation_confirmation_scan


## Cortex ASM - Remediation Guidance

**Product:** Cortex Attack Surface Management

This playbook pulls remediation guidance off of a list based on ASM RuleID to be used in service owner notifications (email or ticketing system)

**Inputs:**

- `IssueTypeID`: Attack surface management issue rule ID.

**Outputs:**

- `RemediationGuidance`

**Dependencies:**

- Commands: asm-get-attack-surface-rule, setAlert


## Cortex ASM - Remediation Objectives

**Product:** Cortex Attack Surface Management

Playbook that populates the remediation objectives field that is used to display the remediation actions to the end user

**Dependencies:**

- Scripts: Set, GridFieldSetup


## Cortex ASM - Remediation Path Rules

**Product:** Cortex Attack Surface Management

This playbook returns "RemediationAction" options based on the return from the Remediation Path Rules API, or defaults to data collection task

**Inputs:**

- `ExternallyDetectedProviders`: Providers of external service.
- `BypassDevCheck`: Determine whether to bypass the Dev Check in automated remediation criteria: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-Expander-User-Guide/Automated-Re

**Outputs:**

- `RemediationAction`
- `RPR_Timestamp`

**Dependencies:**

- Integrations: CortexAttackSurfaceManagement
- Scripts: GetTime, GridFieldSetup, Set, RemediationPathRuleEvaluation
- Commands: asm-list-remediation-rule


## Cortex ASM - Remediation

**Product:** Cortex Attack Surface Management

This playbook contains all the cloud provider sub playbooks for remediation

**Inputs:**

- `AWSAssumeRoleName`: If assuming roles for AWS, this is the name of the role to assume (should be the same for all organizations)

**Dependencies:**

- Sub-playbooks: AWS - Package Upgrade, AWS - Security Group Remediation v2, AWS - Unclaimed S3 Bucket Remediation, Azure - Network Security Group Remediation, Cortex ASM - Cortex Endpoint Remediation, Cortex ASM - On Prem Remediation, GCP - Firewall Remediation


## Cortex EM - Remediation

**Product:** Cortex Exposure Management

This playbook handles exposure issue remediation

**Inputs:**

- `AWSAssumeRoleName`: The name of the role to assume for AWS (should be the same for all organizations).

**Dependencies:**

- Sub-playbooks: AWS - Enrichment, AWS - Security Group Remediation v2, Cortex EM - Exposure Issue


## DSPM Multi-Cloud Risk Remediation

**Product:** DSPM

The playbook ensures efficient incident resolution and compliance with security policies by guiding the user through decision points based on incident type, such as empty storage assets or assets open to the world. It concludes by updating the incident status and closing the playbook upon resolution

**Inputs:**

- `defaultSlackUserName`: In the event that the risk asset tag is absent, the risk notice will be sent to this Slack user email address.
- `slackMessageLifetime`: Lifetime for slack notification (in seconds)
- `rerunTime`: Incident re-run time (in hours)

**Dependencies:**

- Sub-playbooks: DSPM Valid User Response, Send slack notificaton to user, Invalid response sending notification to user again, DSPM notify user in case of error
- Scripts: DSPMCreateSimpleSlackMessageBlock, DSPMCheckAndSetErrorEntries, IsIntegrationAvailable, DSPMIncidentList, DSPMExtractRiskDetails, DeleteContext, DSPMCreateRiskSlackBlocks, isError
- Commands: createList, setList, getList, addToList, closeInvestigation, core-api-post


## DSPM Remediation for Empty storage asset

**Product:** DSPM

This playbook is designed to remediate risks associated with empty storage assets across AWS, Azure, and GCP environments. It identifies the cloud provider for the asset and proceeds to delete the storage container or bucket accordingly. Additionally, it sends notifications via Slack to inform stakeholders about the status of the remediation process

**Dependencies:**

- Integrations: AWS - S3, DSPM, Google Cloud Storage
- Scripts: IsIntegrationAvailable, DSPMIncidentList, DSPMCheckAndSetErrorEntries, DeleteContext, DSPMCreateSimpleSlackMessageBlock
- Commands: aws-s3-delete-bucket, dspm-update-risk-finding-status, gcs-delete-bucket, setList


## DSPM Remediation for Sensitive asset open to world

**Product:** DSPM

The DSPM Remediation Playbook for Sensitive Asset Open to World is designed to handle incidents where sensitive assets are exposed to the public, with specific focus on remediating this vulnerability across different cloud providers (AWS). Below is an overview of the key steps and actions included in this playbook

**Dependencies:**

- Integrations: DSPM, Google Cloud Storage, AWS - S3, Azure Storage Container
- Scripts: DSPMIncidentList, DSPMCreateSimpleSlackMessageBlock, DSPMCheckAndSetErrorEntries, DeleteContext, DSPMGetContianers, IsIntegrationAvailable
- Commands: dspm-update-risk-finding-status, setList, aws-s3-put-public-access-block, gcs-block-public-access-bucket, azure-storage-container-block-public-access, dspm-get-asset-files-by-id


## ETD Email Reclassification And Remediation

**Product:** ETD the platform Connector

Allows analysts to review Cisco ETD emails, reclassify message verdicts, and perform remediation actions

**Dependencies:**

- Integrations: ETDConnector
- Scripts: IsIntegrationAvailable, Print
- Commands: cisco-etd-move-message


## GCP - Firewall Remediation

**Product:** GCP Enrichment and Remediation

This playbook adds new firewall rules with access only from private ip address range and blocks traffic that's exposed to public internet. For example, if RDP is exposed to the entire world, this playbook adds new firewall rules that only allows traffic from private ip address and blocks rest of the RDP traffic

**Inputs:**

- `GcpInstance`: The name of the GCP instance that has the public ip.
- `GcpZone`: The zone of the GCP instance that is hosted in.
- `GcpNetwork`: The VPC network of the GCP instance.
- `RemotePort`: The remote port that is publicly exposed to.
- `RemoteProtocol`: The remote protocol that is publicly exposed to.
- `GcpProject`: The name of the GCP project associated with the instance and related objects.
- `instance_name`: Google Cloud Compute integration instance to use if you have multiple instances configured (optional).

**Dependencies:**

- Integrations: Google Cloud Compute
- Scripts: Set
- Commands: gcp-compute-list-firewall, gcp-compute-insert-firewall, gcp-compute-add-network-tag, gcp-compute-get-instance


## GCP - VM Instance Firewall Rule Remediation

**Product:** Cloud Security Policy Management

This playbook adds new VPC firewall rules to restrict access to private IP address ranges and block traffic exposed to the public internet. For example, if RDP is exposed this playbook adds new firewall rules that allow traffic only from private IP addresses and it blocks all other RDP traffic. New allow and block rules created by this playbook target only the exposed asset

**Inputs:**

- `AssetID`: The asset ID of the VM instance.
- `RemotePort`: The remote port that is publicly exposed.
- `RemoteProtocol`: The remote protocol that is publicly exposed.
- `IntegrationInstance`: The GCP integration instance to use if multiple instances are configured (optional).
- `RemediationAllowRanges`: A comma-separated list of IPv4 network ranges to be used as source addresses for the `cortex-remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically these are priva

**Outputs:**

- `remediatedFlag`
- `remediation_action`

**Dependencies:**

- Integrations: Cortex Core - Platform, GCP
- Scripts: Print, Set
- Commands: core-get-asset-details, gcp-compute-firewall-insert, gcp-compute-firewall-list, gcp-compute-instance-get, gcp-compute-network-tag-set


## GCP Network Exposure - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates the following Network Exposure detection

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: GCP - VM Instance Firewall Rule Remediation, Notify Stakeholders
- Integrations: Cortex Core - Platform
- Scripts: Print
- Commands: core-get-issue-recommendations, setIssueStatus


## GCP Public Access Misconfiguration - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates 2 GCP public access misconfigurations: The playbook removes public IAM policy bindings by deleting 'allUsers' and 'allAuthenticatedUsers' entities from the bucket's Access Control List respectively. Optional stakeholder notification is available via the "Notify Stakeholders" sub-playbook by setting enableNotifications input to 'yes' (default: 'no'). When enabled, configure at least one recipient (email, Slack channel, or Teams channel) in the Notify Stakeholders playbook inputs. The playbook automatically updates the issue status to "Resolved - Fixed" upon successful remediation

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: Notify Stakeholders
- Integrations: Cortex Core - Platform, GCP
- Scripts: Print, Set
- Commands: core-get-asset-details, gcp-storage-bucket-policy-delete, setIssueStatus


## Hostname And IP Address Investigation And Remediation - Chronicle

**Product:** Google SecOps

This playbook receives ChronicleAsset type of indicators from its parent playbook "ChronicleAsset Investigation - Chronicle", performs enrichment and investigation for each one of them, provides an opportunity to isolate and block the hostname or IP address associated with the current indicator, and provides a list of isolated and blocked entities

**Inputs:**

- `chronicleasset_value`: The value of the ChronicleAsset indicator.
- `chronicleasset_hostname`: The hostname associated with the ChronicleAsset.
- `chronicleasset_ip`: The IP address associated with the ChronicleAsset.
- `chronicleasset_support_contact`: The support email address for the ChronicleAsset.
- `auto_block_entities`: Autoblock the detected suspicious IP Address(es). You can manually set this as "Yes" or "No" here or you can set it in a 'Chronicle Auto Block Entities' custom incident field.
- `skip_entity_isolation`: Skip the isolation of entities. You can manually set this as "Yes" or "No" here or you can set it in a 'Chronicle Skip Entity Isolation' custom incident field.

**Outputs:**

- `IsolatedEntities`
- `PotentiallyBlockedIPs`

**Dependencies:**

- Sub-playbooks: IP Enrichment - Generic v2, Isolate Endpoint - Generic, Block IP - Generic v2, Isolate Endpoint - Generic V2, Endpoint Enrichment - Generic v2.1
- Integrations: GoogleChronicleBackstory
- Scripts: DeleteContext, Set
- Commands: df-get-asset, setIndicator, ip


## Prisma Cloud Remediation - AWS CloudTrail is not Enabled on the Account

**Product:** Prisma Cloud by Palo Alto Networks

AWS Cloudtrail is a service which provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. To remediate Prisma Cloud Alert "CloudTrail is not enabled on the account", this playbook creates an S3 bucket to host Cloudtrail logs and enable Cloudtrail (includes all region events and global service events)

**Inputs:**

- `AutoEnableCloudTrail`: The following resources will be created:- S3 bucket cloudtrail-<account_id>- Cloudtrail cloudtrail-<account_id>Type 'Yes' to auto-enable CloudTrail.
- `CloudTrailRegion`: S3 bucket and (global) Cloudtrail will be created on this region

**Dependencies:**

- Commands: aws-s3-put-bucket-policy, aws-cloudtrail-start-logging, aws-cloudtrail-create-trail, aws-s3-create-bucket


## Prisma Cloud Remediation - AWS CloudTrail Is Not Integrated With CloudWatch Logs

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud AWS CloudTrail alerts. Prisma Cloud policies remediated

**Dependencies:**

- Integrations: AWS - CloudTrail, AWS - CloudWatchLogs, AWS - IAM
- Scripts: Sleep, isError
- Commands: aws-cloudtrail-describe-trails, aws-cloudtrail-update-trail, aws-iam-attach-policy, aws-iam-create-policy, aws-iam-create-role, aws-iam-get-role, aws-logs-create-log-group, aws-logs-describe-log-groups


## Prisma Cloud Remediation - AWS CloudTrail Trail Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud AWS CloudTrail alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Grab the Prisma Cloud policy Id.

**Dependencies:**

- Integrations: AWS - CloudTrail
- Commands: aws-cloudtrail-update-trail, aws-cloudtrail-describe-trails


## Prisma Cloud Remediation - AWS EC2 Security Group Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

Remediates the Prisma Cloud AWS EC2 alerts generated by the following policies

**Inputs:**

- `policyId`: Returns the Prisma Cloud policy ID.

**Dependencies:**

- Scripts: isError, Sleep
- Commands: aws-ec2-revoke-security-group-ingress-rule, aws-ec2-describe-security-groups


## Prisma Cloud Remediation - AWS IAM Password Policy Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

Remediates the following Prisma Cloud AWS IAM password policy alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Returns the Prisma Cloud policy ID.

**Dependencies:**

- Commands: aws-iam-update-account-password-policy


## Prisma Cloud Remediation - AWS IAM User Policy Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud AWS IAM User alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Scripts: Print
- Commands: aws-iam-list-access-keys-for-user, aws-iam-update-access-key


## Prisma Cloud Remediation - AWS Inactive Users For More Than 30 Days

**Product:** Prisma Cloud by Palo Alto Networks

Remediates Prisma Cloud Alert inactive users for more than 30 days, this playbook deactivates the user by disabling the access keys (marking them as inactive) as well as resetting the user console password. To increase the security of your AWS account, it is recommended to find and remove IAM user credentials (passwords, access keys) that have not been used within a specified period of time

**Inputs:**

- `AutoQuarantine`: Can be, "yes" - access keys will be disabled and password reset, or "no" - an analyst will be prompted for action.

**Dependencies:**

- Integrations: Builtin
- Scripts: Print
- Commands: aws-iam-update-login-profile, closeInvestigation, aws-iam-list-access-keys-for-user, aws-iam-update-access-key


## Prisma Cloud Remediation - AWS Security Groups Allows Internet Traffic To TCP Port

**Product:** Prisma Cloud by Palo Alto Networks

Extracts the TCP public Security Groups rule and provides manual/automatic options to have the rules revoked

**Inputs:**

- `AutoRevokeRule`: Can be, "yes" - public security group rules will be automatically revoked, or "no" - analyst will be prompted whether or not to allow automatic removal of the rules.

**Dependencies:**

- Integrations: Builtin, AWS - EC2
- Scripts: AwsEC2GetPublicSGRules
- Commands: aws-ec2-revoke-security-group-ingress-rule, aws-ec2-describe-security-groups, closeInvestigation


## Prisma Cloud Remediation - Azure AKS Cluster Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure AKS cluster alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Outputs:**

- `incident.labels.resource.name`

**Dependencies:**

- Integrations: Azure Kubernetes Services
- Scripts: IsIntegrationAvailable
- Commands: azure-ks-cluster-addon-update


## Prisma Cloud Remediation - Azure Network Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud Azure Network alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateAzureNetwork`: Execute Azure Network remediation automatically?
- `policyId`: Grab the Prisma Cloud policy ID.
- `portNumber`: Port number.

**Outputs:**

- `incident.resourcename`

**Dependencies:**

- Commands: closeInvestigation, prisma-cloud-alert-dismiss


## Prisma Cloud Remediation - Azure Network Security Group Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure Network security group alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.
- `portNumber`: Port number.

**Outputs:**

- `incident.resourcename`

**Dependencies:**

- Integrations: Azure Network Security Groups
- Scripts: IsIntegrationAvailable, Set
- Commands: azure-nsg-security-rule-delete


## Prisma Cloud Remediation - Azure SQL Database Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure SQL database alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Azure SQL Management
- Scripts: IsIntegrationAvailable
- Commands: azure-sql-db-threat-policy-create-update, azure-sql-db-audit-policy-create-update


## Prisma Cloud Remediation - Azure SQL Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud Azure SQL alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateAzureSQL`: Execute Azure SQL remediation automatically?
- `policyId`: Grab the Prisma Cloud policy ID.

**Dependencies:**

- Commands: prisma-cloud-alert-dismiss, closeInvestigation


## Prisma Cloud Remediation - Azure Storage Blob Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure Storage blob alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Azure Storage
- Scripts: IsIntegrationAvailable
- Commands: azure-storage-account-create-update


## Prisma Cloud Remediation - GCP Compute Engine Instance Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP Compute Engine VM Instance alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Google Cloud Compute
- Commands: gcp-compute-get-instance, gcp-compute-set-instance-metadata


## Prisma Cloud Remediation - GCP Compute Engine Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud GCP Compute Engine alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateComputeEngine`: Execute GCP Compute Engine remediation automatically?
- `policyId`: Grab the Prima Cloud policy ID.

**Dependencies:**

- Commands: closeInvestigation, prisma-cloud-alert-dismiss


## Prisma Cloud Remediation - GCP Kubernetes Engine Cluster Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP Kubernetes Engine Cluster alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: GoogleKubernetesEngine
- Commands: gcloud-clusters-set-muster-auth, gcloud-clusters-describe, gcloud-clusters-set-binary-auth, gcloud-clusters-set-intra-node-visibility, gcloud-clusters-set-legacy-auth, gcloud-clusters-set-master-authorized-network, gcloud-clusters-set-k8s-stackdriver, gcloud-clusters-set-addons


## Prisma Cloud Remediation - GCP Kubernetes Engine Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud GCP Kubernetes Engine alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateKubernetesEngine`: Execute GCP Kubernetes Engine remediation automatically?
- `policyId`: Grab the Prima Cloud policy ID.

**Dependencies:**

- Commands: prisma-cloud-alert-dismiss, closeInvestigation


## Prisma Cloud Remediation - GCP VPC Network Firewall Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP VPC Network Firewall alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Google Cloud Compute
- Commands: gcp-compute-get-firewall, gcp-compute-patch-firewall


## Prisma Cloud Remediation - GCP VPC Network Project Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP VPC Network Project alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Google Cloud Compute
- Scripts: isError
- Commands: gcp-compute-get-network, gcp-compute-delete-network


## Remediate Message - Agari Phishing Defense

**Product:** Agari Phishing Defense

Remediates a given message id. Supported   versions: 5.0.0 and later

**Inputs:**

- `id`: Id of message to remediate.
- `auto_remediation`: Flag for whether to automatically remediate or not.
- `remediate_action`: Action for remediation.

**Dependencies:**

- Commands: apd-remediate-message


## Rubrik IR Violation Remediation - Rubrik Security Cloud

**Product:** Rubrik Security Cloud

This playbook remediates Identity Resilience (IR) violations by retrieving the latest violation details and updating the violation status

**Inputs:**

- `violation_id`: The ID of the IR violation.Note: Users can get the violation ID by executing the "rubrik-identity-resilience-violation-list" command.
- `policy_type`: The policy type of the violation.Note: Users can get the policy type by executing the "rubrik-identity-resilience-violation-list" command.Possible values are: IDENTITY, IDP,IDENTIT

**Dependencies:**

- Scripts: DeleteContext, RubrikPullIRViolationInformation, Set
- Commands: rubrik-identity-resilience-violation-status-update


## SaaS Security - Remediate an Asset

**Product:** SaaS Security by Palo Alto Networks

Take a remediation action over an asset: Use this playbook as a sub-playbook to take a remediation action on an asset. Available remediation actions are 1) Remove public sharing, 2) Quarantine, and 3) Restore. This playbook implements polling by continuously running the saas-security-remediation-status-get command to get the remediation status for a given asset ID, until the operation completes. The remote action should have the following structure

**Inputs:**

- `asset_id`: The ID of the asset to remediate
- `remediation_type`: The remediation action to take.Possible values: Remove public sharing, Quarantine, Restore.
- `remove_inherited_sharing`: Used when remediation type is “remove_public_sharing”, when set to true, all the parent folder sharing url will be removed.

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: SaaS Security
- Commands: saas-security-remediation-status-get, saas-security-asset-remediate

## Agari Message Remediation - Agari Phishing Defense

**Product:** Agari Phishing Defense

Investigates Agari policy events by obtaining the original message and attachments from the existing email integrations and remediates in Agari. Supported   versions: 5.0.0 and later

**Inputs:**

- `APD Global Message ID`: Global Message Id obtained from the incident.
- `AuthenticateEmail`: Whether the authenticity of the email should be verified, using Authenticity Score.
- `OnCall`: Set to true to assign only user that is currently on shift. Requires the platform.5 or later.
- `Role`: The default role to assign the incident to.
- `ResolveIP`: Resolve IP addresses to hostnames (DNS).
- `AutoRemeditaion`: Whether Automatic remediate message or not.
- `RemediateAction`: Default action for remediation of message.
- `UserEnrichmentEnable`: Flag for enabling User Enrichment.
- `User Id`: Id of User.
- `APD Internal Message ID`: Internal Message Id obtained from the incident.

**Dependencies:**

- Sub-playbooks: Entity Enrichment - Phishing v2, Extract Indicators From File - Generic v2, Email Address Enrichment - Generic v2.1, Retrieve Email Data - Agari Phishing Defense, Calculate Severity - Generic v2, Process Email - Generic, Remediate Message - Agari Phishing Defense, Detonate File - Generic
- Scripts: AssignAnalystToIncident, Set, CheckEmailAuthenticity
- Commands: closeInvestigation, setIncident


## AWS - EC2 Instance Security Group Remediation

**Product:** Cloud Security Policy Management

This playbook identifies the security groups used on an EC2 interface with a specific public IP. It determines which rules allow access via the given port and protocol, creates a copy of the security groups with those rules removed, and updates the interface to use the modified security groups. The original security groups are left unmodified, and the remediated copy is applied to the exposed EC2 instance

**Inputs:**

- `AssetID`: The asset ID of the VM Instance.
- `PublicIP`: The public IP address to remediate for public exposure.
- `RemotePort`: The TCP/UDP port number to be restricted.
- `RemoteProtocol`: The protocol to be restricted (tcp/udp).
- `RemediationAllowRanges`: A comma-separated list of IPv4 network ranges to be used as source addresses for the `cortex-remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically these are priva
- `IntegrationInstance`: The AWS integration instance to use if multiple instances are configured (optional).

**Outputs:**

- `remediatedFlag`
- `remediation_action`

**Dependencies:**

- Integrations: AWS, Cortex Core - Platform
- Scripts: AWSIdentifySGPublicExposure, AWSRemediateSG, GetTime, Print, Set
- Commands: aws-ec2-network-interface-attribute-modify, core-get-asset-details


## AWS - Security Group Remediation v2

**Product:** AWS Enrichment and Remediation

This playbook takes in some information about an EC2 instance (ID and public_ip) and with provided port and protocol, determines what security groups on the primary interface of an EC2 instance are over-permissive. It uses an automation to determine what interface on an EC2 instance has an over-permissive security group on, determine which security groups have over-permissive rules and to replace them with a copy of the security group that has only the over-permissive portion removed. Over-permissive is defined as sensitive ports (SSH, RDP, etc) being exposed to the internet via IPv4

**Inputs:**

- `InstanceID`: ID of the AWS EC2 instance.
- `Port`: TCP/UDP port to be restricted.
- `Protocol`: Protocol of the port to be restricted.
- `PublicIP`: Public IP address of the EC2 instance.
- `AWSAssumeArn`: Name of an AWS role to assume (should be the same for all organizations).
- `Region`: Region where EC2 instance is present.

**Dependencies:**

- Scripts: AWSRecreateSG


## AWS - Unclaimed S3 Bucket Remediation

**Product:** AWS Enrichment and Remediation

The playbook will create the unclaimed S3 bucket

**Inputs:**

- `S3BucketName`: Unclaimed S3 bucket name.

**Dependencies:**

- Integrations: AWS - S3
- Commands: aws-s3-list-buckets, aws-s3-create-bucket


## AWS Network Exposure - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

This playbook remediates the following AWS Network Exposure detections

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Outputs:**

- `remediatedFlag`

**Dependencies:**

- Sub-playbooks: AWS - EC2 Instance Security Group Remediation, Notify Stakeholders
- Integrations: Cortex Core - Platform
- Scripts: Print
- Commands: core-get-issue-recommendations, setIssueStatus


## AWS Public Access Misconfiguration - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates 9 AWS public access misconfigurations: 1 RDS database, 1 EBS snapshot, and 7 S3 bucket issues: The playbook disables public access by modifying RDS publicly_accessible settings, removing EBS snapshot createVolumePermission, and enabling S3 PublicAccessBlockConfiguration respectively. Optional stakeholder notification is available via the "Notify Stakeholders" sub-playbook by setting enableNotifications input to 'yes' (default: 'no'). When enabled, configure at least one recipient (email, Slack channel, or Teams channel) in the Notify Stakeholders playbook inputs. The playbook automatically updates the issue status to "Resolved - Fixed" upon successful remediation

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: Notify Stakeholders
- Integrations: AWS, Cortex Core - Platform
- Scripts: Print, Set
- Commands: aws-ec2-snapshot-attribute-modify, aws-rds-db-instance-modify, aws-s3-public-access-block-update, core-get-asset-details, setIssueStatus


## Azure - Network Security Group Remediation

**Product:** Azure Enrichment and Remediation

This playbook adds new Azure Network Security Groups (NSG) rules to NSGs attached to a NIC. The new rules will give access only to a private IP address range and block traffic that's exposed to the public internet (using the private IP of the VM as stated in Azure documentation). For example, if RDP is exposed to the public internet, this playbook adds new firewall rules that only allow traffic from private IP addresses and blocks the rest of the RDP traffic. Conditions and limitations

**Inputs:**

- `AzureSecurityGroup`: The Azure Network Security Group that will have new rules created or updated.
- `AzureVMPrivateIP`: The private IP of the Azure Virtual Machine.
- `RemoteProtocol`: The remote protocol that is publicly exposed.
- `RemotePort`: The remote port that is publicly exposed.
- `SubscriptionID`: The Azure subscription ID (optional).
- `ResourceGroup`: The Azure resource group (optional).
- `InstanceName`: Azure Network Security Groups integration instance to use if you have multiple instances configured (optional).
- `RemediationAllowRanges`: Comma-separated list of IPv4 network ranges to be used as source addresses for the `remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically this will be private IP 

**Outputs:**

- `remediatedFlag`
- `remediatedReason`

**Dependencies:**

- Integrations: Azure Network Security Groups
- Scripts: Set, AzureFindAvailableNSGPriorities
- Commands: azure-nsg-security-rule-update, azure-nsg-security-rule-create, azure-nsg-security-rules-list


## Azure - VM Instance Network Security Group Remediation

**Product:** Cloud Security Policy Management

This playbook adds new Azure Network Security Group (NSG) rules to NSGs attached to a NIC. The new rules give access to only a private IP address range and block traffic exposed to the public internet using the private IP of the VM, as explained in the (Azure documentation). For example, if RDP is exposed to the public internet, this playbook adds new firewall rules that only allow traffic from private IP addresses and blocks the rest of the RDP traffic. Conditions and limitations

**Inputs:**

- `AssetID`: The asset ID of the VM Instance.
- `PublicIP`: The public IP address to remediate for public exposure.
- `RemoteProtocol`: The remote protocol that is publicly exposed.
- `RemotePort`: The remote port that is publicly exposed.
- `IntegrationInstance`: The Azure Network Security Groups integration instance to use if you have multiple instances configured (optional).
- `RemediationAllowRanges`: A comma-separated list of IPv4 network ranges to be used as source addresses for the `cortex-remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically these are priva

**Outputs:**

- `remediatedFlag`
- `remediation_action`

**Dependencies:**

- Integrations: Azure, Cortex Core - Platform
- Scripts: AzureIdentifyNSGExposureRule, Print, Set, SetAndHandleEmpty
- Commands: azure-vn-network-interface-get, azure-vn-public-ip-address-get, azure-vn-security-rule-create, azure-vn-security-rule-update, azure-vn-security-rules-list, core-get-asset-details


## Azure Network Exposure - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

This playbook remediates the following Azure Network Exposure detections

**Inputs:**

- `enableNotifications`: Options: yes/no Choose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify 

**Dependencies:**

- Sub-playbooks: Azure - Network Security Group Remediation v2, Notify Stakeholders
- Integrations: Cortex Core - Platform
- Scripts: Print
- Commands: core-get-issue-recommendations, setIssueStatus


## Azure Public Access Misconfiguration - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates 3 Azure public access misconfigurations: The playbook disables public access by setting allowBlobPublicAccess to false, configuring VM disk publicNetworkAccess to Disabled with a DenyAll policy, and updating the storage account default network access action to Deny. Optional stakeholder notification is available via the "Notify Stakeholders" sub-playbook by setting enableNotifications input to 'yes' (default: 'no'). When enabled, configure at least one recipient (email, Slack channel, or Teams channel) in the Notify Stakeholders playbook inputs. The playbook automatically updates the issue status to "Resolved - Fixed" upon successful remediation

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: Notify Stakeholders
- Integrations: Azure, Cortex Core - Platform
- Scripts: Print, Set
- Commands: azure-compute-disk-update, azure-storage-account-update, core-get-asset-details, setIssueStatus


## ChronicleAssets Investigation And Remediation - Chronicle

**Product:** Google SecOps

Performs enrichment and investigation of the ChronicleAsset type of indicators, provides an opportunity to remediate in case any of the ChronicleAsset information i.e., hostname or IP address is found to be malicious or suspicious, and sends out an email containing the list of isolated and potentially blocked entities. To select the indicators you want to add, go to playbook inputs, choose "from indicators" and set your query. For example, type:ChronicleAsset etc. The default playbook query is "type:ChronicleAsset". In case indicators with different query parameters are to be investigated, the query must be edited accordingly. This playbook needs to be used with caution as it might use up the integration’s API license when running large amounts of indicators

**Inputs:**

- `Indicator Query`: Indicators matching the indicator query will be used as playbook inputs.
- `chronicleasset_support_contact`: The support email address for the Chronicle asset.
- `auto_block_entities`: Autoblock the detected suspicious IP address(es). You can manuall set this as 'Yes' or 'No' here or you can set it in a 'Chronicle Auto Block Entities' custom incident field.
- `skip_entity_isolation`: Skip the isolation of entities. You can manually set this as 'Yes' or 'No' here or you can set it in a 'Chronicle Skip Entity Isolation' custom incident field.


## Commvault Suspicious File Activity Remediation

**Product:** Commvault Cloud

Playbook to disable data-aging on commvault client when a threat is detected

**Dependencies:**

- Integrations: CommvaultSecurityIQ
- Scripts: AssignAnalystToIncident
- Commands: closeInvestigation, setIncident, disable-data-aging


## Cortex ASM - Cortex Endpoint Remediation

**Product:** Cortex Attack Surface Management

This playbook is used to isolate a single  Endpoint (XSIAM/XDR) for remediation purposes

**Inputs:**

- `CortexEndpointID`: The ID of the Cortex Endpoint (XDR).

**Dependencies:**

- Integrations: Cortex Core - IR, Cortex XDR - IR
- Scripts: Set
- Commands: xdr-endpoint-isolate, core-isolate-endpoint


## Cortex ASM - On Prem Remediation

**Product:** Cortex Attack Surface Management

This playbook adds new block rule(s) to on-prem firewall vendors in order to block internet access for internet exposures. Conditions

**Inputs:**

- `RuleName`: Firewall rule name to look up in the company configuration setting for block rule.
- `RemoteIP`: IP address of the service.
- `RemoteProtocol`: Protocol of the service.
- `RemotePort`: Port number of the service.
- `DeviceGroup`: Device group of the firewall rule to lookup.
- `SecondaryDeviceGroup`: If the rule, address and service are created in the "Shared" location, we need to know what device-groups we can push to because it isn't possible to push to the "Shared" location.

**Dependencies:**

- Sub-playbooks: PAN-OS - Block Destination Service
- Integrations: Panorama
- Commands: pan-os-list-rules


## Cortex ASM - Remediation Confirmation Scan

**Product:** Cortex Attack Surface Management

This playbook handles ASM Remediation Confirmation Scan by first creating a scan for an existing service ID, if the scan does not already exist. It then polls for results of a successful or failed scan

**Dependencies:**

- Scripts: GridFieldSetup, GetTime
- Commands: asm-get-remediation-confirmation-scan-status, asm-start-remediation_confirmation_scan


## Cortex ASM - Remediation Guidance

**Product:** Cortex Attack Surface Management

This playbook pulls remediation guidance off of a list based on ASM RuleID to be used in service owner notifications (email or ticketing system)

**Inputs:**

- `IssueTypeID`: Attack surface management issue rule ID.

**Outputs:**

- `RemediationGuidance`

**Dependencies:**

- Commands: asm-get-attack-surface-rule, setAlert


## Cortex ASM - Remediation Objectives

**Product:** Cortex Attack Surface Management

Playbook that populates the remediation objectives field that is used to display the remediation actions to the end user

**Dependencies:**

- Scripts: Set, GridFieldSetup


## Cortex ASM - Remediation Path Rules

**Product:** Cortex Attack Surface Management

This playbook returns "RemediationAction" options based on the return from the Remediation Path Rules API, or defaults to data collection task

**Inputs:**

- `ExternallyDetectedProviders`: Providers of external service.
- `BypassDevCheck`: Determine whether to bypass the Dev Check in automated remediation criteria: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-Expander-User-Guide/Automated-Re

**Outputs:**

- `RemediationAction`
- `RPR_Timestamp`

**Dependencies:**

- Integrations: CortexAttackSurfaceManagement
- Scripts: GetTime, GridFieldSetup, Set, RemediationPathRuleEvaluation
- Commands: asm-list-remediation-rule


## Cortex ASM - Remediation

**Product:** Cortex Attack Surface Management

This playbook contains all the cloud provider sub playbooks for remediation

**Inputs:**

- `AWSAssumeRoleName`: If assuming roles for AWS, this is the name of the role to assume (should be the same for all organizations)

**Dependencies:**

- Sub-playbooks: AWS - Package Upgrade, AWS - Security Group Remediation v2, AWS - Unclaimed S3 Bucket Remediation, Azure - Network Security Group Remediation, Cortex ASM - Cortex Endpoint Remediation, Cortex ASM - On Prem Remediation, GCP - Firewall Remediation


## Cortex EM - Remediation

**Product:** Cortex Exposure Management

This playbook handles exposure issue remediation

**Inputs:**

- `AWSAssumeRoleName`: The name of the role to assume for AWS (should be the same for all organizations).

**Dependencies:**

- Sub-playbooks: AWS - Enrichment, AWS - Security Group Remediation v2, Cortex EM - Exposure Issue


## DSPM Multi-Cloud Risk Remediation

**Product:** DSPM

The playbook ensures efficient incident resolution and compliance with security policies by guiding the user through decision points based on incident type, such as empty storage assets or assets open to the world. It concludes by updating the incident status and closing the playbook upon resolution

**Inputs:**

- `defaultSlackUserName`: In the event that the risk asset tag is absent, the risk notice will be sent to this Slack user email address.
- `slackMessageLifetime`: Lifetime for slack notification (in seconds)
- `rerunTime`: Incident re-run time (in hours)

**Dependencies:**

- Sub-playbooks: DSPM Valid User Response, Send slack notificaton to user, Invalid response sending notification to user again, DSPM notify user in case of error
- Scripts: DSPMCreateSimpleSlackMessageBlock, DSPMCheckAndSetErrorEntries, IsIntegrationAvailable, DSPMIncidentList, DSPMExtractRiskDetails, DeleteContext, DSPMCreateRiskSlackBlocks, isError
- Commands: createList, setList, getList, addToList, closeInvestigation, core-api-post


## DSPM Remediation for Empty storage asset

**Product:** DSPM

This playbook is designed to remediate risks associated with empty storage assets across AWS, Azure, and GCP environments. It identifies the cloud provider for the asset and proceeds to delete the storage container or bucket accordingly. Additionally, it sends notifications via Slack to inform stakeholders about the status of the remediation process

**Dependencies:**

- Integrations: AWS - S3, DSPM, Google Cloud Storage
- Scripts: IsIntegrationAvailable, DSPMIncidentList, DSPMCheckAndSetErrorEntries, DeleteContext, DSPMCreateSimpleSlackMessageBlock
- Commands: aws-s3-delete-bucket, dspm-update-risk-finding-status, gcs-delete-bucket, setList


## DSPM Remediation for Sensitive asset open to world

**Product:** DSPM

The DSPM Remediation Playbook for Sensitive Asset Open to World is designed to handle incidents where sensitive assets are exposed to the public, with specific focus on remediating this vulnerability across different cloud providers (AWS). Below is an overview of the key steps and actions included in this playbook

**Dependencies:**

- Integrations: DSPM, Google Cloud Storage, AWS - S3, Azure Storage Container
- Scripts: DSPMIncidentList, DSPMCreateSimpleSlackMessageBlock, DSPMCheckAndSetErrorEntries, DeleteContext, DSPMGetContianers, IsIntegrationAvailable
- Commands: dspm-update-risk-finding-status, setList, aws-s3-put-public-access-block, gcs-block-public-access-bucket, azure-storage-container-block-public-access, dspm-get-asset-files-by-id


## ETD Email Reclassification And Remediation

**Product:** ETD the platform Connector

Allows analysts to review Cisco ETD emails, reclassify message verdicts, and perform remediation actions

**Dependencies:**

- Integrations: ETDConnector
- Scripts: IsIntegrationAvailable, Print
- Commands: cisco-etd-move-message


## GCP - Firewall Remediation

**Product:** GCP Enrichment and Remediation

This playbook adds new firewall rules with access only from private ip address range and blocks traffic that's exposed to public internet. For example, if RDP is exposed to the entire world, this playbook adds new firewall rules that only allows traffic from private ip address and blocks rest of the RDP traffic

**Inputs:**

- `GcpInstance`: The name of the GCP instance that has the public ip.
- `GcpZone`: The zone of the GCP instance that is hosted in.
- `GcpNetwork`: The VPC network of the GCP instance.
- `RemotePort`: The remote port that is publicly exposed to.
- `RemoteProtocol`: The remote protocol that is publicly exposed to.
- `GcpProject`: The name of the GCP project associated with the instance and related objects.
- `instance_name`: Google Cloud Compute integration instance to use if you have multiple instances configured (optional).

**Dependencies:**

- Integrations: Google Cloud Compute
- Scripts: Set
- Commands: gcp-compute-list-firewall, gcp-compute-insert-firewall, gcp-compute-add-network-tag, gcp-compute-get-instance


## GCP - VM Instance Firewall Rule Remediation

**Product:** Cloud Security Policy Management

This playbook adds new VPC firewall rules to restrict access to private IP address ranges and block traffic exposed to the public internet. For example, if RDP is exposed this playbook adds new firewall rules that allow traffic only from private IP addresses and it blocks all other RDP traffic. New allow and block rules created by this playbook target only the exposed asset

**Inputs:**

- `AssetID`: The asset ID of the VM instance.
- `RemotePort`: The remote port that is publicly exposed.
- `RemoteProtocol`: The remote protocol that is publicly exposed.
- `IntegrationInstance`: The GCP integration instance to use if multiple instances are configured (optional).
- `RemediationAllowRanges`: A comma-separated list of IPv4 network ranges to be used as source addresses for the `cortex-remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically these are priva

**Outputs:**

- `remediatedFlag`
- `remediation_action`

**Dependencies:**

- Integrations: Cortex Core - Platform, GCP
- Scripts: Print, Set
- Commands: core-get-asset-details, gcp-compute-firewall-insert, gcp-compute-firewall-list, gcp-compute-instance-get, gcp-compute-network-tag-set


## GCP Network Exposure - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates the following Network Exposure detection

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: GCP - VM Instance Firewall Rule Remediation, Notify Stakeholders
- Integrations: Cortex Core - Platform
- Scripts: Print
- Commands: core-get-issue-recommendations, setIssueStatus


## GCP Public Access Misconfiguration - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates 2 GCP public access misconfigurations: The playbook removes public IAM policy bindings by deleting 'allUsers' and 'allAuthenticatedUsers' entities from the bucket's Access Control List respectively. Optional stakeholder notification is available via the "Notify Stakeholders" sub-playbook by setting enableNotifications input to 'yes' (default: 'no'). When enabled, configure at least one recipient (email, Slack channel, or Teams channel) in the Notify Stakeholders playbook inputs. The playbook automatically updates the issue status to "Resolved - Fixed" upon successful remediation

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: Notify Stakeholders
- Integrations: Cortex Core - Platform, GCP
- Scripts: Print, Set
- Commands: core-get-asset-details, gcp-storage-bucket-policy-delete, setIssueStatus


## Hostname And IP Address Investigation And Remediation - Chronicle

**Product:** Google SecOps

This playbook receives ChronicleAsset type of indicators from its parent playbook "ChronicleAsset Investigation - Chronicle", performs enrichment and investigation for each one of them, provides an opportunity to isolate and block the hostname or IP address associated with the current indicator, and provides a list of isolated and blocked entities

**Inputs:**

- `chronicleasset_value`: The value of the ChronicleAsset indicator.
- `chronicleasset_hostname`: The hostname associated with the ChronicleAsset.
- `chronicleasset_ip`: The IP address associated with the ChronicleAsset.
- `chronicleasset_support_contact`: The support email address for the ChronicleAsset.
- `auto_block_entities`: Autoblock the detected suspicious IP Address(es). You can manually set this as "Yes" or "No" here or you can set it in a 'Chronicle Auto Block Entities' custom incident field.
- `skip_entity_isolation`: Skip the isolation of entities. You can manually set this as "Yes" or "No" here or you can set it in a 'Chronicle Skip Entity Isolation' custom incident field.

**Outputs:**

- `IsolatedEntities`
- `PotentiallyBlockedIPs`

**Dependencies:**

- Sub-playbooks: IP Enrichment - Generic v2, Isolate Endpoint - Generic, Block IP - Generic v2, Isolate Endpoint - Generic V2, Endpoint Enrichment - Generic v2.1
- Integrations: GoogleChronicleBackstory
- Scripts: DeleteContext, Set
- Commands: df-get-asset, setIndicator, ip


## Prisma Cloud Remediation - AWS CloudTrail is not Enabled on the Account

**Product:** Prisma Cloud by Palo Alto Networks

AWS Cloudtrail is a service which provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. To remediate Prisma Cloud Alert "CloudTrail is not enabled on the account", this playbook creates an S3 bucket to host Cloudtrail logs and enable Cloudtrail (includes all region events and global service events)

**Inputs:**

- `AutoEnableCloudTrail`: The following resources will be created:- S3 bucket cloudtrail-<account_id>- Cloudtrail cloudtrail-<account_id>Type 'Yes' to auto-enable CloudTrail.
- `CloudTrailRegion`: S3 bucket and (global) Cloudtrail will be created on this region

**Dependencies:**

- Commands: aws-s3-put-bucket-policy, aws-cloudtrail-start-logging, aws-cloudtrail-create-trail, aws-s3-create-bucket


## Prisma Cloud Remediation - AWS CloudTrail Is Not Integrated With CloudWatch Logs

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud AWS CloudTrail alerts. Prisma Cloud policies remediated

**Dependencies:**

- Integrations: AWS - CloudTrail, AWS - CloudWatchLogs, AWS - IAM
- Scripts: Sleep, isError
- Commands: aws-cloudtrail-describe-trails, aws-cloudtrail-update-trail, aws-iam-attach-policy, aws-iam-create-policy, aws-iam-create-role, aws-iam-get-role, aws-logs-create-log-group, aws-logs-describe-log-groups


## Prisma Cloud Remediation - AWS CloudTrail Trail Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud AWS CloudTrail alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Grab the Prisma Cloud policy Id.

**Dependencies:**

- Integrations: AWS - CloudTrail
- Commands: aws-cloudtrail-update-trail, aws-cloudtrail-describe-trails


## Prisma Cloud Remediation - AWS EC2 Security Group Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

Remediates the Prisma Cloud AWS EC2 alerts generated by the following policies

**Inputs:**

- `policyId`: Returns the Prisma Cloud policy ID.

**Dependencies:**

- Scripts: isError, Sleep
- Commands: aws-ec2-revoke-security-group-ingress-rule, aws-ec2-describe-security-groups


## Prisma Cloud Remediation - AWS IAM Password Policy Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

Remediates the following Prisma Cloud AWS IAM password policy alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Returns the Prisma Cloud policy ID.

**Dependencies:**

- Commands: aws-iam-update-account-password-policy


## Prisma Cloud Remediation - AWS IAM User Policy Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud AWS IAM User alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Scripts: Print
- Commands: aws-iam-list-access-keys-for-user, aws-iam-update-access-key


## Prisma Cloud Remediation - AWS Inactive Users For More Than 30 Days

**Product:** Prisma Cloud by Palo Alto Networks

Remediates Prisma Cloud Alert inactive users for more than 30 days, this playbook deactivates the user by disabling the access keys (marking them as inactive) as well as resetting the user console password. To increase the security of your AWS account, it is recommended to find and remove IAM user credentials (passwords, access keys) that have not been used within a specified period of time

**Inputs:**

- `AutoQuarantine`: Can be, "yes" - access keys will be disabled and password reset, or "no" - an analyst will be prompted for action.

**Dependencies:**

- Integrations: Builtin
- Scripts: Print
- Commands: aws-iam-update-login-profile, closeInvestigation, aws-iam-list-access-keys-for-user, aws-iam-update-access-key


## Prisma Cloud Remediation - AWS Security Groups Allows Internet Traffic To TCP Port

**Product:** Prisma Cloud by Palo Alto Networks

Extracts the TCP public Security Groups rule and provides manual/automatic options to have the rules revoked

**Inputs:**

- `AutoRevokeRule`: Can be, "yes" - public security group rules will be automatically revoked, or "no" - analyst will be prompted whether or not to allow automatic removal of the rules.

**Dependencies:**

- Integrations: Builtin, AWS - EC2
- Scripts: AwsEC2GetPublicSGRules
- Commands: aws-ec2-revoke-security-group-ingress-rule, aws-ec2-describe-security-groups, closeInvestigation


## Prisma Cloud Remediation - Azure AKS Cluster Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure AKS cluster alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Outputs:**

- `incident.labels.resource.name`

**Dependencies:**

- Integrations: Azure Kubernetes Services
- Scripts: IsIntegrationAvailable
- Commands: azure-ks-cluster-addon-update


## Prisma Cloud Remediation - Azure Network Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud Azure Network alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateAzureNetwork`: Execute Azure Network remediation automatically?
- `policyId`: Grab the Prisma Cloud policy ID.
- `portNumber`: Port number.

**Outputs:**

- `incident.resourcename`

**Dependencies:**

- Commands: closeInvestigation, prisma-cloud-alert-dismiss


## Prisma Cloud Remediation - Azure Network Security Group Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure Network security group alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.
- `portNumber`: Port number.

**Outputs:**

- `incident.resourcename`

**Dependencies:**

- Integrations: Azure Network Security Groups
- Scripts: IsIntegrationAvailable, Set
- Commands: azure-nsg-security-rule-delete


## Prisma Cloud Remediation - Azure SQL Database Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure SQL database alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Azure SQL Management
- Scripts: IsIntegrationAvailable
- Commands: azure-sql-db-threat-policy-create-update, azure-sql-db-audit-policy-create-update


## Prisma Cloud Remediation - Azure SQL Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud Azure SQL alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateAzureSQL`: Execute Azure SQL remediation automatically?
- `policyId`: Grab the Prisma Cloud policy ID.

**Dependencies:**

- Commands: prisma-cloud-alert-dismiss, closeInvestigation


## Prisma Cloud Remediation - Azure Storage Blob Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure Storage blob alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Azure Storage
- Scripts: IsIntegrationAvailable
- Commands: azure-storage-account-create-update


## Prisma Cloud Remediation - GCP Compute Engine Instance Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP Compute Engine VM Instance alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Google Cloud Compute
- Commands: gcp-compute-get-instance, gcp-compute-set-instance-metadata


## Prisma Cloud Remediation - GCP Compute Engine Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud GCP Compute Engine alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateComputeEngine`: Execute GCP Compute Engine remediation automatically?
- `policyId`: Grab the Prima Cloud policy ID.

**Dependencies:**

- Commands: closeInvestigation, prisma-cloud-alert-dismiss


## Prisma Cloud Remediation - GCP Kubernetes Engine Cluster Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP Kubernetes Engine Cluster alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: GoogleKubernetesEngine
- Commands: gcloud-clusters-set-muster-auth, gcloud-clusters-describe, gcloud-clusters-set-binary-auth, gcloud-clusters-set-intra-node-visibility, gcloud-clusters-set-legacy-auth, gcloud-clusters-set-master-authorized-network, gcloud-clusters-set-k8s-stackdriver, gcloud-clusters-set-addons


## Prisma Cloud Remediation - GCP Kubernetes Engine Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud GCP Kubernetes Engine alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateKubernetesEngine`: Execute GCP Kubernetes Engine remediation automatically?
- `policyId`: Grab the Prima Cloud policy ID.

**Dependencies:**

- Commands: prisma-cloud-alert-dismiss, closeInvestigation


## Prisma Cloud Remediation - GCP VPC Network Firewall Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP VPC Network Firewall alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Google Cloud Compute
- Commands: gcp-compute-get-firewall, gcp-compute-patch-firewall


## Prisma Cloud Remediation - GCP VPC Network Project Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP VPC Network Project alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Google Cloud Compute
- Scripts: isError
- Commands: gcp-compute-get-network, gcp-compute-delete-network


## Remediate Message - Agari Phishing Defense

**Product:** Agari Phishing Defense

Remediates a given message id. Supported   versions: 5.0.0 and later

**Inputs:**

- `id`: Id of message to remediate.
- `auto_remediation`: Flag for whether to automatically remediate or not.
- `remediate_action`: Action for remediation.

**Dependencies:**

- Commands: apd-remediate-message


## Rubrik IR Violation Remediation - Rubrik Security Cloud

**Product:** Rubrik Security Cloud

This playbook remediates Identity Resilience (IR) violations by retrieving the latest violation details and updating the violation status

**Inputs:**

- `violation_id`: The ID of the IR violation.Note: Users can get the violation ID by executing the "rubrik-identity-resilience-violation-list" command.
- `policy_type`: The policy type of the violation.Note: Users can get the policy type by executing the "rubrik-identity-resilience-violation-list" command.Possible values are: IDENTITY, IDP,IDENTIT

**Dependencies:**

- Scripts: DeleteContext, RubrikPullIRViolationInformation, Set
- Commands: rubrik-identity-resilience-violation-status-update


## SaaS Security - Remediate an Asset

**Product:** SaaS Security by Palo Alto Networks

Take a remediation action over an asset: Use this playbook as a sub-playbook to take a remediation action on an asset. Available remediation actions are 1) Remove public sharing, 2) Quarantine, and 3) Restore. This playbook implements polling by continuously running the saas-security-remediation-status-get command to get the remediation status for a given asset ID, until the operation completes. The remote action should have the following structure

**Inputs:**

- `asset_id`: The ID of the asset to remediate
- `remediation_type`: The remediation action to take.Possible values: Remove public sharing, Quarantine, Restore.
- `remove_inherited_sharing`: Used when remediation type is “remove_public_sharing”, when set to true, all the parent folder sharing url will be removed.

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: SaaS Security
- Commands: saas-security-remediation-status-get, saas-security-asset-remediate

## Agari Message Remediation - Agari Phishing Defense

**Product:** Agari Phishing Defense

Investigates Agari policy events by obtaining the original message and attachments from the existing email integrations and remediates in Agari. Supported   versions: 5.0.0 and later

**Inputs:**

- `APD Global Message ID`: Global Message Id obtained from the incident.
- `AuthenticateEmail`: Whether the authenticity of the email should be verified, using Authenticity Score.
- `OnCall`: Set to true to assign only user that is currently on shift. Requires the platform.5 or later.
- `Role`: The default role to assign the incident to.
- `ResolveIP`: Resolve IP addresses to hostnames (DNS).
- `AutoRemeditaion`: Whether Automatic remediate message or not.
- `RemediateAction`: Default action for remediation of message.
- `UserEnrichmentEnable`: Flag for enabling User Enrichment.
- `User Id`: Id of User.
- `APD Internal Message ID`: Internal Message Id obtained from the incident.

**Dependencies:**

- Sub-playbooks: Entity Enrichment - Phishing v2, Extract Indicators From File - Generic v2, Email Address Enrichment - Generic v2.1, Retrieve Email Data - Agari Phishing Defense, Calculate Severity - Generic v2, Process Email - Generic, Remediate Message - Agari Phishing Defense, Detonate File - Generic
- Scripts: AssignAnalystToIncident, Set, CheckEmailAuthenticity
- Commands: closeInvestigation, setIncident


## AWS - EC2 Instance Security Group Remediation

**Product:** Cloud Security Policy Management

This playbook identifies the security groups used on an EC2 interface with a specific public IP. It determines which rules allow access via the given port and protocol, creates a copy of the security groups with those rules removed, and updates the interface to use the modified security groups. The original security groups are left unmodified, and the remediated copy is applied to the exposed EC2 instance

**Inputs:**

- `AssetID`: The asset ID of the VM Instance.
- `PublicIP`: The public IP address to remediate for public exposure.
- `RemotePort`: The TCP/UDP port number to be restricted.
- `RemoteProtocol`: The protocol to be restricted (tcp/udp).
- `RemediationAllowRanges`: A comma-separated list of IPv4 network ranges to be used as source addresses for the `cortex-remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically these are priva
- `IntegrationInstance`: The AWS integration instance to use if multiple instances are configured (optional).

**Outputs:**

- `remediatedFlag`
- `remediation_action`

**Dependencies:**

- Integrations: AWS, Cortex Core - Platform
- Scripts: AWSIdentifySGPublicExposure, AWSRemediateSG, GetTime, Print, Set
- Commands: aws-ec2-network-interface-attribute-modify, core-get-asset-details


## AWS - Security Group Remediation v2

**Product:** AWS Enrichment and Remediation

This playbook takes in some information about an EC2 instance (ID and public_ip) and with provided port and protocol, determines what security groups on the primary interface of an EC2 instance are over-permissive. It uses an automation to determine what interface on an EC2 instance has an over-permissive security group on, determine which security groups have over-permissive rules and to replace them with a copy of the security group that has only the over-permissive portion removed. Over-permissive is defined as sensitive ports (SSH, RDP, etc) being exposed to the internet via IPv4

**Inputs:**

- `InstanceID`: ID of the AWS EC2 instance.
- `Port`: TCP/UDP port to be restricted.
- `Protocol`: Protocol of the port to be restricted.
- `PublicIP`: Public IP address of the EC2 instance.
- `AWSAssumeArn`: Name of an AWS role to assume (should be the same for all organizations).
- `Region`: Region where EC2 instance is present.

**Dependencies:**

- Scripts: AWSRecreateSG


## AWS - Unclaimed S3 Bucket Remediation

**Product:** AWS Enrichment and Remediation

The playbook will create the unclaimed S3 bucket

**Inputs:**

- `S3BucketName`: Unclaimed S3 bucket name.

**Dependencies:**

- Integrations: AWS - S3
- Commands: aws-s3-list-buckets, aws-s3-create-bucket


## AWS Network Exposure - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

This playbook remediates the following AWS Network Exposure detections

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Outputs:**

- `remediatedFlag`

**Dependencies:**

- Sub-playbooks: AWS - EC2 Instance Security Group Remediation, Notify Stakeholders
- Integrations: Cortex Core - Platform
- Scripts: Print
- Commands: core-get-issue-recommendations, setIssueStatus


## AWS Public Access Misconfiguration - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates 9 AWS public access misconfigurations: 1 RDS database, 1 EBS snapshot, and 7 S3 bucket issues: The playbook disables public access by modifying RDS publicly_accessible settings, removing EBS snapshot createVolumePermission, and enabling S3 PublicAccessBlockConfiguration respectively. Optional stakeholder notification is available via the "Notify Stakeholders" sub-playbook by setting enableNotifications input to 'yes' (default: 'no'). When enabled, configure at least one recipient (email, Slack channel, or Teams channel) in the Notify Stakeholders playbook inputs. The playbook automatically updates the issue status to "Resolved - Fixed" upon successful remediation

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: Notify Stakeholders
- Integrations: AWS, Cortex Core - Platform
- Scripts: Print, Set
- Commands: aws-ec2-snapshot-attribute-modify, aws-rds-db-instance-modify, aws-s3-public-access-block-update, core-get-asset-details, setIssueStatus


## Azure - Network Security Group Remediation

**Product:** Azure Enrichment and Remediation

This playbook adds new Azure Network Security Groups (NSG) rules to NSGs attached to a NIC. The new rules will give access only to a private IP address range and block traffic that's exposed to the public internet (using the private IP of the VM as stated in Azure documentation). For example, if RDP is exposed to the public internet, this playbook adds new firewall rules that only allow traffic from private IP addresses and blocks the rest of the RDP traffic. Conditions and limitations

**Inputs:**

- `AzureSecurityGroup`: The Azure Network Security Group that will have new rules created or updated.
- `AzureVMPrivateIP`: The private IP of the Azure Virtual Machine.
- `RemoteProtocol`: The remote protocol that is publicly exposed.
- `RemotePort`: The remote port that is publicly exposed.
- `SubscriptionID`: The Azure subscription ID (optional).
- `ResourceGroup`: The Azure resource group (optional).
- `InstanceName`: Azure Network Security Groups integration instance to use if you have multiple instances configured (optional).
- `RemediationAllowRanges`: Comma-separated list of IPv4 network ranges to be used as source addresses for the `remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically this will be private IP 

**Outputs:**

- `remediatedFlag`
- `remediatedReason`

**Dependencies:**

- Integrations: Azure Network Security Groups
- Scripts: Set, AzureFindAvailableNSGPriorities
- Commands: azure-nsg-security-rule-update, azure-nsg-security-rule-create, azure-nsg-security-rules-list


## Azure - VM Instance Network Security Group Remediation

**Product:** Cloud Security Policy Management

This playbook adds new Azure Network Security Group (NSG) rules to NSGs attached to a NIC. The new rules give access to only a private IP address range and block traffic exposed to the public internet using the private IP of the VM, as explained in the (Azure documentation). For example, if RDP is exposed to the public internet, this playbook adds new firewall rules that only allow traffic from private IP addresses and blocks the rest of the RDP traffic. Conditions and limitations

**Inputs:**

- `AssetID`: The asset ID of the VM Instance.
- `PublicIP`: The public IP address to remediate for public exposure.
- `RemoteProtocol`: The remote protocol that is publicly exposed.
- `RemotePort`: The remote port that is publicly exposed.
- `IntegrationInstance`: The Azure Network Security Groups integration instance to use if you have multiple instances configured (optional).
- `RemediationAllowRanges`: A comma-separated list of IPv4 network ranges to be used as source addresses for the `cortex-remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically these are priva

**Outputs:**

- `remediatedFlag`
- `remediation_action`

**Dependencies:**

- Integrations: Azure, Cortex Core - Platform
- Scripts: AzureIdentifyNSGExposureRule, Print, Set, SetAndHandleEmpty
- Commands: azure-vn-network-interface-get, azure-vn-public-ip-address-get, azure-vn-security-rule-create, azure-vn-security-rule-update, azure-vn-security-rules-list, core-get-asset-details


## Azure Network Exposure - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

This playbook remediates the following Azure Network Exposure detections

**Inputs:**

- `enableNotifications`: Options: yes/no Choose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify 

**Dependencies:**

- Sub-playbooks: Azure - Network Security Group Remediation v2, Notify Stakeholders
- Integrations: Cortex Core - Platform
- Scripts: Print
- Commands: core-get-issue-recommendations, setIssueStatus


## Azure Public Access Misconfiguration - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates 3 Azure public access misconfigurations: The playbook disables public access by setting allowBlobPublicAccess to false, configuring VM disk publicNetworkAccess to Disabled with a DenyAll policy, and updating the storage account default network access action to Deny. Optional stakeholder notification is available via the "Notify Stakeholders" sub-playbook by setting enableNotifications input to 'yes' (default: 'no'). When enabled, configure at least one recipient (email, Slack channel, or Teams channel) in the Notify Stakeholders playbook inputs. The playbook automatically updates the issue status to "Resolved - Fixed" upon successful remediation

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: Notify Stakeholders
- Integrations: Azure, Cortex Core - Platform
- Scripts: Print, Set
- Commands: azure-compute-disk-update, azure-storage-account-update, core-get-asset-details, setIssueStatus


## ChronicleAssets Investigation And Remediation - Chronicle

**Product:** Google SecOps

Performs enrichment and investigation of the ChronicleAsset type of indicators, provides an opportunity to remediate in case any of the ChronicleAsset information i.e., hostname or IP address is found to be malicious or suspicious, and sends out an email containing the list of isolated and potentially blocked entities. To select the indicators you want to add, go to playbook inputs, choose "from indicators" and set your query. For example, type:ChronicleAsset etc. The default playbook query is "type:ChronicleAsset". In case indicators with different query parameters are to be investigated, the query must be edited accordingly. This playbook needs to be used with caution as it might use up the integration’s API license when running large amounts of indicators

**Inputs:**

- `Indicator Query`: Indicators matching the indicator query will be used as playbook inputs.
- `chronicleasset_support_contact`: The support email address for the Chronicle asset.
- `auto_block_entities`: Autoblock the detected suspicious IP address(es). You can manuall set this as 'Yes' or 'No' here or you can set it in a 'Chronicle Auto Block Entities' custom incident field.
- `skip_entity_isolation`: Skip the isolation of entities. You can manually set this as 'Yes' or 'No' here or you can set it in a 'Chronicle Skip Entity Isolation' custom incident field.


## Commvault Suspicious File Activity Remediation

**Product:** Commvault Cloud

Playbook to disable data-aging on commvault client when a threat is detected

**Dependencies:**

- Integrations: CommvaultSecurityIQ
- Scripts: AssignAnalystToIncident
- Commands: closeInvestigation, setIncident, disable-data-aging


## Cortex ASM - Cortex Endpoint Remediation

**Product:** Cortex Attack Surface Management

This playbook is used to isolate a single  Endpoint (XSIAM/XDR) for remediation purposes

**Inputs:**

- `CortexEndpointID`: The ID of the Cortex Endpoint (XDR).

**Dependencies:**

- Integrations: Cortex Core - IR, Cortex XDR - IR
- Scripts: Set
- Commands: xdr-endpoint-isolate, core-isolate-endpoint


## Cortex ASM - On Prem Remediation

**Product:** Cortex Attack Surface Management

This playbook adds new block rule(s) to on-prem firewall vendors in order to block internet access for internet exposures. Conditions

**Inputs:**

- `RuleName`: Firewall rule name to look up in the company configuration setting for block rule.
- `RemoteIP`: IP address of the service.
- `RemoteProtocol`: Protocol of the service.
- `RemotePort`: Port number of the service.
- `DeviceGroup`: Device group of the firewall rule to lookup.
- `SecondaryDeviceGroup`: If the rule, address and service are created in the "Shared" location, we need to know what device-groups we can push to because it isn't possible to push to the "Shared" location.

**Dependencies:**

- Sub-playbooks: PAN-OS - Block Destination Service
- Integrations: Panorama
- Commands: pan-os-list-rules


## Cortex ASM - Remediation Confirmation Scan

**Product:** Cortex Attack Surface Management

This playbook handles ASM Remediation Confirmation Scan by first creating a scan for an existing service ID, if the scan does not already exist. It then polls for results of a successful or failed scan

**Dependencies:**

- Scripts: GridFieldSetup, GetTime
- Commands: asm-get-remediation-confirmation-scan-status, asm-start-remediation_confirmation_scan


## Cortex ASM - Remediation Guidance

**Product:** Cortex Attack Surface Management

This playbook pulls remediation guidance off of a list based on ASM RuleID to be used in service owner notifications (email or ticketing system)

**Inputs:**

- `IssueTypeID`: Attack surface management issue rule ID.

**Outputs:**

- `RemediationGuidance`

**Dependencies:**

- Commands: asm-get-attack-surface-rule, setAlert


## Cortex ASM - Remediation Objectives

**Product:** Cortex Attack Surface Management

Playbook that populates the remediation objectives field that is used to display the remediation actions to the end user

**Dependencies:**

- Scripts: Set, GridFieldSetup


## Cortex ASM - Remediation Path Rules

**Product:** Cortex Attack Surface Management

This playbook returns "RemediationAction" options based on the return from the Remediation Path Rules API, or defaults to data collection task

**Inputs:**

- `ExternallyDetectedProviders`: Providers of external service.
- `BypassDevCheck`: Determine whether to bypass the Dev Check in automated remediation criteria: https://docs-cortex.paloaltonetworks.com/r/Cortex-XPANSE/Cortex-Xpanse-Expander-User-Guide/Automated-Re

**Outputs:**

- `RemediationAction`
- `RPR_Timestamp`

**Dependencies:**

- Integrations: CortexAttackSurfaceManagement
- Scripts: GetTime, GridFieldSetup, Set, RemediationPathRuleEvaluation
- Commands: asm-list-remediation-rule


## Cortex ASM - Remediation

**Product:** Cortex Attack Surface Management

This playbook contains all the cloud provider sub playbooks for remediation

**Inputs:**

- `AWSAssumeRoleName`: If assuming roles for AWS, this is the name of the role to assume (should be the same for all organizations)

**Dependencies:**

- Sub-playbooks: AWS - Package Upgrade, AWS - Security Group Remediation v2, AWS - Unclaimed S3 Bucket Remediation, Azure - Network Security Group Remediation, Cortex ASM - Cortex Endpoint Remediation, Cortex ASM - On Prem Remediation, GCP - Firewall Remediation


## Cortex EM - Remediation

**Product:** Cortex Exposure Management

This playbook handles exposure issue remediation

**Inputs:**

- `AWSAssumeRoleName`: The name of the role to assume for AWS (should be the same for all organizations).

**Dependencies:**

- Sub-playbooks: AWS - Enrichment, AWS - Security Group Remediation v2, Cortex EM - Exposure Issue


## DSPM Multi-Cloud Risk Remediation

**Product:** DSPM

The playbook ensures efficient incident resolution and compliance with security policies by guiding the user through decision points based on incident type, such as empty storage assets or assets open to the world. It concludes by updating the incident status and closing the playbook upon resolution

**Inputs:**

- `defaultSlackUserName`: In the event that the risk asset tag is absent, the risk notice will be sent to this Slack user email address.
- `slackMessageLifetime`: Lifetime for slack notification (in seconds)
- `rerunTime`: Incident re-run time (in hours)

**Dependencies:**

- Sub-playbooks: DSPM Valid User Response, Send slack notificaton to user, Invalid response sending notification to user again, DSPM notify user in case of error
- Scripts: DSPMCreateSimpleSlackMessageBlock, DSPMCheckAndSetErrorEntries, IsIntegrationAvailable, DSPMIncidentList, DSPMExtractRiskDetails, DeleteContext, DSPMCreateRiskSlackBlocks, isError
- Commands: createList, setList, getList, addToList, closeInvestigation, core-api-post


## DSPM Remediation for Empty storage asset

**Product:** DSPM

This playbook is designed to remediate risks associated with empty storage assets across AWS, Azure, and GCP environments. It identifies the cloud provider for the asset and proceeds to delete the storage container or bucket accordingly. Additionally, it sends notifications via Slack to inform stakeholders about the status of the remediation process

**Dependencies:**

- Integrations: AWS - S3, DSPM, Google Cloud Storage
- Scripts: IsIntegrationAvailable, DSPMIncidentList, DSPMCheckAndSetErrorEntries, DeleteContext, DSPMCreateSimpleSlackMessageBlock
- Commands: aws-s3-delete-bucket, dspm-update-risk-finding-status, gcs-delete-bucket, setList


## DSPM Remediation for Sensitive asset open to world

**Product:** DSPM

The DSPM Remediation Playbook for Sensitive Asset Open to World is designed to handle incidents where sensitive assets are exposed to the public, with specific focus on remediating this vulnerability across different cloud providers (AWS). Below is an overview of the key steps and actions included in this playbook

**Dependencies:**

- Integrations: DSPM, Google Cloud Storage, AWS - S3, Azure Storage Container
- Scripts: DSPMIncidentList, DSPMCreateSimpleSlackMessageBlock, DSPMCheckAndSetErrorEntries, DeleteContext, DSPMGetContianers, IsIntegrationAvailable
- Commands: dspm-update-risk-finding-status, setList, aws-s3-put-public-access-block, gcs-block-public-access-bucket, azure-storage-container-block-public-access, dspm-get-asset-files-by-id


## ETD Email Reclassification And Remediation

**Product:** ETD the platform Connector

Allows analysts to review Cisco ETD emails, reclassify message verdicts, and perform remediation actions

**Dependencies:**

- Integrations: ETDConnector
- Scripts: IsIntegrationAvailable, Print
- Commands: cisco-etd-move-message


## GCP - Firewall Remediation

**Product:** GCP Enrichment and Remediation

This playbook adds new firewall rules with access only from private ip address range and blocks traffic that's exposed to public internet. For example, if RDP is exposed to the entire world, this playbook adds new firewall rules that only allows traffic from private ip address and blocks rest of the RDP traffic

**Inputs:**

- `GcpInstance`: The name of the GCP instance that has the public ip.
- `GcpZone`: The zone of the GCP instance that is hosted in.
- `GcpNetwork`: The VPC network of the GCP instance.
- `RemotePort`: The remote port that is publicly exposed to.
- `RemoteProtocol`: The remote protocol that is publicly exposed to.
- `GcpProject`: The name of the GCP project associated with the instance and related objects.
- `instance_name`: Google Cloud Compute integration instance to use if you have multiple instances configured (optional).

**Dependencies:**

- Integrations: Google Cloud Compute
- Scripts: Set
- Commands: gcp-compute-list-firewall, gcp-compute-insert-firewall, gcp-compute-add-network-tag, gcp-compute-get-instance


## GCP - VM Instance Firewall Rule Remediation

**Product:** Cloud Security Policy Management

This playbook adds new VPC firewall rules to restrict access to private IP address ranges and block traffic exposed to the public internet. For example, if RDP is exposed this playbook adds new firewall rules that allow traffic only from private IP addresses and it blocks all other RDP traffic. New allow and block rules created by this playbook target only the exposed asset

**Inputs:**

- `AssetID`: The asset ID of the VM instance.
- `RemotePort`: The remote port that is publicly exposed.
- `RemoteProtocol`: The remote protocol that is publicly exposed.
- `IntegrationInstance`: The GCP integration instance to use if multiple instances are configured (optional).
- `RemediationAllowRanges`: A comma-separated list of IPv4 network ranges to be used as source addresses for the `cortex-remediation-allow-port-<port#>-<tcp|udp>` rule to be created. Typically these are priva

**Outputs:**

- `remediatedFlag`
- `remediation_action`

**Dependencies:**

- Integrations: Cortex Core - Platform, GCP
- Scripts: Print, Set
- Commands: core-get-asset-details, gcp-compute-firewall-insert, gcp-compute-firewall-list, gcp-compute-instance-get, gcp-compute-network-tag-set


## GCP Network Exposure - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates the following Network Exposure detection

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: GCP - VM Instance Firewall Rule Remediation, Notify Stakeholders
- Integrations: Cortex Core - Platform
- Scripts: Print
- Commands: core-get-issue-recommendations, setIssueStatus


## GCP Public Access Misconfiguration - Auto-remediate

**Product:** Cloud Security Posture Management Playbooks

Automatically remediates 2 GCP public access misconfigurations: The playbook removes public IAM policy bindings by deleting 'allUsers' and 'allAuthenticatedUsers' entities from the bucket's Access Control List respectively. Optional stakeholder notification is available via the "Notify Stakeholders" sub-playbook by setting enableNotifications input to 'yes' (default: 'no'). When enabled, configure at least one recipient (email, Slack channel, or Teams channel) in the Notify Stakeholders playbook inputs. The playbook automatically updates the issue status to "Resolved - Fixed" upon successful remediation

**Inputs:**

- `enableNotifications`: Options: yes/noChoose if you wish to notify stakeholders about the remediation actions taken. The recipients need to be configured in the Playbook Triggered header of the "Notify S

**Dependencies:**

- Sub-playbooks: Notify Stakeholders
- Integrations: Cortex Core - Platform, GCP
- Scripts: Print, Set
- Commands: core-get-asset-details, gcp-storage-bucket-policy-delete, setIssueStatus


## Hostname And IP Address Investigation And Remediation - Chronicle

**Product:** Google SecOps

This playbook receives ChronicleAsset type of indicators from its parent playbook "ChronicleAsset Investigation - Chronicle", performs enrichment and investigation for each one of them, provides an opportunity to isolate and block the hostname or IP address associated with the current indicator, and provides a list of isolated and blocked entities

**Inputs:**

- `chronicleasset_value`: The value of the ChronicleAsset indicator.
- `chronicleasset_hostname`: The hostname associated with the ChronicleAsset.
- `chronicleasset_ip`: The IP address associated with the ChronicleAsset.
- `chronicleasset_support_contact`: The support email address for the ChronicleAsset.
- `auto_block_entities`: Autoblock the detected suspicious IP Address(es). You can manually set this as "Yes" or "No" here or you can set it in a 'Chronicle Auto Block Entities' custom incident field.
- `skip_entity_isolation`: Skip the isolation of entities. You can manually set this as "Yes" or "No" here or you can set it in a 'Chronicle Skip Entity Isolation' custom incident field.

**Outputs:**

- `IsolatedEntities`
- `PotentiallyBlockedIPs`

**Dependencies:**

- Sub-playbooks: IP Enrichment - Generic v2, Isolate Endpoint - Generic, Block IP - Generic v2, Isolate Endpoint - Generic V2, Endpoint Enrichment - Generic v2.1
- Integrations: GoogleChronicleBackstory
- Scripts: DeleteContext, Set
- Commands: df-get-asset, setIndicator, ip


## Prisma Cloud Remediation - AWS CloudTrail is not Enabled on the Account

**Product:** Prisma Cloud by Palo Alto Networks

AWS Cloudtrail is a service which provides event history of your AWS account activity, including actions taken through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. To remediate Prisma Cloud Alert "CloudTrail is not enabled on the account", this playbook creates an S3 bucket to host Cloudtrail logs and enable Cloudtrail (includes all region events and global service events)

**Inputs:**

- `AutoEnableCloudTrail`: The following resources will be created:- S3 bucket cloudtrail-<account_id>- Cloudtrail cloudtrail-<account_id>Type 'Yes' to auto-enable CloudTrail.
- `CloudTrailRegion`: S3 bucket and (global) Cloudtrail will be created on this region

**Dependencies:**

- Commands: aws-s3-put-bucket-policy, aws-cloudtrail-start-logging, aws-cloudtrail-create-trail, aws-s3-create-bucket


## Prisma Cloud Remediation - AWS CloudTrail Is Not Integrated With CloudWatch Logs

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud AWS CloudTrail alerts. Prisma Cloud policies remediated

**Dependencies:**

- Integrations: AWS - CloudTrail, AWS - CloudWatchLogs, AWS - IAM
- Scripts: Sleep, isError
- Commands: aws-cloudtrail-describe-trails, aws-cloudtrail-update-trail, aws-iam-attach-policy, aws-iam-create-policy, aws-iam-create-role, aws-iam-get-role, aws-logs-create-log-group, aws-logs-describe-log-groups


## Prisma Cloud Remediation - AWS CloudTrail Trail Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud AWS CloudTrail alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Grab the Prisma Cloud policy Id.

**Dependencies:**

- Integrations: AWS - CloudTrail
- Commands: aws-cloudtrail-update-trail, aws-cloudtrail-describe-trails


## Prisma Cloud Remediation - AWS EC2 Security Group Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

Remediates the Prisma Cloud AWS EC2 alerts generated by the following policies

**Inputs:**

- `policyId`: Returns the Prisma Cloud policy ID.

**Dependencies:**

- Scripts: isError, Sleep
- Commands: aws-ec2-revoke-security-group-ingress-rule, aws-ec2-describe-security-groups


## Prisma Cloud Remediation - AWS IAM Password Policy Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

Remediates the following Prisma Cloud AWS IAM password policy alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Returns the Prisma Cloud policy ID.

**Dependencies:**

- Commands: aws-iam-update-account-password-policy


## Prisma Cloud Remediation - AWS IAM User Policy Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud AWS IAM User alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Scripts: Print
- Commands: aws-iam-list-access-keys-for-user, aws-iam-update-access-key


## Prisma Cloud Remediation - AWS Inactive Users For More Than 30 Days

**Product:** Prisma Cloud by Palo Alto Networks

Remediates Prisma Cloud Alert inactive users for more than 30 days, this playbook deactivates the user by disabling the access keys (marking them as inactive) as well as resetting the user console password. To increase the security of your AWS account, it is recommended to find and remove IAM user credentials (passwords, access keys) that have not been used within a specified period of time

**Inputs:**

- `AutoQuarantine`: Can be, "yes" - access keys will be disabled and password reset, or "no" - an analyst will be prompted for action.

**Dependencies:**

- Integrations: Builtin
- Scripts: Print
- Commands: aws-iam-update-login-profile, closeInvestigation, aws-iam-list-access-keys-for-user, aws-iam-update-access-key


## Prisma Cloud Remediation - AWS Security Groups Allows Internet Traffic To TCP Port

**Product:** Prisma Cloud by Palo Alto Networks

Extracts the TCP public Security Groups rule and provides manual/automatic options to have the rules revoked

**Inputs:**

- `AutoRevokeRule`: Can be, "yes" - public security group rules will be automatically revoked, or "no" - analyst will be prompted whether or not to allow automatic removal of the rules.

**Dependencies:**

- Integrations: Builtin, AWS - EC2
- Scripts: AwsEC2GetPublicSGRules
- Commands: aws-ec2-revoke-security-group-ingress-rule, aws-ec2-describe-security-groups, closeInvestigation


## Prisma Cloud Remediation - Azure AKS Cluster Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure AKS cluster alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Outputs:**

- `incident.labels.resource.name`

**Dependencies:**

- Integrations: Azure Kubernetes Services
- Scripts: IsIntegrationAvailable
- Commands: azure-ks-cluster-addon-update


## Prisma Cloud Remediation - Azure Network Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud Azure Network alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateAzureNetwork`: Execute Azure Network remediation automatically?
- `policyId`: Grab the Prisma Cloud policy ID.
- `portNumber`: Port number.

**Outputs:**

- `incident.resourcename`

**Dependencies:**

- Commands: closeInvestigation, prisma-cloud-alert-dismiss


## Prisma Cloud Remediation - Azure Network Security Group Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure Network security group alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.
- `portNumber`: Port number.

**Outputs:**

- `incident.resourcename`

**Dependencies:**

- Integrations: Azure Network Security Groups
- Scripts: IsIntegrationAvailable, Set
- Commands: azure-nsg-security-rule-delete


## Prisma Cloud Remediation - Azure SQL Database Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure SQL database alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Azure SQL Management
- Scripts: IsIntegrationAvailable
- Commands: azure-sql-db-threat-policy-create-update, azure-sql-db-audit-policy-create-update


## Prisma Cloud Remediation - Azure SQL Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud Azure SQL alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateAzureSQL`: Execute Azure SQL remediation automatically?
- `policyId`: Grab the Prisma Cloud policy ID.

**Dependencies:**

- Commands: prisma-cloud-alert-dismiss, closeInvestigation


## Prisma Cloud Remediation - Azure Storage Blob Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud Azure Storage blob alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Azure Storage
- Scripts: IsIntegrationAvailable
- Commands: azure-storage-account-create-update


## Prisma Cloud Remediation - GCP Compute Engine Instance Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP Compute Engine VM Instance alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Google Cloud Compute
- Commands: gcp-compute-get-instance, gcp-compute-set-instance-metadata


## Prisma Cloud Remediation - GCP Compute Engine Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud GCP Compute Engine alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateComputeEngine`: Execute GCP Compute Engine remediation automatically?
- `policyId`: Grab the Prima Cloud policy ID.

**Dependencies:**

- Commands: closeInvestigation, prisma-cloud-alert-dismiss


## Prisma Cloud Remediation - GCP Kubernetes Engine Cluster Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP Kubernetes Engine Cluster alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: GoogleKubernetesEngine
- Commands: gcloud-clusters-set-muster-auth, gcloud-clusters-describe, gcloud-clusters-set-binary-auth, gcloud-clusters-set-intra-node-visibility, gcloud-clusters-set-legacy-auth, gcloud-clusters-set-master-authorized-network, gcloud-clusters-set-k8s-stackdriver, gcloud-clusters-set-addons


## Prisma Cloud Remediation - GCP Kubernetes Engine Misconfiguration v2

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates Prisma Cloud GCP Kubernetes Engine alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateKubernetesEngine`: Execute GCP Kubernetes Engine remediation automatically?
- `policyId`: Grab the Prima Cloud policy ID.

**Dependencies:**

- Commands: prisma-cloud-alert-dismiss, closeInvestigation


## Prisma Cloud Remediation - GCP VPC Network Firewall Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP VPC Network Firewall alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Google Cloud Compute
- Commands: gcp-compute-get-firewall, gcp-compute-patch-firewall


## Prisma Cloud Remediation - GCP VPC Network Project Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

This playbook remediates the following Prisma Cloud GCP VPC Network Project alerts. Prisma Cloud policies remediated

**Inputs:**

- `policyId`: Prisma Cloud policy Id.

**Dependencies:**

- Integrations: Google Cloud Compute
- Scripts: isError
- Commands: gcp-compute-get-network, gcp-compute-delete-network


## Remediate Message - Agari Phishing Defense

**Product:** Agari Phishing Defense

Remediates a given message id. Supported   versions: 5.0.0 and later

**Inputs:**

- `id`: Id of message to remediate.
- `auto_remediation`: Flag for whether to automatically remediate or not.
- `remediate_action`: Action for remediation.

**Dependencies:**

- Commands: apd-remediate-message


## Rubrik IR Violation Remediation - Rubrik Security Cloud

**Product:** Rubrik Security Cloud

This playbook remediates Identity Resilience (IR) violations by retrieving the latest violation details and updating the violation status

**Inputs:**

- `violation_id`: The ID of the IR violation.Note: Users can get the violation ID by executing the "rubrik-identity-resilience-violation-list" command.
- `policy_type`: The policy type of the violation.Note: Users can get the policy type by executing the "rubrik-identity-resilience-violation-list" command.Possible values are: IDENTITY, IDP,IDENTIT

**Dependencies:**

- Scripts: DeleteContext, RubrikPullIRViolationInformation, Set
- Commands: rubrik-identity-resilience-violation-status-update


## SaaS Security - Remediate an Asset

**Product:** SaaS Security by Palo Alto Networks

Take a remediation action over an asset: Use this playbook as a sub-playbook to take a remediation action on an asset. Available remediation actions are 1) Remove public sharing, 2) Quarantine, and 3) Restore. This playbook implements polling by continuously running the saas-security-remediation-status-get command to get the remediation status for a given asset ID, until the operation completes. The remote action should have the following structure

**Inputs:**

- `asset_id`: The ID of the asset to remediate
- `remediation_type`: The remediation action to take.Possible values: Remove public sharing, Quarantine, Restore.
- `remove_inherited_sharing`: Used when remediation type is “remove_public_sharing”, when set to true, all the parent folder sharing url will be removed.

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: SaaS Security
- Commands: saas-security-remediation-status-get, saas-security-asset-remediate

## Prisma Cloud Remediation - Azure Network Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

**Kind:** playbook

This playbook remediates Prisma Cloud Azure Network alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateAzureNetwork`: Execute Azure Network remediation automatically?
- `policyId`: Grab the Prisma Cloud policy Id.
- `portNumber`: Port number.

**Dependencies:**

- Sub-playbooks: Prisma Cloud Remediation - Azure Network Security Group Misconfiguration
- Integrations: PrismaCloud v2
- Scripts: IsIntegrationAvailable
- Commands: redlock-dismiss-alerts, closeInvestigation

## Prisma Cloud Remediation - Azure SQL Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

**Kind:** playbook

This playbook remediates Prisma Cloud Azure SQL alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateAzureSQL`: Execute Azure SQL remediation automatically?
- `policyId`: Grab the Prisma Cloud policy ID.

**Dependencies:**

- Commands: redlock-dismiss-alerts, closeInvestigation

## Prisma Cloud Remediation - GCP Kubernetes Engine Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

**Kind:** playbook

This playbook remediates Prisma Cloud GCP Kubernetes Engine alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateKubernetesEngine`: Execute GCP Kubernetes Engine remediation automatically?
- `policyId`: Grab the Prima Cloud policy Id.

**Dependencies:**

- Sub-playbooks: Prisma Cloud Remediation - GCP Kubernetes Engine Cluster Misconfiguration
- Integrations: PrismaCloud v2
- Commands: closeInvestigation, redlock-dismiss-alerts

## Prisma Cloud Remediation - Azure Network Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

**Kind:** playbook

This playbook remediates Prisma Cloud Azure Network alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateAzureNetwork`: Execute Azure Network remediation automatically?
- `policyId`: Grab the Prisma Cloud policy Id.
- `portNumber`: Port number.

**Dependencies:**

- Sub-playbooks: Prisma Cloud Remediation - Azure Network Security Group Misconfiguration
- Integrations: PrismaCloud v2
- Scripts: IsIntegrationAvailable
- Commands: redlock-dismiss-alerts, closeInvestigation

## Prisma Cloud Remediation - Azure SQL Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

**Kind:** playbook

This playbook remediates Prisma Cloud Azure SQL alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateAzureSQL`: Execute Azure SQL remediation automatically?
- `policyId`: Grab the Prisma Cloud policy ID.

**Dependencies:**

- Commands: redlock-dismiss-alerts, closeInvestigation

## Prisma Cloud Remediation - GCP Kubernetes Engine Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

**Kind:** playbook

This playbook remediates Prisma Cloud GCP Kubernetes Engine alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateKubernetesEngine`: Execute GCP Kubernetes Engine remediation automatically?
- `policyId`: Grab the Prima Cloud policy Id.

**Dependencies:**

- Sub-playbooks: Prisma Cloud Remediation - GCP Kubernetes Engine Cluster Misconfiguration
- Integrations: PrismaCloud v2
- Commands: closeInvestigation, redlock-dismiss-alerts

## Prisma Cloud Remediation - Azure Network Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

**Kind:** playbook

This playbook remediates Prisma Cloud Azure Network alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateAzureNetwork`: Execute Azure Network remediation automatically?
- `policyId`: Grab the Prisma Cloud policy Id.
- `portNumber`: Port number.

**Dependencies:**

- Sub-playbooks: Prisma Cloud Remediation - Azure Network Security Group Misconfiguration
- Integrations: PrismaCloud v2
- Scripts: IsIntegrationAvailable
- Commands: redlock-dismiss-alerts, closeInvestigation

## Prisma Cloud Remediation - Azure SQL Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

**Kind:** playbook

This playbook remediates Prisma Cloud Azure SQL alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateAzureSQL`: Execute Azure SQL remediation automatically?
- `policyId`: Grab the Prisma Cloud policy ID.

**Dependencies:**

- Commands: redlock-dismiss-alerts, closeInvestigation

## Prisma Cloud Remediation - GCP Kubernetes Engine Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

**Kind:** playbook

This playbook remediates Prisma Cloud GCP Kubernetes Engine alerts. It calls sub-playbooks that perform the actual remediation steps. Remediation

**Inputs:**

- `AutoRemediateKubernetesEngine`: Execute GCP Kubernetes Engine remediation automatically?
- `policyId`: Grab the Prima Cloud policy Id.

**Dependencies:**

- Sub-playbooks: Prisma Cloud Remediation - GCP Kubernetes Engine Cluster Misconfiguration
- Integrations: PrismaCloud v2
- Commands: closeInvestigation, redlock-dismiss-alerts

