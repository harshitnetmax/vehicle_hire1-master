# Generated by Django 2.0.6 on 2019-05-07 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_app', '0025_booking_details_total_fine'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_details',
            name='earnings',
            field=models.BigIntegerField(default=0),
        ),
    ]
