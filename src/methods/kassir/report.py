from fpdf import FPDF


def generate_pdf():
    path = f'static/output.pdf'
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    pdf.cell(200, 10, f"Bugungi hisobot", 0, 1, 'C')
    pdf.output(path)
    return path


generate_pdf()
