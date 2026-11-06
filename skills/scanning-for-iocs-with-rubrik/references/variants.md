# Vendor Variants - Scanning For Iocs With Rubrik

Vendor-specific implementations, feeds, and collectors for this procedure.


## Rubrik IOC Scan v2 - Rubrik Polaris

**Product:** Rubrik Security Cloud

**Kind:** playbook

This playbook starts an advance IOC Scan with the provided IOC values and shows the results upon completion

**Inputs:**

- `object_ids`: The Object ID of the system on which to perform the scan. Supports comma separated values.Note: Users can get the list of object IDs by executing the "rubrik-polaris-objects-list" 
- `start_date`: Filter the snapshots from the provided date. Any snapshots taken before the provided date-time will be excluded.Formats accepted: 2 minutes, 2 hours, 2 days, 2 weeks, 2 months, 2 y
- `end_date`: Filter the snapshots until the provided date. Any snapshots taken after the provided date-time will be excluded.Formats accepted: 2 minutes, 2 hours, 2 days, 2 weeks, 2 months, 2 y
- `ioc_path`: Path of IOC to scan. Supports comma separated multiple values. Note: Do not provide quoted values. Provide the values in proper JSON format (Example: C:\\Users\\Malware_Executible.
- `ioc_hash`: Hash of IOC to scan. Supports comma separated multiple values. Note: Do not provide quoted values.
- `ioc_yara_rule`: Yara Rule(s) for IOC scan. Note: Do not provide quoted values. Provide the values in proper JSON format.
- `polling_interval`: Frequency that the IOC scan command will run (minutes).
- `polling_timeout`: Amount of time to poll before declaring a timeout and resuming the playbook (in minutes).
- `paths_to_include`: Paths to include in the scan. Supports comma separated values.Note: Do not provide quoted values.Format accepted: path_to_include_1, path_to_include_2.
- `paths_to_exclude`: Paths to exclude from the scan. Supports comma separated values.Note: Do not provide quoted values.Format accepted: path_to_exclude_1, path_to_exclude_2.

**Dependencies:**

- Sub-playbooks: GenericPolling
- Scripts: DeleteContext, Set, Print
- Commands: rubrik-advance-ioc-scan, rubrik-ioc-scan-results-v2

## Rubrik IOC Scan v2 - Rubrik Polaris

**Product:** Rubrik Security Cloud

**Kind:** playbook

This playbook starts an advance IOC Scan with the provided IOC values and shows the results upon completion

**Inputs:**

- `object_ids`: The Object ID of the system on which to perform the scan. Supports comma separated values.Note: Users can get the list of object IDs by executing the "rubrik-polaris-objects-list" 
- `start_date`: Filter the snapshots from the provided date. Any snapshots taken before the provided date-time will be excluded.Formats accepted: 2 minutes, 2 hours, 2 days, 2 weeks, 2 months, 2 y
- `end_date`: Filter the snapshots until the provided date. Any snapshots taken after the provided date-time will be excluded.Formats accepted: 2 minutes, 2 hours, 2 days, 2 weeks, 2 months, 2 y
- `ioc_path`: Path of IOC to scan. Supports comma separated multiple values. Note: Do not provide quoted values. Provide the values in proper JSON format (Example: C:\\Users\\Malware_Executible.
- `ioc_hash`: Hash of IOC to scan. Supports comma separated multiple values. Note: Do not provide quoted values.
- `ioc_yara_rule`: Yara Rule(s) for IOC scan. Note: Do not provide quoted values. Provide the values in proper JSON format.
- `polling_interval`: Frequency that the IOC scan command will run (minutes).
- `polling_timeout`: Amount of time to poll before declaring a timeout and resuming the playbook (in minutes).
- `paths_to_include`: Paths to include in the scan. Supports comma separated values.Note: Do not provide quoted values.Format accepted: path_to_include_1, path_to_include_2.
- `paths_to_exclude`: Paths to exclude from the scan. Supports comma separated values.Note: Do not provide quoted values.Format accepted: path_to_exclude_1, path_to_exclude_2.

**Dependencies:**

- Sub-playbooks: GenericPolling
- Scripts: DeleteContext, Set, Print
- Commands: rubrik-advance-ioc-scan, rubrik-ioc-scan-results-v2

## Rubrik IOC Scan v2 - Rubrik Polaris

**Product:** Rubrik Security Cloud

**Kind:** playbook

This playbook starts an advance IOC Scan with the provided IOC values and shows the results upon completion

**Inputs:**

- `object_ids`: The Object ID of the system on which to perform the scan. Supports comma separated values.Note: Users can get the list of object IDs by executing the "rubrik-polaris-objects-list" 
- `start_date`: Filter the snapshots from the provided date. Any snapshots taken before the provided date-time will be excluded.Formats accepted: 2 minutes, 2 hours, 2 days, 2 weeks, 2 months, 2 y
- `end_date`: Filter the snapshots until the provided date. Any snapshots taken after the provided date-time will be excluded.Formats accepted: 2 minutes, 2 hours, 2 days, 2 weeks, 2 months, 2 y
- `ioc_path`: Path of IOC to scan. Supports comma separated multiple values. Note: Do not provide quoted values. Provide the values in proper JSON format (Example: C:\\Users\\Malware_Executible.
- `ioc_hash`: Hash of IOC to scan. Supports comma separated multiple values. Note: Do not provide quoted values.
- `ioc_yara_rule`: Yara Rule(s) for IOC scan. Note: Do not provide quoted values. Provide the values in proper JSON format.
- `polling_interval`: Frequency that the IOC scan command will run (minutes).
- `polling_timeout`: Amount of time to poll before declaring a timeout and resuming the playbook (in minutes).
- `paths_to_include`: Paths to include in the scan. Supports comma separated values.Note: Do not provide quoted values.Format accepted: path_to_include_1, path_to_include_2.
- `paths_to_exclude`: Paths to exclude from the scan. Supports comma separated values.Note: Do not provide quoted values.Format accepted: path_to_exclude_1, path_to_exclude_2.

**Dependencies:**

- Sub-playbooks: GenericPolling
- Scripts: DeleteContext, Set, Print
- Commands: rubrik-advance-ioc-scan, rubrik-ioc-scan-results-v2

