# Generated by Django 5.0.3 on 2024-03-19 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations',
            name='location_pic',
            field=models.ImageField(default='locations/default_location.jpg', upload_to='locations/'),
        ),
    ]