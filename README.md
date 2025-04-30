# Kinyabot - Kinyarwanda Voice Assistant

This project implements a voice assistant that can understand and respond to queries in Kinyarwanda, simulating how a humanoid robot would interact with Rwandan communities.

## Project Overview

Kinyabot is a voice assistant that:

1. Listens to spoken Kinyarwanda questions
2. Transcribes speech to text using KinyaWhisper
3. Matches questions to predefined answers
4. Responds verbally in Kinyarwanda

This demonstrates how modern robotics can be made more accessible by incorporating local languages.

## Features

- **Speech Recognition**: Uses [KinyaWhisper](https://huggingface.co/benax-rw/KinyaWhisper), a specialized ASR model for Kinyarwanda by [Benax Labs](https://huggingface.co/benax-rw).
- **Natural Language Processing**: Simple pattern matching to map questions to answers
- **Text-to-Speech**: Converts answers back to spoken Kinyarwanda
- **User Interface**: Gradio user interface

## Requirements

- Python 3.7+
- PyTorch
- Transformers
- gTTS (Google Text-to-Speech)
- Gradio (for the web interface)

## Installation

```bash
# Clone the repository
git clone https://github.com/kevnnty/KinBot-Voice-Assistantt.git
cd KinBot-Voice-Assistantt

# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Run the main application
python main.py
```

After running the application, a Gradio web interface will launch. You can:

1. Click the microphone button and speak in Kinyarwanda
2. The system will transcribe your speech
3. Match your question to an answer
4. Play back the response in spoken Kinyarwanda

## Project Structure

```
kinyabot/
├── main.py                 # Main application code
├── requirements.txt        # Dependencies
├── README.md               # This file
├── sample_audio/           # Example audio queries
│   ├── rwanda_coding_academy.wav
│   ├── umurwa_mukuru.wav
│   ├── muraho.wav
│   ├── witwa_nde.wav
│   └── tehgikiloji.wav
└── responses/              # Generated audio responses
```

## Supported Questions

The system currently supports these questions (and their variations):

1. "Rwanda Coding Academy iherereye he?" (Where is Rwanda Coding Academy located?)
2. "Umurwa mukuru w'u Rwanda ni uwuhe?" (What is the capital of Rwanda?)
3. "U Rwanda rufite imirenge ingahe?" (How many sectors does Rwanda have?)
4. "Ikinyarwanda ni ururimi ruvugwa na bangahe?" (How many people speak Kinyarwanda?)
5. "Tehgikiloji ni iki?" (What is technology?)
6. "Mutangire mwirirwe" (Good afternoon)
7. "Muraho" (Hello)
8. "Witwa nde?" (What is your name?)
9. "Ni gute wumva ikinyarwanda?" (How do you understand Kinyarwanda?)
10. "Urakoze" (Thank you)

## How It Works

1. **Speech Recognition**:

   - Audio is captured from the microphone
   - KinyaWhisper model transcribes the audio to text

2. **Question Matching**:

   - The transcribed text is normalized and matched against known questions
   - Both exact and partial matching are supported

3. **Answer Generation**:

   - Pre-defined answers are retrieved based on matched questions
   - A default response is provided if no match is found

4. **Text-to-Speech**:
   - The answer is converted to speech using gTTS with Kinyarwanda language
   - The audio response is played back

## Extending the System

To add more questions and answers:

1. Edit the `get_qa_pairs()` function in `main.py`
2. Add new question-answer pairs to the dictionary
3. Use lowercase for questions to improve matching

## Limitations

- KinyaWhisper has limited accuracy for certain dialects and accents
- The NLP matching is simple and may not handle complex variations
- gTTS for Kinyarwanda has some pronunciation limitations

## Future Improvements

- Implement more sophisticated NLP for question understanding
- Add intent recognition for better answer matching
- Expand the knowledge base with more QA pairs
- Implement a custom TTS model trained specifically for Kinyarwanda

## References

```bibtex
@misc{baziramwabo2025kinyawhisper,
  author       = {Gabriel Baziramwabo},
  title        = {KinyaWhisper: Fine-Tuning Whisper for Kinyarwanda ASR},
  year         = {2025},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/benax-rw/KinyaWhisper}},
  note         = {Version 1.0}
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
