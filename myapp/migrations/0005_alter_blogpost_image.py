# Generated by Django 5.0.2 on 2024-03-08 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_category_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
