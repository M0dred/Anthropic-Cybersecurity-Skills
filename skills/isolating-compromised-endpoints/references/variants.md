# Vendor Variants - Isolating Compromised Endpoints

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Block Endpoint - Carbon Black Response V2.1

**Product:** Carbon Black Enterprise Response

Carbon Black Response - isolates an endpoint for a given hostname

**Inputs:**

- `Hostname`: The hostname to isolate.
- `Sensor_id`: The sensor ID of the endpoint.

**Outputs:**

- `CarbonBlackEDR.Sensor`
- `CarbonBlackEDR.Sensor.systemvolume_total_size`
- `CarbonBlackEDR.Sensor.emet_telemetry_path`
- `CarbonBlackEDR.Sensor.os_environment_display_string`
- `CarbonBlackEDR.Sensor.emet_version`
- `CarbonBlackEDR.Sensor.emet_dump_flags`
- `CarbonBlackEDR.Sensor.clock_delta`
- `CarbonBlackEDR.Sensor.supports_cblr`
- `CarbonBlackEDR.Sensor.sensor_uptime`
- `CarbonBlackEDR.Sensor.last_update`

**Dependencies:**

- Scripts: IsIntegrationAvailable, Set
- Commands: cb-edr-sensors-list, cb-edr-quarantine-device


## Carbon Black Response - Unisolate Endpoint

**Product:** Carbon Black Enterprise Response

This playbook unisolates sensors according to the sensor ID that is provided in the playbook input

**Inputs:**

- `Endpoint_ID`: The sensor id you want to unisolate.

**Dependencies:**

- Integrations: carbonblack-v2
- Scripts: IsIntegrationAvailable
- Commands: cb-sensor-info, cb-list-sensors, cb-unquarantine-device


## Cortex XDR - Unisolate Endpoint

**Product:** Cortex XDR by Palo Alto Networks

This playbook unisolates endpoints according to the endpoint ID that is provided in the playbook input

**Inputs:**

- `Endpoint_ID`: The endpoint ID that you want to be unisolated.
- `Hostname`: The endpoint's hostname that you want to be unisolated.
- `IP`: The endpoint's IP that you want to be unisolated.

**Dependencies:**

- Integrations: CortexXDRIR
- Scripts: IsIntegrationAvailable
- Commands: xdr-endpoint-unisolate, xdr-get-endpoints


## Crowdstrike Falcon - Unisolate Endpoint

**Product:** CrowdStrike Falcon

This playbook unisolates devices according to the device ID that is provided in the playbook input

**Inputs:**

- `Endpoint_id`: The endpoint ID/device ID that you want to unisolate.

**Dependencies:**

- Commands: cs-falcon-lift-host-containment, cs-falcon-search-device


## FireEye HX - Unisolate Endpoint

**Product:** FireEye HX

This playbook unisolates endpoints according to the hostname/endpoint ID that is provided by the playbook input

**Inputs:**

- `Endpoint_id`: The endpoint ID/device ID that you want to unisolate.
- `Hostname`: The hostname that you want to unisolate.

**Dependencies:**

- Commands: fireeye-hx-get-host-information, fireeye-hx-cancel-containment


## Microsoft Defender For Endpoint - Unisolate Endpoint

**Product:** Microsoft Defender for Endpoint

This playbook accepts an endpoint ID, IP, or host name and unisolates it using the Microsoft Defender For Endpoint integration

**Inputs:**

- `Device_id`: The device ID to isolate.For more information about the device, you can use the following commands:!microsoft-atp-get-machine-details!microsoft-atp-get-machines
- `Hostname`: The device host name you want to isolate.
- `Device_IP`: The device IP you want to isolate.

**Outputs:**

