==================
Prompt arguments
==================

When running the command

.. code-block:: bash

    cookiecutter https://github.com/fpgmaas/cookiecutter-poetry.git

a prompt will start which enables you to configure your repository. The prompt values and their explanation are as follows:

**author**
    Your full name.

**email**
    Your email address.

**github_author_handle**
    Your github handle, i.e. ``<handle>`` in ``https://github.com/<handle>``

**project_name**
    Your project name. Should be equal to the name of your repository and it should only contain alphanumeric characters and ``-``'s.

**project_slug**
    The project slug, will default to the ``project_name`` with all ``-``'s replaced with ``_``. 
    This will be how you import your code later, e.g.

    .. code-block:: python

        from <project_slug> import foo

**project_description**
    A short description of your project.

**python_version**
    The python version of your project.

**include_pyenv_local_file**
    ``"y"`` or ``"n"``. Adds a ``.python-version`` file to the root directory for pyenv.

**include_github_actions**
    ``"y"`` or ``"n"``. Adds a ``.github`` directory with various actions and workflows to setup the environment and run code formatting checks and unittests.

**publish_to**
    ``"pypi"``, ``"artifactory"``, or ``"none"``. Adds functionality to the ``Makefile`` and Github workflows to make publishing 
    your code as simple as creating a new release release on Github. 
    For more info, see :doc:`Releasing to Pypi or Artifactory <./features/releasing>`.

**sphinx_docs**
    ``"y"`` or ``"n"``. Adds `sphinx <https://www.sphinx-doc.org/en/master/>`_ documentation to your project. This includes automatically parsing your
    docstrings and adding them to the documentation. Documentation will be deployed to the ``gh-pages`` branch.

**open_source_license**
    Choose a `license <https://choosealicense.com/>`_. Options: ``["1. MIT License", "2. BSD license", "3. ISC license", 
    "4. Apache Software License 2.0", "5. GNU General Public License v3", "6. Not open source"]``
