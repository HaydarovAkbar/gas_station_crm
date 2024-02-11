# Generated by Django 5.0.1 on 2024-02-10 12:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0013_alter_fuelcolumnpointer_size_first_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleFuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(verbose_name='Kun')),
                ('size', models.FloatField(verbose_name='Hajmi [litr]')),
                ('price', models.FloatField(verbose_name='Narxi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name="O'zgartirilgan sana")),
                ('fuel_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot.fueltype', verbose_name="Yoqilg'i turi")),
                ('payment_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot.paymenttype', verbose_name="To'lov turi")),
            ],
            options={
                'verbose_name': "Sotilgan yoqilg'i",
                'verbose_name_plural': "Sotilgan yoqilg'i",
                'db_table': 'sale_fuel',
                'indexes': [models.Index(fields=['day', 'fuel_type', 'payment_type'], name='sale_fuel_day_a5ac4b_idx')],
            },
        ),
    ]
