import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

FIRST_PERSON = {"i", "me", "my", "mine", "we", "us", "our", "ours"}
SECOND_PERSON = {"you", "your", "yours"}
THIRD_PERSON = {"he", "him", "his", "she", "her", "hers", "they", "them", "their", "theirs"}

def detect_pov(text: str) -> str:
    """
    Detects point of view (first, second, third) based on pronoun frequency.
    Returns: "first", "second", "third", or "unknown"
    """
    doc = nlp(text.lower())
    pronouns = [token.text for token in doc if token.pos_ == "PRON"]
    counts = Counter(pronouns)
    
    first_count = sum(counts[p] for p in FIRST_PERSON)
    second_count = sum(counts[p] for p in SECOND_PERSON)
    third_count = sum(counts[p] for p in THIRD_PERSON)

    # Decide POV based on max count
    if first_count > second_count and first_count > third_count:
        return "first"
    elif second_count > first_count and second_count > third_count:
        return "second"
    elif third_count > first_count and third_count > second_count:
        return "third"
    else:
        return "unknown"
