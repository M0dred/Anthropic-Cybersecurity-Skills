# XSOAR → Agent Skills：T1 直接立项清单（156 个）

来源：https://xsoar.pan.dev/docs/reference/index ｜ 全量 4,252 条逐条判定 ｜ 2026-08-31

判定口径：能独立成一篇技能（明确输入/步骤/验证），且与现有 818 技能不重复。


## endpoint-security（30）

| # | XSOAR 条目 | 类型 | 建议技能名 | 来源 Pack |
|---|---|---|---|---|
| 1 | AnalyzeOSX | script | `analyzing-macos-artifacts-with-osxcollector` | OSX Collector |
| 2 | CrowdStrike Falcon - Block File | playbook | `blocking-files-with-crowdstrike` | CrowdStrike Falcon |
| 3 | MDE - Block File | playbook | `blocking-files-with-microsoft-defender` | Microsoft Defender for Endpoint |
| 4 | Search and Compare Process Executions - Generic | playbook | `comparing-process-executions` | Common Playbooks |
| 5 | CertificateReputation | script | `enriching-certificate-reputation` | Common Scripts |
| 6 | CertificateExtract | script | `extracting-fields-from-x509-certificates` | Common Scripts |
| 7 | CrowdStrike Falcon - Search Endpoints By Hash | playbook | `hunting-endpoints-with-crowdstrike` | CrowdStrike Falcon |
| 8 | MDE - Host Advanced Hunting | playbook | `hunting-endpoints-with-microsoft-defender` | Microsoft Defender for Endpoint |
| 9 | FireEye HX - Indicators Hunting | playbook | `hunting-indicators-with-fireeye-hx` | FireEye HX |
| 10 | Rapid7 InsightIDR - Indicators Hunting | playbook | `hunting-indicators-with-rapid7-insightidr` | Rapid7 InsightIDR |
| 11 | T1059 - Command and Scripting Interpreter | playbook | `investigating-command-interpreter-alerts` | Core |
| 12 | Local Analysis alert Investigation | playbook | `investigating-local-analysis-alerts` | Core |
| 13 | Cortex XDR Malware - Investigation And Response | playbook | `investigating-malware-with-cortex-xdr` | Cortex XDR by Palo Alto Networks |
| 14 | CrowdStrike Falcon Malware - Investigation and Response | playbook | `investigating-malware-with-crowdstrike` | CrowdStrike Falcon |
| 15 | MDE Malware - Investigation and Response | playbook | `investigating-malware-with-microsoft-defender` | Microsoft Defender for Endpoint |
| 16 | T1036 - Masquerading | playbook | `investigating-masquerading-alerts` | Core |
| 17 | Remote PsExec with LOLBIN command execution alert | playbook | `investigating-psexec-lolbin-execution` | Core |
| 18 | Isolate Endpoint - Generic V2 | playbook | `isolating-compromised-endpoints` | Common Playbooks |
| 19 | Cortex XDR - Isolate Endpoint | playbook | `isolating-endpoints-with-cortex-xdr` | Cortex XDR by Palo Alto Networks |
| 20 | Crowdstrike Falcon - Isolate Endpoint | playbook | `isolating-endpoints-with-crowdstrike` | CrowdStrike Falcon |
| 21 | Isolate Endpoint - Cybereason | playbook | `isolating-endpoints-with-cybereason` | Cybereason |
| 22 | FireEye HX - Isolate Endpoint | playbook | `isolating-endpoints-with-fireeye-hx` | FireEye HX |
| 23 | Microsoft Defender For Endpoint - Isolate Endpoint | playbook | `isolating-endpoints-with-microsoft-defender` | Microsoft Defender for Endpoint |
| 24 | Get File Sample By Hash - Generic v3 | playbook | `retrieving-file-samples-by-hash` | Common Playbooks |
| 25 | Get File Sample From Path - Generic V3 | playbook | `retrieving-file-samples-by-path` | Common Playbooks |
| 26 | Get File Sample - Generic | playbook | `retrieving-file-samples-from-endpoints` | Common Playbooks |
| 27 | Search And Block Software - Generic | playbook | `searching-and-blocking-software` | Common Playbooks |
| 28 | Search Endpoints By Hash - Generic V2 | playbook | `searching-endpoints-by-hash` | Common Playbooks |
| 29 | Unisolate Endpoint - Generic | playbook | `unisolating-endpoints` | Common Playbooks |
| 30 | CrowdStrike Falcon Malware - Verify Containment Actions | playbook | `verifying-containment-actions-with-crowdstrike` | CrowdStrike Falcon |

