# Cookiecutter Poetry

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/fpgmaas/cookiecutter-poetry/merge-to-main)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1)](https://pycqa.github.io/isort/)
[![Dependency management: poetry](https://img.shields.io/badge/tool-poetry-orange)](https://pycqa.github.io/isort/)
[![License](https://img.shields.io/github/license/fpgmaas/cookiecutter-poetry)](https://github.com/fpgmaas/cookiecutter-poetry/blob/main/LICENSE)


This is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) repository to generate the file structure for a Python project that uses [Poetry](https://python-poetry.org/) for its dependency management.

## Features

| <span style="color:white">Feature</span>  | <span style="color:white">Description</span>  |
|------|----|
| <span style="color:white">**Poetry**</span>  | Generates a poetry environment file, ready to be installed with a single command. |
| <span style="color:white">**Makefile**</span>  |  A makefile with pre-configured commands, type `make help` to list the options. |
|  <span style="color:white">**Pytest**</span> | Adds a pytest template.|
|  <span style="color:white">**Formatting**</span> | Adds code formatting with `isort`, `black` and `flake8`.|
|  <span style="color:white">**CI/CD with Github actions**</span> (Optional) | Adds Github actions that run the formatting checks and unittests for pull requests and when merged to `main`. |

## How to use?

First, create an empty [new repository](https://github.com/new) on Github. Give it a name that only contains alphanumeric characters and optionally `-`. <u>Do not check any boxes under the option *'Initialize this repository with'*.</u> 

Then, on your local machine, either install `cookiecutter` in a pre-existing `pip`- or `poetry` managed environment with:

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

Then, run the following commands, replacing `<project-name>`, with the name that you also gave the Github repository and `<github_handle>` with your Github username.

```
cd <project_name>
git init .
git add .
git commit -m "Init commit"
git remote add origin git@github.com:<github_handle>/<project_name>.git
git push -u origin main
```

Finally, install the environment with `make install`.

## FAQ

Note: If you get an error in the shape of 
```
error: src refspec main does not match any
error: failed to push some refs to 'github.com:fpgmaas/example-project.git'
```

you are likely still using `master` as the default branch. You can change this with:

`git config --global init.defaultBranch main`

## Credits

This project is partially based on [Audrey Feldroy's](https://github.com/audreyfeldroy)'s great [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) repository.