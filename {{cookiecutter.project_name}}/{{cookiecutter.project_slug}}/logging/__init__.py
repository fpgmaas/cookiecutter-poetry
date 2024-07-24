""" Logging facility for {{cookiecutter.project_slug}}.

    - Author: {{cookiecutter.author}}
    - Email: {{cookiecutter.email}}
    - Copyright (C) 2024 PartSnap LLC
"""

import logging

PARTSNAP_BASE_LOGGER_NAME = "psnap"

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(levelname)-8s  %(message)-140s [pid(%(process)d)-%(name)s]")
console.setFormatter(formatter)
ps_base_logger = logging.getLogger(PARTSNAP_BASE_LOGGER_NAME)
ps_base_logger.addHandler(console)
ps_base_logger.setLevel(logging.INFO)


def psnap_get_logger(name: str) -> logging.Logger:
    name = name.replace("psnap.", "")  # remove potentially the root logger name
    name = name.strip(".")
    return ps_base_logger if name == "" else ps_base_logger.getChild(name)


def psnap_set_log_level(level: int | str, name: str = "") -> str | int:
    logger = psnap_get_logger(name)
    if isinstance(level, str):
        level = logging.getLevelName(level.upper())
    if not isinstance(level, int):
        msg = f"Invalid log level type {level}"
        ps_base_logger.error(f"{msg} raising TypeError")
        raise TypeError(msg)
    ps_base_logger.debug(f"Setting log level {name} to {level}")
    logger.setLevel(level)
    return logging.getLevelName(logger.getEffectiveLevel())  # type: ignore[no-any-return]


def psnap_get_logger_names() -> list[str]:
    return [name for name in logging.root.manager.loggerDict if name.startswith("psnap")]
