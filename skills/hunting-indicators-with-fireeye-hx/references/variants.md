# Vendor Variants - Hunting Indicators With Fireeye Hx

Vendor-specific implementations, feeds, and collectors for this procedure.


## FireEye HX - Execution Flow Indicators Hunting

**Product:** FireEye HX

**Kind:** playbook

This playbook queries FireEye Endpoint Security (HX) for execution flow indicators, including processes name, registry keys, registry values, and applications. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `Application`: Single or multiple application names or codes to search for within FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without
- `ProcessName`: A single or multiple process names to search for within FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without spaces or 
- `RegistryKey`: A single or multiple registry keys to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `RegistryValue`: A single or multiple registry values to search for within FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without spaces o
- `hostSetName`: The name of host set to be searched.
- `exhaustive`: Whether a search is exhaustive or quick.Possible values are: yes, no. Default is yes.
- `interval_in_seconds`: The interval in seconds between each poll. Default is 60.
- `limit`: Limits the results count (once the limit is reached, the search is stopped).

**Dependencies:**

- Integrations: FireEyeHX v2
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable
- Commands: fireeye-hx-search

## FireEye HX - File Indicators Hunting

**Product:** FireEye HX

**Kind:** playbook

This playbook queries FireEye Endpoint Security (HX) for file indicators, including MD5 hashes, SHA256 hashes, SHA1 hashes, file names, file paths, and file types. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `FileName`: A single or multiple file names to search for FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without spaces or any specia
- `SHA256`: A single or multiple SHA256 file hashes to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA1`: A single or multiple SHA1 file hashes to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `FilePath`: A single or multiple file paths to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `MD5`: A single or multiple MD5 file hashes to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `hostSetName`: The name of host set to be searched.Separate multiple search values by commas only (without spaces or any special characters).
- `exhaustive`: Whether a search is exhaustive or quick.Possible values are: yes, no. Default is yes.
- `interval_in_seconds`: The interval in seconds between each poll. Default is 60.
- `limit`: Limits the results count (once the limit is reached, the search is stopped).

**Dependencies:**

- Integrations: FireEyeHX v2
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty
- Commands: fireeye-hx-search

## FireEye HX - Traffic Indicators Hunting

**Product:** FireEye HX

**Kind:** playbook

This playbook queries FireEye Endpoint Security (HX) for traffic indicators, including IP addresses, URLs, domains, and ports. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: A single or multiple IP address to search for within FireEye HX logs. Used for both source and destination IP addresses.Separate multiple search values by commas only (without spac
- `PortNumber`: A single or multiple port numbers to search for within FireEye HX logs. Used for both remote and local ports.Separate multiple search values by commas only (without spaces or any s
- `URLDomain`: Single or multiple URLs and/or domains to search for within FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without spaces
- `hostSetName`: The name of host set to be searched.
- `interval_in_seconds`: The interval in seconds between each poll. Default is 60.
- `limit`: Limits the results count (once the limit is reached, the search is stopped).
- `exhaustive`: Whether a search is exhaustive or quick.Possible values are: yes, no. Default is yes.

**Dependencies:**

- Integrations: FireEyeHX v2
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable
- Commands: fireeye-hx-search

## FireEye HX - Execution Flow Indicators Hunting

**Product:** FireEye HX

**Kind:** playbook

This playbook queries FireEye Endpoint Security (HX) for execution flow indicators, including processes name, registry keys, registry values, and applications. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `Application`: Single or multiple application names or codes to search for within FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without
- `ProcessName`: A single or multiple process names to search for within FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without spaces or 
- `RegistryKey`: A single or multiple registry keys to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `RegistryValue`: A single or multiple registry values to search for within FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without spaces o
- `hostSetName`: The name of host set to be searched.
- `exhaustive`: Whether a search is exhaustive or quick.Possible values are: yes, no. Default is yes.
- `interval_in_seconds`: The interval in seconds between each poll. Default is 60.
- `limit`: Limits the results count (once the limit is reached, the search is stopped).

**Dependencies:**

- Integrations: FireEyeHX v2
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable
- Commands: fireeye-hx-search

## FireEye HX - File Indicators Hunting

**Product:** FireEye HX

**Kind:** playbook

This playbook queries FireEye Endpoint Security (HX) for file indicators, including MD5 hashes, SHA256 hashes, SHA1 hashes, file names, file paths, and file types. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `FileName`: A single or multiple file names to search for FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without spaces or any specia
- `SHA256`: A single or multiple SHA256 file hashes to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA1`: A single or multiple SHA1 file hashes to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `FilePath`: A single or multiple file paths to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `MD5`: A single or multiple MD5 file hashes to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `hostSetName`: The name of host set to be searched.Separate multiple search values by commas only (without spaces or any special characters).
- `exhaustive`: Whether a search is exhaustive or quick.Possible values are: yes, no. Default is yes.
- `interval_in_seconds`: The interval in seconds between each poll. Default is 60.
- `limit`: Limits the results count (once the limit is reached, the search is stopped).

