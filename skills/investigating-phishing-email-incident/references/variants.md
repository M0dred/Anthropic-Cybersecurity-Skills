# Vendor Variants - Investigating Phishing Email Incident

Vendor-specific implementations, feeds, and collectors for this procedure.


## Entity Enrichment - Phishing v2

**Product:** Phishing

**Kind:** playbook

Enrich entities using one or more integrations

**Inputs:**

- `IP`: The IP addresses to enrich
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `MD5`: File MD5 to enrich
- `SHA256`: File SHA256 to enrich
- `SHA1`: File SHA1 to enrich
- `URL`: URL to enrich
- `Email`: The email addresses to enrich
- `Hostname`: The hostname to enrich
- `Username`: The Username to enrich
- `Domain`: The domain name to enrich

**Dependencies:**

- Sub-playbooks: Domain Enrichment - Generic v2, File Enrichment - Generic v2, IP Enrichment - External - Generic v2, URL Enrichment - Generic v2, Email Address Enrichment - Generic v2.1

## Phishing - Core v2

**Product:** Phishing

**Kind:** playbook

This playbook provides a basic response to phishing incidents, including: This updated playbook uses: 1) Incident fields instead of labels 2) The "Process Email - Core v2" playbook

**Inputs:**

- `GetURLScreenshots`: Whether the user wants the Rasterize integration to produce images of URLs involved in the incident. If "True", screenshots are taken.

**Dependencies:**

- Sub-playbooks: Extract Indicators From File - Generic v2, Process Email - Core v2
- Commands: rasterize, rasterize-email, closeInvestigation, setIncident, send-mail

## Phishing - Core

**Product:** Phishing

**Kind:** playbook

Provides a basic response to phishing incidents. Playbook features

**Inputs:**

- `GetURLScreenshots`: Whether the user wants the Rasterize integration to produce images of URLs that are involved in the incident. If "True", screenshots will be taken.

**Dependencies:**

- Sub-playbooks: Process Email - Core, Extract Indicators From File - Generic v2
- Integrations: Builtin
- Commands: rasterize, send-mail, setIncident, rasterize-email, closeInvestigation

## Phishing - Generic v3

**Product:** Phishing

**Kind:** playbook

This playbook investigates and remediates a potential phishing incident. It engages with the user who triggered the incident while investigating the incident itself. Note

**Inputs:**

- `Role`: The default role to assign the incident to.
- `OnCall`: Set to True to assign only the user that is currently on shift.
- `EmailHuntingCreateNewIncidents`: When "True", the "Phishing - Handle Microsoft 365 Defender Results" sub-playbook will open new phishing incidents for each email that contains one of the malicious indicators. Defa
- `ListenerMailbox`: The mailbox which is being used to fetch phishing incidents. This mailbox would be excluded in the "Phishing - Indicators Hunting" playbook.In case the value of this input is empty
- `SendMailInstance`: The name of the instance to be used when executing the "send-mail" command in the playbook. In case it will be empty, all available instances will be used (default).
- `UserEngagement`: Specify whether to engage with the user via email for investigation updates.Set the value to 'True' to allow user engagement, or 'False' to avoid user engagement.
- `TakeManualActions`: Specify whether to stop the playbook to take additional action before closing the incident.Set the value to 'True' to stop the playbook before closing the incidents, or "False" to 
- `NonMaliciousEmailReview`: In case of an incident with a non-malicious email, it is possible either to close the incident or to review and approve it by an analyst.Set the value "True" for a review of the in
- `DetonateURL`: Determines whether to use the "URL Detonation" playbook. Detonating a URL may take a few minutes.
- `InternalRange`: This input is used in the "Entity Enrichment - Phishing v2" playbook.A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR

**Dependencies:**

- Sub-playbooks: Block Indicators - Generic v3, Calculate Severity - Generic v2, Detect & Manage Phishing Campaigns, Detonate File - Generic, Detonate URL - Generic v1.5, Email Address Enrichment - Generic v2.1, Entity Enrichment - Phishing v2, Extract Indicators From File - Generic v2
- Scripts: AssignAnalystToIncident, CheckEmailAuthenticity, Set, SetAndHandleEmpty
- Commands: closeInvestigation, send-mail, setIncident, setIndicator

## Phishing Playbook - Manual

**Product:** Phishing

**Kind:** playbook

Master playbook for phishing incidents. This playbook is a manual playbook

## Spear Phishing Investigation

**Product:** Phishing

**Kind:** playbook

The "Spear Phishing Investigation" playbook is designed to detect patterns that indicates a spear phishing attempt by the attacker

**Inputs:**

