import spacy

nlp = spacy.load("en_core_web_sm")

HONORIFICS = {"Mr.", "Mrs.", "Ms.", "Miss", "Dr.", "Prof.", "Sir", "Madam"}

def extract_characters(text):
    doc = nlp(text)
    characters = set()

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            # Check if previous token is an honorific
            start_idx = ent.start
            if start_idx > 0:
                prev_token = doc[start_idx - 1]
                if prev_token.text in HONORIFICS:
                    characters.add(f"{prev_token.text} {ent.text.strip()}")
                    continue
            characters.add(ent.text.strip())

    # Cleanup (remove generic terms)
    blacklist = {"Clockmaker", "Secret"}
    characters = {c for c in characters if c not in blacklist}

    return sorted(characters)
