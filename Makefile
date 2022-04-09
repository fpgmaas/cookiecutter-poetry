PYTHON_VERSION := 3.9.7

bake: ## bake without inputs and overwrite if exists.
	@cookiecutter --no-input . --overwrite-if-exists

bake-with-inputs: ## bake with inputs and overwrite if exists.
	@cookiecutter . --overwrite-if-exists

install: ## Install the poetry environment
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry install	
	@poetry shell

format: ## Format code using isort and black.
	@echo "🚀 Formatting code: Running isort and black"
	@isort .
	@black .

lint: ## Check code formatting using isort, black, and flake8.
	@echo "🚀 Checking code formatting: Running black, isort and flake8"
	@isort --check-only --diff .
	@black --check .
	@flake8 .

test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@pytest --doctest-modules tests

docs-test: ## Test Sphinx documentation.
	@sphinx-build docs docs/_build -W --keep-going 

docs-clean: ## Clean the docs/_build folder 
	@rm -r docs/_build

docs-build: ## Build the documentation
	@sphinx-build docs docs/_build

docs-open: ## Open the documentation
	@open docs/_build/index.html

docs: docs-clean docs-build docs-open ## Build and open the documentation

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help