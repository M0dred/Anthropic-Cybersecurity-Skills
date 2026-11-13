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

- `cyberark-aim-list-credentials`: 


## CyberArk Certificate Manager

**Type:** integration  
**Product:** CyberArk Certificate Manager Self-Hosted  

Retrieves information about certificates stored in Venafi

**Commands:**

- `venafi-get-certificates`: 
- `venafi-get-certificate-details`: 


## CyberArk EPM SOC Response

**Type:** integration  
**Product:** CyberArk Endpoint Privilege Manager  

Use the CyberArk EPM integration to activate and deactivate CyberArk EPM risk plans for specific endpoints. This integration was integrated and tested with the CyberArk EPM API

**Commands:**

- `cyberarkepm-activate-risk-plan`: 
- `cyberarkepm-deactivate-risk-plan`: 

**Inputs:**

- `endpoint_name`: Hostname of target endpoint.
- `logged_in_user`: Logged in user name of target endpoint.


## CyberArk Identity Security Platform

**Type:** integration  
**Product:** CyberArk  
**Commands:**

- `cyberark-isp-get-events`: 


## CyberArk PAM

**Type:** integration  
**Product:** CyberArk  

Use the CyberArk Privileged Access Management (PAM) solution to manage users, safes, vaults, and accounts from the platform

**Commands:**

- `cyberark-pas-user-add`: 
- `cyberark-pas-user-update`: 
- `cyberark-pas-user-delete`: 
- `cyberark-pas-users-list`: 
- `cyberark-pas-user-activate`: 
- `cyberark-pas-safes-list`: 
- `cyberark-pas-safe-get-by-name`: 
- `cyberark-pas-safe-add`: 
- `cyberark-pas-safe-update`: 
- `cyberark-pas-safe-delete`: 
- `cyberark-pas-safe-members-list`: 
- `cyberark-pas-safe-member-add`: 
- `cyberark-pas-safe-member-update`: 
- `cyberark-pas-account-add`: 
- `cyberark-pas-account-update`: 


## Entra ID Identity And Access

**Type:** integration  
**Product:** Microsoft Graph Identity and Access  

Use the Entra ID Identity And Access (formerly Azure Active Directory Identity And Access) integration to manage roles and members

**Commands:**

- `msgraph-identity-auth-start`: 
- `msgraph-identity-auth-complete`: 
- `msgraph-identity-auth-reset`: 
- `msgraph-identity-auth-test`: 
- `msgraph-identity-directory-roles-list`: 
- `msgraph-identity-directory-role-activate`: 
- `msgraph-identity-directory-role-members-list`: 
- `msgraph-identity-directory-role-member-add`: 
- `msgraph-identity-directory-role-member-remove`: 
- `msgraph-identity-ip-named-locations-create`: 
- `msgraph-identity-ip-named-locations-get`: 
- `msgraph-identity-ip-named-locations-delete`: 
- `msgraph-identity-ip-named-locations-update`: 
- `msgraph-identity-ip-named-locations-update`: 
- `msgraph-identity-protection-risks-list`: 


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

- `okta-unlock-user`: 


## Okta ASA

**Type:** integration  
**Product:** Okta ASA  

Okta Advanced Server Access integration for Cortex XSIAM allows you to fetch logs of a wide range of configuration, enrollment, authentication, and authorization events that occur within the product and on your servers

**Commands:**

- `okta-asa-get-events`: 


## Okta IAM

**Type:** integration  
**Product:** Okta  

Integrate with Okta's Identity Access Management service to execute CRUD operations to employee lifecycle processes. This integration was integrated and tested with version v1 of the Okta integration. For more information, refer to the Identity Lifecycle Management article

**Commands:**

- `iam-create-user`: 
- `iam-update-user`: 
- `iam-get-user`: 
- `iam-disable-user`: 
- `okta-get-assigned-user-for-app`: 
- `okta-list-applications`: 
- `okta-list-user-applications`: 
- `okta-iam-get-configuration`: 
- `okta-iam-set-configuration`: 
- `iam-get-group`: 
- `okta-get-logs`: 


## Okta IAM (Standard Connector)

**Type:** integration  
**Product:** Okta (Standard Connector)  

Integrate with Okta's Identity Access Management service to execute CRUD operations to employee lifecycle processes. This integration was integrated and tested with version v1 of the Okta integration. For more information, refer to the Identity Lifecycle Management article

**Commands:**

- `iam-create-user`: 
- `iam-update-user`: 
- `iam-get-user`: 
- `iam-disable-user`: 
- `okta-get-assigned-user-for-app`: 
- `okta-list-applications`: 
- `okta-list-user-applications`: 
- `okta-iam-get-configuration`: 
- `okta-iam-set-configuration`: 
- `iam-get-group`: 
- `okta-get-logs`: 


## Okta v2

**Type:** integration  
**Product:** Okta  

Integration with Okta's cloud-based identity management service

**Commands:**

- `okta-unlock-user`: 


## PingOne

**Type:** integration  
**Product:** PingIdentity  

Integrates with the PingOne Management API to unlock, create, delete and update users

**Commands:**

- `pingone-unlock-user`: 
- `pingone-deactivate-user`: 
- `pingone-activate-user`: 
- `pingone-set-password`: 
- `pingone-password-force-change`: 
- `pingone-read-password-state`: 
- `pingone-add-to-group`: 
- `pingone-remove-from-group`: 
- `pingone-get-groups`: 
- `pingone-get-user`: 
- `pingone-create-user`: 
- `pingone-update-user`: 
- `pingone-delete-user`: 


## SailPoint IdentityIQ

**Type:** integration  
**Product:** SailPoint IdentityIQ  

SailPoint IdentityIQ context pack enables platform customers to utilize the deep, enriched contextual data in the SailPoint predictive identity platform to better drive identity-aware security practices. This integration was integrated and tested with version 8.1 of SailPoint IdentityIQ. Supported the platform.0.0 and later

**Commands:**

- `identityiq-search-identities`: 
- `identityiq-get-policyviolations`: 
- `identityiq-get-taskresults`: 
- `identityiq-get-accounts`: 
- `identityiq-disable-account`: 
- `identityiq-enable-account`: 
- `identityiq-delete-account`: 
- `identitytiq-get-launched-workflows`: 
- `identityiq-get-roles`: 
- `identityiq-get-entitlements`: 
- `identityiq-get-alerts`: 
- `identityiq-create-alert`: 


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

- `identitynow-search-identities`: 
- `identitynow-get-accounts`: 
- `identitynow-get-accountactivities`: 
- `identitynow-search-accessprofiles`: 
- `identitynow-search-roles`: 
- `identitynow-search-entitlements`: 
- `identitynow-search-events`: 
- `identitynow-request-grant`: 
- `identitynow-request-revoke`: 

