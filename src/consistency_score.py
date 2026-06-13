import json


def calculate_consistency_score(candidate):

    score = 100

    profile = candidate.get("profile", {})
    summary = profile.get("summary", "").lower()

    skills = candidate.get("skills", [])

    # Rule 1:
    # Expert skill with very low experience

    for skill in skills:

        proficiency = skill.get(
            "proficiency",
            ""
        ).lower()

        duration = skill.get(
            "duration_months",
            0
        )

        if (
            proficiency == "expert"
            and duration < 12
        ):
            score -= 15

    # Rule 2:
    # Claims advanced AI skills
    # but summary says learning ML

    learning_keywords = [
        "learning ml",
        "learning machine learning",
        "transitioning into ai",
        "building competence",
        "new to ml"
    ]

    advanced_ai_skills = [
        "fine-tuning llms",
        "nlp",
        "rag",
        "lora",
        "vector databases",
        "retrieval"
    ]

    summary_learning = any(
        phrase in summary
        for phrase in learning_keywords
    )

    ai_skill_count = 0

    for skill in skills:

        name = skill.get(
            "name",
            ""
        ).lower()

        proficiency = skill.get(
            "proficiency",
            ""
        ).lower()

        if (
            name in advanced_ai_skills
            and proficiency in [
                "advanced",
                "expert"
            ]
        ):
            ai_skill_count += 1

    if (
        summary_learning
        and ai_skill_count >= 2
    ):
        score -= 20

    # Rule 3:
    # Too many expert skills

    expert_count = 0

    for skill in skills:

        if (
            skill.get(
                "proficiency",
                ""
            ).lower()
            == "expert"
        ):
            expert_count += 1

    if expert_count >= 10:
        score -= 20

    if score < 0:
        score = 0

    return score


if __name__ == "__main__":

    with open(
        "data/candidates.jsonl",
        "r",
        encoding="utf-8"
    ) as f:

        candidate = json.loads(
            f.readline()
        )

    score = calculate_consistency_score(
        candidate
    )

    print(
        "Consistency Score:",
        score
    )