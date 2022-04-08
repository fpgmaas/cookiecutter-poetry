from contextlib import contextmanager
from cookiecutter.utils import rmtree
import subprocess
import shlex
import os
import pytest

    
def test_bake_project(cookies):
    
    result = cookies.bake(extra_context={"project_slug": "my-project"})

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
    subprocess.check_call(shlex.split('make install')) == 0
    subprocess.check_call(shlex.split('make test')) == 0