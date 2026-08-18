from pathlib import Path

from app.utils import paths


def test_app_data_dir_under_appdata(temp_appdata):
    d = paths.app_data_dir()
    assert d == Path(temp_appdata) / "VoicePrompt"
    assert d.exists()


def test_subdirs_created(temp_appdata):
    assert paths.models_dir().exists()
    assert paths.logs_dir().exists()
    assert paths.data_dir().exists()


def test_config_and_log_file_paths(temp_appdata):
    assert paths.config_file().name == "config.json"
    assert paths.log_file().parent == paths.logs_dir()
