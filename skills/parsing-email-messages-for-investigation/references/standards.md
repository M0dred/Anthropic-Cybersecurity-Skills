# Standards and References - Parsing Email Messages for Investigation

## RFCs

| RFC | Title | Relevance |
|---|---|---|
| RFC 5322 | Internet Message Format | Header and body grammar |
| RFC 2045-2049 | MIME | Multipart structure, encodings |
| RFC 2047 | Encoded words in headers | Decoding `=?charset?B?...?=` |
| RFC 7208 | SPF | Sender IP authorization |
| RFC 6376 | DKIM | Domain-key signature |
| RFC 7489 | DMARC | Alignment and policy |
| RFC 6532 | Internationalized email headers | UTF-8 headers |

## NIST CSF 2.0

| Function | Category | Control |
|---|---|---|
| Detect | DE.AE-02 | Potentially adverse events are analyzed |
| Respond | RS.AN-03 | Analysis establishes what happened |
| Protect | PR.AT-01 | Personnel are aware of phishing |

## NIST SP 800-53 Rev. 5

| Control | Title | Relevance |
|---|---|---|
| SI-3 | Malicious Code Protection | Attachment inspection |
| SI-8 | Spam Protection | Email filtering and authentication |
| IR-4 | Incident Handling | Phishing triage is an IR procedure |
| AU-6 | Audit Record Review | Preserve the message as evidence |

## MITRE ATT&CK

| Technique | Name | Email evidence |
|---|---|---|
| T1566.001 | Phishing: Spearphishing Attachment | Attachment hash and name |
| T1566.002 | Phishing: Spearphishing Link | URL and redirect chain |
| T1204.002 | User Execution: Malicious File | Attachment opened by the user |
| T1585.002 | Establish Accounts: Email Accounts | Lookalike sender domain |
| T1656 | Impersonation | Display-name spoofing |

## MITRE ATLAS (AI-assisted triage)

- AML.T0047: ML model access — if an ML classifier scores the message, record
  the model version and score alongside the human verdict.

## Evidence handling

- Preserve the original file and its SHA-256 before parsing.
- Write attachments to a read-only evidence directory.
- Keep the defanged and original indicator values in separate fields.
- Record the parser version and the time of parsing.
