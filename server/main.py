from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import whisper
import os

app = FastAPI()
model = whisper.load_model("base")  # You can use "small" or "medium" if needed

@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
    # Save uploaded file
    temp_path = "temp.wav"
    with open(temp_path, "wb") as f:
        f.write(await file.read())
    
    # Transcribe with Whisper
    result = model.transcribe(temp_path)
    os.remove(temp_path)

    return JSONResponse(content={"transcription": result["text"]})

