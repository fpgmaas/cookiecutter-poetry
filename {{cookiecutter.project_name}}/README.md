# {{cookiecutter.project_name}}

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}/merge-to-main)
![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.project_name}})
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1)](https://pycqa.github.io/isort/)
[![Dependency management: poetry](https://img.shields.io/badge/tool-poetry-orange)](https://pycqa.github.io/isort/)
[![License](https://img.shields.io/github/license/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}})](https://github.com/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}/blob/main/LICENSE)

{{cookiecutter.project_description}}


## Releasing a new version

- Create a API Token on [Pypi](https://pypi.org/)
- Add the API Token to your projects secrets with the name `PYPI_TOKEN`, by visiting [this page](https://github.com/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}/settings/secrets/actions/new)).
- Create a [new release](https://github.com/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}/releases/new) on Github. Create a new tag in the form `*.*.*`.