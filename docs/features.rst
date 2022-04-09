====================
Features
====================


.. contents:: :local:
    :depth: 3

Poetry
---------------

This is a `cookiecutter <https://github.com/cookiecutter/cookiecutter>`_ repository to generate the file structure for a Python project that uses `Poetry <https://python-poetry.org/>`_ for its dependency management.
When you have created your repository using this cookiecutter template, a poetry environment is pre-configured in ``pyproject.toml`` and ``poetry.toml``. All you need to do is
add your project-specific dependencies with

.. code-block:: bash

    poetry add <package>

and then install the environment with 

.. code-block:: bash

    make install

By default, the environment is created in a `.venv` folder, so you can easily start a interactive shell within the environment with ``poetry shell``

Makefile
-----------

A ``Makefile`` is available with the following commands:

+------------------------+-----------------------------------------------------------------------------------------------------------+
| Command                | Description                                                                                               |
+========================+===========================================================================================================+
| ``install``            | Install the poetry environment                                                                            |
+------------------------+-----------------------------------------------------------------------------------------------------------+
| ``format``             | Format code using isort and black.                                                                        |
+------------------------+-----------------------------------------------------------------------------------------------------------+
| ``lint``               | Check code formatting using isort, black, and flake8.                                                     |
+------------------------+-----------------------------------------------------------------------------------------------------------+
| ``test``               | Test the code with pytest                                                                                 |
+------------------------+-----------------------------------------------------------------------------------------------------------+
| ``build``              | Build wheel file using poetry                                                                             |
+------------------------+-----------------------------------------------------------------------------------------------------------+
| ``clean-build``        | clean build artifacts                                                                                     |
+------------------------+-----------------------------------------------------------------------------------------------------------+
| ``publish``            | Available if ``publish_to`` is set to ``"pypi"`` or ``"artifactory"``. Publishes to the specified index.  |
+------------------------+-----------------------------------------------------------------------------------------------------------+
| ``build-and-publish``  | Available if ``publish_to`` is set to ``"pypi"`` or ``"artifactory"``. Build and publish.                 |
+------------------------+-----------------------------------------------------------------------------------------------------------+

Pytest
----------

`pytest <https://docs.pytest.org/en/7.1.x/>`_ is automatically added to the environment, there is a template unittests in the ``tests`` directory and 
the tests can be run with

.. code-block:: bash

    make test


If ``include_github_actions`` is set to ``"y"``, the tests are automatically run for every merge request, 
every merge to main, and every release.

Formatting
----------

`isort <https://pycqa.github.io/isort/index.html>`_, `black <https://pypi.org/project/black/>`_ and `flake8 <https://flake8.pycqa.org/en/latest/>`_ are added 
as development dependencies. ``black`` and ``isort`` can be used to format the code with 

.. code-block:: bash

    make format

All three packages can be used to verify the code formatting with 

.. code-block:: bash

    make lint

If ``include_github_actions`` is set to ``"y"``, code formatting is checked for every merge request, every merge to main, and every release.

Pyenv
-------

A `.python-version` file is added with the specified ``python_version`` from the ``cookiecutter`` command, so that the right python version is used when ``make install`` is run.

CI/CD with Github actions (Optional)
---------------------------------------

when ``include_github_actions`` is set to ``"y"``, a ``.github`` directory is added with the following structure:

::

    .github
    ├── workflows
    ├─── run-checks
    │    └── action.yml    
    ├─── setup-poetry-env
    │    └── action.yml         
    ├── on-merge-to-main.yml
    ├── on-pull-request.yml          
    └── on-release-main.yml
      
``on-merge-to-main.yml`` and ``on-pull-request.tml`` are identical except for their trigger conditions; the first is run whenever a new commit is made to ``main`` 
(which should only happen through merge requests, hence the name), and the latter is run whenever a pull request is opened or updated. They call the ``action.yml`` files
to set-up the environment, run the tests, and check the code formatting.

``on-release-main.yml`` does all of the former whenever a new release is made on the ``main`` branch. To learn more about releasing, 
see :doc:`Releasing to Pypi or Artifactory <./releasing>` 