## incident-response（21）

| # | XSOAR 条目 | 类型 | 建议技能名 | 来源 Pack |
|---|---|---|---|---|
| 1 | Block Domain - Generic v2 | playbook | `blocking-malicious-domains` | Common Playbooks |
| 2 | Block File - Generic v2 | playbook | `blocking-malicious-files` | Common Playbooks |
| 3 | Block Indicators - Generic v3 | playbook | `blocking-malicious-indicators` | Common Playbooks |
| 4 | Block URL - Generic v2 | playbook | `blocking-malicious-urls` | Common Playbooks |
| 5 | Calculate Severity - Generic v2 | playbook | `calculating-incident-severity` | Common Playbooks |
| 6 | Calculate Severity - Critical Assets v2 | playbook | `calculating-severity-from-critical-assets` | Common Playbooks |
| 7 | Calculate Severity - Indicators DBotScore | playbook | `calculating-severity-from-indicator-scores` | Common Playbooks |
| 8 | Containment Plan - Isolate Device | playbook | `containing-incident-by-isolating-devices` | Common Playbooks |
| 9 | Containment Plan - Quarantine File | playbook | `containing-incident-by-quarantining-files` | Common Playbooks |
| 10 | Detonate and Analyze File - Generic | playbook | `detonating-and-analyzing-files` | Common Playbooks |
| 11 | Detonate File - Generic | playbook | `detonating-files-in-sandbox` | Common Playbooks |
| 12 | Detonate URL - Generic v1.5 | playbook | `detonating-urls-in-sandbox` | Common Playbooks |
| 13 | Eradication Plan - Delete File | playbook | `eradicating-threats-by-deleting-files` | Common Playbooks |
| 14 | Eradication Plan - Reset Password | playbook | `eradicating-threats-by-resetting-passwords` | Common Playbooks |
| 15 | Eradication Plan - Terminate Process | playbook | `eradicating-threats-by-terminating-processes` | Common Playbooks |
| 16 | Containment Plan | playbook | `executing-incident-containment-plan` | Common Playbooks |
| 17 | Eradication Plan | playbook | `executing-incident-eradication-plan` | Common Playbooks |
| 18 | Recovery Plan | playbook | `executing-incident-recovery-plan` | Common Playbooks |
| 19 | SANS - Incident Handlers Checklist | playbook | `following-sans-incident-handler-checklist` | SANS |
| 20 | Handle False Positive Alerts | playbook | `handling-false-positive-alerts` | Common Playbooks |
| 21 | NIST - Handling an Incident Template | playbook | `handling-incidents-per-nist-800-61` | NIST |

## phishing-defense（20）

| # | XSOAR 条目 | 类型 | 建议技能名 | 来源 Pack |
|---|---|---|---|---|
| 1 | Process Microsoft's Anti-Spam Headers | playbook | `analyzing-anti-spam-headers` | Phishing |
| 2 | Phishing - Machine Learning Analysis | playbook | `analyzing-phishing-with-machine-learning` | Phishing |
| 3 | Block Email - Generic v2 | playbook | `blocking-malicious-email-senders` | Common Playbooks |
| 4 | Calculate Severity By Email Authenticity | playbook | `calculating-severity-from-email-authenticity` | Phishing |
| 5 | EmailDomainBlacklist | script | `checking-email-domains-against-blocklists` | Filters And Transformers |
| 6 | CollectCampaignRecipients | script | `collecting-phishing-campaign-recipients` | Phishing Campaign |
| 7 | CheckSenderDomainDistance | script | `detecting-lookalike-sender-domains` | Common Scripts |
| 8 | Email Address Enrichment - Generic v2.1 | playbook | `enriching-email-addresses` | Common Playbooks |
| 9 | ExtractDomainFromUrlAndEmail | script | `extracting-domains-from-urls-and-emails` | Common Scripts |
| 10 | NOBELIUM - wide scale APT29 spear-phishing | playbook | `hunting-nobelium-spearphishing` | Rapid Breach Response |
| 11 | Phishing - Indicators Hunting | playbook | `hunting-phishing-indicators` | Phishing |
| 12 | IdentifyAttachedEmail | script | `identifying-attached-email-messages` | Common Scripts |
| 13 | FindEmailCampaign | script | `identifying-email-campaigns-by-similarity` | Phishing Campaign |
| 14 | ParseEmailFilesV2 | script | `parsing-email-messages-for-investigation` | Common Scripts |
| 15 | PreprocessEmail | script | `preprocessing-email-for-phishing-triage` | Email Communication |
| 16 | Process Email - Generic v2 | playbook | `processing-email-for-phishing-investigation` | Phishing |
| 17 | Get Original Email - Generic v2 | playbook | `retrieving-original-email-thread` | Phishing |
| 18 | Get Email From Email Gateway - Generic | playbook | `retrieving-original-emails-from-gateway` | Common Playbooks |
| 19 | CheckEmailAuthenticity | script | `validating-email-authentication-results` | Phishing |
| 20 | CheckSender | script | `verifying-email-sender-identity` | Pipl |

