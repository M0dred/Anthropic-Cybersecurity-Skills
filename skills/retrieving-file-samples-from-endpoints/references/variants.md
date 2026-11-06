# Vendor Variants - Retrieving File Samples From Endpoints

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Cortex XDR - Retrieve File by sha256

**Product:** Cortex XDR by Palo Alto Networks

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  The playbook facilitates the process of retrieving files from the investigated devices, unzipping the retrieved files, and loading them into the War Room. This playbook consists of the following steps: Initially, the sub-playbook ' XDR - Get File Path from alerts by hash' examines the SHA256 file hashes and retrieves the file paths associated with each hash. As soon as the SHA256 hashes, file paths, and endpoint IDs are obtained, the playbook attempts to retrieve the files from all the investigated devices. Once the file retrieval automation has been completed successfully, the playbook will unzip the files and load them into the War Room. Note: When retrieving multiple files, ensure that the SHA256 input is set to run in a loop

**Inputs:**

- `Sha256`: SHA256 for the file to be retrieved.

**Outputs:**

- `File`
- `File.Name`
- `File.EntryID`
- `File.Size`
- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `File.SHA512`
- `File.Extension`
- `File.Type`

**Dependencies:**

- Sub-playbooks: Cortex XDR - Get File Path from alerts by hash
- Integrations: CortexXDRIR
- Scripts: PrintErrorEntry, UnzipFile, isError
- Commands: xdr-file-retrieve


## Cortex XDR - Retrieve File v2

**Product:** Cortex XDR by Palo Alto Networks

This playbook retrieves files from selected endpoints. You can retrieve up to 20 files, from 10 endpoints. Inputs for this playbook are

**Inputs:**

- `endpoint_ids`: A comma-separated list of endpoint IDs.
- `file_path`: A comma-separated list of file paths in any platform. It can be used instead of the macOS/Windows/Linux file paths. The order of the files path list must be parallel to the endpoin
- `windows_file_paths`: A comma-separated list of Windows paths.Enter at least one path for either Windows, Linux, or Mac.
- `linux_file_paths`: A comma-separated list Linux paths.Enter at least one path for either Windows, Linux, or Mac.
- `mac_file_paths`: A comma-separated list of Mac paths.Enter at least one path for either Windows, Linux, or Mac.

**Outputs:**

- `File`
- `File.Name`
- `File.EntryID`
- `File.Size`
- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `File.SHA512`
- `File.Extension`
- `File.Type`

**Dependencies:**

- Integrations: CortexXDRIR
- Scripts: PrintErrorEntry, IsIntegrationAvailable
- Commands: xdr-file-retrieve, xdr-retrieve-file-details


## CrowdStrike Falcon - Retrieve File

**Product:** CrowdStrike Falcon

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook retrieves and unzips files from CrowdStrike Falcon and returns a list of the files that were and were not retrieved

**Inputs:**

- `HostId`: The ID of the host to use.
- `PathsToGet`: The path to retrieve the file from the host.
- `ZipPassword`: Default password to unzip files retrieved by CrowdStrike Falcon.
- `FileNames`: The names of the file to retrieve. This is used to validate that all the intended files were retrieved, not to specify which ones will be retrieved.

**Outputs:**

- `ExtractedFiles`
- `NonRetrievedFiles`

**Dependencies:**

- Integrations: CrowdStrikeFalcon
- Scripts: Set, UnzipFile, IsIntegrationAvailable
- Commands: cs-falcon-rtr-retrieve-file


## Cybereason - Download File

**Product:** Cybereason

This playbook downloads a file from Cybereason platform, based on the Malop ID and username provided

**Inputs:**

- `malopGUID, userName`: Malop GUID for fetching a file from a sonsor to download, The complete Cybereason user name string for the user performing the request

**Dependencies:**

- Commands: cybereason-start-fetchfile, cybereason-fetchfile-progress, cybereason-download-file


## MDE - Retrieve File

**Product:** Microsoft Defender for Endpoint

