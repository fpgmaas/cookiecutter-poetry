====================
Cookiecutter Poetry
====================

.. image:: https://img.shields.io/github/workflow/status/fpgmaas/cookiecutter-poetry/merge-to-main
	:target: https://img.shields.io/github/workflow/status/fpgmaas/cookiecutter-poetry/merge-to-main
	:alt: Build status

.. image:: https://img.shields.io/github/commit-activity/m/fpgmaas/cookiecutter-poetry
    :target: https://img.shields.io/github/commit-activity/m/fpgmaas/cookiecutter-poetry
    :alt: Commit activity

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
	:target: https://img.shields.io/badge/code%20style-black-000000.svg
	:alt: Code style with black

.. image:: https://img.shields.io/badge/%20imports-isort-%231674b1
	:target: https://img.shields.io/badge/%20imports-isort-%231674b1
	:alt: Imports with isort

.. image:: https://img.shields.io/badge/tool-poetry-orange
	:target: https://img.shields.io/badge/tool-poetry-orange
	:alt: Dependency management with poetry

.. image:: https://img.shields.io/github/license/fpgmaas/cookiecutter-poetry
	:target: https://img.shields.io/github/license/fpgmaas/cookiecutter-poetry
	:alt: License

This is a `cookiecutter <https://github.com/cookiecutter/cookiecutter>`_ repository to generate the file structure for a Python project that uses `Poetry <https://python-poetry.org/>`_ for its dependency management.

+-------------------------------+----------------------------------------------------------------------------------------------------------------------+
| **Github repository**         | `https://github.com/fpgmaas/cookiecutter-poetry/ <https://github.com/fpgmaas/cookiecutter-poetry/>`_   |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------+
| **Documentation**             | `https://fpgmaas.github.io/cookiecutter-poetry/ <https://fpgmaas.github.io/cookiecutter-poetry/>`_                   |
+-------------------------------+----------------------------------------------------------------------------------------------------------------------+




Features
--------

+-------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Feature                                   | Description                                                                                                     |
+===========================================+=================================================================================================================+
| **Poetry**                                | Generates a poetry environment file, ready to be installed with a single command.                               |
+-------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **Makefile**                              | A makefile with pre-configured commands, type `make help` to list the options.                                  |
+-------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **Pytest**                                | Adds a pytest template.                                                                                         |
+-------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **Formatting**                            | Adds code formatting with ``isort``, ``black`` and ``flake8``.                                                  |
+-------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **Pyenv** (Optional)                      | Automatically adds a ``.python-version`` file for `pyenv <https://github.com/pyenv/pyenv>`_ support.            |
+-------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **CI/CD with Github actions** (Optional)  | Adds Github actions that run the formatting checks and unittests for pull requests and when merged to `main`.   |
+-------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **Release to Pypi** (Optional)            | Release to `Pypi <https://pypi.org>`_ manually, or by creating a new release on Github.                         |
+-------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| **Release to Artifactory** (Optional)     | Release to `Artifactory <https://jfrog.com/artifactory>`_ manually, or by creating a new release on Github.     |
+-------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

Quickstart
------------

First, create an empty `new repository <https://github.com/new>`_ on Github. Give it a name that only contains alphanumeric characters and optionally ``-``. DO NOT check any boxes under the option *'Initialize this repository with'*.

On your local machine, install ``cookiecutter`` with:

.. code-block:: bash

    pip install -U cookiecutter 

Navigate to the directory in which you want to create your project and run:

.. code-block:: bash

    cookiecutter https://github.com/fpgmaas/cookiecutter-poetry.git

Run the following commands, replacing ``<project-name>``, with the name that you also gave the Github repository and ``<github_author_handle>`` with your Github username.

.. code-block:: bash
    
    cd <project_name>
    git init .
    git add .
    git commit -m "Init commit"
    git remote add origin git@github.com:<github_author_handle>/<project_name>.git
    git push -u origin main

Finally, install the environment with ``make install``.


Credits
---------

This project is partially based on 
`Audrey Feldroy's <https://github.com/audreyfeldroy>`_'s great `cookiecutter-pypackage <https://github.com/audreyfeldroy/cookiecutter-pypackage>`_ repository.



