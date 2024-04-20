""" {{cookiecutter.project_slug}}

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- License: {{cookiecutter.license_released_under}}
"""
import pytest
import getpass
from {{cookiecutter.project_slug}}.main import hello

@pytest.fixture()
def name() -> str:
    return getpass.getuser()

def test_foo(name: str) -> None:
    assert hello() == f"Hello {name}!"
