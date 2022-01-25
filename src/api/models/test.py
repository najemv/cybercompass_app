from .basic import *


class Test(Activity):
    pass


class TestQuestion(Question):
    activity = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")


class TestAnswer(Answer):
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, related_name="answers")