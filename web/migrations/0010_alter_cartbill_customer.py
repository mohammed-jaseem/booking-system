# Generated by Django 5.1.4 on 2024-12-19 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_remove_event_tax_charge_event_customer_cartbill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartbill',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.customer'),
        ),
    ]