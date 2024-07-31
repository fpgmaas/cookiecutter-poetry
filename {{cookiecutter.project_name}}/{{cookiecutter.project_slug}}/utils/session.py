"""Test Session using HTTP Requests

- Author: {{cookiecutter.author}}
- Email: {{cookiecutter.email}}
- Copyright (C) 2024 PartSnap LLC
"""

import json
from urllib.parse import urljoin

from requests import Response, Session

from {{cookiecutter.project_slug}}.logging import psnap_get_logger


class PSServerSession(Session):
    """Session helper to manage the base URL"""

    def __init__(self, hostname: str, port: int) -> None:
        super().__init__()
        self.logger = psnap_get_logger("utils.PSServerSession")
        self.base_url = f"http://{hostname}:{port}"
        self.headers = {"accept": "application/json"}

    def request(self, method: str, url: str, *args, **kwargs) -> Response:  # type: ignore[no-untyped-def,override]
        joined_url = urljoin(self.base_url, url)
        self.logger.info(f"sending {method} {joined_url} {args} {kwargs}")
        response = super().request(method, joined_url, *args, **kwargs)
        try:
            self.logger.debug(f"response {response.status_code} {response.json()}")
        except json.JSONDecodeError:
            self.logger.debug(f"response {response.status_code} {response.text}")
        return response
