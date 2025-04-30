from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torchaudio

model = WhisperForConditionalGeneration.from_pretrained("benax-rw/KinyaWhisper")
processor = WhisperProcessor.from_pretrained("benax-rw/KinyaWhisper")

def transcribe_audio(audio_path):
    waveform, sample_rate = torchaudio.load(audio_path)
    inputs = processor(waveform, sampling_rate=sample_rate, return_tensors="pt")
    outputs = model.generate(inputs["input_features"])
    return processor.decode(outputs[0], skip_special_tokens=True)
