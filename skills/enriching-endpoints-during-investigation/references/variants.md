# Vendor Variants - Enriching Endpoints During Investigation

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Cortex ASM - Cortex Endpoint Enrichment

**Product:** Cortex Attack Surface Management

This playbook is used to pull information from  Endpoint (XSIAM/XDR) systems for enrichment purposes

**Inputs:**

- `RemoteIP`: IP address of the service.

**Dependencies:**

- Integrations: Cortex Core - IR, Cortex XDR - IR
- Scripts: GridFieldSetup, Set
- Commands: core-get-endpoints, xdr-get-endpoints, extractIndicators


## Endpoint Enrichment By EntityId - XM Cyber

**Product:** XM Cyber

Enrich an endpoint by entityId using XM Cyber integration. Outputs include affected assets, affected entities, complexity of compromise, and more

**Inputs:**

- `EntityId`: The entityId of the endpoint to enrich.

**Outputs:**

- `Endpoint`
- `Endpoint.Hostname`
- `Endpoint.OS`
- `Endpoint.IP`
- `XMCyber.Entity.isAsset`
- `XMCyber.Entity.affectedEntities`
- `XMCyber.Entity.averageComplexity`
- `XMCyber.Entity.criticalAssetsAtRisk`
- `XMCyber.Entity.averageComplexityLevel`
- `XMCyber.Entity.id`

**Dependencies:**

- Integrations: XMCyber
- Scripts: IsIntegrationAvailable
- Commands: xmcyber-enrich-from-entityId, xmcyber-affected-critical-assets-list, xmcyber-affected-entities-list


## Endpoint Enrichment By Hostname - XM Cyber

**Product:** XM Cyber

Enrich an endpoint by entityId using XM Cyber integration. Outputs include affected assets, affected entities, complexity of compromise, and more

**Inputs:**

- `Hostname`: The hostname of the endpoint to enrich.

**Outputs:**

- `Endpoint`
- `Endpoint.Hostname`
- `Endpoint.OS`
- `Endpoint.IP`
- `XMCyber.Entity.isAsset`
- `XMCyber.Entity.affectedEntities`
- `XMCyber.Entity.averageComplexity`
- `XMCyber.Entity.criticalAssetsAtRisk`
- `XMCyber.Entity.averageComplexityLevel`
- `XMCyber.Entity.id`

**Dependencies:**

- Integrations: XMCyber
- Scripts: IsIntegrationAvailable
- Commands: xmcyber-enrich-from-hostname, xmcyber-affected-critical-assets-list, xmcyber-affected-entities-list


## Endpoint Enrichment By IP - XM Cyber

**Product:** XM Cyber

Enrich an endpoint by IP addresses using XM Cyber integration

**Inputs:**

- `IP`: The IP address to enrich.

**Outputs:**

- `Endpoint`
- `Endpoint.Hostname`
- `Endpoint.IP`
- `Endpoint.OS`
- `XMCyber.Entity.isAsset`
- `XMCyber.Entity.affectedEntities`
- `XMCyber.Entity.averageComplexity`
- `XMCyber.Entity.criticalAssetsAtRisk`
- `XMCyber.Entity.averageComplexityLevel`
- `XMCyber.Entity.type`

**Dependencies:**

- Integrations: XMCyber
- Scripts: IsIntegrationAvailable
- Commands: xmcyber-enrich-from-ip, xmcyber-affected-entities-list, xmcyber-affected-critical-assets-list


## Prisma Cloud Compute - Compliance Alert Host Enrichment Loop

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Compliance Alert v2" playbook. It will loop through all of the given compliance issue IDs and will retrieve the following information for each affected host based on the compliance issue ID: The enriched information will be displayed in the layout in a dedicated table under the "Host Compliance Information" tab

**Inputs:**

- `ComplianceIssueID`: A compliance issue ID. This ID is used to filter relevant hostnames for enrichment.
- `TicketingSystem`: Which ticketing system should be used to create an external ticket.Available options:- Jira- ServiceNowIf neither of the above are selected, no external ticket will be created.For 
- `JiraIssueTypeName`: Issue type name. For example: "Task".
- `JiraProjectName`: The project name with which to associate the issue.

**Dependencies:**

- Sub-playbooks: Prisma Cloud Compute - Jira Compliance Issue, Prisma Cloud Compute - ServiceNow Compliance Ticket
- Scripts: DeleteContext, SetAndHandleEmpty, PrismaCloudComputeComplianceTable
- Commands: setIncident, prisma-cloud-compute-hosts-scan-list

