# Integration and Automation Catalog - Cloud Security

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## Amazon Web Services

**Type:** integration  
**Product:** AWS  

Support for AWS cloud This integration was integrated and tested with version 1.0.0 of AWS

**Commands:**

- `aws-s3-public-access-block-update`: Creates or modifies the PublicAccessBlock configuration for an Amazon S3 bucket. Required IAM permission: s3:PutBucketPublicAccessBlock.
- `aws-s3-bucket-delete`: Delete AWS S3 bucket, the bucket must be empty from files. Required IAM Permission: s3:DeleteBucket.
- `aws-s3-bucket-objects-list`: Returns some or all (up to 1,000) of the objects in a bucket. Required IAM Permission: s3:ListBucket.
- `aws-s3-bucket-objects-list-v2`: Lists objects in an Amazon S3 bucket (up to 1,000 objects) using the ListObjectsV2 API. Unlike aws-s3-bucket-objects-list, this command consistently returns a p
- `aws-s3-bucket-acl-put`: Sets the access control list (ACL) permissions for an existing Amazon S3 bucket. This command allows you to define who can access the bucket and what actions th
- `aws-s3-bucket-logging-put`: Configures logging settings for an AWS S3 bucket, enabling monitoring bucket access via logs delivered to a designated target bucket. Required IAM permission: s
- `aws-s3-bucket-versioning-put`: Sets the versioning state of an existing bucket. Required IAM permission: s3:PutBucketVersioning.
- `aws-s3-bucket-policy-put`: Applies an Amazon S3 bucket policy to an Outposts bucket. Required IAM permission: s3:PutBucketPolicy.
- `aws-s3-bucket-website-delete`: Removes the website configuration for a bucket. Required IAM permission: s3:DeleteBucketWebsite.
- `aws-s3-bucket-ownership-controls-put`: Creates or modifies ownership controls for an Amazon S3 bucket. Required IAM permission: s3:PutBucketOwnershipControls.
- `aws-s3-bucket-website-get`: Retrieves the website configuration for a bucket. Required IAM permission: s3:GetBucketWebsite.
- `aws-s3-bucket-acl-get`: Retrieves the access control list (ACL) of a bucket. Required IAM permission: s3:GetBucketAcl.
- `aws-iam-account-password-policy-get`: Retrieves the AWS account password policy. Required IAM permission: iam:GetAccountPasswordPolicy.
- `aws-iam-account-password-policy-update`: Creates or updates AWS account password policy. Required IAM permission: iam:UpdateAccountPasswordPolicy.
- `aws-iam-role-policy-put`: Adds or updates an inline policy document that is embedded in the specified IAM role. Required IAM permission: iam:PutRolePolicy.


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

- `ali-instance`: Create, Start, Stop, Restart or Terminate an Instance in ECS. Add or Remove Instance to/from a Security Group. Further documentation available at https://docs.a


## Ansible Azure

**Type:** integration  
**Product:** Ansible Azure  

This integration enables the management of Azure Services using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. To use this integration, configure an instance of this integration. This will associate a credential to be used to manage a Azure Subscription. To use this integration you must generate a Service Principal for your Azure subscription. Follow Microsoft's guide on how to create a Azure AD application and associated service principal. After stepping through the guide you will have

**Commands:**

- `azure-rm-autoscale`: Manage Azure autoscale setting Further documentation available at https://docs.ansible.com/ansible/2.9/modules/azure_rm_autoscale_module.html


## Ansible HCloud

**Type:** integration  
**Product:** Ansible Hetzner Cloud  

This integration enables the management of Hetzner Cloud environments using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. To use this integration you must generate an API token for your HCloud project. NOTE: If using 6.0.2 or lower version, put your API Token in the Password field, leave the Username field empty

**Commands:**

- `hcloud-datacenter-info`: Gather info about the Hetzner Cloud datacenters. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/hcloud_datacenter_info_module.h
- `hcloud-floating-ip-info`: Gather infos about the Hetzner Cloud Floating IPs. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/hcloud_floating_ip_info_modul
- `hcloud-image-info`: Gather infos about your Hetzner Cloud images. Further documentation available at https://docs.ansible.com/ansible/2.9/modules/hcloud_image_info_module.html


## Atlassian Cloud MCP

**Type:** integration  
**Product:** Atlassian Cloud MCP  

Use this integration to connect securely with an Atlassian Cloud Model Context Protocol (MCP) server and access its tools in real time

**Commands:**

- `atlassian-cloud-mcp-auth-test`: Test the authentication configuration with the MCP server.
- `atlassian-cloud-mcp-generate-login-url`: Generate an authentication login URL.


## Atlassian Confluence Cloud

**Type:** integration  
**Product:** Atlassian Confluence Cloud  

Atlassian Confluence Cloud allows users to interact with confluence entities like content, space, users and groups. Users can also manage the space permissions. This integration was integrated and tested with version 1000.0.0-847bdcbfcd00 of Atlassian Confluence Cloud

**Commands:**

- `confluence-cloud-space-create`: Creates a new space. Note: If no permissions are specified, the default space permissions defined by the Confluence cloud account admin will be used.
- `confluence-cloud-content-create`: Creates a page or blogpost for a given space. Note: To view the expansion of content properties, execute confluence-cloud-content-list and confluence-cloud-cont
- `confluence-cloud-comment-create`: Creates a comment for the given content. Note: To view the expansion of content properties, execute the confluence-cloud-content-list and confluence-cloud-conte
- `confluence-cloud-space-list`: Returns a list of all Confluence spaces.
- `confluence-cloud-content-list`: Returns the list of content of Confluence.
- `confluence-cloud-content-delete`: Delete the content depending on the content's type and status. Note: If the content's type is page or blogpost, it should be moved to trash before deleting perm
- `confluence-cloud-content-update`: Update the existing content with new content. Note: Updating draft content is currently not supported.
- `confluence-cloud-content-search`: Retrieves a list of content using the Confluence Query Language (CQL).
- `confluence-cloud-user-list`: Returns a list of users.
- `confluence-cloud-group-list`: Returns all user groups.
- `confluence-cloud-get-events`: Retrieves a list of events from the Atlassian Confluence Cloud instance.
- `confluence-cloud-content-get`: Retrieves a piece of content (e.g., page, blogpost) from Confluence Cloud by its ID.
- `confluence-cloud-oauth-start`: Starts the OAuth 2.0 authentication flow. Returns an authorization URL that the user must visit to authorize the integration.
- `confluence-cloud-oauth-complete`: Completes the OAuth 2.0 authentication flow by exchanging the authorization code for access and refresh tokens.
- `confluence-cloud-oauth-test`: Tests the OAuth 2.0 authentication by verifying the current access token is valid.


## AWS - AccessAnalyzer

**Type:** integration  
**Product:** AWS - AccessAnalyzer  

Amazon Web Services IAM Access Analyzer For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-access-analyzer-list-analyzers`: Retrieves a list of analyzers.
- `aws-access-analyzer-list-analyzed-resource`: Retrieves a list of resources that have been analyzed.
- `aws-access-analyzer-list-findings`: Retrieves a list of findings generated by the specified analyzer.
- `aws-access-analyzer-get-analyzed-resource`: Retrieves information about an analyzed resource.
- `aws-access-analyzer-get-finding`: Retrieves information about the specified finding.
- `aws-access-analyzer-start-resource-scan`: Starts a scan of the policies applied to the specified resource.
- `aws-access-analyzer-update-findings`: Updates findings with the new values provided in the request.


## AWS - ACM

**Type:** integration  
**Product:** AWS - ACM  

Amazon Web Services Certificate Manager Service (ACM) For more information regarding the AWS ACM service, please visit the official documentation found here. For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-acm-describe-certificate`: Returns detailed metadata about the specified ACM certificate.
- `aws-acm-list-certificates`: Retrieves a list of certificate ARNs and domain names. You can request that only certificates that match a specific status be listed. You can also filter by spe
- `aws-acm-add-tags-to-certificate`: Adds one or more tags to an ACM certificate.
- `aws-acm-remove-tags-from-certificate`: Remove one or more tags from an ACM certificate.
- `aws-acm-list-tags-for-certificate`: Lists the tags that have been applied to the ACM certificate. Use the certificate's Amazon Resource Name (ARN) to specify the certificate.
- `aws-acm-get-certificate`: Retrieves a certificate specified by an ARN and its certificate chain . The chain is an ordered list of certificates that contains the end entity certificate, i


## AWS - Athena

**Type:** integration  
**Product:** AWS - Athena  

Amazon Web Services Athena

**Commands:**

- `aws-athena-execute-query`: Execute a new query, wait for the query to complete (using polling), and return query's execution information, and query's results (if successful). Either 'Outp
- `aws-athena-start-query`: Start an Athena query. Either 'OutputLocation' or 'WorkGroup' must be specified for the query to run.
- `aws-athena-stop-query`: Stop an existing running query.
- `aws-athena-get-query-execution`: Return execution information of a query.
- `aws-athena-get-query-results`: Return the results of a query.


## AWS - CloudTrail

**Type:** integration  
**Product:** AWS - CloudTrail  

Amazon Web Services CloudTrail. This integration was integrated and tested with version 1.0.11 of AWS - CloudTrail

**Commands:**

