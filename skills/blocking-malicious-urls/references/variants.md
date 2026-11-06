# Vendor Variants - Blocking Malicious Urls

Vendor-specific implementations of this procedure. Each section records the source product, its inputs, and the commands or APIs it uses, so the vendor-neutral workflow can be executed on that product.


## Checkpoint - Block URL

**Product:** Check Point Firewall

This playbook blocks URLs using Check Point Firewall through Custom URL Categories. The playbook checks whether the input URL category already exists, and if the URLs are a part of this category. If not, it creates the category, blocks the URLs, and publishes the configuration

**Inputs:**

- `install_policy`: Whether the playbook should continue install policy process for Check Point Firewall.
- `URL`: An array of URLs to block.Example: example.com,example.org
- `policy_package`: The name of the policy package to be installed.
- `URL_application_site_category`: URL category object name. The category to add URL to.
- `checkpoint_error_handling`: If one of the actions for the Block IP playbook fails due to issues on the Check Point Firewall, this input determines whether the playbook continues or stops for manual review. If
- `block_URL_error_handling`: If one of the actions for Block URL playbook fails due to issues on the Check Point Firewall, this input determines whether the playbook continues or stops for manual review. If th
- `application_site_name`: Define the Application Site Name. Default: Bad_URLs.

**Dependencies:**

- Sub-playbooks: Checkpoint - Publish&Install configuration
- Integrations: CheckPointFirewallV2
- Scripts: Print
- Commands: checkpoint-application-site-category-get, checkpoint-application-site-update, checkpoint-logout, checkpoint-login-and-get-session-id, checkpoint-application-site-category-add, checkpoint-application-site-add


## PAN-OS - Block URL - Custom URL Category

**Product:** PAN-OS by Palo Alto Networks

This playbook blocks URLs using Palo Alto Networks Panorama or Firewall through Custom URL Categories. The playbook checks whether the input URL category already exists, and if the URLs are a part of this category. Otherwise, it will create the category, block the URLs, and commit the configuration

**Inputs:**

- `URL`: URL to block
- `CustomURLCategory`: Custom URL Category name
- `LogForwarding`: Panorama log forwarding object name
- `AutoCommit`: This input establishes whether to commit the configuration automatically.Yes - Commit automatically.No - Commit manually.
- `type`: Custom URL category type. Insert "URL List"/ "Category Match".
- `device-group`: Device group for the Custom URL Category (Panorama instances).
- `categories`: The list of categories. Relevant from PAN-OS v9.x.
- `pre-post`: Specify pre-rulebase or post-rulebase. (Panorama instances).

**Dependencies:**

- Sub-playbooks: PAN-OS Commit Configuration
- Integrations: Panorama
- Commands: pan-os-create-custom-url-category, pan-os-edit-custom-url-category, pan-os-get-custom-url-category, pan-os-custom-block-rule


## Prisma SASE - Block URL

**Product:** Palo Alto Networks - Strata Cloud Manager

The playbook will handle the operation of blocking a URL within the organization. If a category is provided, the URL will be added to the list. If not, a new URL category will be created, and a new security rule that blocks that category

**Inputs:**

- `URL`: List of URLs that are needed to be blocked.
- `CategoryName`: The name of the predefined custom URL category.
- `Folder`: Specify the scope for a newly created security rule to be applied.Remember, this input will only be used when there is no input to the CategoryName.Default: Shared
- `TSGID`: Tenant services group ID. If not provided, the tsg_id integration parameter will be used as the default.
- `AutoCommit`: Possible Values:True -&gt; Will Commit and Push ConfigurationFalse -&gt; Manual Push will be required.Else --&gt; Will ignore the push section and continue the playbook.

**Outputs:**

- `PrismaSase`
- `PrismaSase.SecurityRule`
- `PrismaSase.SecurityRule.action`
- `PrismaSase.SecurityRule.application`
- `PrismaSase.SecurityRule.category`
- `PrismaSase.SecurityRule.description`
- `PrismaSase.SecurityRule.destination`
- `PrismaSase.SecurityRule.folder`
- `PrismaSase.SecurityRule.from`
- `PrismaSase.SecurityRule.id`

**Dependencies:**

