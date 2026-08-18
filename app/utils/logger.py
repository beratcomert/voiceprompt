"""Uygulama loglama. Dosya + konsol. Hassas veri (API key) loglanmaz."""
from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler

from app.utils import paths

_configured = False


def get_logger(name: str = "voiceprompt") -> logging.Logger:
    global _configured
    logger = logging.getLogger("voiceprompt")
    if not _configured:
        logger.setLevel(logging.INFO)
        fmt = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        file_handler = RotatingFileHandler(
            paths.log_file(), maxBytes=1_000_000, backupCount=3, encoding="utf-8"
        )
        file_handler.setFormatter(fmt)
        logger.addHandler(file_handler)

        console = logging.StreamHandler()
        console.setFormatter(fmt)
        logger.addHandler(console)

        _configured = True

    return logger if name == "voiceprompt" else logger.getChild(name)
