import pickle

from src.data_loader import load_candidates
from src.preprocessor import candidate_to_text
from src.embeddings import get_embeddings

print("Loading candidates...")

candidates = load_candidates("data/candidates.jsonl")

print(f"Loaded {len(candidates)} candidates")

texts = [
    candidate_to_text(candidate)
    for candidate in candidates
]

print("Generating embeddings...")

embeddings = get_embeddings(texts)

print("Saving embeddings...")

with open("data/candidate_embeddings.pkl", "wb") as f:
    pickle.dump(embeddings, f)

print("Done!")