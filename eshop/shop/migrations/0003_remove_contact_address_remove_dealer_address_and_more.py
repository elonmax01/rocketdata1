# Generated by Django 5.1.2 on 2024-10-08 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_factory_address_factory_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
        migrations.RemoveField(
            model_name='dealer',
            name='address',
        ),
        migrations.RemoveField(
            model_name='distributor',
            name='address',
        ),
        migrations.RemoveField(
            model_name='ie',
            name='address',
        ),
        migrations.RemoveField(
            model_name='retailer',
            name='address',
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.ManyToManyField(blank=True, to='shop.address'),
        ),
        migrations.AddField(
            model_name='dealer',
            name='address',
            field=models.ManyToManyField(blank=True, to='shop.address'),
        ),
        migrations.AddField(
            model_name='distributor',
            name='address',
            field=models.ManyToManyField(blank=True, to='shop.address'),
        ),
        migrations.AddField(
            model_name='ie',
            name='address',
            field=models.ManyToManyField(blank=True, to='shop.address'),
        ),
        migrations.AddField(
            model_name='retailer',
            name='address',
            field=models.ManyToManyField(blank=True, to='shop.address'),
        ),
    ]
