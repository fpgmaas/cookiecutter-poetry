""" Sample Data Model

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - Copyright (C) 2024 PartSnap LLC
"""

from typing import Optional

from pydantic import ConfigDict
from sqlmodel import Field, SQLModel

from {{cookiecutter.project_slug}}.api_model.common import PartSnapBaseModel

__all__ = ["SampleAPIModelCreate", "SampleAPIModelRead"]


class SampleBaseModel(SQLModel):
    model_config = ConfigDict(strict=True)  # type: ignore[assignment]
    word_string: str = Field(nullable=False)
    description: Optional[str | None] = Field(default="", description="sample description")

    def __str__(self) -> str:
        return f"sample {self.description}"


class SampleAPIModelCreate(SampleBaseModel):
    """Sample Model for creating new records"""


class SampleAPIModelUpdate(SampleBaseModel):
    """Sample for updating new records"""


class SampleAPIModelRead(SampleBaseModel, PartSnapBaseModel):
    """Sample Model for reading existing records"""

    id: Optional[int] = Field(default=None, primary_key=True, description="Sample primary key", nullable=True)
