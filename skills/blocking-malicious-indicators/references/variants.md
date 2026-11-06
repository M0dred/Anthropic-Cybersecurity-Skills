# Vendor Variants - Blocking Malicious Indicators

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## ACTI Block Indicators from an Incident

**Product:** Accenture CTI v2

**Dependencies:**

- Sub-playbooks: ACTI Indicator Enrichment, ACTI Block Indicators with severity greater than equal to 5
- Scripts: DeleteContext
- Commands: extractIndicators

