"""Ana pencere. Faz 0: sadece durum + devre dışı butonlar."""
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from app.config.settings import Settings

STATE_READY = "READY"
STATE_RECORDING = "RECORDING"
STATE_PROCESSING = "PROCESSING"
STATE_SUCCESS = "SUCCESS"
STATE_ERROR = "ERROR"

_STATE_TEXT = {
    STATE_READY: "🎙 Ready",
    STATE_RECORDING: "🔴 Recording...",
    STATE_PROCESSING: "⏳ Processing...",
    STATE_SUCCESS: "✓ Done",
    STATE_ERROR: "❌ Error",
}


class MainWindow(QWidget):
    def __init__(self, settings: Settings) -> None:
        super().__init__()
        self.settings = settings
        self.setWindowTitle("VoicePrompt")
        self.setMinimumWidth(420)
        self._build_ui()
        self.set_state(STATE_READY)

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)

        title = QLabel("VOICEPROMPT")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.status_label = QLabel()
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 15px; padding: 10px;")
        layout.addWidget(self.status_label)

        self.record_button = QPushButton("Start Recording")
        self.record_button.setEnabled(False)
        layout.addWidget(self.record_button)

        info = QHBoxLayout()
        info.addWidget(QLabel("Whisper:"))
        self.model_combo = QComboBox()
        self.model_combo.addItems(["tiny", "base", "small", "medium", "large"])
        self.model_combo.setCurrentText(self.settings.get("whisper", "model"))
        self.model_combo.setEnabled(False)
        info.addWidget(self.model_combo)
        info.addStretch()
        info.addWidget(QLabel(f"AI: {'On' if self.settings.get('ai', 'enabled') else 'Disabled'}"))
        layout.addLayout(info)

        layout.addWidget(QLabel("Last Result"))
        self.result_edit = QTextEdit()
        self.result_edit.setReadOnly(True)
        self.result_edit.setMinimumHeight(120)
        layout.addWidget(self.result_edit)

        buttons = QHBoxLayout()
        self.copy_button = QPushButton("Copy")
        self.copy_button.setEnabled(False)
        self.insert_button = QPushButton("Insert")
        self.insert_button.setEnabled(False)
        buttons.addWidget(self.copy_button)
        buttons.addWidget(self.insert_button)
        layout.addLayout(buttons)

    def set_state(self, state: str) -> None:
        self.status_label.setText(_STATE_TEXT.get(state, state))

    def set_result(self, text: str) -> None:
        self.result_edit.setPlainText(text)
