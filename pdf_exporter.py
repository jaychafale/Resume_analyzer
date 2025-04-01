from fpdf import FPDF
import os

def generate_pdf(resume_text, feedback):
    pdf = FPDF()
    pdf.add_page()

    # Use a Unicode-compatible font
    font_path = os.path.join(os.path.dirname(__file__), "DejaVuSans.ttf")
    if not os.path.exists(font_path):
        raise FileNotFoundError("DejaVuSans.ttf font file is required for Unicode PDF export.")

    pdf.add_font("DejaVu", "", font_path, uni=True)
    pdf.set_font("DejaVu", size=12)

    pdf.multi_cell(0, 10, "Resume Enhancement Report", align='C')
    pdf.ln(10)

    pdf.set_font("DejaVu", size=10)
    pdf.multi_cell(0, 10, "=== Extracted Resume Text ===")
    pdf.multi_cell(0, 10, resume_text[:2000])  # Limit size

    pdf.ln(5)
    pdf.multi_cell(0, 10, "=== Gemini Feedback ===")
    pdf.multi_cell(0, 10, feedback)

    output_path = "Resume_Enhancement_Report.pdf"
    pdf.output(output_path)
    return output_path
