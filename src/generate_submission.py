import csv

from load_top_candidates import (
    load_top_candidate_ids,
    load_top_candidates
)

from reasoning_generator import (
    generate_reasoning
)


def load_top100_scores():

    scores = {}

    with open(
        "outputs/top100_candidates.csv",
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
                row["final_score"]
            )

    return scores


if __name__ == "__main__":

    print(
        "\nLoading Top 100..."
    )

    scores = (
        load_top100_scores()
    )

    candidate_ids = list(
        scores.keys()
    )

    candidates = (
        load_top_candidates(
            candidate_ids
        )
    )

    candidate_map = {

        candidate[
            "candidate_id"
        ]: candidate

        for candidate in candidates

    }

    output_rows = []

    for rank, candidate_id in enumerate(
        candidate_ids,
        start=1
    ):

        candidate = (
            candidate_map[
                candidate_id
            ]
        )

        reasoning = (
            generate_reasoning(
                candidate
            )
        )

        output_rows.append(
            [
                candidate_id,
                rank,
                scores[
                    candidate_id
                ],
                reasoning
            ]
        )

    with open(
        "outputs/final_submission.csv",
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
                "rank",
                "score",
                "reasoning"
            ]
        )

        writer.writerows(
            output_rows
        )

    print()

    print(
        "Submission file saved:"
    )

    print(
        "outputs/final_submission.csv"
    )

    print()

    print(
        f"Total Candidates: "
        f"{len(output_rows)}"
    )