- `MicrosoftATP.MachineAction.ID`
- `MicrosoftATP.NonUnisolateList`
- `MicrosoftATP.UnisolateList`
- `MicrosoftATP.IncorrectIDs`
- `MicrosoftATP.IncorrectHostnames`
- `MicrosoftATP.IncorrectIPs`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Scripts: SetAndHandleEmpty, isError, IsIntegrationAvailable, Print
- Commands: endpoint, microsoft-atp-unisolate-machine


## Rapid ransomware containment - Illumio

**Product:** Illumio Rapid Ransomware Containment

Isolate one or more workloads based on traffic flows to a given port/protocol

**Inputs:**

- `Port`: Provide Port to be blocked.
- `Protocol`: Protocol of Port.
- `Allow Traffic?`: Do You want to allow traffic on this port? (Yes or No)
- `Update the enforcement mode?`: Do you want to update the enforcement mode?(Yes or No)

**Dependencies:**

- Sub-playbooks: Update enforcement mode - Illumio
- Integrations: IllumioCore
- Scripts: Print
- Commands: illumio-object-provision, illumio-workloads-list, illumio-ip-lists-get, illumio-ruleset-create, illumio-enforcement-boundary-create, illumio-service-binding-create, illumio-virtual-service-create, illumio-rule-create


## Scan and Isolate - XM Cyber

**Product:** XM Cyber

An example of playbook using data from XM Cyber to help decide about scanning and isolating a threat

**Outputs:**

- `Traps.IsolateResult.Status`
- `Nexpose.Scan.Status`
- `Nexpose.Scan.Assets`
- `Nexpose.Scan.Vulnerabilities.Total`
- `XMCyber.Entity.isAsset`
- `XMCyber.Entity.averageComplexityLevel`
- `XMCyber.Entity.criticalAssetsAtRisk`

**Dependencies:**

- Sub-playbooks: Isolate Endpoint - Generic V2, Endpoint Enrichment By Hostname - XM Cyber, Endpoint Enrichment By IP - XM Cyber, Scan Assets - Nexpose


## Unisolate Endpoint - Cybereason

**Product:** Cybereason

This playbook unisolates a machine based on the hostname provided

**Inputs:**

- `Hostname`: The hostname of the endpoint you want to unisolate.

## Block Endpoint - Carbon Black Response V2.1

**Product:** Carbon Black Enterprise Response

Carbon Black Response - isolates an endpoint for a given hostname

**Inputs:**

- `Hostname`: The hostname to isolate.
- `Sensor_id`: The sensor ID of the endpoint.

**Outputs:**

- `CarbonBlackEDR.Sensor`
- `CarbonBlackEDR.Sensor.systemvolume_total_size`
- `CarbonBlackEDR.Sensor.emet_telemetry_path`
- `CarbonBlackEDR.Sensor.os_environment_display_string`
- `CarbonBlackEDR.Sensor.emet_version`
- `CarbonBlackEDR.Sensor.emet_dump_flags`
- `CarbonBlackEDR.Sensor.clock_delta`
- `CarbonBlackEDR.Sensor.supports_cblr`
- `CarbonBlackEDR.Sensor.sensor_uptime`
- `CarbonBlackEDR.Sensor.last_update`

**Dependencies:**

- Scripts: IsIntegrationAvailable, Set
- Commands: cb-edr-sensors-list, cb-edr-quarantine-device


## Carbon Black Response - Unisolate Endpoint

**Product:** Carbon Black Enterprise Response

This playbook unisolates sensors according to the sensor ID that is provided in the playbook input

**Inputs:**

- `Endpoint_ID`: The sensor id you want to unisolate.

**Dependencies:**

- Integrations: carbonblack-v2
- Scripts: IsIntegrationAvailable
- Commands: cb-sensor-info, cb-list-sensors, cb-unquarantine-device


## Cortex XDR - Unisolate Endpoint

**Product:** Cortex XDR by Palo Alto Networks

This playbook unisolates endpoints according to the endpoint ID that is provided in the playbook input

**Inputs:**

