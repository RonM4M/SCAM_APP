from pydantic import BaseModel

class TranscriptInput(BaseModel):
    text: str