This playbook is part of the ‘Malware Investigation And Response’ pack. For more information, refer to  This playbook uses the Live Response feature to retrieve a file from an endpoint. The playbook supports a supplied machine id as an input. Otherwise, it will take the Device ID incident field. The playbook supports only one element to be retrieved for each task (if needed more then one - use the playbook loop feature)

**Inputs:**

- `paths`: The file paths to be provided.
- `MachineID`: The ID of the machine.

**Outputs:**

- `ExtractedFiles`
- `MicrosoftATP.LiveResponseAction.status`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Scripts: isError, UnzipFile
- Commands: microsoft-atp-live-response-get-file


## PS Remote Get File Sample From Path

**Product:** Windows Forensics

This playbook leverages the Windows built-in PowerShell and WinRM capabilities to connect to a Windows host to acquire a file as forensic evidence for further analysis

**Inputs:**

- `Host`: A single hostname or IP address of the machine on which the file is located. For example, testpc01.
- `FilePath`: The path on the hostname from which to retrieve the file. For example, c:\tmp\test.txt.If you use the AddHostNameToFile input as true, the file downloaded to the platform will contain of 
- `ZipFile`: Specify "true" to zip the MFT file before sending it to the platform.
- `AddHostNameToFile`: Specify "true" for the name of the downloaded file to contain the hostname or "false" to keep the filename as configured in the FilePath argument.

**Outputs:**

- `AcquiredFile`
- `File`

**Dependencies:**

- Scripts: UnzipFile, IsIntegrationAvailable, AddEvidence, Set
- Commands: ps-remote-download-file

## Cortex XDR - Retrieve File by sha256

**Product:** Cortex XDR by Palo Alto Networks

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  The playbook facilitates the process of retrieving files from the investigated devices, unzipping the retrieved files, and loading them into the War Room. This playbook consists of the following steps: Initially, the sub-playbook ' XDR - Get File Path from alerts by hash' examines the SHA256 file hashes and retrieves the file paths associated with each hash. As soon as the SHA256 hashes, file paths, and endpoint IDs are obtained, the playbook attempts to retrieve the files from all the investigated devices. Once the file retrieval automation has been completed successfully, the playbook will unzip the files and load them into the War Room. Note: When retrieving multiple files, ensure that the SHA256 input is set to run in a loop

**Inputs:**

- `Sha256`: SHA256 for the file to be retrieved.

**Outputs:**

- `File`
- `File.Name`
- `File.EntryID`
- `File.Size`
- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `File.SHA512`
- `File.Extension`
- `File.Type`

**Dependencies:**

- Sub-playbooks: Cortex XDR - Get File Path from alerts by hash
- Integrations: CortexXDRIR
- Scripts: PrintErrorEntry, UnzipFile, isError
- Commands: xdr-file-retrieve


## Cortex XDR - Retrieve File v2

**Product:** Cortex XDR by Palo Alto Networks

This playbook retrieves files from selected endpoints. You can retrieve up to 20 files, from 10 endpoints. Inputs for this playbook are

**Inputs:**

- `endpoint_ids`: A comma-separated list of endpoint IDs.
- `file_path`: A comma-separated list of file paths in any platform. It can be used instead of the macOS/Windows/Linux file paths. The order of the files path list must be parallel to the endpoin
- `windows_file_paths`: A comma-separated list of Windows paths.Enter at least one path for either Windows, Linux, or Mac.
- `linux_file_paths`: A comma-separated list Linux paths.Enter at least one path for either Windows, Linux, or Mac.
- `mac_file_paths`: A comma-separated list of Mac paths.Enter at least one path for either Windows, Linux, or Mac.

**Outputs:**

- `File`
- `File.Name`
- `File.EntryID`
- `File.Size`
- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `File.SHA512`
- `File.Extension`
- `File.Type`

**Dependencies:**

- Integrations: CortexXDRIR
- Scripts: PrintErrorEntry, IsIntegrationAvailable
- Commands: xdr-file-retrieve, xdr-retrieve-file-details


