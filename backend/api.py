# backend/api.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tools.character_extractor import extract_characters
from tools.pov_detector import detect_pov
from tools.gender_detector import detect_genders
from tools.build_charcter_graph import build_character_graph

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
    char_graph = build_character_graph(request.text, [c["name"] for c in gender_info])
    # print("DEBUG: Returning -->", {"characters": gender_info})
    return {"characters": gender_info, "pov": pov_info, "graph": char_graph}

