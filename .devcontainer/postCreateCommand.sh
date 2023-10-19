#! /usr/bin/env bash

# Install Dependencies
poetry install --with dev

# Install pre-commit hooks
poetry run pre-commit install --install-hooks
