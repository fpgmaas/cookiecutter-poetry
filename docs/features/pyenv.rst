==================
Pyenv 
==================

When working with poetry, my recommendation is to use `pyenv <https://github.com/pyenv/pyenv>`_ to manage your python versions.
Pyenv lets you easily switch between Python versions, which is very useful when working on various projects with their own poetry environment.

If ``include_pyenv_local_file`` is set to ``"y"``, a `.python-version` file is added with the specified
``python_version`` from the ``cookiecutter`` command, so that the right python version is used when ``make install`` is
run.

The same result can be achieved by setting ``include_pyenv_local_file`` to ``"n"``, and running 

.. code-block:: bash

    pyenv local x.y.z

in the terminal within the project directory after creation of the project.

For a good introduction to pyenv, see `this tutorial <https://realpython.com/intro-to-pyenv/>`_.

