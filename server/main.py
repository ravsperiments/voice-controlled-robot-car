"""FastAPI server for transcribing audio and returning robot commands."""

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from llama_interface import parse_command
import whisper
import os

app = FastAPI()

# Load the Whisper model once when the server starts. Adjust the model size
# depending on the resources available on your machine.
model = whisper.load_model("base")  # Options: tiny, base, small, medium, large

@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
    """Receive an audio file, transcribe it and return a JSON command."""
    # Whisper expects a file on disk, so we write the uploaded data to a
    # temporary WAV file.
    temp_path = "temp.wav"

    try:
        # Save the uploaded file temporarily so Whisper can access it
        with open(temp_path, "wb") as f:
            f.write(await file.read())

        # Transcribe audio using Whisper
        result = model.transcribe(temp_path)
        transcription = result["text"]

        # Feed the transcription to the LLaMA model which returns a
        # structured JSON command that the robot can interpret.
        command = parse_command(transcription)

        # Remove the temporary file now that we're done with it
        os.remove(temp_path)

        # Return both the raw transcription and the parsed command
        return {
            "transcription": transcription,
            "command": command,
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
