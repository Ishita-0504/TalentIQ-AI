import json

def load_candidates(file_path="data/candidates.jsonl"):
    candidates = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                candidates.append(json.loads(line))

    return candidates