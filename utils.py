import os

def load_gemini_api_key():
    return os.getenv("AIzaSyBLyDQWmYrnKZnyHbJzs_rYNEhr9Lp4jI0")

def styled_output_box(content: str) -> str:
    return f"""
    <div style="
        background-color: rgba(240, 240, 240, 0.1);
        color: inherit;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 0 4px rgba(0,0,0,0.03);
        line-height: 1.6;
        font-size: 1rem;
        white-space: pre-wrap;
        border-left: 4px solid #004080;
    ">
        {content}
    </div>
    """

