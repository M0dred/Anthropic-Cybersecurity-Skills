# Integration and Automation Catalog - Cloud Security

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## Amazon Web Services

**Type:** integration  
**Product:** AWS  

Support for AWS cloud This integration was integrated and tested with version 1.0.0 of AWS

**Commands:**

- `aws-s3-public-access-block-update`: 
- `aws-s3-bucket-delete`: 
- `aws-s3-bucket-objects-list`: 
- `aws-s3-bucket-objects-list-v2`: 
- `aws-s3-bucket-acl-put`: 
- `aws-s3-bucket-logging-put`: 
- `aws-s3-bucket-versioning-put`: 
- `aws-s3-bucket-policy-put`: 
- `aws-s3-bucket-website-delete`: 
- `aws-s3-bucket-ownership-controls-put`: 
- `aws-s3-bucket-website-get`: 
- `aws-s3-bucket-acl-get`: 
- `aws-iam-account-password-policy-get`: 
- `aws-iam-account-password-policy-update`: 
- `aws-iam-role-policy-put`: 


## Analyze URL - ReversingLabs TitaniumCloud

**Type:** playbook  
**Product:** ReversingLabs TitaniumCloud  

Get threat intelligence data for the submitted URL. Required TitaniumCloud API rights: TCA-0403 TCA-0402

**Inputs:**

- `URL`: URL to analyze


## Ansible Alibaba Cloud

**Type:** integration  
**Product:** Ansible Alibaba Cloud  

This integration enables the management of Alibaba Cloud Elastic Compute Service using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. To use this integration, configure an instance of this integration. This will associate a credential to be used to manage a Alibaba tenancy. Create separate instances for each region being managed

**Commands:**

- `ali-instance`: 


## Ansible Azure

**Type:** integration  
**Product:** Ansible Azure  

This integration enables the management of Azure Services using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. To use this integration, configure an instance of this integration. This will associate a credential to be used to manage a Azure Subscription. To use this integration you must generate a Service Principal for your Azure subscription. Follow Microsoft's guide on how to create a Azure AD application and associated service principal. After stepping through the guide you will have

**Commands:**

- `azure-rm-autoscale`: 


## Ansible HCloud

**Type:** integration  
**Product:** Ansible Hetzner Cloud  

This integration enables the management of Hetzner Cloud environments using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. To use this integration you must generate an API token for your HCloud project. NOTE: If using 6.0.2 or lower version, put your API Token in the Password field, leave the Username field empty

**Commands:**

- `hcloud-datacenter-info`: 
- `hcloud-floating-ip-info`: 
- `hcloud-image-info`: 


## Atlassian Cloud MCP

**Type:** integration  
**Product:** Atlassian Cloud MCP  

Use this integration to connect securely with an Atlassian Cloud Model Context Protocol (MCP) server and access its tools in real time

**Commands:**

- `atlassian-cloud-mcp-auth-test`: 
- `atlassian-cloud-mcp-generate-login-url`: 


## Atlassian Confluence Cloud

**Type:** integration  
**Product:** Atlassian Confluence Cloud  

Atlassian Confluence Cloud allows users to interact with confluence entities like content, space, users and groups. Users can also manage the space permissions. This integration was integrated and tested with version 1000.0.0-847bdcbfcd00 of Atlassian Confluence Cloud

**Commands:**

- `confluence-cloud-space-create`: 
- `confluence-cloud-content-create`: 
- `confluence-cloud-comment-create`: 
- `confluence-cloud-space-list`: 
- `confluence-cloud-content-list`: 
- `confluence-cloud-content-delete`: 
- `confluence-cloud-content-update`: 
- `confluence-cloud-content-search`: 
- `confluence-cloud-user-list`: 
- `confluence-cloud-group-list`: 
- `confluence-cloud-get-events`: 
- `confluence-cloud-content-get`: 
- `confluence-cloud-oauth-start`: 
- `confluence-cloud-oauth-complete`: 
- `confluence-cloud-oauth-test`: 


## AWS - AccessAnalyzer

**Type:** integration  
**Product:** AWS - AccessAnalyzer  

Amazon Web Services IAM Access Analyzer For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-access-analyzer-list-analyzers`: 
- `aws-access-analyzer-list-analyzed-resource`: 
- `aws-access-analyzer-list-findings`: 
- `aws-access-analyzer-get-analyzed-resource`: 
- `aws-access-analyzer-get-finding`: 
- `aws-access-analyzer-start-resource-scan`: 
- `aws-access-analyzer-update-findings`: 


## AWS - ACM

**Type:** integration  
**Product:** AWS - ACM  

Amazon Web Services Certificate Manager Service (ACM) For more information regarding the AWS ACM service, please visit the official documentation found here. For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-acm-describe-certificate`: 
- `aws-acm-list-certificates`: 
- `aws-acm-add-tags-to-certificate`: 
- `aws-acm-remove-tags-from-certificate`: 
- `aws-acm-list-tags-for-certificate`: 
- `aws-acm-get-certificate`: 


## AWS - Athena

**Type:** integration  
**Product:** AWS - Athena  

Amazon Web Services Athena

**Commands:**

- `aws-athena-execute-query`: 
- `aws-athena-start-query`: 
- `aws-athena-stop-query`: 
- `aws-athena-get-query-execution`: 
- `aws-athena-get-query-results`: 


## AWS - CloudTrail

**Type:** integration  
**Product:** AWS - CloudTrail  

Amazon Web Services CloudTrail. This integration was integrated and tested with version 1.0.11 of AWS - CloudTrail

**Commands:**

- `aws-cloudtrail-create-trail`: 
- `aws-cloudtrail-delete-trail`: 
- `aws-cloudtrail-describe-trails`: 
- `aws-cloudtrail-update-trail`: 
- `aws-cloudtrail-start-logging`: 
- `aws-cloudtrail-stop-logging`: 
- `aws-cloudtrail-lookup-events`: 
- `aws-cloudtrail-get-trail-status`: 


## AWS - EC2

**Type:** integration  
**Product:** AWS - EC2  

Amazon Web Services Elastic Compute Cloud (EC2)

**Commands:**

- `aws-ec2-describe-instances`: 
- `aws-ec2-describe-iam-instance-profile-associations`: 
- `aws-ec2-describe-images`: 
- `aws-ec2-describe-regions`: 
- `aws-ec2-describe-addresses`: 
- `aws-ec2-describe-snapshots`: 
- `aws-ec2-describe-launch-templates`: 
- `aws-ec2-describe-key-pairs`: 
- `aws-ec2-describe-volumes`: 
- `aws-ec2-describe-volumes`: 
- `aws-ec2-describe-vpcs`: 
- `aws-ec2-describe-subnets`: 
- `aws-ec2-describe-security-groups`: 
- `aws-ec2-allocate-address`: 
- `aws-ec2-associate-address`: 


## AWS - GuardDuty

**Type:** integration  
**Product:** AWS - GuardDuty  

Amazon Web Services Guard Duty Service (gd) Use this integration to detect and manage threats to your AWS system. We recommend that you use roles that have the following built-in AWS policies: For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-gd-create-detector`: 
- `aws-gd-delete-detector`: 
- `aws-gd-get-detector`: 
- `aws-gd-update-detector`: 
- `aws-gd-create-ip-set`: 
- `aws-gd-delete-ip-set`: 
- `aws-gd-list-detectors`: 
- `aws-gd-update-ip-set`: 
- `aws-gd-get-ip-set`: 
- `aws-gd-list-ip-sets`: 
- `aws-gd-create-threatintel-set`: 
- `aws-gd-delete-threatintel-set`: 
- `aws-gd-get-threatintel-set`: 
- `aws-gd-list-threatintel-sets`: 
- `aws-gd-update-threatintel-set`: 


## AWS - IAM (user lifecycle management)

**Type:** integration  
**Product:** AWS-ILM  

Integrate with AWS-ILM Identity Access Management service to execute CRUD (create, read, update, and delete) and group (create, get, update, and delete) operations for employee lifecycle processes. For more information, refer to the Identity Lifecycle Management article

**Commands:**

- `iam-create-user`: 
- `iam-update-user`: 
- `iam-get-user`: 
- `iam-disable-user`: 
- `iam-get-group`: 
- `iam-create-group`: 
- `iam-update-group`: 
- `iam-delete-group`: 


## AWS - IAM Identity Center

**Type:** integration  
**Product:** AWS - IAM Identity Center  

Amazon Web Services Identity and Access Management Identity Center(IAM) For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-iam-identitycenter-create-user`: 
- `aws-iam-identitycenter-get-user`: 
- `aws-iam-identitycenter-list-users`: 
- `aws-iam-identitycenter-list-groups`: 
- `aws-iam-identitycenter-list-groups-for-user`: 
- `aws-iam-identitycenter-add-user-to-group`: 
- `aws-iam-identitycenter-get-group`: 
- `aws-iam-identitycenter-get-user-by-email`: 
- `aws-iam-identitycenter-list-memberships`: 
- `aws-iam-identitycenter-delete-user`: 
- `aws-iam-identitycenter-delete-group`: 
- `aws-iam-identitycenter-create-group`: 
- `aws-iam-identitycenter-update-group`: 
- `aws-iam-identitycenter-update-user`: 
- `aws-iam-identitycenter-delete-group-membership`: 


## AWS - Identity and Access Management

**Type:** integration  
**Product:** AWS - IAM  

Amazon Web Services Identity and Access Management (IAM) For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-iam-create-user`: 
- `aws-iam-get-user`: 
- `aws-iam-list-users`: 
- `aws-iam-update-user`: 
- `aws-iam-delete-user`: 
- `aws-iam-update-login-profile`: 
- `aws-iam-create-group`: 
- `aws-iam-list-groups`: 
- `aws-iam-list-groups-for-user`: 
- `aws-iam-add-user-to-group`: 
- `aws-iam-create-access-key`: 
- `aws-iam-update-access-key`: 
- `aws-iam-list-access-keys-for-user`: 
- `aws-iam-list-policies`: 
- `aws-iam-list-roles`: 


## AWS - Lambda

**Type:** integration  
**Product:** AWS - Lambda  

Amazon Web Services Serverless Compute service (lambda) This integration was integrated and tested with version 2015-03-31 of AWS - Lambda. For detailed instructions about setting up authentication, see: AWS Integrations - Authentication. Required AWS IAM Permissions and Roles for Lambda are documented here

**Commands:**

- `aws-lambda-get-function`: 
- `aws-lambda-list-functions`: 
- `aws-lambda-list-aliases`: 
- `aws-lambda-invoke`: 
- `aws-lambda-get-account-settings`: 
- `aws-lambda-get-policy`: 
- `aws-lambda-list-versions-by-function`: 
- `aws-lambda-get-function-url-config`: 
- `aws-lambda-get-function-configuration`: 
- `aws-lambda-delete-function-url-config`: 
- `aws-lambda-delete-function`: 
- `aws-lambda-create-function`: 
- `aws-lambda-publish-layer-version`: 
- `aws-lambda-list-layer-version`: 
- `aws-lambda-delete-layer-version`: 


## AWS - Organizations

**Type:** integration  
**Product:** AWS Organizations  

Manage Amazon Web Services accounts and their resources. For AWS Organizations quotas, guidelines and restrictions, see the AWS Organizations Quotas page

**Commands:**

- `aws-org-root-list`: 
- `aws-org-children-list`: 
- `aws-org-parent-list`: 
- `aws-org-organization-unit-get`: 
- `aws-org-account-list`: 
- `aws-org-organization-get`: 
- `aws-org-organization-unit-create`: 
- `aws-org-organization-unit-rename`: 
- `aws-org-organization-unit-delete`: 
- `aws-org-policy-list`: 
- `aws-org-policy-get`: 
- `aws-org-policy-attach`: 
- `aws-org-policy-target-list`: 
- `aws-org-target-policy-list`: 
- `aws-org-policy-delete`: 


## AWS - Route53

**Type:** integration  
**Product:** AWS - Route53  

Amazon Web Services Managed Cloud DNS Service

**Commands:**

- `aws-route53-create-record`: 
- `aws-route53-delete-record`: 
- `aws-route53-list-hosted-zones`: 
- `aws-route53-list-resource-record-sets`: 
- `aws-route53-waiter-resource-record-sets-changed`: 
- `aws-route53-test-dns-answer`: 
- `aws-route53-upsert-record`: 


## AWS - S3

**Type:** integration  
**Product:** AWS - S3  

Amazon Web Services Simple Storage Service (S3). This integration was integrated and tested with API Version 2012-11-05. For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-s3-create-bucket`: 
- `aws-s3-delete-bucket`: 
- `aws-s3-list-buckets`: 
- `aws-s3-get-bucket-policy`: 
- `aws-s3-delete-bucket-policy`: 
- `aws-s3-download-file`: 
- `aws-s3-list-bucket-objects`: 
- `aws-s3-put-bucket-policy`: 
- `aws-s3-upload-file`: 
- `aws-s3-get-public-access-block`: 
- `aws-s3-put-public-access-block`: 
- `aws-s3-get-bucket-encryption`: 


## AWS - Security Hub

**Type:** integration  
**Product:** AWS - Security Hub  
**Commands:**

- `aws-securityhub-disable-security-hub`: 
- `aws-securityhub-batch-update-findings`: 


## AWS - Security Hub v2

**Type:** integration  
**Product:** AWS - Security Hub  

Unified security and compliance findings management using the AWS Security Hub V2 API. This integration was integrated and tested with the AWS Security Hub V2 API

**Commands:**

- `aws-securityhub-v2-security-hub-enable`: 
- `aws-securityhub-v2-security-hub-disable`: 
- `aws-securityhub-v2-findings-get`: 
- `aws-securityhub-v2-findings-batch-update`: 
- `get-remote-data`: 
- `get-mapping-fields`: 
- `update-remote-system`: 


## AWS - SNS

**Type:** integration  
**Product:** AWS - SNS  

Amazon Web Services Simple Notification Service (SNS) For more information regarding the AWS SNS service, please visit the official documentation found here. For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-sns-create-subscription`: 
- `aws-sns-send-message`: 
- `aws-sns-delete-topic`: 


## AWS - SQS

**Type:** integration  
**Product:** AWS - SQS  

Amazon Web Services Simple Queuing Service (SQS) For more information regarding the AWS SQS service, please visit the official documentation found here. For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-sqs-get-queue-url`: 
- `aws-sqs-list-queues`: 
- `aws-sqs-send-message`: 
- `aws-sqs-create-queue`: 
- `aws-sqs-delete-queue`: 
- `aws-sqs-purge-queue`: 


## AWS - System Manager

**Type:** integration  
**Product:** AWS Systems Manager  

