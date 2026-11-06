# Vendor Variants - Enriching External Ip Addresses

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Vega Incident - External IP Enrichment - Generic

**Product:** Vega

Enriches incoming IP addresses using the 'IP Enrichment - External - Generic v2' sub-playbook and automatically posts the retrieved endpoint details back to the Vega incident as a comment

**Inputs:**

- `IP_Address`: The IP address(es) to enrich.

**Dependencies:**

- Sub-playbooks: IP Enrichment - External - Generic v2
- Integrations: Vega
- Scripts: IsIntegrationAvailable, Print
- Commands: vega-update-incident

