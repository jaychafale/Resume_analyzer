from fpdf import FPDF

def generate_pdf(resume_text, feedback):
    pdf = FPDF()
    pdf.add_page()

    # Use built-in font
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, "Resume Enhancement Report", align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10, "=== Extracted Resume Text ===")
    pdf.multi_cell(0, 10, resume_text[:1500])  # preview

    pdf.ln(5)
    pdf.multi_cell(0, 10, "=== Gemini Feedback ===")
    pdf.multi_cell(0, 10, feedback[:2000])  # preview

    output_path = "Resume_Enhancement_Report.pdf"
    pdf.output(output_path)
    return output_path
