# Vendor Variants - Executing Incident Containment Plan

Vendor-specific implementations, feeds, and collectors for this procedure.


## Containment Plan - Block Indicators

**Product:** Common Playbooks

**Kind:** playbook

**Inputs:**

- `BlockIndicators`: Set to 'True' to block the indicators.
- `UserVerification`: Possible values: True/False.Whether to provide user verification for blocking those IPs. False - No prompt will be displayed to the user.True - The server will ask the user for blo
- `AutoBlockIndicators`: Possible values: True/False. Default: True.Should the given indicators be automatically blocked, or should the user be given the option to choose?If set to True - no prompt will ap
- `FileHash`: The file hash to block.
- `IP`: The IP indicators.
- `Domain`: The domain indicators.
- `URL`: The URL indicator.
- `Username`: The username to disable.
- `FilePath`: The path of the file to block.
- `AutoContainment`: Whether to execute containment plan automatically.

**Dependencies:**

- Sub-playbooks: Block Indicators - Generic v3
- Commands: setParentIncidentContext, core-blocklist-files

## Containment Plan - Block Indicators

**Product:** Common Playbooks

**Kind:** playbook

**Inputs:**

- `BlockIndicators`: Set to 'True' to block the indicators.
- `UserVerification`: Possible values: True/False.Whether to provide user verification for blocking those IPs. False - No prompt will be displayed to the user.True - The server will ask the user for blo
- `AutoBlockIndicators`: Possible values: True/False. Default: True.Should the given indicators be automatically blocked, or should the user be given the option to choose?If set to True - no prompt will ap
- `FileHash`: The file hash to block.
- `IP`: The IP indicators.
- `Domain`: The domain indicators.
- `URL`: The URL indicator.
- `Username`: The username to disable.
- `FilePath`: The path of the file to block.
- `AutoContainment`: Whether to execute containment plan automatically.

**Dependencies:**

- Sub-playbooks: Block Indicators - Generic v3
- Commands: setParentIncidentContext, core-blocklist-files

## Containment Plan - Block Indicators

**Product:** Common Playbooks

**Kind:** playbook

**Inputs:**

- `BlockIndicators`: Set to 'True' to block the indicators.
- `UserVerification`: Possible values: True/False.Whether to provide user verification for blocking those IPs. False - No prompt will be displayed to the user.True - The server will ask the user for blo
- `AutoBlockIndicators`: Possible values: True/False. Default: True.Should the given indicators be automatically blocked, or should the user be given the option to choose?If set to True - no prompt will ap
- `FileHash`: The file hash to block.
- `IP`: The IP indicators.
- `Domain`: The domain indicators.
- `URL`: The URL indicator.
- `Username`: The username to disable.
- `FilePath`: The path of the file to block.
- `AutoContainment`: Whether to execute containment plan automatically.

**Dependencies:**

- Sub-playbooks: Block Indicators - Generic v3
- Commands: setParentIncidentContext, core-blocklist-files

