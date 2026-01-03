from fastapi import FastAPI
from detector.regex_detector import regex_detect
from detector.fuzzy_detector import fuzzy_detect
from detector.qdrant_detector import qdrant_detect
from detector.semantic_detector import semantic_detect
from detector.llm_detector import llm_detect
from detector.risk_engine import calculate_risk
from forbidden_words import forbidden_list

app = FastAPI()


@app.post("/full_detection")
def full_detection(text: str):
    regex_hits = regex_detect(text, forbidden_list)
    fuzzy_hits = fuzzy_detect(text, forbidden_list)
    qdrant_hits = qdrant_detect(text)
    semantic_hits = semantic_detect(text, forbidden_list)
    llm_hit = llm_detect(text)

    risk = calculate_risk(
        regex_hits, fuzzy_hits, qdrant_hits, semantic_hits, llm_hit
    )

    return {
        "text": text,
        "risk_score": risk,
        "forbidden": risk >= 0.3,
        "details": {
            "regex": regex_hits or None,
            "fuzzy": fuzzy_hits or None,
            "qdrant": qdrant_hits or None,
            "semantic": semantic_hits or None,
            "llm": llm_hit
        }
    }

@app.post("/wise_detect")
def wise_detection(text: str):
    regex_hits = regex_detect(text, forbidden_list)
    fuzzy_hits = None
    qdrant_hits = None
    semantic_hits = None
    llm_hit = None

    if regex_hits == []:
        fuzzy_hits = fuzzy_detect(text, forbidden_list)
        if fuzzy_hits == []:
            qdrant_hits = qdrant_detect(text)
            if qdrant_hits == []:
                semantic_hits = semantic_detect(text, forbidden_list)
                if semantic_hits == []:
                    llm_hit = llm_detect(text)

    risk = calculate_risk(
        regex_hits, fuzzy_hits, qdrant_hits, semantic_hits, llm_hit
    )

    return {
        "text": text,
        "risk_score": risk,
        "forbidden": risk >= 0.3,
        "details": {
            "regex": regex_hits,
            "fuzzy": fuzzy_hits,
            "qdrant": qdrant_hits,
            "semantic": semantic_hits,
            "llm": llm_hit
        }
    }

if __name__ == "__main__":
    FastAPI.run("app:app", host="0.0.0.0", port = "8000")