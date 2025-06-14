"""Simple helper script to post a test audio file to the local server."""

import requests

# Path to the WAV file we want to send. Feel free to swap this out with your
# own recordings.
audio_path = "../sample-audio/forward.wav"

# Endpoint exposed by FastAPI in ``server/main.py``.
url = "http://localhost:8000/process-audio/"

with open(audio_path, "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)

print("Response:", response.json())
