from django.contrib import admin
from .models import CourseModel

class CourseModelEdit(admin.ModelAdmin):
    list_display = ["name","language","price",]
# Register your models here.
admin.site.register(CourseModel,CourseModelEdit)
