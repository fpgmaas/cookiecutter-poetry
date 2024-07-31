"""Typer helper

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- Copyright (C) 2024 PartSnap LLC
"""

import json
from typing import Any

import typer
from typer.testing import CliRunner, Result

from {{cookiecutter.project_slug}}.logging import psnap_get_logger


class PSTyperRunner:
    def __init__(self, use_test_client: bool = False):
        self.logger = psnap_get_logger("utils.PSTyperRunner")
        self.cli_runner = CliRunner()
        self.use_test_client = use_test_client
        self.result: None | Result = None

    def run(self, command: str, exit_code: int = 0) -> Result:
        from {{cookiecutter.project_slug}}.cli import cli_app

        if self.use_test_client:
            command = "--test-client " + command
        msg = f"invoking command: {command}"
        print(msg)
        self.logger.debug(msg)
        self.result = self.cli_runner.invoke(cli_app, command.split())
        if self.result.exit_code != exit_code:
            print(f">>> {command} output")
            typer.secho(self.result.output, fg=typer.colors.BRIGHT_RED)
            print("<<<")
            msg = f"{command} failed with exit code {self.result.exit_code}"
            typer.secho(f"\tFAILED '{command}'", fg=typer.colors.RED)
            raise RuntimeError(msg)
        return self.result

    def extract_json(self) -> Any:
        text = ""
        sep = None
        for line in self.result.output.splitlines():  # type: ignore[union-attr]
            if sep is None:
                if line.startswith("{"):
                    sep = "}"
                    text = text + line + "\n"
                if line.startswith("["):
                    sep = "]"
                    text = text + line + "\n"
                continue
            text = text + line + "\n"
            if line.startswith(sep):
                break
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            print(f"Could not decode JSON from '{text}'")
            raise
