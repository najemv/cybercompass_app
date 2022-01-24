from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    max_score = models.IntegerField()

    class Meta:
        abstract = True

class Question(models.Model):
    question = models.CharField(max_length=256)
    answers = []

    class Meta:
        abstract = True

class Answer(models.Model):
    answer = models.CharField(max_length=1024)
    is_correct = models.BooleanField()
    explanation = models.CharField(max_length=1024)

    class Meta:
        abstract = True