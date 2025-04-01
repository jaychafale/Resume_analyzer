import google.generativeai as genai

def configure_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

def get_resume_feedback(resume_text, job_description, api_key):
    model = configure_gemini(api_key)
    prompt = f"""
You are a professional resume reviewer.
Analyze the resume and suggest improvements in structure, formatting, and alignment with job description.

Resume:
\"\"\"
{resume_text}
\"\"\"

Job Description:
\"\"\"
{job_description or "N/A"}
\"\"\"
"""
    return model.generate_content(prompt).text

def get_recruiter_view(resume_text, api_key):
    model = configure_gemini(api_key)
    prompt = f"""
Pretend you are a recruiter scanning the resume for 30 seconds.
Give your first impression, strengths, and concerns.

Resume:
\"\"\"
{resume_text}
\"\"\"
"""
    return model.generate_content(prompt).text

def rewrite_bullet_point(bullet_point, api_key):
    model = configure_gemini(api_key)
    prompt = f"""
Rewrite this resume bullet point to be more professional, concise, and impactful:

\"{bullet_point}\"
"""
    return model.generate_content(prompt).text

def analyze_soft_skills_and_tone(resume_text, api_key):
    model = configure_gemini(api_key)
    prompt = f"""
Analyze the tone and soft skills in the following resume.
Classify tone (e.g., Aggressive, Passive, Balanced) and list soft skills demonstrated.

Resume:
\"\"\"
{resume_text}
\"\"\"
"""
    return model.generate_content(prompt).text

def estimate_career_progression(resume_text, api_key):
    model = configure_gemini(api_key)
    prompt = f"""
Based on the resume, suggest possible next career roles and a 1–3 year development roadmap.

Resume:
\"\"\"
{resume_text}
\"\"\"
"""
    return model.generate_content(prompt).text
