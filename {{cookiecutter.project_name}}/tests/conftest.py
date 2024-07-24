""" Conftest for tests

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - Copyright (C) 2024 PartSnap LLC
See https://fastapi.tiangolo.com/tutorial/testing/
"""

import logging
import os

import pytest
from sqlmodel import Session

import {{cookiecutter.project_slug}}.dbms.sqlite_db as sqlite_utils
from {{cookiecutter.project_slug}}.logging import psnap_set_log_level
from {{cookiecutter.project_slug}}.model.sample import SampleAPIModelCreate, SampleDBModel

# ps_base_logger.setLevel(logging.DEBUG)
psnap_set_log_level(logging.ERROR, "dbms.SQLiteDBUtils")


def pytest_sessionstart():
    os.environ["{{cookiecutter.project_caps}}_USE_TEST_CLIENT"] = str(True)
    db_utils = sqlite_utils.SQLiteDBUtils()
    db_utils.backup_db()


def pytest_sessionfinish():
    db_utils = sqlite_utils.SQLiteDBUtils()
    db_utils.restore_db()


@pytest.fixture()
def db_session(db_engine):
    with Session(bind=db_engine) as db_session:
        yield db_session


@pytest.fixture()
def db_sample(db_session):
    sample_model = SampleAPIModelCreate(word_string="Hello there", description="this is two words")

    sample_db = SampleDBModel.create(db_session=db_session, sample_model=sample_model)
    yield sample_db
    SampleDBModel.delete(db_session=db_session, sample_id=sample_db.id)
