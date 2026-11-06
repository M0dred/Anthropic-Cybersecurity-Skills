# Vendor Variants - Analyzing Pcap Files With Pcapminer

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Endace Search Archive Download PCAP v2

**Product:** Endace

This playbook uses Endace APIs to search, archive and download PCAP file from either a single EndaceProbe or many via the InvestigationManager. The workflow accepts inputs like “the date and time of the incident or a timeframe”, “source or destination IP address of the incident”, “source or destination IP port of the incident”, “protocol of the incident” and name of archive file. Required Inputs - Either timeframe or start and timeframe or end and timeframe or start and end fields. Either src_host_list or dest_host_list or ip fields. Either src_port_list or dest_port_list or port fields. archive_filename field is required delete_archive field is required download_threshold field is required The Workflow in this playbook

**Inputs:**

- `start`: UTC StartTime in ISO 8601 format as in 2020-04-08T15:46:30
- `end`: UTC EndTime in ISO 8601 format as in 2020-04-08T15:46:30
- `timeframe`: Event timeframe to search. Select one of the values from 30seconds, 1minute, 5minutes, 10minutes, 30minutes, 1hour, 2hours, 5hours, 10hours, 12hours, 1day, 3days, 5days, 1week. Tim
- `ip`: directionless ip address. For valid search either a IP or Src Host or a Dest Host value is required
- `port`: directionless port.
- `src_host_list`: List of comma delimited Source IP addresses to search with a maximum of 10 IP addresses per search. For valid search either a Src Host or a Dest Host value is required.
- `dest_host_list`: List of comma delimited Destination IP addresses to search with a maximum of 10 IP addresses per search. For valid search either a Src Host or a Dest Host value is required.
- `src_port_list`: List of comma delimited Source Port addresses to search with a maximum of 10 Port addresses per search.
- `dest_port_list`: List of comma delimited Destination Port addresses to search with a maximum of 10 Port addresses per search.
- `protocol`: IANA defined IP Protocol Name or Number. For example - either use TCP or tcp or 6 for tcp protocol

**Outputs:**

- `Endace.Download.PCAP.FileName`
- `Endace.Download.PCAP.FileSize`
- `Endace.Download.PCAP.FileUser`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: Endace
- Scripts: IsGreaterThan, IsTrue, Set, AreValuesEqual, Print, AddEvidence
- Commands: endace-create-archive, endace-create-search, endace-delete-archived-file, endace-get-archive-status, endace-download-pcap


## PCAP Analysis

**Product:** PCAP Analysis

This playbook leverages all of the PCAP miner and PCAP file extractor sub playbook capabilities, including: The playbooks is meant to be a demonstration of all the PCAP analysis capabilities however it is more likely to use each of the subplaybooks seperatly. In order to demonstrate the entire flow make sure that at least on of the following playbook inputs is configured in order for search results to exist

**Inputs:**

- `PcapFileEntryID`: This input specifies the file entry ID for the PCAP file if the user provided the file in the incident. One PCAP file can run per incident.
- `RunParsingAndEnrichment`: This input specifies whether to run the parsing and enrichment playbook. Values can be true or any other value for false.
- `RunFileCarving`: This input specifies whether to run the file carving playbook. Values can be true or any other value for false.
- `RsaDecryptKeyEntryID`: This input specifies the file entry ID for the RSA decrypt key if the user provided the key in the incident.
- `WpaPassword`: This input value is used to provide a WPA (Wi-Fi Protected Access) password to decrypt encrypted 802.11 Wi-FI traffic.
- `QueryOperator`: In case the playbook has several search inputs provided such as IPAddressToSearch, TCPPortsToSearch ,UDPPortsToSearch, ProtocolToSearch and AdvancedSearchFilter. This input will sp
- `IPAddressToSearch`: The value of an IP address to search. Can be a single IP or a comma delimited list of IP addresses. CIDR ranges are also acceptable. All IPs will be treated with the OR operator.
- `TCPPortsToSearch`: The value of a TCP port number to search. Can be a single port or a comma delimited list of ports. All TCP ports will be treated with the OR operator.
- `UDPPortsToSearch`: The value of a UDP port number to search. Can be a single port or a comma delimited list of ports. All UDP ports will be treated with the OR operator.
- `ProtocolToSearch`: The protocols to search for within the PCAP file. Can be a single protocol or a comma delimited list of protocols. The protocol names should be the same as searching in Wireshark. 

**Outputs:**

- `InternalIPAddresses`
- `ExternalIPAddresses`
- `DestinationTcpPorts`
- `DestinationUdpPorts`
- `DetectedProtocols`
- `ExternalEmailAddresses`
- `InternalEmailAddresses`
- `ExternalUrls`
- `InternalUrls`
- `PcapResults.Protocols`

**Dependencies:**

- Sub-playbooks: PCAP Parsing And Indicator Enrichment, PCAP Search, PCAP File Carving


## PCAP File Carving

**Product:** PCAP Analysis

This playbook is used to carve (extract) files from within PCAP files and perform enrichment and detonation of the extracted files. Supported PCAP file types are pcap, cap, pcapng. The playbook can handle one PCAP file per incident. Additional inputs allow the user to provide the WPA password for decrypting 802.11 (wireless) traffic and adding an RSA certificate to decrypt SSL traffic. Additional options enable you to filter the files to extract according to the file extension or the actual file type (MIME), and limit the amount of files to extract. Another feature enables you to specify a filter to create a new smaller PCAP file. To display the results within the relevant incident fields, the playbook needs to run in a PCAP Analysis incident type. For handling of PCAP files larger than 30 MB, refer to the PcapMinerV2 documentation

**Inputs:**

