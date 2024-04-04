import openpyxl as px
import os
from openpyxl.utils.dataframe import dataframe_to_rows
from django.utils import timezone
from django.db.models import Sum

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
    residual = FuelStorage.objects.filter(organization=user.organization, fuel_type=fuel_type, is_over=False,
                                          created_at__lt=timezone.now()).aggregate(total=Sum('residual'))['total']
    i = 6
    date_range = [timezone.now().date() - timezone.timedelta(days=7 if week else 30), timezone.now().date()]
    for date in date_range:
        ws.merge_cells(f'B{i}:B{i + organ_fuel_columns - 1}')
        ws[f'B{i}'] = f"{date.day} - {date.strftime('%B')[0:5]}"
        ws.merge_cells(f'C{i}:C{i + organ_fuel_columns - 1}')
        ws[f'C{i}'] = residual
        ws.merge_cells(f'D{i}:D{i + organ_fuel_columns - 1}')
        ws[f'D{i}'] = FuelStorage.objects.filter(organization=user.organization, fuel_type=fuel_type,
                                                 created_at__lt=date).last().remainder
        pointer = FuelColumnPointer.objects.filter(organization=user.organization, fuel_type=fuel_type,
                                                   created_at__lt=date)
        item = 0
        for point in pointer:
            ws[f'E{i + item}'] = point.size_last
            ws[f'F{i + item}'] = point.size_first
        sale_fuel = SaleFuel.objects.filter(organization=user.organization, fuel_type=fuel_type, created_at__lt=date)
        fuel_price_last = FuelPrice.objects.filter(organization=user.organization, fuel_type=fuel_type, created_at__lt=date).last()
        ws.merge_cells(f'G{i}:G{i + organ_fuel_columns - 1}')
        ws[f'G{i}'] = sale_fuel.aggregate(total=Sum('cash_size'))['total'] + sale_fuel.aggregate(
            total=Sum('card_size'))['total']
        ws.merge_cells(f'H{i}:H{i + organ_fuel_columns - 1}')
        ws[f'H{i}'] = sale_fuel.first().price - sale_fuel.first().benefit
        ws.merge_cells(f'I{i}:I{i + organ_fuel_columns - 1}')
        ws[f'I{i}'] = fuel_price_last.price
        ws.merge_cells(f'J{i}:J{i + organ_fuel_columns - 1}')
        ws[f'J{i}'] = sale_fuel.first().price
        ws.merge_cells(f'K{i}:K{i + organ_fuel_columns - 1}')
        ws[f'K{i}'] = sale_fuel.first().card_size
        ws.merge_cells(f'L{i}:L{i + organ_fuel_columns - 1}')
        ws[f'L{i}'] = sale_fuel.first().card_size * fuel_price_last.price
        ws.merge_cells(f'M{i}:M{i + organ_fuel_columns - 1}')
        ws[f'M{i}'] = sale_fuel.first().cash_size
        ws.merge_cells(f'N{i}:N{i + organ_fuel_columns - 1}')
        ws[f'N{i}'] = sale_fuel.first().cash_size * fuel_price_last.price
        ws.merge_cells(f'O{i}:O{i + organ_fuel_columns - 1}')
        ws[f'O{i}'] = sale_fuel.first().benefit
        ws.merge_cells(f'P{i}:P{i + organ_fuel_columns - 1}')
        ws[f'P{i}'] = 6878





    wb.save("test.xlsx")
    return file_path


if __name__ == '__main__':
    get_report_week_test()
