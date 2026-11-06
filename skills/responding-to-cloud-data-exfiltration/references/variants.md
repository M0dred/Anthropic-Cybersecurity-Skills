# Vendor Variants - Responding To Cloud Data Exfiltration

Vendor-specific implementations, feeds, and collectors for this procedure.


## Cortex XDR - Cloud Data Exfiltration Response

**Product:** Cloud Incident Response

**Kind:** playbook

**Inputs:**

- `alertID`: The XDR alert ID.
- `autoUserRemediation`: Whether to execute the user remediation automatically. (Default: False)
- `autoBlockIndicators`: Whether to execute the block remediation automatically. (Default: False)
- `credentialsRemediationType`: The response playbook provides the following remediation actions using AWS, MSGraph Users, GCP and GSuite Admin:Reset: By entering "Reset" in the input, the playbook will execute p
- `shouldCloneSA`: Whether to clone the compromised SA before putting a deny policy to it.Supports: AWS.True/False
- `AWS-newRoleName`: The new role name to assign in the clone service account flow.
- `AWS-newInstanceProfileName`: The new instance profile name to assign in the clone service account flow.
- `AWS-roleNameToRestrict`: If provided, the role will be attached with a deny policy without the compute instance analysis flow.

**Dependencies:**

- Sub-playbooks: Cloud Credentials Rotation - Generic, Cloud User Investigation - Generic, Cloud Threat Hunting - Persistence, Cloud Response - Generic
- Commands: ip, xdr-get-cloud-original-alerts, xdr-get-alerts, closeInvestigation

## Cortex XDR - Cloud Data Exfiltration Response

**Product:** Cloud Incident Response

**Kind:** playbook

**Inputs:**

- `alertID`: The XDR alert ID.
- `autoUserRemediation`: Whether to execute the user remediation automatically. (Default: False)
- `autoBlockIndicators`: Whether to execute the block remediation automatically. (Default: False)
- `credentialsRemediationType`: The response playbook provides the following remediation actions using AWS, MSGraph Users, GCP and GSuite Admin:Reset: By entering "Reset" in the input, the playbook will execute p
- `shouldCloneSA`: Whether to clone the compromised SA before putting a deny policy to it.Supports: AWS.True/False
- `AWS-newRoleName`: The new role name to assign in the clone service account flow.
- `AWS-newInstanceProfileName`: The new instance profile name to assign in the clone service account flow.
- `AWS-roleNameToRestrict`: If provided, the role will be attached with a deny policy without the compute instance analysis flow.

**Dependencies:**

- Sub-playbooks: Cloud Credentials Rotation - Generic, Cloud User Investigation - Generic, Cloud Threat Hunting - Persistence, Cloud Response - Generic
- Commands: ip, xdr-get-cloud-original-alerts, xdr-get-alerts, closeInvestigation

## Cortex XDR - Cloud Data Exfiltration Response

**Product:** Cloud Incident Response

**Kind:** playbook

**Inputs:**

- `alertID`: The XDR alert ID.
- `autoUserRemediation`: Whether to execute the user remediation automatically. (Default: False)
- `autoBlockIndicators`: Whether to execute the block remediation automatically. (Default: False)
- `credentialsRemediationType`: The response playbook provides the following remediation actions using AWS, MSGraph Users, GCP and GSuite Admin:Reset: By entering "Reset" in the input, the playbook will execute p
- `shouldCloneSA`: Whether to clone the compromised SA before putting a deny policy to it.Supports: AWS.True/False
- `AWS-newRoleName`: The new role name to assign in the clone service account flow.
- `AWS-newInstanceProfileName`: The new instance profile name to assign in the clone service account flow.
- `AWS-roleNameToRestrict`: If provided, the role will be attached with a deny policy without the compute instance analysis flow.

**Dependencies:**

- Sub-playbooks: Cloud Credentials Rotation - Generic, Cloud User Investigation - Generic, Cloud Threat Hunting - Persistence, Cloud Response - Generic
- Commands: ip, xdr-get-cloud-original-alerts, xdr-get-alerts, closeInvestigation

