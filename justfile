default:
  @just --list --unsorted

# bake without inputs and overwrite if exists.
bake:
	@cookiecutter --no-input . --overwrite-if-exists

# bake with inputs and overwrite if exists.
bake-with-inputs:
	@cookiecutter . --overwrite-if-exists

# For quick publishing to cookiecutter-poetry-example to test GH Actions
bake-and-test-deploy:
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


# Install the poetry environment
install:
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry install
	@poetry shell

# Run code quality tools.
check:
	@echo "🚀 Checking Poetry lock file consistency with 'pyproject.toml': Running poetry lock --check"
	@poetry check --lock
	@echo "🚀 Linting code: Running pre-commit"
	@poetry run pre-commit run -a
	@echo "🚀 Linting with ruff"
	@poetry run ruff hooks tests cookiecutter_poetry --config pyproject.toml
	@echo "🚀 Static type checking: Running mypy"
	@poetry run mypy
	@echo "🚀 Checking for obsolete dependencies: Running deptry"
	@poetry run deptry .

# Test the code with pytest.
test:
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest --cov --cov-config=pyproject.toml --cov-report=xml tests

# Build wheel file using poetry
build: clean-build
	@echo "🚀 Creating wheel file"
	@poetry build

# clean build artifacts
clean-build: #
	@rm -rf dist

# publish a release to pypi.
publish: #
	@echo "🚀 Publishing: Dry run."
	@poetry config pypi-token.pypi $(PYPI_TOKEN)
	@poetry publish --dry-run
	@echo "🚀 Publishing."
	@poetry publish

# Build and publish.
build-and-publish: build publish

# Test if documentation can be built without warnings or errors
docs-test:
	@mkdocs build -s

# Build and serve the documentation
docs:
	@mkdocs serve
