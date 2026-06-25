AI_KEYWORDS = [
    "ai",
    "machine learning",
    "ml",
    "data scientist",
    "retrieval",
    "ranking",
    "recommendation",
    "nlp",
    "llm",
    "deep learning",
]


def experience_score(candidate):
    score = 0

    for job in candidate.get("career_history", []):
        text = (
            str(job.get("title", "")) + " " +
            str(job.get("description", ""))
        ).lower()

        for keyword in AI_KEYWORDS:
            if keyword in text:
                score += 10

    return min(score, 100)