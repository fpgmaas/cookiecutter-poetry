---
title: Documentation with Sphinx
---

If `sphinx_docs` is set to `"y"`, documentation of your project is
automatically added using
[sphinx](https://www.sphinx-doc.org/en/master/). Next to that, if
`"include_github_actions"` is set to `"y"`, the documentation is
automatically deployed to your `gh-pages` branch, and made available at
`https://<github_handle>.github.io/<project_name>/`.

To view the documentation locally, simply run

``` bash
make docs
```

This command will generate, build and directly open your documentation
in the browser.

# Documenting docstrings

The generated project uses `sphinx-apidoc` to automatically convert all
your docstrings into legible documentation. By default, the project is
configured to work with
[google](https://google.github.io/styleguide/pyguide.html) style
docstrings.

An example of a Google style docstring:

``` python
def function_with_pep484_type_annotations(param1: int, param2: str) -> bool:
"""Example function with PEP 484 type annotations.

Args:
    param1: The first parameter.
    param2: The second parameter.

Returns:
    The return value. True for success, False otherwise.
```

For more examples, see
[here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).
