# VOICEPROMPT

🎙️ **VoicePrompt**, Windows üzerinde çalışan, konuşmayı metne dönüştüren ve isteğe bağlı olarak yapay zekâ ile temizleyip kullanılabilir prompt/metin haline getiren bir masaüstü uygulamasıdır.

Temel amaç:

> Kullanıcı konuşur → Whisper konuşmayı metne çevirir → metin temizlenir → isteğe bağlı AI ile iyileştirilir → sonuç aktif uygulamadaki imlecin bulunduğu alana yazılır.

Uygulama bir kez başlatıldıktan sonra **System Tray üzerinde arka planda çalışmaya devam etmelidir.** Ana pencerenin kapatılması uygulamayı sonlandırmamalıdır. Global klavye kısayolu, arayüz kapalı olsa dahi çalışmalıdır.

---

# 1. Projenin Temel Hedefi

Kullanıcı bilgisayarda herhangi bir uygulamada çalışırken VoicePrompt'u açmak zorunda kalmadan konuşarak metin/prompt oluşturabilmelidir.

Örnek:

Kullanıcı:

> "şimdi şey bana php ile kullanıcı giriş sistemi yap email şifre olacak veritabanından kontrol etsin ve güvenli olsun"

Whisper çıktısı:

```text
şimdi şey bana php ile kullanıcı giriş sistemi yap email şifre olacak veritabanından kontrol etsin ve güvenli olsun
```

Temizlenmiş çıktı:

```text
PHP ile email ve şifre kullanarak çalışan bir kullanıcı giriş sistemi oluştur. Kullanıcı bilgilerini veritabanından güvenli şekilde doğrula.
```

AI Prompt Modu aktifse:

```text
PHP kullanarak güvenli bir kullanıcı giriş sistemi oluştur.

Gereksinimler:
- Email ve şifre ile giriş yapılabilmeli.
- Kullanıcı bilgileri veritabanından doğrulanmalı.
- Şifreler güvenli şekilde işlenmeli.
- SQL Injection ve benzeri yaygın güvenlik açıklarına karşı önlem alınmalı.
- Kod temiz ve anlaşılır olmalı.
```

Sonuç aktif uygulamadaki imlecin bulunduğu yere otomatik olarak yazılmalıdır.

---

# 2. İlk Sürümün Kapsamı — MVP

İlk sürümde gereksiz özelliklerden kaçınılmalıdır.

## MVP özellikleri

- Windows masaüstü uygulaması
- Python tabanlı mimari
- PySide6 arayüzü
- Whisper ile Speech-to-Text
- Türkçe konuşma desteği
- Mikrofon seçimi
- Konuşma başlatma/durdurma
- Global klavye kısayolu
- Kısayolun uygulama içinden değiştirilebilmesi
- System Tray desteği
- Uygulama penceresinin kapatıldığında tray'e küçülmesi
- Uygulamanın arka planda çalışmaya devam etmesi
- Konuşma metninin gösterilmesi
- Basit metin temizleme
- Panoya kopyalama
- Aktif uygulamadaki imlece otomatik yazma
- Basit ayarlar ekranı
- Whisper model seçimi
- AI provider/model/API key ayarları
- Log sistemi
- Windows `.exe` paketleme

AI özellikleri opsiyonel olmalıdır.

---

# 3. Uygulamanın Yaşam Döngüsü

VoicePrompt normal bir masaüstü uygulaması gibi çalışmamalıdır.

Uygulama açıldığında:

```text
VoicePrompt.exe
      ↓
Application Start
      ↓
System Tray oluştur
      ↓
Global Hotkey başlat
      ↓
Background Services başlat
      ↓
GUI göster
```

Kullanıcı pencereyi kapattığında:

```text
GUI
 ↓
closeEvent()
 ↓
window.hide()
 ↓
Application çalışmaya devam eder
 ↓
System Tray aktif
 ↓
Global Hotkey aktif
```

Uygulama yalnızca kullanıcı açıkça **Çıkış** yaptığında tamamen kapanmalıdır.

---

# 4. System Tray

Uygulama Windows System Tray içerisinde çalışmalıdır.

Tray ikonuna sağ tıklandığında:

