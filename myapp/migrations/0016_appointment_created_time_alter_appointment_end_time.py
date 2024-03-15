# Generated by Django 4.2.11 on 2024-03-14 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_appointment_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='end_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]