## CrowdStrike Falcon - Retrieve File

**Product:** CrowdStrike Falcon

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook retrieves and unzips files from CrowdStrike Falcon and returns a list of the files that were and were not retrieved

**Inputs:**

- `HostId`: The ID of the host to use.
- `PathsToGet`: The path to retrieve the file from the host.
- `ZipPassword`: Default password to unzip files retrieved by CrowdStrike Falcon.
- `FileNames`: The names of the file to retrieve. This is used to validate that all the intended files were retrieved, not to specify which ones will be retrieved.

**Outputs:**

- `ExtractedFiles`
- `NonRetrievedFiles`

**Dependencies:**

- Integrations: CrowdStrikeFalcon
- Scripts: Set, UnzipFile, IsIntegrationAvailable
- Commands: cs-falcon-rtr-retrieve-file


## Cybereason - Download File

**Product:** Cybereason

This playbook downloads a file from Cybereason platform, based on the Malop ID and username provided

**Inputs:**

- `malopGUID, userName`: Malop GUID for fetching a file from a sonsor to download, The complete Cybereason user name string for the user performing the request

**Dependencies:**

- Commands: cybereason-start-fetchfile, cybereason-fetchfile-progress, cybereason-download-file


## MDE - Retrieve File

**Product:** Microsoft Defender for Endpoint

This playbook is part of the ‘Malware Investigation And Response’ pack. For more information, refer to  This playbook uses the Live Response feature to retrieve a file from an endpoint. The playbook supports a supplied machine id as an input. Otherwise, it will take the Device ID incident field. The playbook supports only one element to be retrieved for each task (if needed more then one - use the playbook loop feature)

**Inputs:**

- `paths`: The file paths to be provided.
- `MachineID`: The ID of the machine.

**Outputs:**

- `ExtractedFiles`
- `MicrosoftATP.LiveResponseAction.status`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Scripts: isError, UnzipFile
- Commands: microsoft-atp-live-response-get-file


## PS Remote Get File Sample From Path

**Product:** Windows Forensics

This playbook leverages the Windows built-in PowerShell and WinRM capabilities to connect to a Windows host to acquire a file as forensic evidence for further analysis

**Inputs:**

- `Host`: A single hostname or IP address of the machine on which the file is located. For example, testpc01.
- `FilePath`: The path on the hostname from which to retrieve the file. For example, c:\tmp\test.txt.If you use the AddHostNameToFile input as true, the file downloaded to the platform will cont
- `ZipFile`: Specify "true" to zip the MFT file before sending it to the platform.
- `AddHostNameToFile`: Specify "true" for the name of the downloaded file to contain the hostname or "false" to keep the filename as configured in the FilePath argument.

**Outputs:**

- `AcquiredFile`
- `File`

**Dependencies:**

- Scripts: UnzipFile, IsIntegrationAvailable, AddEvidence, Set
- Commands: ps-remote-download-file

## Cortex XDR - Retrieve File by sha256

**Product:** Cortex XDR by Palo Alto Networks

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  The playbook facilitates the process of retrieving files from the investigated devices, unzipping the retrieved files, and loading them into the War Room. This playbook consists of the following steps: Initially, the sub-playbook ' XDR - Get File Path from alerts by hash' examines the SHA256 file hashes and retrieves the file paths associated with each hash. As soon as the SHA256 hashes, file paths, and endpoint IDs are obtained, the playbook attempts to retrieve the files from all the investigated devices. Once the file retrieval automation has been completed successfully, the playbook will unzip the files and load them into the War Room. Note: When retrieving multiple files, ensure that the SHA256 input is set to run in a loop

**Inputs:**

- `Sha256`: SHA256 for the file to be retrieved.

**Outputs:**

- `File`
- `File.Name`
- `File.EntryID`
- `File.Size`
- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `File.SHA512`
- `File.Extension`
- `File.Type`

**Dependencies:**

