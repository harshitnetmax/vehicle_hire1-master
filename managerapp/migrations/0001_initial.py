# Generated by Django 2.0.6 on 2019-04-05 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleCategories',
            fields=[
                ('vehicle_category_name', models.CharField(default='', max_length=225)),
                ('vehicle_category_price', models.IntegerField(default=0)),
                ('type_isactive', models.BooleanField(default=True)),
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleCompany',
            fields=[
                ('company_name', models.CharField(default='', max_length=225)),
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('company_isactive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='VehiclesDetails',
            fields=[
                ('vehicle_ref_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_name', models.CharField(default='', max_length=225)),
                ('vehicle_description', models.CharField(default='', max_length=225)),
                ('vehicle_image', models.CharField(default='', max_length=225)),
                ('vehicle_isactive', models.BooleanField(default=True)),
                ('u_email', models.CharField(default='', max_length=225)),
                ('vehicle_isavailable', models.BooleanField(default=True)),
                ('vehicle_price', models.IntegerField(default=0)),
                ('company_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='managerapp.VehicleCompany')),
                ('vehicle_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='managerapp.VehicleCategories')),
            ],
        ),
    ]
