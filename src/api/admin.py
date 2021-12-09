from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Module)
admin.site.register(Challenge)
admin.site.register(Article)
admin.site.register(MultipleChoiceQuestion)
admin.site.register(TinderSwipe)

