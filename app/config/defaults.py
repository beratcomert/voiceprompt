"""Varsayılan ayarlar. Config dosyası yoksa/eksikse bunlar kullanılır."""
from __future__ import annotations

DEFAULT_SYSTEM_PROMPT = (
    "Sen konuşma metinlerini temizleyen ve yapılandıran bir asistansın. "
    "Kullanıcının asıl amacını değiştirme. Gereksiz dolgu kelimelerini, tekrarları "
    "ve anlamsız konuşma parçalarını kaldır. Teknik terimleri koru. Metni anlaşılır "
    "ve düzenli hale getir. Kullanıcı teknik bir istek veriyorsa gereksinimleri açık "
    "şekilde yapılandır. Çıktıya açıklama ekleme. Sadece son metni döndür."
)

DEFAULTS: dict = {
    "general": {
        "language": "tr",
        "theme": "system",
        "start_with_windows": False,
        "start_minimized": False,
        "minimize_to_tray": True,
    },
    "audio": {
        "microphone_index": None,  # None = sistem varsayılanı
        "sample_rate": 16000,
    },
    "whisper": {
        "model": "base",
        "device": "cpu",
        "compute_type": "int8",
    },
    "ai": {
        "enabled": False,
        "provider": "openai",
        "api_key": "",
        "model": "",
        "base_url": "",
        "system_prompt": DEFAULT_SYSTEM_PROMPT,
    },
    "hotkey": {
        "combination": "ctrl+space",
    },
}
