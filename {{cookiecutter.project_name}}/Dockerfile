FROM python:3.11-slim-buster

ENV POETRY_VERSION=1.4 \
    POETRY_VIRTUALENVS_CREATE=true\
    PARTSNAP_IN_DOCKER=true

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"
# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/
EXPOSE {{cookiecutter.port}}
# Project initialization:
RUN poetry install --no-interaction --no-ansi --no-root --no-dev
# Copy Python code to the Docker image
COPY {{cookiecutter.project_slug}} /code/{{cookiecutter.project_slug}}/

# Uncomment this code below if you want to use docker with a database
# Make a fresh Database
{% if cookiecutter.database == 'y' -%}
RUN poetry run {{cookiecutter.project_slug}} db clear
RUN poetry run {{cookiecutter.project_slug}} --test-client --no-storage-connection db populate
RUN poetry version -s > /code/{{cookiecutter.project_slug}}/VERSION.txt
{% endif -%}

CMD [ "poetry", "run", "start-server", "--port", "{{cookiecutter.port}}", "--log-level", "debug"]
