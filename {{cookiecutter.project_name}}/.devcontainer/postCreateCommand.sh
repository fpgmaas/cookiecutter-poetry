#! /usr/bin/env bash

# Install Dependencies
poetry install --with dev

# Check if the repo is already initialized
if [ ! -d ".git" ]; then
    # Initialize the repo
    git init -b main
    git add .
    # Run pre-commit hooks on all files
    poetry run pre-commit install --install-hooks
    poetry run pre-commit run --all-files
    # Stage modified files
    git add .
else
    # Install pre-commit hooks
    poetry run pre-commit install --install-hooks
fi
