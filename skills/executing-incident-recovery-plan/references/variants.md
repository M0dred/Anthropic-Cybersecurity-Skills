# Vendor Variants - Executing Incident Recovery Plan

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Rubrik Ransomware Discovery and VM Recovery - Rubrik Polaris

**Product:** Rubrik Security Cloud

Use this playbook to recover a virtual machine using the "RubrikPolaris" integration by either exporting or live-mounting a backup snapshot. This playbook also creates tickets on ServiceNow using "ServiceNow v2" integration. Supported integrations

**Inputs:**

- `ObjectId`: Object ID of the incident.
- `ClusterId`: Cluster ID of the incident.

**Dependencies:**

- Sub-playbooks: Rubrik Poll Async Result - Rubrik Polaris, Rubrik IOC Scan - Rubrik Polaris
- Integrations: RubrikPolaris, ServiceNow v2
- Scripts: http, Set, PrintErrorEntry, SetAndHandleEmpty, Print
- Commands: servicenow-create-ticket, rubrik-gps-vm-livemount, rubrik-gps-vm-export, rubrik-gps-vm-datastore-list, servicenow-update-ticket, rubrik-gps-vm-host-list, rubrik-gps-vm-snapshot-create, rubrik-polaris-vm-object-metadata-get


## Veeam - Start Instant Hyper-V VM Recovery Automatically

**Product:** Veeam App

Starts Instant VM Recovery for Microsoft Hyper-V with automatic configuration

**Inputs:**

- `Instance`: 
- `backupObjectId`: 

**Dependencies:**

- Sub-playbooks: GenericPolling, Veeam - Start Instant Hyper-V VM Recovery Manually
- Integrations: VBR REST API
- Scripts: DeleteContext, GetLatestCleanRestorePoint, GetRestoredVmName
- Commands: veeam-vbr-get-backup-object, veeam-vbr-get-inventory-objects, veeam-vbr-get-restore-points, veeam-vbr-get-session, veeam-vbr-get-session-logs, veeam-vbr-start-instant-recovery-hyperv-vm-customized


## Veeam - Start Instant Hyper-V VM Recovery Manually

**Product:** Veeam App

Starts Instant VM Recovery for Microsoft Hyper-V with manual configuration

**Inputs:**

- `Instance`: 
- `backupObjectId`: 

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: VBR REST API
- Scripts: DeleteContext, GetLatestCleanRestorePoint, GetRestoredVmName
- Commands: veeam-vbr-get-backup-object, veeam-vbr-get-restore-points, veeam-vbr-get-session, veeam-vbr-get-session-logs, veeam-vbr-start-instant-recovery-hyperv-vm-customized


## Veeam - Start Instant VM Recovery Manually

**Product:** Veeam App

Starts Instant VM Recovery with manual configuration

**Inputs:**

- `Instance`: 
- `backupObjectId`: 

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: VBR REST API
- Scripts: DeleteContext, GetRestoredVmName
- Commands: veeam-vbr-get-backup-object, veeam-vbr-get-restore-points, veeam-vbr-get-session, veeam-vbr-start-instant-recovery-customized

## Rubrik Ransomware Discovery and VM Recovery - Rubrik Polaris

**Product:** Rubrik Security Cloud

Use this playbook to recover a virtual machine using the "RubrikPolaris" integration by either exporting or live-mounting a backup snapshot. This playbook also creates tickets on ServiceNow using "ServiceNow v2" integration. Supported integrations

**Inputs:**

- `ObjectId`: Object ID of the incident.
- `ClusterId`: Cluster ID of the incident.

**Dependencies:**

- Sub-playbooks: Rubrik Poll Async Result - Rubrik Polaris, Rubrik IOC Scan - Rubrik Polaris
- Integrations: RubrikPolaris, ServiceNow v2
- Scripts: http, Set, PrintErrorEntry, SetAndHandleEmpty, Print
- Commands: servicenow-create-ticket, rubrik-gps-vm-livemount, rubrik-gps-vm-export, rubrik-gps-vm-datastore-list, servicenow-update-ticket, rubrik-gps-vm-host-list, rubrik-gps-vm-snapshot-create, rubrik-polaris-vm-object-metadata-get


