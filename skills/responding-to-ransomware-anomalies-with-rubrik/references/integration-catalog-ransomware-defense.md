# Integration and Automation Catalog - Ransomware Defense

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## Druva Ransomware Response

**Type:** integration  
**Product:** Druva  

Druva Ransomware Response Integration provides ransomware protection for endpoints, SaaS applications and data center workloads for Druva Ransomware Recovery customers

**Commands:**

- `druva-find-device`: Finds device information for a specific hostname.
- `druva-list-quarantine-ranges`: Lists all quarantine ranges in your environment.
- `druva-quarantine-resource`: Quarantines a resource.
- `druva-delete-quarantine-range`: Deletes a quarantine range.
- `druva-view-quarantine-range`: View details of the quarantine range.
- `druva-update-quarantine-range`: Updates an existing quarantine range of a resource.
- `druva-list-quarantine-snapshots`: List all quarantine snapshots for a quarantine range.
- `druva-delete-quarantined-snapshot`: Deletes a quarantined Snapshot. Snapshots that are deleted cannot be recovered.
- `druva-endpoint-search-file-hash`: Searches a file using the SHA1 checksum.
- `druva-endpoint-initiate-restore`: Restores data to a replacement device and deletes a quarantined Snapshot. This command restores your endpoint data from a day prior to the snapshot. Any changes
- `druva-endpoint-check-restore-status`: Checks the restore job status of the endpoint.
- `druva-endpoint-decommission`: Wipes remotely an infected Endpoint Resource and deletes a quarantined Snapshot. This command remote wipes data from the endpoint. This action cannot be undone.
- `druva-find-user`: Finds user information for a specific username.
- `druva-find-userDevice`: Finds device information for a specific user.
- `druva-find-sharePointSites`: Find all share point resources with given user name


## RansomwareDataEncryptionStatus

**Type:** script  
**Product:** Ransomware  

A Widget script - checks for the data encryption status in post ransomware investigation playbook and layout


## RansomwareHostWidget

**Type:** script  
**Product:** Ransomware  

Entry widget that returns the number of affectefd hosts in a Post Intrusion Ransomware incident


## RiskSenseGetRansomewareCVEScript

**Type:** script  
**Product:** RiskSense  

This script is a helper script for the Ransomware Exposure - RiskSense playbook and retrieves information of CVEs and trending CVEs from host finding details

**Inputs:**

- `trending`: Trending is defined by RiskSense as vulnerabilities that are being actively abused by attackers in the wild based on activity in hacker foru


## Veeam - Compare Entra ID Items

**Type:** playbook  
**Product:** Veeam App  

Compares Microsoft Entra ID item properties between a restore point and production

**Inputs:**

- `Instance`: 


## Veeam - Find Entra ID User

**Type:** playbook  
**Product:** Veeam App  

Checks if a user exists in a Microsoft Entra ID tenant backup


## Veeam - Resolve Triggered Alarms

**Type:** playbook  
**Product:** Veeam App  

Resolves Veeam ONE triggered alarms

**Inputs:**

- `TriggeredAlarmId`: 
- `Instance`: 


## Veeam - Start Configuration Backup

**Type:** playbook  
**Product:** Veeam App  

Starts configuration backup job for the Veeam Backup & Replication instance

**Inputs:**

- `Instance`: 


## Veeam - Start Disk Publishing

**Type:** playbook  
**Product:** Veeam App  

Starts a disk publishing session for a specific restore point

**Inputs:**

- `Instance`: 
- `backupObjectId`: 
- `Indicator Query`: Indicators matching the indicator query will be used as playbook input


## Veeam - Start Quick Backup

**Type:** playbook  
**Product:** Veeam App  

Starts a Quick Backup session for a specific virtual machine

**Inputs:**

- `Instance`: 
- `backupObjectId`: 


## Veeam - Stop Disk Publishing

**Type:** playbook  
**Product:** Veeam App  

Stops an active disk publishing session

**Inputs:**

- `Instance`: 
- `mountId`: 
- `Indicator Query`: Indicators matching the indicator query will be used as playbook input


## Veeam Backup & Replication REST API

**Type:** integration  
**Product:** Veeam App  

Veeam Backup & Replication REST API allows you to query information about Veeam Backup & Replication entities and perform operations with these entities using HTTP requests and standard HTTP methods. This integration was integrated and tested with version 1.1-rev2 of VBR REST API

**Commands:**

- `veeam-vbr-create-malware-event`: Create Malware Event.
- `veeam-vbr-get-malware-events`: Get All Malware Events
- `veeam-vbr-get-repository-states`: Get All Repository States
- `veeam-vbr-get-restore-points`: Get All Restore Points
- `veeam-vbr-get-backup-object`: 
- `veeam-vbr-get-backup-object`: Get Backup Object.
- `veeam-vbr-get-inventory-objects`: Get Inventory Objects
- `veeam-vbr-get-session`: Get Session
- `veeam-vbr-start-configuration-backup`: Start Configuration Backup
- `veeam-vbr-start-instant-recovery-customized`: Start Customized VM Instant Recovery
- `veeam-vbr-start-instant-recovery`: Start VM Instant Recovery to Original Location
- `veeam-vbr-mount-entra-id-tenant`: Mounts a Microsoft Entra ID tenant from its backup and starts a mount session required for restore.
- `veeam-vbr-start-security-analyzer`: Starts the Security & Compliance Analyzer scan. The command creates a new session and returns its details.
- `veeam-vbr-start-malware-backup-scan`: Starts a Scan Backup session.
- `veeam-vbr-start-disk-publishing`: Start Disk Publishing. Publishes disk content from a restore point via the Data Integration API using ISCSITarget mount mode.


## Veeam ONE REST API

**Type:** integration  
**Product:** Veeam App  

Veeam ONE REST API allows you to query information about Veeam ONE entities and perform operations with these entities using HTTP requests and standard HTTP methods. This integration was integrated and tested with version 12.2.0 of Veeam ONE

**Commands:**

- `veeam-vone-get-triggered-alarms`: Get All Triggered Alarms.
- `veeam-vone-resolve-triggered-alarms`: Resolve Triggered Alarms.

