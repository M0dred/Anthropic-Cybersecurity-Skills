# Vendor Variants - Remediating Prisma Cloud Compliance Alerts

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## CimTrak - Example - Scan Compliance By IP

**Product:** CimTrak - System Integrity Assurance

**Inputs:**

- `IP`: 

**Dependencies:**

- Integrations: CimTrak
- Commands: get-agent-object-by-ip, compliance-scan-with-summary, get-objects


## McAfee ePO Endpoint Compliance Playbook v2

**Product:** McAfee ePO

Discover endpoints that are not using the latest McAfee AV Signatures

**Dependencies:**

- Integrations: epo
- Scripts: commentsToContext, ServiceNowCreateIncident
- Commands: setIncident, epo-get-latest-dat, closeInvestigation, epo-get-current-dat, epo-update-client-dat


## McAfee ePO Repository Compliance Playbook v2

**Product:** McAfee ePO

Ensures that ePO servers are updated to the latest McAfee published AV signatures (DAT file version)

**Dependencies:**

- Integrations: epo
- Scripts: Sleep, AreValuesEqual
- Commands: closeInvestigation, send-mail, epo-update-repository, epo-get-current-dat, setIncident, epo-get-latest-dat


## Prisma Cloud Compute - Audit Alert Compliance Enrichment

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Audit Alert v2" playbook. Retrieves the following information

**Inputs:**

- `Project`: The project to get the alert profiles for.
- `ComplianceIssues`: Compliance issues for creating the compliance table in the layout.

**Outputs:**

- `ComplianceTable`

**Dependencies:**

- Commands: prisma-cloud-compute-get-waas-policies, prisma-cloud-compute-get-alert-profiles


## Prisma Cloud Compute - Compliance Alert Container Enrichment Loop

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Compliance Alert v2" playbook. It will loop through all of the given compliance issue IDs and will retrieve the following information for each affected container based on the compliance issue ID: The enriched information will be displayed in the layout in a dedicated table under the "Container Compliance Information" tab

**Inputs:**

- `ComplianceIssueID`: A compliance issue ID. This ID is used to filter relevant containers for enrichment.
- `TicketingSystem`: Which ticketing system should be used to create an external ticket.Available options:- Jira- ServiceNowIf neither of the above are selected, no external ticket will be created.For 
- `JiraIssueTypeName`: Issue type name. For example: "Task".
- `JiraProjectName`: The project name with which to associate the issue.

**Dependencies:**

- Sub-playbooks: Prisma Cloud Compute - Jira Compliance Issue, Prisma Cloud Compute - ServiceNow Compliance Ticket
- Scripts: SetAndHandleEmpty, DeleteContext, PrismaCloudComputeComplianceTable
- Commands: setIncident, prisma-cloud-compute-container-scan-results-list


## Prisma Cloud Compute - Compliance Alert Image Enrichment Loop

**Product:** Prisma Cloud Compute by Palo Alto Networks

This is a sub-playbook of the "Prisma Cloud Compute - Compliance Alert v2" playbook. It will loop through all of the given compliance issue IDs and will retrieve the following information for each affected image based on the compliance issue ID: The enriched information will be displayed in the layout in a dedicated table under the "Image Compliance Information" tab

**Inputs:**

- `ComplianceIssueID`: A compliance issue ID. This ID is used to filter relevant images for enrichment.
- `TicketingSystem`: Which ticketing system should be used to create an external ticket.Available options:- Jira- ServiceNowIf neither of the above are selected, no external ticket will be created.For 
- `JiraIssueTypeName`: Issue type name. For example: "Task".
- `JiraProjectName`: The project name with which to associate the issue.

**Dependencies:**

- Sub-playbooks: Prisma Cloud Compute - Jira Compliance Issue, Prisma Cloud Compute - ServiceNow Compliance Ticket
- Scripts: DeleteContext, PrismaCloudComputeComplianceTable, SetAndHandleEmpty
- Commands: setIncident, prisma-cloud-compute-images-scan-list


## Prisma Cloud Compute - Jira Compliance Issue

**Product:** Prisma Cloud Compute by Palo Alto Networks

This playbook is a sub-playbook of the "Prisma Cloud Compute - Compliance Alert Host Enrichment Loop" playbook. It creates a new Jira issue or updates an existing Jira issue for each compliance ID retrieved in the original Prisma Cloud compliance alert, with enriched data for each resource (host, image or container)

**Inputs:**

- `ComplianceIssueID`: The compliance issue ID to open a Jira issue for.
- `ComplianceIssueDescription`: The compliance issue description.
- `ComplianceIssueSeverity`: The compliance issue severity.
- `AttachFileByDefault`: Whether to create the Jira issue with an XLSX file by default.Available options:False - The playbook will create the issue with a markdown table containing the compliance issues. I
- `JiraProjectName`: Issue type name. For example: "Task".
- `JiraIssueTypeName`: The project name with which to associate the issue.

**Dependencies:**

- Sub-playbooks: Prisma Cloud Compute - Jira Ticket (XLSX), Prisma Cloud Compute - Jira Ticket (Markdown Table)
- Scripts: DeleteContext, IsIntegrationAvailable, SetAndHandleEmpty, SetGridField


## Veeam - Start Security and Compliance Analyzer

**Product:** Veeam App

Starts a Security & Compliance Analyzer scan session for the Veeam Backup & Replication instance

**Inputs:**

- `Instance`: 

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: VBR REST API
- Scripts: DeleteContext
- Commands: veeam-vbr-get-security-analyzer-best-practices, veeam-vbr-get-security-analyzer-last-run, veeam-vbr-start-security-analyzer

