---
name: detecting-bec-vendor-fraud
description: >-
  Detects and responds to Business Email Compromise (BEC) vendor fraud, where
  attackers impersonate suppliers to redirect payments or steal goods. Covers
  invoice fraud, payment redirection, W-2 theft, and gift card scams. Use when a
  supplier requests a bank account change, when an executive asks for an urgent
  wire transfer, when payroll reports unusual direct deposit changes, or when
  training finance teams on fraud detection. Keywords: BEC, vendor fraud, invoice
  fraud, payment redirection, W-2 theft, gift card scam, executive impersonation.
  Do not use for general phishing detection - use
  investigating-phishing-email-incident. Do not use for email authentication
  analysis - use validating-email-authentication-results.
domain: cybersecurity
subdomain: phishing-defense
tags:
- bec
- vendor-fraud
- invoice-fraud
- payment-redirection
- social-engineering
version: "1.0"
author: mahipal
license: Apache-2.0
nist_csf:
- DE.AE-02
- RS.AN-03
- PR.AT-01
mitre_attack:
- T1566.001
- T1566.002
- T1656
---

# Detecting BEC Vendor Fraud

## When to Use

- A supplier emails a new bank account for invoice payment.
- An "executive" requests an urgent wire transfer or gift card purchase.
- Payroll reports unusual direct deposit change requests.
- HR receives a W-2 request that looks legitimate.
- Training finance and AP teams on fraud indicators.

**Do not use** for general phishing detection; that is a broader category.
**Do not use** for email authentication analysis (SPF/DKIM/DMARC); that is a
technical control, not fraud detection.

## Prerequisites

- Access to finance and AP email inboxes.
- A verified supplier contact database.
- Out-of-band verification procedures (phone, not email).
- Incident response contacts at your bank.

## Workflow

### Step 1: Know the fraud patterns

| Pattern | Indicator | Loss |
|---|---|---|
| Invoice fraud | Supplier sends new bank details | $10k–$1M |
| Payment redirection | "Executive" requests urgent wire | $50k–$5M |
| W-2 theft | "Employee" requests W-2 for verification | Identity theft |
| Gift card scam | "Boss" asks for iTunes/Google Play cards | $500–$50k |
| Payroll diversion | Employee requests direct deposit change | 1–2 paychecks |
| Vendor impersonation | Fake domain mimics real supplier | Goods or payments |

### Step 2: Detect red flags

**Email indicators:**
- Reply-to address differs from display name.
- Domain is one character off (rnicrosoft.com, g00gle.com).
- Urgent, confidential, or time-sensitive language.
- Unusual tone for the supposed sender.
- Sent outside business hours.

**Request indicators:**
- Bank account change with no prior notice.
- New payment terms (e.g., "wire instead of ACH").
- Amount slightly different from usual invoices.
- Request to bypass normal approval流程.

### Step 3: Verify out-of-band

```text
NEVER verify a bank account change or payment request via email.
Always call the supplier at a known, previously verified number.
If the request came from an executive, call their assistant or
known mobile number.
```

Document the verification: who called, what number, what was confirmed.

### Step 4: Respond to confirmed fraud

1. **Notify the bank immediately.** Wire transfers can be recalled within 24-48 hours.
2. **Report to the FBI IC3** (ic3.gov) for BEC recovery.
3. **Preserve evidence:** headers, email bodies, envelope information.
4. **Notify the supplier** through a verified channel.
5. **Reset credentials** for the compromised account.

### Step 5: Prevent recurrence

- Require dual approval for bank account changes.
- Maintain a verified supplier contact database.
- Train finance teams on red flags quarterly.
- Implement DMARC with enforcement (p=reject).
- Flag external emails with "[EXTERNAL]" in the subject.

## Verification

- All bank account changes are verified by phone within 24 hours.
- Finance team can name the top 3 red flags.
- No payment is released without dual approval for new vendors.
- DMARC is enforced (p=reject) for the domain.
- BEC simulation shows <5% click-through rate.

## Common Pitfalls

- **Verifying via email.** The attacker controls the email thread.
- **Trusting display names.** Display names are trivially spoofed.
- **No dual approval.** Single-approval payments are the primary target.
- **Delayed reporting.** The first 24 hours are critical for wire recall.
- **Assuming the supplier is compromised.** Sometimes the attacker registers a lookalike domain instead.

## References

- `references/api-reference.md` - verification procedures and IC3 reporting
- `references/standards.md` - NIST, ATT&CK mappings
- `references/workflows.md` - detection and response flow
- `scripts/agent.py` - domain similarity and header analysis helper
