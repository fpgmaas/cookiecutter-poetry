""" {{cookiecutter.project_slug}}

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - Copyright (C) 2024 PartSnap LLC
"""

import typer

from {{cookiecutter.project_slug}}.app_builder import start_server


def start_server_entry_point() -> None:
    """Starts the FastAPI server entry point for poetry"""
    typer.run(start_server)


if __name__ == "__main__":
    start_server_entry_point()