```text
VoicePrompt
────────────────
Aç
Ayarlar
Kısayol Ayarları
────────────────
Çıkış
```

gibi bir menü bulunmalıdır.

Davranışlar:

- **Aç:** Ana pencereyi gösterir.
- **Ayarlar:** Ayarlar ekranını açar.
- **Kısayol Ayarları:** Global hotkey ayarlarına yönlendirir.
- **Çıkış:** Uygulamayı tamamen sonlandırır.

Tray ikonuna çift tıklamak da ana pencereyi açmalıdır.

Uygulama penceresindeki `X` butonu:

```text
Uygulamayı kapatma
      ↓
Sadece pencereyi gizle
      ↓
Tray'de çalışmaya devam et
```

şeklinde davranmalıdır.

---

# 5. Global Hotkey

Varsayılan global kısayol:

```text
CTRL + SPACE
```

olmalıdır.

Uygulama arka planda çalışırken dahi bu kısayol çalışmalıdır.

Temel akış:

```text
VoicePrompt arka planda
        ↓
CTRL + SPACE
        ↓
Recording Start
        ↓
Kullanıcı konuşur
        ↓
CTRL + SPACE
        ↓
Recording Stop
        ↓
Whisper
        ↓
Text Cleanup
        ↓
AI Processing (opsiyonel)
        ↓
Output
        ↓
Aktif uygulamaya yapıştır
```

Global hotkey sistemi GUI'den bağımsız olmalıdır.

---

# 6. Kısayol Değiştirme

Kullanıcı global kısayolu uygulama üzerinden değiştirebilmelidir.

Ayarlar:

```text
Global Kısayol

[ CTRL + SPACE ]

[ Değiştir ]
```

Değiştir butonuna basıldığında:

```text
Yeni kısayol kombinasyonunu girin...
```

şeklinde bir dinleme modu açılmalıdır.

Kullanıcı örneğin:

```text
CTRL + ALT + SPACE
CTRL + SHIFT + V
ALT + Q
F8
```

gibi kombinasyonlar belirleyebilmelidir.

Uygulama:

- Kısayolu algılamalı.
- Geçersiz kombinasyonları reddetmeli.
- Tek başına riskli/uygunsuz tuş kombinasyonlarını kontrol etmelidir.
- Mümkün olduğunda çakışmalar konusunda kullanıcıyı uyarmalıdır.
- Yeni kısayolu kaydetmelidir.
- Uygulama yeniden başlatıldığında kaydedilmiş kısayolu yüklemelidir.
- Eski hotkey kaydı kaldırılmalı ve yeni hotkey aktif edilmelidir.

---

# 7. AI Katmanı

AI kullanımı zorunlu değildir.

Uygulama iki temel modda çalışabilmelidir.

## MODE 1 — Sadece Whisper

```text
Microphone
    ↓
Whisper
    ↓
Raw Text
    ↓
Basic Text Cleanup
    ↓
Clipboard / Auto Type
```

Bu modda API key gerekmez.

---

## MODE 2 — Whisper + AI

```text
Microphone
    ↓
Whisper
    ↓
Raw Text
    ↓
Text Cleanup
    ↓
AI Processing
    ↓
Clean / Structured Prompt
    ↓
Clipboard / Auto Type
```

AI kullanmak isteyen kullanıcı kendi API bilgilerini girebilmelidir.

Ayarlar:

```text
AI Provider
API Key
Model
Base URL (opsiyonel)
System Prompt
Enable AI
```

---

# 8. AI Provider Mimarisi

AI sistemi tek bir sağlayıcıya bağımlı tasarlanmamalıdır.

Interface tabanlı bir yapı kullanılmalıdır.

Örnek:

```python
class AIProvider:
    def generate(self, text: str, system_prompt: str) -> str:
        raise NotImplementedError
```

Provider örnekleri:

```text
OpenAIProvider
GeminiProvider
OpenAICompatibleProvider
```

Klasör:

```text
ai/
├── base.py
├── openai_provider.py
├── gemini_provider.py
└── compatible_provider.py
```

Gelecekte başka modeller kolayca eklenebilmelidir.

---

# 9. Whisper Mimarisi

