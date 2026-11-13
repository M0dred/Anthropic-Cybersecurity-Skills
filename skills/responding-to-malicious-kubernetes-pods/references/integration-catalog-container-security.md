# Integration and Automation Catalog - Container Security

Reference entries for integrations, scripts, and playbooks in this domain. Each entry records the product, the commands it exposes, and the inputs it accepts, so the vendor-neutral procedures in this skill can be executed on that product.


## Ansible Kubernetes

**Type:** integration  
**Product:** Ansible Kubernetes  

This integration enables the management of Kubernetes environments using Ansible modules. The Ansible engine is self-contained and pre-configured as part of this pack onto your platform server, all you need to do is provide credentials you are ready to use the feature rich commands. This integration supports API Token, and Username/Password authentication. It is recommended to use API tokens. To create a service account with API token use the following kubectl commands

**Commands:**

- `k8s-k8s`: Manage Kubernetes (K8s) objects Further documentation available at https://docs.ansible.com/ansible/2.9/modules/k8s_module.html


## Google Kubernetes Engine

**Type:** integration  
**Product:** Google Kubernetes Engine  

The Google Kubernetes Engine integration is used for building and managing container based applications in Google Cloud Platform (GCP), powered by the open source Kubernetes technology. Command, argument, and output desctiptions were taken from the Google documentation

**Commands:**

- `gcloud-clusters-list`: Lists all clusters owned by a project in either the specified zone or all zones.
- `gcloud-clusters-describe`: Gets the details of a specific cluster.
- `gcloud-clusters-set-muster-auth`: Enable basic (username/password) auth for the cluster. Enable will create user admin with generated password.
- `gcloud-clusters-set-addons`: Sets the addons for a specific cluster.
- `gcloud-clusters-set-legacy-auth`: Configuration for the legacy Attribute Based Access Control authorization mode.
- `gcloud-clusters-set-master-authorized-network`: Configuration options for the master authorized networks feature. Enabled master authorized networks will disallow all external traffic to access Kubernetes mas
- `gcloud-clusters-set-k8s-stackdriver`: Enable or Disable k8s stackdriver. Important - To use this functinality the user should enable manually logging to "monitoring.googleapis.com/kubernetes" manula
- `gcloud-clusters-set-binary-auth`: Enable or Disable binary auth.
- `gcloud-clusters-set-intra-node-visibility`: Enable or Disable for intra node visibility in cluster.
- `gcloud-node-pool-list`: Lists the node pools for a cluster.
- `gcloud-node-pool-describe`: Retrieves the requested node pool.
- `gcloud-node-pool-set-management`: Sets the NodeManagement options for a node pool.
- `gcloud-operations-list`: List operations in project-zone.
- `gcloud-operations-describe`: Retrieve operation information by name.
- `gcloud-operations-cancel`: Cancel operation by operation name.

