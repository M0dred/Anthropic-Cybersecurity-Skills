# Vendor Variants - Containing Incident By Quarantining Files

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Cortex XDR - Quarantine File v2

**Product:** Cortex XDR by Palo Alto Networks

This playbook accepts "file path", "file hash" and "endpoint id" to quarantine a selected file and wait until the action is done. All 3 inputs are required to quarantine a single file. This playbook does not support the quarantine of multiple files

**Inputs:**

- `file_hash`: The file’s hash. Must be a valid SHA256 hash.
- `file_path`: The path for the selected file.
- `endpoint_id`: The file's location in the system.

**Outputs:**

- `PaloAltoNetworksXDR.quarantineFiles.status.status`
- `PaloAltoNetworksXDR.quarantineFiles.actionIds.endpointIdList.fileHash`
- `PaloAltoNetworksXDR.quarantineFiles.actionIds.endpointIdList.filePath`
- `PaloAltoNetworksXDR.quarantineFiles.actionIds.actionId`

**Dependencies:**

- Commands: xdr-get-quarantine-status, xdr-file-quarantine


## Prisma SASE - Quarantine a SentinelOne Host With Active Threat

**Product:** Palo Alto Networks - Strata Cloud Manager

**Dependencies:**

- Integrations: PrismaSASE
- Scripts: PrintErrorEntry, LoadJSON, IsIntegrationAvailable
- Commands: prisma-sase-quarantine-host, cdl-query-logs


## Rubrik Quarantine Files General

**Product:** Rubrik Security Cloud

This playbook quarantines files using the Microsoft Graph Search (O365 File Management) integration

**Inputs:**

- `file_information`: The list of files to quarantine. Each entry should contain the file name and its path.Example: [{"name": "<file_name>", "path": "<file_path>"}]
- `quarantine_folder_id`: The ID of the quarantine folder where the file will be moved.

**Dependencies:**

- Sub-playbooks: Rubrik Quarantine Files using MS Graph Search
- Scripts: DeleteContext, Set


## Rubrik Quarantine Files using MS Graph Search

**Product:** Rubrik Security Cloud

This playbook quarantines files using the Microsoft Graph Search (O365 File Management) integration by downloading them, uploading them to a quarantine folder and deleting them from their original location

**Inputs:**

- `file_path`: The file path of the file to quarantine in OneDrive/SharePoint.
- `file_name`: The name of the file to quarantine.
- `quarantine_folder_id`: The ID of the quarantine folder where the file will be uploaded.

**Dependencies:**

- Scripts: DeleteContext, Print, Set
- Commands: msgraph-delete-file, msgraph-download-file, msgraph-search-content, msgraph-upload-new-file

