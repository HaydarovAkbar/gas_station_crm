# Generated by Django 5.0.1 on 2024-02-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0012_fuelstorage_input_price_fuelstorage_output_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fuelcolumnpointer',
            name='size_first',
            field=models.FloatField(blank=True, null=True, verbose_name='Hajmi kun boshida [litr]'),
        ),
        migrations.AlterField(
            model_name='fuelcolumnpointer',
            name='size_last',
            field=models.FloatField(blank=True, null=True, verbose_name='Hajmi kun oxirida [litr]'),
        ),
    ]
