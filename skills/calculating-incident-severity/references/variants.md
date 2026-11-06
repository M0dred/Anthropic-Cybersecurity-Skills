# Vendor Variants - Calculating Incident Severity

Vendor-specific implementations, feeds, and collectors for this procedure.


## Calculate Severity - 3rd-party integrations

**Product:** Common Playbooks

**Kind:** playbook

Calculates the incident severity level according to the methodology of a 3rd-party integration

**Inputs:**

- `QualysSeverity`: The Qualys vulnerability severity score (1-5).
- `NexposeSeverity`: The Nexpose vulnerability severity score. Can be, "Moderate", "Severe", "Critical").

**Dependencies:**

- Scripts: Set

## Calculate Severity - Standard

**Product:** Common Playbooks

**Kind:** playbook

Calculates and sets the incident severity based on the combination of the current incident severity, and the severity returned from the Calculate Severity By Highest DBotScore playbook

**Inputs:**

- `DBotScoreIndicators`: A list of DBotScore indicator values.
- `DBotScoreMaxScore`: The highest score (number) that was given to a DBotScore indicator.

**Dependencies:**

- Commands: setIncident

## Calculate Severity By Highest DBotScore

**Product:** Common Playbooks

**Kind:** playbook

Calculates the incident severity level according to the highest DBotScore

**Inputs:**

- `DBotScoreIndicators`: Array of all DBotScore indicator values associated with the incident.
- `DBotScoreMaxScore`: The highest score (number) that was given to a DBotScore indicator.

**Dependencies:**

- Scripts: Set, GetIndicatorDBotScoreFromCache

## Calculate Severity - 3rd-party integrations

**Product:** Common Playbooks

**Kind:** playbook

Calculates the incident severity level according to the methodology of a 3rd-party integration

**Inputs:**

- `QualysSeverity`: The Qualys vulnerability severity score (1-5).
- `NexposeSeverity`: The Nexpose vulnerability severity score. Can be, "Moderate", "Severe", "Critical").

**Dependencies:**

- Scripts: Set

## Calculate Severity - Standard

**Product:** Common Playbooks

**Kind:** playbook

Calculates and sets the incident severity based on the combination of the current incident severity, and the severity returned from the Calculate Severity By Highest DBotScore playbook

**Inputs:**

- `DBotScoreIndicators`: A list of DBotScore indicator values.
- `DBotScoreMaxScore`: The highest score (number) that was given to a DBotScore indicator.

**Dependencies:**

- Commands: setIncident

## Calculate Severity By Highest DBotScore

**Product:** Common Playbooks

**Kind:** playbook

Calculates the incident severity level according to the highest DBotScore

**Inputs:**

- `DBotScoreIndicators`: Array of all DBotScore indicator values associated with the incident.
- `DBotScoreMaxScore`: The highest score (number) that was given to a DBotScore indicator.

**Dependencies:**

- Scripts: Set, GetIndicatorDBotScoreFromCache

## Calculate Severity - 3rd-party integrations

**Product:** Common Playbooks

**Kind:** playbook

Calculates the incident severity level according to the methodology of a 3rd-party integration

**Inputs:**

- `QualysSeverity`: The Qualys vulnerability severity score (1-5).
- `NexposeSeverity`: The Nexpose vulnerability severity score. Can be, "Moderate", "Severe", "Critical").

**Dependencies:**

- Scripts: Set

## Calculate Severity - Standard

**Product:** Common Playbooks

**Kind:** playbook

Calculates and sets the incident severity based on the combination of the current incident severity, and the severity returned from the Calculate Severity By Highest DBotScore playbook

**Inputs:**

- `DBotScoreIndicators`: A list of DBotScore indicator values.
- `DBotScoreMaxScore`: The highest score (number) that was given to a DBotScore indicator.

**Dependencies:**

- Commands: setIncident

## Calculate Severity By Highest DBotScore

**Product:** Common Playbooks

**Kind:** playbook

Calculates the incident severity level according to the highest DBotScore

**Inputs:**

- `DBotScoreIndicators`: Array of all DBotScore indicator values associated with the incident.
- `DBotScoreMaxScore`: The highest score (number) that was given to a DBotScore indicator.

**Dependencies:**

- Scripts: Set, GetIndicatorDBotScoreFromCache

