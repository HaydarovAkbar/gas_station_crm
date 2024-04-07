from fpdf import FPDF


def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    pdf.cell(200, 10, 'Hello World!', 0, 1, 'C')
    pdf.cell(100, 200, 'Powered by FPDF.', 1, 1, 'C')
    pdf.output('tuto1.pdf')


generate_pdf()
