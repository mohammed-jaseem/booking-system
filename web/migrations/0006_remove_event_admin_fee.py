# Generated by Django 5.1.4 on 2024-12-19 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_event_admin_fee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='admin_fee',
        ),
    ]
