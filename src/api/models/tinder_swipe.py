from .basic import *


class TinderSwipe(Activity):
    image = models.ImageField(upload_to ='images/')


class TSQuestion(Question):
    activity = models.OneToOneField(TinderSwipe, on_delete=models.CASCADE, related_name="question")


class TSAnswer(Answer):
    question = models.ForeignKey(TSQuestion, on_delete=models.CASCADE, related_name="answers")
