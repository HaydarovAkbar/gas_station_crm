# Generated by Django 5.0.1 on 2024-02-09 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0011_user_phone_user_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuelstorage',
            name='input_price',
            field=models.FloatField(default=1, verbose_name='Kirim narxi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fuelstorage',
            name='output_price',
            field=models.FloatField(default=1, verbose_name='Chiqim narxi'),
            preserve_default=False,
        ),
    ]
