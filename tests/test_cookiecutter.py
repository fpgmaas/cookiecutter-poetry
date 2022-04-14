import os
import shlex
import subprocess

from contextlib import contextmanager

@contextmanager
def run_within_dir(path: str):
    oldpwd=os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)

def file_contains_text(file: str, text: str) -> bool:
        return open(file, 'r').read().find(text) != -1


def test_bake_project(cookies):

    result = cookies.bake(extra_context={"project_name": "my-project"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "my-project"
    assert result.project_path.is_dir()


def test_using_pytest(cookies, tmpdir):

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


def test_cicd_contains_artifactory_secrets(cookies):
    result = cookies.bake(extra_context={"publish_to": "artifactory"})
    for text in ['ARTIFACTORY_URL', 'ARTIFACTORY_USERNAME','ARTIFACTORY_PASSWORD']:
        assert file_contains_text(f'./{result.project_path.name}/.github/workflows/on-release-main.yml', text)
    assert file_contains_text(f'./{result.project_path.name}/Makefile', 'build-and-publish')

def test_cicd_contains_pypi_secrets(cookies):
    result = cookies.bake(extra_context={"publish_to": "pypi"})
    assert file_contains_text(f'./{result.project_path.name}/.github/workflows/on-release-main.yml', 'PYPI_TOKEN')
    assert file_contains_text(f'./{result.project_path.name}/Makefile', 'build-and-publish')


def test_dont_publish(cookies):
    result = cookies.bake(extra_context={"publish_to": "none"})
    assert not file_contains_text(f'./{result.project_path.name}/.github/workflows/on-release-main.yml', 'make build-and-publish')