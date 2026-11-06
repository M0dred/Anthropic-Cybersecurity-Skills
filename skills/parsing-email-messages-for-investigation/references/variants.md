# Vendor Variants - Parsing Email Messages For Investigation

Vendor-specific implementations, feeds, and collectors for this procedure.


## ParseEmailFiles

**Product:** Common Scripts

**Kind:** script

Parse an email from an eml or msg file and populate all relevant context data to investigate the email. Also extracts inner attachments and returns them to the war room. The incident labels themselves are preserved and not modified - only the "Label/x" context items that originated from the labels, and the best practice is to rely on these for the remainder of the playbook

**Inputs:**

- `entryid`: Entry ID with the Email as a file in msg or eml format
- `parse_only_headers`: Will parse only the headers and return headers table
- `max_depth`: How many levels deep we should parse the attached emails (e.g. email contains an emails contains an email). Default depth level is 3. Minimum level is 1, if set to 1 the script wil

## ParseEmailFiles

**Product:** Common Scripts

**Kind:** script

Parse an email from an eml or msg file and populate all relevant context data to investigate the email. Also extracts inner attachments and returns them to the war room. The incident labels themselves are preserved and not modified - only the "Label/x" context items that originated from the labels, and the best practice is to rely on these for the remainder of the playbook

**Inputs:**

- `entryid`: Entry ID with the Email as a file in msg or eml format
- `parse_only_headers`: Will parse only the headers and return headers table
- `max_depth`: How many levels deep we should parse the attached emails (e.g. email contains an emails contains an email). Default depth level is 3. Minimum level is 1, if set to 1 the script wil

