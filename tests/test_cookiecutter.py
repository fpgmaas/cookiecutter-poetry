from contextlib import contextmanager
from cookiecutter.utils import rmtree
import subprocess
import shlex
import os
import pytest

    
def test_bake_project(cookies):
    result = cookies.bake(extra_context={"project_slug": "helloworld"})

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "helloworld"
    assert result.project_path.is_dir()

    # The `project` attribute is deprecated
    assert result.project.basename == "helloworld"
    assert result.project.isdir()

@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)

def run_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the exit status
    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))

def test_using_pytest(cookies, tmpdir):
    result = cookies.bake(extra_context={"project_slug": "helloworld"})
    
    assert result.project_path.name == "helloworld"
    assert result.project_path.is_dir()

    test_file_path = result.project.join(
        'tests/test_foo.py'
    )
    lines = test_file_path.readlines()
    assert "import pytest" in ''.join(lines)
    # Test the new pytest target
    run_inside_dir('make install', str(result.project))
    run_inside_dir('pytest', str(result.project)) == 0