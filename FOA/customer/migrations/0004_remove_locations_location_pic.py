# Generated by Django 5.0.3 on 2024-03-20 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_locations_location_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locations',
            name='location_pic',
        ),
    ]
