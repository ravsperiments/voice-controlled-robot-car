from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from llama_interface import parse_command
import whisper
import os

app = FastAPI()

# Load the Whisper model once when the server starts
model = whisper.load_model("base")  # Options: tiny, base, small, medium, large

@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
    temp_path = "temp.wav"

    try:
        # Save uploaded file temporarily
        with open(temp_path, "wb") as f:
            f.write(await file.read())

        # Transcribe audio using Whisper
        result = model.transcribe(temp_path)
        transcription = result["text"]

        # Parse command from transcription
        command = parse_command(transcription)

        # Clean up
        os.remove(temp_path)

        # Return transcription and parsed command
        return {
            "transcription": transcription,
            "command": command
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