- Sub-playbooks: Cortex XDR - Get File Path from alerts by hash
- Integrations: CortexXDRIR
- Scripts: PrintErrorEntry, UnzipFile, isError
- Commands: xdr-file-retrieve


## Cortex XDR - Retrieve File v2

**Product:** Cortex XDR by Palo Alto Networks

This playbook retrieves files from selected endpoints. You can retrieve up to 20 files, from 10 endpoints. Inputs for this playbook are

**Inputs:**

- `endpoint_ids`: A comma-separated list of endpoint IDs.
- `file_path`: A comma-separated list of file paths in any platform. It can be used instead of the macOS/Windows/Linux file paths. The order of the files path list must be parallel to the endpoin
- `windows_file_paths`: A comma-separated list of Windows paths.Enter at least one path for either Windows, Linux, or Mac.
- `linux_file_paths`: A comma-separated list Linux paths.Enter at least one path for either Windows, Linux, or Mac.
- `mac_file_paths`: A comma-separated list of Mac paths.Enter at least one path for either Windows, Linux, or Mac.

**Outputs:**

- `File`
- `File.Name`
- `File.EntryID`
- `File.Size`
- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `File.SHA512`
- `File.Extension`
- `File.Type`

**Dependencies:**

- Integrations: CortexXDRIR
- Scripts: PrintErrorEntry, IsIntegrationAvailable
- Commands: xdr-file-retrieve, xdr-retrieve-file-details


## CrowdStrike Falcon - Retrieve File

**Product:** CrowdStrike Falcon

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook retrieves and unzips files from CrowdStrike Falcon and returns a list of the files that were and were not retrieved

**Inputs:**

- `HostId`: The ID of the host to use.
- `PathsToGet`: The path to retrieve the file from the host.
- `ZipPassword`: Default password to unzip files retrieved by CrowdStrike Falcon.
- `FileNames`: The names of the file to retrieve. This is used to validate that all the intended files were retrieved, not to specify which ones will be retrieved.

**Outputs:**

- `ExtractedFiles`
- `NonRetrievedFiles`

**Dependencies:**

- Integrations: CrowdStrikeFalcon
- Scripts: Set, UnzipFile, IsIntegrationAvailable
- Commands: cs-falcon-rtr-retrieve-file


## Cybereason - Download File

**Product:** Cybereason

This playbook downloads a file from Cybereason platform, based on the Malop ID and username provided

**Inputs:**

- `malopGUID, userName`: Malop GUID for fetching a file from a sonsor to download, The complete Cybereason user name string for the user performing the request

**Dependencies:**

- Commands: cybereason-start-fetchfile, cybereason-fetchfile-progress, cybereason-download-file


## MDE - Retrieve File

**Product:** Microsoft Defender for Endpoint

This playbook is part of the ‘Malware Investigation And Response’ pack. For more information, refer to  This playbook uses the Live Response feature to retrieve a file from an endpoint. The playbook supports a supplied machine id as an input. Otherwise, it will take the Device ID incident field. The playbook supports only one element to be retrieved for each task (if needed more then one - use the playbook loop feature)

**Inputs:**

- `paths`: The file paths to be provided.
- `MachineID`: The ID of the machine.

**Outputs:**

- `ExtractedFiles`
- `MicrosoftATP.LiveResponseAction.status`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Scripts: isError, UnzipFile
- Commands: microsoft-atp-live-response-get-file


## PS Remote Get File Sample From Path

**Product:** Windows Forensics

This playbook leverages the Windows built-in PowerShell and WinRM capabilities to connect to a Windows host to acquire a file as forensic evidence for further analysis

**Inputs:**

- `Host`: A single hostname or IP address of the machine on which the file is located. For example, testpc01.
- `FilePath`: The path on the hostname from which to retrieve the file. For example, c:\tmp\test.txt.If you use the AddHostNameToFile input as true, the file downloaded to the platform will cont
- `ZipFile`: Specify "true" to zip the MFT file before sending it to the platform.
- `AddHostNameToFile`: Specify "true" for the name of the downloaded file to contain the hostname or "false" to keep the filename as configured in the FilePath argument.

