# cookiecutter-poetry-example

[![Release](https://img.shields.io/github/v/release/fpgmaas/cookiecutter-poetry-example)](https://img.shields.io/github/v/release/fpgmaas/cookiecutter-poetry-example)
[![Build status](https://img.shields.io/github/workflow/status/fpgmaas/cookiecutter-poetry-example/merge-to-main)](https://img.shields.io/github/workflow/status/fpgmaas/cookiecutter-poetry-example/merge-to-main)
[![Commit activity](https://img.shields.io/github/commit-activity/m/fpgmaas/cookiecutter-poetry-example)](https://img.shields.io/github/commit-activity/m/fpgmaas/cookiecutter-poetry-example)
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://fpgmaas.github.io/cookiecutter-poetry-example/)
[![Code style with black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports with isort](https://img.shields.io/badge/%20imports-isort-%231674b1)](https://pycqa.github.io/isort/)
[![License](https://img.shields.io/github/license/fpgmaas/cookiecutter-poetry-example)](https://img.shields.io/github/license/fpgmaas/cookiecutter-poetry-example)

{{cookiecutter.project_description}}

- **Github repository**: <https://github.com/fpgmaas/cookiecutter-poetry-example/>
- **Documentation** <https://fpgmaas.github.io/cookiecutter-poetry-example/>

## Releasing a new version

{% if cookiecutter.publish_to == "pypi" -%}
- Create an API Token on [Pypi](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting 
[this page](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/settings/secrets/actions/new).
- Create a [new release](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/releases/new) on Github. 
Create a new tag in the form ``*.*.*``.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/releasing.html).
{%- elif cookiecutter.publish_to == "artifactory" -%}
- Add the `ARTIFACTORY_URL`, `ARTIFACTORY_USERNAME`, and `ARTIFACTORY_PASSWORD` to your projects secrets by visiting [this page](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/settings/secrets/actions/new).
- Create a [new release](https://github.com/{{cookiecutter.author_github_handle}}/{{cookiecutter.project_name}}/releases/new) on Github. Create a new tag in the form ``*.*.*``.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/releasing.html).
{%- endif %}

---

Repository initiated with [fpgmaas/cookiecutter-poetry](https://github.com/fpgmaas/cookiecutter-poetry).