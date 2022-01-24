from .basic import *

class TestManager(models.Manager):
    def get_queryset(self):
        activities = super().get_queryset()
        for activity in activities:
            activity.questions = TestQuestion.objects.filter(activity=activity.id)
        return activities

class Test(Activity):
    questions = []
    objects = TestManager()

class TestQuestionManager(models.Manager):
    def get_queryset(self):
        questions = super().get_queryset()
        for question in questions:
            question.answers = TestAnswer.objects.filter(question=question.id)
        return questions

class TestQuestion(Question):
    activity = models.ForeignKey(Test, on_delete=models.CASCADE)
    objects = TestQuestionManager()

class TestAnswer(Answer):
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)