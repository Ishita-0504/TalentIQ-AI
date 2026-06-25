def skill_score(candidate, jd):

    skills = candidate.get("skills", [])

    candidate_skills = []

    for skill in skills:

        if isinstance(skill, dict):

            candidate_skills.append(
                skill.get("name","").lower()
            )

        else:

            candidate_skills.append(
                str(skill).lower()
            )

    matches = 0

    for skill in candidate_skills:

        if skill in jd:

            matches += 1

    return min(matches * 15,100)