import json
import heapq
import time
import csv

from behavior_score import (
    calculate_behavior_score
)

from consistency_score import (
    calculate_consistency_score
)

from candidate_feature_engine import (
    calculate_feature_score
)


def calculate_pre_rank_score(candidate):

    behavior_score = calculate_behavior_score(
        candidate
    )

    consistency_score = calculate_consistency_score(
        candidate
    )

    feature_score = calculate_feature_score(
        candidate
    )

    final_score = (

        0.40 * feature_score +

        0.30 * behavior_score +

        0.30 * consistency_score

    )

    return round(
        final_score,
        2
    )


if __name__ == "__main__":

    start_time = time.time()

    top_candidates = []

    with open(
        "data/candidates.jsonl",
        "r",
        encoding="utf-8"
    ) as f:

        for line_number, line in enumerate(f):

            candidate = json.loads(
                line
            )

            score = calculate_pre_rank_score(
                candidate
            )

            record = (
                score,
                candidate["candidate_id"]
            )

            if len(top_candidates) < 1000:

                heapq.heappush(
                    top_candidates,
                    record
                )

            else:

                heapq.heappushpop(
                    top_candidates,
                    record
                )

            if (line_number + 1) % 10000 == 0:

                print(
                    f"Processed {line_number + 1} candidates"
                )

    top_candidates = sorted(
        top_candidates,
        reverse=True
    )

    with open(
        "outputs/top1000_candidates.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as csvfile:

        writer = csv.writer(
            csvfile
        )

        writer.writerow(
            [
                "candidate_id",
                "pre_rank_score"
            ]
        )

        for row in top_candidates:

            writer.writerow(
                [
                    row[1],
                    row[0]
                ]
            )

    print("\n")

    print(
        "Rank 100 Candidate:"
    )

    print(
        top_candidates[99]
    )

    print("\n")

    print(
        "Rank 1000 Candidate:"
    )

    print(
        top_candidates[999]
    )

    print()

    print(
        "TOP 10 PRE-RANKED CANDIDATES\n"
    )

    for rank, row in enumerate(
        top_candidates[:10],
        start=1
    ):

        print(
            f"{rank}. {row[1]} Score: {row[0]}"
        )

    end_time = time.time()

    print()

    print(
        f"Runtime: {round(end_time - start_time, 2)} seconds"
    )

    print(
        "\nCSV saved to outputs/top1000_candidates.csv"
    )