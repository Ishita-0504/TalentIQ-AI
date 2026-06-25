def behaviour_score(candidate):
    signals = candidate.get("redrob_signals", {})

    score = 0

    # Recruiter response rate (0-20)
    score += signals.get("recruiter_response_rate", 0) * 20

    # Interview completion (0-20)
    score += signals.get("interview_completion_rate", 0) * 20

    # Open to work (10 points)
    if signals.get("open_to_work_flag", False):
        score += 10

    # GitHub activity (0-10)
    score += min(signals.get("github_activity_score", 0), 10)

    # Saved by recruiters (0-10)
    score += min(signals.get("saved_by_recruiters_30d", 0), 10)

    # Profile completeness (0-20)
    score += signals.get("profile_completeness_score", 0) / 5

    # Profile views (0-10)
    score += min(signals.get("profile_views_received_30d", 0) / 5, 10)

    return round(min(score, 100), 2)