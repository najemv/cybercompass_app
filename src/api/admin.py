from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)

admin.site.register(InteractiveReading)
admin.site.register(TinderSwipe)
admin.site.register(Test)
admin.site.register(ReadingPart)

admin.site.register(Module)
admin.site.register(Challenge)




