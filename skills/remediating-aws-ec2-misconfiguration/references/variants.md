# Vendor Variants - Remediating Aws Ec2 Misconfiguration

Vendor-specific implementations, feeds, and collectors for this procedure.


## AWS - Security Group Remediation

**Product:** AWS Enrichment and Remediation

**Kind:** playbook

Replace current security groups with limited access security groups

**Inputs:**

- `VpcID`: This is the VPC ID used for Security group creation.
- `NicID`: This is the Network interface of Ec2 instance.
- `RemediationRule`: The security group that will used for remediating internet exposures.

**Dependencies:**

- Integrations: AWS - EC2
- Scripts: Set
- Commands: aws-ec2-describe-security-groups, aws-ec2-authorize-security-group-ingress-rule, aws-ec2-modify-network-interface-attribute, aws-ec2-create-security-group

## Prisma Cloud Remediation - AWS EC2 Instance Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

**Kind:** playbook

Remediates Prisma Cloud AWS EC2 alerts. It calls the following sub-playbooks to perform the remediation

**Inputs:**

- `AutoUpdateEC2`: Whether to update the AWS EC2 instance automatically.
- `policyId`: Returns the Prisma Cloud policy ID.

**Dependencies:**

- Sub-playbooks: Prisma Cloud Remediation - AWS EC2 Security Group Misconfiguration, Prisma Cloud Remediation - AWS Security Groups Allows Internet Traffic To TCP Port
- Integrations: Builtin, PrismaCloud v2
- Commands: closeInvestigation, redlock-dismiss-alerts

## AWS - Security Group Remediation

**Product:** AWS Enrichment and Remediation

**Kind:** playbook

Replace current security groups with limited access security groups

**Inputs:**

- `VpcID`: This is the VPC ID used for Security group creation.
- `NicID`: This is the Network interface of Ec2 instance.
- `RemediationRule`: The security group that will used for remediating internet exposures.

**Dependencies:**

- Integrations: AWS - EC2
- Scripts: Set
- Commands: aws-ec2-describe-security-groups, aws-ec2-authorize-security-group-ingress-rule, aws-ec2-modify-network-interface-attribute, aws-ec2-create-security-group

## Prisma Cloud Remediation - AWS EC2 Instance Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

**Kind:** playbook

Remediates Prisma Cloud AWS EC2 alerts. It calls the following sub-playbooks to perform the remediation

**Inputs:**

- `AutoUpdateEC2`: Whether to update the AWS EC2 instance automatically.
- `policyId`: Returns the Prisma Cloud policy ID.

**Dependencies:**

- Sub-playbooks: Prisma Cloud Remediation - AWS EC2 Security Group Misconfiguration, Prisma Cloud Remediation - AWS Security Groups Allows Internet Traffic To TCP Port
- Integrations: Builtin, PrismaCloud v2
- Commands: closeInvestigation, redlock-dismiss-alerts

## AWS - Security Group Remediation

**Product:** AWS Enrichment and Remediation

**Kind:** playbook

Replace current security groups with limited access security groups

**Inputs:**

- `VpcID`: This is the VPC ID used for Security group creation.
- `NicID`: This is the Network interface of Ec2 instance.
- `RemediationRule`: The security group that will used for remediating internet exposures.

**Dependencies:**

- Integrations: AWS - EC2
- Scripts: Set
- Commands: aws-ec2-describe-security-groups, aws-ec2-authorize-security-group-ingress-rule, aws-ec2-modify-network-interface-attribute, aws-ec2-create-security-group

## Prisma Cloud Remediation - AWS EC2 Instance Misconfiguration

**Product:** Prisma Cloud by Palo Alto Networks

**Kind:** playbook

Remediates Prisma Cloud AWS EC2 alerts. It calls the following sub-playbooks to perform the remediation

**Inputs:**

- `AutoUpdateEC2`: Whether to update the AWS EC2 instance automatically.
- `policyId`: Returns the Prisma Cloud policy ID.

**Dependencies:**

- Sub-playbooks: Prisma Cloud Remediation - AWS EC2 Security Group Misconfiguration, Prisma Cloud Remediation - AWS Security Groups Allows Internet Traffic To TCP Port
- Integrations: Builtin, PrismaCloud v2
- Commands: closeInvestigation, redlock-dismiss-alerts

