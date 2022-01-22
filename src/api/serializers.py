from django.db.models import fields
from rest_framework import serializers
from .models import *

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'




class TinderSwipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TinderSwipe
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class InteractiveReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractiveReading
        fields = '__all__'

class ReadingPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadingPart
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'