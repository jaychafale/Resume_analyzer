import streamlit as st
from resume_parser import extract_text_from_pdf
from feedback_generator import (
    get_resume_feedback,
    get_recruiter_view,
    rewrite_bullet_point,
    analyze_soft_skills_and_tone,
    estimate_career_progression,
    get_resume_scorecard
)
from pdf_exporter import generate_pdf
from utils import load_gemini_api_key, styled_output_box
from dotenv import load_dotenv
import time

# 🧠 NLP parsers
from nlp_resume_parser import extract_resume_entities
from tfidf_matcher import compute_resume_jd_match  # ✅ NEW

# Load API Key
load_dotenv()
api_key = load_gemini_api_key()

# Page config
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.markdown(
    """
    <style>
        h1, h2, h3 {
            color: #2c3e50;
        }
        .stButton>button {
            background-color: #004080;
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
        }
        .stButton>button:hover {
            background-color: #0059b3;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# UI
st.title("💼 AI Resume Analyzer")
st.markdown("Upload your resume, get actionable feedback, and boost your hiring chances!")
st.markdown("---")

# Upload
resume_file = st.file_uploader("📄 Upload Resume (PDF only)", type=["pdf"])
jd_input = st.text_area("🧾 Paste Job Description (optional)", height=150)

if resume_file:
    resume_text = extract_text_from_pdf(resume_file)

    # Scorecard
    st.subheader("📊 Resume Scorecard (AI-Powered)")
    if st.button("🔎 Analyze Resume Quality"):
        with st.spinner("Scoring resume using AI..."):
            scores = get_resume_scorecard(resume_text, jd_input, api_key)
            for k in ["Structure", "Clarity", "Relevance", "Formatting"]:
                st.text(f"{k}: {scores[k]}/10")
                st.progress(scores[k] / 10)
            st.text(f"Total Score: {scores['Total']}/100")
            st.progress(scores["Total"] / 100)

    with st.expander("👁 Recruiter Eye-View", expanded=False):
        if st.button("Generate Recruiter Insight"):
            with st.spinner("Analyzing resume through recruiter’s eyes..."):
                recruiter_view = get_recruiter_view(resume_text, api_key)
                st.markdown(styled_output_box(recruiter_view), unsafe_allow_html=True)

    with st.expander("✍️ Bullet Point Rewriter", expanded=False):
        bullet = st.text_input("Paste a weak bullet point:")
        if st.button("Rewrite with AI"):
            with st.spinner("Rewriting bullet point..."):
                improved = rewrite_bullet_point(bullet, api_key)
                st.markdown(styled_output_box(improved), unsafe_allow_html=True)

    with st.expander("🧠 Soft Skills & Tone Analyzer", expanded=False):
        if st.button("Analyze Tone & Skills"):
            with st.spinner("Scanning tone and soft skills..."):
                tone_output = analyze_soft_skills_and_tone(resume_text, api_key)
                st.markdown(styled_output_box(tone_output), unsafe_allow_html=True)

    with st.expander("📈 Career Progression Estimator", expanded=False):
        if st.button("Suggest Career Path"):
            with st.spinner("Estimating your next best role..."):
                career_path = estimate_career_progression(resume_text, api_key)
                st.markdown(styled_output_box(career_path), unsafe_allow_html=True)

    with st.expander("📄 Download Resume Enhancement Suggestions (PDF)", expanded=False):
        if st.button("📥 Download PDF Report"):
            with st.spinner("Generating your personalized resume report..."):
                feedback = get_resume_feedback(resume_text, jd_input, api_key)
                pdf_path = generate_pdf(resume_text, feedback)
                time.sleep(1.5)
                st.download_button("⬇️ Download PDF", pdf_path, file_name="Resume_Enhancement_Report.pdf")

    # 🧠 NLP Entity & Skill Extraction via spaCy
    with st.expander("📚 NLP-based Entity & Skill Extraction", expanded=False):
        if st.button("Run NLP Analysis"):
            with st.spinner("Extracting names, degrees, skills, and designations..."):
                try:
                    results = extract_resume_entities(resume_text)
                    for label, items in results.items():
                        if items:
                            st.markdown(f"**{label}:** {', '.join(set(items))}")
                        else:
                            st.markdown(f"**{label}:** _None found_")
                except Exception as e:
                    st.error(f"❌ NLP parsing failed: {e}")

    # ✅ NEW: TF-IDF Resume–JD Matching
    with st.expander("🧮 Resume–JD Match Score (TF-IDF)", expanded=False):
        if st.button("Check TF-IDF Match Score"):
            with st.spinner("Calculating similarity score..."):
                try:
                    score = compute_resume_jd_match(resume_text, jd_input)
                    st.success(f"📈 TF-IDF Similarity Score: {score}%")
                except Exception as e:
                    st.error(f"❌ Failed to compute similarity: {e}")

else:
    st.info("👆 Upload a resume PDF to begin.")