Speech-to-text katmanı AI katmanından tamamen bağımsız olmalıdır.

Örnek:

```python
class SpeechToTextProvider:
    def transcribe(self, audio_path: str) -> str:
        raise NotImplementedError
```

İlk provider:

```text
WhisperProvider
```

Gelecekte:

```text
FasterWhisperProvider
LocalWhisperProvider
OtherSTTProvider
```

eklenebilmelidir.

---

# 10. Whisper Model Yönetimi

Kullanıcı Whisper modelini seçebilmelidir.

Örnek modeller:

```text
tiny
base
small
medium
large
```

İlk MVP için varsayılan model:

```text
base
```

olabilir.

Uygulama model durumunu göstermelidir:

```text
Whisper Model
[ base ▼ ]

Status:
✓ Downloaded
```

veya:

```text
Status:
↓ Download required
```

Model dosyalarının saklanacağı konum merkezi bir configuration/path sistemi üzerinden yönetilmelidir.

---

# 11. Audio Pipeline

Ses kayıt işlemi ayrı bir servis olmalıdır.

```text
AudioRecorder
      ↓
PCM / WAV Audio
      ↓
Whisper
```

AudioRecorder sorumlulukları:

- Mikrofon listeleme
- Mikrofon seçme
- Kayıt başlatma
- Kayıt durdurma
- Kayıt dosyası oluşturma
- Mikrofon hatalarını yönetme

Mikrofon bulunmadığında kullanıcıya anlaşılır hata gösterilmelidir.

---

# 12. Metin İşleme Katmanı

Whisper çıktısı doğrudan kullanıcıya gönderilmemelidir.

Bir processing pipeline bulunmalıdır:

```text
Raw Transcript
      ↓
Normalizer
      ↓
Text Cleaner
      ↓
Optional AI Processor
      ↓
Final Text
```

## Basic Cleanup

AI olmadan da temel metin temizleme yapılmalıdır.

Temel işlemler:

- Gereksiz tekrarların azaltılması
- Dolgu kelimelerinin temizlenmesi
- Fazla boşlukların kaldırılması
- Gereksiz noktalama sorunlarının düzeltilmesi
- Cümle başlangıçlarının düzenlenmesi
- Gereksiz tekrar eden ifadelerin kaldırılması

Örnek:

```text
"şey yani eee php ile bir login sistemi yapalım"
```

↓

```text
"PHP ile bir login sistemi yapalım."
```

Basic cleaner kullanıcının anlamını değiştirmemelidir.

---

# 13. AI Prompt Processing

AI aktifse konuşma metni bir system prompt ile işlenmelidir.

Örnek system prompt:

```text
Sen konuşma metinlerini temizleyen ve yapılandıran bir asistansın.

Kullanıcının asıl amacını değiştirme.

Gereksiz dolgu kelimelerini, tekrarları ve anlamsız konuşma parçalarını kaldır.

Teknik terimleri koru.

Metni anlaşılır ve düzenli hale getir.

Kullanıcı teknik bir istek veriyorsa gereksinimleri açık şekilde yapılandır.

Çıktıya açıklama ekleme.

Sadece son metni döndür.
```

Bu prompt doğrudan business logic içerisine gömülmemelidir.

Configuration/template katmanından yönetilebilmelidir.

Kullanıcı ilerleyen sürümlerde kendi system prompt'unu belirleyebilmelidir.

---

# 14. Output Katmanı

Final metin aktif uygulamaya aktarılmalıdır.

İlk sürümde güvenilir yöntem:

```text
Final Text
    ↓
Clipboard
    ↓
Ctrl + V
```

OutputManager aşağıdaki sorumluluklara sahip olmalıdır:

- Clipboard'a kopyalama
- Paste
- Keyboard input
- Auto insert

Örnek:

```text
output/
├── clipboard.py
└── inserter.py
```

---

# 15. Aktif Uygulama Desteği

VoicePrompt belirli bir uygulamaya bağımlı olmamalıdır.

Kullanıcı şu tarz uygulamalarda kullanabilmelidir:

- Chrome
- Edge
- VS Code
- Visual Studio
- Notepad
- Word
- ChatGPT
- Terminal
- Discord
- Telegram
- Diğer standart metin alanları

