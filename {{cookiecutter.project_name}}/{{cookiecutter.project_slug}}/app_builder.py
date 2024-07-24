""" Application builder

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - Copyright (C) 2024 PartSnap LLC
"""

import os
import pathlib

import uvicorn
from fastapi import FastAPI, status
from fastapi.responses import FileResponse, RedirectResponse, Response

from {{cookiecutter.project_slug}}._server_doc import server_metadata
from {{cookiecutter.project_slug}}.logging import fapi_route, psnap_get_logger, psnap_set_log_level
from {{cookiecutter.project_slug}}.routers import (
    samples,
    tags_metadata,  # Endpoint Documentation
)

LOGGER = psnap_get_logger("app")


def create_fastapi_app(storage_connection: bool = False) -> FastAPI:
    """Create the fastapi app instance

    Returns
    -------
    an instance of FastAPI
    """

    LOGGER.info("creating fastapi app")
    fastapi_app = FastAPI(openapi_tags=tags_metadata, **server_metadata)  # type: ignore[arg-type]
    fastapi_app.include_router(samples.router)
    fastapi_app.include_router(fapi_route.log_router)

    LOGGER.warning("We should redirected / to /docs")

    @fastapi_app.get("/", include_in_schema=False)
    async def docs_redirect() -> RedirectResponse:
        """Redirecting to the docs page."""
        return RedirectResponse(url="/docs")

    @fastapi_app.get("/")
    async def get_status() -> Response:
        return Response(status_code=status.HTTP_200_OK, content="Got Parts?", media_type="text/plain")

    @fastapi_app.get("/favicon.ico", include_in_schema=False)
    async def favicon() -> FileResponse:
        return FileResponse(pathlib.Path(__file__).parent / "assets" / "partsnap-logo.png")

    return fastapi_app


def start_server(port: int = {{cookiecutter.port}}, log_level: str = "info", storage_connection: bool = True) -> None:
    """Starts the FastAPI server"""
    print(f"setting log level to {log_level}")
    if storage_connection is False:
        os.environ["PARTSNAP_NO_STORAGE_CONNECTION"] = "true"
    else:
        os.environ.pop("PARTSNAP_NO_STORAGE_CONNECTION", None)
    psnap_set_log_level(log_level)
    fastapi_app = create_fastapi_app(storage_connection=storage_connection)
    try:
        uvicorn.run(app=fastapi_app, host="0.0.0.0", port=port)  # noqa: S104
    except KeyboardInterrupt:
        print("Terminating")
