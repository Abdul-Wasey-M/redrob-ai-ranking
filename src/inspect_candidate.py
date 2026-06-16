import json


TARGET_ID = "CAND_0018499"


with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in f:

        candidate = json.loads(line)

        if (
            candidate["candidate_id"]
            == TARGET_ID
        ):

            print(
                "\nCandidate ID:"
            )

            print(
                candidate["candidate_id"]
            )

            print(
                "\nProfile:"
            )

            print(
                json.dumps(
                    candidate["profile"],
                    indent=2
                )
            )

            print(
                "\nCareer History:"
            )

            print(
                json.dumps(
                    candidate[
                        "career_history"
                    ],
                    indent=2
                )
            )

            print(
                "\nSkills:"
            )

            print(
                json.dumps(
                    candidate[
                        "skills"
                    ][:15],
                    indent=2
                )
            )

            print(
                "\nRedrob Signals:"
            )

            print(
                json.dumps(
                    candidate[
                        "redrob_signals"
                    ],
                    indent=2
                )
            )

            break