İlk sürümde:

```text
Clipboard → Ctrl + V
```

yaklaşımı tercih edilmelidir.

---

# 16. GUI

GUI için:

```text
PySide6
```

kullanılmalıdır.

Arayüz sade ve modern olmalıdır.

Ana ekran:

```text
┌────────────────────────────────────┐
│ VOICEPROMPT                        │
│                                    │
│           🎙 Ready                 │
│                                    │
│      [ Start Recording ]           │
│                                    │
│ Mode: [ Clean ▼ ]                  │
│                                    │
│ Whisper: [ Base ▼ ]                │
│ AI:      [ Disabled ]              │
│                                    │
│ Last Result                        │
│ ┌────────────────────────────────┐ │
│ │ Final processed text...        │ │
│ └────────────────────────────────┘ │
│                                    │
│ [ Copy ] [ Insert ]                │
└────────────────────────────────────┘
```

Uygulama durumları:

```text
READY
RECORDING
PROCESSING
SUCCESS
ERROR
```

Kullanıcı hangi durumda olduğunu açıkça görebilmelidir.

---

# 17. GUI Kapatma Davranışı

Qt/PySide6 `closeEvent` davranışı özel olarak ele alınmalıdır.

Normal:

```python
window.close()
```

uygulamayı tamamen kapatmamalıdır.

Bunun yerine:

```text
closeEvent()
    ↓
event.ignore()
    ↓
window.hide()
```

uygulanmalıdır.

Application event loop çalışmaya devam etmelidir.

Global hotkey listener ve System Tray yaşamaya devam etmelidir.

Tam kapanma:

```text
Tray → Çıkış
```

üzerinden gerçekleştirilmelidir.

---

# 18. Ayarlar

Ayarlar ekranı bölümlere ayrılmalıdır.

## General

```text
Language
Theme
Start with Windows
Start minimized
Minimize to tray
```

## Audio

```text
Microphone
Sample Rate
Recording Settings
```

## Whisper

```text
Model
Model Path
Device (CPU / CUDA)
```

## AI

```text
Enable AI
Provider
API Key
Model
Base URL
System Prompt
```

## Hotkey

```text
Global Hotkey
```

---

# 19. Configuration

Ayarlar source code içerisine yazılmamalıdır.

Kullanıcı bazlı ayarlar:

```text
%APPDATA%/VoicePrompt/
```

altında saklanabilir.

Örnek:

```text
%APPDATA%/VoicePrompt/
├── config.json
├── models/
├── logs/
└── data/
```

API key gibi hassas veriler için güvenli Windows storage seçenekleri ilerleyen sürümde değerlendirilebilir.

GitHub'a gerçek credentials gönderilmemelidir.

Repository'de:

```text
.env.example
```

bulunmalıdır.

Örneğin:

```env
AI_PROVIDER=openai
AI_API_KEY=
AI_MODEL=
AI_BASE_URL=
```

---

# 20. Önerilen Klasör Yapısı

```text
voiceprompt/
│
├── app/
│   ├── main.py
│   │
│   ├── ui/
│   │   ├── main_window.py
│   │   ├── settings_window.py
│   │   └── widgets/
│   │
│   ├── tray/
│   │   ├── tray_icon.py
│   │   └── tray_menu.py
│   │
│   ├── hotkey/
│   │   ├── manager.py
│   │   ├── listener.py
│   │   └── validator.py
│   │
│   ├── audio/
│   │   ├── recorder.py
│   │   └── microphone.py
│   │
│   ├── stt/
│   │   ├── base.py
│   │   └── whisper_provider.py
│   │
│   ├── ai/
│   │   ├── base.py
│   │   ├── openai_provider.py
│   │   ├── gemini_provider.py
│   │   └── compatible_provider.py
│   │
│   ├── processing/
│   │   ├── cleaner.py
│   │   ├── normalizer.py
│   │   └── pipeline.py
│   │
│   ├── output/
│   │   ├── clipboard.py
│   │   └── inserter.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   └── defaults.py
│   │
│   ├── services/
│   │   └── voice_pipeline.py
│   │
│   └── utils/
│       ├── logger.py
│       └── paths.py
│
├── tests/
│   ├── test_cleaner.py
│   ├── test_pipeline.py
│   ├── test_config.py
│   └── test_hotkey.py
│
├── docs/
│
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── build.py
```

