import json
import time

from final_ranker import (
    calculate_final_score
)

from semantic_ranker import (
    read_job_description
)


def load_candidates(
    file_path,
    limit=100
):

    candidates = []

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as f:

        for i, line in enumerate(f):

            if i >= limit:
                break

            candidates.append(
                json.loads(line)
            )

    return candidates


if __name__ == "__main__":

    start_time = time.time()

    print(
        "\nLoading Job Description..."
    )

    job_text = read_job_description(
        "docs/job_description.docx"
    )

    print(
        "Loading Candidates..."
    )

    candidates = load_candidates(
        "data/candidates.jsonl",
        limit=100
    )

    print(
        f"Loaded {len(candidates)} candidates\n"
    )

    results = []

    for candidate in candidates:

        score_data = calculate_final_score(
            candidate,
            job_text
        )

        results.append({

            "candidate_id":
            candidate[
                "candidate_id"
            ],

            "final_score":
            score_data[
                "final_score"
            ]
        })

    results.sort(
        key=lambda x:
        x["final_score"],
        reverse=True
    )

    print(
        "TOP 10 CANDIDATES\n"
    )

    for rank, row in enumerate(
        results[:10],
        start=1
    ):

        print(
            f"{rank}. "
            f"{row['candidate_id']} "
            f"Score: "
            f"{row['final_score']}"
        )

    end_time = time.time()

    print(
        f"\nRuntime: "
        f"{round(end_time - start_time,2)} "
        f"seconds"
    )