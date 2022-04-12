=======
Poetry
=======

The generated repository will uses `Poetry <https://python-poetry.org/>`_ for its dependency management. When you have
created your repository using this cookiecutter template, a poetry environment is pre-configured in ``pyproject.toml``
and ``poetry.toml``. All you need to do is add your project-specific dependencies with

.. code-block:: bash

    poetry add <package>

and then install the environment with 

.. code-block:: bash

    make install

By default, the environment is created in a ``.venv`` folder, so you can easily start an interactive shell within the environment with ``poetry shell``.