- `DomainSquattingResults`: Results of the domain squatting investigation.
- `KeywordsToSearch`: A comma-separated list of keywords to search in the email body.For example: name of the organization finance app that the attacker might impersonate.
- `MailBody`: The phishing mail body.

## Entity Enrichment - Phishing v2

**Product:** Phishing

**Kind:** playbook

Enrich entities using one or more integrations

**Inputs:**

- `IP`: The IP addresses to enrich
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `MD5`: File MD5 to enrich
- `SHA256`: File SHA256 to enrich
- `SHA1`: File SHA1 to enrich
- `URL`: URL to enrich
- `Email`: The email addresses to enrich
- `Hostname`: The hostname to enrich
- `Username`: The Username to enrich
- `Domain`: The domain name to enrich

**Dependencies:**

- Sub-playbooks: Domain Enrichment - Generic v2, File Enrichment - Generic v2, IP Enrichment - External - Generic v2, URL Enrichment - Generic v2, Email Address Enrichment - Generic v2.1

## Phishing - Core v2

**Product:** Phishing

**Kind:** playbook

This playbook provides a basic response to phishing incidents, including: This updated playbook uses: 1) Incident fields instead of labels 2) The "Process Email - Core v2" playbook

**Inputs:**

- `GetURLScreenshots`: Whether the user wants the Rasterize integration to produce images of URLs involved in the incident. If "True", screenshots are taken.

**Dependencies:**

- Sub-playbooks: Extract Indicators From File - Generic v2, Process Email - Core v2
- Commands: rasterize, rasterize-email, closeInvestigation, setIncident, send-mail

## Phishing - Core

**Product:** Phishing

**Kind:** playbook

Provides a basic response to phishing incidents. Playbook features

**Inputs:**

- `GetURLScreenshots`: Whether the user wants the Rasterize integration to produce images of URLs that are involved in the incident. If "True", screenshots will be taken.

**Dependencies:**

- Sub-playbooks: Process Email - Core, Extract Indicators From File - Generic v2
- Integrations: Builtin
- Commands: rasterize, send-mail, setIncident, rasterize-email, closeInvestigation

## Phishing - Generic v3

**Product:** Phishing

**Kind:** playbook

This playbook investigates and remediates a potential phishing incident. It engages with the user who triggered the incident while investigating the incident itself. Note

**Inputs:**

- `Role`: The default role to assign the incident to.
- `OnCall`: Set to True to assign only the user that is currently on shift.
- `EmailHuntingCreateNewIncidents`: When "True", the "Phishing - Handle Microsoft 365 Defender Results" sub-playbook will open new phishing incidents for each email that contains one of the malicious indicators. Defa
- `ListenerMailbox`: The mailbox which is being used to fetch phishing incidents. This mailbox would be excluded in the "Phishing - Indicators Hunting" playbook.In case the value of this input is empty
- `SendMailInstance`: The name of the instance to be used when executing the "send-mail" command in the playbook. In case it will be empty, all available instances will be used (default).
- `UserEngagement`: Specify whether to engage with the user via email for investigation updates.Set the value to 'True' to allow user engagement, or 'False' to avoid user engagement.
- `TakeManualActions`: Specify whether to stop the playbook to take additional action before closing the incident.Set the value to 'True' to stop the playbook before closing the incidents, or "False" to 
- `NonMaliciousEmailReview`: In case of an incident with a non-malicious email, it is possible either to close the incident or to review and approve it by an analyst.Set the value "True" for a review of the in
- `DetonateURL`: Determines whether to use the "URL Detonation" playbook. Detonating a URL may take a few minutes.
- `InternalRange`: This input is used in the "Entity Enrichment - Phishing v2" playbook.A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR

**Dependencies:**

- Sub-playbooks: Block Indicators - Generic v3, Calculate Severity - Generic v2, Detect & Manage Phishing Campaigns, Detonate File - Generic, Detonate URL - Generic v1.5, Email Address Enrichment - Generic v2.1, Entity Enrichment - Phishing v2, Extract Indicators From File - Generic v2
- Scripts: AssignAnalystToIncident, CheckEmailAuthenticity, Set, SetAndHandleEmpty
- Commands: closeInvestigation, send-mail, setIncident, setIndicator

## Phishing Playbook - Manual

**Product:** Phishing

**Kind:** playbook

Master playbook for phishing incidents. This playbook is a manual playbook

## Spear Phishing Investigation

**Product:** Phishing

**Kind:** playbook

The "Spear Phishing Investigation" playbook is designed to detect patterns that indicates a spear phishing attempt by the attacker

**Inputs:**

- `DomainSquattingResults`: Results of the domain squatting investigation.
- `KeywordsToSearch`: A comma-separated list of keywords to search in the email body.For example: name of the organization finance app that the attacker might impersonate.
- `MailBody`: The phishing mail body.

