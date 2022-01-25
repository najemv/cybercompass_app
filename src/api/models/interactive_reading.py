from .basic import *


class InteractiveReading(Activity):
    pass


class ReadingPart(models.Model):
    text = models.CharField(max_length=20000)
    activity = models.ForeignKey(InteractiveReading, on_delete=models.CASCADE, related_name="parts")


class ReadingQuestion(Question):
    part = models.OneToOneField(ReadingPart, on_delete=models.CASCADE, related_name="question")


class ReadingAnswer(Answer):
    question = models.ForeignKey(ReadingQuestion, on_delete=models.CASCADE, related_name="answers")