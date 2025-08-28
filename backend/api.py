# backend/api.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tools.character_extractor import extract_characters
from tools.pov_detector import detect_pov
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
    pov_info = detect_pov(request.text)
    # print("DEBUG: Returning -->", {"characters": gender_info})
    return {"characters": gender_info, "pov": pov_info}

