
# Cookiecutter Poetry


This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter)
repository to generate the file structure for a Python project that uses
[Poetry](https://python-poetry.org/) for its dependency management. 

A project generated with ``cookiecutter-poetry`` supports the following features:

- [Poetry](https://python-poetry.org/) for dependency management.
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Formatting with [black](https://pypi.org/project/black/) and [isort](https://pycqa.github.io/isort/index.html)
- Publishing to [Pypi](https://pypi.org) or [Artifactory](https://jfrog.com/artifactory) by creating a new release on GitHub.
- Testing with [pytest](https://docs.pytest.org/en/7.1.x/)
- Documentation with [sphinx](https://www.sphinx-doc.org/en/master/)
- Compatibility testing with [Tox](https://tox.wiki/en/latest/)

An example of a repository generated with this package can be found [here](https://github.com/fpgmaas/cookiecutter-poetry-example).

## Quickstart

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following two commands:

``` bash
pip install cookiecutter-poetry 
ccp
```

Alternatively, install `cookiecutter` and directly pass the URL to this
Github repository to the `cookiecutter` command:

``` bash
pip install cookiecutter
cookiecutter https://github.com/fpgmaas/cookiecutter-poetry.git
```

Then run the following commands, replacing `<project-name>`, with the
name that you also gave the Github repository and
`<github_author_handle>` with your Github username.

``` bash
cd <project_name>
git init -b main
git add .
git commit -m "Init commit"
git remote add origin git@github.com:<github_author_handle>/<project_name>.git
git push -u origin main
```

Finally, install the environment with `make install`.

If you want to deploy to Pypi or Artifactory automatically on each
release, you need to set some secrets in your repository on Github. For
more information, see [the
documentation](https://fpgmaas.github.io/cookiecutter-poetry/features/releasing.html).

## Acknowledgements

This project is partially based on [Audrey
Feldroy's](https://github.com/audreyfeldroy) great
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).

