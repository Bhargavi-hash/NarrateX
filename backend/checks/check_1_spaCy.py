import spacy
from spacy.lang.en.examples import sentences 

nlp = spacy.load("en_core_web_sm")
doc = nlp(sentences[0])
print(doc.text)
for token in doc:
    print(token.text, token.pos_, token.dep_)

# | Apple is looking at buying U.K. startup for $1 billion
# | Apple PROPN nsubj
# | is AUX aux
# | looking VERB ROOT
# | at ADP prep
# | buying VERB pcomp
# | U.K. PROPN dobj
# | startup NOUN dep
# | for ADP prep
# | $ SYM quantmod
# | 1 NUM compound
# | billion NUM pobj