AWS Systems Manager is the operations hub for your AWS applications and resources and a secure end-to-end management solution for hybrid cloud environments that enables safe and secure operations at scale. This integration was integrated and tested with Boto3 version 1.28.30 (AWS SDK). For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-ssm-tag-add`: 
- `aws-ssm-tag-remove`: 
- `aws-ssm-tag-list`: 
- `aws-ssm-inventory-list`: 
- `aws-ssm-inventory-entry-list`: 
- `aws-ssm-association-list`: 
- `aws-ssm-association-get`: 
- `aws-ssm-association-version-list`: 
- `aws-ssm-document-list`: 
- `aws-ssm-document-get`: 
- `aws-ssm-automation-execution-run`: 
- `aws-ssm-automation-execution-cancel`: 
- `aws-ssm-automation-execution-list`: 
- `aws-ssm-command-list`: 
- `aws-ssm-command-run`: 


## AWS - Unclaimed S3 Bucket Validation

**Type:** playbook  
**Product:** AWS Enrichment and Remediation  

The playbook sends a HTTP get response to the hostname and validates if there is missing bucket information

**Inputs:**

- `RemoteHostname`: Remote hostname in an incident/alert.


## AWS Network Firewall

**Type:** integration  
**Product:** AWS - Network Firewall  

AWS Network Firewall is a stateful, managed, network firewall and intrusion detection and prevention service for Amazon Virtual Private Cloud (Amazon VPC). With Network Firewall, you can filter traffic at the perimeter of your VPC. This includes filtering traffic going to and coming from an internet gateway, NAT gateway, or over VPN or AWS Direct Connect. Network Firewall uses rules that are compatible with Suricata, a free, open source intrusion detection system (IDS) engine

**Commands:**

- `aws-network-firewall-associate-firewall-policy`: 
- `aws-network-firewall-associate-subnets`: 
- `aws-network-firewall-create-firewall`: 
- `aws-network-firewall-create-firewall-policy`: 
- `aws-network-firewall-create-rule-group`: 
- `aws-network-firewall-delete-firewall`: 
- `aws-network-firewall-delete-firewall-policy`: 
- `aws-network-firewall-delete-resource-policy`: 
- `aws-network-firewall-delete-rule-group`: 
- `aws-network-firewall-describe-firewall`: 
- `aws-network-firewall-describe-firewall-policy`: 
- `aws-network-firewall-describe-logging-configuration`: 
- `aws-network-firewall-describe-resource-policy`: 
- `aws-network-firewall-describe-rule-group`: 
- `aws-network-firewall-disassociate-subnets`: 


## AWS Sagemaker

**Type:** integration  
**Product:** AWS Sagemaker  

AWS Sagemaker - the platform

**Commands:**

- `predict-phishing`: 


## Aws Secrets Manager

**Type:** integration  
**Product:** AWS Secrets Manager  

AWS Secrets Manager helps you to securely encrypt, store, and retrieve credentials for your databases and other services. This integration was integrated and tested with version 1.0 of AwsSecretsManager

**Commands:**

- `aws-secrets-manager-secret-list`: 


## AWS-EKS

**Type:** integration  
**Product:** AWS - EKS  

The AWS EKS integration allows for the management and operation of Amazon Elastic Kubernetes Service (EKS) clusters. This integration was integrated and tested with version 1.29 of AWS-EKS

**Commands:**

- `aws-eks-list-clusters`: 
- `aws-eks-update-cluster-config`: 
- `aws-eks-describe-cluster`: 
- `aws-eks-create-access-entry`: 
- `aws-eks-associate-access-policy`: 
- `aws-eks-update-access-entry`: 


## AWS-WAF

**Type:** integration  
**Product:** AWS WAF  

Amazon Web Services Web Application Firewall (WAF)

**Commands:**

- `aws-waf-ip-set-create`: 
- `aws-waf-ip-set-get`: 
- `aws-waf-ip-set-update`: 
- `aws-waf-ip-set-list`: 
- `aws-waf-ip-set-delete`: 
- `aws-waf-regex-set-create`: 
- `aws-waf-regex-set-get`: 
- `aws-waf-regex-set-update`: 
- `aws-waf-regex-set-list`: 
- `aws-waf-regex-set-delete`: 
- `aws-waf-rule-group-list`: 
- `aws-waf-rule-group-get`: 
- `aws-waf-rule-group-delete`: 
- `aws-waf-rule-group-create`: 
- `aws-waf-ip-rule-create`: 


## AWSAccountHierarchy

**Type:** script  
**Product:** AWS Enrichment and Remediation  

Determine AWS account hierarchy by looking up parent objects until the organization level is reached

**Inputs:**

- `account_id`: The unique identifier (ID) of the Amazon Web Services account that you want information about.


## AwsEC2GetPublicSGRules

**Type:** script  
**Product:** AWS - EC2  

Find Security Group rules which allows ::/0 (IPv4) or 0.0.0.0/0

**Inputs:**

- `groupId`: Security Group ID (sg-xxxxxxxxx)
- `ipPermissions`: JSON string of the ipPermissions. IpPermissions should have one or more rules which are composed of IpProtocol, FromPort, ToPort, or IpRange
- `protocol`: Protocol to check. TCP/UDP/All(-1)
- `fromPort`: Lower bound port range to be checked. If fromPort and toPort are not specified, all ports will be included.
- `toPort`: Upper bound port range to be checked. If fromPort and toPort are not specified, all ports will be included.
- `region`: Security group region
- `includeIPv6`: Include IPv6 in the result. By default, IPv6 is not included


## AwsEC2SyncAccounts

**Type:** script  
**Product:** AWS - EC2  

Update an AWS - EC2 instance with a list of accounts in an AWS organization, which will allow EC2 commands to run in all of them. This script can be run on a schedule to keep an AWS - EC2 instance in sync with the created, deleted or removed accounts of the organization

**Inputs:**

- `ec2_instance_name`: The name of the AWS - EC2 instance integration to update.
- `org_instance_name`: The name of the AWS - Organizations instance to collect account from. If not provided, the primary instance will be used.
- `exclude_accounts`: A comma-separated list of accounts to exclude.
- `max_accounts`: The maximum number of accounts to retrieve. Default is 50.


## AWSIdentifySGPublicExposure

**Type:** script  
**Product:** Cloud Security Policy Management  

Automation to determine which interface on an EC2 instance has a given public IP and identify associated security groups

**Inputs:**

- `account_id`: The AWS Account ID.
- `instance_id`: EC2 Instance ID.
- `public_ip`: Public IP address whose network interface to identify.
- `region`: Region where EC2 instance resides.
- `integration_instance`: The AWS Integration Instance to use.


## AWSRecreateSG

**Type:** script  
**Product:** AWS Enrichment and Remediation  

Automation to determine which interface on an EC2 instance has an over-permissive security group, determine which security groups have over-permissive rules and replace them with a copy of the security group that has only the over-permissive portion removed. Over-permissive is defined as sensitive ports (SSH, RDP, etc.) being exposed to the internet via IPv4

**Inputs:**

- `instance_id`: EC2 Instance ID.
- `port`: TCP/UDP port to be restricted.
- `protocol`: Protocol of the port to be restricted.
- `public_ip`: Public IP address of the EC2 instance.
- `assume_role`: Name of an AWS role to assume (should be the same for all organizations).
- `region`: Region where EC2 instance is present.


## AWSRemediateSG

**Type:** script  
**Product:** Cloud Security Policy Management  

Duplicates security groups and modifies rules to remove public exposure for the specified port. The updated security groups can then be used to remediate public exposure of an AWS resource by replacing the existing list

**Inputs:**

- `account_id`: The AWS account ID.
- `resource_id`: The EC2 resource ID to remediate security groups for.
- `sg_list`: A comma-separated list of security group IDs to recreate.
- `port`: TCP/UDP port to be restricted.
- `protocol`: The protocol of the port to be restricted.
- `region`: The region where the EC2 instance resides.
- `tags`: The tags to apply to the recreated security groups. Use the format key=abc,value=123;key=fed,value=456, with tags separated by a semicolon (
- `integration_instance`: The AWS integration instance to use.


## Azure

**Type:** integration  
**Product:** Azure  

Cloud integrations are installed from the Data Sources page. To configure a cloud integration, go to Settings > Data Sources, click Add Data Source, and select Microsoft Azure. Click Connect, then click Show advanced settings, and under Additional Security Capabilities, enable Automation

**Commands:**

- `azure-nsg-security-rule-update`: 
- `azure-storage-accounts-list`: 
- `azure-storage-blob-containers-list`: 
- `azure-storage-account-update`: 
- `azure-storage-blob-service-properties-set`: 
- `azure-policy-assignment-create`: 
- `azure-postgres-config-set`: 
- `azure-webapp-config-set`: 
- `azure-webapp-auth-update`: 
- `azure-mysql-flexible-server-param-set`: 
- `azure-monitor-log-profile-update`: 
- `azure-disk-update`: 
- `azure-webapp-update`: 
- `azure-acr-update`: 
- `azure-postgres-server-update`: 


## Azure Compute v2

**Type:** integration  
**Product:** Azure Compute  

You can use this integration to create and manage Azure Virtual Machines. This integration was integrated and tested with Azure Compute API Version: 2017-12-01

**Commands:**

- `azure-vm-list-instances`: 
- `azure-vm-start-instance`: 
- `azure-vm-poweroff-instance`: 
- `azure-vm-get-instance-details`: 
- `azure-vm-create-instance`: 
- `azure-list-resource-groups`: 
- `azure-vm-delete-instance`: 
- `azure-list-subscriptions`: 
- `azure-vm-get-nic-details`: 
- `azure-vm-get-public-ip-details`: 
- `azure-vm-get-all-public-ip-details`: 
- `azure-vm-create-nic`: 
- `azure-vm-auth-reset`: 


## Azure Data Explorer

**Type:** integration  
**Product:** Azure Data Explorer  

Use the Azure Data Explorer integration to collect and analyze data inside Azure Data Explorer clusters, and to manage search queries. This integration was integrated and tested with version V1 of AzureDataExplorer. In order to connect to the Azure Data Explorer using either the platform, use one of the following methods

**Commands:**

- `azure-data-explorer-search-query-execute`: 
- `azure-data-explorer-search-query-list`: 
- `azure-data-explorer-running-search-query-list`: 
- `azure-data-explorer-running-search-query-cancel`: 
- `azure-data-explorer-auth-start`: 
- `azure-data-explorer-auth-complete`: 
- `azure-data-explorer-auth-reset`: 
- `azure-data-explorer-auth-test`: 
- `azure-data-explorer-generate-login-url`: 


## Azure Firewall

**Type:** integration  
**Product:** Azure Firewall  

Azure Firewall is a cloud-native and intelligent network firewall security service that provides breed threat protection for cloud workloads running in Azure. It's a fully stateful, firewall as a service, with built-in high availability and unrestricted cloud scalability. This integration was integrated and tested with version 2021-03-01 of Azure Firewall

**Commands:**

- `azure-firewall-auth-test`: 
- `azure-firewall-auth-start`: 
- `azure-firewall-auth-complete`: 
- `azure-firewall-auth-reset`: 
- `azure-firewall-list`: 
- `azure-firewall-get`: 
- `azure-firewall-rule-collection-list`: 
- `azure-firewall-rule-list`: 
- `azure-firewall-rule-get`: 
- `azure-firewall-policy-create`: 
- `azure-firewall-policy-update`: 
- `azure-firewall-policy-get`: 
- `azure-firewall-policy-delete`: 
- `azure-firewall-policy-list`: 
- `azure-firewall-policy-attach`: 


## Azure Key Vault

**Type:** integration  
**Product:** Azure Key Vault  

Use the Azure Key Vault integration to safeguard and manage cryptographic keys and secrets used by cloud applications and services. This integration was integrated and tested with version 2022-07-01 of AzureKeyVault

**Commands:**

- `azure-key-vault-create-update`: 
- `azure-key-vault-delete`: 
- `azure-key-vault-get`: 
- `azure-key-vault-list`: 
- `azure-key-vault-access-policy-update`: 
- `azure-key-vault-key-get`: 
- `azure-key-vault-key-list`: 
- `azure-key-vault-key-delete`: 
- `azure-key-vault-secret-get`: 
- `azure-key-vault-secret-list`: 
- `azure-key-vault-secret-delete`: 
- `azure-key-vault-certificate-get`: 
- `azure-key-vault-certificate-list`: 
- `azure-key-vault-certificate-policy-get`: 
- `azure-key-vault-subscriptions-list`: 


## Azure Kubernetes Services

**Type:** integration  
**Product:** Azure Kubernetes Services  

Deploy and manage containerized applications with a fully managed Kubernetes service. This integration was integrated and tested with API version 2023-02-01 of AKS. In order to connect to the AzureKubernetesServices using either the platform, use one of the following methods: To use a self-configured Azure application, you need to add a new Azure App Registration in the Azure Portal. In case you want to use Device code flow, you must allow public client flows (can be found under the Authentication section of the app). Follow these steps for a self-deployed configuration: Follow these steps for a self-deployed configuration: At end of the process you'll see a message that you've logged in successfully. In order to use the the platform, use the default application ID (ab217a43-e09b-4f80-ae93-482fc7a3d1a3)

**Commands:**

- `azure-ks-auth-test`: 
- `azure-ks-auth-start`: 
- `azure-ks-auth-complete`: 
- `azure-ks-auth-reset`: 
- `azure-ks-clusters-list`: 
- `azure-ks-cluster-addon-update`: 
- `azure-ks-generate-login-url`: 
- `azure-ks-resource-group-list`: 
- `azure-ks-subscriptions-list`: 


## Azure Log Analytics

**Type:** integration  
**Product:** Azure Log Analytics  

Log Analytics is a service that helps you collect and analyze data generated by resources in your cloud and on-premises environments. This integration was integrated and tested with version 2022-10-01 of Azure Log Analytics. In order to connect to the Azure Log Analytics use either the the platform. Depending on the authentication method that you use, the integration parameters might change. Note: The Azure account must have permission to manage applications in Entra ID (Azure AD). Any of the following Entra ID roles include the required permissions: In addition, the user that granted the authorization needs to be assigned the Log Analytics Reader role. For the search job commands the user needs to be assigned the Log Analytics Contributor role. For more information, refer to the following Microsoft article

**Commands:**

- `azure-log-analytics-execute-query`: 


## Azure Log Analytics - Query From Saved Search

**Type:** playbook  
**Product:** Azure Log Analytics  

Executes a query from a saved search in Azure Log Analytics

**Inputs:**

- `saved_search_id`: The ID of the saved search to run.
- `timespan`: The timespan over which to query data. This is an ISO8601 time period value. This timespan is applied in addition to timespans that are spec


## Azure Network Security Groups

**Type:** integration  
**Product:** Azure Network Security Groups  

Azure network security groups are used to filter network traffic to and from Azure resources in an Azure virtual network. This integration was integrated and tested with version 2022-09-01 of Azure Network Security Groups. In order to connect to the Azure Storage Accounts and the Blob Service use either the the platform. Use one of the following methods

**Commands:**

- `azure-nsg-security-groups-list`: 
- `azure-nsg-security-rules-list`: 
- `azure-nsg-auth-test`: 
- `azure-nsg-auth-start`: 
- `azure-nsg-auth-complete`: 
- `azure-nsg-auth-reset`: 
- `azure-nsg-security-rule-delete`: 
- `azure-nsg-security-rule-create`: 
- `azure-nsg-security-rule-update`: 
- `azure-nsg-security-rule-get`: 
- `azure-nsg-generate-login-url`: 
- `azure-nsg-subscriptions-list`: 
- `azure-nsg-resource-group-list`: 
- `azure-nsg-network-interfaces-create`: 
- `azure-nsg-virtual-networks-list`: 


## Azure Open AI Service

**Type:** integration  
**Product:** Azure Open AI Service  

Azure Open AI ServiceAI

**Commands:**

- `azure-openai-send-message`: 


## Azure Resource Graph

**Type:** integration  
**Product:** Azure Resource Graph  

Azure Resource Graph is an Azure service designed to extend Azure Resource Management by providing efficient and performant resource exploration with the ability to query at scale across a given set of resources

**Commands:**

- `azure-rg-list-operations`: 
- `azure-rg-query`: 
- `azure-rg-auth-reset`: 


## Azure Risky Users

**Type:** integration  
**Product:** Azure Risky Users  

Azure Risky Users provides access to all at-risk users and risk detections in Azure AD environment. This integration was integrated and tested with version 1.0 of Microsoft Graph Azure Risky Users. To use a self-configured Azure application, you need to add a new Azure App Registration in the Azure Portal. The application must have the following permissions: In case you want to use Device code flow, you must allow public client flows (can be found under the Authentication section of the app)

**Commands:**

- `azure-risky-users-auth-test`: 
- `azure-risky-users-auth-start`: 
- `azure-risky-users-auth-complete`: 
- `azure-risky-users-auth-reset`: 
- `azure-risky-users-list`: 
- `azure-risky-user-get`: 
- `azure-risky-users-risk-detections-list`: 
- `azure-risky-users-risk-detection-get`: 
- `azure-risky-users-confirm-safe`: 
- `azure-risky-users-confirm-compromise`: 


## Azure SQL Management

**Type:** integration  
**Product:** Azure SQL Management  

Microsoft Azure SQL Management Integration manages the Auditing and Threat Policies for Azure SQL. This integration was integrated and tested with version 2021-11-01 of Azure SQL Management In order to connect to the AzureKubernetesServices using either the platform, use one of the following methods: To use a self-configured Azure application, you need to add a new Azure App Registration in the Azure Portal. The application must have user_impersonation permission and must allow public client flows (found under the Authentication section of the app). And must allow public client flows (found under the Authentication section of the app) for Device-code based authentications

**Commands:**

- `azure-sql-auth-start`: 
- `azure-sql-auth-complete`: 
- `azure-sql-auth-reset`: 
- `azure-sql-auth-test`: 
- `azure-sql-servers-list`: 
- `azure-sql-db-list`: 
- `azure-sql-db-audit-policy-list`: 
- `azure-sql-db-threat-policy-get`: 
- `azure-sql-db-audit-policy-create-update`: 
- `azure-sql-db-threat-policy-create-update`: 
- `azure-sql-generate-login-url`: 
- `azure-sql-subscriptions-list`: 
- `azure-sql-resource-group-list`: 
- `azure-sql-firewall-rule-list`: 
- `azure-sql-firewall-rule-create-update`: 


## Azure Storage Container

**Type:** integration  
**Product:** Azure Storage Container  

Create and Manage Azure Storage Container services. This integration was integrated and tested with version "2020-10-02" of Azure Storage Container

**Commands:**

- `azure-storage-container-list`: 
- `azure-storage-container-create`: 
- `azure-storage-container-property-get`: 
- `azure-storage-container-delete`: 
- `azure-storage-container-blob-list`: 
- `azure-storage-container-blob-create`: 
- `azure-storage-container-blob-update`: 
- `azure-storage-container-blob-get`: 
- `azure-storage-container-blob-tag-get`: 
- `azure-storage-container-blob-tag-set`: 
- `azure-storage-container-blob-delete`: 
- `azure-storage-container-blob-property-get`: 
- `azure-storage-container-blob-property-set`: 
- `azure-storage-container-sas-create`: 
- `azure-storage-container-block-public-access`: 


## Azure Storage FileShare

**Type:** integration  
**Product:** Azure Storage FileShare  

Create and Manage Azure FileShare Files and Directories. This integration was integrated and tested with version "2020-10-02" of Azure Storage FileShare

**Commands:**

- `azure-storage-fileshare-create`: 
- `azure-storage-fileshare-delete`: 
- `azure-storage-fileshare-list`: 
- `azure-storage-fileshare-content-list`: 
- `azure-storage-fileshare-directory-create`: 
- `azure-storage-fileshare-directory-delete`: 
- `azure-storage-fileshare-file-create`: 
- `azure-storage-fileshare-file-get`: 
- `azure-storage-fileshare-file-delete`: 


## Azure Storage Management

**Type:** integration  
**Product:** Azure Storage Management  

This integration enables you to deploy and manage storage accounts and blob services. This integration was integrated and tested with version 2022-09-01 of Azure Storage In order to connect to the Azure Storage Accounts and the Blob Service use either the the platform. Use one of the following methods

**Commands:**

- `azure-storage-auth-test`: 
- `azure-storage-auth-start`: 
- `azure-storage-auth-complete`: 
- `azure-storage-auth-reset`: 
- `azure-storage-account-list`: 
- `azure-storage-account-create-update`: 
- `azure-storage-blob-service-properties-get`: 
- `azure-storage-blob-service-properties-set`: 
- `azure-storage-blob-containers-create`: 
- `azure-storage-blob-containers-update`: 
- `azure-storage-blob-containers-list`: 
- `azure-storage-blob-container-delete`: 
- `azure-storage-generate-login-url`: 
- `azure-storage-subscriptions-list`: 
- `azure-storage-resource-group-list`: 


## Azure Storage Queue

**Type:** integration  
**Product:** Azure Storage Queue  

Create and Manage Azure Storage Queues and Messages. This integration was integrated and tested with version "2020-10-02" of Azure Storage Queue

**Commands:**

- `azure-storage-queue-list`: 
- `azure-storage-queue-create`: 
- `azure-storage-queue-delete`: 
- `azure-storage-queue-message-create`: 
- `azure-storage-queue-message-get`: 
- `azure-storage-queue-message-peek`: 
- `azure-storage-queue-message-dequeue`: 
- `azure-storage-queue-message-update`: 
- `azure-storage-queue-message-delete`: 
- `azure-storage-queue-message-clear`: 


## Azure Storage Table

**Type:** integration  
**Product:** Azure Storage Table  

Create and Manage Azure Storage Tables and Entities. This integration was integrated and tested with version "2020-10-02" of Azure Storage Table

**Commands:**

- `azure-storage-table-create`: 
- `azure-storage-table-delete`: 
- `azure-storage-table-query`: 
- `azure-storage-table-entity-insert`: 
- `azure-storage-table-entity-update`: 
- `azure-storage-table-entity-replace`: 
- `azure-storage-table-entity-query`: 
- `azure-storage-table-entity-delete`: 


## Azure Web Application Firewall

**Type:** integration  
**Product:** Azure WAF  

The Azure WAF (Web Application Firewall) integration provides centralized protection of your web applications from common exploits and vulnerabilities. It enables you to control policies that are configured in the Azure Firewall management platform, and allows you to add, delete, or update policies, and also to get details of a specific policy or a list of policies. In order to connect to the AzureWAF using either the platform, use one of the following methods

**Commands:**

- `azure-waf-policies-get`: 
- `azure-waf-policies-list-all-in-subscription`: 
- `azure-waf-policy-update-or-create`: 
- `azure-waf-policy-delete`: 
- `azure-waf-front-door-policies-list`: 
- `azure-waf-front-door-policies-list-all-in-subscription`: 
- `azure-waf-front-door-policy-update-or-create`: 
- `azure-waf-front-door-policy-delete`: 
- `azure-waf-auth-start`: 
- `azure-waf-auth-complete`: 
- `azure-waf-auth-reset`: 
- `azure-waf-auth-test`: 
- `azure-waf-generate-login-url`: 
- `azure-waf-subscriptions-list`: 
- `azure-waf-resource-group-list`: 


## AzureDevOps

**Type:** integration  
**Product:** AzureDevOps  

Manage Git repositories in Azure DevOps Services. Integration capabilities include retrieving, creating, and updating pull requests. Run pipelines and retrieve git information

**Commands:**

- `azure-devops-auth-test`: 
- `azure-devops-generate-login-url`: 
- `azure-devops-auth-start`: 
- `azure-devops-auth-complete`: 
- `azure-devops-auth-reset`: 
- `get-mapping-fields`: 


## AzureFindAvailableNSGPriorities

**Type:** script  
**Product:** Azure Enrichment and Remediation  

This script takes in a list of numbers that represent Azure priorities for NSG rules, a target priority number, and a number available priorities to return available priorities from the provided list

**Inputs:**

- `target_rule_priority`: The NSG priority to start finding available priorities from. The target priority cannot be 100.
- `number_of_available_priorities_to_retrieve`: The number of priorities that are available to be returned. (limit: 5)
- `list_of_priorities_from_rules`: The list of priorities from rules in an Azure Network Security Group. (limit: 995)


## AzureIdentifyNSGExposureRule

**Type:** script  
**Product:** Cloud Security Policy Management  

This script identifies the first inbound Allow rule in the specified NSG that matches the criteria for network exposure. It returns details about the identified rule as well as a list of available priority numbers to insert new security rules with a higher priority

**Inputs:**

- `subscription_id`: The Azure Subscription ID where the NSG resides.
- `resource_group_name`: The Azure Resource Group Name where the NSG resides.
- `network_security_group_name`: The Azure Network Security Group (NSG) Name to analyze for exposure rules.
- `private_ip_addresses`: The destination private IP address(es) of the Virtual Machine interface.
- `port`: TCP/UDP port to be restricted.
- `protocol`: Protocol of the port to be restricted.
- `priority_count`: The number of available priority values below the matching rule to return.
- `integration_instance`: The Azure Integration Instance to use.


## Carbon Black EDR Search Process

**Type:** playbook  
**Product:** Carbon Black Cloud Enterprise EDR  

Use this playbook to search processes in Carbon Black Enterprise EDR. This playbook implements polling by continuously running the cb-eedr-process-search-results command until the operation completes

**Inputs:**

- `query`: Query with Carbon Black API syntax
- `process_name`: Tokenized file path of the process’ main module.
- `process_hash`: MD5 and SHA-256 hashes of process’ main module in a multi-valued field.
- `event_id`: CBD Event id (valid only for events coming through Analytics)
- `limit`: number of results to fetch
- `interval`: determine how long to wait between fetching data for polling
- `timeout`: determine timeout for polling


## Carbon Black Enterprise EDR

**Type:** integration  
**Product:** Carbon Black Cloud Enterprise EDR  
**Commands:**

- `cb-eedr-alert-workflow-update`: 


## Check Point Dome9 (CloudGuard)

**Type:** integration  
**Product:** Check Point Dome9 (CloudGuard)  

Dome9 integration allows to easily manage the security and compliance of the public cloud. This integration was integrated and tested with version 2 of checkpointdome9

**Commands:**

- `dome9-access-lease-list`: 
- `dome9-access-lease-delete`: 
- `dome9-access-lease-invitation-list`: 
- `dome9-access-lease-invitation-delete`: 
- `dome9-findings-search`: 
- `dome9-ip-list-create`: 
- `dome9-ip-list-update`: 
- `dome9-ip-list-get`: 
- `dome9-ip-list-delete`: 
- `dome9-ip-list-metadata-list`: 
- `dome9-ip-list-metadata-create`: 
- `dome9-ip-list-metadata-update`: 
- `dome9-ip-list-metadata-delete`: 
- `dome9-compliance-remediation-get`: 
- `dome9-compliance-remediation-create`: 


## Cisco Umbrella Cloud Security v2

**Type:** integration  
**Product:** Cisco Umbrella cloud security  

Cisco Umbrella is a cloud security platform providing the first line of defense against internet threats. It uses DNS-layer security to block malicious requests before a connection is established, offering protection against malware, ransomware, phishing, and more. It offers real-time reporting, integrates with other Cisco solutions for layered security, and uses machine learning to uncover and predict threats. This integration was tested with version 2 of Cisco Umbrella Cloud Security

**Commands:**

- `umbrella-destinations-list`: 
- `umbrella-destination-add`: 
- `umbrella-destination-delete`: 
- `umbrella-destination-lists-list`: 
- `umbrella-destination-list-create`: 
- `umbrella-destination-list-update`: 
- `umbrella-destination-list-delete`: 


## Cloud Credentials Rotation - AWS

**Type:** playbook  
**Product:** AWS Enrichment and Remediation  
**Inputs:**

- `IAMRemediationType`: The response playbook provides the following remediation actions for IAM users:Reset - By entering "Reset" in the input, the playbook will e
- `shouldCloneSA`: Whether to clone the compromised SA before putting a deny policy to it.True/False
- `identityType`: The type of identity involved. Usually mapped to the incident field named 'cloudidentitytype'.e.g.USER,SERVICE_ACCOUNT,APPLICATION
- `newRoleName`: The new role name to assign in the clone service account flow.
- `newInstanceProfileName`: The new instance profile name to assign in the clone service account flow.
- `accessKeyID`: The access key ID.
- `username`: The user name.
- `instanceID`: The instance ID.


## Cloud Credentials Rotation - Azure

**Type:** playbook  
**Product:** Azure Enrichment and Remediation  
**Inputs:**

- `IAMRemediationType`: The response playbook provides the following remediation actions using MSGraph Users:Reset: By entering "Reset" in the input, the playbook w
- `appID`: This is the unique application (client) ID of the application.
- `objectID`: This is the unique ID of the service principal object associated with the application.
- `userID`: The user ID or user principal name.
- `identityType`: The type of identity involved. Usually mapped to incident field named 'cloudidentitytype'.e.g.IAM,APPLICATION


## Cloud Credentials Rotation - GCP

**Type:** playbook  
**Product:** GCP Enrichment and Remediation  
**Inputs:**

- `GSuiteRemediationType`: The response playbook provides the following remediation actions using GSuite Admin:Reset: By entering "Reset" in the input, the playbook wi
- `userID`: Identifies the user in the API request. The value can be the user's primary email address, alias email address, or unique user ID.
- `clientID`: The client ID.
- `zone`: The name of the zone.
- `serviceAccountEmail`: The service account email.
- `identityType`: The type of identity involved. Usually mapped to the incident field named 'cloudidentitytype'.e.g.USER,SERVICE_ACCOUNT,APPLICATION
- `cloudProject`: The relevant project that the alert relates to.


## Cloud IDS-IP Blacklist-GCP Firewall_Append

**Type:** playbook  
**Product:** Cloud-IDS  

Use this playbook to update the ip list to patch the GCP firewall


## Cloud IDS-IP Blacklist-GCP Firewall_Combine

**Type:** playbook  
**Product:** Cloud-IDS  

Use this playbook to extract an attacker's IP address from Cloud IDS through Google Pub/Sub, then update the ip list to patch GCP firewall. This playbook calls both Extract and Append


## Cloud IDS-IP Blacklist-GCP Firewall_Extract

**Type:** playbook  
**Product:** Cloud-IDS  

Use this playbook to extract an attacker's IP address from Cloud IDS through Google Pub/Sub, then update the ip list to patch GCP firewall


## CloudConvert

**Type:** integration  
**Product:** Cloud Convert  

Use the CloudConvert integration to convert your files to the required format. This integration was integrated and tested with version v2 of CloudConvert

**Commands:**

- `cloudconvert-upload`: 
- `cloudconvert-convert`: 
- `cloudconvert-check-status`: 
- `cloudconvert-download`: 


## CloudConvert - Convert File

**Type:** playbook  
**Product:** Cloud Convert  

Use this playbook to convert a file to the required format using CloudConvert

**Inputs:**

- `url`: The URL of the uploaded file.
- `entry_id`: The entry ID of the uploaded file.
- `output_format`: The required output format.
- `download_via`: The method for downloading the converted file - URL or war_room_entry.


## Cloudflare MCP

**Type:** integration  
**Product:** Cloudflare MCP  

Use this integration to connect securely with a Cloudflare Model Context Protocol (MCP) server and access its tools in real time

**Commands:**

- `cloudflare-mcp-generate-login-url`: 
- `cloudflare-mcp-auth-test`: 


## Cloudflare WAF

**Type:** integration  
**Product:** Cloudflare WAF  

Cloudflare WAF integration allows customers to manage firewall rules, filters, and IP-lists. It also allows to retrieve zones list for each account. This integration was integrated and tested with version 4 of CloudflareWAF

**Commands:**

- `cloudflare-waf-firewall-rule-create`: 
- `cloudflare-waf-firewall-rule-update`: 
- `cloudflare-waf-firewall-rule-delete`: 
- `cloudflare-waf-firewall-rule-list`: 
- `cloudflare-waf-filter-create`: 
- `cloudflare-waf-filter-update`: 
- `cloudflare-waf-filter-delete`: 
- `cloudflare-waf-filter-list`: 
- `cloudflare-waf-zone-list`: 
- `cloudflare-waf-ip-list-create`: 
- `cloudflare-waf-ip-list-delete`: 
- `cloudflare-waf-ip-lists-list`: 
- `cloudflare-waf-ip-list-item-create`: 
- `cloudflare-waf-ip-list-item-update`: 
- `cloudflare-waf-ip-list-item-delete`: 


## Cloudflare Zero Trust

**Type:** integration  
**Product:** Cloudflare Zero Trust  

Cloudflare provides network and security products for consumers and businesses, utilizing reverse proxies for web traffic, edge computing, and a content distribution network to provide content across its network of servers. This integration was integrated and tested with version 1 of Cloudflare Zero Trust

**Commands:**

- `cloudflare-zero-trust-get-events`: 


## CloudShare (Beta)

**Type:** integration  
**Product:** CloudShare  

This integration is a BETA that covers the API commands from CloudShare

**Commands:**

- `cloudshare-get-envs`: 
- `cloudshare-get-projects`: 
- `cloudshare-get-project`: 
- `cloudshare-get-project-policies`: 
- `cloudshare-get-project-blueprints`: 
- `cloudshare-get-project-blueprint`: 
- `cloudshare-get-classes`: 
- `cloudshare-get-class`: 
- `cloudshare-delete-class`: 
- `cloudshare-delete-class-environments`: 
- `cloudshare-get-classes-countries`: 
- `cloudshare-get-classes-customfields`: 
- `cloudshare-get-classes-detailed`: 
- `cloudshare-get-classes-instructors`: 
- `cloudshare-create-class`: 


## Commvault Cloud

**Type:** integration  
**Product:** Commvault Cloud  

Commvault Cloud provides pre-built integrations, automation workflows, and playbooks to streamline operations, enhance threat intelligence integration, and gain actionable insights through advanced reporting and analytics. This integration was integrated and tested with version 6.9.0 of CommvaultSecurityIQ

**Commands:**

- `commvault-security-set-disable-data-aging`: 
- `commvault-security-get-generate-token`: 
- `commvault-security-get-access-token-from-keyvault`: 
- `commvault-security-set-disable-saml-provider`: 
- `commvault-security-get-copy-files-list-to-war-room`: 
- `commvault-security-set-disable-user`: 
- `commvault-security-set-cleanroom-add-vm-to-recovery-group`: 


## Cortex XDR - Cloud Enrichment

**Type:** playbook  
**Product:** Cloud Incident Response  

This playbook is responsible for collecting data from Cortex XDR detector and enriching data for further usage and building the layout. The playbook collects or enriches the following data

**Inputs:**

- `ResolveIP`: Determines whether to convert the IP address to a hostname using a DNS query (True/ False).
- `InternalRange`: A list of internal IP ranges to check IP addresses against. \nFor IP Enrichment - Generic v2 playbook.


## Datadog

**Type:** integration  
**Product:** Datadog Cloud SIEM  
**Commands:**

- `datadog-event-create`: 
- `datadog-event-list`: 
- `datadog-tag-list`: 
- `datadog-host-tag-create`: 
- `datadog-host-tag-get`: 
- `datadog-host-tag-update`: 
- `datadog-host-tag-delete`: 
- `datadog-active-metric-list`: 
- `datadog-metric-search`: 
- `datadog-metric-metadata-get`: 
- `datadog-metric-metadata-update`: 
- `datadog-incident-create`: 
- `datadog-incident-delete`: 
- `datadog-incident-update`: 
- `datadog-incident-list`: 


## Datadog Cloud SIEM

**Type:** integration  
**Product:** Datadog Cloud SIEM  

Datadog Cloud SIEM integration for the platform. This integration allows security teams to: This integration was integrated and tested with version 2.12.0 of datadog-api-client

**Commands:**

- `datadog-get-signal`: 


## DatadogSyncIncidentFields

**Type:** script  
**Product:** Datadog Cloud SIEM  

This script synchronizes Datadog Cloud SIEM security signal data with platform incident fields. It retrieves the latest security signal information from Datadog and updates the incident with current field values, owner information, and closure state


## DateToTimeStamp

**Type:** script  
**Product:** Rubrik Security Cloud  

Converts a date to timestamp

**Inputs:**

- `value`: Date to convert


## EntryWidgetRegionNameXCLOUD

**Type:** script  
**Product:** Cloud Incident Response  

Entry widget that returns the region involved in the alert


## EntryWidgetResourceTypeXCLOUD

**Type:** script  
**Product:** Cloud Incident Response  

Entry widget that returns the resource type involved in the alert


## File Reputation - ReversingLabs TitaniumCloud

**Type:** playbook  
**Product:** ReversingLabs TitaniumCloud  

Provides file reputation data for a file (malicious, suspicious, known good or unknown). Required TitaniumCloud API rights: TCA-0101

**Inputs:**

- `hash`: File hash.


## Function Deployment - AWS

**Type:** playbook  
**Product:** AWS Enrichment and Remediation  

This playbook automates the deployment of an AWS Lambda function to manage resources within an Amazon EKS cluster. It ensures that all necessary configurations are created, updated, and verified. This playbook provides a comprehensive, automated approach to deploying an AWS Lambda function for managing resources within an EKS cluster, efficiently handling all configurations and potential errors

**Inputs:**

- `ClusterName`: The name of the cluster.
- `region`: The region of the cluster.
- `FunctionName`: The name of the Lambda function.
- `FunctionCode`: Entry ID of the uploaded base64-encoded contents of the deployment package. Amazon Web Services SDK and CLI clients handle the encoding for 
- `FunctionRuntime`: The runtime environment for the function.
- `FunctionHandler`: The name of the method within your code that Lambda calls to execute your function.
- `LayerName`: The name to assign to the new Lambda layer.
- `LayerRuntime`: The name of the method within your code that Lambda calls to execute your function.


## Function Removal - AWS

**Type:** playbook  
**Product:** AWS Enrichment and Remediation  

This playbook automates the removal of an AWS Lambda function and its associated resources used for managing resources within an Amazon EKS cluster. It ensures all related roles, policies, and security configurations are properly detached and deleted. This playbook provides a comprehensive, automated approach to removing an AWS Lambda function and its related resources, ensuring all configurations and dependencies are properly managed and deleted

**Inputs:**

- `region`: The region of the resource.
- `LambdaFunctionName`: The Lambda function name.
- `LambdaLayerVersion`: The Lambda layer version.
- `LambdaLayerName`: The Lambda layer name.
- `LambdaRoleName`: The lambda role name to delete.
- `LambdaRolePolicyARN`: The ARN of the policy to delete.
- `SecurityGroupID`: The security group ID.


## GCP-IAM

**Type:** integration  
**Product:** GCP IAM  
**Commands:**

- `gcp-iam-projects-get`: 
- `gcp-iam-project-iam-policy-get`: 
- `gcp-iam-project-iam-permission-test`: 
- `gcp-iam-project-iam-member-add`: 
- `gcp-iam-project-iam-member-remove`: 
- `gcp-iam-project-iam-policy-set`: 
- `gcp-iam-project-iam-policy-create`: 
- `gcp-iam-folders-get`: 
- `gcp-iam-folder-iam-policy-get`: 
- `gcp-iam-folder-iam-permission-test`: 
- `gcp-iam-folder-iam-member-add`: 
- `gcp-iam-folder-iam-member-remove`: 
- `gcp-iam-folder-iam-policy-set`: 
- `gcp-iam-folder-iam-policy-create`: 
- `gcp-iam-organizations-get`: 


## GCPOffendingFirewallRule

**Type:** script  
**Product:** GCP Enrichment and Remediation  

Determine potential offending firewall rules in GCP based on port, protocol and possibly target tags (network tags). Considerations

**Inputs:**

- `project_id`: The project to look up firewall rules in. The project ID instead of the project number. No need to supply `projects/` before the ID (i.e., u
- `network_url`: The url of the network objects to lookup firewall rules in. This will be the url of the network and not just the name (i.e. https://www.goog
- `port`: Port to match traffic on for firewall rules.
- `protocol`: Protocol to match traffic on for firewall rules.
- `network_tags`: Network tags on GCP VM instance to match rules based on target tag (optional).


## GCPProjectHierarchy

**Type:** script  
**Product:** GCP Enrichment and Remediation  

Determine GCP project hierarchy by looking up parent objects until the organization level is reached

**Inputs:**

- `project_id`: The project ID instead of the project number. No need to supply projects/ before the ID (i.e., use `project-name` instead of `projects/proje


