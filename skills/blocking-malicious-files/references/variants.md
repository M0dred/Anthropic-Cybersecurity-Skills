# Vendor Variants - Blocking Malicious Files

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Block File - Carbon Black Response

**Product:** Carbon Black Enterprise Response

This playbook receives an MD5 hash and adds it to the block list in Carbon Black Enterprise Response. Files with that MD5 hash are blocked from execution on the managed endpoints. If the hash is already on the block list, no action is taken on the MD5. The playbook uses the integration ''VMware Carbon Black EDR v2"

**Inputs:**

- `MD5`: The MD5 hash of the file you want to block.
- `Text`: Text description of block list.

**Outputs:**

- `CbResponse.BlockedHashes.LastBlock.Time`
- `CbResponse.BlockedHashes.LastBlock.Hostname`
- `CbResponse.BlockedHashes.LastBlock.CbSensorID`

**Dependencies:**

- Integrations: CarbonBlackResponseV2
- Commands: cb-edr-binary-ban


## Block File - Cybereason

**Product:** Cybereason

This playbook accepts an MD5 hash and blocks the file using the Cybereason integration

**Inputs:**

- `MD5`: The MD5 hash of the file to block.

**Outputs:**

- `CbResponse.BlockedHashes.LastBlock.Time`
- `CbResponse.BlockedHashes.LastBlock.Hostname`
- `CbResponse.BlockedHashes.LastBlock.CbSensorID`

**Dependencies:**

- Integrations: Cybereason
- Commands: cybereason-prevent-file


## Block File - Cylance Protect v2

**Product:** Cylance Protect

This playbook accepts a SHA256 hash and adds the hash to the Global Quarantine list using the Cylance Protect v2 integration

**Inputs:**

- `SHA256`: The SHA256 hash of the file to block.
- `ListType`: The list type to which the threat belongs. Can be "GlobalQuarantine" or "GlobalSafe".

**Outputs:**

- `CbResponse.BlockedHashes.LastBlock.Time`
- `CbResponse.BlockedHashes.LastBlock.Hostname`
- `CbResponse.BlockedHashes.LastBlock.CbSensorID`

**Dependencies:**

- Integrations: Cylance_Protect_v2
- Commands: cylance-protect-add-hash-to-list


## Cortex XDR - Block File

**Product:** Cortex XDR by Palo Alto Networks

Use this playbook to add files to  XDR block list with a given file SHA256 playbook input

**Inputs:**

- `HashList`: List of hashed files you want to add to block list. Must be a valid SHA256 hash.

**Dependencies:**

- Integrations: CortexXDRIR
- Commands: xdr-blacklist-files

## Block File - Carbon Black Response

**Product:** Carbon Black Enterprise Response

This playbook receives an MD5 hash and adds it to the block list in Carbon Black Enterprise Response. Files with that MD5 hash are blocked from execution on the managed endpoints. If the hash is already on the block list, no action is taken on the MD5. The playbook uses the integration ''VMware Carbon Black EDR v2"

**Inputs:**

- `MD5`: The MD5 hash of the file you want to block.
- `Text`: Text description of block list.

**Outputs:**

- `CbResponse.BlockedHashes.LastBlock.Time`
- `CbResponse.BlockedHashes.LastBlock.Hostname`
- `CbResponse.BlockedHashes.LastBlock.CbSensorID`

**Dependencies:**

- Integrations: CarbonBlackResponseV2
- Commands: cb-edr-binary-ban


## Block File - Cybereason

**Product:** Cybereason

This playbook accepts an MD5 hash and blocks the file using the Cybereason integration

**Inputs:**

- `MD5`: The MD5 hash of the file to block.

**Outputs:**

- `CbResponse.BlockedHashes.LastBlock.Time`
- `CbResponse.BlockedHashes.LastBlock.Hostname`
- `CbResponse.BlockedHashes.LastBlock.CbSensorID`

**Dependencies:**

- Integrations: Cybereason
- Commands: cybereason-prevent-file


## Block File - Cylance Protect v2

**Product:** Cylance Protect

This playbook accepts a SHA256 hash and adds the hash to the Global Quarantine list using the Cylance Protect v2 integration

**Inputs:**

- `SHA256`: The SHA256 hash of the file to block.
- `ListType`: The list type to which the threat belongs. Can be "GlobalQuarantine" or "GlobalSafe".

**Outputs:**

- `CbResponse.BlockedHashes.LastBlock.Time`
- `CbResponse.BlockedHashes.LastBlock.Hostname`
- `CbResponse.BlockedHashes.LastBlock.CbSensorID`

**Dependencies:**

- Integrations: Cylance_Protect_v2
- Commands: cylance-protect-add-hash-to-list


## Cortex XDR - Block File

**Product:** Cortex XDR by Palo Alto Networks

Use this playbook to add files to  XDR block list with a given file SHA256 playbook input

**Inputs:**

- `HashList`: List of hashed files you want to add to block list. Must be a valid SHA256 hash.

**Dependencies:**

