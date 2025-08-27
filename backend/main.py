# backend/agents/gender_inference_agent.py

from backend.tools.character_extractor import extract_characters
from backend.tools.gender_detector import detect_genders
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # backend/agents
file_path = os.path.join(BASE_DIR, "sample_short_stories", "the_clockmakers_secret.txt")

with open(file_path, "r", encoding="utf-8") as f:
    story_text = f.read()

# Step 1: Extract characters using spaCy
characters = extract_characters(story_text)
print("Extracted characters:", characters)

# Step 2: Detect gender using hybrid approach (currently only gender_guesser)
gender_info = detect_genders(characters)

print("\nGender assignment:")
for char in gender_info:
    print(f"- {char['name']}: {char['gender']}")