## Genesys Cloud

**Type:** integration  
**Product:** Genesys Cloud  

Fetch audit events to see changes within a Genesys Cloud organization. This integration was integrated and tested with version 2 of the Genesys Cloud Platform API

**Commands:**

- `genesys-cloud-get-events`: 


## Google Cloud Compute

**Type:** integration  
**Product:** Google Cloud Compute  

Google Compute Engine delivers virtual machines running in Google's innovative data centers and worldwide fiber network. Compute Engine's tooling and workflow support enable scaling from single instances to global, load-balanced cloud computing

**Commands:**

- `gcp-compute-insert-instance`: 


## Google Cloud Functions

**Type:** integration  
**Product:** Google Cloud Functions  

Google Cloud Functions is an event-driven serverless compute platform that enables you to run your code locally or in the cloud without having to provision servers. This integration was integrated and tested with API version 1 of Google Cloud Functions

**Commands:**

- `google-cloud-functions-list`: 


## Google Cloud Logging

**Type:** integration  
**Product:** Google Cloud Logging  

With Google Cloud Logging, users can centralize all their logs in a single location, making it easier to troubleshoot issues and gain insights from their data

**Commands:**

- `gcp-logging-log-entries-list`: 


## Google Cloud Platform

**Type:** integration  
**Product:** GCP  

