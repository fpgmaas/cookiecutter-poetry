---
title: Formatting
---

[isort](https://pycqa.github.io/isort/index.html) and
[black](https://pypi.org/project/black/) are added as development
dependencies. `black` and `isort` can be used to format the code with

``` bash
make format
```

And the code style can be checked with

``` bash
make lint
```

If `include_github_actions` is set to `"y"`, code formatting is checked
for every merge request, every merge to main, and every release.
