from gtts import gTTS
import os

def speak_response(text):
    tts = gTTS(text=text, lang="rw")
    output_path = "audio/response.wav"
    tts.save(output_path)
    os.system(f"play {output_path}")  # Linux/macOS only; on Windows use another player
