from rest_framework import serializers

class AnswerSerializer(serializers.Serializer):
    answer = serializers.CharField()
    is_correct = serializers.BooleanField()
    explanation = serializers.CharField()

class QuestionSerializer(serializers.Serializer):
    question = serializers.CharField()
    answers = serializers.ListField(child=AnswerSerializer())

    #def create(self, validated_data):
    #    answers = validated_data.pop('answers')
    #    question = Question.objects.create(**validated_data)
    #    question.answers = []
    #    #Profile.objects.create(user=user, **profile_data)
    #    for answer in answers:
    #        a = Answer.objects.create(question=question, **answer)
    #        question.answers.append(a)
    #    return question


class ActivitySerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    max_score = serializers.IntegerField()


class TinderSwipeSerializer(ActivitySerializer):
    image = serializers.ImageField()
    question = QuestionSerializer()

class TestSerializer(ActivitySerializer):
    questions = serializers.ListField(child=QuestionSerializer())

class ReadingPartSerializer(serializers.Serializer):
    text = serializers.CharField()
    question = QuestionSerializer()

class InteractiveReadingSerializer(ActivitySerializer):
    parts = serializers.ListField(child=ReadingPartSerializer())



class ModuleSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()

    tests = TestSerializer(many=True)
    tinder_swipes = TinderSwipeSerializer(many=True)
    interactive_readings = InteractiveReadingSerializer(many=True)

class ChallengeSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    valid_from = serializers.DateField()
    valid_to = serializers.DateField()
    points = serializers.DateField()

    tests = TestSerializer(many=True)
    tinder_swipes = TinderSwipeSerializer(many=True)
    interactive_readings = InteractiveReadingSerializer(many=True)