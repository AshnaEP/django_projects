# Generated by Django 5.1.6 on 2025-03-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_rename_carlist_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
