# Vendor Variants - Enriching Domains With Threat Intelligence

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Cortex ASM - Domain Enrichment

**Product:** Cortex Attack Surface Management

Playbook to enrich domain information

**Inputs:**

- `Hostname`: Input for domain enrichment.

**Dependencies:**

- Scripts: Set, GridFieldSetup


## Social Engineering Domain Enrichment

**Product:** Social Engineering Domain Analysis

Enrich a domain and compare against your registered domain for potential social engineering against your organization

**Inputs:**

- `RegisteredDomain`: Your company domain to use for checking if potential InputDomains are potentially used for typosquatting and other similar domain attacks.
- `InputDomain`: The potentially malicious domain to check
- `BadNameservers`: The csv of known bad nameserversExample:nameserverexamplenameserver1examplenameserver2examplenameserver3
- `LevenshteinDistance`: The Levenshtein distance to consider close. Lower scores mean strings are more similar

**Dependencies:**

- Integrations: Rasterize
- Scripts: GetStringsDistance, AddDBotScoreToContext, GetListRow, DeleteContext, GetDomainDNSDetails
- Commands: setIndicator, rasterize, enrichIndicators, whois, createNewIndicator

## Cortex ASM - Domain Enrichment

**Product:** Cortex Attack Surface Management

Playbook to enrich domain information

**Inputs:**

- `Hostname`: Input for domain enrichment.

**Dependencies:**

- Scripts: Set, GridFieldSetup


## Social Engineering Domain Enrichment

**Product:** Social Engineering Domain Analysis

Enrich a domain and compare against your registered domain for potential social engineering against your organization

**Inputs:**

- `RegisteredDomain`: Your company domain to use for checking if potential InputDomains are potentially used for typosquatting and other similar domain attacks.
- `InputDomain`: The potentially malicious domain to check
- `BadNameservers`: The csv of known bad nameserversExample:nameserverexamplenameserver1examplenameserver2examplenameserver3
- `LevenshteinDistance`: The Levenshtein distance to consider close. Lower scores mean strings are more similar

**Dependencies:**

- Integrations: Rasterize
- Scripts: GetStringsDistance, AddDBotScoreToContext, GetListRow, DeleteContext, GetDomainDNSDetails
- Commands: setIndicator, rasterize, enrichIndicators, whois, createNewIndicator

## Cortex ASM - Domain Enrichment

**Product:** Cortex Attack Surface Management

Playbook to enrich domain information

**Inputs:**

- `Hostname`: Input for domain enrichment.

**Dependencies:**

- Scripts: Set, GridFieldSetup


## Social Engineering Domain Enrichment

**Product:** Social Engineering Domain Analysis

Enrich a domain and compare against your registered domain for potential social engineering against your organization

**Inputs:**

- `RegisteredDomain`: Your company domain to use for checking if potential InputDomains are potentially used for typosquatting and other similar domain attacks.
- `InputDomain`: The potentially malicious domain to check
- `BadNameservers`: The csv of known bad nameserversExample:nameserverexamplenameserver1examplenameserver2examplenameserver3
- `LevenshteinDistance`: The Levenshtein distance to consider close. Lower scores mean strings are more similar

**Dependencies:**

- Integrations: Rasterize
- Scripts: GetStringsDistance, AddDBotScoreToContext, GetListRow, DeleteContext, GetDomainDNSDetails
- Commands: setIndicator, rasterize, enrichIndicators, whois, createNewIndicator

## Cortex ASM - Domain Enrichment

**Product:** Cortex Attack Surface Management

Playbook to enrich domain information

**Inputs:**

- `Hostname`: Input for domain enrichment.

**Dependencies:**

- Scripts: Set, GridFieldSetup


## Social Engineering Domain Enrichment

**Product:** Social Engineering Domain Analysis

Enrich a domain and compare against your registered domain for potential social engineering against your organization

**Inputs:**

- `RegisteredDomain`: Your company domain to use for checking if potential InputDomains are potentially used for typosquatting and other similar domain attacks.
- `InputDomain`: The potentially malicious domain to check
- `BadNameservers`: The csv of known bad nameserversExample:nameserverexamplenameserver1examplenameserver2examplenameserver3
- `LevenshteinDistance`: The Levenshtein distance to consider close. Lower scores mean strings are more similar

**Dependencies:**

- Integrations: Rasterize
- Scripts: GetStringsDistance, AddDBotScoreToContext, GetListRow, DeleteContext, GetDomainDNSDetails
- Commands: setIndicator, rasterize, enrichIndicators, whois, createNewIndicator

