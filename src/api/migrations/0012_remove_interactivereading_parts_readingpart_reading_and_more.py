# Generated by Django 4.0 on 2022-01-23 20:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_challenge_valid_from_alter_challenge_valid_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interactivereading',
            name='parts',
        ),
        migrations.AddField(
            model_name='readingpart',
            name='reading',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.interactivereading'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='challenge',
            name='valid_from',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 23, 21, 52, 45, 673789)),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 23, 21, 52, 45, 674789)),
        ),
        migrations.AlterField(
            model_name='readingpart',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='api.question'),
        ),
    ]