"""File Utility functions

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- Copyright (C) 2024 PartSnap LLC
"""

import subprocess
from pathlib import Path

from {{cookiecutter.project_slug}}.logging import psnap_get_logger

LOGGER = psnap_get_logger("utils.file")


def get_mime_type(filename: Path | str) -> str:
    """Returns the MIME type of a file.

    Parameters
    ----------
    filename: Path to the file

    Returns
    -------
    a string containing the MIME type

    Raises
    ------

    FileNotFoundError if the file does not exist
    TypeError if the MIME type could not be identified

    """
    filename = Path(filename).resolve()
    mime_type = "application/octet-stream"
    try:
        result = subprocess.run(["file", "--mime-type", str(filename)], capture_output=True)  # noqa: S603 S607
    except FileNotFoundError as error:
        LOGGER.warning(f"cmd 'file' not found: {error}")
    else:
        if result.returncode != 0:
            LOGGER.warning(f"Could not determine mime type - {result.stderr.decode('utf-8')}")
        else:
            mime_type = result.stdout.decode("utf-8").split(":")[1].strip()
    return mime_type