- `Endpoint_ID`: The endpoint ID that you want to be unisolated.
- `Hostname`: The endpoint's hostname that you want to be unisolated.
- `IP`: The endpoint's IP that you want to be unisolated.

**Dependencies:**

- Integrations: CortexXDRIR
- Scripts: IsIntegrationAvailable
- Commands: xdr-endpoint-unisolate, xdr-get-endpoints


## Crowdstrike Falcon - Unisolate Endpoint

**Product:** CrowdStrike Falcon

This playbook unisolates devices according to the device ID that is provided in the playbook input

**Inputs:**

- `Endpoint_id`: The endpoint ID/device ID that you want to unisolate.

**Dependencies:**

- Commands: cs-falcon-lift-host-containment, cs-falcon-search-device


## FireEye HX - Unisolate Endpoint

**Product:** FireEye HX

This playbook unisolates endpoints according to the hostname/endpoint ID that is provided by the playbook input

**Inputs:**

- `Endpoint_id`: The endpoint ID/device ID that you want to unisolate.
- `Hostname`: The hostname that you want to unisolate.

**Dependencies:**

- Commands: fireeye-hx-get-host-information, fireeye-hx-cancel-containment


## Microsoft Defender For Endpoint - Unisolate Endpoint

**Product:** Microsoft Defender for Endpoint

This playbook accepts an endpoint ID, IP, or host name and unisolates it using the Microsoft Defender For Endpoint integration

**Inputs:**

- `Device_id`: The device ID to isolate.For more information about the device, you can use the following commands:!microsoft-atp-get-machine-details!microsoft-atp-get-machines
- `Hostname`: The device host name you want to isolate.
- `Device_IP`: The device IP you want to isolate.

**Outputs:**

- `MicrosoftATP.MachineAction.ID`
- `MicrosoftATP.NonUnisolateList`
- `MicrosoftATP.UnisolateList`
- `MicrosoftATP.IncorrectIDs`
- `MicrosoftATP.IncorrectHostnames`
- `MicrosoftATP.IncorrectIPs`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Scripts: SetAndHandleEmpty, isError, IsIntegrationAvailable, Print
- Commands: endpoint, microsoft-atp-unisolate-machine


## Rapid ransomware containment - Illumio

**Product:** Illumio Rapid Ransomware Containment

Isolate one or more workloads based on traffic flows to a given port/protocol

**Inputs:**

- `Port`: Provide Port to be blocked.
- `Protocol`: Protocol of Port.
- `Allow Traffic?`: Do You want to allow traffic on this port? (Yes or No)
- `Update the enforcement mode?`: Do you want to update the enforcement mode?(Yes or No)

**Dependencies:**

- Sub-playbooks: Update enforcement mode - Illumio
- Integrations: IllumioCore
- Scripts: Print
- Commands: illumio-object-provision, illumio-workloads-list, illumio-ip-lists-get, illumio-ruleset-create, illumio-enforcement-boundary-create, illumio-service-binding-create, illumio-virtual-service-create, illumio-rule-create


## Scan and Isolate - XM Cyber

**Product:** XM Cyber

An example of playbook using data from XM Cyber to help decide about scanning and isolating a threat

**Outputs:**

- `Traps.IsolateResult.Status`
- `Nexpose.Scan.Status`
- `Nexpose.Scan.Assets`
- `Nexpose.Scan.Vulnerabilities.Total`
- `XMCyber.Entity.isAsset`
- `XMCyber.Entity.averageComplexityLevel`
- `XMCyber.Entity.criticalAssetsAtRisk`

**Dependencies:**

- Sub-playbooks: Isolate Endpoint - Generic V2, Endpoint Enrichment By Hostname - XM Cyber, Endpoint Enrichment By IP - XM Cyber, Scan Assets - Nexpose


## Unisolate Endpoint - Cybereason

**Product:** Cybereason

This playbook unisolates a machine based on the hostname provided

**Inputs:**

