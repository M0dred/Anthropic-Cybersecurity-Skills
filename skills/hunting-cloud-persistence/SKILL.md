---
name: hunting-cloud-persistence
description: >-
  Covers IAM, compute, and serverless persistence. Use when activity related to cloud persistence mechanisms is suspected elsewhere in the estate, or when a hunt needs queries for cloud persistence mechanisms. Keywords: hunting, cloud, persistence, detection, cloud security. Do not use for rotating cloud credentials - use `rotating-cloud-credentials`.
domain: cybersecurity
subdomain: cloud-security
tags:
- cloud-security
- aws
- azure
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- PR.AC-05
- DE.CM-01
- RS.MI-01
mitre_attack:
- T1078.004
- T1530
- T1562.008
---

# Hunting Cloud Persistence

## When to Use

- A threat report or incident suggests cloud persistence mechanisms may be present elsewhere.
- A detection needs validation against historical telemetry.
- A proactive hunt is scheduled for the environment.

**Do not use** for rotating cloud credentials - use `rotating-cloud-credentials`.

## Prerequisites

- Query access to the relevant telemetry: SIEM, EDR, cloud audit logs, or network.
- The data retention window and the field map for each source.
- A hypothesis with a falsifiable test.

## Workflow

### Step 1: State the hypothesis

Write what you expect to see if the activity is present, and what would prove it absent.

### Step 2: Translate to queries

Write one query per telemetry source, with the fields and time window explicit.

### Step 3: Run and triage

Execute, de-duplicate, and rank hits by confidence and asset criticality.

### Step 4: Pivot

For each confirmed hit, pivot on the entity, the technique, and the infrastructure.

### Step 5: Document

Record the queries, the hit counts, the false positives, and the coverage gaps.

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

- The queries are saved and rerunnable.
- Hit counts reconcile with a manual spot check.
- False positives are explained, not silently dropped.
- Coverage gaps are stated explicitly.

## Common Pitfalls

- Hunting without a hypothesis.
- Querying only one telemetry source.
- Ignoring retention limits.
- Reporting hits without triage.

## References

- `references/api-reference.md` - platform commands and script usage
- `references/standards.md` - NIST CSF, NIST 800-53, MITRE ATT&CK mappings
- `references/workflows.md` - decision tree and incident record template
- `scripts/agent.py` - runnable helper for this procedure
