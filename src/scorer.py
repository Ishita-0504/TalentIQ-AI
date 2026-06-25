import numpy as np

def similarity_score(job_embedding, candidate_embedding):
    return float(np.dot(job_embedding, candidate_embedding))