## Veeam - Start Instant Hyper-V VM Recovery Automatically

**Product:** Veeam App

Starts Instant VM Recovery for Microsoft Hyper-V with automatic configuration

**Inputs:**

- `Instance`: 
- `backupObjectId`: 

**Dependencies:**

- Sub-playbooks: GenericPolling, Veeam - Start Instant Hyper-V VM Recovery Manually
- Integrations: VBR REST API
- Scripts: DeleteContext, GetLatestCleanRestorePoint, GetRestoredVmName
- Commands: veeam-vbr-get-backup-object, veeam-vbr-get-inventory-objects, veeam-vbr-get-restore-points, veeam-vbr-get-session, veeam-vbr-get-session-logs, veeam-vbr-start-instant-recovery-hyperv-vm-customized


## Veeam - Start Instant Hyper-V VM Recovery Manually

**Product:** Veeam App

Starts Instant VM Recovery for Microsoft Hyper-V with manual configuration

**Inputs:**

- `Instance`: 
- `backupObjectId`: 

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: VBR REST API
- Scripts: DeleteContext, GetLatestCleanRestorePoint, GetRestoredVmName
- Commands: veeam-vbr-get-backup-object, veeam-vbr-get-restore-points, veeam-vbr-get-session, veeam-vbr-get-session-logs, veeam-vbr-start-instant-recovery-hyperv-vm-customized


## Veeam - Start Instant VM Recovery Manually

**Product:** Veeam App

Starts Instant VM Recovery with manual configuration

**Inputs:**

- `Instance`: 
- `backupObjectId`: 

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: VBR REST API
- Scripts: DeleteContext, GetRestoredVmName
- Commands: veeam-vbr-get-backup-object, veeam-vbr-get-restore-points, veeam-vbr-get-session, veeam-vbr-start-instant-recovery-customized

## Rubrik Ransomware Discovery and VM Recovery - Rubrik Polaris

**Product:** Rubrik Security Cloud

Use this playbook to recover a virtual machine using the "RubrikPolaris" integration by either exporting or live-mounting a backup snapshot. This playbook also creates tickets on ServiceNow using "ServiceNow v2" integration. Supported integrations

**Inputs:**

- `ObjectId`: Object ID of the incident.
- `ClusterId`: Cluster ID of the incident.

**Dependencies:**

- Sub-playbooks: Rubrik Poll Async Result - Rubrik Polaris, Rubrik IOC Scan - Rubrik Polaris
- Integrations: RubrikPolaris, ServiceNow v2
- Scripts: http, Set, PrintErrorEntry, SetAndHandleEmpty, Print
- Commands: servicenow-create-ticket, rubrik-gps-vm-livemount, rubrik-gps-vm-export, rubrik-gps-vm-datastore-list, servicenow-update-ticket, rubrik-gps-vm-host-list, rubrik-gps-vm-snapshot-create, rubrik-polaris-vm-object-metadata-get


## Veeam - Start Instant Hyper-V VM Recovery Automatically

**Product:** Veeam App

Starts Instant VM Recovery for Microsoft Hyper-V with automatic configuration

**Inputs:**

- `Instance`: 
- `backupObjectId`: 

**Dependencies:**

- Sub-playbooks: GenericPolling, Veeam - Start Instant Hyper-V VM Recovery Manually
- Integrations: VBR REST API
- Scripts: DeleteContext, GetLatestCleanRestorePoint, GetRestoredVmName
- Commands: veeam-vbr-get-backup-object, veeam-vbr-get-inventory-objects, veeam-vbr-get-restore-points, veeam-vbr-get-session, veeam-vbr-get-session-logs, veeam-vbr-start-instant-recovery-hyperv-vm-customized


