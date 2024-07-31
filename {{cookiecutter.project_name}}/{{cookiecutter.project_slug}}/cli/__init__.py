"""CLI

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- Copyright (C) 2024 PartSnap LLC
"""

import os

import typer

from {{cookiecutter.project_slug}}.app_builder import create_fastapi_app
from {{cookiecutter.project_slug}}.cli.api import api_app
from {{cookiecutter.project_slug}}.cli.db import db_app
from {{cookiecutter.project_slug}}.logging import psnap_set_log_level
from {{cookiecutter.project_slug}}.utils.session import PSServerSession
from {{cookiecutter.project_slug}}.utils.test_client import PSTestClient

cli_app = typer.Typer(no_args_is_help=True)
cli_app.add_typer(api_app, name="api", help="Restful API command line interface", no_args_is_help=True)
cli_app.add_typer(db_app, name="db", help="Database utilities", no_args_is_help=True)


@cli_app.callback()
def main(
    ctx: typer.Context,
    port: int = typer.Option({{cookiecutter.port}}, envvar="{{cookiecutter.project_caps}}_PORT"),
    host: str = typer.Option("127.0.0.1", envvar="{{cookiecutter.project_caps}}_HOST"),
    log_level: str = typer.Option("error"),
    storage_connection: bool = typer.Option(True),
    test_client: bool = typer.Option(False),
) -> None:
    """
    Manage users in the awesome CLI app.
    """
    if ctx.obj is None:
        ctx.obj = {}
    if storage_connection is False:
        if test_client is False:
            typer.secho(
                "WARNING Disabling storage connection has not effect in non test client mode", fg=typer.colors.YELLOW
            )
        else:
            typer.secho("WARNING Storage connection is disabled", fg=typer.colors.YELLOW)
            os.environ["PARTSNAP_NO_STORAGE_CONNECTION"] = "true"

    psnap_set_log_level(level=log_level)
    if test_client is True:
        typer.secho("Using Test Client", fg=typer.colors.YELLOW)
        fast_api_app = create_fastapi_app()
        ctx.obj["db_session"] = PSTestClient(app=fast_api_app, headers={"content-type": "application/json"})
        ctx.obj["test_client"] = True
    else:
        typer.secho(f"Using Request hostname={host}, port={port}", fg=typer.colors.YELLOW)
        ctx.obj["db_session"] = PSServerSession(hostname=host, port=port)
        ctx.obj["test_client"] = False


if __name__ == "__main__":
    cli_app()
