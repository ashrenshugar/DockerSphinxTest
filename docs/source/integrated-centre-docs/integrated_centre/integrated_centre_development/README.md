---
orphan: true
---
# Information for Integrated Centre Developers

This section contains information that could be useful for development of capabilities in the Integrated Centre.
Developers may be creating new services, or otherwise enhancing the Integrated Centre. Additional supplemental documents
to assist developers are also found within this folder integrated_centre_development:
<!--[integrated_centre_development](/integrated_centre/integrated_centre_development):_-->
- [Ansible Overview](ansible_overview.md)
- [Using Docker with Refactory](using_docker_with_refactory.md)
- [git ssh Instructions](git_ssh_instructions.md)
- [GitLab CI Templates](gitlab_ci_templates.md)
- [Developing with Poetry](developing_with_poetry.md)
- [Tooling Setup](development_environment_setup.md):

Other useful information:
- [Knowledge Base Articles](https://refactory.australiacentral.cloudapp.azure.com/integrated-centre/integrated-centre-docs/-/wikis/Integrated-Centre-Knowledge-Base):
A collection of useful information for doing development in the Integrated Centre and using the current technologies.
- [Cookiecutter Templates](https://refactory.australiacentral.cloudapp.azure.com/integrated-centre/cookiecutters):
Contains various templates for creation of common Python services in the Integrated Centre.

## Integrated Centre Tools

A set of tools has been created with the goal of simplifying and standardising static analysis (checks) and docker
operations. In addition useful utilities have been packaged together.

More information can be found in the
[Integrated Centre Tools - README](https://refactory.australiacentral.cloudapp.azure.com/integrated-centre/integrated-centre-tools/-/blob/master/README.md).

## Developing with Poetry

Going forward, we will endeavour to build our libraries and services using current best practices and Poetry is a
the tool we have selected to help us achieve these goals.

[Instructions on using Poetry](developing_with_poetry.md)

## GitLab CI Templates

When starting a new project (repository), adding CI (Continuous Integration) can be tricky. To help with this process,
job templates and documentation for `.gitlab-ci.yml` files can be found in [`gitlab_ci_templates`](gitlab_ci_templates.md)<!--[ci-templates]-->.

<!--[ci-templates]: integrated_centre/integrated_centre_development/gitlab_ci_templates.md-->

## Project Creation Ansible Role

To simplify creating a new GitLab project, the [`ansible-role-create-project`][ansible-role-create-project]
can be used. This is able to create a project in GitLab / Refactory while using another project as a parameterised
template.

The repository provides instructions how to use the Ansible role and how to set variables that customise the application
of the template.

In the future, this role may be used to support simple project creation through a Web based UI.

[ansible-role-create-project]: https://refactory.australiacentral.cloudapp.azure.com/roles/ansible-role-create-project
