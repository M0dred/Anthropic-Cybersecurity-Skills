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

## Search Endpoints By Hash - Carbon Black Protection

**Product:** Carbon Black Enterprise Protection

**Kind:** playbook

Hunts for endpoint activity involving hash IOCs, using Carbon Black Protection

**Inputs:**

- `Hash`: The MD5 file Hash to hunt for.

**Dependencies:**

- Integrations: carbonblackprotection
- Scripts: CBPCatalogFindHash, Exists, CBPFindRule, Set
- Commands: cbp-computer-get

## Search Endpoints By Hash - Carbon Black Response V2

**Product:** Carbon Black Enterprise Response

**Kind:** playbook

Hunt for malicious indicators using Carbon Black

**Inputs:**

- `Hash`: MD5 Hash

**Dependencies:**

- Integrations: integration-Carbon_Black_Enterprise_Response
- Commands: cb-get-processes

## Search Endpoints By Hash - Cybereason

**Product:** Cybereason

**Kind:** playbook

Hunt for endpoint activity involving hash, using Cybereason

**Inputs:**

- `MD5Hash`: MD5 Hash
- `SHA1Hash`: SHA1 Hash

**Dependencies:**

- Integrations: Cybereason
- Commands: cybereason-query-file

## Search Endpoints By Hash - TIE

**Product:** McAfee Threat Intelligence Exchange

**Kind:** playbook

Hunt for sightings of MD5, SHA1 and/or SHA256 hashes on endpoints, using McAfee TIE (requires ePO as well). Input: Output

**Inputs:**

- `Hash`: The Hash to hunt (Could be MD5,SHA1,SHA256).Default is set to all hashes

**Dependencies:**

- Integrations: McAfee ePO v2, McAfeeTIEV2, McAfee-TIE
- Commands: epo-find-system, tie-file-references

## Search Endpoints By Hash - Carbon Black Protection

**Product:** Carbon Black Enterprise Protection

**Kind:** playbook

Hunts for endpoint activity involving hash IOCs, using Carbon Black Protection

**Inputs:**

- `Hash`: The MD5 file Hash to hunt for.

**Dependencies:**

- Integrations: carbonblackprotection
- Scripts: CBPCatalogFindHash, Exists, CBPFindRule, Set
- Commands: cbp-computer-get

## Search Endpoints By Hash - Carbon Black Response V2

**Product:** Carbon Black Enterprise Response

**Kind:** playbook

Hunt for malicious indicators using Carbon Black

**Inputs:**

- `Hash`: MD5 Hash

**Dependencies:**

- Integrations: integration-Carbon_Black_Enterprise_Response
- Commands: cb-get-processes

## Search Endpoints By Hash - Cybereason

**Product:** Cybereason

**Kind:** playbook

Hunt for endpoint activity involving hash, using Cybereason

**Inputs:**

- `MD5Hash`: MD5 Hash
- `SHA1Hash`: SHA1 Hash

**Dependencies:**

- Integrations: Cybereason
- Commands: cybereason-query-file

## Search Endpoints By Hash - TIE

**Product:** McAfee Threat Intelligence Exchange

**Kind:** playbook

Hunt for sightings of MD5, SHA1 and/or SHA256 hashes on endpoints, using McAfee TIE (requires ePO as well). Input: Output

**Inputs:**

- `Hash`: The Hash to hunt (Could be MD5,SHA1,SHA256).Default is set to all hashes

**Dependencies:**

- Integrations: McAfee ePO v2, McAfeeTIEV2, McAfee-TIE
- Commands: epo-find-system, tie-file-references

## Search Endpoints By Hash - Carbon Black Protection

**Product:** Carbon Black Enterprise Protection

**Kind:** playbook

Hunts for endpoint activity involving hash IOCs, using Carbon Black Protection

**Inputs:**

- `Hash`: The MD5 file Hash to hunt for.

**Dependencies:**

- Integrations: carbonblackprotection
- Scripts: CBPCatalogFindHash, Exists, CBPFindRule, Set
- Commands: cbp-computer-get

## Search Endpoints By Hash - Carbon Black Response V2

**Product:** Carbon Black Enterprise Response

**Kind:** playbook

Hunt for malicious indicators using Carbon Black

**Inputs:**

- `Hash`: MD5 Hash

**Dependencies:**

- Integrations: integration-Carbon_Black_Enterprise_Response
- Commands: cb-get-processes

## Search Endpoints By Hash - Cybereason

**Product:** Cybereason

**Kind:** playbook

Hunt for endpoint activity involving hash, using Cybereason

**Inputs:**

- `MD5Hash`: MD5 Hash
- `SHA1Hash`: SHA1 Hash

**Dependencies:**

- Integrations: Cybereason
- Commands: cybereason-query-file

## Search Endpoints By Hash - TIE

**Product:** McAfee Threat Intelligence Exchange

**Kind:** playbook

Hunt for sightings of MD5, SHA1 and/or SHA256 hashes on endpoints, using McAfee TIE (requires ePO as well). Input: Output

**Inputs:**

- `Hash`: The Hash to hunt (Could be MD5,SHA1,SHA256).Default is set to all hashes

**Dependencies:**

- Integrations: McAfee ePO v2, McAfeeTIEV2, McAfee-TIE
- Commands: epo-find-system, tie-file-references

