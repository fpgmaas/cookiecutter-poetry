#! /usr/bin/env bash
poetry install --with dev
pip install pre-commit
pre-commit install --install-hooks
