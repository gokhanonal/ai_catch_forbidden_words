from rapidfuzz import fuzz

def fuzzy_detect(text, forbidden_list, threshold=85):
    hits = []
    for phrase in forbidden_list:
        score = fuzz.partial_ratio(phrase.lower(), text.lower())
        if score >= threshold:
            hits.append((phrase, score))
    return hits
