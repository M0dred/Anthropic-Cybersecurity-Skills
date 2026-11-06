# Vendor Variants - Hunting Indicators With Rapid7 Insightidr

Vendor-specific implementations, feeds, and collectors for this procedure.


## Rapid7 InsightIDR - Execution Flow Indicators Hunting

**Product:** Rapid7 InsightIDR

**Kind:** playbook

This playbook queries Rapid7 InsightIDR SIEM for execution flow indicators, including registry values, registry keys, registry hives, commands, processes name, and applications. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `Application`: A single or multiple application names to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRAppField`: The name of the fields, in Rapid7 InsightIDR, in which to find the application names.
- `RegistryValue`: A single or multiple registry values to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRRegistryValueField`: The name of the fields, in Rapid7 InsightIDR, in which to find the registry values.
- `RegistryKey`: A single or multiple registry keys to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRRegistryKeyField`: The name of the fields, in Rapid7 InsightIDR, in which to find the registry keys.
- `RegistryHives`: Only relevant for hunting on Windows hosts.A single or multiple registry hives to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without s
- `InsightIDRRegistryHivesField`: The name of the fields, in Rapid7 InsightIDR, in which to find the registry hives.
- `CommandLine`: A single or multiple command to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRCommandLineField`: The name of the fields, in Rapid7 InsightIDR, in which to find the command's lines.

**Dependencies:**

- Integrations: Rapid7 InsightIDR
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable, LoadJSON
- Commands: rapid7-insight-idr-query-log-set

## Rapid7 InsightIDR - File Indicators Hunting

**Product:** Rapid7 InsightIDR

**Kind:** playbook

This playbook queries Rapid7 InsightIDR SIEM for file indicators, including MD5 hashes, SHA256 hashes, SHA1 hashes, file names, file types, and file paths. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `FileType`: A single or multiple file types to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRFileTypeField`: The name of the fields, in Rapid7 InsightIDR, in which to find the file types.
- `FileName`: A single or multiple file names to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRFileNameField`: The name of the fields, in Rapid7 InsightIDR, in which to find the file names.
- `MD5`: A single or multiple MD5 file hashes to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRMD5Field`: The name of the fields, in Rapid7 InsightIDR, in which to find the MD5 hashes.
- `SHA256`: A single or multiple SHA256 file hashes to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRSHA256Field`: The name of the fields, in Rapid7 InsightIDR, in which to find the SHA256 hashes.
- `SHA1`: A single or multiple SHA1 file hashes to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRSHA1Field`: The name of the fields, in Rapid7 InsightIDR, in which to find the SHA1 hashes.

**Dependencies:**

- Integrations: Rapid7 InsightIDR
- Scripts: IsIntegrationAvailable, LoadJSON, SetAndHandleEmpty
- Commands: rapid7-insight-idr-query-log-set

## Rapid7 InsightIDR - HTTP Requests Indicators Hunting

**Product:** Rapid7 InsightIDR

**Kind:** playbook

This playbook queries Rapid7 InsightIDR SIEM for indicators associated with HTTP requests, including HTTP request methods, user agents, URIs, and Ja3. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `UserAgent`: A single or multiple user agents to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRUserAgentField`: The name of the fields, in Rapid7 InsightIDR, in which to find the user agents.
- `URI`: A single or multiple URIs to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRURIField`: The name of the fields, in Rapid7 InsightIDR, in which to find the URIs.
- `HTTPRequestMethods`: A single or multiple HTTP requests methods to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRHttpMethodsField`: The name of the fields, in Rapid7 InsightIDR, in which to find the HTTP request methods.
- `Ja3`: A single or multiple Ja3s to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).JA3 is a method for 
- `InsightIDRJa3Field`: The name of the fields, in Rapid7 InsightIDR, in which to find the Ja3s.
- `LogSetId`: An identifier for a Rapid7 InsightIDR log set to query.
- `time_range`: Specify the timeframe in which the Rapid7 InsightIDR logs will be searched. Most start with 'last' (e.g., last 2 months, last 10 minutes).The 'start_time' and 'end_time' inputs sho

**Dependencies:**

- Integrations: Rapid7 InsightIDR
- Scripts: SetAndHandleEmpty, LoadJSON, IsIntegrationAvailable
- Commands: rapid7-insight-idr-query-log-set

## Rapid7 InsightIDR - Traffic Indicators Hunting

**Product:** Rapid7 InsightIDR

**Kind:** playbook

