# Generated by Django 5.1.6 on 2025-03-10 14:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0008_delete_carbooking'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('pick_up_location', models.CharField(default='Unknown Location', max_length=200)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('num_of_days', models.IntegerField()),
                ('drop_off_location', models.CharField(default='Unknown Location', max_length=200)),
                ('drop_off_date', models.DateField()),
                ('drop_off_time', models.TimeField()),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
