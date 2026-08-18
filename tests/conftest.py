"""Testler için ortak fixture: APPDATA'yı geçici dizine yönlendir."""
from __future__ import annotations

import pytest


@pytest.fixture()
def temp_appdata(tmp_path, monkeypatch):
    monkeypatch.setenv("APPDATA", str(tmp_path))
    yield tmp_path
