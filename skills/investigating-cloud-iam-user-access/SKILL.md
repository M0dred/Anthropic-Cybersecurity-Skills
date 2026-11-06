---
name: investigating-cloud-iam-user-access
description: >-
  Investigate and respond to alerts where a Cloud IAM user access key is used suspiciously to access the cloud environment. The following alerts are supported for AWS, Azure, and GCP environments. Penetration testing tool attempt Penetration testing tool. Focuses on access-key creation and privilege changes. Use when an alert names cloud IAM user access and the scope is unknown, or when a timeline is needed for cloud IAM user access. Keywords: investigating, cloud, iam, user, access, investigation, triage, identity access management. Do not use for investigating cloud user activity - use `investigating-cloud-user-activity`.
domain: cybersecurity
subdomain: identity-access-management
tags:
- identity-access-management
- iam
- containment
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- PR.AC-01
- PR.AC-04
- RS.MI-01
mitre_attack:
- T1078
- T1098
- T1556
---

# Investigating Cloud IAM User Access

## When to Use

- An alert names cloud IAM user access and the scope is not yet known.
- An incident needs a timeline and a verdict before containment.
- A review challenges whether the original conclusion was supported.

**Do not use** for investigating cloud user activity - use `investigating-cloud-user-activity`.

## Prerequisites

- Read access to the relevant telemetry and asset inventory.
- The entity identifiers: user, host, IP, or application.
- A case or ticket to attach evidence to.

## Workflow

### Step 1: Scope the entity

Resolve the identifier to all of its identities and assets.

### Step 2: Collect evidence

Pull authentication, process, network, and cloud audit events for the window.

### Step 3: Build the timeline

Order events, resolve time zones, and mark the first and last malicious action.

### Step 4: Test hypotheses

Distinguish the observed facts from the inference, and check alternative explanations.

### Step 5: Conclude

State the verdict, the confidence, and the recommended containment.

## Platform Commands

The commands below are the platform-native equivalents for this procedure.

```bash
# AWS: inspect and fix the resource
aws cloudtrail describe-trails --query 'trailList[].{Name:Name,S3:S3BucketName,Multi:IsMultiRegionTrail}'
aws cloudtrail update-trail --name management-trail --is-multi-region-trail --enable-log-file-validation
aws ec2 describe-security-groups --group-ids sg-0123456789abcdef0
aws iam get-policy-version --policy-arn arn:aws:iam::123456789012:policy/Example --version-id v3
```

```bash
# Azure: inspect and fix the resource
az storage account show -g rg-prod -n mystorage --query '{https:enableHttpsTrafficOnly,minTls:minimumTlsVersion,public:allowBlobPublicAccess}'
az storage account update -g rg-prod -n mystorage --https-only true --min-tls-version TLS1_2 --allow-blob-public-access false
az aks show -g rg-prod -n aks-prod --query '{rbac:enableRbac,net:networkProfile}'
```

```bash
# GCP: inspect and fix the resource
gcloud compute firewall-rules list --format='table(name,sourceRanges,allowed)'
gcloud compute firewall-rules update deny-all-ingress --source-ranges 10.0.0.0/8
gcloud container clusters describe prod --zone us-central1-a --format='value(masterAuthorizedNetworksConfig)'
```

## Verification

- Every timeline entry has a source and a timestamp.
- The verdict distinguishes facts from inference.
- Alternative explanations are addressed.
- The evidence is attached to the case.

## Common Pitfalls

- Confirmation bias toward the first alert.
- Mixing time zones in the timeline.
- Treating a single log line as proof.
- Closing without checking lateral movement.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
