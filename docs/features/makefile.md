---
title: Makefile
---

The generated repository will have a `Makefile` available. A list of all
available commands that are available can be obtained by running
`make help` in the terminal. Initially, the following commands are
available:

```
install              Install the poetry environment
format               Format code using isort and black.
lint                 Check code formatting using isort and black.
test                 Test the code with pytest
build                Build wheel file using poetry
clean-build          clean build artifacts
publish              publish a release to pypi.
build-and-publish    Build and publish.
docs-generate        convert docstrings to docs
docs-build           Build the docs
docs-open            Open the docs in the browser
docs                 Build and serve the documentation
docs-test            Test if the documentation can be generated and built without errors.
```
