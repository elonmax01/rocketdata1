# Generated by Django 5.1.2 on 2024-10-09 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_contact_address_remove_dealer_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dealer',
            name='distributor',
        ),
        migrations.RemoveField(
            model_name='dealer',
            name='factory',
        ),
        migrations.RemoveField(
            model_name='distributor',
            name='factory',
        ),
        migrations.RemoveField(
            model_name='ie',
            name='dealer',
        ),
        migrations.RemoveField(
            model_name='ie',
            name='distributor',
        ),
        migrations.RemoveField(
            model_name='ie',
            name='factory',
        ),
        migrations.RemoveField(
            model_name='ie',
            name='retailer',
        ),
        migrations.RemoveField(
            model_name='retailer',
            name='dealer',
        ),
        migrations.RemoveField(
            model_name='retailer',
            name='distributor',
        ),
        migrations.RemoveField(
            model_name='retailer',
            name='factory',
        ),
        migrations.AddField(
            model_name='dealer',
            name='level',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='dealer',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.dealer'),
        ),
        migrations.AddField(
            model_name='distributor',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='distributor',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.distributor'),
        ),
        migrations.AddField(
            model_name='factory',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ie',
            name='level',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='ie',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.ie'),
        ),
        migrations.AddField(
            model_name='retailer',
            name='level',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='retailer',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.retailer'),
        ),
    ]