- `RsaDecryptKeyEntryID`: This input specifies the file entry id for the RSA decrypt key if the user provided the key in the incident.
- `PcapFileEntryID`: This input specifies the file entry id for the PCAP file if the user provided the file in the incident. One PCAP file can run per incident.
- `WpaPassword`: This input value is used to provide a WPA (Wi-Fi Protected Access) password to decrypt encrypted 802.11 Wi-FI traffic.
- `PcapFilter`: This input specifies a search filter to be used on the PCAP file. Filters can be used to search only for a specific IP, protocols, and other examples. The syntax is the same as in 
- `ExtractedFilesLimit`: This input limits the number of files to be extracted from the PCAP file. Default value is 5.
- `FileExtensionFilter`: This input is used to select which file extensions to include or exclude from the PCAP file. Extensions must be comma separated, for example, png,gif,exe.This setting cannot be use
- `FileTypeFilter`: This input is used to select which file type (MIME type) to include or exclude from the PCAP file. Extensions must be comma separated, for example, image/jpeg,application/x-javascr
- `FilterType`: This input is combined with the FileExtensionFilter input or the FileTypeFilter input. It specifies if the type/extensions list is inclusive or exclusive. Can be "inclusive" or "ex
- `AutoDetonateFiles`: This input specifies whether to detonate files extracted from the PCAP. The default value is True. Any other value will be considered as false.
- `AutoEnrichFiles`: This input specifies whether to enrich files extracted from the PCAP. The default value is True. Any other value will be considered as false.

**Outputs:**

- `DBotScore`
- `File`
- `File.Malicious`
- `File.Size`
- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `File.SHA512`
- `File.Name`
- `File.SSDeep`

**Dependencies:**

- Sub-playbooks: Detonate File - Generic
- Scripts: PcapFileExtractor, Set, PcapMinerV2
- Commands: file


## PCAP Parsing And Indicator Enrichment

**Product:** PCAP Analysis

This playbook is used to parse and extract indicators within PCAP files and perform enrichment on the detected indicators. Supported file types are pcap, cap, pcapng. The playbook can handle one PCAP file per incident. The user inputs which indicator types are to be enriched including, email, URLs, IP addresses. The user can specify in the inputs which indicators are internal or that will be treated as internal (not enriched). The user can also specify a specific regex pattern to search for. Another option is to specify the protocol types to be printed to context for data extraction. Additional inputs allow the user to provide the WPA password for decrypting 802.11 (wireless) traffic and add an RSA certificate to decrypt SSL traffic. To display the results within the relevant incident fields, the playbook needs to run in a PCAP Analysis incident type. For handling of PCAP files larger than 30 MB, refer to the PcapMinerV2 documentation

**Inputs:**

- `PcapFilter`: This input specifies a search filter to be used on the pcap file. Filters can be used to search only for a specific IP, protocols, and other examples. The syntax is the same as in 

**Outputs:**

- `InternalIPAddresses`
- `ExternalIPAddresses`
- `ExternalEmailAddresses`
- `InternalEmailAddresses`
- `ExternalUrls`
- `InternalUrls`
- `PcapResults.Protocols`
- `DestinationTcpPorts`
- `DestinationUdpPorts`

**Dependencies:**

- Scripts: SetGridField, IsUrlPartOfDomain, PcapMinerV2, SetAndHandleEmpty, IsEmailAddressInternal, IsIPInRanges
- Commands: url, ip, email


## PCAP Search

**Product:** PCAP Analysis

This playbook is used to parse and search within PCAP files. Supported file types are pcap, cap, pcapng. The playbook can handle one PCAP file per incident. The user inputs which objects the playbook should search for in the PCAP. The values to search are IP addresses, CIDR ranges, and TCP or UDP ports or protocols. In the event that more than one input type was specified, specify in the QueryOperator input (such as IP addresses and TCP ports) if the PCAP filter query will use an AND or an OR operator between the inputs. Another option is to use advanced filters just like in Wireshark to use refined filters or for objects not specified in other inputs. Additional inputs allow the user to provide the WPA password for decrypting 802.11 (wireless) traffic and adding an RSA certificate to decrypt SSL traffic. To display the results within the relevant incident fields, the playbook needs to run in a PCAP Analysis incident type. For handling of PCAP files larger than 30 MB, refer to the PcapMinerV2 documentation

**Inputs:**

- `QueryOperator`: In case the playbook has several search inputs provided such as IPAddressToSearch, TCPPortsToSearch ,UDPPortsToSearch, ProtocolToSearch and AdvancedSearchFilter. This input will sp
- `IPAddressToSearch`: The value of an IP address to search. Can be a single IP or a comma delimited list of IP addresses. CIDR ranges are also acceptable. All IPs will be treated with the OR operator.
- `TCPPortsToSearch`: The value of a TCP port number to search. Can be a single port or a comma delimited list of ports. All TCP ports will be treated with the OR operator.
- `UDPPortsToSearch`: The value of a UDP port number to search. Can be a single port or a comma delimited list of ports. All UDP ports will be treated with the OR operator.
- `ProtocolToSearch`: The protocols to search for within the PCAP file. Can be a single protocol or a comma delimited list of protocols. The protocol names should be the same as searching in Wireshark. 
- `WpaPassword`: This input value is used to provide a WPA (Wi-Fi Protected Access) password to decrypt encrypted 802.11 Wi-FI traffic.
- `AdvancedSearchFilter`: Filter to apply on PCAP. Wireshark syntax as can be found here: https://www.wireshark.org/docs/man-pages/wireshark-filter.html
- `This input is meant to handle more complex filters not covered by the other inputs. For example search by an attribute such as http.host, arp.dst.hw etc.`: 
- `RsaDecryptKeyEntryID`: This input specifics the file entry id for the RSA decrypt key if the user provided the key in the incident.
- `PcapFileEntryID`: This input specifics the file entry id for the PCAP file if the user provided the file in the incident. One PCAP file can run per incident.

**Outputs:**

- `InternalIPAddresses`
- `ExternalIPAddresses`
- `DestinationTcpPorts`
- `DestinationUdpPorts`
- `DetectedProtocols`
- `PcapQuery`

**Dependencies:**

