==================================
{{cookiecutter.project_name}}
==================================

.. image:: https://img.shields.io/github/v/release/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}
	:target: https://img.shields.io/github/v/release/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}
	:alt: Release

.. image:: https://img.shields.io/github/workflow/status/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}/merge-to-main
	:target: https://img.shields.io/github/workflow/status/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}/merge-to-main
	:alt: Build status

.. image:: https://img.shields.io/github/commit-activity/m/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}
    :target: https://img.shields.io/github/commit-activity/m/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}
    :alt: Commit activity

.. image:: https://img.shields.io/badge/docs-gh--pages-blue
    :target: https://{{cookiecutter.github_author_handle}}.github.io/{{cookiecutter.project_name}}/
    :alt: Docs

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
	:target: https://github.com/psf/black
	:alt: Code style with black

.. image:: https://img.shields.io/badge/%20imports-isort-%231674b1
	:target: https://pycqa.github.io/isort/
	:alt: Imports with isort

.. image:: https://img.shields.io/github/license/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}
	:target: https://img.shields.io/github/license/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}
	:alt: License

{{cookiecutter.project_description}}

* **Github repository**: `https://github.com/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}/ <https://github.com/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}/>`_
* **Documentation**: `https://{{cookiecutter.github_author_handle}}.github.io/{{cookiecutter.project_name}}/ <https://{{cookiecutter.github_author_handle}}.github.io/{{cookiecutter.project_name}}/>`_


Releasing a new version
-----------------------------

{% if cookiecutter.publish_to == "pypi" -%}
- Create an API Token on `Pypi <https://pypi.org/>`_
- Add the API Token to your projects secrets with the name ``PYPI_TOKEN`` by visiting `this page <https://github.com/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}/settings/secrets/actions/new>`_.
- Create a `new release <https://github.com/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}/releases/new>`_ on Github. Create a new tag in the form ``*.*.*``.

For more details, see `here <https://fpgmaas.github.io/cookiecutter-poetry/releasing.html>`_.
{%- elif cookiecutter.publish_to == "artifactory" -%}
- Add the `ARTIFACTORY_URL`, `ARTIFACTORY_USERNAME`, and `ARTIFACTORY_PASSWORD` to your projects secrets by visiting `this page <https://github.com/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}/settings/secrets/actions/new>`_.
- Create a `new release <https://github.com/{{cookiecutter.github_author_handle}}/{{cookiecutter.project_name}}/releases/new>`_ on Github. Create a new tag in the form ``*.*.*``.

For more details, see `here <https://fpgmaas.github.io/cookiecutter-poetry/releasing.html>`_.
{%- endif %}

---------

Repository initiated with `fpgmaas/cookiecutter-poetry <https://github.com/fpgmaas/cookiecutter-poetry>`_