# Static type checking with Mypy

If `mypy` is set to `"y"`, static type checking is added with [mypy](https://mypy.readthedocs.io/en/stable/). 
If `"github_actions` is also set to `"y"`, the code is checked with `mypy` during every workflow that is triggered.
The default configuration is as shown below, and can be edited in `pyproject.toml`.

```
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