This playbook queries Rapid7 InsightIDR SIEM for traffic indicators, including URLs, domains, ports, IP addresses, IP ranges (CIDR), email addresses, and geolocations. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: A single or multiple IP addresses to search for within Rapid7 InsightIDR logs. Used for both source and destination IP addresses.Separate multiple search values by commas only (wit
- `InsightIDRdstIPField`: The name of the fields, in Rapid7 InsightIDR, in which to find the destination IPs.
- `InsightIDRsrcIPField`: The name of the fields, in Rapid7 InsightIDR, in which to find the source IPs.
- `PortNumber`: A single or multiple IP addresses to search for within Rapid7 InsightIDR logs. Used for both source and destination ports.Separate multiple search values by commas only (without sp
- `InsightIDRsrcPortField`: The name of the fields, in Rapid7 InsightIDR, in which to find the source ports.
- `InsightIDRdstPortField`: The name of the fields, in Rapid7 InsightIDR, in which to find the destination ports.
- `Geolocation`: A single or multiple country names or codes to search for within Rapid7 InsightIDR logs. Used for both source and destination geolocations.Separate multiple search values by commas
- `InsightIDRsrcGeolocationField`: The name of the fields, in Rapid7 InsightIDR, in which to find the source geolocations.
- `InsightIDRSdstGeolocationField`: The name of the fields, in Rapid7 InsightIDR, in which to find the destination geolocations.
- `URLDomain`: Single or multiple URLs and/or domains to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).

**Dependencies:**

- Integrations: Rapid7 InsightIDR
- Scripts: LoadJSON, IsIntegrationAvailable, SetAndHandleEmpty
- Commands: rapid7-insight-idr-query-log-set

## Rapid7 InsightIDR - Execution Flow Indicators Hunting

**Product:** Rapid7 InsightIDR

**Kind:** playbook

This playbook queries Rapid7 InsightIDR SIEM for execution flow indicators, including registry values, registry keys, registry hives, commands, processes name, and applications. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `Application`: A single or multiple application names to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRAppField`: The name of the fields, in Rapid7 InsightIDR, in which to find the application names.
- `RegistryValue`: A single or multiple registry values to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRRegistryValueField`: The name of the fields, in Rapid7 InsightIDR, in which to find the registry values.
- `RegistryKey`: A single or multiple registry keys to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRRegistryKeyField`: The name of the fields, in Rapid7 InsightIDR, in which to find the registry keys.
- `RegistryHives`: Only relevant for hunting on Windows hosts.A single or multiple registry hives to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without s
- `InsightIDRRegistryHivesField`: The name of the fields, in Rapid7 InsightIDR, in which to find the registry hives.
- `CommandLine`: A single or multiple command to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRCommandLineField`: The name of the fields, in Rapid7 InsightIDR, in which to find the command's lines.

**Dependencies:**

- Integrations: Rapid7 InsightIDR
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable, LoadJSON
- Commands: rapid7-insight-idr-query-log-set

## Rapid7 InsightIDR - File Indicators Hunting

**Product:** Rapid7 InsightIDR

**Kind:** playbook

This playbook queries Rapid7 InsightIDR SIEM for file indicators, including MD5 hashes, SHA256 hashes, SHA1 hashes, file names, file types, and file paths. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `FileType`: A single or multiple file types to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRFileTypeField`: The name of the fields, in Rapid7 InsightIDR, in which to find the file types.
- `FileName`: A single or multiple file names to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRFileNameField`: The name of the fields, in Rapid7 InsightIDR, in which to find the file names.
- `MD5`: A single or multiple MD5 file hashes to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRMD5Field`: The name of the fields, in Rapid7 InsightIDR, in which to find the MD5 hashes.
- `SHA256`: A single or multiple SHA256 file hashes to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRSHA256Field`: The name of the fields, in Rapid7 InsightIDR, in which to find the SHA256 hashes.
- `SHA1`: A single or multiple SHA1 file hashes to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRSHA1Field`: The name of the fields, in Rapid7 InsightIDR, in which to find the SHA1 hashes.

**Dependencies:**

- Integrations: Rapid7 InsightIDR
- Scripts: IsIntegrationAvailable, LoadJSON, SetAndHandleEmpty
- Commands: rapid7-insight-idr-query-log-set

## Rapid7 InsightIDR - HTTP Requests Indicators Hunting

**Product:** Rapid7 InsightIDR

**Kind:** playbook

This playbook queries Rapid7 InsightIDR SIEM for indicators associated with HTTP requests, including HTTP request methods, user agents, URIs, and Ja3. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `UserAgent`: A single or multiple user agents to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRUserAgentField`: The name of the fields, in Rapid7 InsightIDR, in which to find the user agents.
- `URI`: A single or multiple URIs to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRURIField`: The name of the fields, in Rapid7 InsightIDR, in which to find the URIs.
- `HTTPRequestMethods`: A single or multiple HTTP requests methods to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRHttpMethodsField`: The name of the fields, in Rapid7 InsightIDR, in which to find the HTTP request methods.
- `Ja3`: A single or multiple Ja3s to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).JA3 is a method for 
- `InsightIDRJa3Field`: The name of the fields, in Rapid7 InsightIDR, in which to find the Ja3s.
- `LogSetId`: An identifier for a Rapid7 InsightIDR log set to query.
- `time_range`: Specify the timeframe in which the Rapid7 InsightIDR logs will be searched. Most start with 'last' (e.g., last 2 months, last 10 minutes).The 'start_time' and 'end_time' inputs sho

