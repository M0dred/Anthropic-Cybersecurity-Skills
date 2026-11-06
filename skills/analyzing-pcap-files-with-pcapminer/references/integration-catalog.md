# Integration and Automation Catalog - Digital Forensics

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## Anomali Enterprise Forensic Search

**Type:** playbook  
**Product:** Anomali Enterprise  

Initiates a Forensic Search on IOCs in Anomali Match

**Inputs:**

- `from`: First appearance time range e.g., 1 hour, 30 minutes).
- `to`: Last appearance time range e.g., 1 hour, 30 minutes). Default is now.
- `indicators`: Indicators to search.


## Etl2Pcap

**Type:** script  
**Product:** Windows Forensics  

Receives an ETL file and converts it to a PCAP file

**Inputs:**

- `EntryID`: The file entry ID of the ETL File.


## ForescoutEyeInspectButtonGetPCAP

**Type:** script  
**Product:** Forescout EyeInspect  

Get PCAP of a Forescout EyeInspect incident


## Illusive-Collect-Forensics-On-Demand

**Type:** playbook  
**Product:** Illusive Networks  

This playbook is used to collect forensics on-demand on any compromised host and retrieve the forensics timeline upon successful collection

**Inputs:**

- `fqdn_or_ip`: The host fqdn or IP address on which to collect forensics
- `start_date`: The starting date of the forensics timeline.
- ``: Optional
- `end_date`: The last date of the forensics timeline.
- ``: Optional


## PcapConvert

**Type:** script  
**Product:** PCAP Analysis  

Convert packet data to the standard pcap. Currently it only supports CDL(NGFW) pcap from which to convert

**Inputs:**

- `value`: The value to be converted from.
- `path`: The context path to the pcap (e.g., PcapData.pcap). If you add a comma + a node name after the path, the output will be set to the node (e.g
- `pcap_type`: The data type of the pcap data.
- `error_action`: The action on error to parsing pcap. Possible values are abort (default), ignore, and keep.


## PcapExtractStreams

**Type:** script  
**Product:** PCAP Analysis  

Extract payloads of each stream from a pcap. The payloads will be retrieved with an array of dictionaries of these keys

**Inputs:**

- `value`: The data of a pcap in base64 from which to extract streams.
- `path`: The context path to the pcap (e.g., PcapData.pcap). If you add a comma plus a node name after the path, the output will be set to the node (
- `pcap_type`: The data type of the pcap data.
- `bin2txt_mode`: The mode of how to convert the binary to text
- `pcap_filter`: Filter to apply on PCAP. Wireshark syntax as can be found here: https://www.wireshark.org/docs/man-pages/wireshark-filter.html
- `rsa_decrypt_key`: The RSA decryption key in base64.
- `wpa_password`: The WPA password. By providing the password you will be able to decrypt encrypted traffic data.
- `filter_keys`: Keys of output items by which to filter them.


## PcapFileExtractor

**Type:** script  
**Product:** PCAP Analysis  

This automation extracts all possible files from a PCAP file

**Inputs:**

- `entry_id`: The EntryID of the PCAP file to extract the files from.


## PCAPMiner

**Type:** script  
**Product:** Common Scripts  

Parses PCAP files and returns, the extracted files that are found, HTTP flows, and other information. PCAPMiner uses a Docker instance located on the Docker hub trorabaugh/dempcap:1.0. To use this script, upload a PCAP file and then run PCAPMiner entryId="<your_entry_id>". To get the entry ID, click on the link on the top right hand corner of a file attachment

**Inputs:**

- `entryId`: The entryID of the file.
- `demistoLibLocation`: The the platform lib location. The default is "/var/lib/the platform/".


## PWEventPcapDownload

**Type:** script  
**Product:** ProtectWise  

Downloads PCAPs related to the requested events. This supports rate throttling

**Inputs:**

- `eventId`: The event ID(s). (comma-seperated)
- `filename`: The filename for the download.
- `burstsize`: Downloads burstsize files every time, and wait waitms milliseconds each time. The defaults are 10 files and 500ms.
- `waitms`: Downloads burstsize files every time, and wait waitms milliseconds each time. The defaults are 10 files and 500ms.


## PWObservationPcapDownload

**Type:** script  
**Product:** ProtectWise  

Downloads PCAPs related to the specified observations. This supports rate throttling

**Inputs:**

- `id`: The observation ID. Can be, a comma-separated list of IDs.
- `sensorId`: The sensor ID. Can be, a comma-separated list of IDs.
- `filename`: The filename provided for the download.
- `burstsize`: The download burstsize files every time, and wait waitms milliseconds each time. The defaults are 10 files and 1 second.
- `waitms`: The download burstsize files every time, and wait waitms milliseconds each time. The defaults are 10 files and 1 second.

