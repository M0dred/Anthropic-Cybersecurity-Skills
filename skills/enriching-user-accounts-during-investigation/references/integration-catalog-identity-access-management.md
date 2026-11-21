# Integration and Automation Catalog - Identity Access Management

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## Allow IP - Okta Zone

**Type:** playbook  
**Product:** Okta  

Sync a list of IP addresses to the Okta Network Zone with the given ID. Existing IPs in the Okta Zone which are not in the input list will be removed and the indicator will be untagged in the platform. IDs can be retrieved using !okta-list-zones. This playbook supports CIDR notation only (1.1.1.1/32) and not range notation (1.1.1.1-1.1.1.1)

**Inputs:**

- `Indicator Query`: Indicators matching the indicator query will be used as playbook input
- `IP`: IP addresses to set in the allow list
- `ZoneID`: ID of the Okta Zone to update. Use !okta-list-zones to obtain
- `IndicatorTagName`: Name of the Indicator Tag to apply to any IPs allow listed by this playbook.


## CyberArk AIM v2

**Type:** integration  
**Product:** CyberArk Central Credential Provider (CCP)  

The CyberArk Central Credential Provider (CCP) provides a secure safe in which to store your account credentials. Use this integration to retrieve the account credentials in CyberArk CCP. This integration fetches credentials. For more information, see Managing Credentials

**Commands:**

- `cyberark-aim-list-credentials`: Lists all available credentials according to the list of credential names configured.


## CyberArk Certificate Manager

**Type:** integration  
**Product:** CyberArk Certificate Manager Self-Hosted  

Retrieves information about certificates stored in Venafi

**Commands:**

- `venafi-get-certificates`: Gets Venafi certificates query. All dates are in 2016-11-12T00:00:00.0000000Z format. For additional field information, see: https://ao-tlspd.dev.ven-eco.com/ap
- `venafi-get-certificate-details`: Uses a certificate GUID to extract more details from the certificate store.


## CyberArk EPM SOC Response

**Type:** integration  
**Product:** CyberArk Endpoint Privilege Manager  

Use the CyberArk EPM integration to activate and deactivate CyberArk EPM risk plans for specific endpoints. This integration was integrated and tested with the CyberArk EPM API

**Commands:**

- `cyberarkepm-activate-risk-plan`: Activates a CyberArk EPM risk plan for a specified endpoint.
- `cyberarkepm-deactivate-risk-plan`: Deactivates a CyberArk EPM risk plan for a specified endpoint.

**Inputs:**

- `endpoint_name`: Hostname of target endpoint.
- `logged_in_user`: Logged in user name of target endpoint.


## CyberArk Identity Security Platform

**Type:** integration  
**Product:** CyberArk  
**Commands:**

- `cyberark-isp-get-events`: Gets audit events from CyberArk Identity Security Platform. This command is used for developing/debugging and is to be used with caution, as it can create event


## CyberArk PAM

**Type:** integration  
**Product:** CyberArk  

Use the CyberArk Privileged Access Management (PAM) solution to manage users, safes, vaults, and accounts from the platform

**Commands:**

- `cyberark-pas-user-add`: Add a new user to the vault.
- `cyberark-pas-user-update`: Update an existing vault user.
- `cyberark-pas-user-delete`: Delete a specific user in the vault.
- `cyberark-pas-users-list`: Return a list of all existing users in the vault that meet the filter and search criteria.
- `cyberark-pas-user-activate`: Activate an existing vault user who was suspended after entering incorrect credentials multiple times. Uses the V1 of the API and may change in the future.
- `cyberark-pas-safes-list`: Return information about all of the user’s safes in the vault.
- `cyberark-pas-safe-get-by-name`: Return information about a specific safe in the vault.
- `cyberark-pas-safe-add`: Add a new safe to the vault.
- `cyberark-pas-safe-update`: Update a single safe in the vault.
- `cyberark-pas-safe-delete`: Delete a safe from the vault.
- `cyberark-pas-safe-members-list`: Return a list of the members of the safe.
- `cyberark-pas-safe-member-add`: Add an existing user as a safe member.
- `cyberark-pas-safe-member-update`: Update an existing safe member. Uses the V1 of the API and may change in the future.
- `cyberark-pas-account-add`: Add a new privileged account or SSH key to the vault.
- `cyberark-pas-account-update`: Update the details of an existing account.