The GCP Integration automates management and security configurations for Compute Engine, Storage, and Container resources on GCP. This integration was integrated and tested with version v1 (Compute, Storage, Container, SERVICE_USAGE), v3 (Resource Manager)

**Commands:**

- `gcp-compute-firewall-patch`: 
- `gcp-storage-bucket-policy-delete`: 
- `gcp-compute-subnet-update`: 
- `gcp-container-cluster-security-update`: 
- `gcp-gke-cluster-legacy-abac-auth-set`: 
- `gcp-gke-clusters-list`: 
- `gcp-gke-cluster-get`: 
- `gcp-gke-node-pools-list`: 
- `gcp-gke-node-pool-get`: 
- `gcp-gke-node-pool-management-set`: 
- `gcp-gke-operations-list`: 
- `gcp-gke-operation-get`: 
- `gcp-gke-operation-cancel`: 
- `gcp-storage-bucket-metadata-update`: 
- `gcp-iam-project-policy-binding-remove`: 


## Google Cloud Pub/Sub

**Type:** integration  
**Product:** Google Cloud Pub / Sub  

Google Cloud Pub / Sub is a fully-managed real-time messaging service that allows you to send and receive messages between independent applications. This integration was integrated and tested with Google Cloud Pub/Sub

**Commands:**

- `gcp-pubsub-topics-list`: 


## Google Cloud SCC

**Type:** integration  
**Product:** Google Cloud SCC  

Security Command Center is a security and risk management platform for Google Cloud. Security Command Center enables you to understand your security and data attack surface by providing asset inventory and discovery, identifying vulnerabilities and threats, and helping you mitigate and remediate risks across an organization. This integration helps you to perform tasks related to findings and assets. This integration was integrated and tested with version v1 and v2 APIs of GoogleCloudSCC

