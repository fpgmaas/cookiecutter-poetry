# Compatibility testing with Tox

If `tox` is set to `"y"` project uses [Tox](https://tox.wiki/en/latest/)
to test compatibility with multiple Python versions. By default, the
project is tested with Python `3.8`, `3.9`, and `3.10`. Testing
is done automatically in the CI/CD pipeline on every pull request, merge
to main, and on each release.

If you want to add more Python versions you can simply add them to
`tox.ini` and to the separate workflows in `.github`.
