import requests

audio_path = "../sample-audio/forward.wav"  # Adjust path as needed
url = "http://localhost:8000/process-audio/"

with open(audio_path, "rb") as f:
    files = {"file": f}
    response = requests.post(url, files=files)

print("Response:", response.json())
