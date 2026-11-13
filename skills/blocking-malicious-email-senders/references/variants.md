# Vendor Variants - Blocking Malicious Email Senders

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Mimecast - Block Sender Domain

**Product:** Mimecast

A playbook to block sender domain name using Mimecast integration

**Inputs:**

- `BlockGroup`: The sender email block group.
- `SenderDomain`: The sender domain to block.
- `QuerySource`: The query source, please input cloud or ldap in the value input.

**Dependencies:**

- Integrations: MimecastV2
- Scripts: IsIntegrationAvailable
- Commands: mimecast-find-groups, mimecast-add-group-member


## Mimecast - Block Sender Email

**Product:** Mimecast

A playbook to block sender email address using Mimecast integration

**Inputs:**

- `BlockGroup`: The sender email block group.
- `SenderEmail`: The sender email to block.
- `QuerySource`: The query source, please input cloud or ldap in the value input.

**Dependencies:**

- Integrations: MimecastV2
- Scripts: IsIntegrationAvailable
- Commands: mimecast-find-groups, mimecast-add-group-member


## Symantec block Email

**Product:** Symantec Messaging Gateway

This playbook will block email address at your email gateway

**Inputs:**

- `EmailToBlock`: The email address that will be blocked.

