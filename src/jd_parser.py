import re

from src.jd_database.roles import ROLES
from src.jd_database.skills import SKILLS
from src.jd_database.education import EDUCATION
from src.jd_database.industries import INDUSTRIES
from src.jd_database.aliases import ALIASES


# ======================================================
# EXPERIENCE
# ======================================================

def extract_experience(text):

    patterns = [

        r'(\d+\s*[-–]\s*\d+\+?\s*(?:years?|yrs?))',

        r'(\d+\s*to\s*\d+\+?\s*(?:years?|yrs?))',

        r'(\d+\+\s*(?:years?|yrs?))',

        r'(minimum\s*\d+\s*(?:years?|yrs?))',

        r'(\d+\s*(?:years?|yrs?)\s*experience)',

        r'(\d+\s*(?:years?|yrs?))'
    ]

    for pattern in patterns:

        match = re.search(pattern, text, re.IGNORECASE)

        if match:
            return match.group(1).strip()

    return "Not Specified"

# ======================================================
# EDUCATION
# ======================================================

def extract_education(text):

    # Normalize text
    text = text.replace("’", "'")
    text = text.replace("‘", "'")

    # Generic Bachelor's
    match = re.search(
        r"bachelor'?s\s+degree(?:\s+in\s+([^.\n]+))?",
        text,
        re.IGNORECASE
    )

    if match:
        if match.group(1):
            return "Bachelor's Degree in " + match.group(1).strip()
        return "Bachelor's Degree"

    # Generic Master's
    match = re.search(
        r"master'?s\s+degree(?:\s+in\s+([^.\n]+))?",
        text,
        re.IGNORECASE
    )

    if match:
        if match.group(1):
            return "Master's Degree in " + match.group(1).strip()
        return "Master's Degree"

    # Other degrees
    for degree in sorted(EDUCATION, key=len, reverse=True):
        pattern = r"\b" + re.escape(degree) + r"\b"

        if re.search(pattern, text, re.IGNORECASE):
            return degree

    return "Not Specified"

# ======================================================
# ROLE
# ======================================================

def extract_role(text):

    for role in ROLES:

        if role.lower() in text.lower():

            return role

    return "Not Specified"


# ======================================================
# INDUSTRY
# ======================================================

def extract_industry(text):

    text = text.lower()

    for industry in INDUSTRIES:

        pattern = r"\b" + re.escape(industry.lower()) + r"\b"

        if re.search(pattern, text):
            return industry

    return "Not Specified"


# ======================================================
# SKILLS
# ======================================================

def extract_skills(text):

    text = text.lower()

    detected = set()

    # Alias matching

    for canonical, aliases in ALIASES.items():

        for alias in aliases:

            if re.search(r'\b' + re.escape(alias.lower()) + r'\b', text):

                detected.add(canonical)

    # Direct skill matching

    for skill in SKILLS:

        if re.search(r'\b' + re.escape(skill.lower()) + r'\b', text):

            detected.add(skill)

    return sorted(list(detected))


# ======================================================
# MAIN PARSER
# ======================================================

def analyze_job_description(jd):

    return {

        "role": extract_role(jd),

        "industry": extract_industry(jd),

        "experience": extract_experience(jd),

        "education": extract_education(jd),

        "skills": extract_skills(jd)

    }