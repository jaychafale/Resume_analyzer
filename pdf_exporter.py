from fpdf import FPDF

def generate_pdf(resume_text, feedback):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, "Resume Enhancement Report", align='C')
    pdf.ln(10)
    pdf.multi_cell(0, 10, "=== Resume Text (Preview) ===")
    pdf.multi_cell(0, 10, resume_text[:1500])  # trim

    pdf.ln(5)
    pdf.multi_cell(0, 10, "=== AI Suggestions ===")
    pdf.multi_cell(0, 10, feedback[:1500])  # trim

    output_path = "Resume_Enhancement_Report.pdf"
    pdf.output(output_path)
    return output_path
