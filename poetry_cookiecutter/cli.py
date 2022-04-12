import os


def main():
    cwd = os.path.dirname(__file__)
    package_dir = os.path.abspath(os.path.join(cwd, ".."))
    os.system(f"cookiecutter {package_dir}")
