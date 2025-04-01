import google.generativeai as genai

def get_resume_feedback(resume_text, job_description, api_key):
    genai.configure(api_key=api_key)

    # Correctly create the model object
    model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

    # Prompt template
    prompt = f"""
    You are a professional resume analyst.

    Resume:
    \"\"\"
    {resume_text}
    \"\"\"

    Job Description:
    \"\"\"
    {job_description or "N/A"}
    \"\"\"

    Tasks:
    1. Assess the resume's structure, clarity, and readability.
    2. Highlight strengths and weaknesses.
    3. Suggest improvements (skills, formatting, bullet point enhancements, etc).
    4. If job description is present, suggest how to tailor the resume.

    Give a concise and actionable response.
    """

    # Generate feedback using Gemini
    response = model.generate_content(prompt)
    return response.text
