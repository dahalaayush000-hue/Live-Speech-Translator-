# Live Speech Translator — HANARO

A real-time speech-to-speech translation web app built for face-to-face conversations between people speaking different languages. Originally built for Korean ↔ foreign language use cases, but supports multiple language pairs.

--


## What it does

Two people open the app in separate tabs (or on separate devices on the same network). Each person speaks in their language, the speech gets transcribed, translated, and shown to the other person — with optional text-to-speech playback.

The UI has a mirrored layout so both people can hold the screen between them and read from their own side.
---
## Tech stack
- **Backend** — Flask + Flask-SocketIO (eventlet)
- **Translation** — `googletrans` (unofficial Google Translate wrapper — see disclaimer below)
- **Speech input** — Web Speech API (browser-native, Chrome/Edge only)
- **Speech output** — SpeechSynthesis API (browser-native)
- **Real-time** — WebSockets via Socket.IO

---
## Running locally

**Requirements:** Python 3.10+, Chrome or Edge browser

```bash
git clone https://github.com/dahalaayush000-hue/Live-Speech-Translator-.git
cd Live-Speech-Translator-

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

Open in your browser:

```
http://localhost:5000/?role=foreigner   # tab 1 — the non-Korean speaker
http://localhost:5000/?role=korean      # tab 2 — the Korean speaker
```

Speak in one tab. The translation appears in the other.

> **Browser note:** Web Speech API only works in Chrome and Edge. Firefox and Safari don't support it — you'll just see a "not supported" message.

---
## Supported languages

On the foreigner side you can select: English, Hindi, Nepali, Chinese (Simplified), Japanese, Spanish, French. The Korean side is fixed to Korean.

---

## Known issues

- `googletrans` is an unofficial library that hits Google Translate without an API key. It works fine for demos but can throw random errors or stop working without warning if Google changes their internal API. For anything production-facing, swap it out for the official Google Cloud Translation API or DeepL.
- Speech recognition quality depends entirely on your microphone and browser. Background noise will hurt accuracy.
- Both tabs need to be on the same server instance — won't work if you open two separate Render/Railway deploys.

---

## Project structure

```
app.py                  # Flask app + all Socket.IO event handlers
templates/index.html    # Single-page UI (both roles, role determined by URL param)
static/style.css        # Styles
requirements.txt
```

---

## Deployment

Tested locally. Should deploy to Render or Railway with minimal changes — just set your `SECRET_KEY` as an environment variable and point the start command at `app.py`.

```
# Procfile (if needed)
web: python app.py
```

---

## Disclaimer

This project uses `googletrans`, which is not an official Google product. It's fine for learning and demos. Don't use it in anything commercial or high-traffic.

---

## License

MIT — Aayush Dahal, 2026