**Dependencies:**

- Integrations: FireEyeHX v2
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty
- Commands: fireeye-hx-search

## FireEye HX - Traffic Indicators Hunting

**Product:** FireEye HX

**Kind:** playbook

This playbook queries FireEye Endpoint Security (HX) for traffic indicators, including IP addresses, URLs, domains, and ports. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: A single or multiple IP address to search for within FireEye HX logs. Used for both source and destination IP addresses.Separate multiple search values by commas only (without spac
- `PortNumber`: A single or multiple port numbers to search for within FireEye HX logs. Used for both remote and local ports.Separate multiple search values by commas only (without spaces or any s
- `URLDomain`: Single or multiple URLs and/or domains to search for within FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without spaces
- `hostSetName`: The name of host set to be searched.
- `interval_in_seconds`: The interval in seconds between each poll. Default is 60.
- `limit`: Limits the results count (once the limit is reached, the search is stopped).
- `exhaustive`: Whether a search is exhaustive or quick.Possible values are: yes, no. Default is yes.

**Dependencies:**

- Integrations: FireEyeHX v2
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable
- Commands: fireeye-hx-search

## FireEye HX - Execution Flow Indicators Hunting

**Product:** FireEye HX

**Kind:** playbook

This playbook queries FireEye Endpoint Security (HX) for execution flow indicators, including processes name, registry keys, registry values, and applications. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `Application`: Single or multiple application names or codes to search for within FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without
- `ProcessName`: A single or multiple process names to search for within FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without spaces or 
- `RegistryKey`: A single or multiple registry keys to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `RegistryValue`: A single or multiple registry values to search for within FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without spaces o
- `hostSetName`: The name of host set to be searched.
- `exhaustive`: Whether a search is exhaustive or quick.Possible values are: yes, no. Default is yes.
- `interval_in_seconds`: The interval in seconds between each poll. Default is 60.
- `limit`: Limits the results count (once the limit is reached, the search is stopped).

**Dependencies:**

- Integrations: FireEyeHX v2
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable
- Commands: fireeye-hx-search

## FireEye HX - File Indicators Hunting

**Product:** FireEye HX

**Kind:** playbook

This playbook queries FireEye Endpoint Security (HX) for file indicators, including MD5 hashes, SHA256 hashes, SHA1 hashes, file names, file paths, and file types. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `FileName`: A single or multiple file names to search for FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without spaces or any specia
- `SHA256`: A single or multiple SHA256 file hashes to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `SHA1`: A single or multiple SHA1 file hashes to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `FilePath`: A single or multiple file paths to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `FileType`: A single or multiple file types to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `MD5`: A single or multiple MD5 file hashes to search for within FireEye HX logs.Separate multiple search values by commas only (without spaces or any special characters).
- `hostSetName`: The name of host set to be searched.Separate multiple search values by commas only (without spaces or any special characters).
- `exhaustive`: Whether a search is exhaustive or quick.Possible values are: yes, no. Default is yes.
- `interval_in_seconds`: The interval in seconds between each poll. Default is 60.
- `limit`: Limits the results count (once the limit is reached, the search is stopped).

**Dependencies:**

- Integrations: FireEyeHX v2
- Scripts: IsIntegrationAvailable, SetAndHandleEmpty
- Commands: fireeye-hx-search

## FireEye HX - Traffic Indicators Hunting

**Product:** FireEye HX

**Kind:** playbook

This playbook queries FireEye Endpoint Security (HX) for traffic indicators, including IP addresses, URLs, domains, and ports. Note that multiple search values should be separated by commas only (without spaces or any special characters)

**Inputs:**

- `IPAddress`: A single or multiple IP address to search for within FireEye HX logs. Used for both source and destination IP addresses.Separate multiple search values by commas only (without spac
- `PortNumber`: A single or multiple port numbers to search for within FireEye HX logs. Used for both remote and local ports.Separate multiple search values by commas only (without spaces or any s
- `URLDomain`: Single or multiple URLs and/or domains to search for within FireEye HX logs.By default, the 'contains' clause is used.Separate multiple search values by commas only (without spaces
- `hostSetName`: The name of host set to be searched.
- `interval_in_seconds`: The interval in seconds between each poll. Default is 60.
- `limit`: Limits the results count (once the limit is reached, the search is stopped).
- `exhaustive`: Whether a search is exhaustive or quick.Possible values are: yes, no. Default is yes.

**Dependencies:**

- Integrations: FireEyeHX v2
- Scripts: SetAndHandleEmpty, IsIntegrationAvailable
- Commands: fireeye-hx-search

