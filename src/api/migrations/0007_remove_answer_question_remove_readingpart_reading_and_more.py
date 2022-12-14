# Generated by Django 4.0 on 2022-01-22 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_answer_interactivereading_question_readingpart_test_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='readingpart',
            name='reading',
        ),
        migrations.AddField(
            model_name='interactivereading',
            name='parts',
            field=models.ManyToManyField(to='api.ReadingPart'),
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(to='api.Answer'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='valid_from',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 22, 19, 34, 5, 168372)),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 22, 19, 34, 5, 168372)),
        ),
    ]