**Commands:**

- `google-cloud-scc-asset-list`: 
- `google-cloud-scc-finding-list`: 
- `google-cloud-scc-finding-update`: 
- `google-cloud-scc-asset-resource-list`: 
- `google-cloud-scc-asset-owner-get`: 
- `google-cloud-scc-finding-state-update`: 
- `google-cloud-scc-v2-finding-list`: 
- `google-cloud-scc-v2-finding-update`: 
- `google-cloud-scc-v2-finding-state-update`: 
- `google-cloud-scc-finding-mute`: 
- `google-cloud-scc-finding-unmute`: 
- `google-cloud-scc-mute-rule-get`: 
- `google-cloud-scc-mute-rule-create`: 


## GoogleCloudSCCMuteFinding

**Type:** script  
**Product:** Google Cloud SCC  

Mutes a Google Cloud Security Command Center finding by its finding name, using the google-cloud-scc-finding-mute command of the Google Cloud SCC integration. The script is designed to be used as an action button on the Google Cloud SCC Finding incident layout. When the finding_name argument is not provided, the finding name is taken from the GoogleCloudSCC Finding Name incident field, so the button can be clicked without providing any input. After the finding is muted, the mute state returned by the command (MUTED when the response does not contain it) is written to the GoogleCloudSCC Finding Mute Status incident field using the setIncident command

**Inputs:**

- `finding_name`: The relative resource name of the finding to mute.In the v2 API the name may include an optional "locations/{location}" segment. If no locat


## GoogleCloudSCCUnmuteFinding

**Type:** script  
**Product:** Google Cloud SCC  

Unmutes a Google Cloud Security Command Center finding by its finding name, using the google-cloud-scc-finding-unmute command of the Google Cloud SCC integration. The script is designed to be used as an action button on the Google Cloud SCC Finding incident layout. When the finding_name argument is not provided, the finding name is taken from the GoogleCloudSCC Finding Name incident field, so the button can be clicked without providing any input. After the finding is unmuted, the mute state returned by the command (UNMUTED when the response does not contain it) is written to the GoogleCloudSCC Finding Mute Status incident field using the setIncident command

**Inputs:**

- `finding_name`: The relative resource name of the finding to unmute.In the v2 API the name may include an optional "locations/{location}" segment. If no loc


## IP Whitelist - AWS Security Group

**Type:** playbook  
**Product:** AWS - EC2  

Sync a list of IP addresses to an AWS Security Group

**Inputs:**

- `Indicator Query`: Indicators matching the indicator query will be used as playbook input
- `IP`: IP addresses to set in the allow list
- `SecurityGroupName`: Name of the AWS Security Group to update
- `IndicatorTagName`: Name of the Indicator Tag to apply to any IPs allowed by this playbook.


## IP Whitelist - GCP Firewall

**Type:** playbook  
**Product:** Google Cloud Compute  

Set a list of IP addresses in GCP firewall

**Inputs:**

- `Indicator Query`: Indicators to trigger the playbook
- `IP`: IP addresses to allow in GCP Firewall
- `GCPFirewallName`: Name of the GCP Firewall where the playbook should set the IPs
- `IndicatorTagName`: Name of the Indicator Tag to apply to any IPs allowed by this playbook.


## Microsoft Defender for Cloud

**Type:** integration  
**Product:** Microsoft Defender for Cloud  

Unified security management and advanced threat protection across hybrid cloud workloads. For more information see Azure Security Center documentation

**Commands:**

- `azure-sc-list-alert`: 


## Microsoft Defender for Cloud Apps

**Type:** integration  
**Product:** Microsoft Defender for Cloud Apps  

Microsoft Cloud App Security is a multimode Cloud Access Security Broker (CASB). It provides rich visibility, control over data travel, and sophisticated analytics to identify and combat cyber threats across all your cloud services. Use the integration to view and resolve alerts, view activities, view files, and view user accounts. This integration was integrated and tested with version 178 of MicrosoftCloudAppSecurity. To use a Device Code Flow, you need to add a new Azure App Registration in the Azure Portal. To add the registration, refer to the following Microsoft article. To connect to the Microsoft Cloud App Security: At the end of the process you'll see a message that you've logged in successfully. Follow these steps for a self-deployed configuration: Make sure to provide the following permissions for the app to work with Microsoft Cloud App Security: To access the Microsoft Cloud App Security API, you need to grant authorization. See the Microsoft documentation to view a detailed explanation of how to create the Server URL and User key (token). For more information about which permissions are required for the token owner in Microsoft Cloud App Security, see Microsoft Cloud App Security - Manage admin access

**Commands:**

- `microsoft-cas-auth-start`: 
- `microsoft-cas-auth-complete`: 
- `microsoft-cas-auth-reset`: 
- `microsoft-cas-auth-test`: 
- `microsoft-cas-alerts-list`: 
- `microsoft-cas-alert-close-benign`: 
- `microsoft-cas-alert-close-true-positive`: 
- `microsoft-cas-alert-close-false-positive`: 
- `microsoft-cas-activities-list`: 
- `microsoft-cas-files-list`: 
- `microsoft-cas-users-accounts-list`: 


## Microsoft Management Activity API (O365 Azure Events)

**Type:** integration  
**Product:** Microsoft Management Activity API (O365/Azure Events)  

The Microsoft Management Activity API integration enables you to subscribe or unsubscribe to different audits, receive their content, and fetch new content as incidents. Through the integration you can subscribe to new content types or stop your subscription, list the available content of each content type, and most importantly, fetch new content records from content types of your choice as the platform. This integration was integrated and tested with version 1.0 of Microsoft Management Activity API (O365 Azure Events). There are two application authentication methods available

**Commands:**

- `ms-management-activity-start-subscription`: 


## Microsoft Policy And Compliance (Audit Log)

**Type:** integration  
**Product:** Office 365 and Azure (Audit Log)  

Use the integration to get logs from the O365 service

**Commands:**

- `o365-auditlog-search`: 


## Palo Alto Networks - Prisma Cloud Compute

**Type:** integration  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

Prisma™ Cloud Compute Edition delivers cloud workload protection (CWPP) for modern enterprises, providing holistic protection across hosts, containers, and serverless deployments in any cloud, throughout the application lifecycle. Prisma Cloud Compute Edition is cloud native and API-enabled, protecting all your workloads regardless of their underlying compute technology or the cloud in which they run. This integration lets you import Palo Alto Networks - Prisma Cloud Compute alerts into the platform

**Commands:**

- `prisma-cloud-compute-profile-host-list`: 
- `prisma-cloud-compute-profile-container-list`: 
- `prisma-cloud-compute-profile-container-hosts-list`: 
- `prisma-cloud-compute-profile-container-forensic-list`: 
- `prisma-cloud-compute-host-forensic-list`: 
- `prisma-cloud-compute-console-version-info`: 
- `prisma-cloud-compute-custom-feeds-ip-list`: 
- `prisma-cloud-compute-custom-feeds-ip-add`: 
- `prisma-cloud-compute-custom-feeds-ip-remove`: 
- `prisma-cloud-compute-custom-feeds-malware-list`: 
- `prisma-cloud-compute-custom-feeds-malware-add`: 
- `prisma-cloud-compute-defenders-list`: 
- `prisma-cloud-compute-collections-list`: 
- `prisma-cloud-compute-container-namespace-list`: 
- `prisma-cloud-compute-images-scan-list`: 


## Palo Alto Networks - Strata Cloud Manager

**Type:** integration  
**Product:** Palo Alto Networks - Strata Cloud Manager  

Provides commands for interaction with Prisma SASE API. This integration was integrated and tested with version v1 of Palo Alto Networks - Prisma SASE

**Commands:**

- `prisma-sase-security-rule-create`: 
- `prisma-sase-security-rule-list`: 
- `prisma-sase-candidate-config-push`: 
- `prisma-sase-security-rule-update`: 
- `prisma-sase-address-object-update`: 
- `prisma-sase-config-job-list`: 
- `prisma-sase-security-rule-delete`: 
- `prisma-sase-address-object-create`: 
- `prisma-sase-address-object-delete`: 
- `prisma-sase-address-object-list`: 
- `prisma-sase-tag-list`: 
- `prisma-sase-tag-create`: 
- `prisma-sase-tag-update`: 
- `prisma-sase-tag-delete`: 
- `prisma-sase-address-group-list`: 


## Palo Alto Networks Prisma AIRS - AI Red Teaming

**Type:** integration  
**Product:** Palo Alto Networks - Prisma AIRS AI Security  

Discover and remediate AI application vulnerabilities with Palo Alto Networks Prisma AIRS AI Red Teaming: manage targets and adapters, run and monitor red-team scans, review attack reports and remediation guidance, and curate prompt sets and custom attacks. This integration was integrated and tested with the Palo Alto Networks Prisma AIRS AI Red Teaming API as of June 2026

**Commands:**

- `prisma-airs-redteam-targets-list`: 
- `prisma-airs-redteam-targets-create`: 
- `prisma-airs-redteam-targets-get`: 
- `prisma-airs-redteam-targets-update`: 
- `prisma-airs-redteam-targets-delete`: 
- `prisma-airs-redteam-targets-probe`: 
- `prisma-airs-redteam-targets-profile`: 
- `prisma-airs-redteam-targets-update-profile`: 
- `prisma-airs-redteam-targets-metadata`: 
- `prisma-airs-redteam-targets-validate-auth`: 
- `prisma-airs-redteam-targets-templates`: 
- `prisma-airs-redteam-targets-error-logs`: 
- `prisma-airs-redteam-scan-error-logs`: 
- `prisma-airs-redteam-dashboard-scan-statistics`: 
- `prisma-airs-redteam-dashboard-score-trend`: 


## Palo Alto Networks Prisma AIRS - AI Runtime Security

**Type:** integration  
**Product:** Palo Alto Networks - Prisma AIRS AI Security  

Integrate with Palo Alto Networks Prisma AIRS for AI security capabilities including runtime scanning, red teaming, AI supply chain security, and DLP configuration. This integration was integrated and tested with Palo Alto Networks Prisma AIRS - AI Runtime Security

**Commands:**

- `prisma-airs-runtime-scan`: 


## Palo Alto Networks Prisma AIRS - AI Supply Chain Security

**Type:** integration  
**Product:** Palo Alto Networks - Prisma AIRS AI Security  

Scan and govern AI models with Palo Alto Networks Prisma AIRS AI Supply Chain Security: model scans, evaluations, violations, labels, model groups, and security rules. This integration was integrated and tested with Palo Alto Networks Prisma AIRS - AI Supply Chain Security

**Commands:**

- `prisma-airs-model-security-scans-list`: 
- `prisma-airs-model-security-scans-create`: 
- `prisma-airs-model-security-scans-get`: 
- `prisma-airs-model-security-scans-violations`: 
- `prisma-airs-model-security-labels-keys`: 
- `prisma-airs-model-security-labels-values`: 
- `prisma-airs-model-security-labels-add`: 
- `prisma-airs-model-security-labels-set`: 
- `prisma-airs-model-security-labels-delete`: 
- `prisma-airs-model-security-scans-evaluation`: 
- `prisma-airs-model-security-scans-violation`: 
- `prisma-airs-model-security-scans-files`: 
- `prisma-airs-model-security-scans-evaluations`: 
- `prisma-airs-model-security-models-list`: 
- `prisma-airs-model-security-models-get`: 


## PCComputeContainerComplianceIssuesButton

**Type:** script  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

This script runs the "prisma-cloud-compute-container-scan-results-list" command for a specific container ID and returns details about its compliance issues, if found. If any compliance issues found, it will create a new tab in the layout called "Detailed Compliance Issues" showing the issues details. Returns the following fields for each compliance ID

**Inputs:**

- `container_id`: The container ID to be enriched.
- `compliance_ids`: A comma-separated list of compliance IDs to be enriched. If no value provided, it will return results for all compliance IDs.


## PCComputeHostComplianceIssuesButton

**Type:** script  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

This script runs the "prisma-cloud-compute-hosts-scan-list" command for a specific hostname and returns details about its compliance issues, if found. If any compliance issues found, it will create a new tab in the layout called "Detailed Compliance Issues" showing the issues details. Returns the following fields for each compliance ID

**Inputs:**

- `hostname`: The hostname to be enriched.
- `compliance_ids`: A comma-separated list of compliance IDs to be enriched. If no value provided, it will return results for all compliance IDs.


## PCComputeImageComplianceIssuesButton

**Type:** script  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

This script runs the "prisma-cloud-compute-images-scan-list" command for a specific container id and returns details about its compliance issues, if found. If any compliance issues found, it will create a new tab in the layout called "Detailed Compliance Issues" showing the issues details. Returns the following fields for each compliance ID

**Inputs:**

- `image_id`: The image ID to be enriched.
- `compliance_ids`: A comma-separated list of compliance IDs to be enriched. If no value provided, it will return results for all compliance IDs.


## Prisma Access

**Type:** integration  
**Product:** Palo Alto Networks - Strata Cloud Manager  
**Commands:**

- `prisma-access-logout-user`: 


## Prisma Access - Logout User

**Type:** playbook  
**Product:** Palo Alto Networks - Strata Cloud Manager  

This playbook forces logout of a specific user and computer from Prisma Access

**Inputs:**

- `username`: Username to log out with Prisma Access
- `domain`: Domain name for the user
- `hostname`: Hostname of the machine to log out


## Prisma Access Whitelist Egress IPs on SaaS Services

**Type:** playbook  
**Product:** Palo Alto Networks - Strata Cloud Manager  

Retrieve Prisma Access Egress IP for specific geographic Zones and populate in security groups within cloud services

**Inputs:**

- `Indicator Query`: Indicators matching the indicator query will be used as playbook input
- `AWSSecurityGroupName`: Name of the AWS Security Group to update with the IPs.
- `GCPFirewallName`: 
- `OktaZoneID`: ID of the Okta Zone to update. Use !okta-list-zones to obtain


## Prisma Cloud - Find AWS Resource by FQDN

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find AWS resources by FQDN using Prisma Cloud inventory. Supported services: EC2, Application Load Balancer, ECS, Route53, CloudFront, S3, API Gateway. Supported the platform.0.0 and later

**Inputs:**

- `FQDN`: FQDN to look up
- `AWSDomains`: AWS domains (comma separated)


## Prisma Cloud - Find AWS Resource by FQDN v2

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find AWS resources by FQDN using Prisma Cloud inventory. Supported services: EC2, Application Load Balancer, ECS, Route53, CloudFront, S3, API Gateway

**Inputs:**

- `FQDN`: FQDN to look up
- `AWSDomains`: A comma-separated list of AWS domains.


