# Generated by Django 5.0.1 on 2024-02-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_user_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="To'liq ismi"),
        ),
    ]
