# Generated by Django 5.1.2 on 2024-10-08 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factory',
            name='address',
        ),
        migrations.AddField(
            model_name='factory',
            name='address',
            field=models.ManyToManyField(blank=True, to='shop.address'),
        ),
    ]
