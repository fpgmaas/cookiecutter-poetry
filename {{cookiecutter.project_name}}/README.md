# {{cookiecutter.project_name}}

<!-- Uncomment and **UPDATE** the following links to integrate documentation status for Read the Docs and Testspace. -->
<!-- [![Documentation Status](https://readthedocs.com/projects/partsnap-llc-{{cookiecutter.project_name}}/badge/?version=latest&token=fbd35572c635fc26d72e64f71a1b36006f1d65c3a70a5fa09bcfdfabc64da3d4)](https://partsnap-llc-partsnap-cookiecutter-poetry.readthedocs-hosted.com/en/latest/?badge=latest) -->
<!-- [![Space Metric](https://partsnap.testspace.com/spaces/276170/badge?token=61b8e588504e74168bfe61130177943269d116ee)](https://partsnap.testspace.com/spaces/276170?utm_campaign=metric&utm_medium=referral&utm_source=badge "Test Cases") -->
<!-- [![Space Metric](https://partsnap.testspace.com/spaces/276170/metrics/616814/badge?token=c8134493abfdc1f719ecc94703e37e77d778b63f)](https://partsnap.testspace.com/spaces/276170/current/Code%20Coverage?utm_campaign=metric&utm_medium=referral&utm_source=badge "Code Coverage (lines)") -->
<!-- [![Space Metric](https://partsnap.testspace.com/spaces/276170/metrics/616813/badge?token=ed02f64788f25309f24a951cf3cae40e97c41487)](https://partsnap.testspace.com/spaces/276170/current/Code%20Coverage?utm_campaign=metric&utm_medium=referral&utm_source=badge "Code Coverage (branches)") -->

{{cookiecutter.project_description}}

- **Github repository**: <https://github.com/partsnap/{{cookiecutter.project_name}}/>
- **Documentation** <https://partsnap.github.io/{{cookiecutter.project_name}}/>

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

## Getting started with your project

---

**NOTE**: Make sure you have performed the
[initial system configuration](#system-configuration-one-time) **once**.

---

First, create/find a directory you want to clone the repo into and run this command:

```bash
git clone https://github.com/partsnap/{{cookiecutter.project_name}}.git
```

Finally, install the environment and run the pre-commit hooks:

```bash
make install
make check
make test
make docs
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPi or Artifactory, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/codecov/).

## Docker Setup

To run the Docker setup, run these commands:

```bash
make docker-build
make docker-start
make docker-stop
```

{% if cookiecutter.database == "y" -%}
## Database CLI Useful Commands

Use these commands to populate and clear the database:
{{cookiecutter.project_slug}} db populate
{{cookiecutter.project_slug}} db clear
{%- endif %}

{%- if cookiecutter.publish_to == "pypi" -%}
## Releasing a new version

- Create an API Token on [Pypi](https://pypi.org/).
- Add the API Token to your projects secrets with the name `PYPI_TOKEN` by visiting [this page](https://github.com/partsnap/{{cookiecutter.project_name}}/settings/secrets/actions/new).
- Create a [new release](https://github.com/partsnap/{{cookiecutter.project_name}}/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).
{%- elif cookiecutter.publish_to == "artifactory" -%}

- Add the `ARTIFACTORY_URL`, `ARTIFACTORY_USERNAME`, and `ARTIFACTORY_PASSWORD` to your projects secrets by visiting [this page](https://github.com/partsnap/{{cookiecutter.project_name}}/settings/secrets/actions/new).
- Create a [new release](https://github.com/partsnap/{{cookiecutter.project_name}}/releases/new) on Github.
- Create a new tag in the form `*.*.*`.

For more details, see [here](https://fpgmaas.github.io/cookiecutter-poetry/features/cicd/#how-to-trigger-a-release).
{%- endif -%}

---

Repository initiated with [partsnap/partsnap-cookiecutter-poetry](https://github.com/partsnap/partsnap-cookiecutter-poetry).
