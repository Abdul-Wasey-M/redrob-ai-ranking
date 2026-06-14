import json


TARGET_LOCATIONS = [
    "pune",
    "noida",
    "delhi",
    "delhi ncr",
    "gurgaon",
    "gurugram",
    "hyderabad",
    "mumbai"
]


RETRIEVAL_KEYWORDS = [
    "retrieval",
    "ranking",
    "search",
    "recommendation",
    "recommender",
    "embedding",
    "embeddings",
    "vector",
    "semantic search",
    "candidate matching",
    "matching system"
]


VECTOR_DB_KEYWORDS = [
    "pinecone",
    "weaviate",
    "qdrant",
    "milvus",
    "faiss",
    "elasticsearch",
    "opensearch"
]


SERVICE_COMPANIES = [
    "tcs",
    "infosys",
    "wipro",
    "cognizant",
    "capgemini",
    "mindtree",
    "hcl",
    "tech mahindra"
]


def calculate_feature_score(candidate):

    score = 0

    profile = candidate.get("profile", {})

    years = profile.get(
        "years_of_experience",
        0
    )

    current_title = profile.get(
        "current_title",
        ""
    ).lower()

    location = profile.get(
        "location",
        ""
    ).lower()

    summary = profile.get(
        "summary",
        ""
    ).lower()

    # -----------------
    # Experience Fit
    # -----------------

    if 5 <= years <= 9:
        score += 20

    elif 4 <= years <= 10:
        score += 10

    # -----------------
    # Title Fit
    # -----------------

    title_keywords = [
        "ai",
        "ml",
        "machine learning",
        "data scientist",
        "search",
        "recommendation",
        "backend engineer"
    ]

    if any(
        keyword in current_title
        for keyword in title_keywords
    ):
        score += 15

    # -----------------
    # Location Fit
    # -----------------

    if any(
        city in location
        for city in TARGET_LOCATIONS
    ):
        score += 10

    # -----------------
    # Retrieval Signals
    # -----------------

    retrieval_hits = 0

    text_blob = summary

    for job in candidate.get(
        "career_history",
        []
    ):

        text_blob += " "

        text_blob += job.get(
            "description",
            ""
        ).lower()

    for keyword in RETRIEVAL_KEYWORDS:

        if keyword in text_blob:
            retrieval_hits += 1

    score += min(
        retrieval_hits * 3,
        20
    )

    # -----------------
    # Vector DB Signals
    # -----------------

    vector_hits = 0

    for skill in candidate.get(
        "skills",
        []
    ):

        skill_name = skill.get(
            "name",
            ""
        ).lower()

        if skill_name in VECTOR_DB_KEYWORDS:
            vector_hits += 1

    score += min(
        vector_hits * 5,
        15
    )

    # -----------------
    # Service Company Penalty
    # -----------------

    company_name = profile.get(
        "current_company",
        ""
    ).lower()

    if company_name in SERVICE_COMPANIES:
        score -= 10

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

    score = calculate_feature_score(
        candidate
    )

    print(
        "Feature Score:",
        score
    )