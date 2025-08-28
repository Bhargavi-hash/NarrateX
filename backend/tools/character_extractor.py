# backend/tools/character_extractor.py
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_characters(text):
    """
    Returns list of dicts like:
    [{"name": "Mr. Finch", "context": "Mr. Finch adjusted his glasses nervously."}, ...]
    """
    doc = nlp(text)
    characters = {}

    for sent in doc.sents:
        for ent in sent.ents:
            if ent.label_ == "PERSON":
                name = ent.text.strip()
                # Store first occurrence sentence as context
                if name not in characters:
                    characters[name] = sent.text.strip()

    # Cleanup generic words if needed
    blacklist = {"Clockmaker", "Secret"}
    characters = {n: c for n, c in characters.items() if n not in blacklist}

    # Convert dict to list of dicts
    return [{"name": n, "context": c} for n, c in characters.items()]