- Scripts: SetAndHandleEmpty, SetGridField, PcapMinerV2, IsIPInRanges

## Endace Search Archive Download PCAP v2

**Product:** Endace

This playbook uses Endace APIs to search, archive and download PCAP file from either a single EndaceProbe or many via the InvestigationManager. The workflow accepts inputs like “the date and time of the incident or a timeframe”, “source or destination IP address of the incident”, “source or destination IP port of the incident”, “protocol of the incident” and name of archive file. Required Inputs - Either timeframe or start and timeframe or end and timeframe or start and end fields. Either src_host_list or dest_host_list or ip fields. Either src_port_list or dest_port_list or port fields. archive_filename field is required delete_archive field is required download_threshold field is required The Workflow in this playbook

**Inputs:**

- `start`: UTC StartTime in ISO 8601 format as in 2020-04-08T15:46:30
- `end`: UTC EndTime in ISO 8601 format as in 2020-04-08T15:46:30
- `timeframe`: Event timeframe to search. Select one of the values from 30seconds, 1minute, 5minutes, 10minutes, 30minutes, 1hour, 2hours, 5hours, 10hours, 12hours, 1day, 3days, 5days, 1week. Tim
- `ip`: directionless ip address. For valid search either a IP or Src Host or a Dest Host value is required
- `port`: directionless port.
- `src_host_list`: List of comma delimited Source IP addresses to search with a maximum of 10 IP addresses per search. For valid search either a Src Host or a Dest Host value is required.
- `dest_host_list`: List of comma delimited Destination IP addresses to search with a maximum of 10 IP addresses per search. For valid search either a Src Host or a Dest Host value is required.
- `src_port_list`: List of comma delimited Source Port addresses to search with a maximum of 10 Port addresses per search.
- `dest_port_list`: List of comma delimited Destination Port addresses to search with a maximum of 10 Port addresses per search.
- `protocol`: IANA defined IP Protocol Name or Number. For example - either use TCP or tcp or 6 for tcp protocol

**Outputs:**

- `Endace.Download.PCAP.FileName`
- `Endace.Download.PCAP.FileSize`
- `Endace.Download.PCAP.FileUser`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: Endace
- Scripts: IsGreaterThan, IsTrue, Set, AreValuesEqual, Print, AddEvidence
- Commands: endace-create-archive, endace-create-search, endace-delete-archived-file, endace-get-archive-status, endace-download-pcap


## PCAP Analysis

**Product:** PCAP Analysis

This playbook leverages all of the PCAP miner and PCAP file extractor sub playbook capabilities, including: The playbooks is meant to be a demonstration of all the PCAP analysis capabilities however it is more likely to use each of the subplaybooks seperatly. In order to demonstrate the entire flow make sure that at least on of the following playbook inputs is configured in order for search results to exist

**Inputs:**

- `PcapFileEntryID`: This input specifies the file entry ID for the PCAP file if the user provided the file in the incident. One PCAP file can run per incident.
- `RunParsingAndEnrichment`: This input specifies whether to run the parsing and enrichment playbook. Values can be true or any other value for false.
- `RunFileCarving`: This input specifies whether to run the file carving playbook. Values can be true or any other value for false.
- `RsaDecryptKeyEntryID`: This input specifies the file entry ID for the RSA decrypt key if the user provided the key in the incident.
- `WpaPassword`: This input value is used to provide a WPA (Wi-Fi Protected Access) password to decrypt encrypted 802.11 Wi-FI traffic.
- `QueryOperator`: In case the playbook has several search inputs provided such as IPAddressToSearch, TCPPortsToSearch ,UDPPortsToSearch, ProtocolToSearch and AdvancedSearchFilter. This input will sp
- `IPAddressToSearch`: The value of an IP address to search. Can be a single IP or a comma delimited list of IP addresses. CIDR ranges are also acceptable. All IPs will be treated with the OR operator.
- `TCPPortsToSearch`: The value of a TCP port number to search. Can be a single port or a comma delimited list of ports. All TCP ports will be treated with the OR operator.
- `UDPPortsToSearch`: The value of a UDP port number to search. Can be a single port or a comma delimited list of ports. All UDP ports will be treated with the OR operator.
- `ProtocolToSearch`: The protocols to search for within the PCAP file. Can be a single protocol or a comma delimited list of protocols. The protocol names should be the same as searching in Wireshark. 

**Outputs:**

- `InternalIPAddresses`
- `ExternalIPAddresses`
- `DestinationTcpPorts`
- `DestinationUdpPorts`
- `DetectedProtocols`
- `ExternalEmailAddresses`
- `InternalEmailAddresses`
- `ExternalUrls`
- `InternalUrls`
- `PcapResults.Protocols`

**Dependencies:**

- Sub-playbooks: PCAP Parsing And Indicator Enrichment, PCAP Search, PCAP File Carving


## PCAP File Carving

**Product:** PCAP Analysis

This playbook is used to carve (extract) files from within PCAP files and perform enrichment and detonation of the extracted files. Supported PCAP file types are pcap, cap, pcapng. The playbook can handle one PCAP file per incident. Additional inputs allow the user to provide the WPA password for decrypting 802.11 (wireless) traffic and adding an RSA certificate to decrypt SSL traffic. Additional options enable you to filter the files to extract according to the file extension or the actual file type (MIME), and limit the amount of files to extract. Another feature enables you to specify a filter to create a new smaller PCAP file. To display the results within the relevant incident fields, the playbook needs to run in a PCAP Analysis incident type. For handling of PCAP files larger than 30 MB, refer to the PcapMinerV2 documentation

**Inputs:**

