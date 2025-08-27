# backend/tools/gender_detector.py

import gender_guesser.detector as gender
from typing import List, Dict

detector = gender.Detector(case_sensitive=False)

def infer_gender(name: str) -> str:
    """
    Infer gender from a first name using gender-guesser.
    Results: male, female, mostly_male, mostly_female, andy (androgynous), unknown
    We'll normalize to: male, female, unknown
    """
    result = detector.get_gender(name.split()[0])  # use first name only
    # if result in ["male", "mostly_male"]:
    #     return "male"
    # elif result in ["female", "mostly_female"]:
    #     return "female"
    # else:
    #     return "unknown"
    return result

def detect_genders(characters: List[str]) -> List[Dict[str, str]]:
    """
    Returns list of dicts: [{"name": "X", "gender": "male/female/unknown"}, ...]
    """
    return [{"name": char, "gender": infer_gender(char)} for char in characters]
