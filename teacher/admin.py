from django.contrib import admin
from .models import Message, Grade, AddClass, AddClassAsClassTeacher


# Register your models here.
admin.site.register(Grade)
admin.site.register(Message)
admin.site.register(AddClass)
admin.site.register(AddClassAsClassTeacher)