- `RsaDecryptKeyEntryID`: This input specifies the file entry id for the RSA decrypt key if the user provided the key in the incident.
- `PcapFileEntryID`: This input specifies the file entry id for the PCAP file if the user provided the file in the incident. One PCAP file can run per incident.
- `WpaPassword`: This input value is used to provide a WPA (Wi-Fi Protected Access) password to decrypt encrypted 802.11 Wi-FI traffic.
- `PcapFilter`: This input specifies a search filter to be used on the PCAP file. Filters can be used to search only for a specific IP, protocols, and other examples. The syntax is the same as in 
- `ExtractedFilesLimit`: This input limits the number of files to be extracted from the PCAP file. Default value is 5.
- `FileExtensionFilter`: This input is used to select which file extensions to include or exclude from the PCAP file. Extensions must be comma separated, for example, png,gif,exe.This setting cannot be use
- `FileTypeFilter`: This input is used to select which file type (MIME type) to include or exclude from the PCAP file. Extensions must be comma separated, for example, image/jpeg,application/x-javascr
- `FilterType`: This input is combined with the FileExtensionFilter input or the FileTypeFilter input. It specifies if the type/extensions list is inclusive or exclusive. Can be "inclusive" or "ex
- `AutoDetonateFiles`: This input specifies whether to detonate files extracted from the PCAP. The default value is True. Any other value will be considered as false.
- `AutoEnrichFiles`: This input specifies whether to enrich files extracted from the PCAP. The default value is True. Any other value will be considered as false.

**Outputs:**

- `DBotScore`
- `File`
- `File.Malicious`
- `File.Size`
- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `File.SHA512`
- `File.Name`
- `File.SSDeep`

**Dependencies:**

- Sub-playbooks: Detonate File - Generic
- Scripts: PcapFileExtractor, Set, PcapMinerV2
- Commands: file


## PCAP Parsing And Indicator Enrichment

**Product:** PCAP Analysis

This playbook is used to parse and extract indicators within PCAP files and perform enrichment on the detected indicators. Supported file types are pcap, cap, pcapng. The playbook can handle one PCAP file per incident. The user inputs which indicator types are to be enriched including, email, URLs, IP addresses. The user can specify in the inputs which indicators are internal or that will be treated as internal (not enriched). The user can also specify a specific regex pattern to search for. Another option is to specify the protocol types to be printed to context for data extraction. Additional inputs allow the user to provide the WPA password for decrypting 802.11 (wireless) traffic and add an RSA certificate to decrypt SSL traffic. To display the results within the relevant incident fields, the playbook needs to run in a PCAP Analysis incident type. For handling of PCAP files larger than 30 MB, refer to the PcapMinerV2 documentation

**Inputs:**

- `PcapFilter`: This input specifies a search filter to be used on the pcap file. Filters can be used to search only for a specific IP, protocols, and other examples. The syntax is the same as in 

**Outputs:**

- `InternalIPAddresses`
- `ExternalIPAddresses`
- `ExternalEmailAddresses`
- `InternalEmailAddresses`
- `ExternalUrls`
- `InternalUrls`
- `PcapResults.Protocols`
- `DestinationTcpPorts`
- `DestinationUdpPorts`

**Dependencies:**

- Scripts: SetGridField, IsUrlPartOfDomain, PcapMinerV2, SetAndHandleEmpty, IsEmailAddressInternal, IsIPInRanges
- Commands: url, ip, email


## PCAP Search

**Product:** PCAP Analysis

This playbook is used to parse and search within PCAP files. Supported file types are pcap, cap, pcapng. The playbook can handle one PCAP file per incident. The user inputs which objects the playbook should search for in the PCAP. The values to search are IP addresses, CIDR ranges, and TCP or UDP ports or protocols. In the event that more than one input type was specified, specify in the QueryOperator input (such as IP addresses and TCP ports) if the PCAP filter query will use an AND or an OR operator between the inputs. Another option is to use advanced filters just like in Wireshark to use refined filters or for objects not specified in other inputs. Additional inputs allow the user to provide the WPA password for decrypting 802.11 (wireless) traffic and adding an RSA certificate to decrypt SSL traffic. To display the results within the relevant incident fields, the playbook needs to run in a PCAP Analysis incident type. For handling of PCAP files larger than 30 MB, refer to the PcapMinerV2 documentation

**Inputs:**

- `QueryOperator`: In case the playbook has several search inputs provided such as IPAddressToSearch, TCPPortsToSearch ,UDPPortsToSearch, ProtocolToSearch and AdvancedSearchFilter. This input will sp
- `IPAddressToSearch`: The value of an IP address to search. Can be a single IP or a comma delimited list of IP addresses. CIDR ranges are also acceptable. All IPs will be treated with the OR operator.
- `TCPPortsToSearch`: The value of a TCP port number to search. Can be a single port or a comma delimited list of ports. All TCP ports will be treated with the OR operator.
- `UDPPortsToSearch`: The value of a UDP port number to search. Can be a single port or a comma delimited list of ports. All UDP ports will be treated with the OR operator.
- `ProtocolToSearch`: The protocols to search for within the PCAP file. Can be a single protocol or a comma delimited list of protocols. The protocol names should be the same as searching in Wireshark. 
- `WpaPassword`: This input value is used to provide a WPA (Wi-Fi Protected Access) password to decrypt encrypted 802.11 Wi-FI traffic.
- `AdvancedSearchFilter`: Filter to apply on PCAP. Wireshark syntax as can be found here: https://www.wireshark.org/docs/man-pages/wireshark-filter.html
- `This input is meant to handle more complex filters not covered by the other inputs. For example search by an attribute such as http.host, arp.dst.hw etc.`: 
- `RsaDecryptKeyEntryID`: This input specifics the file entry id for the RSA decrypt key if the user provided the key in the incident.
- `PcapFileEntryID`: This input specifics the file entry id for the PCAP file if the user provided the file in the incident. One PCAP file can run per incident.

**Outputs:**

- `InternalIPAddresses`
- `ExternalIPAddresses`
- `DestinationTcpPorts`
- `DestinationUdpPorts`
- `DetectedProtocols`
- `PcapQuery`

**Dependencies:**

- Scripts: SetAndHandleEmpty, SetGridField, PcapMinerV2, IsIPInRanges