## Veeam - Start Instant Hyper-V VM Recovery Manually

**Product:** Veeam App

Starts Instant VM Recovery for Microsoft Hyper-V with manual configuration

**Inputs:**

- `Instance`: 
- `backupObjectId`: 

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: VBR REST API
- Scripts: DeleteContext, GetLatestCleanRestorePoint, GetRestoredVmName
- Commands: veeam-vbr-get-backup-object, veeam-vbr-get-restore-points, veeam-vbr-get-session, veeam-vbr-get-session-logs, veeam-vbr-start-instant-recovery-hyperv-vm-customized


## Veeam - Start Instant VM Recovery Manually

**Product:** Veeam App

Starts Instant VM Recovery with manual configuration

**Inputs:**

- `Instance`: 
- `backupObjectId`: 

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: VBR REST API
- Scripts: DeleteContext, GetRestoredVmName
- Commands: veeam-vbr-get-backup-object, veeam-vbr-get-restore-points, veeam-vbr-get-session, veeam-vbr-start-instant-recovery-customized

## Rubrik Ransomware Discovery and VM Recovery - Rubrik Polaris

**Product:** Rubrik Security Cloud

Use this playbook to recover a virtual machine using the "RubrikPolaris" integration by either exporting or live-mounting a backup snapshot. This playbook also creates tickets on ServiceNow using "ServiceNow v2" integration. Supported integrations

**Inputs:**

- `ObjectId`: Object ID of the incident.
- `ClusterId`: Cluster ID of the incident.

**Dependencies:**

- Sub-playbooks: Rubrik Poll Async Result - Rubrik Polaris, Rubrik IOC Scan - Rubrik Polaris
- Integrations: RubrikPolaris, ServiceNow v2
- Scripts: http, Set, PrintErrorEntry, SetAndHandleEmpty, Print
- Commands: servicenow-create-ticket, rubrik-gps-vm-livemount, rubrik-gps-vm-export, rubrik-gps-vm-datastore-list, servicenow-update-ticket, rubrik-gps-vm-host-list, rubrik-gps-vm-snapshot-create, rubrik-polaris-vm-object-metadata-get


## Veeam - Start Instant Hyper-V VM Recovery Automatically

**Product:** Veeam App

Starts Instant VM Recovery for Microsoft Hyper-V with automatic configuration

**Inputs:**

- `Instance`: 
- `backupObjectId`: 

**Dependencies:**

- Sub-playbooks: GenericPolling, Veeam - Start Instant Hyper-V VM Recovery Manually
- Integrations: VBR REST API
- Scripts: DeleteContext, GetLatestCleanRestorePoint, GetRestoredVmName
- Commands: veeam-vbr-get-backup-object, veeam-vbr-get-inventory-objects, veeam-vbr-get-restore-points, veeam-vbr-get-session, veeam-vbr-get-session-logs, veeam-vbr-start-instant-recovery-hyperv-vm-customized


## Veeam - Start Instant Hyper-V VM Recovery Manually

**Product:** Veeam App

Starts Instant VM Recovery for Microsoft Hyper-V with manual configuration

**Inputs:**

- `Instance`: 
- `backupObjectId`: 

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: VBR REST API
- Scripts: DeleteContext, GetLatestCleanRestorePoint, GetRestoredVmName
- Commands: veeam-vbr-get-backup-object, veeam-vbr-get-restore-points, veeam-vbr-get-session, veeam-vbr-get-session-logs, veeam-vbr-start-instant-recovery-hyperv-vm-customized


## Veeam - Start Instant VM Recovery Manually

**Product:** Veeam App

Starts Instant VM Recovery with manual configuration

**Inputs:**

- `Instance`: 
- `backupObjectId`: 

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: VBR REST API
- Scripts: DeleteContext, GetRestoredVmName
- Commands: veeam-vbr-get-backup-object, veeam-vbr-get-restore-points, veeam-vbr-get-session, veeam-vbr-start-instant-recovery-customized

