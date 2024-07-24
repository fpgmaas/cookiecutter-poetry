""" Test Session using the test client

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - Copyright (C) 2024 PartSnap LLC
"""

from fastapi.testclient import TestClient

from {{cookiecutter.project_slug}}.logging import psnap_get_logger


class PSTestClient(TestClient):
    """Session helper to manage the base URL"""

    def __init__(self, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        super().__init__(*args, **kwargs)
        self.logger = psnap_get_logger("utils.PSTestClient")

    def request(self, method: str, url: str, *args, **kwargs):  # type: ignore[no-untyped-def, override]
        self.logger.info(f"sending {method} {url} {args} {kwargs}")
        response = super().request(method, url, *args, **kwargs)
        self.logger.debug(f"response {response.status_code} {response.json()}")
        return response
