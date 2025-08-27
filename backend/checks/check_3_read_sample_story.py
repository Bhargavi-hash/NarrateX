import spacy

nlp = spacy.load("en_core_web_sm")

def extract_characters(text):
    doc = nlp(text)
    characters = set()

    # 1. Use Named Entities for people
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            characters.add(ent.text.strip())

    blacklist = {"Clockmaker", "Secret"}  # adjust as needed
    characters = {c for c in characters if c not in blacklist}

    return sorted(characters)


# Example
with open("../sample_short_stories/the_clockmakers_secret.txt", "r", encoding="utf-8") as f:
    text = f.read()

characters = extract_characters(text)

print("Characters in the story:")
for character in characters:
    print("-", character)
