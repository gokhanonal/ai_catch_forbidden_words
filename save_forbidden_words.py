from detector.qdrant_loader import create_collection, load_phrases
from forbidden_words import forbidden_list

create_collection()
load_phrases(forbidden_list)
