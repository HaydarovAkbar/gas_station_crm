from fpdf import FPDF
from django.utils import timezone
from db.models import Organization, FuelType, FuelStorage, FuelStorageHistory, SaleFuel, FuelPrice, \
    OrganizationFuelColumns, OrganizationFuelTypes, FuelColumnPointer


def generate_pdf():
    path = f'static/output.pdf'
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', size=10)
    pdf.set_text_color(63, 51, 255)
    pdf.text(138, 9, txt="Chop etilgan sanasi: {}".format(timezone.now().strftime('%d.%m.%Y %H:%M')))
    pdf.set_font("Arial", size=12, style='B')
    pdf.set_text_color(0, 0, 0)
    pdf.line(10, 12, 198, 12)
    pdf.set_font("Arial", size=20, style='B')
    pdf.text(92, 25, txt="Hisobot")
    pdf.set_font("Arial", size=12, style='I')
    pdf.text(10, 40, txt="Bugungi umumiy savdo summasi:   {}".format(1000000))
    # pdf.text(138, 9, txt="b: {}".format(timezone.now().strftime('%d.%m.%Y %H:%M')))
    # pdf.set_font("Arial", size=12, style='B')
    # pdf.set_text_color(0, 0, 0)
    # pdf.line(10, 12, 198, 12)
    # pdf.text(104, 20, txt="b")
    # pdf.text(10, 25, txt="b:   {}".format(1000000))

    pdf.output(path)
    return path


generate_pdf()