## Prisma Cloud - Find AWS Resource by Public IP

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find AWS resources by Public IP using Prisma Cloud inventory. Supported services: EC2, Network Load Balancer, ECS, Route53. Supported the platform.0.0 and later

**Inputs:**

- `PublicIPAddress`: Public IP Address to look up


## Prisma Cloud - Find AWS Resource by Public IP v2

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find AWS resources by Public IP using Prisma Cloud inventory. Supported services: EC2, Network Load Balancer, ECS, Route53

**Inputs:**

- `PublicIPAddress`: Public IP address to look up.


## Prisma Cloud - Find Azure Resource by FQDN

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find Azure resources by FQDN using Prisma Cloud inventory. Supported services: Azure VM, Azure Load Balancer, Azure Application Gateway, AKS, Azure Web Apps, Azure Storage. Supported the platform.0.0 and later

**Inputs:**

- `FQDN`: FQDN to look up
- `AzureDomains`: Azure domains (comma separated)


## Prisma Cloud - Find Azure Resource by FQDN v2

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find Azure resources by FQDN using Prisma Cloud inventory. Supported services: Azure VM, Azure Load Balancer, Azure Application Gateway, AKS, Azure Web Apps, Azure Storage

**Inputs:**

- `FQDN`: FQDN to look up.
- `AzureDomains`: A comma-separated list of Azure domains.


## Prisma Cloud - Find Azure Resource by Public IP

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find Azure resources by Public IP using Prisma Cloud inventory. Supported services: Azure VM, Azure Load Balancer, Azure Application Gateway, Azure Web Apps. Supported the platform.0.0 and later

**Inputs:**

- `PublicIPAddress`: Public IP Address to look up


## Prisma Cloud - Find Azure Resource by Public IP v2

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find Azure resources by Public IP using Prisma Cloud inventory. Supported services: Azure VM, Azure Load Balancer, Azure Application Gateway, Azure Web Apps

**Inputs:**

- `PublicIPAddress`: Public IP address to look up.


## Prisma Cloud - Find GCP Resource by FQDN

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find GCP resources by FQDN using Prisma Cloud inventory. Supported services: Cloud DNS. Supported the platform.0.0 and later

**Inputs:**

- `FQDN`: FQDN to look up
- `GCPDomains`: GCP domains (comma separated)


## Prisma Cloud - Find GCP Resource by FQDN v2

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find GCP resources by FQDN using Prisma Cloud inventory. Supported services: Cloud DNS

**Inputs:**

- `FQDN`: FQDN to look up.
- `GCPDomains`: A comma-separated list of GCP domains.


## Prisma Cloud - Find GCP Resource by Public IP

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find GCP resources by Public IP using Prisma Cloud inventory. Supported services: GCE, Load Balancing, GKE. Supported the platform.0.0 and later

**Inputs:**

- `PublicIPAddress`: Public IP Address to look up


## Prisma Cloud - Find GCP Resource by Public IP v2

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find GCP resources by Public IP using Prisma Cloud inventory. Supported services: GCE, Load Balancing, GKE

**Inputs:**

- `PublicIPAddress`: Public IP address to look up.


## Prisma Cloud - Find Public Cloud Resource by FQDN

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find Public Cloud resources by FQDN using Prisma Cloud inventory Supported the platform.0.0 and later

**Inputs:**

- `FQDN`: FQDN to look up
- `CloudProvider`: Public Cloud Provider (AWS, Azure, GCP)


## Prisma Cloud - Find Public Cloud Resource by Public IP

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find a Public Cloud resource by Public IP using Prisma Cloud inventory Supported the platform.0.0 and later

**Inputs:**

- `PublicIPAddress`: Public IP Address to look up
- `CloudProvider`: Public Cloud Provider (AWS, Azure, GCP)


## Prisma Cloud - Find Public Cloud Resource by Public IP v2

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Find Public Cloud resource by Public IP using Prisma Cloud inventory

**Inputs:**

- `PublicIPAddress`: Public IP Address to look up
- `CloudProvider`: Public Cloud Provider (AWS, Azure, GCP)


## Prisma Cloud - Get Account Owner

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Retrieves the details of the owner of a given cloud account from the following playbooks

**Inputs:**

- `AccountID`: The account ID to search the owner for.
- `Namespace`: The namespace that the playbook would search associated users with.
- `Provider`: The account CSP.Available options:- PrismaCloud- GCP
- `EnrichUsers`: Whether to enrich found users or not.


## Prisma Cloud - Get Owner By Namespace

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

This playbook will retrieve the potential owners of a runtime audit alert. This id done using the "Namespace" value of the incident in order to query associated resource lists and user roles with associated users. Eventually the playbook returns a list of user objects (if found)

**Inputs:**

- `Namespace`: The namespace that the playbook would search associated users with.
- `EnrichUsers`: Whether to enrich found users or not.


## Prisma Cloud - Network API and Anomaly Incidents

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

This playbook handles incidents of internet exposed services and detects potential risky configurations that can make your cloud environment vulnerable to attacks, and incidents of unusual network and user activity for all users, and are especially critical for privileged users and assumed roles where detecting unusual activity may indicate the first steps in a potential misuse or account compromise

**Inputs:**

- `serviceNowShortDescription`: A short description of the ticket.
- `serviceNowImpact`: The impact for the new ticket. Leave empty for ServiceNow default impact.
- `serviceNowUrgency`: The urgency of the new ticket. Leave empty for ServiceNow default urgency.
- `serviceNowSeverity`: The severity of the new ticket. Leave empty for ServiceNow default severity.
- `serviceNowTicketType`: The ServiceNow ticket type. Options are "incident", "problem", "change_request", "sc_request", "sc_task", or "sc_req_item". Default is "inci
- `serviceNowCategory`: The category of the ServiceNow ticket.
- `serviceNowAssignmentGroup`: The group to which to assign the new ticket.
- `ZendeskPriority`: The urgency with which the ticket should be addressed. Allowed values are "urgent", "high", "normal", or "low".


## Prisma Cloud - RQL Execution

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

This playbook enables Prisma Cloud RQL Execution from the alert layout


## Prisma Cloud - VM Alert Prioritization

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

This playbook handles incidents related to dozens of Prisma Cloud public VM alerts. It determines the severity of the ingested alert based on data returned from the platform, with all of the relevant information. The playbook updates the the platform. It also extracts and enriches indicators using existing configured integrations and then closes the investigation. The flow of this playbook is as following: 1) Check the CSP type. 2) Check whether there's a public IP associated to the instance. In case there is, it will continue to other steps, if not, it will set the severity of the incident to "Low" and will close the incident. 3) Check if there are any vulnerabilities or findings related to the instance. 4) Check if there are any IAM permissions associated to the instance. 5) Set the incident severity based on the results: This playbook will run when a new incident is created with the Prisma Cloud - VM Alert Prioritization incident type which also includes a dedicated layout. The Layout There are 2 main tabs in the layout: Case Info and Investigation

**Inputs:**

- `JiraProjectName`: The project name with which to associate the issue.
- `JiraIssueTypeName`: The name of the issue type to be opened.
- `CloseIncidentAfterNotification`: Whether to close the incident after Jira/Slack issue was opened.
- `SlackChannelName`: The name of the Slack channel to which to send the message.
- `SlackChannelID`: The ID of the Slack channel to which to send the message.


## Prisma Cloud Compute - Audit Alert

**Type:** playbook  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

Parses Prisma Cloud Compute audit alerts. This is a default playbook


## Prisma Cloud Compute - Audit Alert v2

**Type:** playbook  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

Default playbook for parsing and enrichment of Prisma Cloud Compute audit alerts

**Inputs:**

- `baseUrl`: The base URL of the Prisma Cloud Compute Instance used to create a link back to the alerts for an image.
- `Project`: A specific project name to get alert profiles for


## Prisma Cloud Compute - Audit Alert v3

**Type:** playbook  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

Default playbook for parsing and enrichment of Prisma Cloud Compute audit alerts. The playbook has the following sections: Enrichment: Remediation: Currently, the playbook supports incidents created by Runtime and WAAS triggers

**Inputs:**

- `baseUrl`: The base URL of the Prisma Cloud Compute Instance used to create a link back to the alerts for an image.
- `Project`: A specific project name to get alert profiles for
- `AutoBlockIndicators`: Relevant to the "Block Indicators - Generic v3" playbook.Possible values: True/False. Default: True.Should the given indicators be automatic
- `autoResourceRemediation`: Relevant to the "Cloud Response - Generic playbook".Whether to execute the resource remediation flow automatically.Available options:- True-
- `resourceRemediationType`: Relevant to the "Cloud Response - Generic playbook".Available options:- Stop- Delete
- `autoAccessKeyRemediation`: Relevant to the "Cloud Response - Generic playbook".Whether to execute the access key remediation flow automatically.Available options:- Tru
- `accessKeyRemediationType`: Relevant to the "Cloud Response - Generic playbook".Choose the remediation type for the user's access key.Available types:Disable - for disa
- `userRemediationType`: Relevant to the "Cloud Response - Generic playbook".Whether to execute the user remediation flow automatically.Choose the remediation type f


## Prisma Cloud Compute - Cloud Discovery Alert

**Type:** playbook  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

Parses Prisma Cloud Compute Cloud Discovery alerts. This is a default playbook


## Prisma Cloud Compute - Get Defender Logs

**Type:** playbook  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

This is a sub-playbook of the “Prisma Cloud Compute - Audit Alert v2” playbook

**Inputs:**

- `Hostname`: The Defender hostname. Can be retrieved from the "prisma-cloud-compute-defenders-list" command.
- `Project`: The project to retrieve the backups from.


## Prisma Cloud Compute - Vulnerability Alert

**Type:** playbook  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

Parses Prisma Cloud Compute vulnerability alerts. This is a default playbook


## Prisma Cloud Correlate Alerts

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Search alerts in Prisma Cloud for a specific asset ID and, if present in platform, link them. Supported the platform.0.0 and later

**Inputs:**

- `Prisma Cloud Attribution`: Attribution information from Prisma Cloud.
- `Link Incidents`: Link found Prisma Cloud incidents to current one?


## Prisma Cloud Correlate Alerts v2

**Type:** playbook  
**Product:** Prisma Cloud by Palo Alto Networks  

Search alerts in Prisma Cloud for a specific asset ID and, if present in platform, link them

**Inputs:**

- `Prisma Cloud Attribution`: Attribution information from Prisma Cloud.
- `Link Incidents`: Link found Prisma Cloud incidents to current one?


## Prisma Cloud v2

**Type:** integration  
**Product:** Prisma Cloud by Palo Alto Networks  

Prisma Cloud secures infrastructure, workloads and applications, across the entire cloud-native technology stack. This integration was integrated and tested with version 23.2.1 of PrismaCloud Some changes have been made that might affect your existing content. If you are upgrading from a previous version of this integration, see Breaking Changes

**Commands:**

- `prisma-cloud-alert-dismiss`: 
- `prisma-cloud-alert-get-details`: 
- `prisma-cloud-alert-filter-list`: 
- `prisma-cloud-remediation-command-list`: 
- `prisma-cloud-alert-remediate`: 
- `prisma-cloud-alert-reopen`: 
- `prisma-cloud-alert-search`: 
- `prisma-cloud-config-search`: 
- `prisma-cloud-event-search`: 
- `prisma-cloud-network-search`: 


## Prisma SASE - Add IPs to Static Address Group

**Type:** playbook  
**Product:** Palo Alto Networks - Strata Cloud Manager  

This playbook appends a Static Address Group with provided IPs

**Inputs:**

- `TSGID`: Tenant services group ID. If not provided, the tsg_id integration parameter will be used as the default.
- `AutoCommit`: Possible Values:True -&gt; Will commit and push configuration.False -&gt; Manual push will be required.Else --&gt; Will ignore the push sect
- `IP`: A comma-separated list of IP addresses.
- `AddressGroupName`: The address group name to be appanded.
- `Folder`: The configuration folder group setting.The default value is 'Shared'.


## Prisma SASE - Create a security pre-rule for EDL

**Type:** playbook  
**Product:** Palo Alto Networks - Strata Cloud Manager  

This playbook helps to create a security rule to block indicators from an EDL. This playbook should run only once to setup the EDL object and its rule

**Inputs:**

- `TSGID`: Tenant services group ID. If not provided, the tsg_id integration parameter will be used as the default.
- `Folder`: The configuration folder group setting.The default value is 'Shared'.
- `URL`: The source URL. If the type is ip, url or domain, a value must be provided.
- `EDLObjectName`: The external dynamic list object name.
- `RuleName`: The Security Policy Rule name will be created for blocking the indicators.
- `EDLObjectType`: Possible values:domain,ip,url,predefined_ip,predefined_url
- `AutoCommit`: Possible Values:True -&gt; Will commit and push configuration.False -&gt; Manual push will be required.Else --&gt; Will ignore the push sect


## Prisma SASE - Create Address Object

**Type:** playbook  
**Product:** Palo Alto Networks - Strata Cloud Manager  

This playbook creates new address objects in the Prisma SASE Object section. Those objects can be used later on in other objects such as Security Rules

**Inputs:**

- `IP`: The address value (should match the type)
- `TSGID`: Tenant services group ID. If not provided, the tsg_id integration parameter will be used as the default.
- `Folder`: The configuration folder group setting.The default value is 'Shared'.
- `AutoCommit`: Possible values:True -&gt; Will commit and push configuration.False -&gt; Manual push will be required.Else --&gt; Will ignore the push sect
- `Type`: IP Netmask: IP address or a network using the slash notation - ip_address/mask.IP Range: Range of IP addresses using the notation ip_address
- `limit`: Default: 50 This input controls the limit size for the get IP objects command.This will help to avoid object duplicates in the systems.


## Prisma SASE - Create or Edit EDL object

**Type:** playbook  
**Product:** Palo Alto Networks - Strata Cloud Manager  

This playbook helps to create an EDL object within the Prisma SASE Objects section

**Inputs:**

- `Name`: The external dynamic list object name.
- `Folder`: The configuration folder group setting.The default value is 'Shared'.
- `TSGID`: Tenant services group ID. If not provided, the tsg_id integration parameter will be used as the default.
- `IPListName`: The predefined IP list. If the type is predefined_ip, a value must be provided.Possible values: panw-bulletproof-ip-list,panw-highrisk-ip-li
- `URLListName`: The predefined URL list. If the type is predefined_url, a value must be provided.Possible value:panw–auth-portal-exclude-list
- `SourceURL`: The source URL. If the type is ip, url or domain, a value must be provided.
- `Frequency`: Frequency to check for updates on the EDL URL.Possible values:daily,five_minute,hourly,monthly,weekly
- `FrequencyTime`: The frequency hour. If the frequency argument is daily, weekly or monthly, a value must be provided. Possible values are 00-23.


