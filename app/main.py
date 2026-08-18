"""VoicePrompt giriş noktası."""
from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from app.config.settings import Settings
from app.ui.main_window import MainWindow
from app.utils.logger import get_logger


def main() -> int:
    logger = get_logger()
    logger.info("VoicePrompt starting")

    settings = Settings.load()

    app = QApplication(sys.argv)
    app.setApplicationName("VoicePrompt")

    window = MainWindow(settings)
    window.show()

    logger.info("GUI shown")
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
