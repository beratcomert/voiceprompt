"""Merkezi dosya yolu yönetimi. Tüm kullanıcı verisi %APPDATA%/VoicePrompt altında."""
from __future__ import annotations

import os
from pathlib import Path

APP_NAME = "VoicePrompt"


def app_data_dir() -> Path:
    base = os.environ.get("APPDATA") or str(Path.home())
    path = Path(base) / APP_NAME
    path.mkdir(parents=True, exist_ok=True)
    return path


def config_file() -> Path:
    return app_data_dir() / "config.json"


def models_dir() -> Path:
    path = app_data_dir() / "models"
    path.mkdir(parents=True, exist_ok=True)
    return path


def logs_dir() -> Path:
    path = app_data_dir() / "logs"
    path.mkdir(parents=True, exist_ok=True)
    return path


def data_dir() -> Path:
    path = app_data_dir() / "data"
    path.mkdir(parents=True, exist_ok=True)
    return path


def log_file() -> Path:
    return logs_dir() / "app.log"
