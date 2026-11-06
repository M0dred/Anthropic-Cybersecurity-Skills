# Integration and Automation Catalog - Api Security

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## APIVoid

**Type:** integration  
**Product:** APIVoid  

APIVoid wraps up a number of services such as ipvoid & urlvoid

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


## Core REST API

**Type:** integration  
**Product:** Cortex REST API  
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


## DemistoCreateList

**Type:** script  
**Product:** Cortex REST API  

Creates a new list

**Inputs:**

- `listName`: The name of the list to create.
- `listData`: The initial data of the list.


## DemistoGetIncidentTasksByState

**Type:** script  
**Product:** Cortex REST API  

Gets all tasks for a specific incident by the given state

**Inputs:**

- `incidentId`: The Incident ID to get tasks from.
- `states`: The comma-separated list of states. Can be, "New", "InProgress", "Completed", "Waiting", "Error", "Skipped", "Blocked". You can also leave t


## DemistoLeaveAllInvestigations

**Type:** script  
**Product:** Cortex REST API  

Leaves all investigations that the user is part of (clears out the incidents in the left pane). The incidents owner by the user will remain in the left pane. This requires Core REST API integration to be configured for the server


## DemistoLinkIncidents

**Type:** script  
**Product:** Cortex REST API  

Links two or more incidents

**Inputs:**

- `masterID`: The incident ID used to link to other incidents.
- `otherIDs`: The incident IDs to link.
- `unlink`: Whether to unlink incidents. The default is "no".


## DemistoLogsBundle

**Type:** script  
**Product:** Cortex REST API  

Gets the the platform


## DemistoSendInvite

**Type:** script  
**Product:** Cortex REST API  

Sends an invitation to join the platform

**Inputs:**

- `email`: The email of the user being invited.
- `roles`: The roles of the invited user.


## DemistoUploadFile

**Type:** script  
**Product:** Cortex REST API  

Copies a file from an incident to a specified incident. The file is recorded as an entry in the specified incident's War Room

**Inputs:**

- `entryID`: The file entry ID.
- `incidentID`: The incident ID to upload the file to.
- `body`: Request body


## DemistoUploadFileV2

**Type:** script  
**Product:** Cortex REST API  

Copies a file from this incident to the specified incident. The file is recorded as an entry in the specified incident’s War Room

**Inputs:**

- `entryID`: File entry ID
- `incidentID`: Incident ID to upload the file to
- `body`: Request body
- `target`: Where to upload the file- Available options are:- `war room entry`: the file will be uploaded as war room entry.- `incident attachment`: the


## Google Apigee

**Type:** integration  
**Product:** Google Apigee Edge  

Apigee is Google Cloud's native API management platform that can be used to build, manage, and secure APIs — for any use case, environment, or scale. Apigee offers high performance API proxies to create a consistent, reliable interface for your backend services. The proxy layer gives you granular control over security, rate limiting, quotas, analytics, and more for all of your services. Apigee supports REST, gRPC, SOAP, and GraphQL, providing the flexibility to implement any API architectural style. This integration was integrated and tested with version v1 of Google Apigee

**Commands:**

- `None`: 


## Illumio Core

**Type:** integration  
**Product:** Illumio Rapid Ransomware Containment  

Connects to Illumio Core APIs to perform investigative and restorative actions. This integration was integrated and tested with version 1.1.2 of Illumio Python SDK

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


## IP-API

**Type:** integration  
**Product:** IP-API  

This integration will enrich IP addresses from IP-API with data about the geolocation, as well as a determination of the IP address being associated with a mobile device, hosting or proxy. Revers DNS is also returned. This service is available for free (with a throttle) - or paid. This integration was integrated and tested with IP-API

**Commands:**

- `None`: 


## Microsoft Graph API

**Type:** integration  
**Product:** Microsoft Graph API  

Use the Microsoft Graph API integration to interact with Microsoft APIs that do not have dedicated integrations in the platform, for example, Mail Single-User, etc. Note: In this documentation, we will use the Application resource type as an example

**Commands:**

- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 
- `None`: 


## RapidBreachResponse-CompletedTasksCount-Widget

**Type:** script  
**Product:** Rapid Breach Response  

Rapid Breach Response dynamic section, will show the updated number of completed tasks


## RapidBreachResponse-EradicationTasksCount-Widget

**Type:** script  
**Product:** Rapid Breach Response  

Rapid Breach Response dynamic section, will show the updated number of eradication tasks


## RapidBreachResponse-MitigationTasksCount-Widget

**Type:** script  
**Product:** Rapid Breach Response  

Rapid Breach Response dynamic section, will show the updated number of mitigation tasks


## RapidBreachResponse-RemainingTasksCount-Widget

**Type:** script  
**Product:** Rapid Breach Response  

Rapid Breach Response dynamic section, will show the updated number of remaining tasks


## RapidBreachResponse-RemediationTasksCount-Widget

**Type:** script  
**Product:** Rapid Breach Response  

Rapid Breach Response dynamic section, will show the updated number of remediation tasks


## RapidBreachResponse-TotalIndicatorCount-Widget

**Type:** script  
**Product:** Rapid Breach Response  

Rapid Breach Response dynamic section, will show the updated number of indicators found


## RapidBreachResponse-TotalTasksCount-Widget

**Type:** script  
**Product:** Rapid Breach Response  

Rapid Breach Response dynamic section, will show the updated number of tasks to complete


## RapidBreachResponseParseBlog

**Type:** script  
**Product:** Rapid Breach Response  

Parse Volexity request blog

**Inputs:**

- `url`: The requested URL


## SpurContextAPI

**Type:** integration  
**Product:** Spur Context API  

Enrich indicators using the Spur Context API. This integration was integrated and tested with version 2 of SpurContextAPI

**Commands:**

- `None`: 
- `None`: 


## Update enforcement mode - Illumio

**Type:** playbook  
**Product:** Illumio Rapid Ransomware Containment  

Update the enforcement mode for one or more workloads


## UploadFile

**Type:** script  
**Product:** Cortex REST API  

Copies a file from this incident to the specified incident. The file is recorded as an entry in the specified incident’s War Room

**Inputs:**

- `entryID`: File entry ID.
- `incidentID`: Incident ID to upload the file to.
- `body`: Request body.
- `target`: Where to upload the file- Available options are:- `war room entry`: the file will be uploaded as War Room entry.- `incident attachment`: the
- `using`: Integration instance to use to run the command.

