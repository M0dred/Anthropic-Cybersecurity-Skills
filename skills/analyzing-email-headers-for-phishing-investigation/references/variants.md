# Vendor Variants - Analyzing Email Headers For Phishing Investigation

Vendor-specific implementations, feeds, and collectors for this procedure.


## Email Headers Check - Generic

**Product:** Common Playbooks

**Kind:** playbook

This playbook executes one sub-playbook and one automation to check the email headers

**Inputs:**

- `AuthenticateEmail`: Whether the authenticity of the email should be verified using SPF, DKIM and DMARC.
- `CheckMicrosoftHeaders`: Whether to Check Microsoft headers for BCL/PCL/SCL scores and set the "Severity" and "Email Classification" accordingly.

**Dependencies:**

- Sub-playbooks: Process Microsoft's Anti-Spam Headers
- Scripts: CheckEmailAuthenticity
- Commands: setIncident

## Email Headers Check - Generic

**Product:** Common Playbooks

**Kind:** playbook

This playbook executes one sub-playbook and one automation to check the email headers

**Inputs:**

- `AuthenticateEmail`: Whether the authenticity of the email should be verified using SPF, DKIM and DMARC.
- `CheckMicrosoftHeaders`: Whether to Check Microsoft headers for BCL/PCL/SCL scores and set the "Severity" and "Email Classification" accordingly.

**Dependencies:**

- Sub-playbooks: Process Microsoft's Anti-Spam Headers
- Scripts: CheckEmailAuthenticity
- Commands: setIncident

## Email Headers Check - Generic

**Product:** Common Playbooks

**Kind:** playbook

This playbook executes one sub-playbook and one automation to check the email headers

**Inputs:**

- `AuthenticateEmail`: Whether the authenticity of the email should be verified using SPF, DKIM and DMARC.
- `CheckMicrosoftHeaders`: Whether to Check Microsoft headers for BCL/PCL/SCL scores and set the "Severity" and "Email Classification" accordingly.

**Dependencies:**

- Sub-playbooks: Process Microsoft's Anti-Spam Headers
- Scripts: CheckEmailAuthenticity
- Commands: setIncident

