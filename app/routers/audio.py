'''from fastapi import APIRouter, UploadFile, File
from app.services.stt_service import local_stt  # bytes-based version
import os

router = APIRouter()

@router.post("/audio/upload")
async def upload_audio(file: UploadFile = File(...)):
    # Read bytes from the uploaded file
    audio_bytes = await file.read()

    try:
        transcript = local_stt(audio_bytes)   # expects bytes
    except Exception as e:
        return {"error": str(e)}

    return {
        "transcript": transcript,
        "is_scam": False
    }
  '''  

# ...existing code...
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.stt_service import local_stt  # bytes-based version
from app.services.scam_service import detect_scam
import asyncio
from concurrent.futures import ThreadPoolExecutor

router = APIRouter()
executor = ThreadPoolExecutor(max_workers=2)

@router.post("/audio/upload")
async def upload_audio(file: UploadFile = File(...)):
    # Read bytes from the uploaded file
    audio_bytes = await file.read()
    await file.close()

    try:
        loop = asyncio.get_running_loop()
        transcript = await loop.run_in_executor(executor, local_stt, audio_bytes)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    is_scam = detect_scam(transcript or "")

    return {
        "transcript": transcript,
        "is_scam": is_scam
    }
# ...existing code...

