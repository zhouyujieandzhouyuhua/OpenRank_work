from django.contrib import admin

# Register your models here.
from .models import  Teacher,UserTable,Student
admin.site.register(Teacher)
admin.site.register(UserTable)
admin.site.register(Student)
