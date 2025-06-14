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

## 🛠 Setup

1. Install the Python dependencies inside the `server/` folder:

   ```bash
   pip install -r server/requirements.txt
   ```

2. Start the FastAPI server:

   ```bash
   uvicorn server.main:app --reload
   ```

3. Send an audio file to the `/process-audio/` endpoint. A helper script
   is provided:

   ```bash
   python server/test-upload.py
   ```

   The script posts the sample `forward.wav` recording and prints the
   transcription along with the JSON command parsed by the LLaMA model.

More detailed hardware instructions are tracked in `tasks.md`.

