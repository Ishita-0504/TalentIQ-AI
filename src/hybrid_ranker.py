import numpy as np

from src.preprocessor import candidate_to_text
from src.embeddings import get_embedding
from src.scorer import similarity_score
from src.experience import experience_score
from src.skills import skill_score
from src.behaviour import behaviour_score


def rank_candidates(candidates, job_description):

    # Embed the job description once
    job_embedding = get_embedding(job_description)

    job_description_lower = job_description.lower()

# Compute semantic similarity for ALL candidates at once
    embeddings = np.array([c["_embedding"] for c in candidates])

    semantic_scores = np.dot(embeddings, job_embedding) * 100

    ranked = []

    for candidate, semantic in zip(candidates, semantic_scores):

    # Other scores
        experience = experience_score(candidate)
        skills = skill_score(candidate, job_description_lower)
        behaviour = behaviour_score(candidate)

        # Final weighted score
        final_score = (
            semantic * 0.40 +
            experience * 0.25 +
            skills * 0.20 +
            behaviour * 0.15
        )

        ranked.append({
            "candidate_id": candidate["candidate_id"],
            "semantic_score": round(semantic, 2),
            "experience_score": experience,
            "skill_score": skills,
            "behaviour_score": behaviour,
            "final_score": round(final_score, 2)
        })

    ranked.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    return ranked