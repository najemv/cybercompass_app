# Generated by Django 4.0 on 2022-01-22 15:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_challenge_valid_from_alter_challenge_valid_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('is_true', models.BooleanField()),
                ('explanation', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='InteractiveReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('max_score', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ReadingPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=20000)),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.question')),
                ('reading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.interactivereading')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('max_score', models.IntegerField()),
                ('questions', models.ManyToManyField(to='api.Question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TinderSwipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=1024)),
                ('max_score', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.question')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='challenge',
            name='activities',
        ),
        migrations.RemoveField(
            model_name='module',
            name='activities',
        ),
        migrations.RemoveField(
            model_name='module',
            name='articles',
        ),
        migrations.AlterField(
            model_name='challenge',
            name='description',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='valid_from',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 22, 16, 37, 37, 942189)),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='valid_to',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 22, 16, 37, 37, 942189)),
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.question'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='interactive_readings',
            field=models.ManyToManyField(to='api.InteractiveReading'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='tests',
            field=models.ManyToManyField(to='api.Test'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='tinder_swipes',
            field=models.ManyToManyField(to='api.TinderSwipe'),
        ),
        migrations.AddField(
            model_name='module',
            name='interactive_readings',
            field=models.ManyToManyField(to='api.InteractiveReading'),
        ),
        migrations.AddField(
            model_name='module',
            name='tests',
            field=models.ManyToManyField(to='api.Test'),
        ),
        migrations.AddField(
            model_name='module',
            name='tinder_swipes',
            field=models.ManyToManyField(to='api.TinderSwipe'),
        ),
    ]
