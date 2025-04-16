import spacy
from spacy.matcher import Matcher
from collections import defaultdict

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def extract_resume_entities(resume_text: str) -> dict:
    doc = nlp(resume_text)
    matcher = Matcher(nlp.vocab)

    # ===== Named Entity Extraction =====
    entities = defaultdict(list)
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE", "DATE"]:
            entities[ent.label_].append(ent.text)

    # ===== Custom Matcher for Designations =====
    designation_patterns = [
        [{"LOWER": "data"}, {"LOWER": "scientist"}],
        [{"LOWER": "senior"}, {"LOWER": "analyst"}],
        [{"LOWER": "software"}, {"LOWER": "engineer"}],
        [{"LOWER": "machine"}, {"LOWER": "learning"}, {"LOWER": "engineer"}],
        [{"LOWER": "product"}, {"LOWER": "manager"}],
    ]
    matcher.add("DESIGNATION", designation_patterns)

    # ===== Degree Patterns =====
    degree_patterns = [
        [{"LOWER": "bachelor"}, {"LOWER": "of"}, {"LOWER": "science"}],
        [{"LOWER": "master"}, {"LOWER": "of"}, {"LOWER": "science"}],
        [{"LOWER": "bsc"}],
        [{"LOWER": "msc"}],
        [{"LOWER": "phd"}],
    ]
    matcher.add("DEGREE", degree_patterns)

    # ===== Skill Keywords (simple match) =====
    skill_keywords = [
        "python", "machine learning", "deep learning", "nlp", "sql",
        "data science", "tensorflow", "pandas", "numpy", "java", "c++", "powerbi"
    ]
    skills_found = set()
    for token in doc:
        if token.text.lower() in [kw.lower() for kw in skill_keywords]:
            skills_found.add(token.text)

    # ===== Run matcher =====
    matches = matcher(doc)
    custom_entities = defaultdict(list)
    for match_id, start, end in matches:
        label = nlp.vocab.strings[match_id]
        span = doc[start:end]
        custom_entities[label].append(span.text)

    # ===== Final Output Dictionary =====
    results = {
        "Names": list(set(entities["PERSON"])),
        "Organizations": list(set(entities["ORG"])),
        "Designations": list(set(custom_entities["DESIGNATION"])),
        "Degrees": list(set(custom_entities["DEGREE"])),
        "Skills": list(skills_found),
    }

    return results
