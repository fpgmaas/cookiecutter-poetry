""" {{cookiecutter.project_slug}}

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- License: {{cookiecutter.license_released_under}}
"""

def hello(name: str) -> str:
    """Summary line.

    Extended description of function.

    Args:
        name (str): Description of arg1

    Returns:
        str: Description of return value
    """
    msg = f"Hello {name}!"
    print(msg)
    return msg


if __name__ == "__main__":  # pragma: no cover
    pass
