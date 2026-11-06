# Vendor Variants - Retrieving Original Email Thread

Vendor-specific implementations, feeds, and collectors for this procedure.


## Get Original Email - EWS

**Product:** Phishing

**Kind:** playbook

This playbook retrieves the original email in a thread, including headers and attachments, when the reporting user forwarded the original email not as an attachment. Note: You must have the necessary eDiscovery permissions in the EWS integration to execute a global search

**Inputs:**

- `Mailbox`: Email address of the reporting user.
- `InReplyTo`: The InReplyTo header in the forwarded email.
- `ThreadTopic`: The ThreadTopic header in the forwarded email.

**Dependencies:**

- Integrations: EWS v2
- Scripts: DeleteContext, Set
- Commands: ews-search-mailbox, ews-get-items, ews-get-attachment

## Get Original Email - Gmail

**Product:** Phishing

**Kind:** playbook

Retrieves the original email in a thread, including headers and attahcments, when the reporting user forwarded the original email not as an attachment. You must have the necessary permissions in your Gmail service to execute global search: Google Apps Domain-Wide Delegation of Authority

**Inputs:**

- `EmailID`: The email ID of the forwarded message.
- `User`: The email address of the reporting user.
- `From`: The email address of the thread originator.

**Dependencies:**

- Integrations: Gmail
- Scripts: DeleteContext, Set
- Commands: gmail-get-attachments, gmail-get-mail, gmail-search

## Get Original Email - EWS

**Product:** Phishing

**Kind:** playbook

This playbook retrieves the original email in a thread, including headers and attachments, when the reporting user forwarded the original email not as an attachment. Note: You must have the necessary eDiscovery permissions in the EWS integration to execute a global search

**Inputs:**

- `Mailbox`: Email address of the reporting user.
- `InReplyTo`: The InReplyTo header in the forwarded email.
- `ThreadTopic`: The ThreadTopic header in the forwarded email.

**Dependencies:**

- Integrations: EWS v2
- Scripts: DeleteContext, Set
- Commands: ews-search-mailbox, ews-get-items, ews-get-attachment

## Get Original Email - Gmail

**Product:** Phishing

**Kind:** playbook

Retrieves the original email in a thread, including headers and attahcments, when the reporting user forwarded the original email not as an attachment. You must have the necessary permissions in your Gmail service to execute global search: Google Apps Domain-Wide Delegation of Authority

**Inputs:**

- `EmailID`: The email ID of the forwarded message.
- `User`: The email address of the reporting user.
- `From`: The email address of the thread originator.

**Dependencies:**

- Integrations: Gmail
- Scripts: DeleteContext, Set
- Commands: gmail-get-attachments, gmail-get-mail, gmail-search

## Get Original Email - EWS

**Product:** Phishing

**Kind:** playbook

This playbook retrieves the original email in a thread, including headers and attachments, when the reporting user forwarded the original email not as an attachment. Note: You must have the necessary eDiscovery permissions in the EWS integration to execute a global search

**Inputs:**

- `Mailbox`: Email address of the reporting user.
- `InReplyTo`: The InReplyTo header in the forwarded email.
- `ThreadTopic`: The ThreadTopic header in the forwarded email.

**Dependencies:**

- Integrations: EWS v2
- Scripts: DeleteContext, Set
- Commands: ews-search-mailbox, ews-get-items, ews-get-attachment

## Get Original Email - Gmail

**Product:** Phishing

**Kind:** playbook

Retrieves the original email in a thread, including headers and attahcments, when the reporting user forwarded the original email not as an attachment. You must have the necessary permissions in your Gmail service to execute global search: Google Apps Domain-Wide Delegation of Authority

**Inputs:**

- `EmailID`: The email ID of the forwarded message.
- `User`: The email address of the reporting user.
- `From`: The email address of the thread originator.

**Dependencies:**

- Integrations: Gmail
- Scripts: DeleteContext, Set
- Commands: gmail-get-attachments, gmail-get-mail, gmail-search

