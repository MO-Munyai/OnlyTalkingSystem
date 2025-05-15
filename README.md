# OnlyTalkingSystem (OTTiS) 🎙️🤖

**OTTiS (OnlyTalkingSystem)** is a voice-driven AI prototype that listens to your speech, converts it to text using Google’s Speech Recognition API, 
and saves everything you say to a file called `output.txt`. It also introduces itself with a bit of character, speaking back to you using text-to-speech.

Created by **Orange**, OTTiS playfully encourages users to explore voice interfaces while collecting spoken data.

---

## Features

- 🎤 Listens to microphone input in real-time  
- 🧠 Converts speech to text with `SpeechRecognition` (Google Web Speech API)  
- 📄 Automatically logs the recognized text to `output.txt`  
- 🗣️ Talks back using `pyttsx3` (offline text-to-speech)

---

## Installation

Make sure you have Python 3 installed, then install the following dependencies:

```bash
pip install pyttsx3 SpeechRecognition
pip install pipwin
pipwin install pyaudio


## Run the script:
python ots.py