---

# 21. Katmanlı Mimari

```text
┌──────────────────────────────┐
│             GUI              │
│           PySide6            │
└──────────────┬───────────────┘
               │
┌──────────────▼───────────────┐
│       Application Layer      │
│        Voice Pipeline        │
└──────────────┬───────────────┘
               │
      ┌────────┼─────────┐
      │        │         │
      ▼        ▼         ▼
    Audio     STT       AI
      │        │         │
      └────────┼─────────┘
               │
      ┌────────▼────────┐
      │ Processing Layer│
      └────────┬────────┘
               │
      ┌────────▼────────┐
      │ Output Manager  │
      └────────┬────────┘
               │
          Clipboard/Paste
```

System Tray ve Global Hotkey, UI'dan bağımsız çalışan application services olmalıdır:

```text
                  VoicePrompt
                      │
         ┌────────────┼────────────┐
         ▼            ▼            ▼
      GUI Window   System Tray   Hotkey
         │            │            │
         └────────────┼────────────┘
                      │
               VoicePipeline
```

UI doğrudan Whisper veya AI API çağrısı yapmamalıdır.

---

# 22. Ana Voice Pipeline

Pipeline tüm işlemlerin merkezi orchestration noktası olmalıdır.

Örnek konsept:

```python
class VoicePipeline:

    def execute(self):
        audio = self.recorder.record()

        text = self.stt.transcribe(audio)

        text = self.cleaner.clean(text)

        if self.ai.is_enabled():
            text = self.ai.process(text)

        self.output.insert(text)
```

Gerçek implementasyonda bu işlemler UI thread'ini bloklamayacak şekilde worker/thread üzerinden gerçekleştirilmelidir.

---

# 23. Threading

Whisper ve AI işlemleri uzun sürebilir.

UI thread'i kesinlikle bloklanmamalıdır.

Önerilen yapı:

```text
GUI Thread
     │
     ├── User Interaction
     ├── Tray
     └── Hotkey State
              │
              ▼
        Worker Thread
              │
        ┌─────┼─────┐
        ▼     ▼     ▼
     Audio  Whisper  AI
              │
              ▼
          Processing
              │
              ▼
            Output
```

PySide6 tarafında:

```text
QThread
QRunnable
QThreadPool
```

gibi mekanizmalar değerlendirilebilir.

---

# 24. Global Hotkey Teknik Gereksinimleri

Hotkey manager:

- Uygulama arka plandayken çalışmalı.
- GUI kapalıyken çalışmalı.
- System Tray aktifken çalışmalı.
- Kısayol değiştirildiğinde eski listener kaldırılmalı.
- Yeni listener kaydedilmeli.
- Config üzerinden yüklenmeli.
- Uygulama yeniden başladığında otomatik yüklenmeli.
- Kayıt başlatma/durdurma state'ini yönetmeli.

Örnek:

```text
HotkeyManager
      │
      ├── register()
      ├── unregister()
      ├── update_hotkey()
      ├── load()
      └── validate()
```

---

# 25. Hata Yönetimi

Uygulama kritik hatalarda çökmemelidir.

Desteklenmesi gereken temel hatalar:

```text
Microphone not found
Whisper model missing
Whisper initialization failed
Whisper transcription failed
Invalid API key
AI provider unavailable
Invalid model
Clipboard failed
Text insertion failed
Hotkey registration failed
Hotkey conflict
```

Kullanıcıya teknik exception yerine anlaşılır mesaj gösterilmelidir.

Örneğin:

```text
❌ Mikrofon bulunamadı.

Lütfen Ayarlar > Audio bölümünden kullanılacak mikrofonu seçin.
```

---

# 26. Logging

Log sistemi:

```text
logs/
    app.log
```

olmalıdır.

Loglanabilecek olaylar:

- Uygulama başlatıldı
- System Tray başlatıldı
- Hotkey registered
- Hotkey changed
- Kayıt başladı
- Kayıt durdu
- Whisper başladı
- Whisper tamamlandı
- AI başladı
- AI tamamlandı
- Output başarılı
- Exception

