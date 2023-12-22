# Tutorial

This page contains a complete tutorial on how to create your project.

## Step 1: Install poetry

To start, we will need to install `poetry`. The instructions to install poetry can be found
[here](https://python-poetry.org/docs/). After installing, it is recommended to run

```bash
poetry config virtualenvs.in-project true
```

which will by default create new virtual environments in `./.venv`
whenever you create them with `poetry init`.

## Step 2: Install pyenv (Optional)

I would recommend to use `pyenv` for managing your different Python versions. However, if you prefer another method of
managing your Python versions, feel free to skip this step and continue to [step 3](#step-3-generate-your-project).

The instructions to install pyenv can be found [here](https://github.com/pyenv/pyenv). The instructions to install
poetry can be found [here](https://python-poetry.org/docs/).

Install a version of Python with pyenv. To see a list of available
versions, run:

```bash
pyenv install --list
```

Select a version and install it with

```bash
pyenv install -v 3.9.7
```

Replacing `3.9.7` with a version of your choosing.

Configure pyenv to use the python version you want, either specifically for this project with:

```bash
pyenv local x.y.z
```

...or globally as your primary python version with:

```bash
pyenv global x.y.z
```

## Step 3: Generate your project

First, navigate to the directory in which you want the project to be
created. Then, create your project with the following commands:

```bash
pip install cookiecutter
cookiecutter gh:dvatvani/cookiecutter-poetry
```

## Step 4: Set up your Github repository

Create an empty [new repository](https://github.com/new) on Github. Give
it a name that only contains alphanumeric characters and optionally `-`.
DO NOT check any boxes under the option `Initialize this repository
with`.

## Step 5: Upload your project to Github

Setup the project with the justfile recipe. This initialises the Git repository, installs the poetry environment and pushes the initial state of the project to GitHub.

```bash
just setup-project
```

## Step 6: Activate your environment


Activate the `poetry` environment by running:

```bash
poetry shell
```

## Step 7: Sign up to codecov.io

If you enabled code coverage with codecov for your project, you should sign up with your GitHub account at [codecov.io](https://about.codecov.io/language/python/)

## Step 8: Configure your repository secrets

If you want to deploy your project to Pypi or Artifactory using the
Github Actions, you will have to set some repository secrets. For
instructions on how to do that, see [here](./features/publishing.md#set-up-for-pypi) for PyPi, or
[here](./features/publishing.md#set-up-for-artifactory) for Artifactory.

## Step 9: Create a new release

To trigger a new release, navigate to your repository on GitHub, click `Releases` on the right, and then select `Draft
a new release`. If you fail to find the button, you could also directly visit
`https://github.com/<username>/<repository-name>/releases/new`.

Give your release a title, and add a new tag in the form `*.*.*` where the
`*`'s are alphanumeric. To finish, press `Publish release`.

## Step 10: Enable your documentation

In your repository, navigate to `Settings > Code and Automation > Pages`. If you succesfully created a new release,
you should see a notification saying ` Your site is ready to be published at https://<author_github_handle>.github.io/<project_name>/`.

To finalize deploying your documentation, under `Source`, select the branch `gh-pages`.

## Step 11: You're all set!

That's it! I hope this repository saved you a lot of manual configuration. If you have any improvement suggestions, feel
free to raise an issue or open a PR on Github!
