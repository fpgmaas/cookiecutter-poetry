import os
import shlex
import subprocess
from contextlib import contextmanager

from cookiecutter_poetry.cli import main


@contextmanager
def run_within_dir(path: str):
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


def test_main(mocker, tmp_path):
    # Mock os.system to avoid actually running the Cookiecutter CLI
    mock_os_system = mocker.patch("os.system")

    # Mock os.path.dirname and os.path.abspath to control the paths used in the test
    mocker.patch("os.path.dirname", return_value=str(tmp_path))
    mocker.patch("os.path.abspath", return_value=str(tmp_path / "parent"))

    main()

    mock_os_system.assert_called_once_with(f"cookiecutter {tmp_path / 'parent'}")


def file_contains_text(file: str, text: str) -> bool:
    with open(file) as f:
        return f.read().find(text) != -1


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
            assert subprocess.check_call(shlex.split("poetry install --no-interaction")) == 0
            assert subprocess.check_call(shlex.split("poetry run make test")) == 0


def test_devcontainer(cookies, tmp_path):
    """Test that the devcontainer files are created when devcontainer=y"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"devcontainer": "y"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/.devcontainer/devcontainer.json")
        assert os.path.isfile(f"{result.project_path}/.devcontainer/postCreateCommand.sh")


def test_not_devcontainer(cookies, tmp_path):
    """Test that the devcontainer files are not created when devcontainer=n"""
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"devcontainer": "n"})
        assert result.exit_code == 0
        assert not os.path.isfile(f"{result.project_path}/.devcontainer/devcontainer.json")
        assert not os.path.isfile(f"{result.project_path}/.devcontainer/postCreateCommand.sh")


def test_cicd_contains_artifactory_secrets(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to": "artifactory"})
        assert result.exit_code == 0
        for text in ["ARTIFACTORY_URL", "ARTIFACTORY_USERNAME", "ARTIFACTORY_PASSWORD"]:
            assert file_contains_text(f"{result.project_path}/.github/workflows/on-release-main.yml", text)
        assert file_contains_text(f"{result.project_path}/Makefile", "build-and-publish")


def test_cicd_contains_pypi_secrets(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to": "pypi"})
        assert result.exit_code == 0
        assert file_contains_text(f"{result.project_path}/.github/workflows/on-release-main.yml", "PYPI_TOKEN")
        assert file_contains_text(f"{result.project_path}/Makefile", "build-and-publish")


def test_dont_publish(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"publish_to": "none"})
        assert result.exit_code == 0
        assert not file_contains_text(
            f"{result.project_path}/.github/workflows/on-release-main.yml", "make build-and-publish"
        )


def test_mkdocs(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake()
        assert result.exit_code == 0
        assert file_contains_text(f"{result.project_path}/.github/workflows/on-release-main.yml", "mkdocs gh-deploy")
        assert file_contains_text(f"{result.project_path}/Makefile", "docs:")
        assert os.path.isdir(f"{result.project_path}/docs")


def test_tox(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake()
        assert result.exit_code == 0
        assert file_contains_text(f"{result.project_path}/.github/workflows/main.yml", "pip install tox tox-gh-actions")
        assert os.path.isfile(f"{result.project_path}/tox.ini")
        assert file_contains_text(f"{result.project_path}/tox.ini", "[tox]")


def test_dockerfile(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake()
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/Dockerfile")


def test_database(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"project_name": "my-project", "database": "y"})
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/myproject/cli/db/__init__.py")
        assert os.path.isfile(f"{result.project_path}/myproject/model/db_crud.py")
        assert not os.path.isfile(f"{result.project_path}/myproject/foo.py")
        assert not os.path.isfile(f"{result.project_path}/tests/test_foo.py")


def test_not_database(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake(extra_context={"project_name": "my-project", "database": "n"})
        assert result.exit_code == 0
        assert not os.path.isfile(f"{result.project_path}/myproject/cli/db/__init__.py")
        assert not os.path.isfile(f"{result.project_path}/myproject/model/db_crud.py")
        assert not os.path.isfile(f"{result.project_path}/tests/endpoints/test_samples.py")
        assert os.path.isfile(f"{result.project_path}/myproject/foo.py")
        assert os.path.isfile(f"{result.project_path}/tests/test_foo.py")


def test_codecov(cookies, tmp_path):
    with run_within_dir(tmp_path):
        result = cookies.bake()
        assert result.exit_code == 0
        assert os.path.isfile(f"{result.project_path}/codecov.yaml")
        assert os.path.isfile(f"{result.project_path}/.github/workflows/validate-codecov-config.yml")