- Sub-playbooks: Prisma SASE - Create or Edit Security Policy Rule
- Integrations: PrismaSASE
- Commands: prisma-sase-custom-url-category-create, prisma-sase-custom-url-category-list, prisma-sase-candidate-config-push, prisma-sase-custom-url-category-update

## Checkpoint - Block URL

**Product:** Check Point Firewall

This playbook blocks URLs using Check Point Firewall through Custom URL Categories. The playbook checks whether the input URL category already exists, and if the URLs are a part of this category. If not, it creates the category, blocks the URLs, and publishes the configuration

**Inputs:**

- `install_policy`: Whether the playbook should continue install policy process for Check Point Firewall.
- `URL`: An array of URLs to block.Example: example.com,example.org
- `policy_package`: The name of the policy package to be installed.
- `URL_application_site_category`: URL category object name. The category to add URL to.
- `checkpoint_error_handling`: If one of the actions for the Block IP playbook fails due to issues on the Check Point Firewall, this input determines whether the playbook continues or stops for manual review. If
- `block_URL_error_handling`: If one of the actions for Block URL playbook fails due to issues on the Check Point Firewall, this input determines whether the playbook continues or stops for manual review. If th
- `application_site_name`: Define the Application Site Name. Default: Bad_URLs.

**Dependencies:**

- Sub-playbooks: Checkpoint - Publish&Install configuration
- Integrations: CheckPointFirewallV2
- Scripts: Print
- Commands: checkpoint-application-site-category-get, checkpoint-application-site-update, checkpoint-logout, checkpoint-login-and-get-session-id, checkpoint-application-site-category-add, checkpoint-application-site-add


## PAN-OS - Block URL - Custom URL Category

**Product:** PAN-OS by Palo Alto Networks

This playbook blocks URLs using Palo Alto Networks Panorama or Firewall through Custom URL Categories. The playbook checks whether the input URL category already exists, and if the URLs are a part of this category. Otherwise, it will create the category, block the URLs, and commit the configuration

**Inputs:**

- `URL`: URL to block
- `CustomURLCategory`: Custom URL Category name
- `LogForwarding`: Panorama log forwarding object name
- `AutoCommit`: This input establishes whether to commit the configuration automatically.Yes - Commit automatically.No - Commit manually.
- `type`: Custom URL category type. Insert "URL List"/ "Category Match".
- `device-group`: Device group for the Custom URL Category (Panorama instances).
- `categories`: The list of categories. Relevant from PAN-OS v9.x.
- `pre-post`: Specify pre-rulebase or post-rulebase. (Panorama instances).

**Dependencies:**

- Sub-playbooks: PAN-OS Commit Configuration
- Integrations: Panorama
- Commands: pan-os-create-custom-url-category, pan-os-edit-custom-url-category, pan-os-get-custom-url-category, pan-os-custom-block-rule


## Prisma SASE - Block URL

**Product:** Palo Alto Networks - Strata Cloud Manager

The playbook will handle the operation of blocking a URL within the organization. If a category is provided, the URL will be added to the list. If not, a new URL category will be created, and a new security rule that blocks that category

**Inputs:**

- `URL`: List of URLs that are needed to be blocked.
- `CategoryName`: The name of the predefined custom URL category.
- `Folder`: Specify the scope for a newly created security rule to be applied.Remember, this input will only be used when there is no input to the CategoryName.Default: Shared
- `TSGID`: Tenant services group ID. If not provided, the tsg_id integration parameter will be used as the default.
- `AutoCommit`: Possible Values:True -&gt; Will Commit and Push ConfigurationFalse -&gt; Manual Push will be required.Else --&gt; Will ignore the push section and continue the playbook.

**Outputs:**

- `PrismaSase`
- `PrismaSase.SecurityRule`
- `PrismaSase.SecurityRule.action`
- `PrismaSase.SecurityRule.application`
- `PrismaSase.SecurityRule.category`
- `PrismaSase.SecurityRule.description`
- `PrismaSase.SecurityRule.destination`
- `PrismaSase.SecurityRule.folder`
- `PrismaSase.SecurityRule.from`
- `PrismaSase.SecurityRule.id`

**Dependencies:**

