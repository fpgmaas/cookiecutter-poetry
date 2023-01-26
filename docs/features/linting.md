# Linting and code quality

Code can be linted and quality-checked with the command

``` bash
make check
```

Note that this requires the pre-commit hooks to be installed. 

This command will run the following tools:

## black 

[black](https://pypi.org/project/black/) is used to format the code, and it is configured through `pyproject.toml`:

```toml
[tool.black]
line-length = 120
include = '\.pyi?$'
target-version = ['py39']
fast = true
```

To exclude directories or files, add an `exclude` argument to `pre-commit-config.yaml`. Note that adding an `exclude` argument to `pyproject.toml`
will not work, see also [here](https://stackoverflow.com/a/61046953/8037249).

## ruff

[ruff](https://github.com/charliermarsh/ruff) is used to check the code style, and it is configured through `pyproject.toml`:

```
[tool.ruff]
target-version = "py37"
line-length = 120
fix = false
select = [
    # flake8-2020
    "YTT",
    # flake8-bandit
    "S",
    # flake8-bugbear
    "B",
    # flake8-builtins
    "A",
    # flake8-comprehensions
    "C4",
    # flake8-debugger
    "T10",
    # flake8-print
    "T20",
    # flake8-simplify
    "SIM",
    # isort
    "I",
    # mccabe
    "C90",
    # pycodestyle
    "E", "W",
    # pyflakes
    "F",
    # pygrep-hooks
    "PGH",
    # pyupgrade
    "UP",
    # ruff
    "RUF",
    # tryceratops
    "TRY",
]
ignore = [
    # LineTooLong
    "E501",
    # DoNotAssignLambda
    "E731",
]

[tool.ruff.per-file-ignores]
"tests/*" = ["S101"]
```

# mypy

[mypy](https://mypy.readthedocs.io/en/stable/) is used for static type checking, and it's configuration and can be edited in `pyproject.toml`.

```toml
[tool.mypy]
disallow_untyped_defs = "True"
disallow_any_unimported = "True"
no_implicit_optional = "True"
check_untyped_defs = "True"
warn_return_any = "True"
warn_unused_ignores = "True"
show_error_codes = "True"
exclude = [
    '\.venv',
    '{{cookiecutter.project_name}}',
    'tests'
]
```

# deptry

[deptry](https://github.com/fpgmaas/deptry) is used to check the code for dependency issues, and it's configuration and can be edited in `pyproject.toml`.

```toml
[tool.mypy]
disallow_untyped_defs = "True"
disallow_any_unimported = "True"
no_implicit_optional = "True"
check_untyped_defs = "True"
warn_return_any = "True"
warn_unused_ignores = "True"
show_error_codes = "True"
exclude = [
    '\.venv',
    '{{cookiecutter.project_name}}',
    'tests'
]
```

## Github Actions

If `include_github_actions` is set to `"y"`, code formatting is checked
for every merge request, every merge to main, and every release.