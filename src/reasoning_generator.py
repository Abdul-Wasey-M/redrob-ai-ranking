import json

from load_top_candidates import (
    load_top_candidate_ids,
    load_top_candidates
)


def generate_reasoning(candidate):

    reasons = []

    profile = candidate["profile"]

    skills = candidate.get(
        "skills",
        []
    )

    career_history = candidate.get(
        "career_history",
        []
    )

    title = profile.get(
        "current_title",
        ""
    ).lower()

    experience = profile.get(
        "years_of_experience",
        0
    )

    skill_names = [

        skill["name"].lower()

        for skill in skills

    ]

    retrieval_keywords = [

        "faiss",
        "bm25",
        "embeddings",
        "rag",
        "pinecone",
        "milvus",
        "weaviate",
        "qdrant",
        "vector search",
        "sentence transformers"
    ]

    matched_skills = []

    for keyword in retrieval_keywords:

        if keyword in skill_names:

            matched_skills.append(
                keyword
            )

    if matched_skills:

        reasons.append(

            "Relevant retrieval skills: "
            + ", ".join(
                matched_skills[:4]
            )

        )

    if experience >= 5:

        reasons.append(

            f"{experience} years of professional experience"

        )

    if (

        "engineer" in title

        or

        "machine learning" in title

    ):

        reasons.append(

            "Current role aligned with AI/ML engineering"

        )

    if len(career_history) >= 2:

        reasons.append(

            "Demonstrated experience across multiple organizations"

        )

    if not reasons:

        reasons.append(

            "General profile match"

        )

    return " | ".join(
        reasons
    )


if __name__ == "__main__":

    candidate_ids = (
        load_top_candidate_ids()
    )

    candidates = (
        load_top_candidates(
            candidate_ids
        )
    )

    print()

    print(
        "SAMPLE REASONING\n"
    )

    for candidate in candidates[:5]:

        print(
            candidate[
                "candidate_id"
            ]
        )

        print(

            generate_reasoning(
                candidate
            )

        )

        print()