## threat-intelligence（18）

| # | XSOAR 条目 | 类型 | 建议技能名 | 来源 Pack |
|---|---|---|---|---|
| 1 | Command-Line Analysis | playbook | `analyzing-command-lines` | Common Playbooks |
| 2 | OnionURLReputation | script | `assessing-tor-onion-url-reputation` | Common Scripts |
| 3 | CalculateEntropy | script | `calculating-payload-entropy` | Common Scripts |
| 4 | Get prevalence for IOCs | playbook | `checking-ioc-prevalence` | Common Playbooks |
| 5 | Convert file hash to corresponding hashes | playbook | `converting-file-hashes` | Common Playbooks |
| 6 | Cortex ASM - Enrichment | playbook | `enriching-attack-surface-assets` | Cortex Attack Surface Management |
| 7 | Domain Enrichment - Generic v2 | playbook | `enriching-domains-with-threat-intelligence` | Common Playbooks |
| 8 | Endpoint Enrichment - Generic v2.1 | playbook | `enriching-endpoints-during-investigation` | Common Playbooks |
| 9 | IP Enrichment - External - Generic v2 | playbook | `enriching-external-ip-addresses` | Common Playbooks |
| 10 | Entity Enrichment - Generic v3 | playbook | `enriching-incident-entities` | Common Playbooks |
| 11 | IP Enrichment - Internal - Generic v2 | playbook | `enriching-internal-ip-addresses` | Common Playbooks |
| 12 | URL Enrichment - Generic v2 | playbook | `enriching-urls-with-threat-intelligence` | Common Playbooks |
| 13 | Extract Indicators From File - Generic v2 | playbook | `extracting-indicators-from-files` | Common Playbooks |
| 14 | ExtractIndicatorsFromTextFile | script | `extracting-indicators-from-text-files` | Common Scripts |
| 15 | ExtractIndicatorsFromWordFile | script | `extracting-indicators-from-word-documents` | Common Scripts |
| 16 | CEFParser | script | `parsing-cef-logs` | Common Scripts |
| 17 | StixParser | script | `parsing-stix-threat-intelligence` | Base |
| 18 | Search For Hash In Sandbox - Generic | playbook | `searching-sandbox-for-hash` | Common Playbooks |

## cloud-security（15）

| # | XSOAR 条目 | 类型 | 建议技能名 | 来源 Pack |
|---|---|---|---|---|
| 1 | Cloud Enrichment - Generic | playbook | `enriching-cloud-assets` | Common Playbooks |
| 2 | Cloud Compute Enrichment - Generic | playbook | `enriching-cloud-compute-resources` | Common Playbooks |
| 3 | Cloud Response - Generic | playbook | `executing-cloud-response-actions` | Common Playbooks |
| 4 | ExtractIndicators-CloudLogging | script | `extracting-indicators-from-cloud-logs` | Cloud Incident Response |
| 5 | Cloud Threat Hunting - Persistence | playbook | `hunting-cloud-persistence` | Cloud Incident Response |
| 6 | XCloud Cryptojacking | playbook | `investigating-cloud-cryptojacking` | Cloud Incident Response |
| 7 | Cloud User Investigation - Generic | playbook | `investigating-cloud-user-activity` | Common Playbooks |
| 8 | Prisma Cloud Remediation - AWS CloudTrail Misconfiguration v2 | playbook | `remediating-aws-cloudtrail-misconfiguration` | Prisma Cloud by Palo Alto Networks |
| 9 | Prisma Cloud Remediation - AWS EC2 Instance Misconfiguration v2 | playbook | `remediating-aws-ec2-misconfiguration` | Prisma Cloud by Palo Alto Networks |
| 10 | Prisma Cloud Remediation - AWS IAM Policy Misconfiguration v2 | playbook | `remediating-aws-iam-policy-misconfiguration` | Prisma Cloud by Palo Alto Networks |
| 11 | Prisma Cloud Remediation - Azure AKS Misconfiguration v2 | playbook | `remediating-azure-aks-misconfiguration` | Prisma Cloud by Palo Alto Networks |
| 12 | Prisma Cloud Remediation - Azure Storage Misconfiguration v2 | playbook | `remediating-azure-storage-misconfiguration` | Prisma Cloud by Palo Alto Networks |
| 13 | Prisma Cloud Remediation - GCP VPC Network Misconfiguration v2 | playbook | `remediating-gcp-vpc-network-misconfiguration` | Prisma Cloud by Palo Alto Networks |
| 14 | Cloud Data Exfiltration Response | playbook | `responding-to-cloud-data-exfiltration` | Cloud Incident Response |
| 15 | Cloud Token Theft Response | playbook | `responding-to-cloud-token-theft` | Cloud Incident Response |

