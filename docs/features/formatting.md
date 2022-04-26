# Formatting with black and isort


[isort](https://pycqa.github.io/isort/index.html) and
[black](https://pypi.org/project/black/) are added as development
dependencies. `black` and `isort` can be used to format the code with

``` bash
make format
```

And the code style can be checked with

``` bash
make check
```

Settings for both `black` and `isort` can be edited in `pyproject.toml`. The default settings are:

```
[tool.black]
line-length = 120
include = '\.pyi?$'
target-version = ['py39']
fast = true
exclude = '''
(
  /(                        # exclude a few common directories in the
    \.git                   # root of the project
    | \.pytest_cache
    | python-venv
    | \.venv
    | build
    | dist
    | \.tox
  ))
'''

[tool.isort]
profile = "black"
```

If `include_github_actions` is set to `"y"`, code formatting is checked
for every merge request, every merge to main, and every release.
