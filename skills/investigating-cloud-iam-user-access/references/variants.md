# Vendor Variants - Investigating Cloud Iam User Access

Vendor-specific implementations, feeds, and collectors for this procedure.


## Cortex XDR - Cloud IAM User Access Investigation

**Product:** Cloud Incident Response

**Kind:** playbook

Investigate and respond to Cortex XDR Cloud alerts where a Cloud IAM user`s access key is used suspiciously to access the cloud environment. The following alerts are supported for AWS, Azure, and GCP environments

**Inputs:**

- `alert_id`: The alert ID.
- `autoAccessKeyRemediation`: Whether to execute the user remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `credentialsRemediationType`: The response playbook provides the following remediation actions using AWS, MSGraph Users, GCP and GSuite Admin:Reset: By entering "Reset" in the input, the playbook will execute p
- `AWS-accessKeyRemediationType`: Choose the remediation type for the user's access key.AWS available types:Disable - for disabling the user's access key.Delete - for deleting the user's access key.
- `AWS-userRemediationType`: Choose the remediation type for the user involved.AWS available types:Delete - for the user deletion.Revoke - for revoking the user's credentials.
- `AWS-newRoleName`: The name of the new role to create if the analyst decides to clone the service account.
- `AWS-newInstanceProfileName`: The name of the new instance profile to create if the analyst decides to clone the service account.
- `AWS-roleNameToRestrict`: If provided, the role will be attached with a deny policy without the compute instance analysis flow.

**Dependencies:**

- Sub-playbooks: Cloud Response - Generic, Account Enrichment - Generic v2.1, Cloud Credentials Rotation - Generic, Cloud IAM Enrichment - Generic
- Commands: ip, xdr-get-cloud-original-alerts, setIncident

## Cortex XDR - Cloud IAM User Access Investigation

**Product:** Cloud Incident Response

**Kind:** playbook

Investigate and respond to Cortex XDR Cloud alerts where a Cloud IAM user`s access key is used suspiciously to access the cloud environment. The following alerts are supported for AWS, Azure, and GCP environments

**Inputs:**

- `alert_id`: The alert ID.
- `autoAccessKeyRemediation`: Whether to execute the user remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `credentialsRemediationType`: The response playbook provides the following remediation actions using AWS, MSGraph Users, GCP and GSuite Admin:Reset: By entering "Reset" in the input, the playbook will execute p
- `AWS-accessKeyRemediationType`: Choose the remediation type for the user's access key.AWS available types:Disable - for disabling the user's access key.Delete - for deleting the user's access key.
- `AWS-userRemediationType`: Choose the remediation type for the user involved.AWS available types:Delete - for the user deletion.Revoke - for revoking the user's credentials.
- `AWS-newRoleName`: The name of the new role to create if the analyst decides to clone the service account.
- `AWS-newInstanceProfileName`: The name of the new instance profile to create if the analyst decides to clone the service account.
- `AWS-roleNameToRestrict`: If provided, the role will be attached with a deny policy without the compute instance analysis flow.

**Dependencies:**

- Sub-playbooks: Cloud Response - Generic, Account Enrichment - Generic v2.1, Cloud Credentials Rotation - Generic, Cloud IAM Enrichment - Generic
- Commands: ip, xdr-get-cloud-original-alerts, setIncident

## Cortex XDR - Cloud IAM User Access Investigation

**Product:** Cloud Incident Response

**Kind:** playbook

Investigate and respond to Cortex XDR Cloud alerts where a Cloud IAM user`s access key is used suspiciously to access the cloud environment. The following alerts are supported for AWS, Azure, and GCP environments

**Inputs:**

- `alert_id`: The alert ID.
- `autoAccessKeyRemediation`: Whether to execute the user remediation flow automatically.
- `autoBlockIndicators`: Whether to block the indicators automatically.
- `autoUserRemediation`: Whether to execute the user remediation flow automatically.
- `credentialsRemediationType`: The response playbook provides the following remediation actions using AWS, MSGraph Users, GCP and GSuite Admin:Reset: By entering "Reset" in the input, the playbook will execute p
- `AWS-accessKeyRemediationType`: Choose the remediation type for the user's access key.AWS available types:Disable - for disabling the user's access key.Delete - for deleting the user's access key.
- `AWS-userRemediationType`: Choose the remediation type for the user involved.AWS available types:Delete - for the user deletion.Revoke - for revoking the user's credentials.
- `AWS-newRoleName`: The name of the new role to create if the analyst decides to clone the service account.
- `AWS-newInstanceProfileName`: The name of the new instance profile to create if the analyst decides to clone the service account.
- `AWS-roleNameToRestrict`: If provided, the role will be attached with a deny policy without the compute instance analysis flow.

**Dependencies:**

- Sub-playbooks: Cloud Response - Generic, Account Enrichment - Generic v2.1, Cloud Credentials Rotation - Generic, Cloud IAM Enrichment - Generic
- Commands: ip, xdr-get-cloud-original-alerts, setIncident

