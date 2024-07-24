""" CLI for Database interface

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - Copyright (C) 2024 PartSnap LLC
"""

import os
from copy import copy
from pathlib import Path
from typing import Any, Dict

import typer
from omegaconf import OmegaConf as oconf
from typing_extensions import Annotated

from {{cookiecutter.project_slug}}.dbms.sqlite_db import SQLiteDBUtils
from {{cookiecutter.project_slug}}.utils.typer import PSTyperRunner
from {{cookiecutter.project_slug}}.model.sample import SampleAPIModelCreate


db_app = typer.Typer()

default_data_dir = Path(__file__).parent.parent.parent / "data"


@db_app.command()
def clear() -> None:
    sqlite_utils = SQLiteDBUtils(echo=False)
    sqlite_utils.backup_db()
    typer.secho(f"\tcurrent db backed up as {sqlite_utils.db_backup_file_path}", fg=typer.colors.GREEN)
    sqlite_utils.get_database_engine(new_db=True)
    typer.secho("database is cleared", fg=typer.colors.GREEN)


{% raw -%}
def format_command(cmd_template: str, data: Dict[str, Any]) -> str:
    """Formats the command template and data

    Parameters
    ----------
    cmd_template: A template in the form <litteral> {{field_name}} --field-name {{field_name}}
    data: the data to inject in the template

    Returns
    -------
    cmd: str the formatted command
    """
    cmd = cmd_template
    for key, value in data.items():
        if key.startswith("is_"):
            key = key.replace("is_", "")
        if isinstance(value, bool):
            value = f"--{key}" if value else f"--no-{key}"
        if value is None or value == "":
            value = ""
            cmd = cmd.replace(f"--{key}", "")
            # option have dashes instead of underscores
            cmd = cmd.replace(f"--{key.replace('_', '-')}", "")

        cmd = cmd.replace(f"{{{{{key}}}}}", str(value))
    return cmd
{% endraw -%}


def run_command(runner: PSTyperRunner, validator_cls: Any, entity: str, entity_data: Any) -> None:
    cmd_template = entity_data[entity]["cmd"]
    typer.secho(f"\tcreating {entity}", fg=typer.colors.BRIGHT_BLUE)
    for data in entity_data[entity]["data"]:
        # Validate the data. While we accept name as Ids, the model only
        # accepts integer. So we use the following to bypass Id validation.
        tmp = copy(data)
        for field in tmp:
            if field.endswith("_id"):
                tmp[field] = 0  # stora a random ID
        tmp = validator_cls(**tmp).model_dump()
        tmp.update(data)

        cmd = format_command(cmd_template=cmd_template, data=tmp)
        try:
            runner.run("api " + cmd)
        except RuntimeError as error:
            typer.secho(runner.result.output, fg=typer.colors.BRIGHT_RED)  # type: ignore[union-attr]
            raise typer.Exit(1) from error
        typer.secho(runner.result.output, fg=typer.colors.BRIGHT_BLUE)  # type: ignore[union-attr]
        typer.secho(f"\tOK '{cmd}'", fg=typer.colors.GREEN)


@db_app.command()
def populate(
    ctx: typer.Context,
    model_path: Annotated[Path, typer.Argument(dir_okay=True, file_okay=False, exists=True)] = default_data_dir,
) -> None:
    runner = PSTyperRunner(use_test_client=ctx.obj["test_client"])
    typer.secho(f"searching {model_path}", fg=typer.colors.BRIGHT_BLUE)
    model_path = model_path.absolute()
    yaml_models = []
    for root, _, files in os.walk(model_path):
        search_dir = Path(root)
        for file in files:
            file_path = search_dir / Path(file)
            if file.endswith(".yml") or file.endswith(".yaml"):
                typer.secho(f"\tloading model file {file_path}", fg=typer.colors.BRIGHT_BLUE)
                yaml_models.append(oconf.load(file_path))
    all_models = oconf.merge(*yaml_models)
    oconf.resolve(all_models)
    run_command(entity="samples", validator_cls=SampleAPIModelCreate, runner=runner, entity_data=all_models)
