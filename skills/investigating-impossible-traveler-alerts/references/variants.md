# Vendor Variants - Investigating Impossible Traveler Alerts

Vendor-specific implementations, feeds, and collectors for this procedure.


## Impossible Traveler - Enrichment

**Product:** Core

**Kind:** playbook

This playbook get as an input all of the involved IP addresses and identities from the Impossible Traveler playbook alert, and enriches them based on the following

**Inputs:**

- `sourceip`: The source IP to iterate over.
- `username`: The username to iterate over.
- `domain`: The organization domain.

**Dependencies:**

- Sub-playbooks: Account Enrichment - Generic v2.1
- Integrations: CortexCoreIR, CoreIOCs
- Scripts: http, Set, DeleteContext, ParseJSON
- Commands: ip

## Impossible Traveler

**Product:** Impossible Traveler

**Kind:** playbook

This playbook investigates an event whereby a user has multiple application login attempts from various locations in a short time period (impossible traveler). The playbook gathers user, timestamp and IP information associated with the multiple application login attempts. The playbook then measures the time difference between the multiple login attempts and computes the distance between the two locations to verify whether it is possible the user could traverse the distance in the amount of time determined. Also, it takes steps to remediate the incident by blocking the offending IPs and disabling the user account, if chosen to do so

**Inputs:**

- `MaxMilesPerHourAllowed`: The maximum miles per hour that is still considered reasonable. If the geographical distance and difference in time between logins is greater than this value, the user will be cons
- `WhitelistedIPs`: CSV of IP addresses that are allowed to be used across long distances.
- `AutomaticallyBlockIPs`: Whether to automatically block the source IPs that the login originated from. Can be False or True.
- `DefaultMapLink`: The default link from which to create a travel map. The "SOURCE" and "DESTINATION" words are replaced with the previous coordinates and current coordinates of the traveler, respect
- `AutomaticallyDisableUser`: Whether to automatically disable the impossible traveler account using Active Directory.
- `ContactUserManager`: Whether to ask the user manager for the legitimacy of the login events, in case of an alleged impossible traveler.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3, IP Enrichment - Generic v2, Active Directory - Get User Manager Details
- Scripts: Set, EmailAskUser, CalculateTimeDifference, CalculateGeoDistance
- Commands: rasterize, ip, setIncident, ad-get-user, ad-disable-account, closeInvestigation

## Impossible Traveler - Enrichment

**Product:** Core

**Kind:** playbook

This playbook get as an input all of the involved IP addresses and identities from the Impossible Traveler playbook alert, and enriches them based on the following

**Inputs:**

- `sourceip`: The source IP to iterate over.
- `username`: The username to iterate over.
- `domain`: The organization domain.

**Dependencies:**

- Sub-playbooks: Account Enrichment - Generic v2.1
- Integrations: CortexCoreIR, CoreIOCs
- Scripts: http, Set, DeleteContext, ParseJSON
- Commands: ip

## Impossible Traveler

**Product:** Impossible Traveler

**Kind:** playbook

This playbook investigates an event whereby a user has multiple application login attempts from various locations in a short time period (impossible traveler). The playbook gathers user, timestamp and IP information associated with the multiple application login attempts. The playbook then measures the time difference between the multiple login attempts and computes the distance between the two locations to verify whether it is possible the user could traverse the distance in the amount of time determined. Also, it takes steps to remediate the incident by blocking the offending IPs and disabling the user account, if chosen to do so

**Inputs:**

- `MaxMilesPerHourAllowed`: The maximum miles per hour that is still considered reasonable. If the geographical distance and difference in time between logins is greater than this value, the user will be cons
- `WhitelistedIPs`: CSV of IP addresses that are allowed to be used across long distances.
- `AutomaticallyBlockIPs`: Whether to automatically block the source IPs that the login originated from. Can be False or True.
- `DefaultMapLink`: The default link from which to create a travel map. The "SOURCE" and "DESTINATION" words are replaced with the previous coordinates and current coordinates of the traveler, respect
- `AutomaticallyDisableUser`: Whether to automatically disable the impossible traveler account using Active Directory.
- `ContactUserManager`: Whether to ask the user manager for the legitimacy of the login events, in case of an alleged impossible traveler.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3, IP Enrichment - Generic v2, Active Directory - Get User Manager Details
- Scripts: Set, EmailAskUser, CalculateTimeDifference, CalculateGeoDistance
- Commands: rasterize, ip, setIncident, ad-get-user, ad-disable-account, closeInvestigation

## Impossible Traveler - Enrichment

**Product:** Core

**Kind:** playbook

This playbook get as an input all of the involved IP addresses and identities from the Impossible Traveler playbook alert, and enriches them based on the following

**Inputs:**

- `sourceip`: The source IP to iterate over.
- `username`: The username to iterate over.
- `domain`: The organization domain.

**Dependencies:**

- Sub-playbooks: Account Enrichment - Generic v2.1
- Integrations: CortexCoreIR, CoreIOCs
- Scripts: http, Set, DeleteContext, ParseJSON
- Commands: ip

## Impossible Traveler

**Product:** Impossible Traveler

**Kind:** playbook

This playbook investigates an event whereby a user has multiple application login attempts from various locations in a short time period (impossible traveler). The playbook gathers user, timestamp and IP information associated with the multiple application login attempts. The playbook then measures the time difference between the multiple login attempts and computes the distance between the two locations to verify whether it is possible the user could traverse the distance in the amount of time determined. Also, it takes steps to remediate the incident by blocking the offending IPs and disabling the user account, if chosen to do so

**Inputs:**

- `MaxMilesPerHourAllowed`: The maximum miles per hour that is still considered reasonable. If the geographical distance and difference in time between logins is greater than this value, the user will be cons
- `WhitelistedIPs`: CSV of IP addresses that are allowed to be used across long distances.
- `AutomaticallyBlockIPs`: Whether to automatically block the source IPs that the login originated from. Can be False or True.
- `DefaultMapLink`: The default link from which to create a travel map. The "SOURCE" and "DESTINATION" words are replaced with the previous coordinates and current coordinates of the traveler, respect
- `AutomaticallyDisableUser`: Whether to automatically disable the impossible traveler account using Active Directory.
- `ContactUserManager`: Whether to ask the user manager for the legitimacy of the login events, in case of an alleged impossible traveler.
- `InternalRange`: A list of internal IP ranges to check IP addresses against. The comma-separated list should be provided in CIDR notation. For example, a list of ranges would be: "172.16.0.0/12,10.

**Dependencies:**

- Sub-playbooks: Block IP - Generic v3, IP Enrichment - Generic v2, Active Directory - Get User Manager Details
- Scripts: Set, EmailAskUser, CalculateTimeDifference, CalculateGeoDistance
- Commands: rasterize, ip, setIncident, ad-get-user, ad-disable-account, closeInvestigation

