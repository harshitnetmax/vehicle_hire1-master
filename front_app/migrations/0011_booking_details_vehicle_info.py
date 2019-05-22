# Generated by Django 2.0.6 on 2019-04-25 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managerapp', '0006_auto_20190416_2251'),
        ('front_app', '0010_booking_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_details',
            name='vehicle_info',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='managerapp.VehiclesDetails'),
        ),
    ]
