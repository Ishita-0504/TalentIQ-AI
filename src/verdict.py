def recruiter_verdict(result):

    score = result["final_score"]
    semantic = result["semantic_score"]
    skills = result["skill_score"]
    experience = result["experience_score"]
    behaviour = result["behaviour_score"]

    strengths = []
    gaps = []

    # -------- Strengths --------
    if semantic >= 80:
        strengths.append("Excellent semantic alignment with the job description.")

    if skills >= 70:
        strengths.append("Possesses most of the required technical skills.")

    if experience >= 70:
        strengths.append("Strong relevant professional experience.")

    if behaviour >= 70:
        strengths.append("Positive behavioural and professional indicators.")

    # -------- Gaps --------
    if semantic < 60:
        gaps.append("Limited alignment with the job description.")

    if skills < 50:
        gaps.append("Several required skills are missing.")

    if experience < 50:
        gaps.append("Professional experience is below expectations.")

    if behaviour < 50:
        gaps.append("Behavioural indicators could be stronger.")

    return strengths, gaps