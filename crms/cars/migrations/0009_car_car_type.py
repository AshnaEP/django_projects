# Generated by Django 5.1.6 on 2025-03-12 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_delete_carbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_type',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], default='Manual', max_length=10),
        ),
    ]
