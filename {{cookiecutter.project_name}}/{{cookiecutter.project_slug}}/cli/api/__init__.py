"""CLI for API interface

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- Copyright (C) 2024 PartSnap LLC
"""

import typer

import {{cookiecutter.project_slug}}.cli.api.samples as samples

api_app = typer.Typer(no_args_is_help=True)
api_app.add_typer(samples.app, name="samples", help="manage samples", no_args_is_help=True)
