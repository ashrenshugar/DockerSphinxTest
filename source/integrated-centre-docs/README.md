<!-- Code commented out below as it was interfering with creating a pdf-->
# Intergrated Centre Docs

[[_TOC_]]

[![Quality Gate Status](https://refactory.australiacentral.cloudapp.azure.com/sonar/api/project_badges/measure?project=integrated-centre-integrated-centre-docs&metric=alert_status&token=e53ee9330e5b995d44771e2f007e9070b92224a7)](https://refactory.australiacentral.cloudapp.azure.com/sonar/dashboard?id=integrated-centre-integrated-centre-docs)
[![Code Smells](https://refactory.australiacentral.cloudapp.azure.com/sonar/api/project_badges/measure?project=integrated-centre-integrated-centre-docs&metric=code_smells&token=e53ee9330e5b995d44771e2f007e9070b92224a7)](https://refactory.australiacentral.cloudapp.azure.com/sonar/dashboard?id=integrated-centre-integrated-centre-docs)
[![Coverage](https://refactory.australiacentral.cloudapp.azure.com/sonar/api/project_badges/measure?project=integrated-centre-integrated-centre-docs&metric=coverage&token=e53ee9330e5b995d44771e2f007e9070b92224a7)](https://refactory.australiacentral.cloudapp.azure.com/sonar/dashboard?id=integrated-centre-integrated-centre-docs)
[![Reliability Rating](https://refactory.australiacentral.cloudapp.azure.com/sonar/api/project_badges/measure?project=integrated-centre-integrated-centre-docs&metric=reliability_rating&token=e53ee9330e5b995d44771e2f007e9070b92224a7)](https://refactory.australiacentral.cloudapp.azure.com/sonar/dashboard?id=integrated-centre-integrated-centre-docs)
[![Security Rating](https://refactory.australiacentral.cloudapp.azure.com/sonar/api/project_badges/measure?project=integrated-centre-integrated-centre-docs&metric=security_rating&token=e53ee9330e5b995d44771e2f007e9070b92224a7)](https://refactory.australiacentral.cloudapp.azure.com/sonar/dashboard?id=integrated-centre-integrated-centre-docs)
[![Technical Debt](https://refactory.australiacentral.cloudapp.azure.com/sonar/api/project_badges/measure?project=integrated-centre-integrated-centre-docs&metric=sqale_index&token=e53ee9330e5b995d44771e2f007e9070b92224a7)](https://refactory.australiacentral.cloudapp.azure.com/sonar/dashboard?id=integrated-centre-integrated-centre-docs)
[![Vulnerabilities](https://refactory.australiacentral.cloudapp.azure.com/sonar/api/project_badges/measure?project=integrated-centre-integrated-centre-docs&metric=vulnerabilities&token=e53ee9330e5b995d44771e2f007e9070b92224a7)](https://refactory.australiacentral.cloudapp.azure.com/sonar/dashboard?id=integrated-centre-integrated-centre-docs)

## License, Classification and Distribution Statement

<!--- - [License](LICENSE.md) --> 
- License
- [Classification](CLASSIFICATION.md)
- Distribution Statement
  <!--- [Distribution Statement](DISTRIBUTION_STATEMENT.md) -->

## Introduction

This repository contains documentation about the Integrated Centre that is to be versioned controlled and does not have
a natural home anywhere else. It does not seek to document individual services or components but rather documents wider
Integrated Centre themes.

## Documentation
<!--[Integrated Centre](integrated_centre)-->
The documents contained within the <i>Integrated Centre<i> directory constitute the primary
documentation set of the Integrated Centre. They have been grouped in to their document types, as detailed below.

### Integrated Centre System

A set of documents that describe what the Integrated Centre is and the concepts and systems that exist within
the environment such as Reference Deployments, Refactory and Rogue Shadow.

[Integrated Centre Overview](integrated_centre/integrated_centre_system/integrated_centre_overview.md)

[Integrated Centre Technology Strategy](integrated_centre/integrated_centre_system/integrated_centre_technology_strategy.md)

[Integrated Centre Standards and Technologies](integrated_centre/integrated_centre_system/integrated_centre_standards_and_technologies.md)

Current Reference Deployments
<!--[Current Reference Deployments](integrated_centre/integrated_centre_system/integrated_centre_overview.md#rogue-shadow-reference-deployments)-->

[Rogue Shadow Technical Description](integrated_centre/integrated_centre_system/rogue_shadow/rogue_shadow_technical_description.md)

[Rogue Shadow Unit Cells Design](integrated_centre/integrated_centre_system/rogue_shadow/rogue_shadow_unit_cells_detailed_design.md)

[Rogue Shadow Digital Fabric Design](integrated_centre/integrated_centre_system/rogue_shadow/rogue_shadow_digital_fabric_detailed_design.md)

### Integrated Centre Catalogue

The services, roles and deployments in the Integrated Centre are described here:
[Integrated Centre Catalogue](integrated_centre/integrated_centre_catalogue/integrated-centre-catalogue.md)

This catalogue is a place to discover Integrated Centre capabilities such as services and tools that may be useful in
achieving a research outcome.

Details of the subscriptions and publications made by services can be found at [Service Async APIs](integrated_centre/integrated_centre_catalogue/service_async_apis.md).
This includes information about channel names and payloads.

### Integrated Centre Development

A set of documents with information and guides to assist developers with contributing to the Integrated Centre.

- [Developer Information](integrated_centre/integrated_centre_development/README.md)
- [Ansible Overview](integrated_centre/integrated_centre_development/ansible_overview.md)
- [Using Docker with Refactory](integrated_centre/integrated_centre_development/using_docker_with_refactory.md)
- [git ssh Instructions](integrated_centre/integrated_centre_development/git_ssh_instructions.md)
- [GitLab CI Templates](integrated_centre/integrated_centre_development/gitlab_ci_templates.md)
- [Developing with Poetry](integrated_centre/integrated_centre_development/developing_with_poetry.md)
- [Development Environment Setup](integrated_centre/integrated_centre_development/development_environment_setup.md)

### Integrated Centre Hardware

A set of documents to assist users with the obtaining, deploying, or configuring the various hardware that may be used
within Integrated Centre deployments.

- [Experimentation NUC](integrated_centre/integrated_centre_hardware/experimentation_nuc/README.md)
- [Jetson AGX Xavier Setup](integrated_centre/integrated_centre_hardware/jetson_agx_xavier_setup.md)
- [Windows BitLocker Instructions](integrated_centre/integrated_centre_hardware/windows_bitlocker_instructions.md)
- [Windows VirtualBox Instructions](integrated_centre/integrated_centre_hardware/windows_virtualbox_instructions.md)

## Integrated Centre Docs Repository Developers

Information for developers of this repository can be found in the [Developer Readme](developer_readme.md).