## Prisma SASE - Create or Edit Security Policy Rule

**Type:** playbook  
**Product:** Palo Alto Networks - Strata Cloud Manager  

This playbook handles the creation or editing of the Security Policy Rule for Prisma SASE integration

**Inputs:**

- `TSGID`: Tenant services group ID. If not provided, the tsg_id integration parameter will be used as the default.
- `Folder`: The configuration folder group setting.The default value is 'Shared'.
- `Action`: Possible values:allow,deny,drop,reset-both,reset-client,reset-server.
- `Position`: Rule position.The default value is 'pre'.
- `Source`: A comma-separated list of source networks.The default value is 'any'.
- `Destination`: A comma-separated list of destination networks.The default value is 'any'.
- `Service`: Services the rule applies to.Default value is 'any'.
- `Application`: A comma-separated list of applications.Default value is 'any'.


## PrismaCloud IAM

**Type:** integration  
**Product:** Prisma Cloud by Palo Alto Networks  

Note: This integration should be used as part of our Identity Lifecycle Management premium pack. For more information, please refer to the Identity Lifecycle Management article. The Prisma Cloud IAM API consists of a set of API endpoints that allow customers to perform CRUD operation on their user profiles

**Commands:**

- `iam-create-user`: 
- `iam-update-user`: 
- `iam-get-user`: 
- `iam-disable-user`: 


## PrismaCloudAttribution

**Type:** script  
**Product:** Prisma Cloud by Palo Alto Networks  

Recursively extracts specified fields from provided list of assets for Prisma Cloud attribution use case

**Inputs:**

- `assets`: List of Prisma Cloud assets to return.
- `fields`: Fields to be returned (comma separated).


## PrismaCloudComputeComplianceTable

**Type:** script  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

Iterate over EnrichedComplianceIssue information in the context data and add the important keys to a table under PrismaCloudCompute.ComplianceTable or a provided grid id

**Inputs:**

- `resourceType`: Type of resource to add to the table.
- `contextPath`: The context path to the enriched compliance issues list.


## PrismaCloudComputeParseCloudDiscoveryAlert

**Type:** script  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

Parse Cloud Discovery alert raw JSON data

**Inputs:**

- `alert_raw_json`: The compliance alert raw JSON


## PrismaCloudComputeParseComplianceAlert

**Type:** script  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

Parse Compliance alert raw JSON data

**Inputs:**

- `alert_raw_json`: The compliance alert raw JSON


## PrismaCloudComputeParseVulnerabilityAlert

**Type:** script  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

Parse Vulnerability alert raw JSON data

**Inputs:**

- `alert_raw_json`: The vulneribility alert raw JSON data


## PrismaCloudLocalTrustedImagesListUpdate

**Type:** script  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

Takes the results of "prisma-cloud-compute-images-scan-list" and "prisma-cloud-ci-scan-results-list" commands and creates or updates a list of trusted images which can be used for updating the "Trusted Images" list in Prisma Cloud, using the PrismaCloudRemoteTrustedImagesListUpdate automation

**Inputs:**

- `list_name`: The name of the the platform.
- `deployed_images`: The results of the "prisma-cloud-compute-images-scan-list" command.
- `passed_ci_scan_images`: The "entityInfo" results of the "prisma-cloud-compute-ci-scan-results-list" command.
- `time_frame`: The time passed since the last time an image was updated based on the given deployed_images and passed_ci_scan_images inputs. If an image wa


## PrismaCloudRemoteTrustedImagesListUpdate

**Type:** script  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

Gets the existing "Trusted Images" results from Prisma Cloud Compute and updates the relevant trust group with the images stored in the given internal list

**Inputs:**

- `list_name`: The name of the platform internal list we wish to use in order to update the remote trust images list.
- `trusted_group_id`: The trusted group which should be updated with the images of the given list. In order to get the trusted groups ID, either use the Prisma Cl
- `current_trusted_images`: The current state of the trusted images in Prisma Cloud. Can be retrieved with the "prisma-cloud-compute-trusted-images-list" command.


## Proofpoint Cloud Threat Response

**Type:** integration  
**Product:** Proofpoint Cloud Threat Response  

Fetches Proofpoint Cloud Threat Response (CTR) incidents into the platform, and exposes commands to list and retrieve incident details. This integration was integrated and tested with version 1.0 of Proofpoint Cloud Threat Response

**Commands:**

- `proofpoint-ctr-incidents-list`: 
- `proofpoint-ctr-incident-get`: 


## Radware Cloud DDoS Protection Services

**Type:** integration  
**Product:** Radware Cloud DDoS Protection Services  

Radware Cloud Service provides customers and partners with the ability to programmatically perform service-related actions. The integration can be used to automate application and assets creation and day-to-day management to retrieve up-to-date data about Security Events and Operational Alerts This integration was integrated and tested with version 25.3.1 of Radware Cloud DDoS Protection Services

**Commands:**

- `radware-cloud-ddos-protection-services-get-events`: 


## Rapid7 InsightVM Cloud

**Type:** integration  
**Product:** Rapid7 InsightVM Cloud  

InsightVM is a Vulnerability Management Tool which Scan your Network, Eliminate Vulnerabilities, Track and Communicate progress

**Commands:**

- `insightvm-cloud-get-asset`: 
- `insightvm-cloud-get-scan`: 
- `insightvm-cloud-get-scan-engines`: 
- `insightvm-cloud-get-health-check`: 
- `insightvm-cloud-search-assets`: 
- `insightvm-cloud-last-sites`: 
- `insightvm-cloud-search-vulnerabilities`: 
- `insightvm-cloud-start-scan`: 
- `insightvm-cloud-stop-scan`: 


## ReversingLabs TitaniumCloud v2

**Type:** integration  
**Product:** ReversingLabs TitaniumCloud  

ReversingLabs TitaniumCloud provides threat analysis data from various ReversingLabs cloud services

**Commands:**

- `reversinglabs-titaniumcloud-file-reputation`: 


## Rubrik Data Object Discovery - Rubrik Polaris

**Type:** playbook  
**Product:** Rubrik Security Cloud  

Data discovery of the object available in the incident

**Inputs:**

- `object_name`: Name of the object to discover.
- `object_id`: ID of the object to discover.


## Rubrik File Context Analysis - Rubrik Polaris

**Type:** playbook  
**Product:** Rubrik Security Cloud  

This playbook fetches file context information for the provided file, folder, or file share name and the object ID to get the policy hits

**Inputs:**

- `object_id`: The Object ID or the Snappable ID. Default can be received from incident if present.Note: Users can get the list of the object IDs by execut
- `file_name`: Specify the name of the file, folder, or file share object.
- `file_path`: Specify the standard folder/directory path to filter with.
- `user_id`: Specify the user ID to filter with.Note: Users can get the list of the user IDs by executing the "rubrik-sonar-user-access-list" command.
- `limit`: Number of results to retrieve in the response. The maximum allowed size is 1000.


## Rubrik List Snapshots - Rubrik Polaris

**Type:** playbook  
**Product:** Rubrik Security Cloud  

List snapshots for all object ids provided

**Inputs:**

- `object_id`: ID of the object to discover.


## Rubrik Object Context Analysis - Rubrik Polaris

**Type:** playbook  
**Product:** Rubrik Security Cloud  

This playbook will investigate based on the object type from the Rubrik Anomaly incident to retrieve the policy hits of the files related to the object

**Inputs:**

- `object_id`: The Object ID or the Snappable ID. Default can be received from incident if present.
- `object_type`: The Object type. Default can be received from incident if present.


## Rubrik Polaris - Anomaly Analysis

**Type:** playbook  
**Product:** Rubrik Security Cloud  

Monitor the progress of a Rubrik Radar anomaly event and use Rubrik Sonar to check for data classification hits


## Rubrik Poll Async Result - Rubrik Polaris

**Type:** playbook  
**Product:** Rubrik Security Cloud  

Poll async result for any asynchronous request made to rubrik

**Inputs:**

- `ClusterId`: Cluster ID of the object.
- `RequestId`: ID of the asynchronous request.
- `PollingInterval`: Frequency with which the polling command will run (minutes).
- `PollingTimeout`: Amount of time to poll before declaring a timeout and resuming the playbook (in minutes).
- `cluster_ip_address`: IP address of the cluster node to access the download link. Only required to retrieve the results of the command "rubrik-gps-snapshot-files-


## Rubrik Retrieve Anomaly Result - Rubrik Security Cloud

**Type:** playbook  
**Product:** Rubrik Security Cloud  

This playbook retrieves the list of anomaly files for the provided snapshot ID (or activity series ID) and generates the downloadable links for the file path(s)

**Inputs:**

- `file_paths`: The absolute path of the file(s) for which a downloadable link needs to be generated.
- `snapshot_id`: The snapshot ID for which to retrieve the anomaly results. Default can be received from incident (activity series ID) if present.Note: Users
- `download_csv_file`: If set to True, the playbook downloads the anomaly analysis csv file directly on platform server.
- `close_notes`: Add notes for closing the incident.
- `object_id`: The Object ID or the Snappable ID.Note: Users can get the list of the object IDs by executing the "rubrik-polaris-object-list" command.


## Rubrik Retrieve User Access Information - Rubrik Polaris

**Type:** playbook  
**Product:** Rubrik Security Cloud  

This playbook retrieves User Intelligence information for the provided username or email, which includes the user's risk level and the types of analyzer hits

**Inputs:**

- `user_name`: The name of the user to search for.
- `user_email`: The email or the UPN of the user to search for.
- `search_time_period`: Specify the search time period to look for user access.
- `risk_levels`: The comma-separated list of risk levels.Supported values are: UNKNOWN_RISK, HIGH_RISK, MEDIUM_RISK, LOW_RISK, NO_RISK.Note: For any other va


## Rubrik Security Cloud

**Type:** integration  
**Product:** Rubrik Security Cloud  

The Rubrik Security Cloud integration will fetch the Rubrik Anomaly Event and is rich with commands to perform the on-demand scans, backups, recoveries and many more features to manage and protect the organizational data. This integration was integrated and tested with version 1.0.0 of Rubrik Security Cloud

**Commands:**

- `rubrik-radar-analysis-status`: 
- `rubrik-sonar-sensitive-hits`: 
- `rubrik-cdm-cluster-location`: 
- `rubrik-cdm-cluster-connection-state`: 
- `rubrik-polaris-object-search`: 
- `rubrik-sonar-policies-list`: 
- `rubrik-sonar-policy-analyzer-groups-list`: 
- `rubrik-polaris-vm-object-metadata-get`: 
- `rubrik-polaris-vm-objects-list`: 
- `rubrik-sonar-ondemand-scan`: 
- `rubrik-sonar-ondemand-scan-status`: 
- `rubrik-polaris-vm-object-snapshot-list`: 
- `rubrik-sonar-ondemand-scan-result`: 
- `rubrik-radar-anomaly-csv-analysis`: 
- `rubrik-sonar-csv-download`: 


## Rubrik Sensitive Data Object Discovery - Rubrik Security Cloud

**Type:** playbook  
**Product:** Rubrik Security Cloud  

This playbook retrieves the files information for the sensitive data object and updates the incident with the data

**Inputs:**

- `object_id`: The object ID.Note: Users can retrieve the object ID by executing the "rubrik-polaris-objects-list" command.
- `snapshot_id`: The snapshot ID.Note: Users can retrieve the snapshot ID by executing the "rubrik-polaris-object-snapshot-list" command.
- `limit`: Number of results to retrieve in the response. The maximum allowed size is 1000.


## Rubrik Sensitive Data Object File Analysis - Rubrik Security Cloud

**Type:** playbook  
**Product:** Rubrik Security Cloud  

This playbook retrieves detailed information for a file

**Inputs:**

- `object_id`: The object ID.Note: Users can retrieve the object ID by executing the "rubrik-polaris-objects-list" command.
- `snapshot_id`: The snapshot ID.Note: Users can retrieve the snapshot ID by executing the "rubrik-polaris-object-snapshot-list" command.
- `file_path`: The full path of the file for which to retrieve information.
- `resolve_sids`: Whether to resolve SIDs to display names in the file response.


## Rubrik Sensitive Data Object Files Discovery - Rubrik Security Cloud

**Type:** playbook  
**Product:** Rubrik Security Cloud  

This playbook retrieves the list of files for the sensitive data object

**Inputs:**

- `object_id`: The object ID.Note: Users can retrieve the object ID by executing the "rubrik-polaris-objects-list" command.
- `snapshot_id`: The snapshot ID.Note: Users can retrieve the snapshot ID by executing the "rubrik-polaris-object-snapshot-list" command.
- `limit`: Number of results to retrieve in the response. The maximum allowed size is 1000.


## Rubrik Update Anomaly Status- Rubrik Security Cloud

**Type:** playbook  
**Product:** Rubrik Security Cloud  

This playbook updates status of the Anomaly Detection snapshot for the provided anomaly ID (or activity series ID) and workload ID (or Object ID)

**Inputs:**

- `anomaly_type`: The type of the anomaly.Note: For Anomaly Type, users can execute the "rubrik-radar-suspicious-file-list" command.
- `anomaly_id`: The ID of the Anomaly or Activity Series ID.Note: For Activity Series ID, users can execute the "rubrik-event-list" command with the "activi
- `workload_id`: The workload ID (Snappable ID).Note: Users can execute the "rubrik-event-list" command with the "activity_type" argument set to "ANOMALY" an


## Rubrik User Access Analysis - Rubrik Polaris

**Type:** playbook  
**Product:** Rubrik Security Cloud  

This playbook fetches User Intelligence information for the provided username or email, and then increases the incident severity based on the user risk levels

**Inputs:**

- `user_name`: The name of the user to search for.
- `user_email`: The email or the UPN of the user to search for.
- `search_time_period`: Specify the search time period to look for user access.
- `risk_levels`: The comma-separated list of risk levels.Supported values are: UNKNOWN_RISK, HIGH_RISK, MEDIUM_RISK, LOW_RISK, NO_RISK.Note: For any other va


## Rubrik Workload Analysis - Rubrik Security Cloud

**Type:** playbook  
**Product:** Rubrik Security Cloud  

This playbook fetches workload information for the provided IPs or domains/hostnames, and then increases the platform incident severity based on the workload risk levels and threat information

**Inputs:**

- `increase_severity_by`: Specify the level in number by which to increase the platform incident severity. Only applicable if match found for the malicious threat hun
- `ip_addresses`: The optional comma-separated list of IP address(es) for which to use workload information to increase the platform incident severity.
- `domains`: The optional comma-separated list of domain(s)/hostname(s) for which to use workload information to increase the platform incident severity.