**Outputs:**

- `AcquiredFile`
- `File`

**Dependencies:**

- Scripts: UnzipFile, IsIntegrationAvailable, AddEvidence, Set
- Commands: ps-remote-download-file

## Cortex XDR - Retrieve File by sha256

**Product:** Cortex XDR by Palo Alto Networks

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  The playbook facilitates the process of retrieving files from the investigated devices, unzipping the retrieved files, and loading them into the War Room. This playbook consists of the following steps: Initially, the sub-playbook ' XDR - Get File Path from alerts by hash' examines the SHA256 file hashes and retrieves the file paths associated with each hash. As soon as the SHA256 hashes, file paths, and endpoint IDs are obtained, the playbook attempts to retrieve the files from all the investigated devices. Once the file retrieval automation has been completed successfully, the playbook will unzip the files and load them into the War Room. Note: When retrieving multiple files, ensure that the SHA256 input is set to run in a loop

**Inputs:**

- `Sha256`: SHA256 for the file to be retrieved.

**Outputs:**

- `File`
- `File.Name`
- `File.EntryID`
- `File.Size`
- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `File.SHA512`
- `File.Extension`
- `File.Type`

**Dependencies:**

- Sub-playbooks: Cortex XDR - Get File Path from alerts by hash
- Integrations: CortexXDRIR
- Scripts: PrintErrorEntry, UnzipFile, isError
- Commands: xdr-file-retrieve


## Cortex XDR - Retrieve File v2

**Product:** Cortex XDR by Palo Alto Networks

This playbook retrieves files from selected endpoints. You can retrieve up to 20 files, from 10 endpoints. Inputs for this playbook are

**Inputs:**

- `endpoint_ids`: A comma-separated list of endpoint IDs.
- `file_path`: A comma-separated list of file paths in any platform. It can be used instead of the macOS/Windows/Linux file paths. The order of the files path list must be parallel to the endpoin
- `windows_file_paths`: A comma-separated list of Windows paths.Enter at least one path for either Windows, Linux, or Mac.
- `linux_file_paths`: A comma-separated list Linux paths.Enter at least one path for either Windows, Linux, or Mac.
- `mac_file_paths`: A comma-separated list of Mac paths.Enter at least one path for either Windows, Linux, or Mac.

**Outputs:**

- `File`
- `File.Name`
- `File.EntryID`
- `File.Size`
- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `File.SHA512`
- `File.Extension`
- `File.Type`

**Dependencies:**

- Integrations: CortexXDRIR
- Scripts: PrintErrorEntry, IsIntegrationAvailable
- Commands: xdr-file-retrieve, xdr-retrieve-file-details


## CrowdStrike Falcon - Retrieve File

**Product:** CrowdStrike Falcon

This playbook is part of the 'Malware Investigation And Response' pack. For more information, refer to  This playbook retrieves and unzips files from CrowdStrike Falcon and returns a list of the files that were and were not retrieved

**Inputs:**

- `HostId`: The ID of the host to use.
- `PathsToGet`: The path to retrieve the file from the host.
- `ZipPassword`: Default password to unzip files retrieved by CrowdStrike Falcon.
- `FileNames`: The names of the file to retrieve. This is used to validate that all the intended files were retrieved, not to specify which ones will be retrieved.

**Outputs:**

- `ExtractedFiles`
- `NonRetrievedFiles`

**Dependencies:**

- Integrations: CrowdStrikeFalcon
- Scripts: Set, UnzipFile, IsIntegrationAvailable
- Commands: cs-falcon-rtr-retrieve-file


## Cybereason - Download File

**Product:** Cybereason

This playbook downloads a file from Cybereason platform, based on the Malop ID and username provided

**Inputs:**

- `malopGUID, userName`: Malop GUID for fetching a file from a sonsor to download, The complete Cybereason user name string for the user performing the request