## Endace Search Archive Download PCAP v2

**Product:** Endace

This playbook uses Endace APIs to search, archive and download PCAP file from either a single EndaceProbe or many via the InvestigationManager. The workflow accepts inputs like “the date and time of the incident or a timeframe”, “source or destination IP address of the incident”, “source or destination IP port of the incident”, “protocol of the incident” and name of archive file. Required Inputs - Either timeframe or start and timeframe or end and timeframe or start and end fields. Either src_host_list or dest_host_list or ip fields. Either src_port_list or dest_port_list or port fields. archive_filename field is required delete_archive field is required download_threshold field is required The Workflow in this playbook

**Inputs:**

- `start`: UTC StartTime in ISO 8601 format as in 2020-04-08T15:46:30
- `end`: UTC EndTime in ISO 8601 format as in 2020-04-08T15:46:30
- `timeframe`: Event timeframe to search. Select one of the values from 30seconds, 1minute, 5minutes, 10minutes, 30minutes, 1hour, 2hours, 5hours, 10hours, 12hours, 1day, 3days, 5days, 1week. Tim
- `ip`: directionless ip address. For valid search either a IP or Src Host or a Dest Host value is required
- `port`: directionless port.
- `src_host_list`: List of comma delimited Source IP addresses to search with a maximum of 10 IP addresses per search. For valid search either a Src Host or a Dest Host value is required.
- `dest_host_list`: List of comma delimited Destination IP addresses to search with a maximum of 10 IP addresses per search. For valid search either a Src Host or a Dest Host value is required.
- `src_port_list`: List of comma delimited Source Port addresses to search with a maximum of 10 Port addresses per search.
- `dest_port_list`: List of comma delimited Destination Port addresses to search with a maximum of 10 Port addresses per search.
- `protocol`: IANA defined IP Protocol Name or Number. For example - either use TCP or tcp or 6 for tcp protocol

**Outputs:**

- `Endace.Download.PCAP.FileName`
- `Endace.Download.PCAP.FileSize`
- `Endace.Download.PCAP.FileUser`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: Endace
- Scripts: IsGreaterThan, IsTrue, Set, AreValuesEqual, Print, AddEvidence
- Commands: endace-create-archive, endace-create-search, endace-delete-archived-file, endace-get-archive-status, endace-download-pcap


## PCAP Analysis

**Product:** PCAP Analysis

This playbook leverages all of the PCAP miner and PCAP file extractor sub playbook capabilities, including: The playbooks is meant to be a demonstration of all the PCAP analysis capabilities however it is more likely to use each of the subplaybooks seperatly. In order to demonstrate the entire flow make sure that at least on of the following playbook inputs is configured in order for search results to exist

**Inputs:**

- `PcapFileEntryID`: This input specifies the file entry ID for the PCAP file if the user provided the file in the incident. One PCAP file can run per incident.
- `RunParsingAndEnrichment`: This input specifies whether to run the parsing and enrichment playbook. Values can be true or any other value for false.
- `RunFileCarving`: This input specifies whether to run the file carving playbook. Values can be true or any other value for false.
- `RsaDecryptKeyEntryID`: This input specifies the file entry ID for the RSA decrypt key if the user provided the key in the incident.
- `WpaPassword`: This input value is used to provide a WPA (Wi-Fi Protected Access) password to decrypt encrypted 802.11 Wi-FI traffic.
- `QueryOperator`: In case the playbook has several search inputs provided such as IPAddressToSearch, TCPPortsToSearch ,UDPPortsToSearch, ProtocolToSearch and AdvancedSearchFilter. This input will sp
- `IPAddressToSearch`: The value of an IP address to search. Can be a single IP or a comma delimited list of IP addresses. CIDR ranges are also acceptable. All IPs will be treated with the OR operator.
- `TCPPortsToSearch`: The value of a TCP port number to search. Can be a single port or a comma delimited list of ports. All TCP ports will be treated with the OR operator.
- `UDPPortsToSearch`: The value of a UDP port number to search. Can be a single port or a comma delimited list of ports. All UDP ports will be treated with the OR operator.
- `ProtocolToSearch`: The protocols to search for within the PCAP file. Can be a single protocol or a comma delimited list of protocols. The protocol names should be the same as searching in Wireshark. 

**Outputs:**

- `InternalIPAddresses`
- `ExternalIPAddresses`
- `DestinationTcpPorts`
- `DestinationUdpPorts`
- `DetectedProtocols`
- `ExternalEmailAddresses`
- `InternalEmailAddresses`
- `ExternalUrls`
- `InternalUrls`
- `PcapResults.Protocols`

**Dependencies:**

- Sub-playbooks: PCAP Parsing And Indicator Enrichment, PCAP Search, PCAP File Carving


## PCAP File Carving

**Product:** PCAP Analysis

This playbook is used to carve (extract) files from within PCAP files and perform enrichment and detonation of the extracted files. Supported PCAP file types are pcap, cap, pcapng. The playbook can handle one PCAP file per incident. Additional inputs allow the user to provide the WPA password for decrypting 802.11 (wireless) traffic and adding an RSA certificate to decrypt SSL traffic. Additional options enable you to filter the files to extract according to the file extension or the actual file type (MIME), and limit the amount of files to extract. Another feature enables you to specify a filter to create a new smaller PCAP file. To display the results within the relevant incident fields, the playbook needs to run in a PCAP Analysis incident type. For handling of PCAP files larger than 30 MB, refer to the PcapMinerV2 documentation

**Inputs:**