- `Hostname`: The hostname of the endpoint you want to unisolate.

## Block Endpoint - Carbon Black Response V2.1

**Product:** Carbon Black Enterprise Response

Carbon Black Response - isolates an endpoint for a given hostname

**Inputs:**

- `Hostname`: The hostname to isolate.
- `Sensor_id`: The sensor ID of the endpoint.

**Outputs:**

- `CarbonBlackEDR.Sensor`
- `CarbonBlackEDR.Sensor.systemvolume_total_size`
- `CarbonBlackEDR.Sensor.emet_telemetry_path`
- `CarbonBlackEDR.Sensor.os_environment_display_string`
- `CarbonBlackEDR.Sensor.emet_version`
- `CarbonBlackEDR.Sensor.emet_dump_flags`
- `CarbonBlackEDR.Sensor.clock_delta`
- `CarbonBlackEDR.Sensor.supports_cblr`
- `CarbonBlackEDR.Sensor.sensor_uptime`
- `CarbonBlackEDR.Sensor.last_update`

**Dependencies:**

- Scripts: IsIntegrationAvailable, Set
- Commands: cb-edr-sensors-list, cb-edr-quarantine-device


## Carbon Black Response - Unisolate Endpoint

**Product:** Carbon Black Enterprise Response

This playbook unisolates sensors according to the sensor ID that is provided in the playbook input

**Inputs:**

- `Endpoint_ID`: The sensor id you want to unisolate.

**Dependencies:**

- Integrations: carbonblack-v2
- Scripts: IsIntegrationAvailable
- Commands: cb-sensor-info, cb-list-sensors, cb-unquarantine-device


## Cortex XDR - Unisolate Endpoint

**Product:** Cortex XDR by Palo Alto Networks

This playbook unisolates endpoints according to the endpoint ID that is provided in the playbook input

**Inputs:**

- `Endpoint_ID`: The endpoint ID that you want to be unisolated.
- `Hostname`: The endpoint's hostname that you want to be unisolated.
- `IP`: The endpoint's IP that you want to be unisolated.

**Dependencies:**

- Integrations: CortexXDRIR
- Scripts: IsIntegrationAvailable
- Commands: xdr-endpoint-unisolate, xdr-get-endpoints


## Crowdstrike Falcon - Unisolate Endpoint

**Product:** CrowdStrike Falcon

This playbook unisolates devices according to the device ID that is provided in the playbook input

**Inputs:**

- `Endpoint_id`: The endpoint ID/device ID that you want to unisolate.

**Dependencies:**

- Commands: cs-falcon-lift-host-containment, cs-falcon-search-device


## FireEye HX - Unisolate Endpoint

**Product:** FireEye HX

This playbook unisolates endpoints according to the hostname/endpoint ID that is provided by the playbook input

**Inputs:**

- `Endpoint_id`: The endpoint ID/device ID that you want to unisolate.
- `Hostname`: The hostname that you want to unisolate.

**Dependencies:**

- Commands: fireeye-hx-get-host-information, fireeye-hx-cancel-containment


## Microsoft Defender For Endpoint - Unisolate Endpoint

**Product:** Microsoft Defender for Endpoint

This playbook accepts an endpoint ID, IP, or host name and unisolates it using the Microsoft Defender For Endpoint integration

**Inputs:**

- `Device_id`: The device ID to isolate.For more information about the device, you can use the following commands:!microsoft-atp-get-machine-details!microsoft-atp-get-machines
- `Hostname`: The device host name you want to isolate.
- `Device_IP`: The device IP you want to isolate.

**Outputs:**

- `MicrosoftATP.MachineAction.ID`
- `MicrosoftATP.NonUnisolateList`
- `MicrosoftATP.UnisolateList`
- `MicrosoftATP.IncorrectIDs`
- `MicrosoftATP.IncorrectHostnames`
- `MicrosoftATP.IncorrectIPs`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Scripts: SetAndHandleEmpty, isError, IsIntegrationAvailable, Print
- Commands: endpoint, microsoft-atp-unisolate-machine


