import streamlit as st
from resume_parser import extract_text_from_pdf
from feedback_generator import (
    get_resume_feedback,
    get_recruiter_view,
    rewrite_bullet_point,
    analyze_soft_skills_and_tone,
    estimate_career_progression
)
from pdf_exporter import generate_pdf
from utils import load_gemini_api_key
from dotenv import load_dotenv
import time

# ========== App Setup ==========
load_dotenv()
api_key = load_gemini_api_key()
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.markdown(
    """
    <style>
        .main { background-color: #f8f9fa; }
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
        .stTextInput>div>div>input {
            border: 1px solid #ccc;
            padding: 0.5rem;
            border-radius: 5px;
        }
        .report-style {
            background-color: #ffffff;
            padding: 1rem;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ========== Header ==========
st.title("💼 AI Resume Analyzer")
st.markdown("Upload your resume, get actionable feedback, and boost your hiring chances!")

st.markdown("---")

# ========== Upload Section ==========
resume_file = st.file_uploader("📄 Upload Resume (PDF only)", type=["pdf"])
jd_input = st.text_area("🧾 Paste Job Description (optional)", height=150)

if resume_file:
    resume_text = extract_text_from_pdf(resume_file)

    with st.expander("👁 Recruiter Eye-View", expanded=False):
        if st.button("Generate Recruiter Insight"):
            with st.spinner("Analyzing resume through recruiter’s eyes..."):
                recruiter_view = get_recruiter_view(resume_text, api_key)
                st.markdown(f"<div class='report-style'>{recruiter_view}</div>", unsafe_allow_html=True)

    with st.expander("✍️ Bullet Point Rewriter", expanded=False):
        bullet = st.text_input("Paste a weak bullet point:")
        if st.button("Rewrite with AI"):
            with st.spinner("Rewriting bullet point..."):
                improved = rewrite_bullet_point(bullet, api_key)
                st.markdown(f"<div class='report-style'><b>Improved:</b><br>{improved}</div>", unsafe_allow_html=True)

    with st.expander("🧠 Soft Skills & Tone Analyzer", expanded=False):
        if st.button("Analyze Tone & Skills"):
            with st.spinner("Scanning tone and soft skills..."):
                tone_output = analyze_soft_skills_and_tone(resume_text, api_key)
                st.markdown(f"<div class='report-style'>{tone_output}</div>", unsafe_allow_html=True)

    with st.expander("📈 Career Progression Estimator", expanded=False):
        if st.button("Suggest Career Path"):
            with st.spinner("Estimating your next best role..."):
                career_path = estimate_career_progression(resume_text, api_key)
                st.markdown(f"<div class='report-style'>{career_path}</div>", unsafe_allow_html=True)

    with st.expander("📄 Download Resume Enhancement Suggestions (PDF)", expanded=False):
        if st.button("📥 Download PDF Report"):
            with st.spinner("Generating your personalized resume report..."):
                feedback = get_resume_feedback(resume_text, jd_input, api_key)
                pdf_path = generate_pdf(resume_text, feedback)
                time.sleep(1.5)
                with open(pdf_path, "rb") as f:
                    st.success("Report ready! Click to download below 👇")
                    st.download_button("⬇️ Download PDF", f, file_name="Resume_Enhancement_Report.pdf")

else:
    st.info("👆 Upload a resume PDF to begin.")
