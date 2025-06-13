# Voice-Controlled Robot Car 🤖🎤

This project transforms an Elegoo Smart Robot Car into a voice-controlled robot using:

- 📡 ESP32 for Wi-Fi and motor control
- 🎙️ INMP441 I²S mic to capture voice
- 🧠 FastAPI + Whisper to transcribe audio
- 🔍 Local LLaMA model to understand commands

## 🧭 Architecture
1. Voice captured via ESP32 mic
2. Audio sent to local server
3. Transcribed using Whisper
4. Parsed via local LLaMA
5. JSON command returned (e.g., `{"action": "turn_left", "duration": 2}`)

## 🛠 Setup instructions and more coming soon.

