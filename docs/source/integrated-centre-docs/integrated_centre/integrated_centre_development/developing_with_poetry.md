---
orphan: true
---
# Developing with Poetry

Going forward, we will endeavour to build our libraries and services using current best practices including:

- Following [Semantic Versioning](https://semver.org/) principles:
  - Backward incompatible changes bump the major version number
    - When removing classes, functions, or required parameters
    - When renaming topics, or changing payloads in `AsyncApi`s
  - Feature additions bump the minor version number
    - When adding classes, functions, or parameters with defaults
  - Bug fixes and patches bump the patch number
    - Not changing the public interface, but improving error handling
    - Fixing non-functional code
- Setting version constraints between services and libraries:
  - Recording the minimum version known to work for each service, with upper bounds if known
  - Recording the tested versions of dependencies, and capturing for later debugging and analysis

Poetry is a tool we have selected to help us achieve these goals.


[lock-advice]: https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control

## Setting up credentials

Latin 

## Setting up sources

Latin

## Poetry commands

Some useful commands for managing a poetry project

```bash
# Add new dependencies
poetry add "new-dependency[extra]"
# Update dependencies to their latest compatible version
poetry update
# Bump project version number
poetry version minor
# Configure your poetry install to put the virtualenv inside the project folder
poetry config virtualenvs.in-project true
```

## Getting setup with an existing Poetry project

Latin