- Sub-playbooks: Prisma SASE - Create or Edit Security Policy Rule
- Integrations: PrismaSASE
- Commands: prisma-sase-custom-url-category-create, prisma-sase-custom-url-category-list, prisma-sase-candidate-config-push, prisma-sase-custom-url-category-update

## Checkpoint - Block URL

**Product:** Check Point Firewall

This playbook blocks URLs using Check Point Firewall through Custom URL Categories. The playbook checks whether the input URL category already exists, and if the URLs are a part of this category. If not, it creates the category, blocks the URLs, and publishes the configuration

**Inputs:**

- `install_policy`: Whether the playbook should continue install policy process for Check Point Firewall.
- `URL`: An array of URLs to block.Example: example.com,example.org
- `policy_package`: The name of the policy package to be installed.
- `URL_application_site_category`: URL category object name. The category to add URL to.
- `checkpoint_error_handling`: If one of the actions for the Block IP playbook fails due to issues on the Check Point Firewall, this input determines whether the playbook continues or stops for manual review. If
- `block_URL_error_handling`: If one of the actions for Block URL playbook fails due to issues on the Check Point Firewall, this input determines whether the playbook continues or stops for manual review. If th
- `application_site_name`: Define the Application Site Name. Default: Bad_URLs.

**Dependencies:**

- Sub-playbooks: Checkpoint - Publish&Install configuration
- Integrations: CheckPointFirewallV2
- Scripts: Print
- Commands: checkpoint-application-site-category-get, checkpoint-application-site-update, checkpoint-logout, checkpoint-login-and-get-session-id, checkpoint-application-site-category-add, checkpoint-application-site-add


## PAN-OS - Block URL - Custom URL Category

**Product:** PAN-OS by Palo Alto Networks

This playbook blocks URLs using Palo Alto Networks Panorama or Firewall through Custom URL Categories. The playbook checks whether the input URL category already exists, and if the URLs are a part of this category. Otherwise, it will create the category, block the URLs, and commit the configuration

**Inputs:**

- `URL`: URL to block
- `CustomURLCategory`: Custom URL Category name
- `LogForwarding`: Panorama log forwarding object name
- `AutoCommit`: This input establishes whether to commit the configuration automatically.Yes - Commit automatically.No - Commit manually.
- `type`: Custom URL category type. Insert "URL List"/ "Category Match".
- `device-group`: Device group for the Custom URL Category (Panorama instances).
- `categories`: The list of categories. Relevant from PAN-OS v9.x.
- `pre-post`: Specify pre-rulebase or post-rulebase. (Panorama instances).

**Dependencies:**

- Sub-playbooks: PAN-OS Commit Configuration
- Integrations: Panorama
- Commands: pan-os-create-custom-url-category, pan-os-edit-custom-url-category, pan-os-get-custom-url-category, pan-os-custom-block-rule


## Prisma SASE - Block URL

**Product:** Palo Alto Networks - Strata Cloud Manager

The playbook will handle the operation of blocking a URL within the organization. If a category is provided, the URL will be added to the list. If not, a new URL category will be created, and a new security rule that blocks that category

**Inputs:**

- `URL`: List of URLs that are needed to be blocked.
- `CategoryName`: The name of the predefined custom URL category.
- `Folder`: Specify the scope for a newly created security rule to be applied.Remember, this input will only be used when there is no input to the CategoryName.Default: Shared
- `TSGID`: Tenant services group ID. If not provided, the tsg_id integration parameter will be used as the default.
- `AutoCommit`: Possible Values:True -&gt; Will Commit and Push ConfigurationFalse -&gt; Manual Push will be required.Else --&gt; Will ignore the push section and continue the playbook.

**Outputs:**

- `PrismaSase`
- `PrismaSase.SecurityRule`
- `PrismaSase.SecurityRule.action`
- `PrismaSase.SecurityRule.application`
- `PrismaSase.SecurityRule.category`
- `PrismaSase.SecurityRule.description`
- `PrismaSase.SecurityRule.destination`
- `PrismaSase.SecurityRule.folder`
- `PrismaSase.SecurityRule.from`
- `PrismaSase.SecurityRule.id`

**Dependencies:**

- Sub-playbooks: Prisma SASE - Create or Edit Security Policy Rule
- Integrations: PrismaSASE
- Commands: prisma-sase-custom-url-category-create, prisma-sase-custom-url-category-list, prisma-sase-candidate-config-push, prisma-sase-custom-url-category-update

