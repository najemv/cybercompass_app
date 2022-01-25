from api.models.others import Module, Profile, Progress
from .models import *



def get_user_profile(username: str):
    print(username)
    user_progress = Profile.objects.get(user__username=username)
    print(user_progress)
    return user_progress
