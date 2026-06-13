import json


def count_candidates(file_path):
    count = 0

    with open(file_path, "r", encoding="utf-8") as f:
        for _ in f:
            count += 1

    return count


def get_first_candidate(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        first_line = f.readline()
        return json.loads(first_line)


if __name__ == "__main__":

    file_path = "data/candidates.jsonl"

    total = count_candidates(file_path)

    first_candidate = get_first_candidate(file_path)

    print("Total Candidates:", total)

    print("\nFirst Candidate ID:")
    print(first_candidate["candidate_id"])