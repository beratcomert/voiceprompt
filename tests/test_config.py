import json

from app.config.defaults import DEFAULTS
from app.config.settings import Settings
from app.utils import paths


def test_load_creates_config_file(temp_appdata):
    assert not paths.config_file().exists()
    settings = Settings.load()
    assert paths.config_file().exists()
    assert settings.get("hotkey", "combination") == "ctrl+space"


def test_defaults_applied(temp_appdata):
    settings = Settings()
    assert settings.get("whisper", "model") == DEFAULTS["whisper"]["model"]
    assert settings.get("ai", "enabled") is False


def test_missing_keys_filled_from_defaults(temp_appdata):
    # Sadece bir alan içeren bozuk/eksik config
    partial = {"hotkey": {"combination": "alt+q"}}
    settings = Settings(partial)
    assert settings.get("hotkey", "combination") == "alt+q"
    # Eksik bölümler defaults'tan gelmeli
    assert settings.get("whisper", "model") == DEFAULTS["whisper"]["model"]
    assert settings.get("audio", "sample_rate") == DEFAULTS["audio"]["sample_rate"]


def test_save_and_reload_roundtrip(temp_appdata):
    settings = Settings.load()
    settings.set("whisper", "model", "small")
    settings.set("hotkey", "combination", "ctrl+alt+space")
    settings.save()

    reloaded = Settings.load()
    assert reloaded.get("whisper", "model") == "small"
    assert reloaded.get("hotkey", "combination") == "ctrl+alt+space"


def test_corrupt_config_falls_back_to_defaults(temp_appdata):
    paths.config_file().write_text("{ not valid json", encoding="utf-8")
    settings = Settings.load()
    assert settings.get("hotkey", "combination") == "ctrl+space"


def test_saved_json_is_utf8_readable(temp_appdata):
    settings = Settings.load()
    data = json.loads(paths.config_file().read_text(encoding="utf-8"))
    assert "hotkey" in data