- `RsaDecryptKeyEntryID`: This input specifies the file entry id for the RSA decrypt key if the user provided the key in the incident.
- `PcapFileEntryID`: This input specifies the file entry id for the PCAP file if the user provided the file in the incident. One PCAP file can run per incident.
- `WpaPassword`: This input value is used to provide a WPA (Wi-Fi Protected Access) password to decrypt encrypted 802.11 Wi-FI traffic.
- `PcapFilter`: This input specifies a search filter to be used on the PCAP file. Filters can be used to search only for a specific IP, protocols, and other examples. The syntax is the same as in 
- `ExtractedFilesLimit`: This input limits the number of files to be extracted from the PCAP file. Default value is 5.
- `FileExtensionFilter`: This input is used to select which file extensions to include or exclude from the PCAP file. Extensions must be comma separated, for example, png,gif,exe.This setting cannot be use
- `FileTypeFilter`: This input is used to select which file type (MIME type) to include or exclude from the PCAP file. Extensions must be comma separated, for example, image/jpeg,application/x-javascr
- `FilterType`: This input is combined with the FileExtensionFilter input or the FileTypeFilter input. It specifies if the type/extensions list is inclusive or exclusive. Can be "inclusive" or "ex
- `AutoDetonateFiles`: This input specifies whether to detonate files extracted from the PCAP. The default value is True. Any other value will be considered as false.
- `AutoEnrichFiles`: This input specifies whether to enrich files extracted from the PCAP. The default value is True. Any other value will be considered as false.

**Outputs:**

- `DBotScore`
- `File`
- `File.Malicious`
- `File.Size`
- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `File.SHA512`
- `File.Name`
- `File.SSDeep`

**Dependencies:**

- Sub-playbooks: Detonate File - Generic
- Scripts: PcapFileExtractor, Set, PcapMinerV2
- Commands: file


## PCAP Parsing And Indicator Enrichment

**Product:** PCAP Analysis

This playbook is used to parse and extract indicators within PCAP files and perform enrichment on the detected indicators. Supported file types are pcap, cap, pcapng. The playbook can handle one PCAP file per incident. The user inputs which indicator types are to be enriched including, email, URLs, IP addresses. The user can specify in the inputs which indicators are internal or that will be treated as internal (not enriched). The user can also specify a specific regex pattern to search for. Another option is to specify the protocol types to be printed to context for data extraction. Additional inputs allow the user to provide the WPA password for decrypting 802.11 (wireless) traffic and add an RSA certificate to decrypt SSL traffic. To display the results within the relevant incident fields, the playbook needs to run in a PCAP Analysis incident type. For handling of PCAP files larger than 30 MB, refer to the PcapMinerV2 documentation

**Inputs:**

- `PcapFilter`: This input specifies a search filter to be used on the pcap file. Filters can be used to search only for a specific IP, protocols, and other examples. The syntax is the same as in 

**Outputs:**

- `InternalIPAddresses`
- `ExternalIPAddresses`
- `ExternalEmailAddresses`
- `InternalEmailAddresses`
- `ExternalUrls`
- `InternalUrls`
- `PcapResults.Protocols`
- `DestinationTcpPorts`
- `DestinationUdpPorts`

**Dependencies:**

- Scripts: SetGridField, IsUrlPartOfDomain, PcapMinerV2, SetAndHandleEmpty, IsEmailAddressInternal, IsIPInRanges
- Commands: url, ip, email


## PCAP Search

**Product:** PCAP Analysis

This playbook is used to parse and search within PCAP files. Supported file types are pcap, cap, pcapng. The playbook can handle one PCAP file per incident. The user inputs which objects the playbook should search for in the PCAP. The values to search are IP addresses, CIDR ranges, and TCP or UDP ports or protocols. In the event that more than one input type was specified, specify in the QueryOperator input (such as IP addresses and TCP ports) if the PCAP filter query will use an AND or an OR operator between the inputs. Another option is to use advanced filters just like in Wireshark to use refined filters or for objects not specified in other inputs. Additional inputs allow the user to provide the WPA password for decrypting 802.11 (wireless) traffic and adding an RSA certificate to decrypt SSL traffic. To display the results within the relevant incident fields, the playbook needs to run in a PCAP Analysis incident type. For handling of PCAP files larger than 30 MB, refer to the PcapMinerV2 documentation

**Inputs:**

- `QueryOperator`: In case the playbook has several search inputs provided such as IPAddressToSearch, TCPPortsToSearch ,UDPPortsToSearch, ProtocolToSearch and AdvancedSearchFilter. This input will sp
- `IPAddressToSearch`: The value of an IP address to search. Can be a single IP or a comma delimited list of IP addresses. CIDR ranges are also acceptable. All IPs will be treated with the OR operator.
- `TCPPortsToSearch`: The value of a TCP port number to search. Can be a single port or a comma delimited list of ports. All TCP ports will be treated with the OR operator.
- `UDPPortsToSearch`: The value of a UDP port number to search. Can be a single port or a comma delimited list of ports. All UDP ports will be treated with the OR operator.
- `ProtocolToSearch`: The protocols to search for within the PCAP file. Can be a single protocol or a comma delimited list of protocols. The protocol names should be the same as searching in Wireshark. 
- `WpaPassword`: This input value is used to provide a WPA (Wi-Fi Protected Access) password to decrypt encrypted 802.11 Wi-FI traffic.
- `AdvancedSearchFilter`: Filter to apply on PCAP. Wireshark syntax as can be found here: https://www.wireshark.org/docs/man-pages/wireshark-filter.html
- `This input is meant to handle more complex filters not covered by the other inputs. For example search by an attribute such as http.host, arp.dst.hw etc.`: 
- `RsaDecryptKeyEntryID`: This input specifics the file entry id for the RSA decrypt key if the user provided the key in the incident.
- `PcapFileEntryID`: This input specifics the file entry id for the PCAP file if the user provided the file in the incident. One PCAP file can run per incident.

**Outputs:**

- `InternalIPAddresses`
- `ExternalIPAddresses`
- `DestinationTcpPorts`
- `DestinationUdpPorts`
- `DetectedProtocols`
- `PcapQuery`

**Dependencies:**

- Scripts: SetAndHandleEmpty, SetGridField, PcapMinerV2, IsIPInRanges

