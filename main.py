from asr.kinya_whisper import transcribe_audio
from nlp.matcher import get_answer
from tts.tts_engine import speak_response

def process(audio_file):
    text = transcribe_audio(audio_file)
    answer = get_answer(text)
    speak_response(answer)
    return text, answer

if __name__ == "__main__":
    from interface.ui_gradio import launch_interface
    launch_interface(process)