## digital-forensics（12）

| # | XSOAR 条目 | 类型 | 建议技能名 | 来源 Pack |
|---|---|---|---|---|
| 1 | Acquire And Analyze Host Forensics | playbook | `acquiring-host-forensics` | Windows Forensics |
| 2 | PS-Remote Get MFT | playbook | `acquiring-mft-over-winrm` | Windows Forensics |
| 3 | PS-Remote Get Registry | playbook | `acquiring-registry-hives-over-winrm` | Windows Forensics |
| 4 | PS-Remote Acquire Host Forensics | playbook | `acquiring-windows-forensics-over-winrm` | Windows Forensics |
| 5 | Forensics Tools Analysis | playbook | `analyzing-forensic-tool-output` | Windows Forensics |
| 6 | PcapMinerV2 | script | `analyzing-pcap-files-with-pcapminer` | PCAP Analysis |
| 7 | PS-Remote Get Network Traffic | playbook | `capturing-network-traffic-over-winrm` | Windows Forensics |
| 8 | PcapHTTPExtractor | script | `extracting-http-flows-from-pcap` | Common Scripts |
| 9 | PcapFileExtractStreams | script | `extracting-tcp-streams-from-pcap` | PCAP Analysis |
| 10 | BMCTool | script | `parsing-rdp-bitmap-cache` | Common Scripts |
| 11 | Registry Parse Data Analysis | playbook | `parsing-registry-for-forensics` | Windows Forensics |
| 12 | RegistryParse | script | `parsing-windows-registry-hives` | Windows Forensics |

## identity-access-management（10）

| # | XSOAR 条目 | 类型 | 建议技能名 | 来源 Pack |
|---|---|---|---|---|
| 1 | Block Account - Generic v2 | playbook | `blocking-compromised-accounts` | Common Playbooks |
| 2 | Containment Plan - Clear User Sessions | playbook | `containing-incident-by-clearing-user-sessions` | Common Playbooks |
| 3 | Containment Plan - Disable Account | playbook | `containing-incident-by-disabling-accounts` | Common Playbooks |
| 4 | Cloud IAM Enrichment - Generic | playbook | `enriching-cloud-iam-identities` | Common Playbooks |
| 5 | Account Enrichment - Generic v2.1 | playbook | `enriching-user-accounts-during-investigation` | Common Playbooks |
| 6 | Get Cloud Account Owner - Generic | playbook | `identifying-cloud-account-owners` | Common Playbooks |
| 7 | Cloud IAM User Access Investigation | playbook | `investigating-cloud-iam-user-access` | Cloud Incident Response |
| 8 | Identity Analytics - Alert Handling | playbook | `investigating-identity-analytics-alerts` | Core |
| 9 | Impossible Traveler Response | playbook | `investigating-impossible-traveler-alerts` | Core |
| 10 | Cloud Credentials Rotation - Generic | playbook | `rotating-cloud-credentials` | Common Playbooks |

## vulnerability-management（9）

