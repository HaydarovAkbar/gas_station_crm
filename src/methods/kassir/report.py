from fpdf import FPDF
from django.utils import timezone


def generate_pdf():
    path = f'static/output.pdf'
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=12)
    pdf.cell(200, 10, f"Bugungi hisobot", 0, 1, 'C')
    pdf.cell(200, 200, f"Hisobot yaratilgan vaqt: {timezone.now().strftime('%Y.%m.%d %H:%M')}", 0, 1, 'C')
    pdf.cell(200, 250, f"Hisobot turi: Kunlik", 0, 1, 'C')
    pdf.output(path)
    return path


generate_pdf()