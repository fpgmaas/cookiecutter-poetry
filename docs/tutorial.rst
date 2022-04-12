==========
Tutorial
==========

This page contains a complete tutorial on how to create your project.

Step 1: Install pyenv and poetry
------------------------------------

To start, we will need to install ``pyenv`` and ``poetry``. The instructions to install pyenv can be found `here <https://github.com/pyenv/pyenv>`_.
The instructions to install poetry can be found `here <https://python-poetry.org/docs/>`__.

Then, install a version of Python with pyenv. To see a list of available versions, run:

.. code-block:: bash

    pyenv install --list

Select a version and install it with

.. code-block:: bash

    pyenv install -v 3.9.7

Replacing ``3.9.7`` with a version of your choosing. For the rest of this tutorial, replace ``3.9.7`` with the version you have chosen here.

It is also recommended to run

.. code-block:: bash

    poetry config virtualenvs.in-project true

which will by default create new virtual environments in ``./.venv`` whenever you create them with ``poetry init``.

Step 2: Install cookiecutter
------------------------------

First, navigate to the directory in which you want the project to be created. Then, we need to install cookiecutter.

There are multiple ways of installing cookiecutter. If you have ``pip`` installed, you could install it simply with

.. code-block:: bash

    pip install cookiecutter

You could also create a temporary poetry environment and install it there:

.. code-block::

    pyenv local 3.9.7
    poetry init
    poetry add cookiecutter
    poetry shell

Step 3: Generate your project
---------------------------------

Within the directory in which you want to create your project, run:

.. code-block:: bash

    cookiecutter https://github.com/fpgmaas/cookiecutter-poetry.git

For an explanation of the prompt arguments, see :doc:`Prompt arguments <./prompt_arguments>`.

Step 4: Set up your Github repository
----------------------------------------

Create an empty `new repository <https://github.com/new>`_ on Github. 
Give it a name that only contains alphanumeric characters and optionally ``-``. 
DO NOT check any boxes under the option *'Initialize this repository with'*.

Step 5: Upload your project to Github
--------------------------------------

Run the following commands, replacing ``<project-name>`` with the name that you also gave the Github repository and ``<github_author_handle>`` with your Github username.

.. code-block:: bash
    
    cd <project_name>
    git init -b main
    git add .
    git commit -m "Init commit"
    git remote add origin git@github.com:<github_author_handle>/<project_name>.git
    git push -u origin main

Step 6: Activate your environment
--------------------------------------

Install and activate the environment by running:

.. code-block:: bash

    poetry install
    poetry shell

Step 6: Configure your repository secrets
-------------------------------------------

If you want to deploy your project to Pypi or Artifactory using the Github Actions, you will have to set some repository secrets.
For instructions on how to do that, see :doc:`Releasing to Pypi or Artifactory <./features/releasing>`.