## Checkpoint - Block URL

**Product:** Check Point Firewall

This playbook blocks URLs using Check Point Firewall through Custom URL Categories. The playbook checks whether the input URL category already exists, and if the URLs are a part of this category. If not, it creates the category, blocks the URLs, and publishes the configuration

**Inputs:**

- `install_policy`: Whether the playbook should continue install policy process for Check Point Firewall.
- `URL`: An array of URLs to block.Example: example.com,example.org
- `policy_package`: The name of the policy package to be installed.
- `URL_application_site_category`: URL category object name. The category to add URL to.
- `checkpoint_error_handling`: If one of the actions for the Block IP playbook fails due to issues on the Check Point Firewall, this input determines whether the playbook continues or stops for manual review. If
- `block_URL_error_handling`: If one of the actions for Block URL playbook fails due to issues on the Check Point Firewall, this input determines whether the playbook continues or stops for manual review. If th
- `application_site_name`: Define the Application Site Name. Default: Bad_URLs.

**Dependencies:**

- Sub-playbooks: Checkpoint - Publish&Install configuration
- Integrations: CheckPointFirewallV2
- Scripts: Print
- Commands: checkpoint-application-site-category-get, checkpoint-application-site-update, checkpoint-logout, checkpoint-login-and-get-session-id, checkpoint-application-site-category-add, checkpoint-application-site-add


## PAN-OS - Block URL - Custom URL Category

**Product:** PAN-OS by Palo Alto Networks

This playbook blocks URLs using Palo Alto Networks Panorama or Firewall through Custom URL Categories. The playbook checks whether the input URL category already exists, and if the URLs are a part of this category. Otherwise, it will create the category, block the URLs, and commit the configuration

**Inputs:**

- `URL`: URL to block
- `CustomURLCategory`: Custom URL Category name
- `LogForwarding`: Panorama log forwarding object name
- `AutoCommit`: This input establishes whether to commit the configuration automatically.Yes - Commit automatically.No - Commit manually.
- `type`: Custom URL category type. Insert "URL List"/ "Category Match".
- `device-group`: Device group for the Custom URL Category (Panorama instances).
- `categories`: The list of categories. Relevant from PAN-OS v9.x.
- `pre-post`: Specify pre-rulebase or post-rulebase. (Panorama instances).

**Dependencies:**

- Sub-playbooks: PAN-OS Commit Configuration
- Integrations: Panorama
- Commands: pan-os-create-custom-url-category, pan-os-edit-custom-url-category, pan-os-get-custom-url-category, pan-os-custom-block-rule


## Prisma SASE - Block URL

**Product:** Palo Alto Networks - Strata Cloud Manager

The playbook will handle the operation of blocking a URL within the organization. If a category is provided, the URL will be added to the list. If not, a new URL category will be created, and a new security rule that blocks that category

**Inputs:**

- `URL`: List of URLs that are needed to be blocked.
- `CategoryName`: The name of the predefined custom URL category.
- `Folder`: Specify the scope for a newly created security rule to be applied.Remember, this input will only be used when there is no input to the CategoryName.Default: Shared
- `TSGID`: Tenant services group ID. If not provided, the tsg_id integration parameter will be used as the default.
- `AutoCommit`: Possible Values:True -&gt; Will Commit and Push ConfigurationFalse -&gt; Manual Push will be required.Else --&gt; Will ignore the push section and continue the playbook.

**Outputs:**

- `PrismaSase`
- `PrismaSase.SecurityRule`
- `PrismaSase.SecurityRule.action`
- `PrismaSase.SecurityRule.application`
- `PrismaSase.SecurityRule.category`
- `PrismaSase.SecurityRule.description`
- `PrismaSase.SecurityRule.destination`
- `PrismaSase.SecurityRule.folder`
- `PrismaSase.SecurityRule.from`
- `PrismaSase.SecurityRule.id`

**Dependencies:**

- Sub-playbooks: Prisma SASE - Create or Edit Security Policy Rule
- Integrations: PrismaSASE
- Commands: prisma-sase-custom-url-category-create, prisma-sase-custom-url-category-list, prisma-sase-candidate-config-push, prisma-sase-custom-url-category-update

