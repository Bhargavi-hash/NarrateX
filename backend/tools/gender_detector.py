# backend/tools/gender_detector.py

import gender_guesser.detector as gender
# from llm_support_agents.llm_gender_detection_agent import infer_gender_with_llm
from typing import List, Dict

detector = gender.Detector(case_sensitive=False)

def infer_gender(name: str) -> str:
    """
    Infer gender from a first name using gender-guesser.
    Results: male, female, mostly_male, mostly_female, andy (androgynous), unknown
    We'll normalize to: male, female, ambiguous
    """
    result = detector.get_gender(name.split()[0])  # use first name only
    if result in ["male"]:
        return "male"
    elif result in ["female"]:
        return "female"
    else:
        return "ambiguous"
    # return result

def detect_genders(characters: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    characters: [{"name": "Mr. Finch", "context": "Mr. Finch ..."}, ...]
    Returns: [{"name": X, "gender": male/female/unknown}, ...]
    """
    # output = []
    # for char in characters:
    #     base_gender = infer_gender(char["name"])
    #     if base_gender == "ambiguous":
    #         refined = infer_gender_with_llm(char["name"], char["context"])
    #         output.append({"name": char["name"], "gender": refined})
    #     else:
    #         output.append({"name": char["name"], "gender": base_gender})

    # return output

    # Skip LLM
    return [{"name": char["name"], "gender": infer_gender(char["name"])} for char in characters]
