# Vendor Variants - Detonating Files With Threatzone

Vendor-specific implementations, feeds, and collectors for this procedure.


## Analyze File - Sandbox - ThreatZone

**Product:** ThreatZone

**Kind:** playbook

Analyzes one file using the ThreatZone sandbox integration. Returns relevant reports to the War Room and file reputations to the context data. Dynamic Scan Extensions: exe, docx, dochtml, docm, doc, rtf, ps1, bat, cmd, xlw, xltx, xltm, xls, xlsx, odc, csv, xlshtml

**Inputs:**

- `File`: File object of the file to analyze. The File is taken from the context.
- `Interval`: Frequency (in minutes) between polling attempts.
- `Timeout`: Maximum polling duration (in minutes) before the playbook resumes.

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: ThreatZone
- Commands: tz-get-result, tz-sandbox-upload-sample

## Analyze File - Static Scan - ThreatZone

**Product:** ThreatZone

**Kind:** playbook

Analyzes one file using the ThreatZone static scan integration. Returns relevant reports to the War Room and file reputations to the context data. All file types are supported

**Inputs:**

- `File`: File object of the file to analyze. The File is taken from the context.
- `Interval`: Frequency (in minutes) between polling attempts.
- `Timeout`: Maximum polling duration (in minutes) before the playbook resumes.

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: ThreatZone
- Commands: tz-static-upload-sample, tz-get-result

## Analyze File - Sandbox - ThreatZone

**Product:** ThreatZone

**Kind:** playbook

Analyzes one file using the ThreatZone sandbox integration. Returns relevant reports to the War Room and file reputations to the context data. Dynamic Scan Extensions: exe, docx, dochtml, docm, doc, rtf, ps1, bat, cmd, xlw, xltx, xltm, xls, xlsx, odc, csv, xlshtml

**Inputs:**

- `File`: File object of the file to analyze. The File is taken from the context.
- `Interval`: Frequency (in minutes) between polling attempts.
- `Timeout`: Maximum polling duration (in minutes) before the playbook resumes.

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: ThreatZone
- Commands: tz-get-result, tz-sandbox-upload-sample

## Analyze File - Static Scan - ThreatZone

**Product:** ThreatZone

**Kind:** playbook

Analyzes one file using the ThreatZone static scan integration. Returns relevant reports to the War Room and file reputations to the context data. All file types are supported

**Inputs:**

- `File`: File object of the file to analyze. The File is taken from the context.
- `Interval`: Frequency (in minutes) between polling attempts.
- `Timeout`: Maximum polling duration (in minutes) before the playbook resumes.

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: ThreatZone
- Commands: tz-static-upload-sample, tz-get-result

## Analyze File - Sandbox - ThreatZone

**Product:** ThreatZone

**Kind:** playbook

Analyzes one file using the ThreatZone sandbox integration. Returns relevant reports to the War Room and file reputations to the context data. Dynamic Scan Extensions: exe, docx, dochtml, docm, doc, rtf, ps1, bat, cmd, xlw, xltx, xltm, xls, xlsx, odc, csv, xlshtml

**Inputs:**

- `File`: File object of the file to analyze. The File is taken from the context.
- `Interval`: Frequency (in minutes) between polling attempts.
- `Timeout`: Maximum polling duration (in minutes) before the playbook resumes.

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: ThreatZone
- Commands: tz-get-result, tz-sandbox-upload-sample

## Analyze File - Static Scan - ThreatZone

**Product:** ThreatZone

**Kind:** playbook

Analyzes one file using the ThreatZone static scan integration. Returns relevant reports to the War Room and file reputations to the context data. All file types are supported

**Inputs:**

- `File`: File object of the file to analyze. The File is taken from the context.
- `Interval`: Frequency (in minutes) between polling attempts.
- `Timeout`: Maximum polling duration (in minutes) before the playbook resumes.

**Dependencies:**

- Sub-playbooks: GenericPolling
- Integrations: ThreatZone
- Commands: tz-static-upload-sample, tz-get-result

