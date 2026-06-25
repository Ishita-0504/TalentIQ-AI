def explain_candidate(candidate, scores):

    reasons = []

    if scores["semantic_score"] >= 40:
        reasons.append(
            f"Good semantic match ({scores['semantic_score']:.1f}/100) with the job description."
        )

    if scores["experience_score"] >= 20:
        reasons.append(
            "Relevant professional experience."
        )

    if scores["skill_score"] >= 10:
        reasons.append(
            "Possesses several required skills."
        )

    if scores["behaviour_score"] >= 60:
        reasons.append(
            "Strong recruiter engagement and profile quality."
        )

    signals = candidate.get("redrob_signals", {})

    if signals.get("github_activity_score", 0) >= 7:
        reasons.append("Highly active GitHub profile.")

    if signals.get("saved_by_recruiters_30d", 0) >= 3:
        reasons.append("Frequently viewed/saved by recruiters.")

    if signals.get("open_to_work_flag"):
        reasons.append("Currently open to work.")

    return reasons