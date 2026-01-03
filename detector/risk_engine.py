def calculate_risk(regex_hits, fuzzy_hits, semantic_hits, llm_hit):
    score = 0.0

    if regex_hits:
        score += 0.4
    if fuzzy_hits:
        score += 0.3
    if semantic_hits:
        score += 0.4
    if llm_hit:
        score += 0.5

    return min(score, 1.0)
