import os

def load_gemini_api_key():
    return os.getenv("AIzaSyBLyDQWmYrnKZnyHbJzs_rYNEhr9Lp4jI0")

def styled_output_box(content: str) -> str:
    return f"""
    <div style="
        background-color: #f8f9fa;
        color: #1e1e1e;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.05);
        line-height: 1.6;
        font-size: 1rem;
        white-space: pre-wrap;
    ">
        {content}
    </div>
    """
