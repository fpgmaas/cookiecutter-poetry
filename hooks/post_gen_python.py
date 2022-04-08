#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":

    if "{{cookiecutter.pyenv_local_file}}" != "y":
        remove_file("python-version")

    if "Not open source" == "{{cookiecutter.open_source_license}}":
        remove_file("LICENSE")
