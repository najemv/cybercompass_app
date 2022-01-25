from rest_framework import serializers
from django.contrib.auth.models import User


class AnswerSerializer(serializers.Serializer):
    answer = serializers.CharField()
    is_correct = serializers.BooleanField()
    explanation = serializers.CharField()


class QuestionSerializer(serializers.Serializer):
    question = serializers.CharField()
    answers = AnswerSerializer(many=True)


class ActivitySerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    max_score = serializers.IntegerField()


class TinderSwipeSerializer(ActivitySerializer):
    image = serializers.ImageField()
    question = QuestionSerializer()


class TestSerializer(ActivitySerializer):
    questions = QuestionSerializer(many=True)


class ReadingPartSerializer(serializers.Serializer):
    text = serializers.CharField()
    question = QuestionSerializer()


class InteractiveReadingSerializer(ActivitySerializer):
    parts = ReadingPartSerializer(many=True)


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()


class ChallengeSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    valid_from = serializers.DateField()
    valid_to = serializers.DateField()
    points = serializers.DateField()


    tests = TestSerializer(many=True)
    tinder_swipes = TinderSwipeSerializer(many=True)
    interactive_readings = InteractiveReadingSerializer(many=True)


class ModuleSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    articles = ArticleSerializer(many=True)
    challenges = ChallengeSerializer(many=True)
    tests = TestSerializer(many=True)
    tinder_swipes = TinderSwipeSerializer(many=True)
    interactive_readings = InteractiveReadingSerializer(many=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]


class ProgressSerializer(serializers.Serializer):
    current_score = serializers.IntegerField()
    available = serializers.BooleanField
    module = ModuleSerializer()


class ProfileSerializer(serializers.Serializer):
    user = UserSerializer()
    total_score = serializers.IntegerField()
    current_progress = ProgressSerializer(source="progress_set", many=True)
