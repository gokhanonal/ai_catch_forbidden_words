from sentence_transformers import SentenceTransformer
from detector.qdrant_client import qdrant

COLLECTION_NAME = "forbidden_tr"

model = SentenceTransformer(
    "emrecan/bert-base-turkish-cased-mean-nli-stsb-tr"
)

def qdrant_detect(text: str, threshold: float = 0.70, limit: int = 5):
    embedding = model.encode(text).tolist()

    hits = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=embedding,
        limit=limit,
        with_payload=True
    )

    results = []
    for point in hits.points:
        if point.score >= threshold:
            results.append({
                "phrase": point.payload.get("text"),
                "score": point.score,
                "category": point.payload.get("category")
            })

    return results
