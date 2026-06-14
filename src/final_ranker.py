import json

from semantic_ranker import (
    calculate_similarity,
    read_job_description
)

from build_candidate_text import (
    build_candidate_text
)

from behavior_score import (
    calculate_behavior_score
)

from consistency_score import (
    calculate_consistency_score
)

from candidate_feature_engine import (
    calculate_feature_score
)


def calculate_final_score(
    candidate,
    job_text
):

    candidate_text = build_candidate_text(
        candidate
    )

    semantic_score = calculate_similarity(
        job_text,
        candidate_text
    )

    behavior_score = calculate_behavior_score(
        candidate
    )

    consistency_score = calculate_consistency_score(
        candidate
    )

    feature_score = calculate_feature_score(
        candidate
    )

    # ------------------------
    # Normalization
    # ------------------------

    semantic_score = semantic_score * 100

    feature_score = min(
        feature_score,
        60
    )

    feature_score = (
        feature_score / 60
    ) * 100

    # ------------------------
    # Weighted Score
    # ------------------------

    final_score = (

        0.35 * semantic_score +

        0.25 * feature_score +

        0.20 * behavior_score +

        0.20 * consistency_score

    )

    return {

        "semantic_score":
        round(
            semantic_score,
            2
        ),

        "behavior_score":
        round(
            behavior_score,
            2
        ),

        "consistency_score":
        round(
            consistency_score,
            2
        ),

        "feature_score":
        round(
            feature_score,
            2
        ),

        "final_score":
        round(
            final_score,
            2
        )
    }


if __name__ == "__main__":

    job_text = read_job_description(
        "docs/job_description.docx"
    )

    with open(
        "data/candidates.jsonl",
        "r",
        encoding="utf-8"
    ) as f:

        candidate = json.loads(
            f.readline()
        )

    results = calculate_final_score(
        candidate,
        job_text
    )

    print()

    for key, value in results.items():

        print(
            f"{key}: {value}"
        )