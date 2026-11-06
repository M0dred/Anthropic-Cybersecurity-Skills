# Vendor Variants - Enriching Cloud Assets

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Cortex ASM - Prisma Cloud Enrichment

**Product:** Cortex Attack Surface Management

Given the IP address this playbook enriches information from Prisma Cloud

**Inputs:**

- `remoteIP`: IP address of service.
- `cloudProvider`: Cloud service provider.

**Dependencies:**

- Sub-playbooks: Prisma Cloud - Find Public Cloud Resource by Public IP v2
- Scripts: GridFieldSetup

