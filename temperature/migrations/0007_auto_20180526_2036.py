# Generated by Django 2.0.2 on 2018-05-26 20:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('temperature', '0006_auto_20180526_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='visit_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 26, 20, 36, 38, 287687, tzinfo=utc)),
        ),
    ]
