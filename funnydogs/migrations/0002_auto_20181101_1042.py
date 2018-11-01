# Generated by Django 2.1.2 on 2018-11-01 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funnydogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='timeStamp',
            new_name='time_stamp',
        ),
        migrations.AddField(
            model_name='author',
            name='time_stamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]