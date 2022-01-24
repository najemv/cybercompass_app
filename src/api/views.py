from urllib import response
from django.shortcuts import render
from .serializers import *
from .models.interactive_reading import *
from .models.test import *
from .models.tinder_swipe import *
from .models.others import *
from .helper import *
from rest_framework.views import APIView
from rest_framework import generics, mixins, status
from rest_framework.response import Response
# Create your views here.

class ModuleView(APIView):
    def get(self, request, id=None):
        if id is None:
            modules = Module.objects.all()
            serializer = ModuleSerializer(modules, many=True)
            return Response(serializer.data)
        else:
            q = Question.objects.get(id=id)
            q.answers = Answer.objects.filter(question=q.id)
            serializer = QuestionSerializer(q)
            return Response(serializer.data)


class ChallengeView(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


class QuestionView(APIView):
    def get(self, request, id=None):
        if id is None:
            questions = TestQuestion.objects.all()
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data)
        else:
            q = Question.objects.get(id=id)
            q.answers = Answer.objects.filter(question=q.id)
            serializer = QuestionSerializer(q)
            return Response(serializer.data)

    #def post(self, request):
    #    serializer = QuestionSerializer(data=request.data)
#
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def put(self, request, id=None):
    #    return self.update(request, id)
#
    #def delete(self, request, id):
    #    return self.destroy(request, id)