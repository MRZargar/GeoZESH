# Generated by Django 3.0.3 on 2020-09-28 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0014_auto_20200928_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setup',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 16, 35, 20, 48687)),
        ),
        migrations.AlterField(
            model_name='setup',
            name='health_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 16, 35, 20, 48865)),
        ),
    ]