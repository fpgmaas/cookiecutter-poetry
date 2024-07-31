TMP_DIR="./tmp"

.PHONY: bake
bake: ## bake without inputs and overwrite if exists.
	@cookiecutter --no-input . --overwrite-if-exists

.PHONY: bake-with-inputs
bake-with-inputs: ## bake with inputs and overwrite if exists.
	@cookiecutter . --overwrite-if-exists

.PHONY: bake-and-test-deploy
bake-and-test-deploy: ## For quick publishing to cookiecutter-poetry-example to test GH Actions
	@rm -rf cookiecutter-poetry-example || true
	@cookiecutter --no-input . --overwrite-if-exists \
		author="Florian Maas" \
		email="fpgmaas@gmail.com" \
		github_author_handle=fpgmaas \
		project_name=cookiecutter-poetry-example \
		project_slug=cookiecutter_poetry_example
	@cd cookiecutter-poetry-example; poetry install && \
		git init -b main && \
		git add . && \
		poetry run pre-commit install && \
		poetry run pre-commit run -a || true && \
		git add . && \
		poetry run pre-commit run -a || true && \
		git add . && \
		git commit -m "init commit" && \
		git remote add origin git@github.com:fpgmaas/cookiecutter-poetry-example.git && \
		git push -f origin main


.PHONY: install
install: ## Install the poetry environment
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry install
	@poetry shell

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry check --lock"
	@poetry check --lock
	@echo "🚀 Linting code: Running pre-commit"
	@poetry run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@poetry run mypy
	@echo "🚀 Checking for obsolete dependencies: Running deptry"
	@poetry run deptry .

.PHONY: clean-tox
clean-tox: ## deleting tox directory
	@echo "🚀 Deleting Tox folder"
	@rm -rf .tox

.PHONY: tox
tox: ## running test in tox
	@echo "🚀 Testing code: Running Tox"
	@poetry run tox --recreate

.PHONY: test
test: ## Test the code with pytest.
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest --cov --cov-config=pyproject.toml --cov-report=xml tests

.PHONY: build
build: clean-build ## Build wheel file using poetry
	@echo "🚀 Creating wheel file"
	@poetry build

.PHONY: clean-build
clean-build: ## clean build artifacts
	@rm -rf dist

.PHONY: publish
publish: ## publish a release to pypi.
	@echo "🚀 Publishing: Dry run."
	@poetry config pypi-token.pypi $(PYPI_TOKEN)
	@poetry publish --dry-run
	@echo "🚀 Publishing."
	@poetry publish

.PHONY: build-and-publish
build-and-publish: build publish ## Build and publish.

.PHONY: docs-test
docs-test: full-monty ## Test if documentation can be built without warnings or errors
	@poetry run mkdocs build -s

.PHONY: docs
docs: ## Build and serve the documentation
	@poetry run mkdocs serve

.PHONY: 'full-monty'
full-monty: ## Test project generation
	@test -e $(TMP_DIR) || mkdir $(TMP_DIR)
	@echo 'cookcutter -f --output $(TMP_DIR)'
	@echo 'cd $(TMP_DIR) && git init .'
	@echo 'cd $(TMP_DIR) && git add .'
	@echo 'cd $(TMP_DIR) && make install'
	@echo 'cd $(TMP_DIR) && make check'
	@echo 'cd $(TMP_DIR) && make docs-test test tox'
	@echo 'cd $(TMP_DIR) && make docker-build'
	@echo 'cd $(TMP_DIR) && make docker-start'
	@echo 'sleep 5'
	@echo 'curl -f -X GET http://localhost:8080/health'
	@echo 'cd $(TMP_DIR) && make docker-stop'
	@echo 'cd $(TMP_DIR) && git commit -am "inial commit"'
	rm -rf $(TMP_DIR)

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
