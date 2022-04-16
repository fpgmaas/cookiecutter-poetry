install: ## Install the poetry environment
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry install	
	@poetry shell

format: ## Format code using isort and black.
	@echo "🚀 Formatting code: Running isort and black"
	@isort .
	@black .

lint: ## Check code formatting using isort and black.
	@echo "🚀 Checking code formatting: Running isort and black"
	@isort --check-only --diff .
	@black --check .

test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@pytest --doctest-modules

build: clean-build ## Build wheel file using poetry
	@echo "🚀 Creating wheel file"
	@poetry build

clean-build: ## clean build artifacts
	@rm -rf dist

{%- if cookiecutter.publish_to == "pypi"%}

publish: ## publish a release to pypi.
	@echo "🚀 Publishing: Dry run."
	@poetry config pypi-token.pypi $(PYPI_TOKEN)
	@poetry publish --dry-run
	@echo "🚀 Publishing."
	@poetry publish

build-and-publish: build publish ## Build and publish.
{%- elif cookiecutter.publish_to == "artifactory" %}

publish: ## Publish to the Artifactory repository using poetry. Requires ARTIFACTORY_TOKEN for DPS-FF-ILO to be set.
	@echo "🚀 Publishing: Dry run."
	@poetry config repositories.artifactory $(ARTIFACTORY_URL)
	@poetry publish --repository artifactory --username $(ARTIFACTORY_USERNAME) --password $(ARTIFACTORY_PASSWORD) --dry-run
	@echo "🚀 Publishing."
	@poetry publish --repository artifactory --username $(ARTIFACTORY_USERNAME) --password $(ARTIFACTORY_PASSWORD)

build-and-publish: build publish ## Build and publish.
{%- endif%}

{%- if cookiecutter.mkdocs == "y" %}

docs-test: ## Test if documentation can be built without warnings or errors
	@mkdocs build -s

docs: ## Build and serve the documentation
	@mkdocs serve

.PHONY: docs
{%- endif %}

.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help