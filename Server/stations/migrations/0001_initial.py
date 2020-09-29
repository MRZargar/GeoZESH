# Generated by Django 3.0.3 on 2020-09-25 18:56

import datetime
import django.core.validators
from django.db import migrations, models
import stations.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Deactivate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to=stations.models.station_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Raspberry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raspberryID', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_name', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(max_length=150)),
                ('station_id', models.CharField(max_length=8, unique=True, validators=[django.core.validators.MinLengthValidator(8)])),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('owner', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 9, 25, 22, 26, 55, 554650))),
                ('status', models.BooleanField(default=False)),
                ('sensor_type', models.CharField(choices=[('type1', 'TYPE1'), ('type2', 'TYPE2')], default='type1', max_length=50)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=20)),
                ('health', models.IntegerField(default=0)),
                ('raspberryID', models.IntegerField()),
                ('health_time', models.DateTimeField(default=datetime.datetime(2020, 9, 25, 22, 26, 55, 554875))),
            ],
        ),
    ]