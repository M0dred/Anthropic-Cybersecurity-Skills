# Vendor Variants - Searching Endpoints By Hash

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## CrowdStrike Falcon - Search Endpoints By Indicators

**Product:** CrowdStrike Falcon

This playbooks searches for different indicators (IP,IPV6,File hashes,Domain) in the crowdstrike falcon console. The output will be all the endpoitns found associated with provided indicators. Provided agent id as an input will be excluded from the returned list

**Inputs:**

- `FileSha256`: The SHA256 file hash to search for.
- `HostId`: The host ID which will be excluded from the results.
- `SHA1`: The SHA1 file hash to search for.
- `MD5`: The MD5 file hash to search for.
- `IP`: The IPV4 indicator to search for.
- `Domain`: The Domain Indicator to search for.
- `IPV6`: The IPv6 Indicator to search for.

**Outputs:**

- `Endpoint`
- `CrowdStrike.IOC.DeviceCount`
- `Endpoint.Hostname`
- `CrowdStrike.IOC.Type`
- `Endpoint.IPAddress`
- `CrowdStrike.IOC.Value`
- `Endpoint.OS`
- `Endpoint.Status`
- `Endpoint.IsIsolated`
- `CrowdStrike.DeviceID`

**Dependencies:**

- Integrations: CrowdStrikeFalcon, CrowdstrikeFalcon
- Commands: cs-falcon-device-count-ioc, cs-falcon-device-ran-on, endpoint

