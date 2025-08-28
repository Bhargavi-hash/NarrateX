# backend/tools/build_character_graph.py

import spacy
from collections import defaultdict

nlp = spacy.load("en_core_web_sm")

def build_character_graph(text, characters):
    """
    Build a simple co-occurrence graph of characters.
    Returns dict with nodes and edges:
    {
        "nodes": [{"id": "Alice"}, {"id": "Bob"}],
        "edges": [{"from": "Alice", "to": "Bob", "value": 1}, ...]
    }
    """
    doc = nlp(text)
    edges_count = defaultdict(int)

    for sent in doc.sents:
        sent_text_lower = sent.text.lower()
        # Find characters present in this sentence
        present = [c for c in characters if c.lower() in sent_text_lower]
        # Add edges between every pair
        if len(present) > 1:
            for i in range(len(present)):
                for j in range(i + 1, len(present)):
                    pair = tuple(sorted((present[i], present[j])))
                    edges_count[pair] += 1

    # Convert to frontend format
    nodes = [{"id": c} for c in characters]
    edges = [{"from": a, "to": b, "value": w} for (a, b), w in edges_count.items()]

    return {"nodes": nodes, "edges": edges}