API key veya hassas kullanıcı bilgileri loglanmamalıdır.

---

# 27. Güvenlik

API key gibi hassas veriler source code içine yazılmamalıdır.

GitHub'a kesinlikle gerçek credentials gönderilmemelidir.

`.gitignore` içerisinde en az:

```text
.env
*.env
config.local.json
secrets.json
```

bulunmalıdır.

İlerleyen sürümlerde API key'lerin Windows Credential Manager gibi güvenli storage mekanizmalarında saklanması değerlendirilebilir.

---

# 28. Teknoloji Stack

## Core

```text
Python 3.11+
PySide6
```

## Speech-to-Text

```text
Whisper
```

## Audio

```text
sounddevice
numpy
```

veya ihtiyaç doğrultusunda alternatif bir audio backend.

## Clipboard / Input

```text
pyperclip
keyboard / pynput
```

kullanılabilecek teknolojiler olarak değerlendirilebilir.

Global hotkey için Windows uyumluluğu öncelikli olmalıdır.

## AI

```text
OpenAI API
Gemini API
OpenAI-compatible APIs
```

## Packaging

```text
PyInstaller
```

---

# 29. İlk Geliştirme Sırası

Agent projeyi tek seferde karmaşık hale getirmemelidir.

Her aşama çalışan durumda bırakılmalıdır.

## Phase 1 — Temel Whisper MVP

Önce:

```text
Microphone
   ↓
Whisper
   ↓
Text
   ↓
GUI
```

çalıştırılmalıdır.

Amaç: Kullanıcı konuştuğunda doğru Türkçe metnin alınması.

---

## Phase 2 — Output

```text
Whisper
   ↓
Text
   ↓
Clipboard
   ↓
Paste
```

eklenmelidir.

---

## Phase 3 — Global Hotkey

Varsayılan:

```text
CTRL + SPACE
```

ile kayıt başlatılıp durdurulmalıdır.

Bu aşamada uygulama arka planda çalışmalı ve GUI kapalıyken dahi hotkey çalışmalıdır.

---

## Phase 4 — System Tray

Uygulama:

```text
GUI açık
   ↓
X
   ↓
GUI gizlenir
   ↓
Tray'de çalışır
```

şeklinde davranmalıdır.

Tam kapanma yalnızca:

```text
Tray → Çıkış
```

ile yapılmalıdır.

---

## Phase 5 — Hotkey Settings

Kullanıcı uygulama içinden global hotkey değiştirebilmelidir.

Örnek:

```text
CTRL + SPACE
↓
CTRL + ALT + SPACE
```

Değişiklik anında aktif olmalı ve config'e kaydedilmelidir.

---

## Phase 6 — Text Cleanup

AI olmadan basic cleaner eklenmelidir.

```text
Raw Text
 ↓
Normalizer
 ↓
Cleaner
 ↓
Final Text
```

---

## Phase 7 — AI Provider

AI provider sistemi eklenmelidir.

```text
Raw Text
 ↓
Cleanup
 ↓
Selected AI Provider
 ↓
Prompt Optimization
 ↓
Final Text
```

Kullanıcı AI'yi tamamen kapatabilmelidir.

---

## Phase 8 — Settings

Aşağıdakiler tamamlanmalıdır:

```text
Microphone
Whisper Model
AI Provider
API Key
Model
System Prompt
Global Hotkey
Theme
Start with Windows
```

---

## Phase 9 — EXE

Windows executable oluşturulmalıdır.

PyInstaller kullanılabilir.

Örneğin:

```bash
pyinstaller --onefile --windowed app/main.py
```

Ancak Whisper model dosyalarının boyutu ve dağıtımı ayrıca ele alınmalıdır.

Daha gelişmiş build aşamasında gerekirse:

```text
.spec
installer
model downloader
```

yapısı oluşturulabilir.

---

# 30. Definition of Done — MVP

MVP tamamlandığında kullanıcı aşağıdaki akışı gerçekleştirebilmelidir:

