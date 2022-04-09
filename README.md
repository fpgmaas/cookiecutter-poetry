# Cookiecutter Poetry

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/fpgmaas/cookiecutter-poetry/on-merge-to-main.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat)](https://pycqa.github.io/isort/)
[![Dependency management: poetry](https://img.shields.io/badge/%20tool-poetry-%231674b1?style=flat)](https://pycqa.github.io/isort/)

## What is it?

This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) repository to generate the file structure for a Python project that uses [Poetry](https://python-poetry.org/) for its dependency management.

### Features

| <span style="color:white">Feature</span>  | <span style="color:white">Description</span>  |
|------|----|
| <span style="color:white">**Poetry**</span>  | Generates a poetry environment file, ready to be installed with a single command. |
| <span style="color:white">**Makefile**</span>  |  A makefile with pre-configured commands, type `make help` to list the options. |
|  <span style="color:white">**Pytest**</span> | Adds a pytest template.|
|  <span style="color:white">**Formatting**</span> | Adds code formatting with `isort`, `black` and `flake8`.|
|  <span style="color:white">**Github actions**</span> (Optional) | Adds Github actions that run the formatting checks and unittests for pull requests and when merged to `main`. |

## How to use?

Either install `cookiecutter` in a pre-existing pip- or poetry managed environment with:

```bash
pip install -U cookiecutter
```
or
```
poetry add cookiecutter
```

Then, navigate to the directory in which you want to create your project and run:

```
cookiecutter https://github.com/fpgmaas/cookiecutter-poetry.git
```

### Prerequisities

You should have either a Python environment with pip or with poetry installed. The recommended method for managing multiple python enviornments is with [pyenv](https://github.com/pyenv/pyenv#installation).

### Install cookiecutter

Navigate to an empty directory and install cookiecutter:
```
pyenv local <PYTHON_VERSION>
poetry config --local virtualenvs.in-project true
poetry init
```