from fastapi import FastAPI,HTTPException
from app.routers import audio

app = FastAPI()

# include routers
app.include_router(audio.router)

@app.get("/")
def root():
    return {"message": "Backend working!"}
@app.get("/test")
def test_connection():
    print("Flutter called /test ")
    return {"message": "Backend connection successful!"}

'''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

    # Define the data format for chat
class ChatRequest(BaseModel):
        message: str

@app.get("/")
def read_root():
        return {"message": "Server is running!"}

@app.get("/news")
def get_news():
        print("NEWS ENDPOINT HIT: App requested news!")
        return [
            {
                "title": "Backend Connected Successfully!",
                "subtitle": "This news item is coming live from your FastAPI server.",
                "source": "Your Server",
                "icon": "security", # Simple string logic on frontend handles this
                "url": "https://fastapi.tiangolo.com"
            },
            {
                "title": "Digital Arrest Scam Alert",
                "subtitle": "Police will never arrest you over a video call.",
                "source": "Cyber Cell",
                "icon": "videocam_off",
                "url": "https://cybercrime.gov.in"
            }
        ]

# ---- ADD THIS NEW ENDPOINT ----
@app.get("/test")
def test_endpoint():
    print(" TEST ENDPOINT HIT!")
    return {"message": "Test successful! Connection is working."}
# -------------------------------

@app.post("/chat")
def chat(request: ChatRequest):
        print(f"CHAT RECEIVED: {request.message}")
        return {"response": f"Backend received: '{request.message}'. I am ready to help!"}

if __name__ == "__main__":
    # 0.0.0.0 is CRITICAL for mobile connection
    uvicorn.run(app, host="0.0.0.0", port=8000)
'''