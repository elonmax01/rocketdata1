# Generated by Django 5.1.2 on 2024-10-09 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='date_of_admission',
        ),
    ]
