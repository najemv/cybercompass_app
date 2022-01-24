from .basic import *

class InteractiveReadingManager(models.Manager):
    def get_queryset(self):
        activities = super().get_queryset()
        for activity in activities:
            activity.reading_parts = ReadingPart.objects.filter(activity=activity.id)
        return activities

class InteractiveReading(Activity):
    parts = []
    objects = InteractiveReadingManager()

class ReadingPartManager(models.Manager):
    def get_queryset(self):
        parts = super().get_queryset()
        for part in parts:
            try:
                part.question = ReadingQuestion.objects.get(part=part.id)
            except:
                pass
        return parts

class ReadingPart(models.Model):
    text = models.CharField(max_length=20000)
    activity = models.ForeignKey(InteractiveReading, on_delete=models.CASCADE)
    question = None
    objects = ReadingPartManager()

class ReadingQuestionManager(models.Manager):
    def get_queryset(self):
        questions = super().get_queryset()
        for question in questions:
            question.answers = ReadingAnswer.objects.filter(question=question.id)
        return questions

class ReadingQuestion(Question):
    part = models.OneToOneField(ReadingPart, on_delete=models.CASCADE)
    objects = ReadingQuestionManager()

class ReadingAnswer(Answer):
    question = models.ForeignKey(ReadingQuestion, on_delete=models.CASCADE)