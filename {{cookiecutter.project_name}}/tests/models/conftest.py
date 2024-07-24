""" Models Conftest

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - Copyright (C) 2024 PartSnap LLC
See https://fastapi.tiangolo.com/tutorial/testing/
"""

import pytest
from sqlmodel import SQLModel, create_engine

from {{cookiecutter.project_slug}}.dbms.sqlite_db import SQLiteDBUtils


@pytest.fixture()
def db_engine():
    db_file = SQLiteDBUtils().db_dir / "model_test.db"
    if db_file.exists():
        db_file.unlink()
    driver = f"sqlite:///{db_file!s}"
    engine = create_engine(driver, echo=False)
    SQLModel.metadata.create_all(engine)
    return engine
