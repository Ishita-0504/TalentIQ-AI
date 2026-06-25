def candidate_to_text(candidate):
    profile = candidate.get("profile", {})

    text = []

    # Headline
    if profile.get("headline"):
        text.append(profile["headline"])

    # Summary
    if profile.get("summary"):
        text.append(profile["summary"])

    # Career History
    for job in candidate.get("career_history", []):
        if job.get("title"):
            text.append(job["title"])

        if job.get("company"):
            text.append(job["company"])

        if job.get("description"):
            text.append(job["description"])

    # Skills
    skills = candidate.get("skills", [])

    if isinstance(skills, list):
        for skill in skills:
            if isinstance(skill, dict):
                if skill.get("name"):
                    text.append(skill["name"])
            elif isinstance(skill, str):
                text.append(skill)

    return "\n".join(text)