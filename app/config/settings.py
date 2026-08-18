"""Ayarların JSON olarak yüklenip kaydedilmesi. Eksik alanlar defaults ile doldurulur."""
from __future__ import annotations

import copy
import json
from typing import Any

from app.config.defaults import DEFAULTS
from app.utils import paths


def _deep_merge(base: dict, override: dict) -> dict:
    """override değerlerini base üzerine bindirir; eksik anahtarlar base'den gelir."""
    result = copy.deepcopy(base)
    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result


class Settings:
    def __init__(self, data: dict | None = None) -> None:
        self._data = _deep_merge(DEFAULTS, data or {})

    @classmethod
    def load(cls) -> "Settings":
        path = paths.config_file()
        if not path.exists():
            settings = cls()
            settings.save()
            return settings
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            data = {}
        return cls(data)

    def save(self) -> None:
        path = paths.config_file()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, ensure_ascii=False, indent=2)

    def get(self, section: str, key: str) -> Any:
        return self._data[section][key]

    def set(self, section: str, key: str, value: Any) -> None:
        self._data.setdefault(section, {})[key] = value

    def section(self, name: str) -> dict:
        return self._data[name]

    def as_dict(self) -> dict:
        return copy.deepcopy(self._data)
