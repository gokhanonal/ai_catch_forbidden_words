def calculate_risk(
        regex_hits,
        fuzzy_hits,
        qdrant_hits,
        semantic_hits,
        llm_hit):

    score = 0.0

    if regex_hits:
        score += 0.4
    if fuzzy_hits:
        score += 0.3
    if qdrant_hits:
        score += 0.2
    if semantic_hits:
        score += 0.3
    if llm_hit:
        score += 0.8

    return min(score, 1.0)
