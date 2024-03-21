# Generated by Django 5.0.3 on 2024-03-21 04:24

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_rides_book_id_alter_rides_journey_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rides',
            name='book_id',
            field=models.UUIDField(default=uuid.UUID('d79e4c1c-2615-42aa-aa46-94a2e206a91b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rides',
            name='journey_end_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Journey End Time'),
        ),
        migrations.AlterField(
            model_name='rides',
            name='journey_start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Journey Start Time'),
        ),
    ]
