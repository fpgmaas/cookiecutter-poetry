tag:=latest
DOCKER_PROJECT_IMAGE_NAME={{ cookiecutter.project_name }}
DOCKER_PROJECT_CONTAINER_NAME={{ cookiecutter.project_name }}
DOCKER_PROJECT_TAGGED_IMAGE_NAME=$(DOCKER_PROJECT_IMAGE_NAME):$(tag)
SERVICE_PORT={{ cookiecutter.port }}

.PHONY: install
install: ## Install the poetry environment
	@echo "🚀 Creating virtual environment using pyenv and poetry"
	@poetry env use 3.12
	@poetry install
	@poetry run pre-commit install
	@poetry shell

.PHONY: check
check: ## Run code quality tools.
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

.PHONY: clean-tox
clean-tox: ## deleting tox directory
	@echo "🚀 Deleting Tox folder"
	@rm -rf .tox

.PHONY: tox
tox: ## running test in tox
	@echo "🚀 Testing code: Running Tox"
	@poetry run tox --recreate

.PHONY: test
test: ## Test the code with pytest
	@echo "🚀 Testing code: Running pytest"
	@poetry run pytest --cov --cov-config=pyproject.toml --cov-report=xml

{%- if cookiecutter.publish_to == "pypi"%}
.PHONY: publish
publish: ## publish a release to pypi.
    @echo "🚀 Publishing: Dry run."
    @poetry config pypi-token.pypi $(PYPI_TOKEN)
    @poetry publish --dry-run
    @echo "🚀 Publishing."
    @poetry publish

.PHONY: build-and-publish
build-and-publish: build publish ## Build and publish.
{%- elif cookiecutter.publish_to == "artifactory" %}

.PHONY: publish
publish: ## Publish to the Artifactory repository using poetry. Requires ARTIFACTORY_TOKEN to be set.
    @echo "🚀 Publishing: Dry run."
    @poetry config repositories.artifactory $(ARTIFACTORY_URL)
    @poetry publish --repository artifactory --username $(ARTIFACTORY_USERNAME) --password $(ARTIFACTORY_PASSWORD) --dry-run
    @echo "🚀 Publishing."
    @poetry publish --repository artifactory --username $(ARTIFACTORY_USERNAME) --password $(ARTIFACTORY_PASSWORD)

.PHONY: build-and-publish
build-and-publish: build publish ## Build and publish.
{%- endif%}

# .PHONY: build
# build: clean-build ## Build wheel file using poetry
# 	@echo "🚀 Creating wheel file"
# 	@poetry build

# .PHONY: clean-build
# clean-build: ## clean build artifacts
# 	@rm -rf dist

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@poetry run mkdocs build -s

.PHONY: docs
docs: ## Build and serve the documentation
	@poetry run mkdocs serve

.PHONY: docker-login
docker-login: ## Logs in to DockerHub with read priviliges only
	@docker login -u $(PS_DOCKERHUB_USERNAME) -p $(PS_DOCKERHUB_TOKEN)

.PHONY: docker-build
docker-build: ## Build the docker image
	@echo "🚀 building docker image $(DOCKER_PROJECT_TAGGED_IMAGE_NAME)"
	@docker build . -t $(PS_DOCKERHUB_USERNAME)/$(DOCKER_PROJECT_TAGGED_IMAGE_NAME)

.PHONY: docker-start
docker-start: ## run the docker image
	@echo "🚀 creating 'partsnap' network"
	@docker network create partsnap
	@echo "🚀 starting docker image $(PS_DOCKERHUB_USERNAME)/$(DOCKER_PROJECT_TAGGED_IMAGE_NAME) on port $(SERVICE_PORT)"
	@docker run --network="partsnap" --add-host host.docker.internal:host-gateway -d --rm --name $(DOCKER_PROJECT_CONTAINER_NAME) -p $(SERVICE_PORT):$(SERVICE_PORT) $(PS_DOCKERHUB_USERNAME)/$(DOCKER_PROJECT_TAGGED_IMAGE_NAME)
	@docker ps --filter "name='{{ cookiecutter.project_name }}*'"
	@echo {{ cookiecutter.project_name }} service: connect to http://localhost:$(SERVICE_PORT)/docs

.PHONY: docker-stop
docker-stop: ## run the docker image
	@-docker kill $(DOCKER_PROJECT_CONTAINER_NAME)
	@docker ps --filter "name='{{ cookiecutter.project_name }}*'"
	@echo "🚀 deleting 'partsnap' network"
	@ docker network rm partsnap

.PHONY: docker-push
docker-push: ## push to docker
	@docker push $(PS_DOCKERHUB_USERNAME)/$(DOCKER_PROJECT_TAGGED_IMAGE_NAME)

.PHONY: docker-image-clean
docker-clean: ## remove all project images and containers locally
	@-docker rm -vf `docker ps -f name='{{ cookiecutter.project_name }}*' -aq` 2>/dev/null
	@-docker rmi `docker images -f "dangling=true" -q` 2>/dev/null
	@-docker rmi -f `docker image ls -f reference='{{ cookiecutter.project_name }}*' -aq` 2>/dev/null
	@-docker rmi -f `docker image ls -f reference='pslbrack/{{ cookiecutter.project_name }}*' -aq` 2>/dev/null
	@docker image ls

{%- if cookiecutter.database == 'y' %}
.PHONY: reset-db
reset-db: ## clears and repopulate the database
	@{{ cookiecutter.project_name }} --test-client db clear
	@{{ cookiecutter.project_name }} --test-client --no-storage-connection db populate
{%- endif %}

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo tag=$(tag)
.DEFAULT_GOAL := help