## Endace Search Archive Download PCAP v2

**Product:** Endace

This playbook uses Endace APIs to search, archive and download PCAP file from either a single EndaceProbe or many via the InvestigationManager. The workflow accepts inputs like “the date and time of the incident or a timeframe”, “source or destination IP address of the incident”, “source or destination IP port of the incident”, “protocol of the incident” and name of archive file. Required Inputs - Either timeframe or start and timeframe or end and timeframe or start and end fields. Either src_host_list or dest_host_list or ip fields. Either src_port_list or dest_port_list or port fields. archive_filename field is required delete_archive field is required download_threshold field is required The Workflow in this playbook

**Inputs:**

- `start`: UTC StartTime in ISO 8601 format as in 2020-04-08T15:46:30
- `end`: UTC EndTime in ISO 8601 format as in 2020-04-08T15:46:30
- `timeframe`: Event timeframe to search. Select one of the values from 30seconds, 1minute, 5minutes, 10minutes, 30minutes, 1hour, 2hours, 5hours, 10hours, 12hours, 1day, 3days, 5days, 1week. Tim
- `ip`: directionless ip address. For valid search either a IP or Src Host or a Dest Host value is required
- `port`: directionless port.
- `src_host_list`: List of comma delimited Source IP addresses to search with a maximum of 10 IP addresses per search. For valid search either a Src Host or a Dest Host value is required.
- `dest_host_list`: List of comma delimited Destination IP addresses to search with a maximum of 10 IP addresses per search. For valid search either a Src Host or a Dest Host value is required.
- `src_port_list`: List of comma delimited Source Port addresses to search with a maximum of 10 Port addresses per search.
- `dest_port_list`: List of comma delimited Destination Port addresses to search with a maximum of 10 Port addresses per search.
- `protocol`: IANA defined IP Protocol Name or Number. For example - either use TCP or tcp or 6 for tcp protocol

**Outputs:**

- `Endace.Download.PCAP.FileName`
- `Endace.Download.PCAP.FileSize`
- `Endace.Download.PCAP.FileUser`

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: Endace
- Scripts: IsGreaterThan, IsTrue, Set, AreValuesEqual, Print, AddEvidence
- Commands: endace-create-archive, endace-create-search, endace-delete-archived-file, endace-get-archive-status, endace-download-pcap


## PCAP Analysis

**Product:** PCAP Analysis

This playbook leverages all of the PCAP miner and PCAP file extractor sub playbook capabilities, including: The playbooks is meant to be a demonstration of all the PCAP analysis capabilities however it is more likely to use each of the subplaybooks seperatly. In order to demonstrate the entire flow make sure that at least on of the following playbook inputs is configured in order for search results to exist

**Inputs:**

- `PcapFileEntryID`: This input specifies the file entry ID for the PCAP file if the user provided the file in the incident. One PCAP file can run per incident.
- `RunParsingAndEnrichment`: This input specifies whether to run the parsing and enrichment playbook. Values can be true or any other value for false.
- `RunFileCarving`: This input specifies whether to run the file carving playbook. Values can be true or any other value for false.
- `RsaDecryptKeyEntryID`: This input specifies the file entry ID for the RSA decrypt key if the user provided the key in the incident.
- `WpaPassword`: This input value is used to provide a WPA (Wi-Fi Protected Access) password to decrypt encrypted 802.11 Wi-FI traffic.
- `QueryOperator`: In case the playbook has several search inputs provided such as IPAddressToSearch, TCPPortsToSearch ,UDPPortsToSearch, ProtocolToSearch and AdvancedSearchFilter. This input will sp
- `IPAddressToSearch`: The value of an IP address to search. Can be a single IP or a comma delimited list of IP addresses. CIDR ranges are also acceptable. All IPs will be treated with the OR operator.
- `TCPPortsToSearch`: The value of a TCP port number to search. Can be a single port or a comma delimited list of ports. All TCP ports will be treated with the OR operator.
- `UDPPortsToSearch`: The value of a UDP port number to search. Can be a single port or a comma delimited list of ports. All UDP ports will be treated with the OR operator.
- `ProtocolToSearch`: The protocols to search for within the PCAP file. Can be a single protocol or a comma delimited list of protocols. The protocol names should be the same as searching in Wireshark. 

**Outputs:**

- `InternalIPAddresses`
- `ExternalIPAddresses`
- `DestinationTcpPorts`
- `DestinationUdpPorts`
- `DetectedProtocols`
- `ExternalEmailAddresses`
- `InternalEmailAddresses`
- `ExternalUrls`
- `InternalUrls`
- `PcapResults.Protocols`

**Dependencies:**

- Sub-playbooks: PCAP Parsing And Indicator Enrichment, PCAP Search, PCAP File Carving


## PCAP File Carving

**Product:** PCAP Analysis

This playbook is used to carve (extract) files from within PCAP files and perform enrichment and detonation of the extracted files. Supported PCAP file types are pcap, cap, pcapng. The playbook can handle one PCAP file per incident. Additional inputs allow the user to provide the WPA password for decrypting 802.11 (wireless) traffic and adding an RSA certificate to decrypt SSL traffic. Additional options enable you to filter the files to extract according to the file extension or the actual file type (MIME), and limit the amount of files to extract. Another feature enables you to specify a filter to create a new smaller PCAP file. To display the results within the relevant incident fields, the playbook needs to run in a PCAP Analysis incident type. For handling of PCAP files larger than 30 MB, refer to the PcapMinerV2 documentation

**Inputs:**

