"""Logging routes

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- Copyright (C) 2024 PartSnap LLC
"""

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

import {{cookiecutter.project_slug}}.logging as psnap_log
from {{cookiecutter.project_slug}}.routers.api_models import ErrorMessageModel, StatusModel

log_router = APIRouter(prefix="/logging", tags=["logging"])


@log_router.post(
    "/level",
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorMessageModel},
        status.HTTP_200_OK: {"model": StatusModel},
    },
)
def post_log_level(level_id: int | str, logger_name: str | None = None) -> JSONResponse:
    try:
        logger_name = logger_name if logger_name else ""
        level_id = psnap_log.psnap_set_log_level(level=level_id, name=logger_name)
    except ValueError as error:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail": str(error)})
    return JSONResponse(content={"status": f"logger {logger_name} set to {level_id}"})


@log_router.get("/loggers")
def get_log_level() -> list[str]:
    return psnap_log.psnap_get_logger_names()
