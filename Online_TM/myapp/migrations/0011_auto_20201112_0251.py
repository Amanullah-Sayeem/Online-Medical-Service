# Generated by Django 3.0.8 on 2020-11-11 20:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20201112_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 11, 11, 20, 51, 33, 356303, tzinfo=utc)),
        ),
    ]