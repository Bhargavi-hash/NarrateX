import spacy

nlp = spacy.load("en_core_web_sm")

# Your own text goes here:
text = "Alice said hello. Bob cried. Celeste ran. A dog barked. The dog's owner, Jack said 'What's happening here?'"

doc = nlp(text)
print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)

print("\nProper Nouns (PROPN) in the text:")

# Listing down all the PROPN tokens
for token in doc:
    if token.pos_ == "PROPN":
        print(token.text)
