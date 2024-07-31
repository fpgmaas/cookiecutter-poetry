"""Api Model Routes

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- Copyright (C) 2024 PartSnap LLC
"""

from typing import Optional

from pydantic import ConfigDict
from sqlmodel import Field, SQLModel


class ErrorMessageModel(SQLModel):
    model_config = ConfigDict(strict=True)  # type: ignore[assignment]
    detail: str = Field(description="error message detail")


class StatusModel(SQLModel):
    """Status information"""

    model_config = ConfigDict(strict=True)  # type: ignore[assignment]
    status: str = Field(description="status message detail")


class ObjStorePresignedURL(SQLModel):
    model_config = ConfigDict(strict=True)  # type: ignore[assignment]
    url: str = Field(description="presigned URL valid for 5 minutes")
    filename: str = Field(description="filename")
    command: Optional[str] = Field(description="curl command to download label", default="")
