import json


def build_candidate_text(candidate):

    profile = candidate.get("profile", {})

    headline = profile.get("headline", "")
    summary = profile.get("summary", "")
    current_title = profile.get("current_title", "")
    years_of_experience = profile.get("years_of_experience", "")

    skills = []

    for skill in candidate.get("skills", []):
        skills.append(skill.get("name", ""))

    career_descriptions = []

    for job in candidate.get("career_history", []):
        title = job.get("title", "")
        company = job.get("company", "")
        description = job.get("description", "")

        career_descriptions.append(
            f"{title} at {company}. {description}"
        )

    combined_text = f"""
    Headline:
    {headline}

    Summary:
    {summary}

    Current Title:
    {current_title}

    Years Of Experience:
    {years_of_experience}

    Skills:
    {' '.join(skills)}

    Career History:
    {' '.join(career_descriptions)}
    """

    return combined_text.strip()


if __name__ == "__main__":

    with open("data/candidates.jsonl", "r", encoding="utf-8") as f:
        first_candidate = json.loads(f.readline())

    text = build_candidate_text(first_candidate)

    print(text[:1500])