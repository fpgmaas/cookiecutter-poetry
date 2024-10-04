from __future__ import annotations

import os
import sys


def main() -> None:
    cwd = os.path.dirname(__file__)
    package_dir = os.path.abspath(os.path.join(cwd, ".."))
    try:
        os.system(f"cookiecutter {package_dir}")  # noqa: S605 | No injection, retrieving path in OS
    except KeyboardInterrupt:
        sys.exit(0)
