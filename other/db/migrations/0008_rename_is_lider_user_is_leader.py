# Generated by Django 4.2.10 on 2024-03-28 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0007_organizationfueltypes_organizationfuelcolumns'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_lider',
            new_name='is_leader',
        ),
    ]
