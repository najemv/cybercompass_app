from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    content = models.CharField(max_length=30000)


class MultipleChoiceQuestion(models.Model):
    question = models.CharField(max_length=256)
    corrent_answer_no = models.IntegerField()
    answer1 = models.CharField(max_length=256)
    explanation1 = models.CharField(max_length=256)
    answer2 = models.CharField(max_length=256)
    explanation2 = models.CharField(max_length=256)
    answer3 = models.CharField(max_length=256)
    explanation3 = models.CharField(max_length=256)
    answer4 = models.CharField(max_length=256)
    explanation4 = models.CharField(max_length=256)


class TinderSwipe(models.Model):
    # TODO put images here
    #image = models.ImageField()
    correct_answer = models.BooleanField()
    explanation = models.CharField(max_length=256)


class Challenge(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    questions = models.ManyToManyField(MultipleChoiceQuestion)


class Module(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    articles = models.ManyToManyField(Article)
