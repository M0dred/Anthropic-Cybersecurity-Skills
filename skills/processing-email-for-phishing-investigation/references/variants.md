# Vendor Variants - Processing Email For Phishing Investigation

Vendor-specific implementations, feeds, and collectors for this procedure.


## Process Email - Core v2

**Product:** Phishing

**Kind:** playbook

This playbook adds email details to the relevant context entities and handles the case where original emails are attached

**Inputs:**

- `File`: An EML or MSG file.
- `Email`: The receiving email address.
- `EmailCC`: CC addresses
- `EmailFrom`: The originator of the email.
- `EmailSubject`: The email subject.
- `EmailText`: The email text.
- `EmailHtml`: The HTML version of the email.
- `EmailHeaders`: The email headers.
- `EmailFormat`: The email format.

**Dependencies:**

- Scripts: IdentifyAttachedEmail, Set, SetAndHandleEmpty, SetGridField, ParseEmailFiles
- Commands: setIncident

## Process Email - Core

**Product:** Phishing

**Kind:** playbook

Adds email details to the relevant context entities and handle the case where original emails are attached

**Inputs:**

- `File`: The EML or MSG file.
- `Email`: The receiving email address
- `Email/cc`: THe CC addresses.
- `Email/from`: The originator of the email.
- `Email/subject`: The email’s subject.
- `Email/text`: The email text.
- `Email/html`: The HTML version of the email.
- `Email/headers`: The email’s headers.
- `Email/format`: The email’s format.

**Dependencies:**

- Integrations: Builtin
- Scripts: ParseEmailFiles, Set, IdentifyAttachedEmail
- Commands: setIncident

## Process Email - Generic

**Product:** Phishing

**Kind:** playbook

This playbook adds email details to the relevant context entities and handles original email attachments

**Inputs:**

- `File`: An EML or MSG file.
- `Email`: The receiving email address.
- `Email/cc`: The CC addresses.
- `Email/from`: The originator of the email.
- `Email/subject`: The email subject.
- `Email/text`: The email text.
- `Email/html`: The email HTML.
- `Email/headers`: The email headers.
- `Email/format`: The email format.
- `GetOriginalEmail`: Retrieves the original email in the thread. You must have the necessary permissions in your email service to execute global search.- EWS: eDiscovery- Gmail: Google Apps Domain-Wide

**Dependencies:**

- Scripts: SetAndHandleEmpty, ParseEmailFiles, Set, IdentifyAttachedEmail, SetGridField
- Commands: rasterize-email, setIncident

## Process Email - Core v2

**Product:** Phishing

**Kind:** playbook

This playbook adds email details to the relevant context entities and handles the case where original emails are attached

**Inputs:**

- `File`: An EML or MSG file.
- `Email`: The receiving email address.
- `EmailCC`: CC addresses
- `EmailFrom`: The originator of the email.
- `EmailSubject`: The email subject.
- `EmailText`: The email text.
- `EmailHtml`: The HTML version of the email.
- `EmailHeaders`: The email headers.
- `EmailFormat`: The email format.

**Dependencies:**

- Scripts: IdentifyAttachedEmail, Set, SetAndHandleEmpty, SetGridField, ParseEmailFiles
- Commands: setIncident

## Process Email - Core

**Product:** Phishing

**Kind:** playbook

Adds email details to the relevant context entities and handle the case where original emails are attached

**Inputs:**

- `File`: The EML or MSG file.
- `Email`: The receiving email address
- `Email/cc`: THe CC addresses.
- `Email/from`: The originator of the email.
- `Email/subject`: The email’s subject.
- `Email/text`: The email text.
- `Email/html`: The HTML version of the email.
- `Email/headers`: The email’s headers.
- `Email/format`: The email’s format.

**Dependencies:**

- Integrations: Builtin
- Scripts: ParseEmailFiles, Set, IdentifyAttachedEmail
- Commands: setIncident

## Process Email - Generic

**Product:** Phishing

**Kind:** playbook

This playbook adds email details to the relevant context entities and handles original email attachments

**Inputs:**

- `File`: An EML or MSG file.
- `Email`: The receiving email address.
- `Email/cc`: The CC addresses.
- `Email/from`: The originator of the email.
- `Email/subject`: The email subject.
- `Email/text`: The email text.
- `Email/html`: The email HTML.
- `Email/headers`: The email headers.
- `Email/format`: The email format.
- `GetOriginalEmail`: Retrieves the original email in the thread. You must have the necessary permissions in your email service to execute global search.- EWS: eDiscovery- Gmail: Google Apps Domain-Wide

**Dependencies:**

- Scripts: SetAndHandleEmpty, ParseEmailFiles, Set, IdentifyAttachedEmail, SetGridField
- Commands: rasterize-email, setIncident

## Process Email - Core v2

**Product:** Phishing

**Kind:** playbook

This playbook adds email details to the relevant context entities and handles the case where original emails are attached

**Inputs:**

- `File`: An EML or MSG file.
- `Email`: The receiving email address.
- `EmailCC`: CC addresses
- `EmailFrom`: The originator of the email.
- `EmailSubject`: The email subject.
- `EmailText`: The email text.
- `EmailHtml`: The HTML version of the email.
- `EmailHeaders`: The email headers.
- `EmailFormat`: The email format.

**Dependencies:**

- Scripts: IdentifyAttachedEmail, Set, SetAndHandleEmpty, SetGridField, ParseEmailFiles
- Commands: setIncident

## Process Email - Core

**Product:** Phishing

**Kind:** playbook

Adds email details to the relevant context entities and handle the case where original emails are attached

**Inputs:**

- `File`: The EML or MSG file.
- `Email`: The receiving email address
- `Email/cc`: THe CC addresses.
- `Email/from`: The originator of the email.
- `Email/subject`: The email’s subject.
- `Email/text`: The email text.
- `Email/html`: The HTML version of the email.
- `Email/headers`: The email’s headers.
- `Email/format`: The email’s format.

**Dependencies:**

- Integrations: Builtin
- Scripts: ParseEmailFiles, Set, IdentifyAttachedEmail
- Commands: setIncident

## Process Email - Generic

**Product:** Phishing

**Kind:** playbook

This playbook adds email details to the relevant context entities and handles original email attachments

**Inputs:**

- `File`: An EML or MSG file.
- `Email`: The receiving email address.
- `Email/cc`: The CC addresses.
- `Email/from`: The originator of the email.
- `Email/subject`: The email subject.
- `Email/text`: The email text.
- `Email/html`: The email HTML.
- `Email/headers`: The email headers.
- `Email/format`: The email format.
- `GetOriginalEmail`: Retrieves the original email in the thread. You must have the necessary permissions in your email service to execute global search.- EWS: eDiscovery- Gmail: Google Apps Domain-Wide

**Dependencies:**

- Scripts: SetAndHandleEmpty, ParseEmailFiles, Set, IdentifyAttachedEmail, SetGridField
- Commands: rasterize-email, setIncident

