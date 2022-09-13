#!/usr/bin/env python
import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath: str) -> None:
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "{{cookiecutter.include_github_actions}}" != "y":
        remove_dir(".github")

    if "{{cookiecutter.mkdocs}}" != "y":
        remove_dir("docs")

    if "{{cookiecutter.dockerfile}}" != "y":
        remove_file("Dockerfile")

    if "{{cookiecutter.codecov}}" != "y":
        remove_file("codecov.yaml")
