# Generated by Django 4.0 on 2022-01-23 19:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_remove_answer_question_remove_readingpart_reading_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='is_true',
            new_name='is_correct',
        ),
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.question'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='valid_from',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 23, 20, 22, 14, 755760)),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 23, 20, 22, 14, 755760)),
        ),
    ]