- `RsaDecryptKeyEntryID`: This input specifies the file entry id for the RSA decrypt key if the user provided the key in the incident.
- `PcapFileEntryID`: This input specifies the file entry id for the PCAP file if the user provided the file in the incident. One PCAP file can run per incident.
- `WpaPassword`: This input value is used to provide a WPA (Wi-Fi Protected Access) password to decrypt encrypted 802.11 Wi-FI traffic.
- `PcapFilter`: This input specifies a search filter to be used on the PCAP file. Filters can be used to search only for a specific IP, protocols, and other examples. The syntax is the same as in 
- `ExtractedFilesLimit`: This input limits the number of files to be extracted from the PCAP file. Default value is 5.
- `FileExtensionFilter`: This input is used to select which file extensions to include or exclude from the PCAP file. Extensions must be comma separated, for example, png,gif,exe.This setting cannot be use
- `FileTypeFilter`: This input is used to select which file type (MIME type) to include or exclude from the PCAP file. Extensions must be comma separated, for example, image/jpeg,application/x-javascr
- `FilterType`: This input is combined with the FileExtensionFilter input or the FileTypeFilter input. It specifies if the type/extensions list is inclusive or exclusive. Can be "inclusive" or "ex
- `AutoDetonateFiles`: This input specifies whether to detonate files extracted from the PCAP. The default value is True. Any other value will be considered as false.
- `AutoEnrichFiles`: This input specifies whether to enrich files extracted from the PCAP. The default value is True. Any other value will be considered as false.

**Outputs:**

- `DBotScore`
- `File`
- `File.Malicious`
- `File.Size`
- `File.MD5`
- `File.SHA1`
- `File.SHA256`
- `File.SHA512`
- `File.Name`
- `File.SSDeep`

**Dependencies:**

- Sub-playbooks: Detonate File - Generic
- Scripts: PcapFileExtractor, Set, PcapMinerV2
- Commands: file


## PCAP Parsing And Indicator Enrichment

**Product:** PCAP Analysis

This playbook is used to parse and extract indicators within PCAP files and perform enrichment on the detected indicators. Supported file types are pcap, cap, pcapng. The playbook can handle one PCAP file per incident. The user inputs which indicator types are to be enriched including, email, URLs, IP addresses. The user can specify in the inputs which indicators are internal or that will be treated as internal (not enriched). The user can also specify a specific regex pattern to search for. Another option is to specify the protocol types to be printed to context for data extraction. Additional inputs allow the user to provide the WPA password for decrypting 802.11 (wireless) traffic and add an RSA certificate to decrypt SSL traffic. To display the results within the relevant incident fields, the playbook needs to run in a PCAP Analysis incident type. For handling of PCAP files larger than 30 MB, refer to the PcapMinerV2 documentation

**Inputs:**

- `PcapFilter`: This input specifies a search filter to be used on the pcap file. Filters can be used to search only for a specific IP, protocols, and other examples. The syntax is the same as in 

**Outputs:**

- `InternalIPAddresses`
- `ExternalIPAddresses`
- `ExternalEmailAddresses`
- `InternalEmailAddresses`
- `ExternalUrls`
- `InternalUrls`
- `PcapResults.Protocols`
- `DestinationTcpPorts`
- `DestinationUdpPorts`

**Dependencies:**

- Scripts: SetGridField, IsUrlPartOfDomain, PcapMinerV2, SetAndHandleEmpty, IsEmailAddressInternal, IsIPInRanges
- Commands: url, ip, email


## PCAP Search

**Product:** PCAP Analysis

This playbook is used to parse and search within PCAP files. Supported file types are pcap, cap, pcapng. The playbook can handle one PCAP file per incident. The user inputs which objects the playbook should search for in the PCAP. The values to search are IP addresses, CIDR ranges, and TCP or UDP ports or protocols. In the event that more than one input type was specified, specify in the QueryOperator input (such as IP addresses and TCP ports) if the PCAP filter query will use an AND or an OR operator between the inputs. Another option is to use advanced filters just like in Wireshark to use refined filters or for objects not specified in other inputs. Additional inputs allow the user to provide the WPA password for decrypting 802.11 (wireless) traffic and adding an RSA certificate to decrypt SSL traffic. To display the results within the relevant incident fields, the playbook needs to run in a PCAP Analysis incident type. For handling of PCAP files larger than 30 MB, refer to the PcapMinerV2 documentation

**Inputs:**

- `QueryOperator`: In case the playbook has several search inputs provided such as IPAddressToSearch, TCPPortsToSearch ,UDPPortsToSearch, ProtocolToSearch and AdvancedSearchFilter. This input will sp
- `IPAddressToSearch`: The value of an IP address to search. Can be a single IP or a comma delimited list of IP addresses. CIDR ranges are also acceptable. All IPs will be treated with the OR operator.
- `TCPPortsToSearch`: The value of a TCP port number to search. Can be a single port or a comma delimited list of ports. All TCP ports will be treated with the OR operator.
- `UDPPortsToSearch`: The value of a UDP port number to search. Can be a single port or a comma delimited list of ports. All UDP ports will be treated with the OR operator.
- `ProtocolToSearch`: The protocols to search for within the PCAP file. Can be a single protocol or a comma delimited list of protocols. The protocol names should be the same as searching in Wireshark. 
- `WpaPassword`: This input value is used to provide a WPA (Wi-Fi Protected Access) password to decrypt encrypted 802.11 Wi-FI traffic.
- `AdvancedSearchFilter`: Filter to apply on PCAP. Wireshark syntax as can be found here: https://www.wireshark.org/docs/man-pages/wireshark-filter.html
- `This input is meant to handle more complex filters not covered by the other inputs. For example search by an attribute such as http.host, arp.dst.hw etc.`: 
- `RsaDecryptKeyEntryID`: This input specifics the file entry id for the RSA decrypt key if the user provided the key in the incident.
- `PcapFileEntryID`: This input specifics the file entry id for the PCAP file if the user provided the file in the incident. One PCAP file can run per incident.

**Outputs:**

- `InternalIPAddresses`
- `ExternalIPAddresses`
- `DestinationTcpPorts`
- `DestinationUdpPorts`
- `DetectedProtocols`
- `PcapQuery`

**Dependencies:**

- Scripts: SetAndHandleEmpty, SetGridField, PcapMinerV2, IsIPInRanges

