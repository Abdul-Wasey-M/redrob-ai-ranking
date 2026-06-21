import csv
import time

from semantic_ranker import (
    calculate_similarity,
    read_job_description
)

from load_top_candidates import (
    load_top_candidate_ids,
    load_top_candidates
)

from build_candidate_text import (
    build_candidate_text
)


def load_pre_rank_scores(

    csv_file="outputs/top1000_candidates.csv"

):

    scores = {}

    with open(
        csv_file,
        "r",
        encoding="utf-8"
    ) as f:

        reader = csv.DictReader(
            f
        )

        for row in reader:

            scores[
                row["candidate_id"]
            ] = float(
                row["pre_rank_score"]
            )

    return scores


if __name__ == "__main__":

    start_time = time.time()

    print(
        "\nLoading Job Description..."
    )

    job_text = read_job_description(
        "docs/job_description.docx"
    )

    print(
        "Loading Top Candidates..."
    )

    candidate_ids = (
        load_top_candidate_ids()
    )

    candidates = (
        load_top_candidates(
            candidate_ids
        )
    )

    pre_rank_scores = (
        load_pre_rank_scores()
    )

    final_results = []

    print(
        f"Loaded {len(candidates)} candidates"
    )

    for index, candidate in enumerate(
        candidates,
        start=1
    ):

        candidate_text = (
            build_candidate_text(
                candidate
            )
        )

        semantic_score = (
            calculate_similarity(
                job_text,
                candidate_text
            )
            * 100
        )

        pre_rank_score = (
            pre_rank_scores[
                candidate[
                    "candidate_id"
                ]
            ]
        )

        final_score = (

            0.60 *
            semantic_score +

            0.40 *
            pre_rank_score

        )

        final_results.append(

            (
                candidate[
                    "candidate_id"
                ],
                round(
                    semantic_score,
                    2
                ),
                round(
                    pre_rank_score,
                    2
                ),
                round(
                    final_score,
                    2
                )
            )

        )

        if index % 100 == 0:

            print(
                f"Processed "
                f"{index} "
                f"candidates"
            )

    final_results.sort(
        key=lambda x: x[3],
        reverse=True
    )

    with open(
        "outputs/top100_candidates.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(
            f
        )

        writer.writerow(
            [
                "candidate_id",
                "semantic_score",
                "pre_rank_score",
                "final_score"
            ]
        )

        for row in final_results[:100]:

            writer.writerow(
                row
            )

    print()

    print(
        "TOP 10 FINAL CANDIDATES\n"
    )

    for rank, row in enumerate(
        final_results[:10],
        start=1
    ):

        print(
            f"{rank}. "
            f"{row[0]} "
            f"Final Score: "
            f"{row[3]}"
        )

    end_time = time.time()

    print()

    print(
        f"Runtime: "
        f"{round(end_time - start_time,2)} "
        f" seconds"
    )

    print(
        "\nSaved:"
    )

    print(
        "outputs/top100_candidates.csv"
    )