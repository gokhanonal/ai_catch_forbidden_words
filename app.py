from fastapi import FastAPI
from detector.regex_detector import regex_detect
from detector.fuzzy_detector import fuzzy_detect
from detector.semantic_detector import semantic_detect
from detector.llm_detector import llm_detect
from detector.risk_engine import calculate_risk

app = FastAPI()

forbidden_list = [
    "yasadışı para kazanma",
    "kredi kartı çalmak",
    "dolandırıcılık",
    "hacklemek",
    "kumar",
    "www",
    "@",
    "http",
    "050",
    "053",
    ".com",
    ".tr",
    ".istanbul"
    ".net",
    ".ai",
    ".org",
    ".com.tr",
    ".gov.tr",
    "telefon no",
    "cep telefon no",
    "web sitesi link"
]

@app.post("/moderate")
def moderate(text: str):
    regex_hits = regex_detect(text, forbidden_list)
    fuzzy_hits = fuzzy_detect(text, forbidden_list)
    semantic_hits = semantic_detect(text, forbidden_list)
    llm_hit = llm_detect(text)

    risk = calculate_risk(
        regex_hits, fuzzy_hits, semantic_hits, llm_hit
    )

    return {
        "text": text,
        "risk_score": risk,
        "forbidden": risk >= 0.6,
        "details": {
            "regex": regex_hits or None,
            "fuzzy": fuzzy_hits or None,
            "semantic": semantic_hits or None,
            "llm": llm_hit
        }
    }

@app.post("/wise_detect")
def wise_detection(text: str):
    regex_hits = regex_detect(text, forbidden_list)
    fuzzy_hits = None
    semantic_hits = None
    llm_hit = None

    if regex_hits == []:
        fuzzy_hits = fuzzy_detect(text, forbidden_list)
        if fuzzy_hits == []:
            semantic_hits = semantic_detect(text, forbidden_list)
            if semantic_hits == []:
                llm_hit = llm_detect(text)


    return {
        "text": text,
        "details": {
            "regex": regex_hits,
            "fuzzy": fuzzy_hits,
            "semantic": semantic_hits,
            "llm": llm_hit
        }
    }

if __name__ == "__main__":
    FastAPI.run("app:app", host="0.0.0.0", port = "8000")