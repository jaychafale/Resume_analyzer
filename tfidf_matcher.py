from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def compute_resume_jd_match(resume_text: str, job_description: str) -> float:
    # ✅ Step 1: Clean inputs
    resume_text = re.sub(r'[^\x00-\x7F]+', ' ', resume_text)
    job_description = re.sub(r'[^\x00-\x7F]+', ' ', job_description)

    if len(resume_text.strip()) < 100 or len(job_description.strip()) < 100:
        print("❗ Input too short to compute TF-IDF.")
        return 0.0

    # ✅ Step 2: Preview inputs
    print("🔍 Resume length:", len(resume_text))
    print("🔍 JD length:", len(job_description))
    print("🔍 Resume preview:", resume_text[:300])
    print("🔍 JD preview:", job_description[:300])

    # ✅ Step 3: Token overlap before TF-IDF
    resume_tokens = set(resume_text.lower().split())
    jd_tokens = set(job_description.lower().split())
    common_tokens = resume_tokens & jd_tokens
    print("🔁 Common tokens:", common_tokens)
    print("🔁 Overlap count:", len(common_tokens))

    # ✅ Step 4: TF-IDF matching
    documents = [resume_text.lower(), job_description.lower()]
    vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)
    tfidf_matrix = vectorizer.fit_transform(documents)

    print("🔍 TF-IDF Vocabulary:", vectorizer.get_feature_names_out())
    print("🔍 Resume Vector (sample):", tfidf_matrix[0].toarray()[:1])
    print("🔍 JD Vector (sample):", tfidf_matrix[1].toarray()[:1])

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    score = round(float(similarity[0][0]) * 100, 2)

    print(f"✅ TF-IDF Similarity Score: {score}%")
    return score
