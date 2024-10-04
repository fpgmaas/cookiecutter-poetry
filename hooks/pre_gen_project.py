from __future__ import annotations

import re
import sys

PROJECT_NAME_REGEX = r"^[-a-zA-Z][-a-zA-Z0-9]+$"
project_name = "{{cookiecutter.project_name}}"
if not re.match(PROJECT_NAME_REGEX, project_name):
    print(
        f"ERROR: The project name {project_name} is not a valid Python module name. Please do not use a _ and use - instead"
    )
    # Exit to cancel project
    sys.exit(1)

PROJECT_SLUG_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
project_slug = "{{cookiecutter.project_slug}}"
if not re.match(PROJECT_SLUG_REGEX, project_slug):
    print(
        f"ERROR: The project slug {project_slug} is not a valid Python module name. Please do not use a - and use _ instead"
    )
    # Exit to cancel project
    sys.exit(1)

# Update python version matrix
"""
{% set python_version_matrix = [] %}
{% for ver in range(
    cookiecutter.minor_python_version|replace("3.", "")|int, 13
) %}
{% set _ = python_version_matrix.append("3." ~ ver) %}
{% endfor %}
{{ cookiecutter.update({"_python_version_matrix": python_version_matrix}) }}
"""

# Update OS matrix
"""
{% set os_matrix = [] %}
{% if cookiecutter.test_on_windows == "y" %}
{% set _ = os_matrix.append("windows-latest") %}
{% endif %}
{% if cookiecutter.test_on_macos == "y" %}
{% set _ = os_matrix.append("macos-latest") %}
{% endif %}
{% if cookiecutter.test_on_ubuntu == "y" or os_matrix|length == 0 %}
{% set _ = os_matrix.append("ubuntu-latest") %}
{% endif %}
{{ cookiecutter.update({"_os_matrix": os_matrix}) }}
"""