## Rapid ransomware containment - Illumio

**Product:** Illumio Rapid Ransomware Containment

Isolate one or more workloads based on traffic flows to a given port/protocol

**Inputs:**

- `Port`: Provide Port to be blocked.
- `Protocol`: Protocol of Port.
- `Allow Traffic?`: Do You want to allow traffic on this port? (Yes or No)
- `Update the enforcement mode?`: Do you want to update the enforcement mode?(Yes or No)

**Dependencies:**

- Sub-playbooks: Update enforcement mode - Illumio
- Integrations: IllumioCore
- Scripts: Print
- Commands: illumio-object-provision, illumio-workloads-list, illumio-ip-lists-get, illumio-ruleset-create, illumio-enforcement-boundary-create, illumio-service-binding-create, illumio-virtual-service-create, illumio-rule-create


## Scan and Isolate - XM Cyber

**Product:** XM Cyber

An example of playbook using data from XM Cyber to help decide about scanning and isolating a threat

**Outputs:**

- `Traps.IsolateResult.Status`
- `Nexpose.Scan.Status`
- `Nexpose.Scan.Assets`
- `Nexpose.Scan.Vulnerabilities.Total`
- `XMCyber.Entity.isAsset`
- `XMCyber.Entity.averageComplexityLevel`
- `XMCyber.Entity.criticalAssetsAtRisk`

**Dependencies:**

- Sub-playbooks: Isolate Endpoint - Generic V2, Endpoint Enrichment By Hostname - XM Cyber, Endpoint Enrichment By IP - XM Cyber, Scan Assets - Nexpose


## Unisolate Endpoint - Cybereason

**Product:** Cybereason

This playbook unisolates a machine based on the hostname provided

**Inputs:**

- `Hostname`: The hostname of the endpoint you want to unisolate.

## Block Endpoint - Carbon Black Response V2.1

**Product:** Carbon Black Enterprise Response

Carbon Black Response - isolates an endpoint for a given hostname

**Inputs:**

- `Hostname`: The hostname to isolate.
- `Sensor_id`: The sensor ID of the endpoint.

**Outputs:**

- `CarbonBlackEDR.Sensor`
- `CarbonBlackEDR.Sensor.systemvolume_total_size`
- `CarbonBlackEDR.Sensor.emet_telemetry_path`
- `CarbonBlackEDR.Sensor.os_environment_display_string`
- `CarbonBlackEDR.Sensor.emet_version`
- `CarbonBlackEDR.Sensor.emet_dump_flags`
- `CarbonBlackEDR.Sensor.clock_delta`
- `CarbonBlackEDR.Sensor.supports_cblr`
- `CarbonBlackEDR.Sensor.sensor_uptime`
- `CarbonBlackEDR.Sensor.last_update`

**Dependencies:**

- Scripts: IsIntegrationAvailable, Set
- Commands: cb-edr-sensors-list, cb-edr-quarantine-device


## Carbon Black Response - Unisolate Endpoint

**Product:** Carbon Black Enterprise Response

This playbook unisolates sensors according to the sensor ID that is provided in the playbook input

**Inputs:**

- `Endpoint_ID`: The sensor id you want to unisolate.

**Dependencies:**

- Integrations: carbonblack-v2
- Scripts: IsIntegrationAvailable
- Commands: cb-sensor-info, cb-list-sensors, cb-unquarantine-device


## Cortex XDR - Unisolate Endpoint

**Product:** Cortex XDR by Palo Alto Networks

This playbook unisolates endpoints according to the endpoint ID that is provided in the playbook input

**Inputs:**

- `Endpoint_ID`: The endpoint ID that you want to be unisolated.
- `Hostname`: The endpoint's hostname that you want to be unisolated.
- `IP`: The endpoint's IP that you want to be unisolated.

