# Vendor Variants - Remediating Dspm Violations With Rubrik

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## DSPM Valid User Response

**Product:** DSPM

The DSPM Valid User Response playbook is designed to assess and manage user responses to DSPM-identified risks. It checks the user’s selected action (e.g., creating a Jira ticket or remediating specific risk types) and initiates the appropriate remediation or notification workflows. If no user response is received, the playbook logs the incident for future action, ensuring comprehensive tracking and response handling for DSPM incidents

**Inputs:**

- `rerunTime`: Incident re-run time (in hours)

**Dependencies:**

- Sub-playbooks: DSPM Remediation playbook for Sensitive asset open to world., DSPM Jira Ticket Creation, DSPM Remediation playbook for Empty storage asset
- Scripts: SlackBlockBuilder, IsIntegrationAvailable, DSPMIncidentList, DSPMCreateSimpleSlackMessageBlock, DeleteContext
- Commands: setList, getList, addToList, createList

## DSPM Valid User Response

**Product:** DSPM

The DSPM Valid User Response playbook is designed to assess and manage user responses to DSPM-identified risks. It checks the user’s selected action (e.g., creating a Jira ticket or remediating specific risk types) and initiates the appropriate remediation or notification workflows. If no user response is received, the playbook logs the incident for future action, ensuring comprehensive tracking and response handling for DSPM incidents

**Inputs:**

- `rerunTime`: Incident re-run time (in hours)

**Dependencies:**

- Sub-playbooks: DSPM Remediation playbook for Sensitive asset open to world., DSPM Jira Ticket Creation, DSPM Remediation playbook for Empty storage asset
- Scripts: SlackBlockBuilder, IsIntegrationAvailable, DSPMIncidentList, DSPMCreateSimpleSlackMessageBlock, DeleteContext
- Commands: setList, getList, addToList, createList

## DSPM Valid User Response

**Product:** DSPM

The DSPM Valid User Response playbook is designed to assess and manage user responses to DSPM-identified risks. It checks the user’s selected action (e.g., creating a Jira ticket or remediating specific risk types) and initiates the appropriate remediation or notification workflows. If no user response is received, the playbook logs the incident for future action, ensuring comprehensive tracking and response handling for DSPM incidents

**Inputs:**

- `rerunTime`: Incident re-run time (in hours)

**Dependencies:**

- Sub-playbooks: DSPM Remediation playbook for Sensitive asset open to world., DSPM Jira Ticket Creation, DSPM Remediation playbook for Empty storage asset
- Scripts: SlackBlockBuilder, IsIntegrationAvailable, DSPMIncidentList, DSPMCreateSimpleSlackMessageBlock, DeleteContext
- Commands: setList, getList, addToList, createList

## DSPM Valid User Response

**Product:** DSPM

The DSPM Valid User Response playbook is designed to assess and manage user responses to DSPM-identified risks. It checks the user’s selected action (e.g., creating a Jira ticket or remediating specific risk types) and initiates the appropriate remediation or notification workflows. If no user response is received, the playbook logs the incident for future action, ensuring comprehensive tracking and response handling for DSPM incidents

**Inputs:**

- `rerunTime`: Incident re-run time (in hours)

**Dependencies:**

- Sub-playbooks: DSPM Remediation playbook for Sensitive asset open to world., DSPM Jira Ticket Creation, DSPM Remediation playbook for Empty storage asset
- Scripts: SlackBlockBuilder, IsIntegrationAvailable, DSPMIncidentList, DSPMCreateSimpleSlackMessageBlock, DeleteContext
- Commands: setList, getList, addToList, createList

