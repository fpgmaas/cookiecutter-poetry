PYTHON_VERSION := {{cookiecutter.python_version}}

format: ## Format code using isort and black.
	@echo "🚀 Formatting code: Running isort and black"
	@isort .
	@black .

test-format: ## Check code formatting using isort, black, and flake8.
	@echo "🚀 Checking code formatting: Running black, isort and flake8"
	@isort --check-only --diff .
	@black --check .
	@flake8 .

test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@pytest --doctest-modules

install: ## Install the poetry environment
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry install	
	@poetry shell

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help