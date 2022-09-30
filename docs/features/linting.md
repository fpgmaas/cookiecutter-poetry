# Linting and code quality

Code can be linted and quality-checked with the command

``` bash
make check
```

Note that this requires the pre-commit hooks to be installed. 

This command will run the following tools:

## isort

[isort](https://pycqa.github.io/isort/index.html) is run to sort the imports and it is configured through `pyproject.toml`:

```toml
[tool.isort]
profile = "black"
```

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

## flake8

[flake8](https://flake8.pycqa.org/en/latest/) is used to check the code style, and it is configured through `tox.ini`:

```
[flake8]
per-file-ignores = __init__.py:F401
# PEP-8 The following are ignored:
# E731 do not assign a lambda expression, use a def
# E203 whitespace before ':'
# E501 line too long
# W503 line break before binary operator
# W605 invalid escape sequence
ignore = E731, E203, E501, W503, W605
exclude =
    .git,
    __pycache__,
    docs/source/conf.py,
    old,
    build,
    dist,
    .venv,
max-complexity = 10
max-line-length = 120
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