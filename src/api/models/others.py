from .basic import *
from django.db import models
from datetime import datetime
from .tinder_swipe import TinderSwipe
from .interactive_reading import InteractiveReading
from .test import Test
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ModuleManager(models.Manager):
    def get_queryset(self):
        modules = super().get_queryset()
        for module in modules:
            module.challenges = Challenge.objects.filter(module=module.id)
        return modules

class Module(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    tests = models.ManyToManyField(Test)
    tinder_swipes = models.ManyToManyField(TinderSwipe)
    interactive_readings = models.ManyToManyField(InteractiveReading)
    challenges = []
    objects = ModuleManager()

class Challenge(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    valid_from = models.DateTimeField(default=datetime.now())
    valid_to = models.DateTimeField(default=datetime.now())
    points = models.IntegerField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    
    tests = models.ManyToManyField(Test)
    tinder_swipes = models.ManyToManyField(TinderSwipe)
    interactive_readings = models.ManyToManyField(InteractiveReading)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_score = models.IntegerField()
    modules_progress = models.ManyToManyField(Module, through="Progress")

class Progress(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    current_score = models.IntegerField()
    available = models.BooleanField()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()