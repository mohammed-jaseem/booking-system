# Generated by Django 5.1.4 on 2024-12-17 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_event_admin_fee_event_is_approved'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='admin_fee',
        ),
        migrations.RemoveField(
            model_name='event',
            name='is_approved',
        ),
    ]