| # | XSOAR 条目 | 类型 | 建议技能名 | 来源 Pack |
|---|---|---|---|---|
| 1 | CVSSCalculator | script | `calculating-cvss-scores` | Common Scripts |
| 2 | cveReputationV2 | script | `enriching-cve-severity` | Common Scripts |
| 3 | CVE Enrichment - Generic v2 | playbook | `enriching-cve-vulnerabilities` | Common Playbooks |
| 4 | NexposeEmailParserForVuln | script | `parsing-nessus-nexpose-reports` | Rapid7 InsightVM |
| 5 | Cortex EM - AWS VM Exposure Remediation | playbook | `remediating-aws-vm-exposures` | Cortex Exposure Management |
| 6 | Cortex EM - Azure VM Exposure Remediation | playbook | `remediating-azure-vm-exposures` | Cortex Exposure Management |
| 7 | Cortex EM - Exposure Issue | playbook | `remediating-exposure-issues` | Cortex Exposure Management |
| 8 | Cortex EM - GCP VM Exposure Remediation | playbook | `remediating-gcp-vm-exposures` | Cortex Exposure Management |
| 9 | Search Endpoint by CVE - Generic | playbook | `searching-endpoints-by-cve` | Common Playbooks |

## threat-hunting（7）

| # | XSOAR 条目 | 类型 | 建议技能名 | 来源 Pack |
|---|---|---|---|---|
| 1 | AnalyzeTimestampIntervals | script | `detecting-beaconing-from-timestamp-intervals` | Common Scripts |
| 2 | FireEye Red Team Tools Investigation and Response | playbook | `hunting-fireeye-red-team-tools` | Rapid Breach Response |
| 3 | HAFNIUM - Exchange 0-day exploits | playbook | `hunting-hafnium-exchange-exploitation` | Rapid Breach Response |
| 4 | Proactive Threat Hunting - SDO Threat Hunting | playbook | `hunting-security-data-objects` | Proactive Threat Hunting |
| 5 | SolarStorm and SUNBURST Hunting and Response Playbook | playbook | `hunting-sunburst-backdoor` | Rapid Breach Response |
| 6 | Threat Hunting - Generic | playbook | `hunting-threat-indicators-across-siem` | Common Playbooks |
| 7 | Proactive Threat Hunting | playbook | `running-proactive-threat-hunts` | Proactive Threat Hunting |

## ransomware-defense（6）

| # | XSOAR 条目 | 类型 | 建议技能名 | 来源 Pack |
|---|---|---|---|---|
| 1 | Rubrik Ransomware Discovery and File Recovery - Rubrik Polaris | playbook | `recovering-ransomware-files-with-rubrik` | Rubrik Security Cloud |
| 2 | Veeam - Start Instant VM Recovery Automatically | playbook | `recovering-vms-with-veeam` | Veeam App |
| 3 | Rubrik DSPM Violation Remediation - Rubrik Security Cloud | playbook | `remediating-dspm-violations-with-rubrik` | Rubrik Security Cloud |
| 4 | Rubrik Anomaly Incident Response - Rubrik Polaris | playbook | `responding-to-ransomware-anomalies-with-rubrik` | Rubrik Security Cloud |
| 5 | Veeam - Start Scan Backup | playbook | `scanning-backups-with-veeam` | Veeam App |
| 6 | Rubrik IOC Scan - Rubrik Polaris | playbook | `scanning-for-iocs-with-rubrik` | Rubrik Security Cloud |

## network-security（4）

| # | XSOAR 条目 | 类型 | 建议技能名 | 来源 Pack |
|---|---|---|---|---|
| 1 | Block IP - Generic v3 | playbook | `blocking-malicious-ip-addresses` | Common Playbooks |
| 2 | NGFW Internal Scan | playbook | `investigating-internal-network-scans` | Core |
| 3 | NGFW Scan | playbook | `investigating-network-scan-alerts` | Core |
| 4 | Port Scan - Generic | playbook | `investigating-port-scan-alerts` | Port Scan |

## container-security（2）

| # | XSOAR 条目 | 类型 | 建议技能名 | 来源 Pack |
|---|---|---|---|---|
| 1 | Prisma Cloud Compute - Compliance Alert v2 | playbook | `remediating-prisma-cloud-compliance-alerts` | Prisma Cloud Compute by Palo Alto Networks |
| 2 | Cortex XDR - Malicious Pod Response - Agent | playbook | `responding-to-malicious-kubernetes-pods` | Cloud Incident Response |

## soc-operations（2）

| # | XSOAR 条目 | 类型 | 建议技能名 | 来源 Pack |
|---|---|---|---|---|
| 1 | Get User Devices - Generic | playbook | `inventorying-user-devices` | Common Playbooks |
| 2 | SIEM - Search for Failed logins | playbook | `searching-siem-for-failed-logins` | Common Playbooks |