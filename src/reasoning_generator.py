import json

from load_top_candidates import (
load_top_candidate_ids,
load_top_candidates
)

def generate_reasoning(candidate):

    profile = candidate["profile"]

    skills = candidate.get(
        "skills",
        []
    )

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    title = profile.get(
        "current_title",
        ""
    )

    experience = profile.get(
        "years_of_experience",
        0
    )

    skill_names = [

        skill["name"]

        for skill in skills

    ]

    retrieval_keywords = [

        "FAISS",
        "BM25",
        "Embeddings",
        "RAG",
        "Pinecone",
        "Milvus",
        "Weaviate",
        "Qdrant",
        "Sentence Transformers",
        "Learning to Rank"
    ]

    matched_skills = []

    for skill in skill_names:

        if skill in retrieval_keywords:

            matched_skills.append(
                skill
            )

    reasoning_parts = []

    reasoning_parts.append(

        f"{title} with "
        f"{experience} years of "
        f"professional experience"

    )

    ai_titles = [

        "ai",
        "machine learning",
        "ml",
        "search",
        "recommendation",
        "data scientist",
        "nlp"

    ]

    title_lower = title.lower()

    aligned_title = False

    for keyword in ai_titles:

        if keyword in title_lower:

            aligned_title = True
            break

    if matched_skills:

        reasoning_parts.append(

            "Strong match for Redrob's "
            "retrieval and ranking needs "
            "through experience with "
            + ", ".join(
                matched_skills[:4]
            )

        )

        if aligned_title:

            reasoning_parts.append(

                "Current role is closely aligned "
                "with AI/ML and retrieval systems"

            )

        else:

            reasoning_parts.append(

                "Demonstrates relevant retrieval "
                "skills despite a non-traditional "
                "current title"

            )

    else:

        reasoning_parts.append(

            "Demonstrates relevant software "
            "engineering experience, though "
            "retrieval-specific experience is "
            "less visible in the profile"

        )

    response_rate = signals.get(
        "recruiter_response_rate",
        0
    )

    if response_rate >= 0.70:

        reasoning_parts.append(

            "High recruiter response rate"

        )

    github_score = signals.get(
        "github_activity_score",
        -1
    )

    if github_score >= 80:

        reasoning_parts.append(

            "Strong GitHub activity"

        )

    open_to_work = signals.get(
        "open_to_work_flag",
        False
    )

    if open_to_work:

        reasoning_parts.append(

            "Actively open to new opportunities"

        )

    return ". ".join(
        reasoning_parts
    ) + "."

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