from django.contrib import admin
from .models import Course, Student, Teacher, Payment


admin.site.register([Course, Student, Teacher, Payment])
