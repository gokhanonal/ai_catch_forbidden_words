from sentence_transformers import SentenceTransformer
from qdrant_client.models import VectorParams, Distance, PointStruct
from detector.qdrant_client import qdrant

model = SentenceTransformer(
    "emrecan/bert-base-turkish-cased-mean-nli-stsb-tr"
)

COLLECTION_NAME = "forbidden_tr"

def create_collection():
    qdrant.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=768,
            distance=Distance.COSINE
        )
    )

def load_phrases(phrases):
    embeddings = model.encode(phrases)

    points = [
        PointStruct(
            id=i,
            vector=embeddings[i].tolist(),
            payload={
                "text": phrases[i],
                "type": "forbidden"
            }
        )
        for i in range(len(phrases))
    ]

    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )
