# Standards and References - Extracting Indicators from Files

## STIX 2.1

| Object | Use |
|---|---|
| `indicator` | A pattern with a STIX pattern expression |
| `observed-data` | A bundle of observations with `first_observed` |
| `malware` | The family an indicator belongs to |
| `infrastructure` | C2 or staging infrastructure |
| `relationship` | `indicates`, `uses`, `targets` |

Pattern examples:

```
[ipv4-addr:value = '203.0.113.10']
[domain-name:value = 'evil.example']
[url:value = 'https://evil.example/a']
[file:hashes.'SHA-256' = 'abc...']
[email-addr:value = 'phish@evil.example']
```

## MISP

| Attribute type | Category |
|---|---|
| `ip-dst`, `ip-src` | Network activity |
| `domain`, `hostname` | Network activity |
| `url` | Network activity |
| `md5`, `sha1`, `sha256` | Payload delivery |
| `email-src`, `email-dst` | Payload delivery |
| `filename` | Payload delivery |

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Identify | ID.RA-01 | Vulnerabilities and threats are identified |
| Detect | DE.AE-02 | Adverse events are analyzed |
| Respond | RS.AN-03 | Analysis establishes what happened |

## NIST SP 800-53 Rev. 5

| Control | Title | Relevance |
|---|---|---|
| SI-4 | System Monitoring | Indicators feed monitoring |
| IR-4 | Incident Handling | Extraction supports analysis |
| RA-3 | Risk Assessment | Threat intelligence informs risk |
| AU-6 | Audit Record Review | Evidence preservation |

## MITRE ATT&CK

| Technique | Name | Indicator relevance |
|---|---|---|
| T1588.001 | Obtain Capabilities: Malware | Hashes and family names |
| T1204.002 | User Execution: Malicious File | Attachment hashes |
| T1027 | Obfuscated Files or Information | Defanged and encoded strings |
| T1583.001 | Acquire Infrastructure: Domains | Domain indicators |
| T1071 | Application Layer Protocol | URL and domain C2 |

## Confidence model

| Factor | Weight |
|---|---|
| Structural validity (parses as the claimed type) | 0.2 |
| Context mentions malware, phishing, C2, or a CVE | 0.2 |
| Appears more than once | 0.1 |
| Not on the allowlist | 0.2 |
| Not a shared or public service | 0.2 |
| Corroborated by a second source | 0.1 |

Scores are advisory. A human decides whether an indicator is malicious.