## Entity Enrichment - Phishing v2

**Product:** Phishing

**Kind:** playbook

Enrich entities using one or more integrations

**Inputs:**

- `IP`: The IP addresses to enrich
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.
- `MD5`: File MD5 to enrich
- `SHA256`: File SHA256 to enrich
- `SHA1`: File SHA1 to enrich
- `URL`: URL to enrich
- `Email`: The email addresses to enrich
- `Hostname`: The hostname to enrich
- `Username`: The Username to enrich
- `Domain`: The domain name to enrich

**Dependencies:**

- Sub-playbooks: Domain Enrichment - Generic v2, File Enrichment - Generic v2, IP Enrichment - External - Generic v2, URL Enrichment - Generic v2, Email Address Enrichment - Generic v2.1

## Phishing - Core v2

**Product:** Phishing

**Kind:** playbook

This playbook provides a basic response to phishing incidents, including: This updated playbook uses: 1) Incident fields instead of labels 2) The "Process Email - Core v2" playbook

**Inputs:**

- `GetURLScreenshots`: Whether the user wants the Rasterize integration to produce images of URLs involved in the incident. If "True", screenshots are taken.

**Dependencies:**

- Sub-playbooks: Extract Indicators From File - Generic v2, Process Email - Core v2
- Commands: rasterize, rasterize-email, closeInvestigation, setIncident, send-mail

## Phishing - Core

**Product:** Phishing

**Kind:** playbook

Provides a basic response to phishing incidents. Playbook features

**Inputs:**

- `GetURLScreenshots`: Whether the user wants the Rasterize integration to produce images of URLs that are involved in the incident. If "True", screenshots will be taken.

**Dependencies:**

- Sub-playbooks: Process Email - Core, Extract Indicators From File - Generic v2
- Integrations: Builtin
- Commands: rasterize, send-mail, setIncident, rasterize-email, closeInvestigation

## Phishing - Generic v3

**Product:** Phishing

**Kind:** playbook

This playbook investigates and remediates a potential phishing incident. It engages with the user who triggered the incident while investigating the incident itself. Note

**Inputs:**

- `Role`: The default role to assign the incident to.
- `OnCall`: Set to True to assign only the user that is currently on shift.
- `EmailHuntingCreateNewIncidents`: When "True", the "Phishing - Handle Microsoft 365 Defender Results" sub-playbook will open new phishing incidents for each email that contains one of the malicious indicators. Defa
- `ListenerMailbox`: The mailbox which is being used to fetch phishing incidents. This mailbox would be excluded in the "Phishing - Indicators Hunting" playbook.In case the value of this input is empty
- `SendMailInstance`: The name of the instance to be used when executing the "send-mail" command in the playbook. In case it will be empty, all available instances will be used (default).
- `UserEngagement`: Specify whether to engage with the user via email for investigation updates.Set the value to 'True' to allow user engagement, or 'False' to avoid user engagement.
- `TakeManualActions`: Specify whether to stop the playbook to take additional action before closing the incident.Set the value to 'True' to stop the playbook before closing the incidents, or "False" to 
- `NonMaliciousEmailReview`: In case of an incident with a non-malicious email, it is possible either to close the incident or to review and approve it by an analyst.Set the value "True" for a review of the in
- `DetonateURL`: Determines whether to use the "URL Detonation" playbook. Detonating a URL may take a few minutes.
- `InternalRange`: This input is used in the "Entity Enrichment - Phishing v2" playbook.A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR

**Dependencies:**

- Sub-playbooks: Block Indicators - Generic v3, Calculate Severity - Generic v2, Detect & Manage Phishing Campaigns, Detonate File - Generic, Detonate URL - Generic v1.5, Email Address Enrichment - Generic v2.1, Entity Enrichment - Phishing v2, Extract Indicators From File - Generic v2
- Scripts: AssignAnalystToIncident, CheckEmailAuthenticity, Set, SetAndHandleEmpty
- Commands: closeInvestigation, send-mail, setIncident, setIndicator

## Phishing Playbook - Manual

**Product:** Phishing

**Kind:** playbook

Master playbook for phishing incidents. This playbook is a manual playbook

## Spear Phishing Investigation

**Product:** Phishing

**Kind:** playbook

The "Spear Phishing Investigation" playbook is designed to detect patterns that indicates a spear phishing attempt by the attacker

**Inputs:**

- `DomainSquattingResults`: Results of the domain squatting investigation.
- `KeywordsToSearch`: A comma-separated list of keywords to search in the email body.For example: name of the organization finance app that the attacker might impersonate.
- `MailBody`: The phishing mail body.

