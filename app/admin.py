from django.contrib import admin

from app.models import Professor, University, Student, Course

admin.site.register(University)
admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Course)