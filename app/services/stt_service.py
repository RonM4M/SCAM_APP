# stt_service.py (bytes-based)
import os
from vosk import Model, KaldiRecognizer
import json
from pydub import AudioSegment
import io
import wave

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "vosk-model-small-en-us")

print("Loading Vosk model from:", model_path)

if not os.path.exists(model_path):
    raise Exception("Model folder not found at: " + model_path)

model = Model(model_path)

def local_stt(audio_bytes: bytes) -> str:
    # Convert bytes to WAV with pydub (in-memory)
    audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
    audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)
    wav_path = "temp.wav"
    audio.export(wav_path, format="wav")

    wf = wave.open(wav_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())

    text_result = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            text_result += " " + res.get("text", "")

    final_res = json.loads(rec.FinalResult())
    text_result += " " + final_res.get("text", "")

    # cleanup
    try:
        wf.close()
        os.remove(wav_path)
    except:
        pass

    return text_result.strip()
