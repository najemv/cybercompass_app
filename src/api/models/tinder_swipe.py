from .basic import *

class TinderSwipeManager(models.Manager):
    def get_queryset(self):
        activities = super().get_queryset()
        for activity in activities:
            try:
                activity.question = TSQuestion.objects.get(activity=activity.id)
            except:
                pass
        return activities

class TinderSwipe(Activity):
    image = models.ImageField(upload_to ='images/')
    question = None
    objects = TinderSwipeManager()

class TSQuestionManager(models.Manager):
    def get_queryset(self):
        questions = super().get_queryset()
        for question in questions:
            question.answers = TSAnswer.objects.filter(question=question.id)
        return questions

class TSQuestion(Question):
    activity = models.OneToOneField(TinderSwipe, on_delete=models.CASCADE)
    objects = TSQuestionManager()


class TSAnswer(Answer):
    question = models.ForeignKey(TSQuestion, on_delete=models.CASCADE)
