# Generated by Django 4.2.11 on 2024-03-14 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_appointment_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.TimeField(default=datetime.datetime(2024, 3, 14, 15, 29, 1, 287318)),
        ),
    ]
