#! /usr/bin/env bash
poetry install --with dev
poetry run pre-commit install --install-hooks