```text
1. VoicePrompt.exe'yi açar.
2. Uygulama System Tray'e yerleşir.
3. Ana pencere gösterilir.
4. Kullanıcı pencereyi kapatır.
5. VoicePrompt arka planda çalışmaya devam eder.
6. Kullanıcı CTRL + SPACE'e basar.
7. Kayıt başlar.
8. Kullanıcı konuşur.
9. CTRL + SPACE'e basar.
10. Kayıt durur.
11. Whisper konuşmayı metne çevirir.
12. Metin temizlenir.
13. Sonuç panoya alınır.
14. Aktif uygulamadaki imlece yapıştırılır.
```

AI aktifse:

```text
Whisper
   ↓
Cleanup
   ↓
Selected AI Provider
   ↓
Prompt Optimization
   ↓
Clipboard
   ↓
Active Application
```

Bu akış tamamen çalışıyorsa VoicePrompt MVP başarılı kabul edilir.

---

# 31. Gelecek Roadmap

## V1

```text
Faster Whisper
CUDA acceleration
Tray improvements
Windows startup
Better hotkey management
Better settings
```

## V2

```text
Real-time transcription
Local LLM
Prompt templates
Conversation history
Application-specific modes
```

## V3

```text
Voice commands
Custom AI agents
Plugin system
Application awareness
Context awareness
Advanced Windows automation
```

Uzun vadeli hedef:

> VoicePrompt'u yalnızca bir speech-to-text uygulaması değil, Windows üzerinde çalışan genel amaçlı bir **sesli üretkenlik ve AI input katmanı** haline getirmek.

---

# 32. Agent İçin Kritik Kurallar

Agent aşağıdaki kurallara kesinlikle uymalıdır:

1. Tüm özellikleri aynı anda geliştirme.
2. Her phase sonunda uygulama çalışır durumda olmalı.
3. Mevcut çalışan özellikleri sonraki geliştirmelerde bozmama.
4. UI ile business logic'i ayır.
5. Whisper ve AI provider'ları interface üzerinden kullan.
6. API key'leri source code'a koyma.
7. Uzun işlemleri UI thread'inde çalıştırma.
8. GUI kapanırken application event loop'u sonlandırma.
9. GUI `closeEvent` sırasında pencereyi gizle ve uygulamayı tray'de çalıştır.
10. System Tray uygulamanın ana yaşam döngüsünün bir parçası olmalı.
11. Global hotkey GUI'den bağımsız çalışmalı.
12. Hotkey değiştiğinde eski listener temizlenmeli.
13. Kısayol ayarı kalıcı olarak kaydedilmeli.
14. Uygulama yeniden başlatıldığında kayıtlı hotkey otomatik yüklenmeli.
15. Hataları kullanıcı dostu biçimde yönet.
16. Hassas verileri loglama.
17. Yeni STT ve AI provider eklemeyi kolaylaştıracak şekilde kodla.
18. Her önemli servis için unit test yazılabilecek yapı kullan.
19. Windows üzerinde çalışan gerçek bir uygulama gibi davran; sadece prototip kod üretme.
20. Önce çalışan MVP'yi tamamla, sonra optimizasyon ve ileri özelliklere geç.

---

# 33. MVP Başlangıç Hedefi

İlk kodlama görevi yalnızca aşağıdaki sistemi çalıştırmaktır:

```text
                   ┌───────────────┐
                   │ VoicePrompt    │
                   │   Windows     │
                   └───────┬───────┘
                           │
                  ┌────────▼────────┐
                  │   System Tray   │
                  └────────┬────────┘
                           │
                    CTRL + SPACE
                           │
                  ┌────────▼────────┐
                  │  Audio Recorder │
                  └────────┬────────┘
                           │
                  ┌────────▼────────┐
                  │     Whisper     │
                  └────────┬────────┘
                           │
                     Transcribed Text
                           │
                  ┌────────▼────────┐
                  │  Basic Cleaner  │
                  └────────┬────────┘
                           │
                  ┌────────▼────────┐
                  │    Clipboard    │
                  └────────┬────────┘
                           │
                       CTRL + V
                           │
                  Aktif Uygulama
```

Bu temel akış tamamen stabil hale geldikten sonra AI provider, gelişmiş temizleme, ayarlar ve diğer özellikler aşamalı olarak eklenmelidir.