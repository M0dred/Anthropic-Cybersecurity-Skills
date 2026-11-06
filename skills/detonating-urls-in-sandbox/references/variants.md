# Vendor Variants - Detonating Urls In Sandbox

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## URL Scan - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook scans URLs using GTI private scanning and evaluates the results against GTI assessment parameters, including Threat Score, Severity, and Verdict. URLs that meet the defined high-risk criteria are returned for further action

**Inputs:**

- `url`: Provide url for Private Scanning.

**Outputs:**

- `url_output_list`

**Dependencies:**

- Scripts: Set
- Commands: gti-private-url-scan-and-analysis-get, gti-privatescanning-url

## URL Scan - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook scans URLs using GTI private scanning and evaluates the results against GTI assessment parameters, including Threat Score, Severity, and Verdict. URLs that meet the defined high-risk criteria are returned for further action

**Inputs:**

- `url`: Provide url for Private Scanning.

**Outputs:**

- `url_output_list`

**Dependencies:**

- Scripts: Set
- Commands: gti-private-url-scan-and-analysis-get, gti-privatescanning-url

## URL Scan - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook scans URLs using GTI private scanning and evaluates the results against GTI assessment parameters, including Threat Score, Severity, and Verdict. URLs that meet the defined high-risk criteria are returned for further action

**Inputs:**

- `url`: Provide url for Private Scanning.

**Outputs:**

- `url_output_list`

**Dependencies:**

- Scripts: Set
- Commands: gti-private-url-scan-and-analysis-get, gti-privatescanning-url

## URL Scan - Google Threat Intelligence

**Product:** GoogleThreatIntelligence

This playbook scans URLs using GTI private scanning and evaluates the results against GTI assessment parameters, including Threat Score, Severity, and Verdict. URLs that meet the defined high-risk criteria are returned for further action

**Inputs:**

- `url`: Provide url for Private Scanning.

**Outputs:**

- `url_output_list`

**Dependencies:**

- Scripts: Set
- Commands: gti-private-url-scan-and-analysis-get, gti-privatescanning-url

## Detonate URL - Generic

**Product:** Common Playbooks

**Kind:** playbook

Detonate URL through active integrations that support URL detonation

**Inputs:**

- `URL`: The URL object of the URL to be detonated.

**Dependencies:**

- Sub-playbooks: Detonate URL - JoeSecurity, Detonate URL - Hybrid Analysis, Detonate URL - Lastline v2, Detonate URL - ThreatGrid, Detonate URL - WildFire v2.1, Detonate URL - McAfee ATD, Detonate URL - ANYRUN, Detonate URL - Group-IB TDS Polygon
- Integrations: CrowdStrike Falcon Sandbox V2, OPSWAT Filescan
- Commands: cs-falcon-sandbox-submit-url, opswat-filescan-scan-url

## Detonate URL - Generic

**Product:** Common Playbooks

**Kind:** playbook

Detonate URL through active integrations that support URL detonation

**Inputs:**

- `URL`: The URL object of the URL to be detonated.

**Dependencies:**

- Sub-playbooks: Detonate URL - JoeSecurity, Detonate URL - Hybrid Analysis, Detonate URL - Lastline v2, Detonate URL - ThreatGrid, Detonate URL - WildFire v2.1, Detonate URL - McAfee ATD, Detonate URL - ANYRUN, Detonate URL - Group-IB TDS Polygon
- Integrations: CrowdStrike Falcon Sandbox V2, OPSWAT Filescan
- Commands: cs-falcon-sandbox-submit-url, opswat-filescan-scan-url

## Detonate URL - Generic

**Product:** Common Playbooks

**Kind:** playbook

Detonate URL through active integrations that support URL detonation

**Inputs:**

- `URL`: The URL object of the URL to be detonated.

**Dependencies:**

- Sub-playbooks: Detonate URL - JoeSecurity, Detonate URL - Hybrid Analysis, Detonate URL - Lastline v2, Detonate URL - ThreatGrid, Detonate URL - WildFire v2.1, Detonate URL - McAfee ATD, Detonate URL - ANYRUN, Detonate URL - Group-IB TDS Polygon
- Integrations: CrowdStrike Falcon Sandbox V2, OPSWAT Filescan
- Commands: cs-falcon-sandbox-submit-url, opswat-filescan-scan-url

