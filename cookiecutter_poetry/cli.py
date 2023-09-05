import os
from pathlib import Path


def main() -> None:
    cwd = os.path.dirname(__file__)
    package_dir = os.path.abspath(os.path.join(cwd, ".."))
    template_dir = Path(package_dir) / "templates" / "cookiecutter-poetry"
    os.system(f"cookiecutter {str(template_dir)}")
