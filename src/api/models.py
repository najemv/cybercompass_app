from datetime import datetime
from statistics import mode
from django.db import models

# Question

class Answer(models.Model):
    text = models.CharField(max_length=1024)
    is_true = models.BooleanField()
    explanation = models.CharField(max_length=1024)

class Question(models.Model):
    question = models.CharField(max_length=256)
    answers = models.ManyToManyField(Answer)


# Activity

class Activity(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    max_score = models.IntegerField()

    class Meta:
        abstract = True

class Test(Activity):
    questions = models.ManyToManyField(Question)


class TinderSwipe(Activity):
    image = models.ImageField(upload_to ='images/')
    question = models.OneToOneField(Question, on_delete=models.CASCADE)


class ReadingPart(models.Model):
    text = models.CharField(max_length=20000)
    question = models.OneToOneField(Question, on_delete=models.CASCADE)

class InteractiveReading(Activity):
    parts = models.ManyToManyField(ReadingPart)



# Basic structure

class Challenge(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    valid_from = models.DateTimeField(default=datetime.now())
    valid_to = models.DateTimeField(default=datetime.now())
    points = models.IntegerField(default=0)

    tests = models.ManyToManyField(Test)
    tinder_swipes = models.ManyToManyField(TinderSwipe)
    interactive_readings = models.ManyToManyField(InteractiveReading)


class Module(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    tests = models.ManyToManyField(Test)
    tinder_swipes = models.ManyToManyField(TinderSwipe)
    interactive_readings = models.ManyToManyField(InteractiveReading)