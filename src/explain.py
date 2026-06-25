def explain_candidate(candidate, scores):

    reasons = []

    # Semantic match
    if scores["semantic_score"] >= 40:
        reasons.append(
            f"Strong semantic alignment with the job description ({scores['semantic_score']:.1f}/100)."
        )

    # Candidate skills
    skills = candidate.get("skills", [])

    skill_names = []

    for s in skills[:5]:

        if isinstance(s, dict):
            skill_names.append(s.get("name", ""))

        else:
            skill_names.append(str(s))

    if skill_names:
        reasons.append(
            "Key skills include: " + ", ".join(skill_names[:4]) + "."
        )

    # Career history
    career = candidate.get("career_history", [])

    if career:

        latest_role = career[0].get("title", "")

        if latest_role:
            reasons.append(
                f"Recent experience as {latest_role}."
            )

    # Behaviour signals
    signals = candidate.get("redrob_signals", {})

    if signals.get("github_activity_score", 0) >= 7:
        reasons.append(
            "Demonstrates strong GitHub activity."
        )

    if signals.get("saved_by_recruiters_30d", 0) >= 3:
        reasons.append(
            "Profile has attracted recruiter interest."
        )

    if signals.get("open_to_work_flag"):
        reasons.append(
            "Currently open to new opportunities."
        )

    return reasons

def find_gaps(candidate, jd_skills):

    candidate_skills = []

    for s in candidate.get("skills", []):
        if isinstance(s, dict):
            candidate_skills.append(
                s.get("name", "").lower()
            )
        else:
            candidate_skills.append(
                str(s).lower()
            )

    missing = []

    for skill in jd_skills:
        if skill.lower() not in candidate_skills:
            missing.append(skill)

    return missing[:3]