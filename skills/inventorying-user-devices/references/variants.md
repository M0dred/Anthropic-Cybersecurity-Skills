# Vendor Variants - Inventorying User Devices

Vendor-specific implementations, feeds, and collectors for this procedure.


## Get User Devices by Email Address - Generic

**Product:** Common Playbooks

**Kind:** playbook

This playbook retrieves information on all of the associated user devices, based on the user email. In order to get a generic output, the following information on all of the retrieved devices will be saved under the UserDevices context key: Note that not all of the supported integrations will be able to retrieve this information. Supported integrations

**Inputs:**

- `UserEmail`: The email address of the user.
- `GsuiteCustomerID`: If using Google Workspace, a customer ID is needed.
- `CustomADAttribute`: A custom Active Directory attribute.In case there is a custom attribute in Active Directory which stores the name of the computer assigned to the user in the user object, it would 

**Dependencies:**

- Integrations: Microsoft Graph API, jamf v2, ServiceNow v2
- Scripts: IsIntegrationAvailable, SetMultipleValues, SetAndHandleEmpty
- Commands: ad-get-user, servicenow-query-users, gsuite-mobiledevice-list, jamf-get-mobile-device-by-id, jamf-get-computer-by-match, jamf-get-mobile-device-by-match, msgraph-api-request, jamf-get-computer-by-id

## Get User Devices by Username - Generic

**Product:** Common Playbooks

**Kind:** playbook

This playbook retrieves information on all of the associated user devices, based on the user's username. In order to get a generic output, the following information on all of the retrieved devices will be saved under the UserDevices context key: Note that not all of the supported integrations will be able to retrieve this information. Supported integrations

**Inputs:**

- `Username`: The username of the user.
- `GsuiteCustomerID`: If using Google Workspace, a customer ID is needed.
- `CustomADAttribute`: A custom Active Directory attribute.In case there is a custom attribute in Active Directory which stores the name of the computer assigned to the user in the user object, it would 

**Dependencies:**

- Integrations: ServiceNow v2, Cortex XDR - IR, jamf v2, Microsoft Defender Advanced Threat Protection
- Scripts: SetAndHandleEmpty, SetMultipleValues, IsIntegrationAvailable
- Commands: gsuite-mobiledevice-list, jamf-get-mobile-device-by-match, ad-get-user, microsoft-atp-get-user-machines, servicenow-query-computers, core-get-endpoints, jamf-get-mobile-device-by-id, servicenow-query-users

## Get User Devices by Email Address - Generic

**Product:** Common Playbooks

**Kind:** playbook

This playbook retrieves information on all of the associated user devices, based on the user email. In order to get a generic output, the following information on all of the retrieved devices will be saved under the UserDevices context key: Note that not all of the supported integrations will be able to retrieve this information. Supported integrations

**Inputs:**

- `UserEmail`: The email address of the user.
- `GsuiteCustomerID`: If using Google Workspace, a customer ID is needed.
- `CustomADAttribute`: A custom Active Directory attribute.In case there is a custom attribute in Active Directory which stores the name of the computer assigned to the user in the user object, it would 

**Dependencies:**

- Integrations: Microsoft Graph API, jamf v2, ServiceNow v2
- Scripts: IsIntegrationAvailable, SetMultipleValues, SetAndHandleEmpty
- Commands: ad-get-user, servicenow-query-users, gsuite-mobiledevice-list, jamf-get-mobile-device-by-id, jamf-get-computer-by-match, jamf-get-mobile-device-by-match, msgraph-api-request, jamf-get-computer-by-id

## Get User Devices by Username - Generic

**Product:** Common Playbooks

**Kind:** playbook

This playbook retrieves information on all of the associated user devices, based on the user's username. In order to get a generic output, the following information on all of the retrieved devices will be saved under the UserDevices context key: Note that not all of the supported integrations will be able to retrieve this information. Supported integrations

**Inputs:**

- `Username`: The username of the user.
- `GsuiteCustomerID`: If using Google Workspace, a customer ID is needed.
- `CustomADAttribute`: A custom Active Directory attribute.In case there is a custom attribute in Active Directory which stores the name of the computer assigned to the user in the user object, it would 

**Dependencies:**

- Integrations: ServiceNow v2, Cortex XDR - IR, jamf v2, Microsoft Defender Advanced Threat Protection
- Scripts: SetAndHandleEmpty, SetMultipleValues, IsIntegrationAvailable
- Commands: gsuite-mobiledevice-list, jamf-get-mobile-device-by-match, ad-get-user, microsoft-atp-get-user-machines, servicenow-query-computers, core-get-endpoints, jamf-get-mobile-device-by-id, servicenow-query-users

