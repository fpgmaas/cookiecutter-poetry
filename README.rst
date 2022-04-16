====================
Cookiecutter Poetry
====================

.. image:: https://img.shields.io/github/v/release/fpgmaas/cookiecutter-poetry
	:target: https://pypi.org/project/cookiecutter-poetry/
	:alt: Release

.. image:: https://img.shields.io/github/workflow/status/fpgmaas/cookiecutter-poetry/merge-to-main
	:target: https://img.shields.io/github/workflow/status/fpgmaas/cookiecutter-poetry/merge-to-main
	:alt: Build status

.. image:: https://img.shields.io/pypi/pyversions/cookiecutter-poetry
    :target: https://pypi.org/project/cookiecutter-poetry/
    :alt: Supported Python versions

.. image:: https://img.shields.io/badge/docs-gh--pages-blue
    :target: https://fpgmaas.github.io/cookiecutter-poetry/
    :alt: Docs

.. image:: https://img.shields.io/github/commit-activity/m/fpgmaas/cookiecutter-poetry
    :target: https://img.shields.io/github/commit-activity/m/fpgmaas/cookiecutter-poetry
    :alt: Commit activity

.. image:: https://img.shields.io/github/license/fpgmaas/cookiecutter-poetry
	:target: https://img.shields.io/github/license/fpgmaas/cookiecutter-poetry
	:alt: License

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
	:target: https://github.com/psf/black
	:alt: Code style with black

.. image:: https://img.shields.io/badge/%20imports-isort-%231674b1
	:target: https://pycqa.github.io/isort/
	:alt: Imports with isort

This is a `cookiecutter <https://github.com/cookiecutter/cookiecutter>`_ repository to generate the file structure for a Python project that uses `Poetry <https://python-poetry.org/>`_ for its dependency management.

+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| **Documentation**             | `https://fpgmaas.github.io/cookiecutter-poetry/ <https://fpgmaas.github.io/cookiecutter-poetry/>`_                                   |
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| **Example Repository**        | `https://github.com/fpgmaas/cookiecutter-poetry-example/ <https://github.com/fpgmaas/cookiecutter-poetry-example/>`_                 |
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| **Pypi**                      | `https://pypi.org/project/cookiecutter-poetry/ <https://pypi.org/project/cookiecutter-poetry//>`_                                    |
+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+


Features
--------

+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Feature                                      | Description                                                                                                                                                |
+==============================================+============================================================================================================================================================+
| **Poetry**                                   | Generates a `poetry <https://python-poetry.org/>`_ environment file, ready to be installed with a single command.                                          |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Makefile**                                 | A makefile with pre-configured commands, type `make help` to list the options.                                                                             |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Pytest**                                   | Adds a `pytest <https://docs.pytest.org/en/7.1.x/>`_ template.                                                                                             |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Formatting**                               | Adds code formatting with `isort <https://github.com/PyCQA/isort>`_ and `black <https://pypi.org/project/black/>`_.                                        |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **CI/CD with Github actions**                | Adds Github actions that run the formatting checks and unittests for pull requests and when merged to `main`.                                              |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Release to Pypi**                          | Release to `Pypi <https://pypi.org>`_ by creating a new release on Github.                                                                                 |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Release to Artifactory**                   | Release to `Artifactory <https://jfrog.com/artifactory>`_ by creating a new release on Github.                                                             |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Documentation with MkDocs**                | Automatically add documentation to your project and its code with `MkDocs <https://www.mkdocs.org/>`_.                                                     |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Tox testing**                              | Setup and CI/CD integration to easily test for different Python versions with `Tox <https://tox.wiki/>`_.                                                  |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+


Example CI/CD Pipeline
--------------------------

.. image:: https://raw.githubusercontent.com/fpgmaas/cookiecutter-poetry/main/static/images/pipeline.png
	:target: https://raw.githubusercontent.com/fpgmaas/cookiecutter-poetry/main/static/images/pipeline.png
	:alt: Example pipeline
    
Quickstart
------------

On your local machine, navigate to the directory in which you want to create a project directory, and run the following two commands:

.. code-block:: bash

    pip install cookiecutter-poetry 
    ccp

Alternatively, install ``cookiecutter`` and directly pass the URL to this Github repository to the ``cookiecutter`` command:

.. code-block:: bash

    pip install cookiecutter
    cookiecutter https://github.com/fpgmaas/cookiecutter-poetry.git

Then run the following commands, replacing ``<project-name>``, with the name that you also gave the Github repository and ``<github_author_handle>`` with your Github username.

.. code-block:: bash
    
    cd <project_name>
    git init -b main
    git add .
    git commit -m "Init commit"
    git remote add origin git@github.com:<github_author_handle>/<project_name>.git
    git push -u origin main


Finally, install the environment with `make install`. 

You are now ready to start development on your project! The CI/CD pipeline will be triggered when you open a pull
request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory through CI/CD, see `here <https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi>`_. 
For activating the automatic documentation with MkDocs, see `here <https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github>`__.


Acknowledgements
-----------------

This project is partially based on 
`Audrey Feldroy's <https://github.com/audreyfeldroy>`_'s great `cookiecutter-pypackage <https://github.com/audreyfeldroy/cookiecutter-pypackage>`_ repository.