**Dependencies:**

- Integrations: Rapid7 InsightIDR
- Scripts: SetAndHandleEmpty, LoadJSON, IsIntegrationAvailable
- Commands: rapid7-insight-idr-query-log-set

## Rapid7 InsightIDR - Traffic Indicators Hunting

**Product:** Rapid7 InsightIDR

**Kind:** playbook

This playbook queries Rapid7 InsightIDR SIEM for traffic indicators, including URLs, domains, ports, IP addresses, IP ranges (CIDR), email addresses, and geolocations. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: A single or multiple IP addresses to search for within Rapid7 InsightIDR logs. Used for both source and destination IP addresses.Separate multiple search values by commas only (wit
- `InsightIDRdstIPField`: The name of the fields, in Rapid7 InsightIDR, in which to find the destination IPs.
- `InsightIDRsrcIPField`: The name of the fields, in Rapid7 InsightIDR, in which to find the source IPs.
- `PortNumber`: A single or multiple IP addresses to search for within Rapid7 InsightIDR logs. Used for both source and destination ports.Separate multiple search values by commas only (without sp
- `InsightIDRsrcPortField`: The name of the fields, in Rapid7 InsightIDR, in which to find the source ports.
- `InsightIDRdstPortField`: The name of the fields, in Rapid7 InsightIDR, in which to find the destination ports.
- `Geolocation`: A single or multiple country names or codes to search for within Rapid7 InsightIDR logs. Used for both source and destination geolocations.Separate multiple search values by commas
- `InsightIDRsrcGeolocationField`: The name of the fields, in Rapid7 InsightIDR, in which to find the source geolocations.
- `InsightIDRSdstGeolocationField`: The name of the fields, in Rapid7 InsightIDR, in which to find the destination geolocations.
- `URLDomain`: Single or multiple URLs and/or domains to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).

**Dependencies:**

- Integrations: Rapid7 InsightIDR
- Scripts: LoadJSON, IsIntegrationAvailable, SetAndHandleEmpty
- Commands: rapid7-insight-idr-query-log-set

## Rapid7 InsightIDR - Execution Flow Indicators Hunting

**Product:** Rapid7 InsightIDR

**Kind:** playbook

This playbook queries Rapid7 InsightIDR SIEM for execution flow indicators, including registry values, registry keys, registry hives, commands, processes name, and applications. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `Application`: A single or multiple application names to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRAppField`: The name of the fields, in Rapid7 InsightIDR, in which to find the application names.
- `RegistryValue`: A single or multiple registry values to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRRegistryValueField`: The name of the fields, in Rapid7 InsightIDR, in which to find the registry values.
- `RegistryKey`: A single or multiple registry keys to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRRegistryKeyField`: The name of the fields, in Rapid7 InsightIDR, in which to find the registry keys.
- `RegistryHives`: Only relevant for hunting on Windows hosts.A single or multiple registry hives to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without s
- `InsightIDRRegistryHivesField`: The name of the fields, in Rapid7 InsightIDR, in which to find the registry hives.
- `CommandLine`: A single or multiple command to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRCommandLineField`: The name of the fields, in Rapid7 InsightIDR, in which to find the command's lines.

**Dependencies:**

- Integrations: Rapid7 InsightIDR
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable, LoadJSON
- Commands: rapid7-insight-idr-query-log-set

## Rapid7 InsightIDR - File Indicators Hunting

**Product:** Rapid7 InsightIDR

**Kind:** playbook

This playbook queries Rapid7 InsightIDR SIEM for file indicators, including MD5 hashes, SHA256 hashes, SHA1 hashes, file names, file types, and file paths. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `FileType`: A single or multiple file types to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRFileTypeField`: The name of the fields, in Rapid7 InsightIDR, in which to find the file types.
- `FileName`: A single or multiple file names to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRFileNameField`: The name of the fields, in Rapid7 InsightIDR, in which to find the file names.
- `MD5`: A single or multiple MD5 file hashes to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRMD5Field`: The name of the fields, in Rapid7 InsightIDR, in which to find the MD5 hashes.
- `SHA256`: A single or multiple SHA256 file hashes to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRSHA256Field`: The name of the fields, in Rapid7 InsightIDR, in which to find the SHA256 hashes.
- `SHA1`: A single or multiple SHA1 file hashes to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRSHA1Field`: The name of the fields, in Rapid7 InsightIDR, in which to find the SHA1 hashes.

**Dependencies:**

- Integrations: Rapid7 InsightIDR
- Scripts: IsIntegrationAvailable, LoadJSON, SetAndHandleEmpty
- Commands: rapid7-insight-idr-query-log-set

## Rapid7 InsightIDR - HTTP Requests Indicators Hunting

**Product:** Rapid7 InsightIDR

**Kind:** playbook

This playbook queries Rapid7 InsightIDR SIEM for indicators associated with HTTP requests, including HTTP request methods, user agents, URIs, and Ja3. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `UserAgent`: A single or multiple user agents to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRUserAgentField`: The name of the fields, in Rapid7 InsightIDR, in which to find the user agents.
- `URI`: A single or multiple URIs to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRURIField`: The name of the fields, in Rapid7 InsightIDR, in which to find the URIs.
- `HTTPRequestMethods`: A single or multiple HTTP requests methods to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).
- `InsightIDRHttpMethodsField`: The name of the fields, in Rapid7 InsightIDR, in which to find the HTTP request methods.
- `Ja3`: A single or multiple Ja3s to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).JA3 is a method for 
- `InsightIDRJa3Field`: The name of the fields, in Rapid7 InsightIDR, in which to find the Ja3s.
- `LogSetId`: An identifier for a Rapid7 InsightIDR log set to query.
- `time_range`: Specify the timeframe in which the Rapid7 InsightIDR logs will be searched. Most start with 'last' (e.g., last 2 months, last 10 minutes).The 'start_time' and 'end_time' inputs sho

**Dependencies:**

- Integrations: Rapid7 InsightIDR
- Scripts: SetAndHandleEmpty, LoadJSON, IsIntegrationAvailable
- Commands: rapid7-insight-idr-query-log-set

## Rapid7 InsightIDR - Traffic Indicators Hunting

**Product:** Rapid7 InsightIDR

**Kind:** playbook

This playbook queries Rapid7 InsightIDR SIEM for traffic indicators, including URLs, domains, ports, IP addresses, IP ranges (CIDR), email addresses, and geolocations. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: A single or multiple IP addresses to search for within Rapid7 InsightIDR logs. Used for both source and destination IP addresses.Separate multiple search values by commas only (wit
- `InsightIDRdstIPField`: The name of the fields, in Rapid7 InsightIDR, in which to find the destination IPs.
- `InsightIDRsrcIPField`: The name of the fields, in Rapid7 InsightIDR, in which to find the source IPs.
- `PortNumber`: A single or multiple IP addresses to search for within Rapid7 InsightIDR logs. Used for both source and destination ports.Separate multiple search values by commas only (without sp
- `InsightIDRsrcPortField`: The name of the fields, in Rapid7 InsightIDR, in which to find the source ports.
- `InsightIDRdstPortField`: The name of the fields, in Rapid7 InsightIDR, in which to find the destination ports.
- `Geolocation`: A single or multiple country names or codes to search for within Rapid7 InsightIDR logs. Used for both source and destination geolocations.Separate multiple search values by commas
- `InsightIDRsrcGeolocationField`: The name of the fields, in Rapid7 InsightIDR, in which to find the source geolocations.
- `InsightIDRSdstGeolocationField`: The name of the fields, in Rapid7 InsightIDR, in which to find the destination geolocations.
- `URLDomain`: Single or multiple URLs and/or domains to search for within Rapid7 InsightIDR logs.Separate multiple search values by commas only (without spaces or any special characters).

**Dependencies:**

- Integrations: Rapid7 InsightIDR
- Scripts: LoadJSON, IsIntegrationAvailable, SetAndHandleEmpty
- Commands: rapid7-insight-idr-query-log-set