## RubrikCDMClusterConnectionState

**Type:** script  
**Product:** Rubrik Security Cloud  

Shows the Rubrik Polaris CDM Cluster Connection State


## RubrikPullDSPMViolationFileInformation

**Type:** script  
**Product:** Rubrik Security Cloud  

Syncs the DSPM violation information from RSC to platform

**Inputs:**

- `violation_id`: The ID of the DSPM Violation.Note: If not provided, the script will try to retrieve it from the incident context.
- `object_id`: The Object ID.Note: If not provided, the script will try to retrieve it from the incident context.
- `snapshot_id`: The Snapshot ID.Note: If not provided, the script will try to retrieve it from the incident context.
- `limit`: Number of results to retrieve in the response. The maximum allowed size is 1000.


## RubrikPullDSPMViolationInformation

**Type:** script  
**Product:** Rubrik Security Cloud  

Syncs the DSPM violation information from RSC to platform

**Inputs:**

- `violation_id`: The ID of the DSPM Violation.Note: If not provided, the script will try to retrieve it from the incident context.


## RubrikPullIRViolationInformation

**Type:** script  
**Product:** Rubrik Security Cloud  

Syncs the IR violation information from RSC to the platform

**Inputs:**

- `violation_id`: The ID of the IR Violation.Note: If not provided, the script will try to retrieve it from the incident context.
- `policy_type`: The policy type of the IR Violation.Note: If not provided, the script will try to retrieve it from the incident context.


## RubrikPullSensitiveDataObjectFileInformation

**Type:** script  
**Product:** Rubrik Security Cloud  

Syncs the sensitive data object file information from RSC to the platform

**Inputs:**

- `object_id`: The Object ID.Note: If not provided, the script will try to retrieve it from the incident context.
- `snapshot_id`: The Snapshot ID.Note: If not provided, the script will try to retrieve it from the incident context.
- `limit`: The number of results to retrieve in the response. The maximum allowed size is 1000.


## RubrikPushDSPMViolationStatus

**Type:** script  
**Product:** Rubrik Security Cloud  

Syncs the DSPM violation status from platform to RSC

**Inputs:**

- `violation_id`: The ID of the DSPM Violation.Note: If not provided, the script will try to retrieve it from the incident context.
- `violation_status`: The status to update for violation.Note: If not provided, the script will try to retrieve it from the incident context.


## RubrikPushIRViolationStatus

**Type:** script  
**Product:** Rubrik Security Cloud  

Syncs the IR violation status from the platform

**Inputs:**

- `violation_id`: The ID of the IR Violation.Note: If not provided, the script will try to retrieve it from the incident context.
- `violation_status`: The status to update for the violation.Note: If not provided, the script will try to retrieve it from the incident context.


## RubrikRadarFilesAdded

**Type:** script  
**Product:** Rubrik Security Cloud  

Shows the Rubrik Polaris Radar Files Added Count under the File Change attributes


## RubrikRadarFilesDeleted

**Type:** script  
**Product:** Rubrik Security Cloud  

Shows the Rubrik Polaris Radar Files Modified Count under the File Change attributes


## RubrikRadarFilesModified

**Type:** script  
**Product:** Rubrik Security Cloud  

Shows the Rubrik Polaris Radar Files Deleted Count under the File Change attributes


## RubrikSetIncidentSeverityUsingWorkLoadRiskLevel

**Type:** script  
**Product:** Rubrik Security Cloud  

Script used to set the platform incident severity using the workload data provided from the argument

**Inputs:**

- `risk_levels`: Specify the risk level values. Supports comma separated values.Supported values are: High, Medium, Low, No Risk.
- `anomaly_severities`: Specify the anomaly severity values. Supports comma separated values.Supported values are: Critical, Warning, Informational.
- `threat_hunt_malicious`: Specify the malicious threat hunt values. Supports comma separated values.Supported values are: Matches Found, No Matches Found.
- `threat_monitoring_malicious`: Specify the malicious threat monitoring values. Supports comma separated values.Supported values are: Matches Found, No Matches Found.
- `increase_severity_by`: Specify the level in number by which to increase the platform incident severity. Only applicable if match found for the malicious threat hun


## RubrikSonarFileHits

**Type:** script  
**Product:** Rubrik Security Cloud  

Shows the Rubrik Polaris Sonar File Hits Count


## RubrikSonarOpenAccessFileHits

**Type:** script  
**Product:** Rubrik Security Cloud  

Shows the Rubrik Polaris Sonar Open Access File Hits Count


## RubrikSonarOpenAccessFiles

**Type:** script  
**Product:** Rubrik Security Cloud  

Shows the Rubrik Polaris Sonar Open Access Files Count


## RubrikSonarSensitiveHits

**Type:** script  
**Product:** Rubrik Security Cloud  

Shows the Rubrik Polaris Sonar data classification results


## RubrikSonarSetIncidentSeverityUsingUserRiskLevel

**Type:** script  
**Product:** Rubrik Security Cloud  

Script used to set the incident severity using the risk level(s) provided from the argument

**Inputs:**

- `risk_levels`: The comma-separated list of risk levels.Supported values are: UNKNOWN_RISK, HIGH_RISK, MEDIUM_RISK, LOW_RISK, NO_RISK.


## RubrikSonarTotalHits

**Type:** script  
**Product:** Rubrik Security Cloud  

Shows the Rubrik Polaris Sonar data classification results


## RubrikSuspiciousFileCount

**Type:** script  
**Product:** Rubrik Security Cloud  

Shows the Rubrik Suspicious File Count


## SAP Cloud For Customer (C4C)

**Type:** integration  
**Product:** SAP Cloud For Customer C4C  

Use the SAP Cloud for Customer C4C integration to fetch events from SAP Cloud API

**Commands:**

- `sap-cloud-get-events`: 


## Saviynt Enterprise Identity Cloud

**Type:** integration  
**Product:** Saviynt Enterprise Identity Cloud  

Collector for Saviynt Enterprise Identity Cloud (EIC) audit logs using Analytics Runtime Control V2. This integration was tested with Saviynt EIC API Reference for Amsterdam GA Release (API v5)

**Commands:**

- `saviynt-eic-get-events`: 


## Spring Core and Cloud Function SpEL RCEs

**Type:** playbook  
**Product:** Spring Core and Cloud Function SpEL RCEs  

On March 29, 2022, information about a 0-day vulnerability in the popular Java library Spring Core appeared on Twitter. Spring Framework is an extremely popular framework used by Java developers to build modern applications. If you rely on the Java stack, it is very likely that your development teams use Spring. In some cases, a single specially crafted request is enough to exploit the vulnerability. Later, it was discovered that these are two separate vulnerabilities, one in Spring Core and the other in Spring Cloud Function: CVE-2022-22965 - RCE in "Spring Core" is a severe vulnerability, aka Spring4Shell CVE-2022-22963 - RCE in "Spring Cloud Function SpEL" CVE-2022-22947 - RCE in "Spring Cloud Gateway" Spring Core vulnerability requirements: Spring Cloud Function unaffected versions: This playbook will provide you with a first response kit which includes: Note: You can execute this playbook using the Incidents view by creating a new incident or by using a dedicated job to schedule the playbook execution. Additional resources: Spring Framework RCE CVE-2022-22965: Spring Core Remote Code Execution Vulnerability Exploited In the Wild

**Inputs:**

- `RelatedCVEs`: The vulnerability assigned CVE.
- `PlaybookDescription`: The playbook description. Will be used in the Rapid Breach Response - Set Incident Info sub-playbook.
- `AutoCloseIncident`: Whether to close the incident automatically or continue with manual investigation.
- `BlockIndicatorsAutomatically`: Whether to block the indicators automatically.
- `RunXQLHuntingQueries`: Whether to hunt using XQL queries.
- `XQLTimeFrame`: The XQL search time frame.Time in relative date or range format (for example: "1 day", "3 weeks ago", "between 2021-01-01 12:34:56 +02:00 an


## SpyCloud

**Type:** integration  
**Product:** SpyCloud  

With the SpyCloud integration, data from breaches can be pulled and further processed in Playbooks. Filtering parameters can be used to filter the data set This integration was integrated and tested with version 2 of SpyCloud

**Commands:**

- `spycloud-list-breaches`: 
- `spycloud-get-breach-data`: 
- `spycloud-domain-data`: 
- `spycloud-email-data`: 
- `spycloud-watchlist-data`: 


## SpyCloud Enterprise Protection Enrichment

**Type:** integration  
**Product:** SpyCloud Enterprise Protection  
**Commands:**

- `spycloud-breach-catalog-list`: 
- `spycloud-breach-catalog-get`: 
- `spycloud-domain-data-get`: 
- `spycloud-username-data-get`: 
- `spycloud-ip-address-data-get`: 
- `spycloud-email-data-get`: 
- `spycloud-password-data-get`: 
- `spycloud-watchlist-data-list`: 
- `spycloud-compass-device-data-get`: 
- `spycloud-compass-data-list`: 
- `spycloud-compass-device-list`: 
- `spycloud-compass-application-data-get`: 


## Sumo Logic Cloud SIEM

**Type:** integration  
**Product:** Sumo Logic Cloud SIEM  

Freeing the analyst with autonomous decisions. This integration was integrated and tested with version 6.1.0 of SumoLogicSEC

**Commands:**

- `sumologic-sec-insight-get-details`: 
- `sumologic-sec-insight-get-comments`: 
- `sumologic-sec-insight-get-comments`: 
- `sumologic-sec-signal-get-details`: 
- `sumologic-sec-entity-get-details`: 
- `sumologic-sec-insight-search`: 
- `sumologic-sec-signal-search`: 
- `sumologic-sec-entity-search`: 
- `sumologic-sec-insight-set-status`: 
- `sumologic-sec-match-list-get`: 
- `sumologic-sec-match-list-update`: 
- `sumologic-sec-threat-intel-search-indicators`: 
- `sumologic-sec-threat-intel-get-sources`: 
- `sumologic-sec-threat-intel-update-source`: 


## Sumo Logic Cloud SIEM - Link Signal Incidents

**Type:** playbook  
**Product:** Sumo Logic Cloud SIEM  

Playbook to link Sumo Logic Signal Incidents to the corresponding Insight Incident

**Inputs:**

- `Sumo Logic Insight`: The Sumo Logic Insight incident to which we will link its Signal incidents


## TagIndicatorButton

**Type:** script  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

This is a wrapper around the setIndicators script

**Inputs:**

- `Indicators`: The CSV list of indicators to tag.
- `Tags`: The tags to add to the indicators.


## Trellix Email Security - Cloud

**Type:** integration  
**Product:** Trellix Email Security - Cloud  
**Commands:**

- `fireeye-etp-search-messages`: 


## Trend Micro CAS - Take Action On Emails

**Type:** playbook  
**Product:** TrendAI™ Cloud App Security  

This playbook runs various actions on emails using TrendAI™ Cloud App Security, such as deleting and quarantine email messages, using the "trendmicro-cas-email-take-action" command and returns the results from the "trendmicro-cas-email-action-result-query" command

**Inputs:**

- `action_type`: The action to take on an email message, such as delete or quarantine. Can be: "MAIL_DELETE", or "MAIL_QUARANTINE".
- `mailbox`: The email address of an email message for which to take action.
- `mail_messge_id`: The Internet message ID of an email message for which to take action. To retrieve the ID use the "trendmicro-cas-email-sweep" command.
- `mail_unique_id`: The unique ID of an email message for which to take action. To retrieve the ID use the "trendmicro-cas-email-sweep" command.
- `mail_message_delivery_time`: The time and date when an email message is sent. To retrieve the information, use the "trendmicro-cas-email-sweep" command.
- `Interval`: 
- `Timeout`: 


## Trend Micro CAS - Take Action On User Accounts

**Type:** playbook  
**Product:** TrendAI™ Cloud App Security  

This playbook runs various actions on a user's account using TrendAI™ Cloud App Security, such as disabling accounts, requesting multi-factor authentication, and requesting a password, using the "trendmicro-cas-user-take-action" command and returns the result using the "trendmicro-cas-user-action-result-query" command

**Inputs:**

- `action_type`: Action to take on an email message. Options include:MAIL_DELETE: deletes an email messageMAIL_QUARANTINE: quarantines an email message
- `account_user_email`: The account user email for which to take action.
- `Interval`: 
- `Timeout`: 


## TrendAI™ Cloud App Security

**Type:** integration  
**Product:** TrendAI™ Cloud App Security  

Use TrendAI™ Cloud App Security integration to protect against ransomware, phishing, malware, and unauthorized transmission of sensitive data for cloud applications, such as Microsoft 365, Box, Dropbox, Google G Suite and Salesforce

**Commands:**

- `trendmicro-cas-security-events-list`: 
- `trendmicro-cas-email-sweep`: 
- `trendmicro-cas-user-take-action`: 
- `trendmicro-cas-email-take-action`: 
- `trendmicro-cas-user-action-result-query`: 
- `trendmicro-cas-email-action-result-query`: 
- `trendmicro-cas-blocked-lists-get`: 
- `trendmicro-cas-blocked-lists-update`: 


## URL Reputation - ReversingLabs TitaniumCloud

**Type:** playbook  
**Product:** ReversingLabs TitaniumCloud  

Get reputation data for the submitted URL. Required TitaniumCloud API rights: TCA-0403

**Inputs:**

- `URL`: URL to analyze


## WootCloud

**Type:** integration  
**Product:** WootCloud  
**Commands:**

- `wootcloud-get-pkt-alerts`: 


## XCloud Alert Enrichment

**Type:** playbook  
**Product:** Cloud Incident Response  

This playbook is responsible for data collection and enrichment. The playbook collects or enriches the following data

**Inputs:**

- `ResolveIP`: Determines whether to convert the IP address to a hostname using a DNS query (True/ False).
- `InternalRange`: A list of internal IP ranges to check IP addresses against. For IP Enrichment - Generic v2 playbook.


## XCloudAdditionalAlertInformationWidget

**Type:** script  
**Product:** Cloud Incident Response  

This script retrieves additional original alert information from the context


## XCloudIdentitiesWidget

**Type:** script  
**Product:** Cloud Incident Response  

This script retrieves the identity fields from the incident context


## XCloudProviderWidget

**Type:** script  
**Product:** Cloud Incident Response  

This script returns an HTML result of the cloud providers in the incident. The result will be displayed in the following font colors: AWS - red, GCP - green, Azure - blue


## XCloudRelatedAlertsWidget

**Type:** script  
**Product:** Cloud Incident Response  

This script retrieves additional original alert information from the context

