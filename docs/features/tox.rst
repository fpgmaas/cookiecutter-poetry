==================
Tox
==================

The project uses `Tox <https://tox.wiki/en/latest/>`_ to test compatibility with multiple Python versions. By default, the project is tested
with Python ``3.7``, ``3.8``, and ``3.9``. Testing is done automatically in the CI/CD pipeline on every pull request, merge to main, and on each release.

If you want to add more Python versions you can simply add them to ``tox.ini`` and to the separate workflows in ``.github``.





