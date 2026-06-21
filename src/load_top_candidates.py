import csv
import json


def load_top_candidate_ids(

    csv_file="outputs/top1000_candidates.csv"

):

    candidate_ids = set()

    with open(
        csv_file,
        "r",
        encoding="utf-8"
    ) as f:

        reader = csv.DictReader(
            f
        )

        for row in reader:

            candidate_ids.add(
                row["candidate_id"]
            )

    return candidate_ids


def load_top_candidates(

    candidate_ids,

    jsonl_file="data/candidates.jsonl"

):

    candidates = []

    with open(
        jsonl_file,
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            candidate = json.loads(
                line
            )

            if (
                candidate[
                    "candidate_id"
                ]
                in candidate_ids
            ):

                candidates.append(
                    candidate
                )

    return candidates


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
        f"Loaded "
        f"{len(candidates)} "
        f"top candidates"
    )

    print()

    print(
        "First Candidate:"
    )

    print(
        candidates[0][
            "candidate_id"
        ]
    )