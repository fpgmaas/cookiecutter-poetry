"""CLI for API interface

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- Copyright (C) 2024 PartSnap LLC
"""

from fastapi import Depends

from .database import ps_db_session

basic_dependencies = [Depends(ps_db_session)]
