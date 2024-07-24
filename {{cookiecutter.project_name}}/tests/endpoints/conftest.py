""" Endpoints Conftest

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - Copyright (C) 2024 PartSnap LLC
See https://fastapi.tiangolo.com/tutorial/testing/
"""

import os
import re

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

import {{cookiecutter.project_slug}}.dbms.sqlite_db as sqlite_utils
from {{cookiecutter.project_slug}}.app_builder import create_fastapi_app
from {{cookiecutter.project_slug}}.utils.typer import PSTyperRunner


@pytest.fixture(scope="session")
def db_engine():
    db_utils = sqlite_utils.SQLiteDBUtils()
    db_utils.get_database_engine(new_db=True)
    PSTyperRunner().run("--test-client db populate")
    return db_utils.get_database_engine()


@pytest.fixture(scope="session")
def fast_api_app() -> FastAPI:
    return create_fastapi_app()


@pytest.fixture()
def client(fast_api_app):
    return TestClient(app=fast_api_app, headers={"content-type": "application/json"})


@pytest.fixture()
def {{cookiecutter.project_slug}}_path():
    match = re.search(r"^.+{{cookiecutter.project_slug}}", os.getcwd())
    path = match.group(0) if match else None
    return path
