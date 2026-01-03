import re

def regex_detect(text, forbidden_list):
    hits = []
    text = text.lower()
    for phrase in forbidden_list:
        if re.search(rf"\b{re.escape(phrase)}\b", text):
            hits.append(phrase)
    return hits
