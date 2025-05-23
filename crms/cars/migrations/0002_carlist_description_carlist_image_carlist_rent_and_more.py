# Generated by Django 5.1.6 on 2025-02-21 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlist',
            name='description',
            field=models.TextField(default='cars'),
        ),
        migrations.AddField(
            model_name='carlist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='carlist',
            name='rent',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carlist',
            name='color',
            field=models.CharField(max_length=30),
        ),
    ]