**Dependencies:**

- Integrations: CortexXDRIR
- Scripts: IsIntegrationAvailable
- Commands: xdr-endpoint-unisolate, xdr-get-endpoints


## Crowdstrike Falcon - Unisolate Endpoint

**Product:** CrowdStrike Falcon

This playbook unisolates devices according to the device ID that is provided in the playbook input

**Inputs:**

- `Endpoint_id`: The endpoint ID/device ID that you want to unisolate.

**Dependencies:**

- Commands: cs-falcon-lift-host-containment, cs-falcon-search-device


## FireEye HX - Unisolate Endpoint

**Product:** FireEye HX

This playbook unisolates endpoints according to the hostname/endpoint ID that is provided by the playbook input

**Inputs:**

- `Endpoint_id`: The endpoint ID/device ID that you want to unisolate.
- `Hostname`: The hostname that you want to unisolate.

**Dependencies:**

- Commands: fireeye-hx-get-host-information, fireeye-hx-cancel-containment


## Microsoft Defender For Endpoint - Unisolate Endpoint

**Product:** Microsoft Defender for Endpoint

This playbook accepts an endpoint ID, IP, or host name and unisolates it using the Microsoft Defender For Endpoint integration

**Inputs:**

- `Device_id`: The device ID to isolate.For more information about the device, you can use the following commands:!microsoft-atp-get-machine-details!microsoft-atp-get-machines
- `Hostname`: The device host name you want to isolate.
- `Device_IP`: The device IP you want to isolate.

**Outputs:**

- `MicrosoftATP.MachineAction.ID`
- `MicrosoftATP.NonUnisolateList`
- `MicrosoftATP.UnisolateList`
- `MicrosoftATP.IncorrectIDs`
- `MicrosoftATP.IncorrectHostnames`
- `MicrosoftATP.IncorrectIPs`

**Dependencies:**

- Integrations: MicrosoftDefenderAdvancedThreatProtection
- Scripts: SetAndHandleEmpty, isError, IsIntegrationAvailable, Print
- Commands: endpoint, microsoft-atp-unisolate-machine


## Rapid ransomware containment - Illumio

**Product:** Illumio Rapid Ransomware Containment

Isolate one or more workloads based on traffic flows to a given port/protocol

**Inputs:**

- `Port`: Provide Port to be blocked.
- `Protocol`: Protocol of Port.
- `Allow Traffic?`: Do You want to allow traffic on this port? (Yes or No)
- `Update the enforcement mode?`: Do you want to update the enforcement mode?(Yes or No)

**Dependencies:**

- Sub-playbooks: Update enforcement mode - Illumio
- Integrations: IllumioCore
- Scripts: Print
- Commands: illumio-object-provision, illumio-workloads-list, illumio-ip-lists-get, illumio-ruleset-create, illumio-enforcement-boundary-create, illumio-service-binding-create, illumio-virtual-service-create, illumio-rule-create


## Scan and Isolate - XM Cyber

**Product:** XM Cyber

An example of playbook using data from XM Cyber to help decide about scanning and isolating a threat

**Outputs:**

- `Traps.IsolateResult.Status`
- `Nexpose.Scan.Status`
- `Nexpose.Scan.Assets`
- `Nexpose.Scan.Vulnerabilities.Total`
- `XMCyber.Entity.isAsset`
- `XMCyber.Entity.averageComplexityLevel`
- `XMCyber.Entity.criticalAssetsAtRisk`

**Dependencies:**

- Sub-playbooks: Isolate Endpoint - Generic V2, Endpoint Enrichment By Hostname - XM Cyber, Endpoint Enrichment By IP - XM Cyber, Scan Assets - Nexpose


## Unisolate Endpoint - Cybereason

**Product:** Cybereason

This playbook unisolates a machine based on the hostname provided

**Inputs:**

- `Hostname`: The hostname of the endpoint you want to unisolate.

