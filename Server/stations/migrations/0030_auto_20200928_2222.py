# Generated by Django 3.0.3 on 2020-09-28 18:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0029_auto_20200928_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setup',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 22, 22, 39, 331003)),
        ),
        migrations.AlterField(
            model_name='setup',
            name='health_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 28, 22, 22, 39, 331281)),
        ),
    ]