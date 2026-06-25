import pickle

from src.data_loader import load_candidates


def load_candidates_with_embeddings():

    candidates = load_candidates("data/candidates.jsonl")

    with open("data/candidate_embeddings.pkl", "rb") as f:
        embeddings = pickle.load(f)

    for candidate, embedding in zip(candidates, embeddings):
        candidate["_embedding"] = embedding

    return candidates




