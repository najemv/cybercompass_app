# Generated by Django 4.0 on 2022-01-24 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_challenge_valid_from_alter_challenge_valid_to_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='valid_from',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 14, 59, 24, 878050)),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 24, 14, 59, 24, 878050)),
        ),
    ]
