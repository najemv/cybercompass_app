from django.contrib import admin
from .models.interactive_reading import *
from .models.test import *
from .models.tinder_swipe import *
from .models.others import *

# Register your models here.


admin.site.register(InteractiveReading)
admin.site.register(ReadingPart)
admin.site.register(ReadingQuestion)
admin.site.register(ReadingAnswer)

admin.site.register(TinderSwipe)
admin.site.register(TSQuestion)
admin.site.register(TSAnswer)

admin.site.register(Test)
admin.site.register(TestQuestion)
admin.site.register(TestAnswer)

admin.site.register(Module)
admin.site.register(Challenge)
admin.site.register(Profile)




