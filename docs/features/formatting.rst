===============
Formatting
===============

`isort <https://pycqa.github.io/isort/index.html>`_ and `black <https://pypi.org/project/black/>`_ are added 
as development dependencies. ``black`` and ``isort`` can be used to format the code with 

.. code-block:: bash

    make format

All three packages can be used to verify the code formatting with 

.. code-block:: bash

    make lint

If ``include_github_actions`` is set to ``"y"``, code formatting is checked for every merge request, every merge to main, and every release.