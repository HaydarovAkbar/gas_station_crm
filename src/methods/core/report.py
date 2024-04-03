import openpyxl as px
import os
from openpyxl.utils.dataframe import dataframe_to_rows

# from db.models import Organization, PaymentType, FuelType, FuelStorage, FuelColumnPointer, SaleFuel, OrganizationFuelColumns, OrganizationFuelTypes, FuelPrice


def get_report_week_test():
    file_path = os.path.join(os.getcwd(), 'static', 'report.xlsx')
    wb = px.Workbook()
    ws = wb.active
    ws.title = "Weekly Report"
    print(ws.title)
    ws.merge_cells('E6:E7')
    ws['E6'] = 'Tushumlar'
    ws.merge_cells('F6:F7')
    ws['F6'] = 'Chiqimlar'

    # save to new name file
    wb.save("test.xlsx")
    return file_path


def get_report_week(user):
    pass