import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from googletrans import Translator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')
translator = Translator()

# Store user language: session id -> language code
user_languages = {}

@app.route('/')
def index():
    return render_template('index1.html')


@socketio.on('connect')
def on_connect():
    print('Client connected', request.sid)

@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected', request.sid)
    if request.sid in user_languages:
        del user_languages[request.sid]

# Client sets their chosen language
@socketio.on('set_language')
def set_language(data):
    lang = data.get('lang', 'en')
    user_languages[request.sid] = lang
    print(f"User {request.sid} set language: {lang}")

@socketio.on('speak')
def handle_speak(payload):
    role = payload.get('role', 'foreigner')
    text = payload.get('text', '').strip()
    src = payload.get('src', 'auto')

    if not text:
        return

    # Determine target language
    if role == 'foreigner':
        target = 'ko'  # foreigner speech → Korean
    else:
        # Korean speech → use foreigner's selected language
        target = next((lang for sid, lang in user_languages.items() if sid != request.sid), 'en')

    try:
        translated = translator.translate(text, src=src, dest=target).text
    except Exception as e:
        print('Translation error:', e)
        translated = text

    payload_for_origin = {
        'normal_text': text,
        'mirrored_text': translated,
        'origin': role,
        'tts_lang': target  # send TTS language
    }
    payload_for_other = {
        'normal_text': translated,
        'mirrored_text': text,
        'origin': role,
        'tts_lang': target
    }

    emit('new_message', {
        'origin_role': role,
        'payload_for_origin': payload_for_origin,
        'payload_for_other': payload_for_other
    }, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