- `aws-cloudtrail-create-trail`: Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket. A maximum of five trails can exist in a region, irrespective of the
- `aws-cloudtrail-delete-trail`: Deletes a trail. This operation must be called from the region in which the trail was created. DeleteTrail cannot be called on the shadow trails (replicated tra
- `aws-cloudtrail-describe-trails`: Retrieves settings for the trail associated with the current region for your account.
- `aws-cloudtrail-update-trail`: Updates the settings that specify delivery of log files. Changes to a trail do not require stopping the CloudTrail service.
- `aws-cloudtrail-start-logging`: Starts the recording of AWS API calls and log file delivery for a trail. For a trail that is enabled in all regions, this operation must be called from the regi
- `aws-cloudtrail-stop-logging`: Suspends the recording of AWS API calls and log file delivery for the specified trail. Under most circumstances, there is no need to use this action. You can up
- `aws-cloudtrail-lookup-events`: Looks up API activity events captured by CloudTrail that create, update, or delete resources in your account. Events for a region can be looked up for the times
- `aws-cloudtrail-get-trail-status`: Returns a JSON-formatted list of information about the specified trail. Fields include information on delivery errors, Amazon SNS and Amazon S3 errors, and star


## AWS - EC2

**Type:** integration  
**Product:** AWS - EC2  

Amazon Web Services Elastic Compute Cloud (EC2)

**Commands:**

- `aws-ec2-describe-instances`: Describes one or more of your instances.
- `aws-ec2-describe-iam-instance-profile-associations`: Describes your IAM instance profile associations.
- `aws-ec2-describe-images`: Describes one or more of the images (AMIs, AKIs, and ARIs) available to you. Images available to you include public images, private images that you own, and pri
- `aws-ec2-describe-regions`: Describes one or more regions that are currently available to you.
- `aws-ec2-describe-addresses`: Describes one or more of your Elastic IP addresses.
- `aws-ec2-describe-snapshots`: Describes one or more of the EBS snapshots available to you.
- `aws-ec2-describe-launch-templates`: Describes one or more launch templates.
- `aws-ec2-describe-key-pairs`: Describes one or more of your key pairs.
- `aws-ec2-describe-volumes`: !aws-ec2-describe-key-pairs
- `aws-ec2-describe-volumes`: Describes the specified EBS volumes.
- `aws-ec2-describe-vpcs`: Describes one or more of your VPCs.
- `aws-ec2-describe-subnets`: Describes one or more of your subnets.
- `aws-ec2-describe-security-groups`: Describes one or more of your security groups.
- `aws-ec2-allocate-address`: Allocates an Elastic IP address.
- `aws-ec2-associate-address`: Associates an Elastic IP address with an instance or a network interface.


## AWS - GuardDuty

**Type:** integration  
**Product:** AWS - GuardDuty  

Amazon Web Services Guard Duty Service (gd) Use this integration to detect and manage threats to your AWS system. We recommend that you use roles that have the following built-in AWS policies: For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-gd-create-detector`: Create an AWS Guard Duty Detector on the integration instance specified aws account.
- `aws-gd-delete-detector`: Deletes a Amazon GuardDuty detector specified by the detector ID.
- `aws-gd-get-detector`: Retrieves an Amazon GuardDuty detector specified by the detectorId.
- `aws-gd-update-detector`: Updates an Amazon GuardDuty detector specified by the detectorId.
- `aws-gd-create-ip-set`: A list of trusted IP addresses on allow list for secure communication with AWS infrastructure and applications.
- `aws-gd-delete-ip-set`: Deletes the IPSet specified by the IPSet ID.
- `aws-gd-list-detectors`: Lists detectorIds of all the existing Amazon GuardDuty detector resources.
- `aws-gd-update-ip-set`: Updates the IPSet specified by the IPSet ID.
- `aws-gd-get-ip-set`: Retrieves the IPSet specified by the IPSet ID.
- `aws-gd-list-ip-sets`: Lists the IPSets of the GuardDuty service specified by the detector ID.
- `aws-gd-create-threatintel-set`: Create a new ThreatIntelSet. ThreatIntelSets consist of known malicious IP addresses. GuardDuty generates findings based on ThreatIntelSets.
- `aws-gd-delete-threatintel-set`: Deletes ThreatIntelSet specified by the ThreatIntelSet ID.
- `aws-gd-get-threatintel-set`: Retrieves the ThreatIntelSet that is specified by the ThreatIntelSet ID.
- `aws-gd-list-threatintel-sets`: Lists the ThreatIntelSets of the GuardDuty service specified by the detector ID.
- `aws-gd-update-threatintel-set`: Updates the ThreatIntelSet specified by ThreatIntelSet ID.


## AWS - IAM (user lifecycle management)

**Type:** integration  
**Product:** AWS-ILM  

Integrate with AWS-ILM Identity Access Management service to execute CRUD (create, read, update, and delete) and group (create, get, update, and delete) operations for employee lifecycle processes. For more information, refer to the Identity Lifecycle Management article

**Commands:**

- `iam-create-user`: Creates a user.
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Disable an active user.
- `iam-get-group`: Retrieves a group
- `iam-create-group`: Creates an empty group
- `iam-update-group`: Updates an existing group resource. This command allows individual (or groups of) users to be added or removed from the group with a single operation. A maximum
- `iam-delete-group`: Permanently removes a group.


## AWS - IAM Identity Center

**Type:** integration  
**Product:** AWS - IAM Identity Center  

Amazon Web Services Identity and Access Management Identity Center(IAM) For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-iam-identitycenter-create-user`: Creates a new IAM Identity Center user for your AWS account.
- `aws-iam-identitycenter-get-user`: Retrieves information about the specified IAM user.
- `aws-iam-identitycenter-list-users`: Lists the IAM users, returns all users in the AWS account.
- `aws-iam-identitycenter-list-groups`: Lists all the IAM groups in the AWS account.
- `aws-iam-identitycenter-list-groups-for-user`: Lists the IAM Identity Center groups that the specified IAM user belongs to.
- `aws-iam-identitycenter-add-user-to-group`: Adds the specified user to the specified group.
- `aws-iam-identitycenter-get-group`: Get AWS IAM Identity Center group Information.
- `aws-iam-identitycenter-get-user-by-email`: Retrieves information about the specified IAM user.
- `aws-iam-identitycenter-list-memberships`: Lists the memberships of the group.
- `aws-iam-identitycenter-delete-user`: Removes the specified user from the AWS IAM Identity Center.
- `aws-iam-identitycenter-delete-group`: Removes the specified group from the IAM Identity Center.
- `aws-iam-identitycenter-create-group`: Creates a new IAM Identity Center group for your AWS account.
- `aws-iam-identitycenter-update-group`: Updates an IAM Identity Center group for your AWS account.
- `aws-iam-identitycenter-update-user`: Updates an IAM Identity Center user for your AWS account.
- `aws-iam-identitycenter-delete-group-membership`: Deletes a user from all groups if a username is provided, or deletes multiple memberships if a list of memberships is provided.


## AWS - Identity and Access Management

**Type:** integration  
**Product:** AWS - IAM  

Amazon Web Services Identity and Access Management (IAM) For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-iam-create-user`: Creates a new IAM user for your AWS account.
- `aws-iam-get-user`: Retrieves information about the specified IAM user, including the user's creation date, path, unique ID, and ARN.
- `aws-iam-list-users`: Lists the IAM users, returns all users in the AWS account.
- `aws-iam-update-user`: Updates the name and/or the path of the specified IAM user.
- `aws-iam-delete-user`: Deletes the specified IAM user. The user must not belong to any groups or have any access keys, signing certificates, or attached policies.
- `aws-iam-update-login-profile`: Changes the password for the specified IAM user.
- `aws-iam-create-group`: Creates a new iam group.
- `aws-iam-list-groups`: Lists all the IAM groups in the AWS account
- `aws-iam-list-groups-for-user`: Lists the IAM groups that the specified IAM user belongs to.
- `aws-iam-add-user-to-group`: Adds the specified user to the specified group.
- `aws-iam-create-access-key`: Creates a new AWS secret access key and corresponding AWS access key ID for the specified user. The default status for new keys is Active .
- `aws-iam-update-access-key`: Changes the status of the specified access key from Active to Inactive, or vice versa. This operation can be used to disable a user's key as part of a key rotat
- `aws-iam-list-access-keys-for-user`: Returns information about the access key IDs associated with the specified IAM user.
- `aws-iam-list-policies`: Lists all the managed policies that are available in your AWS account, including your own customer-defined managed policies and all AWS managed policies.
- `aws-iam-list-roles`: Lists all IAM roles


## AWS - Lambda

**Type:** integration  
**Product:** AWS - Lambda  

Amazon Web Services Serverless Compute service (lambda) This integration was integrated and tested with version 2015-03-31 of AWS - Lambda. For detailed instructions about setting up authentication, see: AWS Integrations - Authentication. Required AWS IAM Permissions and Roles for Lambda are documented here

**Commands:**

- `aws-lambda-get-function`: Returns the configuration information of the Lambda function and a presigned URL link to the .zip file you uploaded with CreateFunction so you can download the 
- `aws-lambda-list-functions`: Returns a list of your Lambda functions. For each function, the response includes the function configuration information. You must use GetFunction to retrieve t
- `aws-lambda-list-aliases`: Returns list of aliases created for a Lambda function. For each alias, the response includes information such as the alias ARN, description, alias name, and the
- `aws-lambda-invoke`: Invokes a Lambda function. Specify just a function name to invoke the latest version of the function. To invoke a published version, use the Qualifier parameter
- `aws-lambda-get-account-settings`: Retrieves details about your account's limits and usage in an AWS Region.
- `aws-lambda-get-policy`: Returns the resource-based IAM policy for a function, version, or alias.
- `aws-lambda-list-versions-by-function`: Returns a list of versions, with the version-specific configuration of each.
- `aws-lambda-get-function-url-config`: Returns details about a Lambda function URL.
- `aws-lambda-get-function-configuration`: Returns the version-specific settings of a Lambda function or version. The output includes only options that can vary between versions of a function.
- `aws-lambda-delete-function-url-config`: Deletes a Lambda function URL. When you delete a function URL, you can’t recover it. Creating a new function URL results in a different URL address.
- `aws-lambda-delete-function`: Deletes a Lambda function. To delete a specific function version, use the Qualifier parameter. Otherwise, all versions and aliases are deleted.
- `aws-lambda-create-function`: Creates a Lambda function. To create a function, you need a deployment package and an execution role.
- `aws-lambda-publish-layer-version`: Creates an Lambda layer from a ZIP archive.
- `aws-lambda-list-layer-version`: Lists the versions of an Lambda layer.
- `aws-lambda-delete-layer-version`: Deletes a version of an Lambda layer.


## AWS - Organizations

**Type:** integration  
**Product:** AWS Organizations  

Manage Amazon Web Services accounts and their resources. For AWS Organizations quotas, guidelines and restrictions, see the AWS Organizations Quotas page

**Commands:**

- `aws-org-root-list`: List the roots that are defined in the current organization.
- `aws-org-children-list`: List all of the organizational units (OUs) or accounts that are contained in the specified parent OU or root.
- `aws-org-parent-list`: Lists all of the organizational units (OUs) or accounts that are a parent OU or root of the specified child. This command returns only the immediate parents in 
- `aws-org-organization-unit-get`: Retrieve information about an organizational unit (OU). This command can be called only from the organization's management account or by a member account that i
- `aws-org-account-list`: Lists all the accounts in the organization or a specific account by ID.
- `aws-org-organization-get`: Retrieves information about the organization that the user's account belongs to.
- `aws-org-organization-unit-create`: Creates an organizational unit (OU) within a root or parent OU. An OU is a container for accounts that enables the organization of accounts to apply policies ac
- `aws-org-organization-unit-rename`: Renames the specified organizational unit (OU). The ID and ARN don’t change. The child OUs and accounts remain in place, and any attached policies of the OU rem
- `aws-org-organization-unit-delete`: Deletes an organizational unit (OU) from a root or another OU. All accounts and child OUs must first be removed.
- `aws-org-policy-list`: Retrieves the list of all policies in an organization of a specified type.
- `aws-org-policy-get`: Retrieves information about a policy.
- `aws-org-policy-attach`: Attaches a policy to a root, an organizational unit (OU), or an individual account.
- `aws-org-policy-target-list`: Lists all the roots, organizational units (OUs), and accounts that the specified policy is attached to.
- `aws-org-target-policy-list`: Lists the policies that are directly attached to the specified target root, organizational unit (OU), or account.
- `aws-org-policy-delete`: Deletes the specified policy from the organization. Before performing this operation, the policy must be detached from all organizational units (OUs), roots, an


## AWS - Route53

**Type:** integration  
**Product:** AWS - Route53  

Amazon Web Services Managed Cloud DNS Service

**Commands:**

- `aws-route53-create-record`: Creates a resource record set. Creates a resource record set that has the specified values.
- `aws-route53-delete-record`: Deletes a resource record set. Deletes an existing resource record set that has the specified values.
- `aws-route53-list-hosted-zones`: Retrieves a list of the public and private hosted zones that are associated with the current AWS account.
- `aws-route53-list-resource-record-sets`: Lists the resource record sets in a specified hosted zone.
- `aws-route53-waiter-resource-record-sets-changed`: A waiter function that waits until record set change is successful
- `aws-route53-test-dns-answer`: Gets the value that Amazon Route 53 returns in response to a DNS request for a specified record name and type. You can optionally specify the IP address of a DN
- `aws-route53-upsert-record`: Upsert a resource record set. If a resource record set does not already exist, AWS creates it. If a resource set does exist, Amazon Route 53 updates it with the


## AWS - S3

**Type:** integration  
**Product:** AWS - S3  

Amazon Web Services Simple Storage Service (S3). This integration was integrated and tested with API Version 2012-11-05. For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-s3-create-bucket`: Create AWS S3 bucket.
- `aws-s3-delete-bucket`: Delete AWS S3 bucket.
- `aws-s3-list-buckets`: List all S3 buckets in AWS account
- `aws-s3-get-bucket-policy`: Get AWS S3 Bucket Policy
- `aws-s3-delete-bucket-policy`: Deletes the policy from the bucket.
- `aws-s3-download-file`: Download a file from S3 bucket to war room.
- `aws-s3-list-bucket-objects`: List object in S3 bucket.
- `aws-s3-put-bucket-policy`: Replaces a policy on a bucket. If the bucket already has a policy, the one in this request completely replaces it.
- `aws-s3-upload-file`: Upload file to S3 bucket
- `aws-s3-get-public-access-block`: Retrieves the PublicAccessBlock configuration for an Amazon S3 bucket.
- `aws-s3-put-public-access-block`: Creates or modifies the PublicAccessBlock configuration for an Amazon S3 bucket.
- `aws-s3-get-bucket-encryption`: Get AWS S3 Bucket Encryption


## AWS - Security Hub

**Type:** integration  
**Product:** AWS - Security Hub  
**Commands:**

- `aws-securityhub-disable-security-hub`: Disables Security Hub in your account only in the current Region. To disable Security Hub in all Regions, you must submit one request per Region where you have 
- `aws-securityhub-batch-update-findings`: Used by Security Hub customers to update information about their investigation into a finding. Requested by master accounts or member accounts. Master accounts 
- `aws-securityhub-enable-security-hub`: Enables Security Hub for your account in the current Region or the Region you specify in the request. Enabling Security Hub also enables the CIS AWS Foundations
- `aws-securityhub-get-findings`: Returns a list of findings that match the specified criteria.
- `aws-securityhub-get-master-account`: Provides the details for the Security Hub master account to the current member account.
- `aws-securityhub-list-members`: Lists details about all member accounts for the current Security Hub master account.
- `get-remote-data`: Get remote data from a remote incident. This method does not update the current incident, and should be used for debugging purposes only.
- `get-mapping-fields`: Returns the list of fields to map in outgoing mirroring. This command is only used for debugging purposes.


## AWS - Security Hub v2

**Type:** integration  
**Product:** AWS - Security Hub  

Unified security and compliance findings management using the AWS Security Hub V2 API. This integration was integrated and tested with the AWS Security Hub V2 API

**Commands:**

- `aws-securityhub-v2-security-hub-enable`: Enables AWS Security Hub V2 for the configured account and region. Required IAM Permission: securityhub:EnableSecurityHubV2.
- `aws-securityhub-v2-security-hub-disable`: Disables AWS Security Hub V2 for the configured account and region. Required IAM Permission: securityhub:DisableSecurityHubV2.
- `aws-securityhub-v2-findings-get`: Retrieves a list of OCSF-formatted findings from AWS Security Hub V2. Required IAM Permission: securityhub:GetFindingsV2.
- `aws-securityhub-v2-findings-batch-update`: Updates one or more AWS Security Hub V2 findings in a single batch request. Findings are targeted by metadata_uids and/or finding_identifiers. Required IAM Perm
- `get-remote-data`: Returns the updated data of a single mirrored AWS Security Hub V2 finding. This command is used for mirroring and is not intended to be run manually.
- `get-mapping-fields`: Returns the list of fields available for outgoing mirroring. This command is used for mirroring and is not intended to be run manually.
- `update-remote-system`: Pushes local (the platform. This command is used for mirroring and is not intended to be run manually.


## AWS - SNS

**Type:** integration  
**Product:** AWS - SNS  

Amazon Web Services Simple Notification Service (SNS) For more information regarding the AWS SNS service, please visit the official documentation found here. For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-sns-create-subscription`: Subscribes an endpoint to an Amazon SNS topic. If the endpoint type is HTTP/S or email, or if the endpoint and the topic are not in the same Amazon Web Services
- `aws-sns-send-message`: Sends a message to an Amazon SNS topic, a text message (SMS message) directly to a phone number, or a message to a mobile platform endpoint (when you specify th
- `aws-sns-delete-topic`: Deletes a topic and all its subscriptions.


## AWS - SQS

**Type:** integration  
**Product:** AWS - SQS  

Amazon Web Services Simple Queuing Service (SQS) For more information regarding the AWS SQS service, please visit the official documentation found here. For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-sqs-get-queue-url`: Returns the URL of an existing queue. To access a queue that belongs to another AWS account, use the queueOwnerAWSAccountId parameter to specify the account ID 
- `aws-sqs-list-queues`: Returns a list of your queues. The maximum number of queues that can be returned is 1,000. If you specify a value for the optional QueueNamePrefix parameter, on
- `aws-sqs-send-message`: Delivers a message to the specified queue.
- `aws-sqs-create-queue`: Creates a new standard or FIFO queue. You can pass one or more attributes in the request.
- `aws-sqs-delete-queue`: Deletes the queue specified by the QueueUrl , regardless of the queue's contents. If the specified queue doesn't exist, Amazon SQS returns a successful response
- `aws-sqs-purge-queue`: Deletes the messages in a queue specified by the QueueURL parameter.


## AWS - System Manager

**Type:** integration  
**Product:** AWS Systems Manager  

AWS Systems Manager is the operations hub for your AWS applications and resources and a secure end-to-end management solution for hybrid cloud environments that enables safe and secure operations at scale. This integration was integrated and tested with Boto3 version 1.28.30 (AWS SDK). For detailed instructions about setting up authentication, see: AWS Integrations - Authentication

**Commands:**

- `aws-ssm-tag-add`: Adds or overwrites one tag for the specified resource. Tags are metadata that you can assign to the automations, documents, managed nodes, maintenance windows, 
- `aws-ssm-tag-remove`: Removes tag keys from the specified resource.
- `aws-ssm-tag-list`: Returns a list of the tags assigned to the specified resource.
- `aws-ssm-inventory-list`: Query inventory information. This includes the managed node status, such as Stopped or Terminated.
- `aws-ssm-inventory-entry-list`: A list of inventory items returned by the request.
- `aws-ssm-association-list`: Returns all State Manager associations in the current Amazon Web Services account and Amazon Web Services Region. Note: An association is a binding between a do
- `aws-ssm-association-get`: Describes the association for the specified target or managed node. If the association was established using the Targets parameter, the association details must
- `aws-ssm-association-version-list`: Retrieves all versions of an association for a specific association ID.
- `aws-ssm-document-list`: Returns all Systems Manager (SSM) documents in the current Amazon Web Services account and Amazon Web Services Region.
- `aws-ssm-document-get`: Describes the specified Amazon Web Services Systems Manager document (SSM document).
- `aws-ssm-automation-execution-run`: Initiates execution of an Automation runbook.
- `aws-ssm-automation-execution-cancel`: Stop an Automation execution.
- `aws-ssm-automation-execution-list`: If the argument execution_id is provided, the command returns detailed information about a particular Automation execution. if not provided, the command provide
- `aws-ssm-command-list`: Lists the commands requested by users of the Amazon Web Services account.
- `aws-ssm-command-run`: Runs commands on one or more managed nodes.


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

- `aws-network-firewall-associate-firewall-policy`: Associates a FirewallPolicy to a Firewall. A firewall policy defines how to monitor and manage your VPC network traffic, using a collection of inspection rule g
- `aws-network-firewall-associate-subnets`: Associates the specified subnets in the Amazon VPC to the firewall. You can specify one subnet for each of the Availability Zones that the VPC spans. This reque
- `aws-network-firewall-create-firewall`: Creates an AWS Network Firewall Firewall and accompanying FirewallStatus for a VPC. The firewall defines the configuration settings for an AWS Network Firewall 
- `aws-network-firewall-create-firewall-policy`: Creates the firewall policy for the firewall according to the specifications. An AWS Network Firewall firewall policy defines the behavior of a firewall, in a c
- `aws-network-firewall-create-rule-group`: Creates the specified stateless or stateful rule group, which includes the rules for network traffic inspection, a capacity setting, and tags. You provide your 
- `aws-network-firewall-delete-firewall`: Deletes the specified Firewall and its FirewallStatus. This operation requires the firewall's DeleteProtection flag to be FALSE. You can't revert this operation
- `aws-network-firewall-delete-firewall-policy`: Deletes the specified FirewallPolicy.
- `aws-network-firewall-delete-resource-policy`: Deletes a resource policy that you created in a PutResourcePolicy request.
- `aws-network-firewall-delete-rule-group`: Deletes the specified RuleGroup.
- `aws-network-firewall-describe-firewall`: Returns the data objects for the specified firewall.
- `aws-network-firewall-describe-firewall-policy`: Returns the data objects for the specified firewall policy.
- `aws-network-firewall-describe-logging-configuration`: Returns the logging configuration for the specified firewall.
- `aws-network-firewall-describe-resource-policy`: Retrieves a resource policy that you created in a PutResourcePolicy request.
- `aws-network-firewall-describe-rule-group`: Returns the data objects for the specified rule group.
- `aws-network-firewall-disassociate-subnets`: Removes the specified subnet associations from the firewall. This removes the firewall endpoints from the subnets and removes any network filtering protections 


## AWS Sagemaker

**Type:** integration  
**Product:** AWS Sagemaker  

AWS Sagemaker - the platform

**Commands:**

- `predict-phishing`: Classify input text (usually email content)


## Aws Secrets Manager

**Type:** integration  
**Product:** AWS Secrets Manager  

AWS Secrets Manager helps you to securely encrypt, store, and retrieve credentials for your databases and other services. This integration was integrated and tested with version 1.0 of AwsSecretsManager

**Commands:**

- `aws-secrets-manager-secret-list`: Retrieve all secrets.
- `aws-secrets-manager-secret–value-get`: Retrieve a secret value by key.
- `aws-secrets-manager-secret–delete`: Delete a specific secret.
- `aws-secrets-manager-secret–restore`: Restore a specific secret after deletion.
- `aws-secrets-manager-secret–policy-get`: Get the Secret Manager policy for a specific secret.


## AWS-EKS

**Type:** integration  
**Product:** AWS - EKS  

The AWS EKS integration allows for the management and operation of Amazon Elastic Kubernetes Service (EKS) clusters. This integration was integrated and tested with version 1.29 of AWS-EKS

**Commands:**

- `aws-eks-list-clusters`: Lists the Amazon EKS clusters in your Amazon Web Services account in the specified Amazon Web Services Region.
- `aws-eks-update-cluster-config`: Updates an Amazon EKS cluster configuration. Only one type of update is allowed. Potentially harmful: once the authentication mode is updated to 'API' it is irr
- `aws-eks-describe-cluster`: Describes an Amazon EKS cluster.
- `aws-eks-create-access-entry`: Creates an access entry.
- `aws-eks-associate-access-policy`: Associates an access policy and its scope to an access entry.
- `aws-eks-update-access-entry`: Updates an access entry.


## AWS-WAF

**Type:** integration  
**Product:** AWS WAF  

Amazon Web Services Web Application Firewall (WAF)

**Commands:**

- `aws-waf-ip-set-create`: Create a new IP set.
- `aws-waf-ip-set-get`: Get a specific IP set.
- `aws-waf-ip-set-update`: Update an IP set.
- `aws-waf-ip-set-list`: Lists IP sets.
- `aws-waf-ip-set-delete`: Delete a specific IP set.
- `aws-waf-regex-set-create`: Create a new regex set.
- `aws-waf-regex-set-get`: Get a specific regex set.
- `aws-waf-regex-set-update`: Update a regex set.
- `aws-waf-regex-set-list`: Lists regex sets.
- `aws-waf-regex-set-delete`: Delete a specific regex set.
- `aws-waf-rule-group-list`: Lists rule groups.
- `aws-waf-rule-group-get`: Get a specific rule group.
- `aws-waf-rule-group-delete`: Delete a specific rule group.
- `aws-waf-rule-group-create`: Create a new rule group.
- `aws-waf-ip-rule-create`: Create an IP rule.


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

- `azure-nsg-security-rule-update`: Update a security rule. If one does not exist, it will be created. The command is deprecated, please use azure-vn-security-rule-update. Required Permissions: Mi
- `azure-storage-accounts-list`: Lists storage accounts, or retrieves a single storage account when an account name is provided. Required permission: Microsoft.Storage/storageAccounts/read.
- `azure-storage-blob-containers-list`: Lists blob containers, or retrieves a single blob container when a container name is provided. Required permission: Microsoft.Storage/storageAccounts/blobServic
- `azure-storage-account-update`: Updates a specific account storage. Required permissions: Microsoft.Storage/storageAccounts/read, Microsoft.Storage/storageAccounts/write.
- `azure-storage-blob-service-properties-set`: Sets properties for the blob service in a specific account storage. The command is deprecated, please use azure-storage-blob-service-property-set. Required Perm
- `azure-policy-assignment-create`: Creates a policy assignment. Required permissions: Microsoft.Authorization/policyAssignments/read, Microsoft.Authorization/policyAssignments/write.
- `azure-postgres-config-set`: Updates a configuration of a server. The command is deprecated due to the retirement of Azure PostgreSQL Single Server.
- `azure-webapp-config-set`: Updates the configuration settings of an existing Azure Web App. The command is deprecated, please use azure-appservice-webapp-config-update. Required Permissio
- `azure-webapp-auth-update`: Updates the authentication and authorization settings of an existing Azure Web App. The command is deprecated, please use azure-appservice-webapp-auth-settings-
- `azure-mysql-flexible-server-param-set`: Updates a server configuration. Required permissions: Microsoft.DBforMySQL/flexibleServers/configurations/read, Microsoft.DBforMySQL/flexibleServers/configurati
- `azure-monitor-log-profile-update`: Updates a log profile in Azure Monitoring REST API. Required permissions: Microsoft.Insights/logprofiles/read, Microsoft.Insights/logprofiles/write.
- `azure-disk-update`: Updates a disk. The command is deprecated, please use azure-compute-disk-update. Required Permissions: Microsoft.Compute/disks/read, Microsoft.Compute/disks/wri
- `azure-webapp-update`: Updates an Azure Web App. The command is deprecated, please use azure-appservice-webapp-update. Required Permissions: Microsoft.Web/sites/read, Microsoft.Web/si
- `azure-acr-update`: Updates a container registry. The command is deprecated, please use azure-cr-registry-update. Required Permissions: Microsoft.ContainerRegistry/registries/read,
- `azure-postgres-server-update`: Updates an existing server. The command is deprecated due to the retirement of Azure PostgreSQL Single Server.


## Azure Compute v2

**Type:** integration  
**Product:** Azure Compute  

You can use this integration to create and manage Azure Virtual Machines. This integration was integrated and tested with Azure Compute API Version: 2017-12-01

**Commands:**

- `azure-vm-list-instances`: Lists the virtual machine instances in the given resource group.
- `azure-vm-start-instance`: Powers on a given virtual machine.
- `azure-vm-poweroff-instance`: Powers off a given virtual machine.
- `azure-vm-get-instance-details`: Gets the properties of a given virtual machine.
- `azure-vm-create-instance`: Creates a virtual machine instance with the specified OS image.
- `azure-list-resource-groups`: Lists all resource groups that belong to your Azure subscription.
- `azure-vm-delete-instance`: Deletes a specified virtual machine.
- `azure-list-subscriptions`: Lists the subscriptions for this application.
- `azure-vm-get-nic-details`: Gets the properties of a given network interface.
- `azure-vm-get-public-ip-details`: Gets the properties of a given public IP address.
- `azure-vm-get-all-public-ip-details`: Gets the properties of all public ip address in a subscription.
- `azure-vm-create-nic`: Creates a virtual machine network interface.
- `azure-vm-auth-reset`: Run this command if for some reason you need to rerun the authentication process.


## Azure Data Explorer

**Type:** integration  
**Product:** Azure Data Explorer  

Use the Azure Data Explorer integration to collect and analyze data inside Azure Data Explorer clusters, and to manage search queries. This integration was integrated and tested with version V1 of AzureDataExplorer. In order to connect to the Azure Data Explorer using either the platform, use one of the following methods

**Commands:**

- `azure-data-explorer-search-query-execute`: Execute a Kusto Query Language (KQL) query against the given database inside a cluster. The Kusto query is a read-only request to process data and return result
- `azure-data-explorer-search-query-list`: List search queries that have reached a final state in the given database. A database admin or database monitor can see any command that was invoked on their da
- `azure-data-explorer-running-search-query-list`: List currently executing search queries in the given database. A database admin or database monitor can see any search query that was invoked on their database.
- `azure-data-explorer-running-search-query-cancel`: Starts a best-effort attempt to cancel a specific running search query in the specified database.
- `azure-data-explorer-auth-start`: Run this command to start the authorization process and follow the instructions in the command results.
- `azure-data-explorer-auth-complete`: Run this command to complete the authorization process. This should be used after running the azure-data-explorer-auth-start command.
- `azure-data-explorer-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `azure-data-explorer-auth-test`: Run this command to test the connectivity to Azure Data Explorer.
- `azure-data-explorer-generate-login-url`: Generate the login url used for Authorization code flow.


## Azure Firewall

**Type:** integration  
**Product:** Azure Firewall  

Azure Firewall is a cloud-native and intelligent network firewall security service that provides breed threat protection for cloud workloads running in Azure. It's a fully stateful, firewall as a service, with built-in high availability and unrestricted cloud scalability. This integration was integrated and tested with version 2021-03-01 of Azure Firewall

**Commands:**

- `azure-firewall-auth-test`: Tests the connectivity to Azure.
- `azure-firewall-auth-start`: Run this command to start the authorization process and follow the instructions in the command results.
- `azure-firewall-auth-complete`: Run this command to complete the authorization process. Should be used after running the azure-firewall-auth-start command.
- `azure-firewall-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `azure-firewall-list`: List Azure firewalls in the specified resource group or subscription.
- `azure-firewall-get`: Retrieve Azure firewall information.
- `azure-firewall-rule-collection-list`: List the collection rules in the firewall or policy. One of the arguments 'firewall_name' or 'policy' must be provided.
- `azure-firewall-rule-list`: List rules in the firewall or in the policy. One of the arguments 'firewall_name' or 'policy' must be provided.
- `azure-firewall-rule-get`: Retrieve rule information. One of the arguments 'firewall_name' or 'policy' must be provided.
- `azure-firewall-policy-create`: Create a firewall policy. This command only creates the policy resource. In order to attach the policy to a firewall, run the 'azure-firewall-policy-attach' com
- `azure-firewall-policy-update`: Update the policy resource. The command will update the provided arguments.
- `azure-firewall-policy-get`: Retrieve policy information.
- `azure-firewall-policy-delete`: Delete policy resource.
- `azure-firewall-policy-list`: List the policy in the resource group or subscription.
- `azure-firewall-policy-attach`: Attach a policy to a firewall. The policy and firewall have to belong to the same tier.


## Azure Key Vault

**Type:** integration  
**Product:** Azure Key Vault  

Use the Azure Key Vault integration to safeguard and manage cryptographic keys and secrets used by cloud applications and services. This integration was integrated and tested with version 2022-07-01 of AzureKeyVault

**Commands:**

- `azure-key-vault-create-update`: Create or update a key vault in the specified subscription. If the Key Vault exists, the updated properties will overwrite the existing ones. Please use azure-k
- `azure-key-vault-delete`: Delete the specified key vault.
- `azure-key-vault-get`: Get the specified key vault.
- `azure-key-vault-list`: The List operation gets information about the vaults associated with the subscription. For a limit greater than 25, more than one API call will be required and 
- `azure-key-vault-access-policy-update`: Update access policies in a key vault in the specified subscription. The update regards only the access policy for the specified object ID.
- `azure-key-vault-key-get`: Get the public part of a stored key. This operation requires the keys/get permission.
- `azure-key-vault-key-list`: List keys in the specified vault. For a limit greater than 25, more than one API call will be required and the command might take longer time. This operation re
- `azure-key-vault-key-delete`: Delete a key of any type from storage in Azure Key vault. This operation requires the keys/delete permission.
- `azure-key-vault-secret-get`: Get a specified secret from a given key vault. The GET operation is applicable to any secret stored in Azure Key Vault. This operation requires the secrets/get 
- `azure-key-vault-secret-list`: List secrets in a specified key vault. For a limit greater than 25, more than one API call will be required and the command might take longer time. This operati
- `azure-key-vault-secret-delete`: Delete a secret from a specified key vault. This operation requires the secrets/delete permission.
- `azure-key-vault-certificate-get`: Gets information about a specific certificate. This operation requires the certificates/get permission.
- `azure-key-vault-certificate-list`: List certificates in a specified key vault. For a limit greater than 25, more than one API call will be required and the command might take longer time. This op
- `azure-key-vault-certificate-policy-get`: Get the policy of the specified certificate.This operation requires the certificates/get permission.
- `azure-key-vault-subscriptions-list`: List all subscriptions for a tenant.


## Azure Kubernetes Services

**Type:** integration  
**Product:** Azure Kubernetes Services  

Deploy and manage containerized applications with a fully managed Kubernetes service. This integration was integrated and tested with API version 2023-02-01 of AKS. In order to connect to the AzureKubernetesServices using either the platform, use one of the following methods: To use a self-configured Azure application, you need to add a new Azure App Registration in the Azure Portal. In case you want to use Device code flow, you must allow public client flows (can be found under the Authentication section of the app). Follow these steps for a self-deployed configuration: Follow these steps for a self-deployed configuration: At end of the process you'll see a message that you've logged in successfully. In order to use the the platform, use the default application ID (ab217a43-e09b-4f80-ae93-482fc7a3d1a3)

**Commands:**

- `azure-ks-auth-test`: Tests the connectivity to Azure.
- `azure-ks-auth-start`: Run this command to start the authorization process and follow the instructions in the command results.
- `azure-ks-auth-complete`: Run this command to complete the authorization process. Should be used after running the azure-ks-auth-start command.
- `azure-ks-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `azure-ks-clusters-list`: Gets a list of managed clusters in the specified subscription.
- `azure-ks-cluster-addon-update`: Updates a managed cluster with the specified configuration.
- `azure-ks-generate-login-url`: Generate the login url used for Authorization code flow.
- `azure-ks-resource-group-list`: Gets all resource groups for a subscription.
- `azure-ks-subscriptions-list`: Gets all subscriptions for a tenant.


## Azure Log Analytics

**Type:** integration  
**Product:** Azure Log Analytics  

Log Analytics is a service that helps you collect and analyze data generated by resources in your cloud and on-premises environments. This integration was integrated and tested with version 2022-10-01 of Azure Log Analytics. In order to connect to the Azure Log Analytics use either the the platform. Depending on the authentication method that you use, the integration parameters might change. Note: The Azure account must have permission to manage applications in Entra ID (Azure AD). Any of the following Entra ID roles include the required permissions: In addition, the user that granted the authorization needs to be assigned the Log Analytics Reader role. For the search job commands the user needs to be assigned the Log Analytics Contributor role. For more information, refer to the following Microsoft article

**Commands:**

- `azure-log-analytics-execute-query`: Executes an Analytics query for data.


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

- `azure-nsg-security-groups-list`: List all network security groups.
- `azure-nsg-security-rules-list`: List all rules of the specified security groups.
- `azure-nsg-auth-test`: Tests the connectivity to the Azure Network Security Groups.
- `azure-nsg-auth-start`: Run this command to start the authorization process and follow the instructions in the command results.
- `azure-nsg-auth-complete`: Run this command to complete the authorization process. Should be used after running the azure-nsg-auth-start command.
- `azure-nsg-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `azure-nsg-security-rule-delete`: Delete a security rule.
- `azure-nsg-security-rule-create`: Create a security rule.
- `azure-nsg-security-rule-update`: Update a security rule. If one does not exist, it will be created.
- `azure-nsg-security-rule-get`: Get a specific rule.
- `azure-nsg-generate-login-url`: Generate the login url used for Authorization code.
- `azure-nsg-subscriptions-list`: Gets all subscriptions for a tenant.
- `azure-nsg-resource-group-list`: Gets all resource groups for a subscription.
- `azure-nsg-network-interfaces-create`: Creates or updates a network interface.
- `azure-nsg-virtual-networks-list`: Gets virtual networks in a resource group.


## Azure Open AI Service

**Type:** integration  
**Product:** Azure Open AI Service  

Azure Open AI ServiceAI

**Commands:**

- `azure-openai-send-message`: Send message to Azure Open AI


## Azure Resource Graph

**Type:** integration  
**Product:** Azure Resource Graph  

Azure Resource Graph is an Azure service designed to extend Azure Resource Management by providing efficient and performant resource exploration with the ability to query at scale across a given set of resources

**Commands:**

- `azure-rg-list-operations`: 
- `azure-rg-query`: 
- `azure-rg-auth-reset`: Run this command if for some reason you need to rerun the authentication process.


## Azure Risky Users

**Type:** integration  
**Product:** Azure Risky Users  

Azure Risky Users provides access to all at-risk users and risk detections in Azure AD environment. This integration was integrated and tested with version 1.0 of Microsoft Graph Azure Risky Users. To use a self-configured Azure application, you need to add a new Azure App Registration in the Azure Portal. The application must have the following permissions: In case you want to use Device code flow, you must allow public client flows (can be found under the Authentication section of the app)

**Commands:**

- `azure-risky-users-auth-test`: Tests the connectivity to Azure.
- `azure-risky-users-auth-start`: Run this command to start the authorization process and follow the instructions in the command results.
- `azure-risky-users-auth-complete`: Run this command to complete the authorization process. Should be used after running the azure-risky-users-auth-start command.
- `azure-risky-users-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `azure-risky-users-list`: Returns a list of all risky users and their properties.
- `azure-risky-user-get`: Retrieve properties and relationships of a Risky User.
- `azure-risky-users-risk-detections-list`: Get a list of the riskDetection objects and their properties.
- `azure-risky-users-risk-detection-get`: Read the properties and relationships of a riskDetection object.
- `azure-risky-users-confirm-safe`: Confirms user(s) as safe (post-investigation).
- `azure-risky-users-confirm-compromise`: Confirms user(s) as compromised.


## Azure SQL Management

**Type:** integration  
**Product:** Azure SQL Management  

Microsoft Azure SQL Management Integration manages the Auditing and Threat Policies for Azure SQL. This integration was integrated and tested with version 2021-11-01 of Azure SQL Management In order to connect to the AzureKubernetesServices using either the platform, use one of the following methods: To use a self-configured Azure application, you need to add a new Azure App Registration in the Azure Portal. The application must have user_impersonation permission and must allow public client flows (found under the Authentication section of the app). And must allow public client flows (found under the Authentication section of the app) for Device-code based authentications

**Commands:**

- `azure-sql-auth-start`: Run this command to start the authorization process and follow the instructions in the command results.
- `azure-sql-auth-complete`: Run this command to complete the authorization process. Should be used after running the azure-sql-auth-start command.
- `azure-sql-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `azure-sql-auth-test`: Tests the connectivity to the Azure SQL Management.
- `azure-sql-servers-list`: Lists all the servers.
- `azure-sql-db-list`: Lists all of the databases for the server.
- `azure-sql-db-audit-policy-list`: Gets the audit settings of the specified database.
- `azure-sql-db-threat-policy-get`: Gets the threat detection policy of the specified database.
- `azure-sql-db-audit-policy-create-update`: Creates or updates the database's auditing policy.
- `azure-sql-db-threat-policy-create-update`: Creates or updates the database's threat detection policy.
- `azure-sql-generate-login-url`: Generate the login url used for Authorization code flow.
- `azure-sql-subscriptions-list`: Gets all subscriptions for a tenant.
- `azure-sql-resource-group-list`: Gets all the resource groups for a subscription.
- `azure-sql-firewall-rule-list`: Retrieves a list of firewall rules or a specific firewall rule. Required Permissions: Microsoft.Sql/servers/firewallRules/read.
- `azure-sql-firewall-rule-create-update`: Creates or updates a firewall rule. Required Permissions: Microsoft.Sql/servers/firewallRules/write.


## Azure Storage Container

**Type:** integration  
**Product:** Azure Storage Container  

Create and Manage Azure Storage Container services. This integration was integrated and tested with version "2020-10-02" of Azure Storage Container

**Commands:**

- `azure-storage-container-list`: List Containers under the specified storage account.
- `azure-storage-container-create`: Create a new Container under the specified account.
- `azure-storage-container-property-get`: Retrieve properties for the specified Container.
- `azure-storage-container-delete`: Marks the specified Container for deletion. The Container and any Blobs contained within it, will be deleted during garbage collection.
- `azure-storage-container-blob-list`: List Blobs under the specified container.
- `azure-storage-container-blob-create`: Create a new Blob under the specified Container.
- `azure-storage-container-blob-update`: Update the content of an existing Blob.
- `azure-storage-container-blob-get`: Retrieve Blob from Container.
- `azure-storage-container-blob-tag-get`: Retrieve the tags of the specified Blob.
- `azure-storage-container-blob-tag-set`: Sets the tags for the specified Blob. The command replace the entire tags of the Blob and can be used to remove tags.
- `azure-storage-container-blob-delete`: Marks the specified Blob for deletion. The Blob will be deleted during garbage collection.
- `azure-storage-container-blob-property-get`: Retrieve Blob properties.
- `azure-storage-container-blob-property-set`: Set Blob properties.
- `azure-storage-container-sas-create`: Retrieve Blob properties.
- `azure-storage-container-block-public-access`: Block public access to a container..


## Azure Storage FileShare

**Type:** integration  
**Product:** Azure Storage FileShare  

Create and Manage Azure FileShare Files and Directories. This integration was integrated and tested with version "2020-10-02" of Azure Storage FileShare

**Commands:**

- `azure-storage-fileshare-create`: Create a new Azure file share under the specified account.
- `azure-storage-fileshare-delete`: Delete file share under the specified account.
- `azure-storage-fileshare-list`: list Azure file shares under the specified account.
- `azure-storage-fileshare-content-list`: List files and directories under the specified share or directory.
- `azure-storage-fileshare-directory-create`: Create a new directory under the specified share or parent directory.
- `azure-storage-fileshare-directory-delete`: Delete the specified empty directory. Note that the directory must be empty before it can be deleted.
- `azure-storage-fileshare-file-create`: Creates a new file in Share.
- `azure-storage-fileshare-file-get`: Retrieve file from Share.
- `azure-storage-fileshare-file-delete`: Delete file from Share.


## Azure Storage Management

**Type:** integration  
**Product:** Azure Storage Management  

This integration enables you to deploy and manage storage accounts and blob services. This integration was integrated and tested with version 2022-09-01 of Azure Storage In order to connect to the Azure Storage Accounts and the Blob Service use either the the platform. Use one of the following methods

**Commands:**

- `azure-storage-auth-test`: Tests the connectivity to Azure.
- `azure-storage-auth-start`: Run this command to start the authorization process and follow the instructions in the command results.
- `azure-storage-auth-complete`: Run this command to complete the authorization process. Should be used after running the azure-storage-auth-start command.
- `azure-storage-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `azure-storage-account-list`: Run this command to get the all or specific account storage details.
- `azure-storage-account-create-update`: Run this command to create or update a specific account storage.
- `azure-storage-blob-service-properties-get`: Run this command to get the blob service properties of a specific account storage.
- `azure-storage-blob-service-properties-set`: Run this command to set properties for the blob service in a specific account storage
- `azure-storage-blob-containers-create`: Run this command to create a blob container.
- `azure-storage-blob-containers-update`: Run this command to update a specific blob container.
- `azure-storage-blob-containers-list`: Run this command to get the all or specific blob container details.
- `azure-storage-blob-container-delete`: Run this command to delete a specific blob container.
- `azure-storage-generate-login-url`: Generate the login url used for Authorization code flow.
- `azure-storage-subscriptions-list`: Gets all subscriptions for a tenant.
- `azure-storage-resource-group-list`: Gets all resource groups for a subscription.


## Azure Storage Queue

**Type:** integration  
**Product:** Azure Storage Queue  

Create and Manage Azure Storage Queues and Messages. This integration was integrated and tested with version "2020-10-02" of Azure Storage Queue

**Commands:**

- `azure-storage-queue-list`: List queues in storage account.
- `azure-storage-queue-create`: Create new queue in storage account.
- `azure-storage-queue-delete`: Delete queue from storage account.
- `azure-storage-queue-message-create`: Add a new message to the back of the queue.
- `azure-storage-queue-message-get`: Retrieves messages from the front of the queue. Retrieved messages will move to the end of the queue,and will be visible after 'TimeNextVisible' param.
- `azure-storage-queue-message-peek`: Retrieves messages from the front of the queue. The command does not alter the visibility of the message.
- `azure-storage-queue-message-dequeue`: Dequeue a message from the front of the queue.
- `azure-storage-queue-message-update`: Update message content in the queue.
- `azure-storage-queue-message-delete`: Delete message from a Queue.
- `azure-storage-queue-message-clear`: Delete all messages from the specified Queue.


## Azure Storage Table

**Type:** integration  
**Product:** Azure Storage Table  

Create and Manage Azure Storage Tables and Entities. This integration was integrated and tested with version "2020-10-02" of Azure Storage Table

**Commands:**

- `azure-storage-table-create`: Creates a new table in a storage account.
- `azure-storage-table-delete`: Delete the specified table and any data it contains.
- `azure-storage-table-query`: List tables under the specified account.
- `azure-storage-table-entity-insert`: Insert a new entity into a table.
- `azure-storage-table-entity-update`: Update an existing entity in a table. The Update Entity command does not replace the existing entity.
- `azure-storage-table-entity-replace`: Replace an existing entity in a table. The Replace Entity command replace the entire entity and can be used to remove properties.
- `azure-storage-table-entity-query`: Query Entities in a table.
- `azure-storage-table-entity-delete`: Delete an existing entity in a table.


## Azure Web Application Firewall

**Type:** integration  
**Product:** Azure WAF  

The Azure WAF (Web Application Firewall) integration provides centralized protection of your web applications from common exploits and vulnerabilities. It enables you to control policies that are configured in the Azure Firewall management platform, and allows you to add, delete, or update policies, and also to get details of a specific policy or a list of policies. In order to connect to the AzureWAF using either the platform, use one of the following methods

**Commands:**

- `azure-waf-policies-get`: Retrieves protection policies within a resource group.
- `azure-waf-policies-list-all-in-subscription`: Retrieves all the WAF policies in a subscription.
- `azure-waf-policy-update-or-create`: Creates or updates a policy with a specified rule set name within a resource group.
- `azure-waf-policy-delete`: Deletes a policy.
- `azure-waf-front-door-policies-list`: Lists all of the Front Door protection policies within a resource group.
- `azure-waf-front-door-policies-list-all-in-subscription`: Lists all of the Front Door protection policies within a subscription.
- `azure-waf-front-door-policy-update-or-create`: Creates or updates a Front Door policy with a specified rule set name within a resource group.
- `azure-waf-front-door-policy-delete`: Deletes a Front Door policy.
- `azure-waf-auth-start`: Run this command to start the authorization process and follow the instructions provided in the command results.
- `azure-waf-auth-complete`: Run this command to complete the authorization process. Should be used after running the azure_waf-auth-start command.
- `azure-waf-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `azure-waf-auth-test`: Tests connectivity to the Azure Web Application Firewall.
- `azure-waf-generate-login-url`: Generate the login url used for Authorization code flow.
- `azure-waf-subscriptions-list`: Gets all subscriptions for a tenant.
- `azure-waf-resource-group-list`: Gets all the resource groups for a subscription.


## AzureDevOps

**Type:** integration  
**Product:** AzureDevOps  

Manage Git repositories in Azure DevOps Services. Integration capabilities include retrieving, creating, and updating pull requests. Run pipelines and retrieve git information

**Commands:**

- `azure-devops-auth-test`: Tests the connectivity to Azure.
- `azure-devops-generate-login-url`: Generate the login url used for Authorization code flow.
- `azure-devops-auth-start`: Run this command to start the authorization process and follow the instructions in the command results.
- `azure-devops-auth-complete`: Run this command to complete the authorization process. Should be used after running the azure-devops-auth-start command.
- `azure-devops-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `get-mapping-fields`: Get mapping fields from remote incident. Please note that this method will not update the current incident. It's here for debugging purposes.


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

- `cb-eedr-alert-workflow-update`: Updates the workflow of a single event.
- `cb-eedr-device-quarantine`: Quarantines a device.
- `cb-eedr-device-unquarantine`: Removes a device from quarantine.
- `cb-eedr-device-background-scan-stop`: Stops a background scan on the specified devices.
- `cb-eedr-device-background-scan`: Start a background scan on device.
- `cb-eedr-device-bypass`: Enable a bypass on device.
- `cb-eedr-device-unbypass`: Disable a bypass on device.
- `cb-eedr-device-policy-update`: Update device policy.
- `cb-eedr-devices-list`: List devices based on the search query.
- `cb-eedr-list-alerts`: Returns a list of alerts.
- `cb-eedr-watchlist-list`: Retrieves all watchlists.
- `cb-eedr-get-watchlist-by-id`: Gets watchlist information by watchlist ID.
- `cb-eedr-watchlist-alerts-status`: Retrieves the alert status for the watchlist with given watchlist ID.
- `cb-eedr-watchlist-alerts-enable`: Turns on alerts for the watchlist with the specified watchlist ID.
- `cb-eedr-watchlist-alerts-disable`: Turns off alerts for the watchlist with the specified watchlist ID.


## Check Point Dome9 (CloudGuard)

**Type:** integration  
**Product:** Check Point Dome9 (CloudGuard)  

Dome9 integration allows to easily manage the security and compliance of the public cloud. This integration was integrated and tested with version 2 of checkpointdome9

**Commands:**

- `dome9-access-lease-list`: Get a list of all active Access Leases.
- `dome9-access-lease-delete`: Terminate an Access Lease.
- `dome9-access-lease-invitation-list`: Get a lease invitation.
- `dome9-access-lease-invitation-delete`: Delete an Access Lease invitation.
- `dome9-findings-search`: Search for findings in CloudGuard.
- `dome9-ip-list-create`: Add a new IP list.
- `dome9-ip-list-update`: Update an IP list. This will override the existing IP list.
- `dome9-ip-list-get`: Get an IP List by ID.
- `dome9-ip-list-delete`: Delete an IP List by ID.
- `dome9-ip-list-metadata-list`: Get all IP addresses metadata.
- `dome9-ip-list-metadata-create`: Add metadata for a new IP address. An IP address metadata must contain the CIDR, name, and classification. Classification can be External, Unsafe, Dmz, Internal
- `dome9-ip-list-metadata-update`: Update an existing IP address metadata. Classification can only be External, Unsafe, Dmz, InternalVpc, InternalDc, or NoClassification.
- `dome9-ip-list-metadata-delete`: Delete an IP address metadata with a specific CIDR.
- `dome9-compliance-remediation-get`: Get a list of remediations for the account.
- `dome9-compliance-remediation-create`: Add a new remediation.


## Cisco Umbrella Cloud Security v2

**Type:** integration  
**Product:** Cisco Umbrella cloud security  

Cisco Umbrella is a cloud security platform providing the first line of defense against internet threats. It uses DNS-layer security to block malicious requests before a connection is established, offering protection against malware, ransomware, phishing, and more. It offers real-time reporting, integrates with other Cisco solutions for layered security, and uses machine learning to uncover and predict threats. This integration was tested with version 2 of Cisco Umbrella Cloud Security

**Commands:**

- `umbrella-destinations-list`: Get destinations within a destination list. A destination is a URL, IP or fully qualified domain name.
- `umbrella-destination-add`: Add a destination to a destination list. A destination is a URL, IPv4, CIDR or fully qualified domain name. Accepted types for destination list with the access 
- `umbrella-destination-delete`: Remove a destination from a destination list. A destination is a URL, IP or fully qualified domain name.
- `umbrella-destination-lists-list`: Get destination lists. A list of destinations (for example, domain name or URL) to which you can block or allow access.
- `umbrella-destination-list-create`: Create a destination list. A list of destinations (for example, domain name or URL) to which you can block or allow access. Accepted types for destination list 
- `umbrella-destination-list-update`: Edit a destination list. A list of destinations (for example, domain name or URL) to which you can block or allow access.
- `umbrella-destination-list-delete`: Delete a destination list. A list of destinations (for example, domain name or URL) to which you can block or allow access.


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

- `cloudconvert-upload`: Uploads a file for conversion.
- `cloudconvert-convert`: Converts an uploaded file to the required format.
- `cloudconvert-check-status`: Checks the status of an operation. Use the 'create_war_room_entry' argument to also create a war room entry of the file when checking on a download operation.
- `cloudconvert-download`: Downloads a converted file as a URL or a War Room entry.


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

- `cloudflare-mcp-generate-login-url`: Generate an authentication login URL.
- `cloudflare-mcp-auth-test`: Test the authentication configuration with the MCP server.


## Cloudflare WAF

**Type:** integration  
**Product:** Cloudflare WAF  

Cloudflare WAF integration allows customers to manage firewall rules, filters, and IP-lists. It also allows to retrieve zones list for each account. This integration was integrated and tested with version 4 of CloudflareWAF

**Commands:**

- `cloudflare-waf-firewall-rule-create`: will be as deprecated, available until 2025-06-15 Create a new firewall rule that create new filter or use an exist filter. Permissions required for the API tok
- `cloudflare-waf-firewall-rule-update`: will be as deprecated, available until 2025-06-15 Update firewall rule by the specified rule ID. Can update rule action, paused, description, priority, products
- `cloudflare-waf-firewall-rule-delete`: will be as deprecated, available until 2025-06-15 Delete firewall rule by the specified rule ID. Permissions required for the API token: Account: Account Firewa
- `cloudflare-waf-firewall-rule-list`: will be as deprecated, available until 2025-06-15 List of firewall rules or details of individual rule by ID. Permissions required for the API token: Account: A
- `cloudflare-waf-filter-create`: Create a new filter which can be added to a firewall rule. Permissions required for the API token: Account: Account Filter Lists:Edit Zone: Firewall Services:Ed
- `cloudflare-waf-filter-update`: Update filter by the specified filter ID. Permissions required for the API token: Account: Account Filter Lists:Edit Zone: Firewall Services:Edit
- `cloudflare-waf-filter-delete`: Delete an exist filter (Note that a filter linked to firewall rule cannot be deleted). Permissions required for the API token: Account: Account Filter Lists:Edi
- `cloudflare-waf-filter-list`: List filters. Permissions required for the API token: Account: Account Filter Lists:Read Zone: Firewall Services:Read
- `cloudflare-waf-zone-list`: List all account zones. Permissions required for the API token: Zone: Zone Settings:Read Zone:Read
- `cloudflare-waf-ip-list-create`: Create a new IP-list. An IP-list is a list that includes IP addresses and CIDR. IP-list is used in the filter expression. Permissions required for the API token
- `cloudflare-waf-ip-list-delete`: Delete IP-list by the specified list ID. Permissions required for the API token: Account: All accounts - Account WAF:Edit
- `cloudflare-waf-ip-lists-list`: List IP-lists. Permissions required for the API token: Account: All accounts - Account WAF:Read
- `cloudflare-waf-ip-list-item-create`: Create new items for exist IP-list. Permissions required for the API token: Account: All accounts - Account WAF:Edit
- `cloudflare-waf-ip-list-item-update`: Replace the IP-list items with a new items Permissions required for the API token: Account: All accounts - Account WAF:Edit
- `cloudflare-waf-ip-list-item-delete`: Delete item of a IP-list by the specified list ID and list item. Permissions required for the API token: Account: All accounts - Account WAF:Edit


## Cloudflare Zero Trust

**Type:** integration  
**Product:** Cloudflare Zero Trust  

Cloudflare provides network and security products for consumers and businesses, utilizing reverse proxies for web traffic, edge computing, and a content distribution network to provide content across its network of servers. This integration was integrated and tested with version 1 of Cloudflare Zero Trust

**Commands:**

- `cloudflare-zero-trust-get-events`: Gets events from Cloudflare Zero Trust.


## CloudShare (Beta)

**Type:** integration  
**Product:** CloudShare  

This integration is a BETA that covers the API commands from CloudShare

**Commands:**

- `cloudshare-get-envs`: Retrieves environments
- `cloudshare-get-projects`: Retrieves all available projects
- `cloudshare-get-project`: Retrieves a specified project's details
- `cloudshare-get-project-policies`: Retrieves all environment policies available in a specified project. Environment policies define how long an environment will run, when it will be deleted, and 
- `cloudshare-get-project-blueprints`: Retrieves all blueprints available in a specified project
- `cloudshare-get-project-blueprint`: Retrieves details of a specified blueprint, including snapshots.
- `cloudshare-get-classes`: Retrieves all classes visible to the user
- `cloudshare-get-class`: Retrieves details of a specified class
- `cloudshare-delete-class`: Deletes a class
- `cloudshare-delete-class-environments`: Deletes all active student environments in a class
- `cloudshare-get-classes-countries`: Retrieves all countries that can be set as class locations
- `cloudshare-get-classes-customfields`: Retrieves any custom class creation fields defined in a specified project.
- `cloudshare-get-classes-detailed`: Retrieves all the details of a specified class, including full student data.
- `cloudshare-get-classes-instructors`: Retrieves project member users who can be assigned to classes as instructors
- `cloudshare-create-class`: Creates a class


## Commvault Cloud

**Type:** integration  
**Product:** Commvault Cloud  

Commvault Cloud provides pre-built integrations, automation workflows, and playbooks to streamline operations, enhance threat intelligence integration, and gain actionable insights through advanced reporting and analytics. This integration was integrated and tested with version 6.9.0 of CommvaultSecurityIQ

**Commands:**

- `commvault-security-set-disable-data-aging`: Disables data aging on CS
- `commvault-security-get-generate-token`: Generate Token
- `commvault-security-get-access-token-from-keyvault`: Read the access token from KeyVault
- `commvault-security-set-disable-saml-provider`: Disable SAML provider
- `commvault-security-get-copy-files-list-to-war-room`: Copy the list of affected files list to war room
- `commvault-security-set-disable-user`: Disables user
- `commvault-security-set-cleanroom-add-vm-to-recovery-group`: Add VM to Cleanroom


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

- `datadog-event-create`: This endpoint allows you to post events to the stream.
- `datadog-event-list`: Get a list of events / Get the details of a particular event.
- `datadog-tag-list`: Return a mapping of tags to hosts for your whole infrastructure.
- `datadog-host-tag-create`: This endpoint allows you to add new tags to a host, optionally specifying where these tags come from.
- `datadog-host-tag-get`: Return the list of tags that apply to a given host.
- `datadog-host-tag-update`: This endpoint allows you to replace all tags in an integration source with those supplied in the request.
- `datadog-host-tag-delete`: This endpoint allows you to remove all user-assigned tags for a single host.
- `datadog-active-metric-list`: Get the list of actively reporting metrics.
- `datadog-metric-search`: Search for metrics from the last 24 hours in Datadog.
- `datadog-metric-metadata-get`: Get metadata about a specific metric.
- `datadog-metric-metadata-update`: Edit metadata of a specific metric.
- `datadog-incident-create`: Create an incident.
- `datadog-incident-delete`: Delete an existing incident.
- `datadog-incident-update`: Updates an incident. Provide only the attributes that should be updated as this request is a partial update.
- `datadog-incident-list`: Get all incidents for the user’s organization / Get the details of an incident using incident_id.


## Datadog Cloud SIEM

**Type:** integration  
**Product:** Datadog Cloud SIEM  

Datadog Cloud SIEM integration for the platform. This integration allows security teams to: This integration was integrated and tested with version 2.12.0 of datadog-api-client

**Commands:**

- `datadog-get-signal`: Get a specific security signal by ID from Datadog Cloud SIEM.
- `datadog-list-signals`: Get a list of security signals from Datadog Cloud SIEM with optional filtering and pagination.
- `datadog-update-signal-state`: Update a security signal's assignee and/or state in Datadog Cloud SIEM. Can update assignee only, state only, or both in a single command.
- `datadog-add-signal-comment`: Add a comment to a security signal in Datadog Cloud SIEM.
- `datadog-list-signal-comments`: List all comments for a security signal in Datadog Cloud SIEM.
- `datadog-get-rule`: Get a specific security monitoring rule by ID from Datadog Cloud SIEM.
- `datadog-query-logs`: Query logs in Datadog Cloud SIEM with optional filtering for security investigations.
- `datadog-update-signal-assignee`: Update a security signal's assignee in Datadog Cloud SIEM.
- `datadog-update-suppression`: Update an existing suppression rule by ID.
- `datadog-list-suppressions`: List all suppressions affecting a specific security monitoring rule.
- `datadog-list-security-filters`: List all security filters from Datadog Cloud SIEM.
- `datadog-list-signal-notification-rules`: List all signal notification rules from Datadog Cloud SIEM.
- `datadog-list-vulnerability-notification-rules`: List all vulnerability notification rules from Datadog Cloud SIEM.
- `datadog-bitsai-get-investigation`: Get the BitsAI investigation for a security signal.
- `datadog-list-risk-scores`: List risk scores from Datadog Cloud SIEM.


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

- `gcp-iam-projects-get`: Lists project under the specified parent, or retrieves a specific project''s information. One of the arguments: ''parent'' or ''project_name'' must be provided.
- `gcp-iam-project-iam-policy-get`: Retrieves the IAM access control policy for the specified project.
- `gcp-iam-project-iam-permission-test`: Returns permissions that a caller has on the specified project. The permission list can be obtained by running the 'gcp-iam-testable-permission-list' command.
- `gcp-iam-project-iam-member-add`: Adds members to the project policy.
- `gcp-iam-project-iam-member-remove`: Removes members from the project policy.
- `gcp-iam-project-iam-policy-set`: Sets the IAM access control policy for the specified project. This operation will overwrite any existing policy.
- `gcp-iam-project-iam-policy-create`: Adds a new project IAM policy.
- `gcp-iam-folders-get`: Lists folders under the specified parent, or retrieves a specific folder information. One of the arguments: ''parent'' or ''folder_name'' must be provided.
- `gcp-iam-folder-iam-policy-get`: Retrieves the IAM access control policy for the specified folder.
- `gcp-iam-folder-iam-permission-test`: Returns permissions that a caller has on the specified folder. The permission list can be obtained by running the 'gcp-iam-testable-permission-list' command.
- `gcp-iam-folder-iam-member-add`: Adds members to the folder policy.
- `gcp-iam-folder-iam-member-remove`: Removes members from the folder policy.
- `gcp-iam-folder-iam-policy-set`: Sets the IAM access control policy for the specified folder. This operation will overwrite any existing policy.
- `gcp-iam-folder-iam-policy-create`: Adds a new folder IAM policy.
- `gcp-iam-organizations-get`: Lists organization resources that are visible to the caller, or retrieves an organization's information.


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

- `genesys-cloud-get-events`: Retrieves audit events from Genesys Cloud from the past 14 days. This command is intended for development and debugging purposes, as it may produce duplicate ev


## Google Cloud Compute

**Type:** integration  
**Product:** Google Cloud Compute  

Google Compute Engine delivers virtual machines running in Google's innovative data centers and worldwide fiber network. Compute Engine's tooling and workflow support enable scaling from single instances to global, load-balanced cloud computing

**Commands:**

- `gcp-compute-insert-instance`: Creates an instance resource in the specified project using the data included in the request.
- `gcp-compute-get-image-from-family`: Returns the latest image that is part of an image family and is not deprecated.
- `gcp-compute-get-network`: Returns the specified network.
- `gcp-compute-list-instances`: Retrieves the list of instances contained within the specified zone.
- `gcp-compute-aggregated-list-instances`: Retrieves aggregated list of all of the instances in your project across all regions and zones.
- `gcp-compute-get-global-operation`: Retrieves the specified Operations resource. Gets a list of operations by making a list() request.
- `gcp-compute-get-zone-operation`: Retrieves the specified zone-specific Operations resource.
- `gcp-compute-list-zone-operation`: Retrieves a list of Operation resources contained within the specified zone.
- `gcp-compute-delete-zone-operation`: Deletes the specified zone-specific Operations resource.
- `gcp-compute-get-instance`: Returns the specified Instance resource. Gets a list of available instances by making a list() request.
- `gcp-compute-delete-instance`: Deletes the specified Instance resource. For more information, see Stopping or Deleting an Instance.
- `gcp-compute-start-instance`: Starts an instance that was stopped using the instances().stop method. For more information, see Restart an instance.
- `gcp-compute-stop-instance`: Stops a running instance, shutting it down cleanly, and allows you to restart the instance at a later time. Stopped instances do not incur VM usage charges whil
- `gcp-compute-reset-instance`: Performs a reset on the instance. This is a hard reset the VM does not do a graceful shutdown. For more information, see Resetting an instance.
- `gcp-compute-set-instance-labels`: Sets labels on an instance. To learn more about labels, read the Labeling Resources documentation.


## Google Cloud Functions

**Type:** integration  
**Product:** Google Cloud Functions  

Google Cloud Functions is an event-driven serverless compute platform that enables you to run your code locally or in the cloud without having to provision servers. This integration was integrated and tested with API version 1 of Google Cloud Functions

**Commands:**

- `google-cloud-functions-list`: Lists all Google Cloud functions.
- `google-cloud-function-regions-list`: Lists all regions in the project.
- `google-cloud-function-get-by-name`: Gets the details of a specific Google Cloud function.
- `google-cloud-function-execute`: Executes a Google Cloud function.


## Google Cloud Logging

**Type:** integration  
**Product:** Google Cloud Logging  

With Google Cloud Logging, users can centralize all their logs in a single location, making it easier to troubleshoot issues and gain insights from their data

**Commands:**

- `gcp-logging-log-entries-list`: Lists log entries. Use this method to retrieve log entries that originated from a project/folder/organization/billing account.


## Google Cloud Platform

**Type:** integration  
**Product:** GCP  

The GCP Integration automates management and security configurations for Compute Engine, Storage, and Container resources on GCP. This integration was integrated and tested with version v1 (Compute, Storage, Container, SERVICE_USAGE), v3 (Resource Manager)

**Commands:**

- `gcp-compute-firewall-patch`: Updates a specific firewall rule with the data included in the request. Required permissions: compute.firewalls.update, compute.firewalls.get, compute.firewalls
- `gcp-storage-bucket-policy-delete`: Removes an entity from a bucket's Access Control List. Required permissions: storage.buckets.getIamPolicy, storage.buckets.setIamPolicy.
- `gcp-compute-subnet-update`: Enables flow logs or Private Google Access on a subnet. Required permissions: compute.subnetworks.setPrivateIpGoogleAccess, compute.subnetworks.update, compute.
- `gcp-container-cluster-security-update`: Configures security settings for GKE clusters, including access controls and visibility. Required permissions: container.clusters.update, container.clusters.get
- `gcp-gke-cluster-legacy-abac-auth-set`: Enables or disables legacy ABAC authorization for a GKE cluster. Required permissions: container.clusters.update.
- `gcp-gke-clusters-list`: Lists all GKE clusters owned by a project in the specified location. Required permissions: container.clusters.list.
- `gcp-gke-cluster-get`: Gets the details of a specific GKE cluster. Required permissions: container.clusters.get.
- `gcp-gke-node-pools-list`: Lists the node pools for a GKE cluster. Required permissions: container.clusters.get.
- `gcp-gke-node-pool-get`: Gets the details of a specific node pool in a GKE cluster. Required permissions: container.clusters.get.
- `gcp-gke-node-pool-management-set`: Enables or disables the auto-repair and/or auto-upgrade management features of a node pool. Required permissions: container.clusters.update.
- `gcp-gke-operations-list`: Lists all GKE operations in a project for the specified location. Required permissions: container.operations.list.
- `gcp-gke-operation-get`: Gets the details of a specific GKE operation. Required permissions: container.operations.get.
- `gcp-gke-operation-cancel`: Cancels a specific GKE operation. Required permissions: container.operations.get.
- `gcp-storage-bucket-metadata-update`: Updates Google Cloud Storage (GCS) bucket metadata, including settings such as versioning and Uniform Bucket-Level Access (UBLA). Required permission: storage.b
- `gcp-iam-project-policy-binding-remove`: Removes a specified IAM role binding from a GCP project. Required permissions: resourcemanager.projects.getIamPolicy, resourcemanager.projects.setIamPolicy.


## Google Cloud Pub/Sub

**Type:** integration  
**Product:** Google Cloud Pub / Sub  

Google Cloud Pub / Sub is a fully-managed real-time messaging service that allows you to send and receive messages between independent applications. This integration was integrated and tested with Google Cloud Pub/Sub

**Commands:**

- `gcp-pubsub-topics-list`: Get a list of the project's topics.
- `gcp-pubsub-topic-publish-message`: Publish a message in a topic.
- `gcp-pubsub-topic-subscription-get-by-name`: Get subscription details by subscription ID.
- `gcp-pubsub-topic-subscriptions-list`: Get a list of subscriptions by project ID or topic ID.
- `gcp-pubsub-topic-messages-pull`: Pull messages that were published.
- `gcp-pubsub-topic-subscription-create`: Create a pull or push subscription.
- `gcp-pubsub-topic-create`: Create a topic.
- `gcp-pubsub-topic-delete`: Delete a topic.
- `gcp-pubsub-topic-update`: Updates a topic.
- `gcp-pubsub-topic-subscription-update`: Update a subscription.
- `gcp-pubsub-topic-messages-seek`: Seeks a subscription to a given point in time or to a given snapshot.
- `gcp-pubsub-topic-snapshots-list`: Get a list of snapshots by project ID and topic ID.
- `gcp-pubsub-topic-snapshot-create`: Creates a snapshot from the requested subscription. Snapshots are used in gcp-pubsub-topic-messages-seek command.
- `gcp-pubsub-topic-snapshot-update`: Updates an existing snapshot. Snapshots are used in gcp-pubsub-topic-messages-seek command.
- `gcp-pubsub-topic-snapshot-delete`: Removes an existing snapshot.


## Google Cloud SCC

**Type:** integration  
**Product:** Google Cloud SCC  

Security Command Center is a security and risk management platform for Google Cloud. Security Command Center enables you to understand your security and data attack surface by providing asset inventory and discovery, identifying vulnerabilities and threats, and helping you mitigate and remediate risks across an organization. This integration helps you to perform tasks related to findings and assets. This integration was integrated and tested with version v1 and v2 APIs of GoogleCloudSCC

**Commands:**

- `google-cloud-scc-asset-list`: Lists an organization's assets.
- `google-cloud-scc-finding-list`: Use google-cloud-scc-v2-finding-list instead. Lists an organization or source's findings.
- `google-cloud-scc-finding-update`: Use google-cloud-scc-v2-finding-update instead. Update an organization's or source's finding.
- `google-cloud-scc-asset-resource-list`: Lists cloud asset's resources.
- `google-cloud-scc-asset-owner-get`: Gets the owner information for the provided projects.
- `google-cloud-scc-finding-state-update`: Use google-cloud-scc-v2-finding-state-update instead. Update the state of organization's or source's finding.
- `google-cloud-scc-v2-finding-list`: Lists an organization or source's findings using the Security Command Center v2 API.
- `google-cloud-scc-v2-finding-update`: Update an organization's or source's finding using the Security Command Center v2 API.
- `google-cloud-scc-v2-finding-state-update`: Update the state of an organization's or source's finding using the Security Command Center v2 API.
- `google-cloud-scc-finding-mute`: Mute an organization's or source's finding using the Security Command Center v2 API.
- `google-cloud-scc-finding-unmute`: Unmute an organization's or source's finding using the Security Command Center v2 API.
- `google-cloud-scc-mute-rule-get`: Get a mute rule (mute config) of an organization using the Security Command Center v2 API.
- `google-cloud-scc-mute-rule-create`: Create a mute rule (mute config) for an organization using the Security Command Center v2 API.


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

- `azure-sc-list-alert`: Lists alerts for the subscription according to the specified filters. The OData select, expand, and filter arguments are deprecated, as they are no longer suppo
- `azure-sc-update-atp`: Updates Advanced Threat Detection settings.
- `azure-sc-get-atp`: Returns the Advanced Threat Protection setting.
- `azure-sc-update-aps`: Updates a specific auto provisioning setting.
- `azure-sc-get-aps`: Returns details of a specific auto provisioning setting.
- `azure-sc-list-aps`: Lists auto provisioning settings in the subscription.
- `azure-sc-list-jit`: Lists all policies for protecting resources using Just-in-Time access control.
- `azure-sc-list-storage`: Lists all the storage accounts available under the subscription.
- `azure-list-subscriptions`: List available subscriptions for this application.
- `azure-sc-list-location`: The location of the responsible ASC of the specific subscription. For each subscription there is only one responsible location.
- `azure-sc-get-alert`: Get an alert that is associated a resource group or a subscription.


## Microsoft Defender for Cloud Apps

**Type:** integration  
**Product:** Microsoft Defender for Cloud Apps  

Microsoft Cloud App Security is a multimode Cloud Access Security Broker (CASB). It provides rich visibility, control over data travel, and sophisticated analytics to identify and combat cyber threats across all your cloud services. Use the integration to view and resolve alerts, view activities, view files, and view user accounts. This integration was integrated and tested with version 178 of MicrosoftCloudAppSecurity. To use a Device Code Flow, you need to add a new Azure App Registration in the Azure Portal. To add the registration, refer to the following Microsoft article. To connect to the Microsoft Cloud App Security: At the end of the process you'll see a message that you've logged in successfully. Follow these steps for a self-deployed configuration: Make sure to provide the following permissions for the app to work with Microsoft Cloud App Security: To access the Microsoft Cloud App Security API, you need to grant authorization. See the Microsoft documentation to view a detailed explanation of how to create the Server URL and User key (token). For more information about which permissions are required for the token owner in Microsoft Cloud App Security, see Microsoft Cloud App Security - Manage admin access

**Commands:**

- `microsoft-cas-auth-start`: Run this command to start the authorization process and follow the instructions in the command results. (for device-code mode)
- `microsoft-cas-auth-complete`: Run this command to complete the authorization process. Should be used after running the microsoft-cas-auth-start command. (for device-code mode)
- `microsoft-cas-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `microsoft-cas-auth-test`: Tests the connectivity to the Microsoft cas.
- `microsoft-cas-alerts-list`: Returns a list of alerts that match the specified filters.
- `microsoft-cas-alert-close-benign`: An alert on a suspicious but not malicious activity, such as a penetration test or other authorized suspicious action
- `microsoft-cas-alert-close-true-positive`: Cֹlose multiple alerts matching the specified filters as true positive (an alert on a confirmed malicious activity.
- `microsoft-cas-alert-close-false-positive`: Close multiple alerts matching the specified filters as false positive (an alert on a non-malicious activity).
- `microsoft-cas-activities-list`: Returns a list of activities that match the specified filters.
- `microsoft-cas-files-list`: Returns a list of files that match the specified filters. Filters include file type, file share value, file extension, file quarantine status, and a custom filt
- `microsoft-cas-users-accounts-list`: Returns a list of user accounts that match the specified filters. Filters include user account type, group ID, external/internal, user account status, and custo


## Microsoft Management Activity API (O365 Azure Events)

**Type:** integration  
**Product:** Microsoft Management Activity API (O365/Azure Events)  

The Microsoft Management Activity API integration enables you to subscribe or unsubscribe to different audits, receive their content, and fetch new content as incidents. Through the integration you can subscribe to new content types or stop your subscription, list the available content of each content type, and most importantly, fetch new content records from content types of your choice as the platform. This integration was integrated and tested with version 1.0 of Microsoft Management Activity API (O365 Azure Events). There are two application authentication methods available

**Commands:**

- `ms-management-activity-start-subscription`: Starts a subscription to a given content type.
- `ms-management-activity-stop-subscription`: Stops a subscription to a given content type.
- `ms-management-activity-list-subscriptions`: List the content types you are currently subscribed to.
- `ms-management-activity-list-content`: Returns all content of a specific content type.
- `ms-management-activity-generate-login-url`: Generate the login url used for Authorization code flow.
- `ms-management-activity-auth-reset`: Run this command if for some reason you need to rerun the authentication process.


## Microsoft Policy And Compliance (Audit Log)

**Type:** integration  
**Product:** Office 365 and Azure (Audit Log)  

Use the integration to get logs from the O365 service

**Commands:**

- `o365-auditlog-search`: Use the o365-search-auditlog command to search the unified audit log. This log contains events from Exchange Online, SharePoint Online, OneDrive for Business, E


## Palo Alto Networks - Prisma Cloud Compute

**Type:** integration  
**Product:** Prisma Cloud Compute by Palo Alto Networks  

Prisma™ Cloud Compute Edition delivers cloud workload protection (CWPP) for modern enterprises, providing holistic protection across hosts, containers, and serverless deployments in any cloud, throughout the application lifecycle. Prisma Cloud Compute Edition is cloud native and API-enabled, protecting all your workloads regardless of their underlying compute technology or the cloud in which they run. This integration lets you import Palo Alto Networks - Prisma Cloud Compute alerts into the platform

**Commands:**

- `prisma-cloud-compute-profile-host-list`: Get information about the hosts and their profile events. This command supports asterisks which allows you to get host profiles by filtering its fields accordin
- `prisma-cloud-compute-profile-container-list`: Get information about the containers and their profile events. This command supports asterisks which allows you to get container profiles by filtering its field
- `prisma-cloud-compute-profile-container-hosts-list`: Get the hosts where a specific container is running.
- `prisma-cloud-compute-profile-container-forensic-list`: Get runtime forensics data for a specific container on a specific host.
- `prisma-cloud-compute-host-forensic-list`: Get forensics on a specific host.
- `prisma-cloud-compute-console-version-info`: Get the console version.
- `prisma-cloud-compute-custom-feeds-ip-list`: Get all the blacklisted IP addresses in the system.
- `prisma-cloud-compute-custom-feeds-ip-add`: Add a list of banned IP addresses to be blocked by the system.
- `prisma-cloud-compute-custom-feeds-ip-remove`: Remove a list of IPs from the system's block list.
- `prisma-cloud-compute-custom-feeds-malware-list`: List all custom uploaded md5 malwares.
- `prisma-cloud-compute-custom-feeds-malware-add`: Add custom md5 malware hashes.
- `cve`: Get information about the CVEs in the system. Will return a maximum of 50 records. It is possible to query for a partial CVE description such as cve-2020 or cve
- `prisma-cloud-compute-defenders-list`: Retrieve a list of defenders and their information.
- `prisma-cloud-compute-collections-list`: Retrieves a list of all collections.
- `prisma-cloud-compute-container-namespace-list`: Get the containers namespaces names.


## Palo Alto Networks - Strata Cloud Manager

**Type:** integration  
**Product:** Palo Alto Networks - Strata Cloud Manager  

Provides commands for interaction with Prisma SASE API. This integration was integrated and tested with version v1 of Palo Alto Networks - Prisma SASE

**Commands:**

- `prisma-sase-security-rule-create`: Create a new security rule.
- `prisma-sase-security-rule-list`: Lists all security rules.
- `prisma-sase-candidate-config-push`: Push the candidate configuration.
- `prisma-sase-security-rule-update`: Update an existing security rule.
- `prisma-sase-address-object-update`: Update an existing address object.
- `prisma-sase-config-job-list`: Lists all configuration jobs.
- `prisma-sase-security-rule-delete`: Delete a specific security rule.
- `prisma-sase-address-object-create`: Create a new address object.
- `prisma-sase-address-object-delete`: Delete a specific address object.
- `prisma-sase-address-object-list`: Lists all addresses objects.
- `prisma-sase-tag-list`: Lists all tags.
- `prisma-sase-tag-create`: Create a new tag.
- `prisma-sase-tag-update`: Update an existing tag.
- `prisma-sase-tag-delete`: Delete a specific tag.
- `prisma-sase-address-group-list`: Lists all address groups.


## Palo Alto Networks Prisma AIRS - AI Red Teaming

**Type:** integration  
**Product:** Palo Alto Networks - Prisma AIRS AI Security  

Discover and remediate AI application vulnerabilities with Palo Alto Networks Prisma AIRS AI Red Teaming: manage targets and adapters, run and monitor red-team scans, review attack reports and remediation guidance, and curate prompt sets and custom attacks. This integration was integrated and tested with the Palo Alto Networks Prisma AIRS AI Red Teaming API as of June 2026

**Commands:**

- `prisma-airs-redteam-targets-list`: List all Red Team targets.
- `prisma-airs-redteam-targets-create`: Create a new Red Team target.
- `prisma-airs-redteam-targets-get`: Get Red Team target details by UUID.
- `prisma-airs-redteam-targets-update`: Update an existing Red Team target.
- `prisma-airs-redteam-targets-delete`: Delete a Red Team target.
- `prisma-airs-redteam-targets-probe`: Probe a Red Team target to validate connectivity and gather profiling data.
- `prisma-airs-redteam-targets-profile`: Get Red Team target profile (background, context, profiling status). View detailed profiling information including background context and AI-generated fields.
- `prisma-airs-redteam-targets-update-profile`: Update Red Team target profile (background and additional context). Modify target background information or add additional context like model details and suppor
- `prisma-airs-redteam-targets-metadata`: Get Red Team target field metadata. Returns field definitions (types, requirements, constraints) for all available target configuration fields. Useful for under
- `prisma-airs-redteam-targets-validate-auth`: Validate authentication credentials for a Red Team target provider without creating or modifying a target. Useful for verifying credentials before creating a ta
- `prisma-airs-redteam-targets-templates`: List Red Team target configuration templates per provider. Each template describes the connection fields expected for that target provider type. Read-only.
- `prisma-airs-redteam-targets-error-logs`: List target-profile (profiling) error logs for a Red Team target. Returns the failures recorded while Prisma AIRS was probing or profiling the target (for examp
- `prisma-airs-redteam-scan-error-logs`: List job-level error logs for a Red Team scan. Returns the per-attack probe failures recorded while a scan job was running (for example, timeouts or target conn
- `prisma-airs-redteam-dashboard-scan-statistics`: Get Red Team scan statistics and risk profile (dashboard telemetry). Returns aggregate scan counts and, when available, breakdowns by target type, scan status, 
- `prisma-airs-redteam-dashboard-score-trend`: Get the Red Team risk score trend for a target (dashboard telemetry). Returns time-bucketed labels plus one or more data series showing how the target's score c


## Palo Alto Networks Prisma AIRS - AI Runtime Security

**Type:** integration  
**Product:** Palo Alto Networks - Prisma AIRS AI Security  

Integrate with Palo Alto Networks Prisma AIRS for AI security capabilities including runtime scanning, red teaming, AI supply chain security, and DLP configuration. This integration was integrated and tested with Palo Alto Networks Prisma AIRS - AI Runtime Security

**Commands:**

- `prisma-airs-runtime-scan`: Scan a single prompt against a security profile for AI security threats.


## Palo Alto Networks Prisma AIRS - AI Supply Chain Security

**Type:** integration  
**Product:** Palo Alto Networks - Prisma AIRS AI Security  

Scan and govern AI models with Palo Alto Networks Prisma AIRS AI Supply Chain Security: model scans, evaluations, violations, labels, model groups, and security rules. This integration was integrated and tested with Palo Alto Networks Prisma AIRS - AI Supply Chain Security

**Commands:**

- `prisma-airs-model-security-scans-list`: List all model security scans.
- `prisma-airs-model-security-scans-create`: Create a new model security scan to check a model for supply chain security issues. Scan is asynchronous - use scans-get to poll for completion.
- `prisma-airs-model-security-scans-get`: Get model security scan status and results. Use this to poll scan completion after scans-create.
- `prisma-airs-model-security-scans-violations`: Get rule violations for a model security scan. Shows detailed information about which security rules failed and why.
- `prisma-airs-model-security-labels-keys`: Get distinct label keys across all model security scans. Use for discovering available labels for filtering/organization.
- `prisma-airs-model-security-labels-values`: Get distinct values for a specific label key across all model security scans. Use to discover what values exist for a given label.
- `prisma-airs-model-security-labels-add`: Add labels to a model security scan for organization and filtering. Labels are key-value pairs.
- `prisma-airs-model-security-labels-set`: Set labels on a model security scan, replacing all existing labels. Use this to completely update scan labels.
- `prisma-airs-model-security-labels-delete`: Delete labels from a model security scan by key. Removes specific labels while preserving others.
- `prisma-airs-model-security-scans-evaluation`: Get a single rule evaluation by UUID. Retrieves detailed information about how a specific rule was evaluated during a scan.
- `prisma-airs-model-security-scans-violation`: Get a single violation by UUID. Retrieves detailed information about a specific security rule violation found during a scan.
- `prisma-airs-model-security-scans-files`: Get files for a scan. Lists all files that were scanned within a model, showing file structure and scan results.
- `prisma-airs-model-security-scans-evaluations`: Get rule evaluations for a scan. Lists all rule evaluations showing which security rules passed, failed, or had errors.
- `prisma-airs-model-security-models-list`: List Model Security model catalog entries (aggregate over their scanned versions). Read-only.
- `prisma-airs-model-security-models-get`: Get a single Model Security model by UUID. Read-only.


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

- `prisma-access-logout-user`: Force logout a specific user from Prisma Access
- `prisma-access-query`: Run a query via the Prisma Access CLI
- `prisma-access-cli-command`: Run a custom CLI command on Prisma Access
- `prisma-access-active-users`: Query currently active users.


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

- `prisma-cloud-alert-dismiss`: Dismiss or snooze the alerts matching the given filter. Either policy IDs or alert IDs must be provided. When no absolute time nor relative time arguments are p
- `prisma-cloud-alert-get-details`: Gets the details of an alert based on the alert ID.
- `prisma-cloud-alert-filter-list`: List the acceptable filters and values for alerts.
- `prisma-cloud-remediation-command-list`: Generates and returns a list of remediation commands for the specified alerts and policies. Data returned for a successful call include fully constructed comman
- `prisma-cloud-alert-remediate`: Remediates the alert with the specified ID, if that alert is associated with a remediable policy. In order to check what remediation would run, use the "prisma-
- `prisma-cloud-alert-reopen`: Re-open the alerts matching the given filter. Either policy IDs or alert IDs must be provided. When no absolute time nor relative time arguments are provided, t
- `prisma-cloud-alert-search`: Search alerts on the Prisma Cloud platform. When no absolute time nor relative time arguments are provided, the search will show alerts from the last 7 days.
- `prisma-cloud-config-search`: Search configuration inventory on the Prisma Cloud platform using RQL language. Use this command for all queries that start with "config". When no absolute time
- `prisma-cloud-event-search`: Search events inventory on the Prisma Cloud platform using RQL language. Use this command for all queries that start with "event". When no absolute time nor rel
- `prisma-cloud-network-search`: Search networks inventory on the Prisma Cloud platform using RQL language. Use this command for all queries that start with "networks". When no absolute time no


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

- `iam-create-user`: Creates a user.
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Disable an active user.


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

- `proofpoint-ctr-incidents-list`: Returns a list of Proofpoint Cloud Threat Response incidents matching the supplied filters.
- `proofpoint-ctr-incident-get`: Returns full details for a specific Proofpoint Cloud Threat Response incident.


## Radware Cloud DDoS Protection Services

**Type:** integration  
**Product:** Radware Cloud DDoS Protection Services  

Radware Cloud Service provides customers and partners with the ability to programmatically perform service-related actions. The integration can be used to automate application and assets creation and day-to-day management to retrieve up-to-date data about Security Events and Operational Alerts This integration was integrated and tested with version 25.3.1 of Radware Cloud DDoS Protection Services

**Commands:**

- `radware-cloud-ddos-protection-services-get-events`: Send events from Radware Cloud DDoS Protection Services to XSIAM. Used mainly for debugging.


## Rapid7 InsightVM Cloud

**Type:** integration  
**Product:** Rapid7 InsightVM Cloud  

InsightVM is a Vulnerability Management Tool which Scan your Network, Eliminate Vulnerabilities, Track and Communicate progress

**Commands:**

- `insightvm-cloud-get-asset`: Returns the assessment and details of an asset (specified by id). Only assets which the caller has access to can be returned.
- `insightvm-cloud-get-scan`: Retrieves the scan with the specified identifier.
- `insightvm-cloud-get-scan-engines`: Retrieves a page of scan engines.
- `insightvm-cloud-get-health-check`: Returns an indicator of the health of the API.
- `insightvm-cloud-search-assets`: Returns the inventory, assessment, and summary details for a page of assets.
- `insightvm-cloud-last-sites`: Returns the details for sites
- `insightvm-cloud-search-vulnerabilities`: Returns all vulnerabilities that can be assessed.
- `insightvm-cloud-start-scan`: Starts a scan.
- `insightvm-cloud-stop-scan`: Stops the scan with the specified identifier.


## ReversingLabs TitaniumCloud v2

**Type:** integration  
**Product:** ReversingLabs TitaniumCloud  

ReversingLabs TitaniumCloud provides threat analysis data from various ReversingLabs cloud services

**Commands:**

- `reversinglabs-titaniumcloud-file-reputation`: Retrieve File Reputation data from TitaniumCloud


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

- `rubrik-radar-analysis-status`: Check the Radar Event for updates.
- `rubrik-sonar-sensitive-hits`: Find data classification hits on an object.
- `rubrik-cdm-cluster-location`: Find the CDM GeoLocation of a CDM Cluster.
- `rubrik-cdm-cluster-connection-state`: Find the CDM Connection State of a CDM Cluster.
- `rubrik-polaris-object-search`: Search for Rubrik discovered objects of any type, return zero or more matches.
- `rubrik-sonar-policies-list`: Retrieve the list of all the available Sonar policies.
- `rubrik-sonar-policy-analyzer-groups-list`: List the analyzer group policies.
- `rubrik-polaris-vm-object-metadata-get`: Retrieve details for a Vsphere object based on the provided object ID.
- `rubrik-polaris-vm-objects-list`: Retrieve a list of all the objects of the Vsphere Vm known to the Rubrik.
- `rubrik-sonar-ondemand-scan`: Trigger an on-demand scan of a system. Supports "Vsphere VM" object type only.
- `rubrik-sonar-ondemand-scan-status`: Retrieve the status of a scanned system.
- `rubrik-polaris-vm-object-snapshot-list`: Search for a Rubrik snapshot of an object based on the provided snapshot ID, exact timestamp, or specific value like earliest/latest, or closest before/after a 
- `rubrik-sonar-ondemand-scan-result`: Retrieve the download link for the requested scanned file.
- `rubrik-radar-anomaly-csv-analysis`: Request for the analysis and retrieve the download link or directly download file for the Radar CSV analyzed file.
- `rubrik-sonar-csv-download`: Request to download the Sonar CSV Snapshot results file.


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

- `sap-cloud-get-events`: Retrieves events from the SAP Cloud for Customer API.


## Saviynt Enterprise Identity Cloud

**Type:** integration  
**Product:** Saviynt Enterprise Identity Cloud  

Collector for Saviynt Enterprise Identity Cloud (EIC) audit logs using Analytics Runtime Control V2. This integration was tested with Saviynt EIC API Reference for Amsterdam GA Release (API v5)

**Commands:**

- `saviynt-eic-get-events`: Gets events from Saviynt EIC.


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

- `spycloud-list-breaches`: Lists the breaches identified. By default this lists all breaches known in Spycloud. With the arguments it's possible to scope the results on date and keywords.
- `spycloud-get-breach-data`: Retrieves the breach details. While very similar to list-breaches, this command obtains one specific breach, which is easier for automation tasks
- `spycloud-domain-data`: Get all the data from a monitored domain and the breaches occurred that relates with it. Can be scoped by domain, type and severity
- `spycloud-email-data`: Get all the data from a monitored email address and the breaches occurred that relates with it. Can be scoped by date, severity and breach
- `spycloud-watchlist-data`: Get all the data from a watchlist.


## SpyCloud Enterprise Protection Enrichment

**Type:** integration  
**Product:** SpyCloud Enterprise Protection  
**Commands:**

- `spycloud-breach-catalog-list`: List the Breach Catalog. By default, this lists all breaches in SpyCloud. With the arguments, it's possible to scope the results.
- `spycloud-breach-catalog-get`: Get Breach Catalog Information by ID.
- `spycloud-domain-data-get`: Get Breach Data by Domain.
- `spycloud-username-data-get`: Get Breach Data by Username.
- `spycloud-ip-address-data-get`: Get Breach Data by IP Address.
- `spycloud-email-data-get`: Get Breach Data by Email.
- `spycloud-password-data-get`: Get Breach Data by Password.
- `spycloud-watchlist-data-list`: List Breach Data. By default, this lists all breach data for the customer's configured watchlist. With the arguments, it's possible to scope the results.
- `spycloud-compass-device-data-get`: Get Compass device data by infected_machine_id.
- `spycloud-compass-data-list`: List Compass data. By default, this lists all Compass data. With the arguments, it's possible to scope the results.
- `spycloud-compass-device-list`: List Compass device data. By default, this lists all devices. With the arguments, it's possible to scope the results.
- `spycloud-compass-application-data-get`: Get Compass application data for a specific application.


## Sumo Logic Cloud SIEM

**Type:** integration  
**Product:** Sumo Logic Cloud SIEM  

Freeing the analyst with autonomous decisions. This integration was integrated and tested with version 6.1.0 of SumoLogicSEC

**Commands:**

- `sumologic-sec-insight-get-details`: Get Insight details for a specific Insight ID.
- `sumologic-sec-insight-add-comment`: Get comments for a specific Insight ID. (Users can post and update comments on the Sumo Logic Cloud SIEM portal for any Insight ID.)
- `sumologic-sec-insight-get-comments`: Get comments for a specific Insight ID. (Users can post and update comments on the Sumo Logic Cloud SIEM portal for any Insight ID.)
- `sumologic-sec-signal-get-details`: Get Signal details for a specific Signal ID. Signal details command references signals in Sumo Logic Cloud SIEM which are created when records exhibit suspiciou
- `sumologic-sec-entity-get-details`: Get entity details for a specific entity ID
- `sumologic-sec-insight-search`: Search insights using available filters
- `sumologic-sec-signal-search`: Search signals using available filters
- `sumologic-sec-entity-search`: Search entities using the available filters
- `sumologic-sec-insight-set-status`: Change status of Insight
- `sumologic-sec-match-list-get`: Get match lists
- `sumologic-sec-match-list-update`: Add item to match list
- `sumologic-sec-threat-intel-search-indicators`: Search Threat Intel Indicators
- `sumologic-sec-threat-intel-get-sources`: Get Threat Intel Sources
- `sumologic-sec-threat-intel-update-source`: Add Threat Intel Indicator to Threat Intel Source


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

- `fireeye-etp-search-messages`: Search for messages using specific message attributes as indicators.
- `fireeye-etp-get-message`: Get the data of a specific message.
- `fireeye-etp-list-alerts`: Get summary format information about the alerts.
- `fireeye-etp-download-alert-case-files`: Downloads all case files for the specified alert ID as a ZIP file. You can obtain the alert ID from the Alert Summary response, for example: "id": "AV7zzRy7kvIw
- `fireeye-etp-list-yara-rulesets`: Fetch the list of YARA rulesets and return a list with all the rules.
- `fireeye-etp-download-yara-file`: Downloads a YARA file.
- `fireeye-etp-upload-yara-file`: Update or replace the YARA rule file in the existing ruleset.
- `fireeye-etp-get-events-data`: Returns all events of the alert by the alert ID.
- `fireeye-etp-quarantine-release`: Releases the email file present in the quarantine for the given email. Cloud message ID.


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

- `trendmicro-cas-security-events-list`: Retrieves security event logs of services.
- `trendmicro-cas-email-sweep`: Searches for email messages in mailboxes, matching search criteria.
- `trendmicro-cas-user-take-action`: Takes action on a batch of specified user accounts, such as disabling users accounts, requesting multi-factor authentication, and requesting to reset a password
- `trendmicro-cas-email-take-action`: Takes action on a batch of specified email messages, such as deleting and quarantining email messages. Relevant for office365 exchange only.
- `trendmicro-cas-user-action-result-query`: Queries the results of actions taken on a user's account.
- `trendmicro-cas-email-action-result-query`: Queries the results of actions taken for email messages.
- `trendmicro-cas-blocked-lists-get`: Retrieves all blocked senders, URLs, and SHA-1 hash values that have been configured to quarantine Exchange Online email messages.
- `trendmicro-cas-blocked-lists-update`: Adds or removes senders, URLs, SHA-1 hash values to or from blocked lists. You must specify one of senders, urls, or filehashes.


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

- `wootcloud-get-pkt-alerts`: list packet alerts generated in requested time span
- `wootcloud-get-bt-alerts`: list bluetooth alerts generated in requested time span
- `wootcloud-get-anomaly-alerts`: list anomaly alerts generated in requested time span
- `wootcloud-fetch-packet-alert`: retrieve single packet alert given packet id
- `wootcloud-fetch-bluetooth-alert`: retrieve single bluetooth alert given packet id
- `wootcloud-fetch-anomaly-alert`: retrieve single anomaly alert given packet id


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

