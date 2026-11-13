# Vendor Variants - Handling Incidents Per Nist 800 61

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Cortex ASM - ServiceNow CMDB Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches ServiceNow CMDB information relevant to ASM alerts

**Inputs:**

- `RemoteIP`: IP address of service

**Dependencies:**

- Sub-playbooks: ServiceNow CMDB Search
- Integrations: ServiceNow v2
- Scripts: GridFieldSetup, GetTime
- Commands: servicenow-query-users


## Cortex ASM - ServiceNow ITSM Enrichment

**Product:** Cortex Attack Surface Management

Given search terms, this playbook will query ServiceNow ticket descriptions and short descriptions over the last 30 days and set users that were found in the assigned_to field in those ServiceNow tickets. Note, the max amount of tickets returned from querying is 100

**Inputs:**

- `search_terms`: Search terms to be used in the ServiceNow ITSM query search

**Dependencies:**

- Scripts: GridFieldSetup, GetTime, Set
- Commands: servicenow-get-record, servicenow-query-tickets

