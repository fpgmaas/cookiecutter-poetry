"""Api Conftest

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - Copyright (C) 2024 PartSnap LLC
See https://fastapi.tiangolo.com/tutorial/testing/
"""

import logging

import pytest

from {{cookiecutter.project_slug}}.dbms.sqlite_db import SQLiteDBUtils
from {{cookiecutter.project_slug}}.logging import psnap_get_logger
from {{cookiecutter.project_slug}}.utils.typer import PSTyperRunner

logger = psnap_get_logger("utils.PSTyperRunner")
logger.setLevel(logging.DEBUG)


@pytest.fixture()
def db_engine():
    db_utils = SQLiteDBUtils()
    db_utils.get_database_engine(new_db=True)
    return db_utils.get_database_engine()


@pytest.fixture
def clirunner():
    return PSTyperRunner(use_test_client=True)


@pytest.fixture()
def formatted_options(options):
    opt_str = ""
    for key, value in options.items():
        if isinstance(value, bool):
            opt_str += f" --{key}" if value else f" --no-{key}"
        else:
            opt_str += f" --{key} {value}"
    return opt_str
