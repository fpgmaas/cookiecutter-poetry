import os
import shlex
import subprocess


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
    os.chdir(str(result.project_path))
    subprocess.check_call(shlex.split("poetry install --no-interaction --no-root")) == 0
    subprocess.check_call(shlex.split("poetry run make test")) == 0
