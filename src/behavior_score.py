import json
from datetime import datetime


def calculate_behavior_score(candidate):

    signals = candidate.get("redrob_signals", {})

    score = 0

    # Open To Work
    if signals.get("open_to_work_flag", False):
        score += 20

    # Recruiter Response Rate
    response_rate = signals.get(
        "recruiter_response_rate", 0
    )

    score += response_rate * 20

    # Interview Completion
    interview_rate = signals.get(
        "interview_completion_rate", 0
    )

    score += interview_rate * 20

    # GitHub Activity
    github_score = signals.get(
        "github_activity_score", -1
    )

    if github_score >= 0:
        score += github_score * 0.2

    # Notice Period
    notice_days = signals.get(
        "notice_period_days", 180
    )

    if notice_days <= 30:
        score += 15

    elif notice_days <= 60:
        score += 10

    elif notice_days <= 90:
        score += 5

    # Last Active Date

    last_active = signals.get(
        "last_active_date"
    )

    if last_active:

        try:

            last_active_date = datetime.strptime(
                last_active,
                "%Y-%m-%d"
            )

            days_inactive = (
                datetime.now() -
                last_active_date
            ).days

            if days_inactive <= 30:
                score += 15

            elif days_inactive <= 90:
                score += 10

            elif days_inactive <= 180:
                score += 5

        except:
            pass

    return round(score, 2)


if __name__ == "__main__":

    with open(
        "data/candidates.jsonl",
        "r",
        encoding="utf-8"
    ) as f:

        candidate = json.loads(
            f.readline()
        )

    behavior_score = calculate_behavior_score(
        candidate
    )

    print(
        "Behavior Score:",
        behavior_score
    )