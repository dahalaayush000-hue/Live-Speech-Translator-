# 🌐 Live Translator — HANARO

A real-time speech-to-speech translation web application designed for seamless communication between people speaking different languages.

---

## 🚀 Features

* 🎤 Real-time voice input (Web Speech API)
* 🌍 Live language translation
* 🔁 Mirrored UI for face-to-face conversations
* 🔊 Text-to-speech playback
* ⚡ Real-time communication using WebSockets

---

## 🛠 Tech Stack

* Backend: Flask + Flask-SocketIO
* Frontend: HTML, CSS, JavaScript
* Translation: googletrans (unofficial Google Translate API)
* Speech: Web Speech API

---

## 📂 Project Structure

app.py
templates/index.html
static/style.css

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py
```

Open in browser:
http://localhost:5000

---

## 🧪 Usage

Open two tabs:

http://localhost:5000/?role=foreigner
http://localhost:5000/?role=korean

Speak in one tab → translation appears in the other.

---

## ⚠️ Disclaimer

This project uses `googletrans`, an unofficial API wrapper for Google Translate.
It is intended for educational and demonstration purposes only.

---

## 📌 Future Improvements

* Replace with official translation APIs
* Add authentication system
* Store conversation history
* Deploy to cloud (Render / Railway)
* Improve UI/UX

---

## 📄 License

This project is licensed under the MIT License.
