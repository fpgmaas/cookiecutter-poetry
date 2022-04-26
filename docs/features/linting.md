# Linting with flake8

[flake8](https://flake8.pycqa.org/en/latest/) is added as development
dependency. The settings for `flake8` can be found in `tox.ini`, and they are defaulted to:

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

If `include_github_actions` is set to `"y"`, code linting is checked with `flake8`
for every merge request, every merge to main, and every release.
