<p align="center">
<div class="row">
  <div class="column">
    <img width="100" src="static/partsnap-woman.png">
  </div>
  <div class="column">
  <img width="600" src="static/cookiecutter.svg">
  </div>
</div>
</p style = "margin-bottom: 2rem;">
<style>
  .md-typeset h1,
  .md-content__button {
    display: none;
  }
  .column {
  float: left;
  width: 33.33%;
  padding: 5px;
}
.row::after {
  content: "";
  clear: both;
  display: table;
}
</style>

---

[![Release](https://img.shields.io/github/v/release/fpgmaas/cookiecutter-poetry)](https://pypi.org/project/cookiecutter-poetry/)
[![Build status](https://img.shields.io/github/actions/workflow/status/fpgmaas/cookiecutter-poetry/main.yml?branch=main)](https://github.com/fpgmaas/cookiecutter-poetry/actions/workflows/main.yml?query=branch%3Amain)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/cookiecutter-poetry)](https://pypi.org/project/cookiecutter-poetry/)
[![License](https://img.shields.io/github/license/fpgmaas/cookiecutter-poetry)](https://img.shields.io/github/license/fpgmaas/cookiecutter-poetry)

This is a modern Cookiecutter template that can be used to initiate a Python project with all the necessary tools for development, testing, and deployment. See [Features](#features) for a list of capabilities.

---

**NOTE**

This version is a for from https://github.com/fpgmaas/cookiecutter-poetry. See [Acknowledgements](#acknowledgements)

---

## Quickstart

---

**NOTE**: Make sure you have performed the
[initial system configuration](#system-configuration-one-time) **once**.

---

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following two commands:

```
cookiecutter https://github.com/partsnap/partsnap-cookiecutter-poetry.git
```

Create a repository on GitHub, and then run the following commands, replacing `<project-name>`, with the name that you gave the Github repository and
`<github_author_handle>` with your Github username.

```bash
cd <project_name>
git init -b main
git add .
git commit -m "Init commit"
git remote add origin git@github.com:<github_author_handle>/<project_name>.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see [here](./features/publishing.md#set-up-for-pypi). For activating the automatic documentation with MkDocs, see [here](./features/mkdocs.md#enabling-the-documentation-on-github). To enable the code coverage reports, see [here](./features/codecov.md).

## System Configuration (One Time)

install [pipx](https://pipx.pypa.io/stable/installation/)
make sure you run `pipx ensurepath` and restart your shell

install [NixOS](https://nixos.org/) if you haven't done so already
install [direnv](https://direnv.net/). On the latest OSX version do:

```bash
  $ brew install direnv
  $ echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
```

configure [direnv](https://direnv.net/man/direnv.toml.1.html) toml file to trust our org

```bash
  $ mkdir -p ~/.config/direnv/
  $ touch ~/.config/direnv/config.toml
```

copy the following in your `config.toml` file (you can change the path to wherever your GitHub root is. Note that this will trust `ALL` directories underneath)

```
  [global]
  warn_timeout="20s"
  [whitelist]
  prefix = ["~/github/partsnap"]
```

install cookiecutter

```bash
pipx install cookiecutter
```

## Features

This is a modern Cookiecutter template that can be used to initiate a Python project with all the necessary tools for development, testing, and deployment. It supports the following features:

- [Poetry](https://python-poetry.org/) for dependency management
- CI/CD with [GitHub Actions](https://github.com/features/actions)
- Pre-commit hooks with [pre-commit](https://pre-commit.com/)
- Code quality with [ruff](https://github.com/charliermarsh/ruff), [mypy](https://mypy.readthedocs.io/en/stable/), [deptry](https://github.com/fpgmaas/deptry/) and [prettier](https://prettier.io/)
- Publishing to [Pypi](https://pypi.org) or [Artifactory](https://jfrog.com/artifactory) by creating a new release on GitHub
- Testing and coverage with [pytest](https://docs.pytest.org/en/7.1.x/) and [codecov](https://about.codecov.io/)
- Documentation with [MkDocs](https://www.mkdocs.org/)
- Compatibility testing for multiple versions of Python with [Tox](https://tox.wiki/en/latest/)
- Containerization with [Docker](https://www.docker.com/)
- Development environment with [VSCode devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)

An example of a repository generated with this package can be found [here](https://github.com/fpgmaas/cookiecutter-poetry-example).

## Acknowledgements

This project is a fork from [Florian Maas](https://github.com/fpgmaas) which is
partially based on [Audrey Feldroy's](https://github.com/audreyfeldroy) great
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).
