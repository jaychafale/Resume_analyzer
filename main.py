import streamlit as st
from resume_parser import extract_text_from_pdf
from feedback_generator import get_resume_feedback
from utils import load_gemini_api_key
import os
from dotenv import load_dotenv

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

load_dotenv()
api_key = load_gemini_api_key()

st.title("💼 AI-Powered Resume Analyzer")
st.markdown("Upload your **resume** and an optional **job description**. Let Gemini evaluate and improve it!")

resume_file = st.file_uploader("📄 Upload Resume (PDF only)", type=["pdf"])
jd_input = st.text_area("🧾 Paste Job Description (optional)", height=200)

if st.button("🔍 Analyze Resume"):
    if not resume_file:
        st.warning("Please upload a resume.")
    else:
        with st.spinner("Analyzing with Gemini..."):
            resume_text = extract_text_from_pdf(resume_file)
            feedback = get_resume_feedback(resume_text, jd_input, api_key)
            st.subheader("📊 AI Feedback")
            st.markdown(feedback)
