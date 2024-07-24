""" Datbase dependency

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - Copyright (C) 2024 PartSnap LLC
"""

import sqlalchemy

from {{cookiecutter.project_slug}}.dbms.sqlite_db import SQLiteDBUtils
from {{cookiecutter.project_slug}}.logging import psnap_get_logger


def ps_db_session() -> sqlalchemy.Engine:
    logger = psnap_get_logger("dependencies.database")
    engine = SQLiteDBUtils().get_database_engine()
    logger.debug(f"[ps_db_session] return engine {engine}")
    return engine
