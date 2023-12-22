# Justfile

The generated repository will have a `justfile` available. A list of all
available commands that are available can be obtained by running
`just` in the terminal. Initially, if all features are selected, the following commands are
available:

```

setup-project-no-github: # Initial setup of project, without any commit to GitHub
setup-project            # Initial setup of project, including an initial push to GitHub
install                  # Install the poetry environment and install the pre-commit hooks
check                    # Run code quality tools.
test                     # Test the code with pytest.
build                    # Build wheel file using poetry
clean-build              # clean build artifacts
publish                  # publish a release to pypi.
build-and-publish        # Build and publish.
docs-test                # Test if documentation can be built without warnings or errors
docs                     # Build and serve the documentation
```
