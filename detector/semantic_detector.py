from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer(
    "emrecan/bert-base-turkish-cased-mean-nli-stsb-tr"
)

def semantic_detect(text, forbidden_list, threshold=0.65):
    emb_text = model.encode(text, convert_to_tensor=True)
    emb_forbidden = model.encode(forbidden_list, convert_to_tensor=True)

    scores = util.cos_sim(emb_text, emb_forbidden)[0]
    hits = []

    for i, score in enumerate(scores):
        if score >= threshold:
            hits.append((forbidden_list[i], float(score)))

    return hits
