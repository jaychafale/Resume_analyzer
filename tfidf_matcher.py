from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def compute_resume_jd_match(resume_text: str, job_description: str) -> float:
    # ✅ Clean non-ASCII junk
    resume_text = re.sub(r'[^\x00-\x7F]+', ' ', resume_text)
    job_description = re.sub(r'[^\x00-\x7F]+', ' ', job_description)

    # ✅ Ensure content isn't too short
    if len(resume_text.strip()) < 100 or len(job_description.strip()) < 100:
        return 0.0

    # ✅ Preprocess to lowercase (optional redundancy)
    documents = [resume_text.lower(), job_description.lower()]

    # ✅ Vectorize and compute cosine similarity
    vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return round(float(similarity[0][0]) * 100, 2)  # As percentage
