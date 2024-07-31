"""Sample Type API commands

This file contains command implementation to perform CRUD operations on samples.

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- Copyright (C) 2024 PartSnap LLC
"""
# ruff: noqa: B006

from typing import Optional

import typer
from fastapi import status as http_status
from typing_extensions import Annotated

from {{cookiecutter.project_slug}}.model.sample import SampleAPIModelCreate
from {{cookiecutter.project_slug}}.utils.cli import dump_response

app = typer.Typer()


@app.command()
def get(
    ctx: typer.Context,
    sample_data: Annotated[str, typer.Argument(help="sample data")] = "",
) -> None:
    """Get information about all samples or a specific one/multiple based on sample_id or word_string."""
    response = ctx.obj["db_session"].get(f"/samples/{sample_data}")
    dump_response(response=response, success=http_status.HTTP_200_OK)


@app.command()
def create(
    ctx: typer.Context,
    word_string: str = typer.Argument(help="word string"),
    description: Optional[str] = typer.Option(default="", help="description"),
) -> None:
    new_sample = SampleAPIModelCreate(
        word_string=word_string,
        description=description,
    )
    response = ctx.obj["db_session"].post("/samples/", json=new_sample.model_dump())
    dump_response(response=response, success=http_status.HTTP_201_CREATED)


@app.command()
def delete(ctx: typer.Context, sample_id: Annotated[str, typer.Argument(help="sample_id")] = "") -> None:
    response = ctx.obj["db_session"].delete(f"/samples/{sample_id}")
    dump_response(response=response, success=http_status.HTTP_200_OK)
