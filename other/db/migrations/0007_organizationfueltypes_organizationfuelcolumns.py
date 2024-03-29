# Generated by Django 4.2.10 on 2024-03-27 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0006_delete_usertypes_remove_fuel_fuel_day_fb774c_idx_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationFuelTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('fuel_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.fueltype', verbose_name="Yoqilg'i turi")),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.organization', verbose_name='Tashkilot')),
            ],
            options={
                'verbose_name': "Tashkilotlar yoqilg'i turi",
                'verbose_name_plural': "Tashkilotlar yoqilg'i turlari",
                'db_table': 'organization_fuel_types',
            },
        ),
        migrations.CreateModel(
            name='OrganizationFuelColumns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('fuel_column', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.fuelcolumn', verbose_name="Yoqilg'i ustuni")),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.organization', verbose_name='Tashkilot')),
            ],
            options={
                'verbose_name': "Tashkilotlar yoqilg'i ustuni",
                'verbose_name_plural': "Tashkilotlar yoqilg'i ustunlari",
                'db_table': 'organization_fuel_columns',
            },
        ),
    ]
