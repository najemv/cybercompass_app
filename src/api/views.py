from urllib import response
from django.shortcuts import render
from .serializers import *
from .models.interactive_reading import *
from .models.test import *
from .models.tinder_swipe import *
from .models.others import *
from .helper import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ProfileView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Shows profile for the user who requests it.
        """
        profile = get_user_profile(request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class ModuleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        """
        Shows list of all modules in the system (or just one).
        """
        modules = Module.objects.all()
        serializer = ModuleSerializer(modules, many=True)
        return Response(serializer.data)


class ChallengeView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        """
        Shows list of all challenges in the system.
        """
        challenges = Challenge.objects.all()
        serializer = ChallengeSerializer(challenges, many=True)
        return Response(serializer.data)


class ArticleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        """
        Shows list of all articles in the system.
        """
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ActivityView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        """
        Shows list of all activities in the system.
        """
        tests = Test.objects.all()
        tss = TinderSwipe.objects.all()
        readings = InteractiveReading.objects.all()
        tests_ser = TestSerializer(tests, many=True)
        tss_ser = TinderSwipeSerializer(tss, many=True)
        readings_ser = InteractiveReadingSerializer(readings, many=True)
        return Response({
            "tests" : tests_ser.data,
            "tinder_swipes" : tss_ser.data,
            "interactive_readings" : readings_ser.data
        })

