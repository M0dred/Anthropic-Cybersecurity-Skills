# Integration and Automation Catalog - Api Security

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## APIVoid

**Type:** integration  
**Product:** APIVoid  

APIVoid wraps up a number of services such as ipvoid & urlvoid

**Commands:**

- `apivoid-ip`: Returns the reputation and extended context of the IP.
- `apivoid-domain`: Returns the reputation of the domain.
- `apivoid-url`: Returns the reputation of the URL.
- `ip`: Returns the reputation of the IP.
- `domain`: Returns the reputation of the domain.
- `url`: Returns the reputation of the URL.
- `apivoid-dns-lookup`: Gets DNS records of a host.
- `apivoid-ssl-info`: Get useful SSL information from a remote host
- `apivoid-email-verify`: Checks if an email address is disposable, if it has MX records, and more.
- `apivoid-threatlog`: Check if a website is present on ThreatLog database
- `apivoid-parked-domain`: Detect if a domain (i.e google.com) is actually parked
- `apivoid-domain-age`: Get the registration date of a domain and the domain age in days
- `apivoid-url-to-image`: Capture a high-quality screenshot of any website or URL
- `apivoid-url-to-pdf`: Convert an URL info high-quality and printable PDF document
- `apivoid-url-to-html`: Get the body of an html page after javascript has been executed


## Core REST API

**Type:** integration  
**Product:** Cortex REST API  
**Commands:**

- `core-api-post`: send HTTP POST request
- `core-api-get`: send HTTP GET requests
- `core-api-put`: send HTTP PUT request
- `core-api-patch`: send HTTP PATCH request
- `core-api-delete`: send HTTP DELETE request
- `core-api-download`: Download files from core server
- `core-api-multipart`: Send HTTP Multipart request to upload files to Core server
- `core-delete-incidents`: Delete Core incidents
- `core-api-install-packs`: Upload packs to Core server from url or the marketplace.
- `core-api-file-upload`: Upload to the incident a file that the user provided according to the entry_id or the content of the file.
- `core-api-file-delete`: Delete a war room (investigation) file entry.
- `core-api-file-attachment-delete`: Delete a file attachment from an incident — specifically from the incident’s file attachments (not from the war room).
- `core-api-file-check`: Check if the file exists in the platform.


## Google Apigee

**Type:** integration  
**Product:** Google Apigee Edge  

Apigee is Google Cloud's native API management platform that can be used to build, manage, and secure APIs — for any use case, environment, or scale. Apigee offers high performance API proxies to create a consistent, reliable interface for your backend services. The proxy layer gives you granular control over security, rate limiting, quotas, analytics, and more for all of your services. Apigee supports REST, gRPC, SOAP, and GraphQL, providing the flexibility to implement any API architectural style. This integration was integrated and tested with version v1 of Google Apigee

**Commands:**

- `google-apigee-get-events`: Gets logs from Google Apigee.


## Illumio Core

**Type:** integration  
**Product:** Illumio Rapid Ransomware Containment  

Connects to Illumio Core APIs to perform investigative and restorative actions. This integration was integrated and tested with version 1.1.2 of Illumio Python SDK

**Commands:**

- `illumio-traffic-analysis`: Retrieves traffic flow of a particular port & protocol within the specified time range based on policy decisions.
- `illumio-virtual-service-create`: Creates a virtual service for a particular port & protocol, which can be further binded to workloads. Until provisioned with the 'illumio-object-provision' comm
- `illumio-service-binding-create`: Binds the existing or a new virtual service to the workloads.
- `illumio-object-provision`: A utility method for provisioning policy objects from draft to active state. Policy objects only affect the network once they've been provisioned.
- `illumio-workload-get`: Retrieves the details of the workload based on the provided workload's HREF.
- `illumio-workloads-list`: Retrieves the list of workloads based on the provided filters.
- `illumio-enforcement-boundary-create`: Creates an enforcement boundary for a particular port/protocol. After completion of this command, provisioning will be done using the "illumio-object-provision"
- `illumio-enforcement-mode-update`: Update the Enforcement Mode for one or more workloads.
- `illumio-ip-list-get`: Retrieves the list of IPs based on the name of the IP list.
- `illumio-ip-lists-get`: Retrieves the list of IPs based on the query parameters.
- `illumio-ruleset-create`: Creates a ruleset with a unique name. Until provisioned with the 'illumio-object-provision' command, this object will remain in a draft state.
- `illumio-rule-create`: Creates & assigns rules to a particular ruleset. Added or updated Rules will remain in draft state until their containing Rule Set is provisioned using the "ill


## IP-API

**Type:** integration  
**Product:** IP-API  

This integration will enrich IP addresses from IP-API with data about the geolocation, as well as a determination of the IP address being associated with a mobile device, hosting or proxy. Revers DNS is also returned. This service is available for free (with a throttle) - or paid. This integration was integrated and tested with IP-API

**Commands:**

- `ip`: Return IP information


## Microsoft Graph API

**Type:** integration  
**Product:** Microsoft Graph API  

Use the Microsoft Graph API integration to interact with Microsoft APIs that do not have dedicated integrations in the platform, for example, Mail Single-User, etc. Note: In this documentation, we will use the Application resource type as an example

**Commands:**

- `msgraph-api-auth-start`: Run this command to start the authorization process and follow the instructions in the command results.
- `msgraph-api-auth-complete`: Run this command to complete the authorization process. Should be used after running the msgraph-api-auth-start command.
- `msgraph-api-test`: Tests connectivity to Microsoft.
- `msgraph-api-request`: Run a Microsoft Graph API query.
- `msgraph-api-auth-reset`: Run this command if for some reason you need to rerun the authentication process.
- `msgraph-api-generate-login-url`: Generate the login URL used for Authorization code flow.


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

- `spur-context-api-enrich`: Enrich indicators using the Spur Context API.
- `ip`: IP reputation command using the Spur Context API.


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

