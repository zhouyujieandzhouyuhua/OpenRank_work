from django.contrib import admin

# Register your models here.
from .models import TestPaper,Question,Record
admin.site.register(TestPaper)
admin.site.register(Question)
admin.site.register(Record)