**Dependencies:**

- Commands: cybereason-start-fetchfile, cybereason-fetchfile-progress, cybereason-download-file


## MDE - Retrieve File

**Product:** Microsoft Defender for Endpoint

This playbook is part of the ‘Malware Investigation And Response’ pack. For more information, refer to  This playbook uses the Live Response feature to retrieve a file from an endpoint. The playbook supports a supplied machine id as an input. Otherwise, it will take the Device ID incident field. The playbook supports only one element to be retrieved for each task (if needed more then one - use the playbook loop feature)

**Inputs:**

- `paths`: The file paths to be provided.
- `MachineID`: The ID of the machine.

**Outputs:**

- `ExtractedFiles`
- `MicrosoftATP.LiveResponseAction.status`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Scripts: isError, UnzipFile
- Commands: microsoft-atp-live-response-get-file


## PS Remote Get File Sample From Path

**Product:** Windows Forensics

This playbook leverages the Windows built-in PowerShell and WinRM capabilities to connect to a Windows host to acquire a file as forensic evidence for further analysis

**Inputs:**

- `Host`: A single hostname or IP address of the machine on which the file is located. For example, testpc01.
- `FilePath`: The path on the hostname from which to retrieve the file. For example, c:\tmp\test.txt.If you use the AddHostNameToFile input as true, the file downloaded to the platform will cont
- `ZipFile`: Specify "true" to zip the MFT file before sending it to the platform.
- `AddHostNameToFile`: Specify "true" for the name of the downloaded file to contain the hostname or "false" to keep the filename as configured in the FilePath argument.

**Outputs:**

- `AcquiredFile`
- `File`

**Dependencies:**

- Scripts: UnzipFile, IsIntegrationAvailable, AddEvidence, Set
- Commands: ps-remote-download-file

## Retrieve File from Endpoint - Generic V3

**Product:** Common Playbooks

**Kind:** playbook

'This playbook retrieves a file sample from an endpoint using the following playbooks:'

**Inputs:**

- `MD5`: The MD5 hash value for the file to retrieve.
- `SHA256`: The SHA256 hash value for the file to retrieve.
- `Host`: Hostname of the machine on which the file is located for PS remote it can also be an IP address.
- `Path`: The path of the file to retrieve.For example:C:\users\folder\file.txt
- `Agent_ID`: The ID of the agent in the relevant integration (such as EDR).

**Dependencies:**

- Sub-playbooks: Get File Sample By Hash - Generic v3, Get File Sample From Path - Generic V3

## Retrieve File from Endpoint - Generic V3

**Product:** Common Playbooks

**Kind:** playbook

'This playbook retrieves a file sample from an endpoint using the following playbooks:'

**Inputs:**

- `MD5`: The MD5 hash value for the file to retrieve.
- `SHA256`: The SHA256 hash value for the file to retrieve.
- `Host`: Hostname of the machine on which the file is located for PS remote it can also be an IP address.
- `Path`: The path of the file to retrieve.For example:C:\users\folder\file.txt
- `Agent_ID`: The ID of the agent in the relevant integration (such as EDR).

**Dependencies:**

- Sub-playbooks: Get File Sample By Hash - Generic v3, Get File Sample From Path - Generic V3

## Retrieve File from Endpoint - Generic V3

**Product:** Common Playbooks

**Kind:** playbook

'This playbook retrieves a file sample from an endpoint using the following playbooks:'

**Inputs:**

- `MD5`: The MD5 hash value for the file to retrieve.
- `SHA256`: The SHA256 hash value for the file to retrieve.
- `Host`: Hostname of the machine on which the file is located for PS remote it can also be an IP address.
- `Path`: The path of the file to retrieve.For example:C:\users\folder\file.txt
- `Agent_ID`: The ID of the agent in the relevant integration (such as EDR).

**Dependencies:**

- Sub-playbooks: Get File Sample By Hash - Generic v3, Get File Sample From Path - Generic V3

