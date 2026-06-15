from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from docx import Document
import json

from build_candidate_text import build_candidate_text

# LOAD MODEL ONLY ONCE
model = SentenceTransformer("all-MiniLM-L6-v2")


def read_job_description(docx_path):

    doc = Document(docx_path)

    text = []

    for para in doc.paragraphs:
        text.append(para.text)

    return "\n".join(text)


def get_first_candidate(candidate_file):

    with open(candidate_file, "r", encoding="utf-8") as f:
        first_line = f.readline()

    return json.loads(first_line)


def calculate_similarity(job_text, candidate_text):

    embeddings = model.encode(
        [job_text, candidate_text],
        convert_to_numpy=True
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return similarity


if __name__ == "__main__":

    job_text = read_job_description(
        "docs/job_description.docx"
    )

    candidate = get_first_candidate(
        "data/candidates.jsonl"
    )

    candidate_text = build_candidate_text(
        candidate
    )

    score = calculate_similarity(
        job_text,
        candidate_text
    )

    print("\nCandidate ID:")
    print(candidate["candidate_id"])

    print("\nSimilarity Score:")
    print(round(score, 4))