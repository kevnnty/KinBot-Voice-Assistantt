import gradio as gr

def launch_interface(process_fn):
    def run(audio_file):
        text, answer = process_fn(audio_file)
        return f"Transcription: {text}\nResponse: {answer}"

    gr.Interface(
        fn=run,
        inputs=gr.Audio(source="microphone", type="filepath"),
        outputs="text",
        title="Kinyarwanda Voice Assistant"
    ).launch()
