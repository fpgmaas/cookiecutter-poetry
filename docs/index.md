
# Cookiecutter Poetry


This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter)
repository to generate the file structure for a Python project that uses
[Poetry](https://python-poetry.org/) for its dependency management. 

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

## Features

- **Poetry**: Generates a [poetry](https://python-poetry.org/) environment file, ready to be installed with a single command.
- **Makefile**: A makefile with pre-configured commands, type `make help` to list the options.
- **Pytest**: Adds a [pytest](https://docs.pytest.org/en/7.1.x/) template.
- **Formatting**: Adds code formatting with [isort](https://github.com/PyCQA/isort) and [black](https://pypi.org/project/black/).
- **CI/CD with Github actions**: Adds Github actions that run the formatting checks and unittests for pull requests and when merged to `main`.
- **Release to Pypi**: Release to [Pypi](https://pypi.org) by creating a new release on Github.
- **Release to Artifactory**: Release to [Artifactory](https://jfrog.com/artifactory) by creating a new release on Github.
- **Documentation with Sphinx**: Automatically add documentation to your project and its code with [Sphinx](https://www.sphinx-doc.org/).
- **Tox testing** Setup and CI/CD integration to easily test for different Python versions with [Tox](https://tox.wiki/).



## Acknowledgements

This project is partially based on [Audrey
Feldroy's](https://github.com/audreyfeldroy) great
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).

