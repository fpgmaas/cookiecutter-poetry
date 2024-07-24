<p align="center">
  <div class="row">
  <div class="column">
    <img width="100" src="./docs/static/partsnap-woman.png">
  </div>
  <div class="column">
  <img width="600" src="./docs/static/cookiecutter.svg">
  </div>
</div>
</p style = "margin-bottom: 2rem;">

[![Documentation Status](https://readthedocs.com/projects/partsnap-llc-partsnap-cookiecutter-poetry/badge/?version=latest&token=fbd35572c635fc26d72e64f71a1b36006f1d65c3a70a5fa09bcfdfabc64da3d4)](https://partsnap-llc-partsnap-cookiecutter-poetry.readthedocs-hosted.com/en/latest/?badge=latest)

<!-- [![Space Metric](https://partsnap.testspace.com/spaces/276170/badge?token=61b8e588504e74168bfe61130177943269d116ee)](https://partsnap.testspace.com/spaces/276170?utm_campaign=metric&utm_medium=referral&utm_source=badge "Test Cases") -->
<!-- [![Space Metric](https://partsnap.testspace.com/spaces/276170/metrics/616814/badge?token=c8134493abfdc1f719ecc94703e37e77d778b63f)](https://partsnap.testspace.com/spaces/276170/current/Code%20Coverage?utm_campaign=metric&utm_medium=referral&utm_source=badge "Code Coverage (lines)") -->
<!-- [![Space Metric](https://partsnap.testspace.com/spaces/276170/metrics/616813/badge?token=ed02f64788f25309f24a951cf3cae40e97c41487)](https://partsnap.testspace.com/spaces/276170/current/Code%20Coverage?utm_campaign=metric&utm_medium=referral&utm_source=badge "Code Coverage (branches)") -->

> This is the latest version that is supporting web services and library projects for PARTSNAP LLC.
> To use the original version, invoke cookiecutter with template version 1.0.0

`cookiecutter git@github.com:partsnap/partsnap-cookiecutter-poetry.git -c 1.0.0`

> For more information or to report any bug, see [DOPS-19 PartSnap Cookie Cutter Improvements](https://partsnap.atlassian.net/browse/DOPS-19)

**NOTE**

This version is a fork from https://github.com/fpgmaas/cookiecutter-poetry. See [Acknowledgements](#acknowledgements)

To view the original documentation click [here](https://fpgmaas.github.io/cookiecutter-poetry/)

---

## System Configuration (One Time)

install [NixOS](https://nixos.org/) if you don't have NixOS installed yet
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

We want to make sure Nix OS doesn't break if you update your Mac OS to the newest version.
To do this we need to edit the .zshrc with nano.

```bash
  $ nano ~/.zshrc
```

Make sure everything is here. (your_user) is going to depend on your system user you are using located on that export PATH.

```
    export PATH="$PATH:/Users/(your_user_)/.local/bin"
    eval "$(direnv hook zsh)"
    # Nix
    if [ -e '/nix/var/nix/profiles/default/etc/profile.d/nix-daemon.sh' ]; then
    . '/nix/var/nix/profiles/default/etc/profile.d/nix-daemon.sh'
    fi
    # End Nix
```

After closing nano and returning to bash make sure to source the changes.

```bash
  $ source ~/.zshrc
```

Now Nix-OS should be properly set for any projects located in the specified location you put.

install cookiecutter

```bash
pipx install cookiecutter
```

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
make check
make docs
```

You are now ready to start development on your project! The CI/CD
pipeline will be triggered when you open a pull request, merge to main,
or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see [here](./features/publishing.md#set-up-for-pypi). For activating the automatic documentation with MkDocs, see [here](./features/mkdocs.md#enabling-the-documentation-on-github). To enable the code coverage reports, see [here](./features/codecov).

## Testspace Integration

This template supports Testspace from the start. You just need to go to [Testspace PartSnap LLC](https://partsnap.testspace.com/).
Top right "+ New Project" button and tie the repostiory you just created with Testspace. Documenation for Testspace on project creation
is commented out by default and will have to be manually updated once you connect the new repoistory to Testspace.

## Useful Tutorials

### Integration with PyCharm

If you are using NixOS and Pycharm, check this [tutorial](./docs/tutorials/pycharm_nixos.md)
for setting things up.

### Mermaid Diagram and Charting System

check this [tutorial](./docs/tutorials/mermaid.md)

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

## Reference

- [Developing Python and Rust projects on NixOS using IntelliJ IDEA and PyCharm](https://o.librepush.net/solutions/nix/developing-python-rust-projects-on-nixos/)
- [Package and deploy Python apps faster with Poetry and Nix](https://www.youtube.com/watch?v=TbIHRHy7_JM)

## Acknowledgements

This project is a fork from [Florian Maas](https://github.com/fpgmaas) which is
partially based on [Audrey Feldroy's](https://github.com/audreyfeldroy) great
[cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).
