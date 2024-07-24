#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    if "{{cookiecutter.database}}" == "y":
        remove_file("{{cookiecutter.project_slug}}/foo.py")
        remove_file("tests/test_foo.py")

    if "{{cookiecutter.database}}" != "y":
        remove_dir("{{cookiecutter.project_slug}}/api_model")
        remove_dir("{{cookiecutter.project_slug}}/assets")
        remove_dir("{{cookiecutter.project_slug}}/cli")
        remove_dir("{{cookiecutter.project_slug}}/data")
        remove_dir("{{cookiecutter.project_slug}}/dbms")
        remove_dir("{{cookiecutter.project_slug}}/dependencies")
        remove_dir("{{cookiecutter.project_slug}}/logging")
        remove_dir("{{cookiecutter.project_slug}}/model")
        remove_dir("{{cookiecutter.project_slug}}/routers")
        remove_dir("{{cookiecutter.project_slug}}/utils")
        remove_file("{{cookiecutter.project_slug}}/_server_doc.py")
        remove_file("{{cookiecutter.project_slug}}/app_builder.py")
        remove_file("{{cookiecutter.project_slug}}/db_tables.py")
        remove_file("{{cookiecutter.project_slug}}/main.py")
        remove_dir("tests/cli")
        remove_dir("tests/models")
        remove_file("tests/conftest.py")
        remove_file("tests/endpoints/conftest.py")
        remove_file("tests/endpoints/test_samples.py")

    if "{{cookiecutter.devcontainer}}" != "y":
        remove_dir(".devcontainer")
