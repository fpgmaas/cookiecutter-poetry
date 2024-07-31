"""PartSnap Base Model

Whenever a record is created or updated, it shall be stamped
with the date and time of the transaction as well as with the
information related to the user performing such transaction.

Each model should derive from this class to add the required
database fields. Stamping is automatically handled by the
mixin in {{cookiecutter.project_slug}}.model.mixins

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- Copyright (C) 2024 PartSnap LLC
"""

from typing import Optional

from sqlmodel import Field, SQLModel

__all__ = ["PartSnapBaseModel"]


class PartSnapBaseModel(SQLModel):
    created_by: Optional[int] = Field(description="record was created by", default=None, nullable=True)
    updated_by: Optional[int] = Field(description="record was updated by", default=None, nullable=True)
