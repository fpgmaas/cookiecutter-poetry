PYTHON_VERSION := 3.9.7

bake: ## Run cookiecutter with default arguments.
	@echo "🚀 Running cookiecutter with default arguments."
	@cookiecutter --no-input . --overwrite-if-exists

format: ## Format code using isort and black.
	@echo "🚀 Formatting code: Running isort and black"
	@isort .
	@black .

test-format: ## Check code formatting using isort, black, and flake8.
	@echo "🚀 Checking code formatting: Running black, isort and flake8"
	@echo "Running isort..."
	@isort --check-only --diff .
	@echo "Running black..."
	@black --check .
	@echo "Running flake8..."
	@flake8 .

test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@pytest tests --doctest-modules

install: ## Install the poetry environment
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@eval "$(pyenv init --path)"
	@pyenv install -s ${PYTHON_VERSION}
	@pyenv local ${PYTHON_VERSION}
	@poetry config --local virtualenvs.in-project true
	@poetry install	
	@poetry shell

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help