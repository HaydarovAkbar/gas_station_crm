import openpyxl as px
import os
from openpyxl.utils.dataframe import dataframe_to_rows
from django.utils import timezone

from db.models import Organization, PaymentType, FuelType, FuelStorage, FuelColumnPointer, SaleFuel, \
    OrganizationFuelColumns, OrganizationFuelTypes, FuelPrice


def get_report_week_test():
    # file_path = os.path.join(os.getcwd(), 'static', 'report.xlsx')
    file_path = os.path.join('report.xlsx')
    wb = px.load_workbook(file_path)
    print(wb.sheetnames)
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


def get_report_1(user, week=False, fuel_type=None):
    file_path = os.path.join(os.getcwd(), 'static', 'report.xlsx')
    wb = px.load_workbook(file_path)
    ws = wb.active
    ws.title = "Haftalik hisobot"
    organ_fuel_columns = OrganizationFuelColumns.objects.filter(organization=user.organization).count()
    i = 6
    date_range = [timezone.now().date() - timezone.timedelta(days=7 if week else 30), timezone.now().date()]
    for date in date_range:
        ws.merge_cells(f'B{i}:B{i + organ_fuel_columns - 1}')
        ws[f'B{i}'] = f"{date.day} - {date.strftime('%B')[0:5]}"
        ws.merge_cells(f'C{i}:C{i + organ_fuel_columns - 1}')
        ws[f'C{i}'] = date.strftime('%Y')
    wb.save("test.xlsx")
    return file_path


if __name__ == '__main__':
    get_report_week_test()
