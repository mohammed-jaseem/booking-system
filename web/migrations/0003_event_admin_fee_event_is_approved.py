# Generated by Django 5.1.4 on 2024-12-17 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_event_description_alter_event_enquiry_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='admin_fee',
            field=models.DecimalField(decimal_places=2, default=50, max_digits=10, verbose_name='Admin Fee'),
        ),
        migrations.AddField(
            model_name='event',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
