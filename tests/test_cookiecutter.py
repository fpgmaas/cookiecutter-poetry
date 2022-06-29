import os
import shlex
import subprocess
from contextlib import contextmanager


@contextmanager
def run_within_dir(path: str):
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


def file_contains_text(file: str, text: str) -> bool:
    return open(file, "r").read().find(text) != -1


def test_bake_project(cookies):

    result = cookies.bake(extra_context={"project_name": "my-project"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "my-project"
    assert result.project_path.is_dir()


def test_using_pytest(cookies, tmp_path):
    with run_within_dir(tmp_path):

        result = cookies.bake()

        # Assert that project was created.
        assert result.exit_code == 0
        assert result.exception is None
        assert result.project_path.name == "example-project"
        assert result.project_path.is_dir()

        # Install the poetry environment and run the tests.
        with run_within_dir(str(result.project_path)):
            subprocess.check_call(shlex.split("poetry install --no-interaction --no-root")) == 0
            subprocess.check_call(shlex.split("poetry run make test")) == 0


def test_cicd_contains_artifactory_secrets(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to": "artifactory"})
        for text in ["ARTIFACTORY_URL", "ARTIFACTORY_USERNAME", "ARTIFACTORY_PASSWORD"]:
            assert file_contains_text(f"{result.project_path}/.github/workflows/on-release-main.yml", text)
        assert file_contains_text(f"{result.project_path}/Makefile", "build-and-publish")


def test_cicd_contains_pypi_secrets(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to": "pypi"})
        assert file_contains_text(f"{result.project_path}/.github/workflows/on-release-main.yml", "PYPI_TOKEN")
        assert file_contains_text(f"{result.project_path}/Makefile", "build-and-publish")


def test_dont_publish(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to": "none"})
        assert not file_contains_text(
            f"{result.project_path}/.github/workflows/on-release-main.yml", "make build-and-publish"
        )


def test_mkdocs(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"mkdocs": "y"})
        assert file_contains_text(f"{result.project_path}/.github/workflows/on-release-main.yml", "mkdocs gh-deploy")
        assert file_contains_text(f"{result.project_path}/Makefile", "docs:")
        assert os.path.isdir(f"{result.project_path}/docs")


def test_not_mkdocs(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"mkdocs": "n"})
        assert not file_contains_text(
            f"{result.project_path}/.github/workflows/on-release-main.yml", "mkdocs gh-deploy"
        )
        assert not file_contains_text(f"{result.project_path}/Makefile", "docs:")
        assert not os.path.isdir(f"{result.project_path}/docs")


def test_tox(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"tox": "y"})
        assert file_contains_text(
            f"{result.project_path}/.github/workflows/on-release-main.yml", "poetry add tox-gh-actions"
        )
        assert file_contains_text(
            f"{result.project_path}/.github/workflows/on-merge-to-main.yml", "poetry add tox-gh-actions"
        )
        assert file_contains_text(
            f"{result.project_path}/.github/workflows/on-pull-request.yml", "poetry add tox-gh-actions"
        )
        assert os.path.isfile(f"{result.project_path}/tox.ini")
        assert file_contains_text(f"{result.project_path}/tox.ini", "[tox]")


def test_not_tox(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"tox": "n"})
        assert not file_contains_text(
            f"{result.project_path}/.github/workflows/on-release-main.yml", "poetry add tox-gh-actions"
        )
        assert not file_contains_text(f"{result.project_path}/tox.ini", "[tox]")


def test_dockerfile(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"dockerfile": "y"})
        assert os.path.isfile(f"{result.project_path}/Dockerfile")


def test_not_dockerfile(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"dockerfile": "n"})
        assert not os.path.isfile(f"{result.project_path}/Dockerfile")