- Integrations: CortexXDRIR
- Commands: xdr-blacklist-files

## Block File - Carbon Black Response

**Product:** Carbon Black Enterprise Response

This playbook receives an MD5 hash and adds it to the block list in Carbon Black Enterprise Response. Files with that MD5 hash are blocked from execution on the managed endpoints. If the hash is already on the block list, no action is taken on the MD5. The playbook uses the integration ''VMware Carbon Black EDR v2"

**Inputs:**

- `MD5`: The MD5 hash of the file you want to block.
- `Text`: Text description of block list.

**Outputs:**

- `CbResponse.BlockedHashes.LastBlock.Time`
- `CbResponse.BlockedHashes.LastBlock.Hostname`
- `CbResponse.BlockedHashes.LastBlock.CbSensorID`

**Dependencies:**

- Integrations: CarbonBlackResponseV2
- Commands: cb-edr-binary-ban


## Block File - Cybereason

**Product:** Cybereason

This playbook accepts an MD5 hash and blocks the file using the Cybereason integration

**Inputs:**

- `MD5`: The MD5 hash of the file to block.

**Outputs:**

- `CbResponse.BlockedHashes.LastBlock.Time`
- `CbResponse.BlockedHashes.LastBlock.Hostname`
- `CbResponse.BlockedHashes.LastBlock.CbSensorID`

**Dependencies:**

- Integrations: Cybereason
- Commands: cybereason-prevent-file


## Block File - Cylance Protect v2

**Product:** Cylance Protect

This playbook accepts a SHA256 hash and adds the hash to the Global Quarantine list using the Cylance Protect v2 integration

**Inputs:**

- `SHA256`: The SHA256 hash of the file to block.
- `ListType`: The list type to which the threat belongs. Can be "GlobalQuarantine" or "GlobalSafe".

**Outputs:**

- `CbResponse.BlockedHashes.LastBlock.Time`
- `CbResponse.BlockedHashes.LastBlock.Hostname`
- `CbResponse.BlockedHashes.LastBlock.CbSensorID`

**Dependencies:**

- Integrations: Cylance_Protect_v2
- Commands: cylance-protect-add-hash-to-list


## Cortex XDR - Block File

**Product:** Cortex XDR by Palo Alto Networks

Use this playbook to add files to  XDR block list with a given file SHA256 playbook input

**Inputs:**

- `HashList`: List of hashed files you want to add to block list. Must be a valid SHA256 hash.

**Dependencies:**

- Integrations: CortexXDRIR
- Commands: xdr-blacklist-files

## Block File - Carbon Black Response

**Product:** Carbon Black Enterprise Response

This playbook receives an MD5 hash and adds it to the block list in Carbon Black Enterprise Response. Files with that MD5 hash are blocked from execution on the managed endpoints. If the hash is already on the block list, no action is taken on the MD5. The playbook uses the integration ''VMware Carbon Black EDR v2"

**Inputs:**

- `MD5`: The MD5 hash of the file you want to block.
- `Text`: Text description of block list.

**Outputs:**

- `CbResponse.BlockedHashes.LastBlock.Time`
- `CbResponse.BlockedHashes.LastBlock.Hostname`
- `CbResponse.BlockedHashes.LastBlock.CbSensorID`

**Dependencies:**

- Integrations: CarbonBlackResponseV2
- Commands: cb-edr-binary-ban


## Block File - Cybereason

**Product:** Cybereason

This playbook accepts an MD5 hash and blocks the file using the Cybereason integration

**Inputs:**

- `MD5`: The MD5 hash of the file to block.

**Outputs:**

- `CbResponse.BlockedHashes.LastBlock.Time`
- `CbResponse.BlockedHashes.LastBlock.Hostname`
- `CbResponse.BlockedHashes.LastBlock.CbSensorID`

**Dependencies:**

- Integrations: Cybereason
- Commands: cybereason-prevent-file


## Block File - Cylance Protect v2

**Product:** Cylance Protect

This playbook accepts a SHA256 hash and adds the hash to the Global Quarantine list using the Cylance Protect v2 integration

**Inputs:**

- `SHA256`: The SHA256 hash of the file to block.
- `ListType`: The list type to which the threat belongs. Can be "GlobalQuarantine" or "GlobalSafe".

**Outputs:**

- `CbResponse.BlockedHashes.LastBlock.Time`
- `CbResponse.BlockedHashes.LastBlock.Hostname`
- `CbResponse.BlockedHashes.LastBlock.CbSensorID`

**Dependencies:**

- Integrations: Cylance_Protect_v2
- Commands: cylance-protect-add-hash-to-list


## Cortex XDR - Block File

**Product:** Cortex XDR by Palo Alto Networks

Use this playbook to add files to  XDR block list with a given file SHA256 playbook input

**Inputs:**

- `HashList`: List of hashed files you want to add to block list. Must be a valid SHA256 hash.

**Dependencies:**

- Integrations: CortexXDRIR
- Commands: xdr-blacklist-files

