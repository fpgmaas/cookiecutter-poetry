---
title: CI/CD with Github actions
---

when `include_github_actions` is set to `"y"`, a `.github` directory is
added with the following structure:

    .github
    ├── workflows
    ├─── run-checks
    │    └── action.yml    
    ├─── setup-poetry-env
    │    └── action.yml         
    ├── on-merge-to-main.yml
    ├── on-pull-request.yml          
    └── on-release-main.yml

`on-merge-to-main.yml` and `on-pull-request.yml` are identical except
for their trigger conditions; the first is run whenever a new commit is
made to `main` (which should
[only](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/about-protected-branches)
happen through merge requests, hence the name), and the latter is run
whenever a pull request is opened or updated. They call the `action.yml`
files to set-up the environment, run the tests, and check the code
formatting.

`on-release-main.yml` does all of the former whenever a new release is
made on the `main` branch. In addition, `on-release-main.yml` also
publishes the project to Pypi or Artifactory if `publish_to` is set to
`"pypi"` or `"artifactory"`, and it builds and deploys the documentation
if `sphinx_docs` is set to `"y"`. To learn more about these features,
see `Releasing to Pypi or Artifactory <./releasing>`{.interpreted-text
role="doc"} and `Documentation with Sphinx
<./sphinx>`{.interpreted-text role="doc"}

Additionally, all workflows check for compatibility with multiple Python
versions if `tox` is set to `"y"`.

## Example CI/CD Pipeline

[![Example pipeline](https://raw.githubusercontent.com/fpgmaas/cookiecutter-poetry/main/static/images/pipeline.png)](https://raw.githubusercontent.com/fpgmaas/cookiecutter-poetry/main/static/images/pipeline.png)