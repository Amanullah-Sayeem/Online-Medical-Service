# Generated by Django 3.0.5 on 2020-08-10 17:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20200810_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 8, 10, 17, 50, 42, 553620, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(),
        ),
    ]
