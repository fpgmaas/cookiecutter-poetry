"""CLI Utility functions

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- Copyright (C) 2024 PartSnap LLC
"""

import json

import typer
from requests import Response


def dump_response(response: Response, error_msg: str = "", success: int = 200) -> None:
    """Dump response to stdout

    Takes a response like object, check its status code against the expected one.
    Either prints the response content (on success) or raises an exception

    Parameters
    ----------
    response: A response object
    error_msg: any customer error message to print on error
    success: http status code to check against
    """
    json_response = response.json()
    try:
        reason = json_response.get("detail", response.reason) if isinstance(json_response, dict) else response.reason
    except AttributeError:
        reason = "unknown reason"

    if response.status_code != success:
        typer.secho(f"Error[{response.status_code}] {error_msg}  reason={reason}", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    if json_response:
        typer.secho(json.dumps(response.json(), indent=2), fg=typer.colors.GREEN)
    typer.secho(f"{response.status_code} {reason}", fg=typer.colors.GREEN)
