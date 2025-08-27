# backend/api.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tools.character_extractor import extract_characters
from tools.gender_detector import detect_genders

app = FastAPI()

# --- Add this block ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:8080"] if you want to restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ----------------------

class StoryRequest(BaseModel):
    text: str

@app.post("/analyze-story")
def analyze_story(request: StoryRequest):
    characters = extract_characters(request.text)
    gender_info = detect_genders(characters)
    return {"characters": gender_info}

