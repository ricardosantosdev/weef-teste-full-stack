from django.contrib import admin
from .models import Class, Course, Instructor

admin.site.register(Course)
admin.site.register(Class)
admin.site.register(Instructor)