## Entra ID Identity And Access

**Type:** integration  
**Product:** Microsoft Graph Identity and Access  

Use the Entra ID Identity And Access (formerly Azure Active Directory Identity And Access) integration to manage roles and members

**Commands:**

- `msgraph-identity-auth-start`: Run this command to start the authorization process and follow the instructions in the command results.
- `msgraph-identity-auth-complete`: Run this command to complete the authorization process. Should be used after running the msgraph-identity-auth-start command.
- `msgraph-identity-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `msgraph-identity-auth-test`: Tests connectivity to Microsoft.
- `msgraph-identity-directory-roles-list`: Lists the roles in the directory.
- `msgraph-identity-directory-role-activate`: Activates a role by its template ID.
- `msgraph-identity-directory-role-members-list`: Gets all members in a role ID.
- `msgraph-identity-directory-role-member-add`: Adds a user to a role.
- `msgraph-identity-directory-role-member-remove`: Removes a user from a role.
- `msgraph-identity-ip-named-locations-create`: Create an ip named location.
- `msgraph-identity-ip-named-locations-get`: Gets an ip named location.
- `msgraph-identity-ip-named-locations-delete`: Deletes an ip named location.
- `msgraph-identity-ip-named-locations-update`: Updates an ip named location.
- `msgraph-identity-ip-named-locations-update`: update an ip named location by id.
- `msgraph-identity-protection-risks-list`: Retrieve the properties of a collection of riskDetection objects.


## IAMInitOktaUser

**Type:** script  
**Product:** Okta  

Generates a password and sets the password for an Okta user. Enables the account. Sends an email to the user with the account information. This script is running the send-mail command, make sure there is a mail sender integration configured

**Inputs:**

- `pwdGenerationScript`: The password generator script.
- `username`: The Okta username of the user.
- `displayname`: The display name of the employee.
- `temporary_password`: When true, you'll need to change the password in the next login.
- `to_email`: The email address that the password will be sent to.
- `inc_id`: The incident ID.
- `email_subject`: The subject of the email sent to IT.
- `email_body`: The body of the email sent to IT.


## Okta (Standard Connector)

**Type:** integration  
**Product:** Okta (Standard Connector)  

Integration with Okta's cloud-based identity management service

**Commands:**

- `okta-unlock-user`: Unlocks a single user.
- `okta-deactivate-user`: Deactivates a single user.
- `okta-activate-user`: Activates a single user.
- `okta-suspend-user`: Suspends a single user. This operation can only be performed on users with an ACTIVE status. After the porcess is completed, the user's status is SUSPENDED.
- `okta-unsuspend-user`: Returns a single user to ACTIVE status. This operation can only be performed on users that have a SUSPENDED status.
- `okta-get-user-factors`: Returns all the enrolled factors for the specified user.
- `okta-reset-factor`: Un-enrolls an existing factor for the specified user. This enables the user to enroll a new factor.
- `okta-set-password`: Sets passwords without validating existing user credentials.
- `okta-add-to-group`: Adds a user to a group with OKTA_GROUP type.
- `okta-remove-from-group`: Removes a user from a group with OKTA_GROUP type.
- `okta-get-groups`: Returns all user groups associated with a specified user.
- `okta-verify-push-factor`: Enrolls and verifies a push factor for the specified user.
- `okta-verify-mfa-status`: Verifies the status of a push factor challenge.
- `okta-search`: Searches for Okta users.
- `okta-get-user`: Fetches information for a single user. You must enter one or more parameters for the command to run.


## Okta ASA

**Type:** integration  
**Product:** Okta ASA  

Okta Advanced Server Access integration for Cortex XSIAM allows you to fetch logs of a wide range of configuration, enrollment, authentication, and authorization events that occur within the product and on your servers

**Commands:**

- `okta-asa-get-events`: Gets events from Okta ASA.


## Okta IAM

**Type:** integration  
**Product:** Okta  

Integrate with Okta's Identity Access Management service to execute CRUD operations to employee lifecycle processes. This integration was integrated and tested with version v1 of the Okta integration. For more information, refer to the Identity Lifecycle Management article

**Commands:**

- `iam-create-user`: Creates a user.
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Disable an active user.
- `okta-get-app-user-assignment`: Gets a specific user assignment for an application by id.
- `okta-iam-list-applications`: Returns a list of Okta applications data.
- `okta-iam-list-user-applications`: Returns a list of Okta applications data.
- `okta-iam-get-configuration`: Gets the IAM configuration data from the integration context.
- `okta-iam-set-configuration`: Updates IAM configuration data in the integration context.
- `iam-get-group`: Retrieves the group information, including its members.
- `okta-get-logs`: Gets logs by providing optional filters.


## Okta IAM (Standard Connector)

**Type:** integration  
**Product:** Okta (Standard Connector)  

Integrate with Okta's Identity Access Management service to execute CRUD operations to employee lifecycle processes. This integration was integrated and tested with version v1 of the Okta integration. For more information, refer to the Identity Lifecycle Management article

**Commands:**

- `iam-create-user`: Creates a user.
- `iam-update-user`: Updates an existing user with the data passed in the user-profile argument.
- `iam-get-user`: Retrieves a single user resource.
- `iam-disable-user`: Disable an active user.
- `okta-get-app-user-assignment`: Gets a specific user assignment for an application by id.
- `okta-iam-list-applications`: Returns a list of Okta applications data.
- `okta-iam-list-user-applications`: Returns a list of Okta applications data.
- `okta-iam-get-configuration`: Gets the IAM configuration data from the integration context.
- `okta-iam-set-configuration`: Updates IAM configuration data in the integration context.
- `iam-get-group`: Retrieves the group information, including its members.
- `okta-get-logs`: Gets logs by providing optional filters.


## Okta v2

**Type:** integration  
**Product:** Okta  

Integration with Okta's cloud-based identity management service

**Commands:**

- `okta-unlock-user`: Unlocks a single user.
- `okta-deactivate-user`: Deactivates a single user.
- `okta-activate-user`: Activates a single user.
- `okta-suspend-user`: Suspends a single user. This operation can only be performed on users with an ACTIVE status. After the porcess is completed, the user's status is SUSPENDED.
- `okta-unsuspend-user`: Returns a single user to ACTIVE status. This operation can only be performed on users that have a SUSPENDED status.
- `okta-get-user-factors`: Returns all the enrolled factors for the specified user.
- `okta-reset-factor`: Un-enrolls an existing factor for the specified user. This enables the user to enroll a new factor.
- `okta-set-password`: Sets passwords without validating existing user credentials.
- `okta-add-to-group`: Adds a user to a group with OKTA_GROUP type.
- `okta-remove-from-group`: Removes a user from a group with OKTA_GROUP type.
- `okta-get-groups`: Returns all user groups associated with a specified user.
- `okta-verify-push-factor`: Enrolls and verifies a push factor for the specified user.
- `okta-verify-mfa-status`: Verifies the status of a push factor challenge.
- `okta-search`: Searches for Okta users.
- `okta-get-user`: Fetches information for a single user. You must enter one or more parameters for the command to run.


## PingOne

**Type:** integration  
**Product:** PingIdentity  

Integrates with the PingOne Management API to unlock, create, delete and update users

**Commands:**

- `pingone-unlock-user`: Unlock a user's account.
- `pingone-deactivate-user`: Deactivate a user's account.
- `pingone-activate-user`: Activate a user's account.
- `pingone-set-password`: Sets a user's password. Further password details available here: https://apidocs.pingidentity.com/pingone/platform/v1/api/#put-update-password-self
- `pingone-password-force-change`: Force a user's password change on next login.
- `pingone-read-password-state`: Read a user's password state.
- `pingone-add-to-group`: Add user to the group. One of the following has to be given username or userId and groupName or groupId.
- `pingone-remove-from-group`: Remove user from the group. One of the following has to be given username or userId and groupName or groupId.
- `pingone-get-groups`: Returns user's group memberships.
- `pingone-get-user`: Returns a PingOne user. One of the following has to be given username or userId.
- `pingone-create-user`: Create a PingOne user.
- `pingone-update-user`: Update a PingOne user.
- `pingone-delete-user`: Delete a PingOne user. One of the following has to be given username or userId.


## SailPoint IdentityIQ

**Type:** integration  
**Product:** SailPoint IdentityIQ  

SailPoint IdentityIQ context pack enables platform customers to utilize the deep, enriched contextual data in the SailPoint predictive identity platform to better drive identity-aware security practices. This integration was integrated and tested with version 8.1 of SailPoint IdentityIQ. Supported the platform.0.0 and later

**Commands:**

- `identityiq-search-identities`: Search identities by search/filter parameters (id, email, risk & active) using IdentityIQ SCIM API's.
- `identityiq-get-policyviolations`: Fetch policy violation by id or all policy violations using IdentityIQ SCIM API's.
- `identityiq-get-taskresults`: Fetch task result by id or all task results using IdentityIQ SCIM API's.
- `identityiq-get-accounts`: Fetch accounts by search/filter parameters (id, display_name, last_refresh, native_identity, last_target_agg, identity_name & application_name) using IdentityIQ
- `identityiq-disable-account`: Disable account's active status by id using IdentityIQ SCIM API's.
- `identityiq-enable-account`: Enable account's active status by id using IdentityIQ SCIM API's.
- `identityiq-delete-account`: Delete account by id using IdentityIQ SCIM API's.
- `identitytiq-get-launched-workflows`: Fetch launched workflow by id or all launched workflows using IdentityIQ SCIM API's.
- `identityiq-get-roles`: Fetch role by id or all roles using IdentityIQ SCIM API's.
- `identityiq-get-entitlements`: Fetch entitlement by id or all entitlements using IdentityIQ SCIM API's.
- `identityiq-get-alerts`: Fetch alert by id or all alerts using IdentityIQ SCIM API's.
- `identityiq-create-alert`: Create an alert using IdentityIQ SCIM API's.


## SailPoint IdentityIQ Disable User Account Access

**Type:** playbook  
**Product:** SailPoint IdentityIQ  

Checks if the risk score of an identity exceeds a set threshold of 500 and disables the accounts

**Inputs:**

- `email`: Email of the identity.


## SailPoint IdentityNow

**Type:** integration  
**Product:** SailPoint IdentityNow  

SailPoint IdentityNow This integration was integrated and tested with SailPoint IdentityNow

**Commands:**

- `identitynow-search-identities`: Search for identity(identities) using elastic search query used by IdentityNow Search Engine.
- `identitynow-get-accounts`: Get accounts by search/filter parameters (id, name, native_identity).
- `identitynow-get-accountactivities`: Get account activities by search/filter parameters (requested_for, requested_by, regarding_identity, type).
- `identitynow-search-accessprofiles`: Search for access profile(s) using elastic search query used by IdentityNow Search Engine.
- `identitynow-search-roles`: Search for role(s) using elastic search query used by IdentityNow Search Engine.
- `identitynow-search-entitlements`: Search for entitlement(s) using elastic search query used by IdentityNow Search Engine.
- `identitynow-search-events`: Search for event(s) using elastic search query used by IdentityNow Search Engine.
- `identitynow-request-grant`: Grant access request for a single object(access profile or role) for a single user.
- `identitynow-request-revoke`: Revoke access request for a single object(access profile or role) for a single user.

## CertificateManagerSaaSApiModule

**Type:** script  
**Product:** CyberArk

Provides shared CyberArk Certificate Manager SaaS code, which the Certificate Manager SaaS and Next-Gen Trust Security integrations reuse. The code includes parsing, GraphQL queries, paging, commands, and the expiry fetch.

