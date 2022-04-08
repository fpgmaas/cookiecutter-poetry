import pytest
from {{cookiecutter.module_name}}.foo import foo


def test_foo():
    assert foo() == "foo"