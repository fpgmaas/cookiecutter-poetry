"""Health route

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- Copyright (C) 2024 PartSnap LLC
"""

import importlib.metadata
import os
from pathlib import Path

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/health", tags=["health"])
version_file = Path(__file__).parent.parent / "VERSION.txt"

# Workaround for getting the package version
# Because of the docker installation model, it appears to not be
# possible to get the version from importlib.meta data. In this case
# we export the version, via poetry, to a file generated during the
# docker build process
VERSION = "Unknown"
try:
    VERSION = importlib.metadata.distribution("parttrack").version
    print(f"Version: {VERSION} from importlib.metadata")
except importlib.metadata.PackageNotFoundError:
    if version_file.is_file():
        VERSION = version_file.open("r").read().strip()
        print(f"Version: {VERSION} from {version_file!s}")


@router.get("/")
async def get_status() -> JSONResponse:
    """return 200 OK"""

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "ok",
            "version": VERSION,
            "docker": os.getenv("PARTSNAP_IN_DOCKER", "false"),
            "environment": dict(os.environ),
        },
    )
